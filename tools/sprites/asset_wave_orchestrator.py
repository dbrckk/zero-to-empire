#!/usr/bin/env python3
"""Autonomous producer for the 235-asset Zero -> Empire target.

This script only schedules production/evidence work. It never marks semantic
approval or strict DONE automatically.
"""
from __future__ import annotations

import json
import os
from datetime import datetime,timezone
from pathlib import Path
from typing import Any

from asset_queue_utils import (
    BUILDING_PRIORITY,
    BUILDING_QUEUE,
    CHARACTER_PRIORITY,
    CHARACTER_QUEUE,
    MASTER,
    MAX_ATTEMPTS,
    STATE,
    ensure_master,
    load_json,
    save_json,
    stats,
    sync_controlled_queues,
    write_summary,
)

TRIGGER_WORKFLOW = os.getenv("AUTOF_TRIGGER_WORKFLOW", "")
TRIGGER_CONCLUSION = os.getenv("AUTOF_TRIGGER_CONCLUSION", "")
TRIGGER_RUN_ID = os.getenv("AUTOF_TRIGGER_RUN_ID", "")
TRIGGER_DISPATCH_TOKEN = os.getenv("AUTOF_TRIGGER_DISPATCH_TOKEN", "")
CURRENT_DISPATCH_TOKEN = os.getenv("GITHUB_RUN_ID", "")
KAGGLE_BUSY = os.getenv("AUTOF_KAGGLE_BUSY", "0") == "1"
FX_BUSY = os.getenv("AUTOF_FX_BUSY", "0") == "1"
CHARACTER_GENERATION_EPOCH = "identity-lock-v1.18-carry-identity-lock"
CHARACTER_EPOCH_ATTEMPT_LIMIT = 3
CHARACTER_BATCH_SIZE = 12
INFRA_FAILURE_LIMIT = 3

# A character in one of these states already has a produced candidate/evidence.
# It must not be regenerated merely because strict semantic approval is pending.
CHARACTER_PRODUCED_STATUSES = {
    "AWAITING_REVIEW",
    "CANDIDATE",
    "TECHNICAL_PASS",
    "VALIDATED",
    "APPROVED",
    "DONE",
}


def by_id(queue: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {x["id"]: x for x in queue["assets"]}


def mirror_character_outcomes_from_controlled(queue: dict[str, Any], active: list[dict[str, Any]]) -> None:
    controlled = load_json(CHARACTER_QUEUE, {}) or {}
    outcomes = {
        str(item.get("id", "")).upper(): str(item.get("status", "")).upper()
        for item in controlled.get("targets", [])
    }
    reasons = {
        str(item.get("id", "")).upper(): str(item.get("review_reason") or "")
        for item in controlled.get("targets", [])
    }
    for asset in active:
        if asset.get("last_generator") != "kaggle-character-sheet":
            continue
        status = outcomes.get(asset["id"])
        if status == "AWAITING_REVIEW":
            asset["pipeline_status"] = "AWAITING_REVIEW"
            asset["review_reason"] = "Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion."
        elif status in {"REJECTED", "REJECTED_SEMANTIC"}:
            asset["pipeline_status"] = "REJECTED_SEMANTIC"
            asset["review_reason"] = reasons.get(asset["id"]) or "Kaggle generator rejected the candidate before semantic review."
            asset["last_error"] = asset["review_reason"]
        elif status == "BLOCKED_INFRA_LIMIT":
            asset["pipeline_status"] = "BLOCKED_INFRA_LIMIT"


def update_from_trigger(queue: dict[str, Any]) -> None:
    if TRIGGER_WORKFLOW == "Kaggle Mass Sprite Factory" and TRIGGER_CONCLUSION:
        active = [
            x for x in queue["assets"]
            if x["pipeline_status"] == "DISPATCHED"
            and x.get("last_generator") in {"kaggle-building-family", "kaggle-character-sheet"}
            and (
                (TRIGGER_DISPATCH_TOKEN and str(x.get("dispatch_token") or "") == TRIGGER_DISPATCH_TOKEN)
                or (not TRIGGER_DISPATCH_TOKEN and not x.get("dispatch_token"))
            )
        ]
        if TRIGGER_CONCLUSION == "success":
            mirror_character_outcomes_from_controlled(queue, active)
            for x in active:
                x["last_run_id"] = int(TRIGGER_RUN_ID) if TRIGGER_RUN_ID else x.get("last_run_id")
                if x["pipeline_status"] != "REJECTED_SEMANTIC":
                    x["last_error"] = None
        else:
            for x in active:
                x["pipeline_status"] = "PENDING_KAGGLE"
                x["last_run_id"] = int(TRIGGER_RUN_ID) if TRIGGER_RUN_ID else x.get("last_run_id")
                x["infra_failures"] = int(x.get("infra_failures") or 0) + 1
                if x.get("last_generator") == "kaggle-character-sheet":
                    x["attempts"] = max(0, int(x.get("attempts") or 0) - 1)
                    if x.get("generation_epoch") == CHARACTER_GENERATION_EPOCH:
                        x["epoch_attempts"] = max(0, int(x.get("epoch_attempts") or 0) - 1)
                if int(x.get("infra_failures") or 0) >= INFRA_FAILURE_LIMIT:
                    x["pipeline_status"] = "BLOCKED_INFRA_LIMIT"
                    x["last_error"] = (
                        f"Kaggle producer failed {x['infra_failures']} times; infrastructure recovery required."
                    )
                else:
                    x["last_error"] = (
                        f"Kaggle producer: {TRIGGER_CONCLUSION}; infrastructure retry "
                        f"{x['infra_failures']}/{INFRA_FAILURE_LIMIT} scheduled"
                    )
            for path in (BUILDING_QUEUE, CHARACTER_QUEUE):
                controlled = load_json(path, {}) or {}
                changed = False
                for item in controlled.get("targets", []):
                    aid = str(item.get("id", "")).upper()
                    if any(x["id"] == aid for x in active):
                        asset = next((x for x in active if x["id"] == aid), None)
                        if asset and str(asset.get("pipeline_status", "")).upper() == "BLOCKED_INFRA_LIMIT":
                            item["status"] = "BLOCKED_INFRA_LIMIT"
                        else:
                            item["status"] = "PENDING_KAGGLE"
                        item["autofactory_retry_after_run"] = int(TRIGGER_RUN_ID) if TRIGGER_RUN_ID else None
                        changed = True
                if changed:
                    save_json(path, controlled)

    if TRIGGER_WORKFLOW == "FX Historical Review Evidence":
        target = [
            x for x in queue["assets"]
            if x["lane"] == "fx-runtime-reconciliation"
            and x["pipeline_status"] in {"EVIDENCE_DISPATCHED", "PENDING_EVIDENCE"}
        ]
        if TRIGGER_CONCLUSION == "success":
            for x in target:
                x["pipeline_status"] = "AWAITING_REVIEW"
                x["last_generator"] = "fx-historical-review-evidence"
                x["last_run_id"] = int(TRIGGER_RUN_ID) if TRIGGER_RUN_ID else x.get("last_run_id")
                x["last_error"] = None
        elif TRIGGER_CONCLUSION:
            for x in target:
                x["pipeline_status"] = "PENDING_EVIDENCE"
                x["last_error"] = f"FX evidence workflow: {TRIGGER_CONCLUSION}"


def active_pending(path: Path) -> list[dict[str, Any]]:
    q = load_json(path, {}) or {}
    return [x for x in q.get("targets", []) if str(x.get("status", "")).upper() == "PENDING_KAGGLE"]


def character_retry_available(asset: dict[str, Any]) -> bool:
    status = str(asset.get("pipeline_status", "")).upper()
    if status in CHARACTER_PRODUCED_STATUSES:
        return False
    current_epoch = asset.get("generation_epoch") == CHARACTER_GENERATION_EPOCH
    current_error = str(asset.get("last_error") or "")
    if int(asset.get("infra_failures") or 0) >= INFRA_FAILURE_LIMIT and current_error.startswith("Kaggle producer"):
        return False
    if current_epoch:
        return int(asset.get("epoch_attempts") or 0) < CHARACTER_EPOCH_ATTEMPT_LIMIT
    # A new generation epoch is an explicit algorithm/prompt change. Historical
    # semantic attempts must not consume the new epoch's retry budget.
    if status in {"REJECT", "REJECTED", "REJECTED_SEMANTIC", "PENDING", "PENDING_KAGGLE", "PAUSED", "BLOCKED", "BLOCKED_AUTOMATION_LIMIT"}:
        return True
    total_attempts = int(asset.get("attempts") or 0)
    if total_attempts < MAX_ATTEMPTS:
        return True
    legacy_failure = "Legacy APK character sheet rejected" in str(asset.get("last_error") or "")
    infra_retry = str(asset.get("last_error") or "").startswith("Kaggle producer")
    stride_retry = "WALK lacks clear alternating stride" in str(asset.get("review_reason") or "")
    return legacy_failure or infra_retry or stride_retry


def mark_dispatch(queue: dict[str, Any], ids: list[str], generator: str) -> list[str]:
    assets = by_id(queue)
    eligible: list[str] = []
    for aid in ids:
        x = assets.get(aid)
        if not x or x["strict_status"] == "DONE":
            continue
        attempts = int(x.get("attempts") or 0)
        if generator == "kaggle-character-sheet":
            if not character_retry_available(x):
                x["pipeline_status"] = "BLOCKED_AUTOMATION_LIMIT"
                x["last_error"] = x.get("last_error") or f"Reached {MAX_ATTEMPTS} automatic attempts"
                continue
            if x.get("generation_epoch") != CHARACTER_GENERATION_EPOCH:
                x["generation_epoch"] = CHARACTER_GENERATION_EPOCH
                x["epoch_attempts"] = 0
            if not str(x.get("last_error") or "").startswith("Kaggle producer"):
                x["infra_failures"] = 0
            x["epoch_attempts"] = int(x.get("epoch_attempts") or 0) + 1
        elif attempts >= MAX_ATTEMPTS:
            x["pipeline_status"] = "BLOCKED_AUTOMATION_LIMIT"
            x["last_error"] = f"Reached {MAX_ATTEMPTS} automatic attempts"
            continue
        x["attempts"] = attempts + 1
        x["pipeline_status"] = "DISPATCHED"
        x["last_generator"] = generator
        x["dispatch_token"] = CURRENT_DISPATCH_TOKEN or None
        # Once a fresh dispatch is accepted, historical retry/recovery errors
        # are no longer the current state. Keep evidence in the rejection
        # ledger, but do not surface stale errors as if the active wave failed.
        x["last_error"] = None
        x["review_reason"] = (
            f"Fresh {generator} dispatch {CURRENT_DISPATCH_TOKEN or 'manual'} is active; "
            "semantic review remains required after candidate collection."
        )
        eligible.append(aid)
    return eligible


def prioritize_controlled_character_targets(ids: list[str]) -> int:
    """Put dispatched actions first and include one IDLE identity anchor per role.

    Strict-DONE IDLE sheets are allowed as context-only regeneration targets:
    they do not consume strict progress or become dispatched in the master
    queue, but producing them in the same Kaggle run gives semantic review a
    complete six-action family and lets promotion replace a legacy IDLE sheet
    with bytes from the exact same identity generation epoch.
    """
    ordered_ids = list(dict.fromkeys(str(aid).upper() for aid in ids if aid))
    selected = set(ordered_ids)
    if not selected:
        return 0

    controlled = load_json(CHARACTER_QUEUE, {}) or {}
    targets = controlled.setdefault("targets", [])
    by_target = {
        str(item.get("id", "")).upper(): item
        for item in targets
        if item.get("id")
    }

    groups: list[str] = []
    for aid in ordered_ids:
        parts = aid.split("-")
        if len(parts) >= 3 and parts[0] == "CHR":
            group = "-".join(parts[:2])
            if group not in groups:
                groups.append(group)

    context_ids: list[str] = []
    for group in groups:
        idle = f"{group}-IDLE"
        if idle in selected:
            continue
        item = by_target.get(idle)
        if item is None:
            item = {
                "id": idle,
                "status": "PENDING_KAGGLE",
                "autofactory_context_only": True,
            }
            targets.append(item)
            by_target[idle] = item
        else:
            item["status"] = "PENDING_KAGGLE"
            item["autofactory_context_only"] = True
        context_ids.append(idle)

    for aid in selected:
        item = by_target.get(aid)
        if item is not None:
            item.pop("autofactory_context_only", None)

    priority: list[str] = []
    for group in groups:
        idle = f"{group}-IDLE"
        if idle in selected or idle in context_ids:
            priority.append(idle)
        priority.extend(aid for aid in ordered_ids if aid.startswith(group + "-") and aid != idle)
    rank = {aid: i for i, aid in enumerate(priority)}
    targets.sort(key=lambda item: rank.get(str(item.get("id", "")).upper(), len(rank)))
    save_json(CHARACTER_QUEUE, controlled)
    return len(selected) + len(context_ids)


def building_family_ids(group: str) -> list[str]:
    return [f"{group}-T{tier}" for tier in range(7)]


def prepare_building_group(queue: dict[str, Any], group: str) -> dict[str, Any]:
    assets = by_id(queue)
    unresolved = [aid for aid in building_family_ids(group) if aid in assets and assets[aid]["strict_status"] != "DONE"]
    if not unresolved:
        raise RuntimeError(f"No unresolved assets in building group {group}")
    targets = [{"id": aid, "status": "PENDING_KAGGLE", "autofactory_context_only": aid not in unresolved} for aid in building_family_ids(group)]
    save_json(BUILDING_QUEUE, {"mode": "kaggle-candidate-only", "family": group, "reason": f"Autofactory 235: generate coherent {group} family candidate set; strict promotion remains manual.", "targets": targets})
    dispatched = mark_dispatch(queue, unresolved, "kaggle-building-family")
    return {"group": group, "ids": dispatched, "count": 7}


def prepare_character_burst(queue: dict[str, Any], groups: list[str]) -> dict[str, Any]:
    action_order = {"IDLE": 0, "WALK": 1, "WORK": 2, "CARRY": 3, "REPAIR": 4, "CELEB": 5}
    targets: list[dict[str, Any]] = []
    selected_groups: list[str] = []
    producer_slots = 0
    assets = by_id(queue)

    for group in groups:
        group_assets = sorted(
            [
                x for x in queue["assets"]
                if x["group"] == group
                and x["strict_status"] != "DONE"
                and str(x.get("pipeline_status", "")).upper() not in CHARACTER_PRODUCED_STATUSES
                and character_retry_available(x)
            ],
            key=lambda x: action_order.get(x["id"].split("-")[-1], 99),
        )
        if not group_assets:
            continue

        idle_id = f"{group}-IDLE"
        idle_is_selected = any(x["id"] == idle_id for x in group_assets)
        needs_idle_context = (
            not idle_is_selected
            and idle_id in assets
            and assets[idle_id]["strict_status"] == "DONE"
        )
        group_cost = len(group_assets) + (1 if needs_idle_context else 0)

        # Keep role families together whenever possible. Splitting a six-action
        # identity family across unrelated GPU runs weakens the semantic review
        # evidence and can produce different faces/clothing for one role.
        if producer_slots and producer_slots + group_cost > CHARACTER_BATCH_SIZE:
            continue

        available = CHARACTER_BATCH_SIZE - producer_slots - (1 if needs_idle_context else 0)
        if available <= 0:
            continue
        chosen = group_assets[:available]
        if not chosen:
            continue

        # Keep the exact semantic rejection reason in the next producer
        # overlay. Replacing the controlled queue without this evidence made
        # queue_rejection_hint() forget why a previous ENG frame failed.
        group_targets = [
            {
                "id": x["id"],
                "status": "PENDING_KAGGLE",
                **(
                    {"review_reason": str(x["review_reason"])}
                    if x.get("review_reason") and str(x.get("pipeline_status", "")).upper()
                    in {"REJECTED", "REJECTED_SEMANTIC", "REJECT"}
                    else {}
                ),
            }
            for x in chosen
        ]
        targets.extend(group_targets)
        selected_groups.append(group)
        producer_slots += len(chosen) + (1 if needs_idle_context else 0)

        if producer_slots >= CHARACTER_BATCH_SIZE:
            break

    if not targets:
        return {"group": "+".join(groups), "ids": [], "count": 0}

    save_json(CHARACTER_QUEUE, {
        "mode": "kaggle-character-burst-v1.18-strict-completion",
        "reason": (
            "Autofactory 235: high-throughput identity-locked character production. "
            "Each role is kept in one producer wave when capacity allows; a strict-DONE "
            "IDLE sheet may be regenerated as context-only identity evidence so review "
            "and promotion can replace a legacy anchor with the same generated family."
        ),
        "groups": selected_groups,
        "targets": targets,
    })
    dispatched = mark_dispatch(queue, [x["id"] for x in targets], "kaggle-character-sheet")
    producer_count = prioritize_controlled_character_targets(dispatched)
    return {"group": "+".join(selected_groups), "ids": dispatched, "count": producer_count}

def next_group(queue: dict[str, Any], lane: str, priority: list[str]) -> str | None:
    groups = {
        x["group"]
        for x in queue["assets"]
        if x["lane"] == lane
        and x["strict_status"] != "DONE"
        and x["pipeline_status"] in {"PENDING", "PENDING_KAGGLE", "PAUSED", "BLOCKED", "REJECT", "REJECTED", "REJECTED_SEMANTIC", "BLOCKED_AUTOMATION_LIMIT"}
        and (
            character_retry_available(x)
            if lane == "kaggle-character-sheet"
            else int(x.get("attempts") or 0) < MAX_ATTEMPTS
        )
    }
    for g in priority:
        if g in groups:
            return g
    return sorted(groups)[0] if groups else None


def close_exhausted_character_dispatches(queue: dict[str, Any]) -> None:
    master = by_id(queue)
    controlled = load_json(CHARACTER_QUEUE, {}) or {}
    controlled_status = {
        str(item.get("id", "")).upper(): str(item.get("status", "")).upper()
        for item in controlled.get("targets", [])
    }

    # KAGGLE_BUSY is repository-wide, but only one async character wave owns
    # the durable active token. A newer wave can supersede an older one via
    # workflow concurrency; do not let the newer ENG wave keep stale OP/LOG
    # dispatches locked merely because *some* Kaggle work is still active.
    async_state = load_json(Path("art/production/kaggle-async-state.json"), {}) or {}
    active_async_token = (
        str(async_state.get("dispatch_token") or "")
        if str(async_state.get("status", "")).upper() == "ACTIVE"
        else ""
    )
    for item in controlled.get("targets", []):
        aid = str(item.get("id", "")).upper()
        asset = master.get(aid)
        if not asset or asset["strict_status"] == "DONE":
            continue
        if str(asset.get("pipeline_status", "")).upper() != "DISPATCHED":
            continue
        if KAGGLE_BUSY:
            asset_token = str(asset.get("dispatch_token") or "")
            # Preserve only dispatches owned by the currently active async wave.
            # If no active token is known, keep the conservative old behaviour.
            if not active_async_token or asset_token == active_async_token:
                continue

        # A cancelled/superseded async producer can leave the master ledger in
        # DISPATCHED even though no Kaggle run remains active. The controlled
        # queue staying PENDING_KAGGLE is the durable evidence that no candidate
        # was collected. Recover that orphaned dispatch so the next autofactory
        # pass can retry it instead of deadlocking strict completion forever.
        if controlled_status.get(aid) == "PENDING_KAGGLE":
            asset["pipeline_status"] = "PENDING_KAGGLE"
            asset["attempts"] = max(0, int(asset.get("attempts") or 0) - 1)
            if asset.get("generation_epoch") == CHARACTER_GENERATION_EPOCH:
                asset["epoch_attempts"] = max(0, int(asset.get("epoch_attempts") or 0) - 1)
            asset["dispatch_token"] = None
            asset["last_error"] = "Recovered orphaned Kaggle dispatch; no active async wave or collected candidate exists."
            continue

        if not character_retry_available(asset):
            asset["pipeline_status"] = "BLOCKED_AUTOMATION_LIMIT"
            if asset.get("generation_epoch") == CHARACTER_GENERATION_EPOCH:
                asset["last_error"] = (
                    f"Exhausted {CHARACTER_EPOCH_ATTEMPT_LIMIT} attempts in "
                    f"{CHARACTER_GENERATION_EPOCH}; semantic review or a new generation epoch is required."
                )


def active_pollinations_repair() -> list[str]:
    """Honor a time-bounded independent repair lane; never replace its queue.

    The provider is allowed to fail/retry without Autofactory dispatching the
    same character to Kaggle or wiping its preserved source evidence.
    """
    controlled=load_json(CHARACTER_QUEUE,{}) or {}
    if controlled.get('mode')!='pollinations-controlled-repair':
        return []
    end=controlled.get('reservation_expires_utc')
    if not isinstance(end,str):
        return []
    try:
        expires=datetime.fromisoformat(end.replace('Z','+00:00'))
        if expires.tzinfo is None or expires<=datetime.now(timezone.utc):
            return []
    except ValueError:
        return []
    blocked={'PENDING','PENDING_POLLINATIONS','BLOCKED','PROVIDER_ERROR',
             'CANDIDATE','AWAITING_REVIEW'}
    return [str(x.get('id','')).upper() for x in controlled.get('targets',[])
            if str(x.get('status','')).upper() in blocked
            and str(x.get('id','')).upper().startswith('CHR-')]


def pending_ids_from_controlled(path: Path, queue: dict[str, Any]) -> list[str]:
    ids = [str(x.get("id", "")).upper() for x in active_pending(path)]
    master = by_id(queue)
    return [
        aid
        for aid in ids
        if aid in master
        and master[aid]["strict_status"] != "DONE"
        and str(master[aid].get("pipeline_status", "")).upper() not in (CHARACTER_PRODUCED_STATUSES | {"DISPATCHED"})
        and (
            character_retry_available(master[aid])
            if path == CHARACTER_QUEUE
            else int(master[aid].get("attempts") or 0) < MAX_ATTEMPTS
        )
    ]


def make_decision(queue: dict[str, Any]) -> dict[str, Any]:
    close_exhausted_character_dispatches(queue)
    s = stats(queue)
    if s["strict_done"] >= queue["stop_when_strict_done"]:
        return {"action": "STOP_STRICT_TARGET_REACHED", "group": None, "stats": s}
    building_pending = pending_ids_from_controlled(BUILDING_QUEUE, queue)
    if building_pending:
        if KAGGLE_BUSY:
            return {"action": "WAIT_KAGGLE_BUSY", "group": "controlled-building", "stats": s}
        ids = mark_dispatch(queue, building_pending, "kaggle-building-family")
        if ids:
            return {"action": "DISPATCH_KAGGLE_BUILDING", "group": "controlled-building", "ids": ids, "count": len(ids), "stats": s}
    group = next_group(queue, "kaggle-building-family", BUILDING_PRIORITY)
    if group:
        if KAGGLE_BUSY:
            return {"action": "WAIT_KAGGLE_BUSY", "group": group, "stats": s}
        prepared = prepare_building_group(queue, group)
        return {"action": "DISPATCH_KAGGLE_BUILDING", **prepared, "stats": s}
    # Defer competing Kaggle character dispatches while the explicitly
    # reserved Pollinations repair lane is active (other lanes remain free).
    repair_ids=active_pollinations_repair()
    if repair_ids:
        return {"action":"WAIT_EXTERNAL_CHARACTER_REPAIR",
                "group":"+".join(repair_ids),"ids":repair_ids,"stats":s}
    character_pending = pending_ids_from_controlled(CHARACTER_QUEUE, queue)
    if character_pending:
        if KAGGLE_BUSY:
            return {"action": "WAIT_KAGGLE_BUSY", "group": "controlled-character", "stats": s}
        ids = mark_dispatch(queue, character_pending[:CHARACTER_BATCH_SIZE], "kaggle-character-sheet")
        if ids:
            producer_count = prioritize_controlled_character_targets(ids)
            return {"action": "DISPATCH_KAGGLE_CHARACTER", "group": "controlled-character", "ids": ids, "count": producer_count, "stats": s}
    first_group = next_group(queue, "kaggle-character-sheet", CHARACTER_PRIORITY)
    if first_group:
        candidate_groups = [
            g for g in CHARACTER_PRIORITY
            if g == first_group or any(
                x["group"] == g
                and x["lane"] == "kaggle-character-sheet"
                and x["strict_status"] != "DONE"
                and str(x.get("pipeline_status", "")).upper() in {
                    "PENDING", "PENDING_KAGGLE", "PAUSED", "BLOCKED",
                    "REJECT", "REJECTED", "REJECTED_SEMANTIC", "BLOCKED_AUTOMATION_LIMIT"
                }
                and character_retry_available(x)
                for x in queue["assets"]
            )
        ]
        ordered = [first_group] + [g for g in candidate_groups if g != first_group]
        burst_groups = ordered[:3]
        if KAGGLE_BUSY:
            return {"action": "WAIT_KAGGLE_BUSY", "group": "+".join(burst_groups), "stats": s}
        prepared = prepare_character_burst(queue, burst_groups)
        if prepared["ids"]:
            return {"action": "DISPATCH_KAGGLE_CHARACTER", **prepared, "stats": s}
    fx = [x for x in queue["assets"] if x["lane"] == "fx-runtime-reconciliation" and x["strict_status"] != "DONE" and x["pipeline_status"] == "PENDING_EVIDENCE" and int(x.get("attempts") or 0) < MAX_ATTEMPTS]
    if fx:
        if FX_BUSY:
            return {"action": "WAIT_FX_BUSY", "group": "FX-HISTORICAL", "stats": s}
        for x in fx:
            x["attempts"] = int(x.get("attempts") or 0) + 1
            x["pipeline_status"] = "EVIDENCE_DISPATCHED"
            x["last_generator"] = "fx-historical-review-evidence"
        return {"action": "DISPATCH_FX_EVIDENCE", "group": "FX-HISTORICAL", "ids": [x["id"] for x in fx], "count": len(fx), "stats": s}
    refreshed = stats(queue)
    if refreshed["production_remaining"] == 0:
        return {"action": "PRODUCTION_235_COMPLETE_REVIEW_BACKLOG", "group": None, "stats": refreshed}
    return {"action": "NO_AUTOMATIC_WORK_AVAILABLE", "group": None, "stats": refreshed}


def main() -> int:
    queue = ensure_master()
    # Apply the producer callback while dispatched assets and their ownership
    # token are still intact. Controlled-queue sync can otherwise change the
    # master status first and make the correlated callback miss its assets.
    update_from_trigger(queue)
    sync_controlled_queues(queue)
    decision = make_decision(queue)
    save_json(MASTER, queue)
    decision["stats_after"] = stats(queue)
    save_json(STATE, decision)
    write_summary(queue, decision)
    print(json.dumps(decision, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
