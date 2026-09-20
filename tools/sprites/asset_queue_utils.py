#!/usr/bin/env python3
"""Shared state helpers for the 235-asset autonomous production queue.

The master queue deliberately does not trust per-row DONE values from the legacy
manifest while the historical semantic review is open. The strict baseline is defined by the reviewed ledger. BLD-11 and seven
historical FX have now been explicitly reconciled; unresolved work remains in
building families, 24 character sheets and FX-01/02/03.
ONB-00 is outside the 235 production target.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
MASTER = ROOT / "art/production/master-asset-queue.json"
BUILDING_QUEUE = ROOT / "art/production/controlled-building-regen-queue.json"
CHARACTER_QUEUE = ROOT / "art/production/controlled-character-regen-queue.json"
STATE = ROOT / "art/production/autofactory-state.json"
SUMMARY = ROOT / "art/production/autofactory-summary.md"

ROW = re.compile(
    r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$"
)

TARGET_TOTAL = 235
STRICT_BASELINE = 143
MAX_ATTEMPTS = 8

BUILDING_PRIORITY = ["BLD-04", "BLD-07", "BLD-11", "BLD-12", "BLD-13",
                     "BLD-02", "BLD-03", "BLD-05", "BLD-06", "BLD-08",
                     "BLD-09", "BLD-10"]
CHARACTER_PRIORITY = ["CHR-OP", "CHR-TECH", "CHR-LOG", "CHR-ENG"]


def load_json(path: Path, default: Any = None) -> Any:
    if not path.is_file():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def manifest_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if not m:
            continue
        asset_id, name, description, runtime, _status = [x.strip() for x in m.groups()]
        if asset_id == "ONB-00":
            continue
        rows.append({
            "id": asset_id,
            "name": name,
            "description": description,
            "runtime": runtime,
        })
    if len(rows) != TARGET_TOTAL:
        raise RuntimeError(f"Expected {TARGET_TOTAL} production assets excluding ONB-00, got {len(rows)}")
    return rows


def unresolved_ids() -> set[str]:
    ids: set[str] = set()
    ids.update(f"BLD-02-T{tier}" for tier in range(4, 7))
    ids.update(f"BLD-03-T{tier}" for tier in range(0, 2))
    for family in range(4, 14):
        if family == 11:
            continue
        ids.update(f"BLD-{family:02d}-T{tier}" for tier in range(7))
    ids.update(r["id"] for r in manifest_rows() if r["id"].startswith("CHR-"))
    ids.update({"FX-01", "FX-02", "FX-03"})
    if len(ids) != 95:
        raise RuntimeError(f"Strict unresolved set drifted: expected 95, got {len(ids)}")
    return ids


def default_asset(row: dict[str, str], unresolved: set[str]) -> dict[str, Any]:
    asset_id = row["id"]
    needs = asset_id in unresolved
    if not needs:
        lane, group, priority, required, pipeline = "strict-done", asset_id.split("-")[0], 1000, False, "DONE"
    elif asset_id.startswith("BLD-"):
        group = "-".join(asset_id.split("-")[:2])
        lane, priority, required, pipeline = "kaggle-building-family", 10 + int(asset_id.split("-")[1]), True, "PENDING"
    elif asset_id.startswith("CHR-"):
        group = "-".join(asset_id.split("-")[:2])
        role = asset_id.split("-")[1]
        lane, priority, required, pipeline = "kaggle-character-sheet", 200 + max(0, CHARACTER_PRIORITY.index(group)) * 10, True, "PENDING"
    elif asset_id.startswith("FX-"):
        group = "FX-HISTORICAL"
        lane, priority, required, pipeline = "fx-runtime-reconciliation", 400 + int(asset_id.split("-")[1]), False, "PENDING_EVIDENCE"
    else:
        raise RuntimeError(f"Unhandled unresolved asset {asset_id}")
    return {
        **row,
        "strict_status": "NEEDS_REVIEW" if needs else "DONE",
        "pipeline_status": pipeline,
        "lane": lane,
        "group": group,
        "priority": priority,
        "generation_required": required,
        "attempts": 0,
        "last_run_id": None,
        "last_generator": None,
        "last_error": None,
        "review_reason": None,
    }


def ensure_master() -> dict[str, Any]:
    existing = load_json(MASTER, {}) or {}
    old = {x["id"]: x for x in existing.get("assets", []) if isinstance(x, dict) and x.get("id")}
    unresolved = unresolved_ids()
    assets: list[dict[str, Any]] = []
    for row in manifest_rows():
        base = default_asset(row, unresolved)
        prev = old.get(row["id"])
        if prev:
            for key in ("pipeline_status", "attempts", "last_run_id", "last_generator", "last_error", "review_reason"):
                if key in prev:
                    base[key] = prev[key]
        assets.append(base)
    queue = {
        "schema_version": 1,
        "target_total": TARGET_TOTAL,
        "excluded_from_target": ["ONB-00"],
        "strict_done_baseline": STRICT_BASELINE,
        "stop_when_strict_done": TARGET_TOTAL,
        "policy": {
            "automatic_generation": True,
            "automatic_technical_qa": True,
            "automatic_semantic_done": False,
            "automatic_runtime_promotion": False,
            "preserve_manual_review_gate": True,
            "max_attempts_per_asset": MAX_ATTEMPTS,
        },
        "assets": assets,
    }
    save_json(MASTER, queue)
    return queue


def sync_controlled_queues(queue: dict[str, Any]) -> None:
    by_id = {x["id"]: x for x in queue["assets"]}

    bq = load_json(BUILDING_QUEUE, {}) or {}
    for item in bq.get("targets", []):
        aid = str(item.get("id", "")).upper()
        asset = by_id.get(aid)
        if not asset or asset["strict_status"] == "DONE":
            continue
        status = str(item.get("status", "")).upper()
        if status:
            asset["pipeline_status"] = status
        if item.get("kaggle_run_id"):
            asset["last_run_id"] = int(item["kaggle_run_id"])
            asset["last_generator"] = "kaggle-building-family"
        if item.get("review_reason"):
            asset["review_reason"] = item["review_reason"]

    cq = load_json(CHARACTER_QUEUE, {}) or {}
    for item in cq.get("targets", []):
        aid = str(item.get("id", "")).upper()
        asset = by_id.get(aid)
        if not asset or asset["strict_status"] == "DONE":
            continue
        status = str(item.get("status", "")).upper()
        if status:
            asset["pipeline_status"] = status
        if item.get("kaggle_run_id"):
            asset["last_run_id"] = int(item["kaggle_run_id"])
            asset["last_generator"] = "kaggle-character-sheet"
        if item.get("review_reason"):
            asset["review_reason"] = item["review_reason"]

    save_json(MASTER, queue)


def stats(queue: dict[str, Any]) -> dict[str, Any]:
    assets = queue["assets"]
    strict_done = sum(x["strict_status"] == "DONE" for x in assets)
    awaiting = sum(x["pipeline_status"] == "AWAITING_REVIEW" for x in assets)
    blocked = sum(str(x["pipeline_status"]).startswith(("BLOCKED", "PAUSED_AUTOMATION")) for x in assets)
    evidence = sum(x["pipeline_status"] in {"EVIDENCE_DISPATCHED", "AWAITING_REVIEW"} and x["lane"] == "fx-runtime-reconciliation" for x in assets)
    production_processed = sum(
        x["strict_status"] == "DONE"
        or x["pipeline_status"] in {"AWAITING_REVIEW", "RUNTIME_READY", "DONE"}
        for x in assets
    )
    return {
        "target_total": TARGET_TOTAL,
        "strict_done": strict_done,
        "strict_remaining": TARGET_TOTAL - strict_done,
        "production_processed": production_processed,
        "production_remaining": TARGET_TOTAL - production_processed,
        "awaiting_review": awaiting,
        "blocked": blocked,
        "fx_evidence_processed": evidence,
        "by_lane": {
            lane: sum(x["lane"] == lane and x["strict_status"] != "DONE" for x in assets)
            for lane in sorted({x["lane"] for x in assets if x["strict_status"] != "DONE"})
        },
    }


def write_summary(queue: dict[str, Any], decision: dict[str, Any]) -> None:
    s = stats(queue)
    lines = [
        "# Asset Autofactory — 235 target",
        "",
        f"- Strict DONE: **{s['strict_done']} / {TARGET_TOTAL}**",
        f"- Production processed to DONE/review: **{s['production_processed']} / {TARGET_TOTAL}**",
        f"- Awaiting semantic review: **{s['awaiting_review']}**",
        f"- Automation-blocked: **{s['blocked']}**",
        f"- Current action: **{decision.get('action', 'NONE')}**",
        f"- Current group: **{decision.get('group') or 'none'}**",
        "",
        "The autofactory may generate and technically validate candidates automatically,",
        "but it never promotes a visually unreviewed candidate to strict DONE.",
        "",
    ]
    SUMMARY.write_text("\n".join(lines), encoding="utf-8")
