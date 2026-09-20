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
KAGGLE_BUSY = os.getenv("AUTOF_KAGGLE_BUSY", "0") == "1"
FX_BUSY = os.getenv("AUTOF_FX_BUSY", "0") == "1"


def by_id(queue: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {x["id"]: x for x in queue["assets"]}


def update_from_trigger(queue: dict[str, Any]) -> None:
    # Producer failures must never strand assets in DISPATCHED forever. The
    # workflow_run event is authoritative: put the active Kaggle lane back into
    # the controlled queue so the next autofactory cycle can retry it, subject
    # to the per-asset attempt budget.
    if TRIGGER_WORKFLOW == "Kaggle Mass Sprite Factory" and TRIGGER_CONCLUSION:
        active = [
            x for x in queue["assets"]
            if x["pipeline_status"] == "DISPATCHED"
            and x.get("last_generator") in {"kaggle-building-family", "kaggle-character-sheet"}
        ]
        if TRIGGER_CONCLUSION == "success":
            # The producer writes AWAITING_REVIEW into the controlled queue.
            # sync_controlled_queues() below will import that exact state.
            for x in active:
                x["last_run_id"] = int(TRIGGER_RUN_ID) if TRIGGER_RUN_ID else x.get("last_run_id")
                x["last_error"] = None
        else:
            for x in active:
                x["pipeline_status"] = "PENDING_KAGGLE"
                x["last_run_id"] = int(TRIGGER_RUN_ID) if TRIGGER_RUN_ID else x.get("last_run_id")
                x["last_error"] = f"Kaggle producer: {TRIGGER_CONCLUSION}; autonomous retry scheduled"

            # Keep the specialized controlled queues aligned with master state.
            for path in (BUILDING_QUEUE, CHARACTER_QUEUE):
                controlled = load_json(path, {}) or {}
                changed = False
                for item in controlled.get("targets", []):
                    aid = str(item.get("id", "")).upper()
                    if any(x["id"] == aid for x in active):
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
    return [
        x for x in q.get("targets", [])
        if str(x.get("status", "")).upper() == "PENDING_KAGGLE"
    ]


def mark_dispatch(queue: dict[str, Any], ids: list[str], generator: str) -> list[str]:
    assets = by_id(queue)
    eligible: list[str] = []
    for aid in ids:
        x = assets.get(aid)
        if not x or x["strict_status"] == "DONE":
            continue
        attempts = int(x.get("attempts") or 0)
        if attempts >= MAX_ATTEMPTS:
            x["pipeline_status"] = "BLOCKED_AUTOMATION_LIMIT"
            x["last_error"] = f"Reached {MAX_ATTEMPTS} automatic attempts"
            continue
        x["attempts"] = attempts + 1
        x["pipeline_status"] = "DISPATCHED"
        x["last_generator"] = generator
        eligible.append(aid)
    return eligible


def building_family_ids(group: str) -> list[str]:
    return [f"{group}-T{tier}" for tier in range(7)]


def prepare_building_group(queue: dict[str, Any], group: str) -> dict[str, Any]:
    assets = by_id(queue)
    unresolved = [aid for aid in building_family_ids(group) if aid in assets and assets[aid]["strict_status"] != "DONE"]
    if not unresolved:
        raise RuntimeError(f"No unresolved assets in building group {group}")
    targets = []
    for aid in building_family_ids(group):
        targets.append({
            "id": aid,
            "status": "PENDING_KAGGLE",
            "autofactory_context_only": aid not in unresolved,
        })
    save_json(BUILDING_QUEUE, {
        "mode": "kaggle-candidate-only",
        "family": group,
        "reason": f"Autofactory 235: generate coherent {group} family candidate set; strict promotion remains manual.",
        "targets": targets,
    })
    dispatched = mark_dispatch(queue, unresolved, "kaggle-building-family")
    return {"group": group, "ids": dispatched, "count": 7}


def prepare_character_group(queue: dict[str, Any], group: str) -> dict[str, Any]:
    assets = by_id(queue)
    group_assets = sorted(
        [
            x for x in queue["assets"]
            if x["group"] == group
            and x["strict_status"] != "DONE"
            and x["pipeline_status"] != "PAUSED"
        ],
        key=lambda x: x["id"],
    )
    targets = []
    for x in group_assets:
        if int(x.get("attempts") or 0) >= MAX_ATTEMPTS:
            x["pipeline_status"] = "BLOCKED_AUTOMATION_LIMIT"
            continue
        targets.append({"id": x["id"], "status": "PENDING_KAGGLE"})
    if not targets:
        return {"group": group, "ids": [], "count": 0}
    save_json(CHARACTER_QUEUE, {
        "mode": "kaggle-candidate-only",
        "reason": f"Autofactory 235: identity-locked candidate production for {group}; no automatic semantic promotion.",
        "targets": targets,
    })
    dispatched = mark_dispatch(queue, [x["id"] for x in targets[:2]], "kaggle-character-sheet")
    return {"group": group, "ids": dispatched, "count": min(2, len(targets))}


def next_group(queue: dict[str, Any], lane: str, priority: list[str]) -> str | None:
    groups = {
        x["group"]
        for x in queue["assets"]
        if x["lane"] == lane
        and x["strict_status"] != "DONE"
        and x["pipeline_status"] in {
            "PENDING", "PENDING_KAGGLE", "BLOCKED",
            "REJECT", "REJECTED", "REJECTED_SEMANTIC", "BLOCKED_AUTOMATION_LIMIT"
        }
        and int(x.get("attempts") or 0) < MAX_ATTEMPTS
    }
    for g in priority:
        if g in groups:
            return g
    return sorted(groups)[0] if groups else None


def pending_ids_from_controlled(path: Path, queue: dict[str, Any]) -> list[str]:
    ids = [str(x.get("id", "")).upper() for x in active_pending(path)]
    master = by_id(queue)
    return [
        aid for aid in ids
        if aid in master
        and master[aid]["strict_status"] != "DONE"
        and int(master[aid].get("attempts") or 0) < MAX_ATTEMPTS
    ]


def make_decision(queue: dict[str, Any]) -> dict[str, Any]:
    s = stats(queue)
    if s["strict_done"] >= queue["stop_when_strict_done"]:
        return {"action": "STOP_STRICT_TARGET_REACHED", "group": None, "stats": s}

    # Existing controlled building work always has priority because the Kaggle
    # router itself prioritizes CONTROLLED_BLD over CONTROLLED_CHR.
    building_pending = pending_ids_from_controlled(BUILDING_QUEUE, queue)
    if building_pending:
        if KAGGLE_BUSY:
            return {"action": "WAIT_KAGGLE_BUSY", "group": "controlled-building", "stats": s}
        ids = mark_dispatch(queue, building_pending, "kaggle-building-family")
        if ids:
            return {"action": "DISPATCH_KAGGLE_BUILDING", "group": "controlled-building", "ids": ids, "count": 7, "stats": s}

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
        ids = mark_dispatch(queue, character_pending[:2], "kaggle-character-sheet")
        if ids:
            return {"action": "DISPATCH_KAGGLE_CHARACTER", "group": "controlled-character", "ids": ids, "count": 2, "stats": s}

    group = next_group(queue, "kaggle-character-sheet", CHARACTER_PRIORITY)
    if group:
        if KAGGLE_BUSY:
            return {"action": "WAIT_KAGGLE_BUSY", "group": group, "stats": s}
        prepared = prepare_character_group(queue, group)
        if prepared["ids"]:
            return {"action": "DISPATCH_KAGGLE_CHARACTER", **prepared, "stats": s}

    fx = [
        x for x in queue["assets"]
        if x["lane"] == "fx-runtime-reconciliation"
        and x["strict_status"] != "DONE"
        and x["pipeline_status"] == "PENDING_EVIDENCE"
        and int(x.get("attempts") or 0) < MAX_ATTEMPTS
    ]
    if fx:
        if FX_BUSY:
            return {"action": "WAIT_FX_BUSY", "group": "FX-HISTORICAL", "stats": s}
        for x in fx:
            x["attempts"] = int(x.get("attempts") or 0) + 1
            x["pipeline_status"] = "EVIDENCE_DISPATCHED"
            x["last_generator"] = "fx-historical-review-evidence"
        return {
            "action": "DISPATCH_FX_EVIDENCE",
            "group": "FX-HISTORICAL",
            "ids": [x["id"] for x in fx],
            "count": len(fx),
            "stats": s,
        }

    refreshed = stats(queue)
    if refreshed["production_remaining"] == 0:
        return {
            "action": "PRODUCTION_235_COMPLETE_REVIEW_BACKLOG",
            "group": None,
            "stats": refreshed,
        }

    return {
        "action": "NO_AUTOMATIC_WORK_AVAILABLE",
        "group": None,
        "stats": refreshed,
    }


def main() -> int:
    queue = ensure_master()
    sync_controlled_queues(queue)
    update_from_trigger(queue)
    decision = make_decision(queue)
    save_json(MASTER, queue)
    decision["stats_after"] = stats(queue)
    save_json(STATE, decision)
    write_summary(queue, decision)
    print(json.dumps(decision, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
