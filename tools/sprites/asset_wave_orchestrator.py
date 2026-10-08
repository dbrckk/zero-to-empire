#!/usr/bin/env python3
"""Autonomous producer for the 235-asset Zero -> Empire target.

This script only schedules production/evidence work. It never marks semantic
approval or strict DONE automatically.
"""
from __future__ import annotations

import json
import os
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
CHARACTER_GENERATION_EPOCH = "identity-lock-v1.17-articulated-border-fix"
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
        if str(x.get("review_reason") or "").startswith("Character production paused until"):
            x["review_reason"] = "Identity-locked character generation is available; automatic candidate production resumed."
        eligible.append(aid)
    return eligible


def prioritize_controlled_character_targets(ids: list[str]) -> None:
    """Keep exact dispatched assets first so Kaggle --count matches dispatch state."""
    selected = set(ids)
    if not selected:
        return
    controlled = load_json(CHARACTER_QUEUE, {}) or {}
    targets = controlled.get("targets", [])
    targets.sort(key=lambda item: 0 if str(item.get("id", "")).upper() in selected else 1)
    save_json(CHARACTER_QUEUE, controlled)


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
    targets = []
    selected_groups = []
    for group in groups:
        group_assets = sorted(
            [
                x for x in queue["assets"]
                if x["group"] == group
                and x["strict_status"] != "DONE"
                and str(x.get("pipeline_status", "")).upper() not in CHARACTER_PRODUCED_STATUSES
            ],
            key=lambda x: action_order.get(x["id"].split("-")[-1], 99),
        )
        group_targets = []
        for x in group_assets:
            if len(targets) >= CHARACTER_BATCH_SIZE:
                break
            if not character_retry_available(x):
                x["pipeline_status"] = "BLOCKED_AUTOMATION_LIMIT"
                continue
            x["pipeline_status"] = "PENDING_KAGGLE"
            row = {"id": x["id"], "status": "PENDING_KAGGLE"}
            targets.append(row)
            group_targets.append(row)
        if group_targets:
            selected_groups.append(group)
        if len(targets) >= CHARACTER_BATCH_SIZE:
            break
    if not targets:
        return {"group": "+".join(groups), "ids": [], "count": 0}
    save_json(CHARACTER_QUEUE, {
        "mode": "kaggle-character-burst-v1.12",
        "reason": (
            "Autofactory 235: high-throughput identity-locked character production; "
            "each role keeps its own identity anchor and semantic promotion remains manual."
        ),
        "groups": selected_groups,
        "targets": targets,
    })
    dispatched = mark_dispatch(queue, [x["id"] for x in targets], "kaggle-character-sheet")
    prioritize_controlled_character_targets(dispatched)
    return {"group": "+".join(selected_groups), "ids": dispatched, "count": len(dispatched)}


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
    if KAGGLE_BUSY:
        return
    master = by_id(queue)
    controlled = load_json(CHARACTER_QUEUE, {}) or {}
    for item in controlled.get("targets", []):
        aid = str(item.get("id", "")).upper()
        asset = master.get(aid)
        if not asset or asset["strict_status"] == "DONE":
            continue
        if str(asset.get("pipeline_status", "")).upper() != "DISPATCHED":
            continue
        if not character_retry_available(asset):
            asset["pipeline_status"] = "BLOCKED_AUTOMATION_LIMIT"
            if asset.get("generation_epoch") == CHARACTER_GENERATION_EPOCH:
                asset["last_error"] = (
                    f"Exhausted {CHARACTER_EPOCH_ATTEMPT_LIMIT} attempts in "
                    f"{CHARACTER_GENERATION_EPOCH}; semantic review or a new generation epoch is required."
                )


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
    character_pending = pending_ids_from_controlled(CHARACTER_QUEUE, queue)
    if character_pending:
        if KAGGLE_BUSY:
            return {"action": "WAIT_KAGGLE_BUSY", "group": "controlled-character", "stats": s}
        ids = mark_dispatch(queue, character_pending[:CHARACTER_BATCH_SIZE], "kaggle-character-sheet")
        if ids:
            prioritize_controlled_character_targets(ids)
            return {"action": "DISPATCH_KAGGLE_CHARACTER", "group": "controlled-character", "ids": ids, "count": len(ids), "stats": s}
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
