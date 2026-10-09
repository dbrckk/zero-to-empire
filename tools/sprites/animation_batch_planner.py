#!/usr/bin/env python3
"""Plan unresolved animation assets from the authoritative 235-target queue.

This planner is READ-ONLY. It explicitly separates art generation from human
semantic review; an installed runtime sheet is not proof of strict DONE.
Frame sizes/counts match the actual Android runtime contracts, not aspirational
older production notes.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
MASTER = ROOT / "art/production/master-asset-queue.json"
INCOMING = ROOT / "art/incoming/final-sprites"
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
MAX_BATCH = 16

# Canonical sources: process_final_sprites.py, CanonicalCharacterRaster.kt.
CHR_FRAMES = {
    "IDLE": 6, "WALK": 8, "WORK": 10,
    "CARRY": 8, "REPAIR": 10, "CELEB": 8,
}
MCH_FRAMES = 8


def frame_contract(asset_id: str) -> tuple[int, int, int, int, str]:
    if asset_id.startswith("CHR-"):
        action = asset_id.rsplit("-", 1)[-1]
        frames = CHR_FRAMES[action]
        cell, cols, pivot = 256, 4, "feet-center"
    else:
        frames = MCH_FRAMES
        cell, cols, pivot = 512, 4, "machine-base-center"
    return frames, cell, cols, math.ceil(frames / cols), pivot


def task_for(pipeline_status: str) -> str:
    if pipeline_status in {"BLOCKED", "REJECTED_SEMANTIC"}:
        return "regenerate"
    if pipeline_status in {
        "AWAITING_REVIEW", "CANDIDATE", "TECHNICAL_PASS",
        "VALIDATED", "APPROVED", "RUNTIME_READY",
    }:
        return "semantic-review"
    return "generate"


def items(kind: str, root: Path = ROOT) -> list[dict]:
    master = json.loads((root / MASTER.relative_to(ROOT)).read_text(encoding="utf-8"))
    assets = master.get("assets", [])
    if master.get("target_total") != 235 or len(assets) != 235:
        raise ValueError("Master queue must contain exactly 235 canonical targets")
    by_id = {a["id"]: a for a in assets}
    if len(by_id) != 235:
        raise ValueError("Duplicate canonical asset IDs")

    planned: list[dict] = []
    manifest_ids: set[str] = set()
    for line in (root / MANIFEST.relative_to(ROOT)).read_text(encoding="utf-8").splitlines():
        match = ROW.match(line)
        if not match:
            continue
        asset_id, name, description, runtime, status = [x.strip() for x in match.groups()]
        if asset_id in manifest_ids:
            raise ValueError("Duplicate manifest asset: " + asset_id)
        manifest_ids.add(asset_id)
        family = "CHR" if asset_id.startswith("CHR-") else "MCH" if asset_id.startswith("MCH-") else None
        if family is None or (kind != "ALL" and family != kind):
            continue
        record = by_id.get(asset_id)
        if record is None:
            raise ValueError("Animation asset missing from 235 queue: " + asset_id)
        if record.get("strict_status") == "DONE":
            if status != "DONE":
                raise ValueError("Strict DONE and manifest disagree for: " + asset_id)
            continue
        if status == "DONE":
            raise ValueError("Premature manifest DONE: " + asset_id)

        frames, cell, cols, rows, pivot = frame_contract(asset_id)
        stem = Path(runtime).stem
        candidate = root / INCOMING.relative_to(ROOT) / (stem + ".png")
        runtime_path = root / runtime
        pipeline_status = str(record.get("pipeline_status") or "")
        planned.append({
            "id": asset_id,
            "name": name,
            "description": description,
            "runtime": runtime,
            "stem": stem,
            "family": family,
            "frames": frames,
            "cell": cell,
            "columns": cols,
            "rows": rows,
            "sheet_width": cols * cell,
            "sheet_height": rows * cell,
            "padding": 8 if family == "CHR" else 4,
            "pivot": pivot,
            "loop": not asset_id.endswith("CELEB"),
            "pipeline_status": pipeline_status,
            "manifest_status": status,
            "task": task_for(pipeline_status),
            "has_source_candidate": candidate.is_file(),
            "has_runtime_asset": runtime_path.is_file(),
            "semantic_approved": False,
            "automatic_promotion_permitted": False,
        })

    # Exactly the two historically rejected candidates should lead the repair
    # queue; AWAITING_REVIEW items need human review, not another blind GPU run.
    priority = {"regenerate": 0, "semantic-review": 1, "generate": 2}
    return sorted(planned, key=lambda i: (priority[i["task"]], i["id"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=["ALL", "CHR", "MCH"], default="ALL")
    parser.add_argument("--count", type=int, default=8)
    args = parser.parse_args()
    if not 1 <= args.count <= MAX_BATCH:
        raise SystemExit(f"count must be between 1 and {MAX_BATCH}")
    all_items = items(args.kind)
    selected = all_items[:args.count]
    print(json.dumps({
        "include": selected,
        "unresolved_count": len(all_items),
        "regeneration_count": sum(a["task"] == "regenerate" for a in all_items),
        "semantic_review_count": sum(a["task"] == "semantic-review" for a in all_items),
        "approved_by_planner": 0,
        "strict_count_increased": False,
    }, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
