#!/usr/bin/env python3
"""Plan animation-heavy CHR/MCH deliverables from the canonical sprite manifest.

This does not generate art. It turns vague manifest frame budgets into a stable
production contract so future GPU workers and validators agree on frame count,
cell size, sheet geometry, pivot rules and loop behavior before consuming quota.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
INCOMING = ROOT / "art/incoming/final-sprites"
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
MAX_BATCH = 16

# Fixed targets chosen inside the manifest budgets. Keeping a deterministic count
# makes sheet validation and runtime animation timing reproducible.
CHR_FRAMES = {
    "IDLE": 8,
    "WALK": 8,
    "WORK": 12,
    "CARRY": 8,
    "REPAIR": 12,
    "CELEB": 10,
}
MCH_FRAMES = 8


def frame_contract(asset_id: str) -> tuple[int, int, int, int, str]:
    if asset_id.startswith("CHR-"):
        action = asset_id.rsplit("-", 1)[-1]
        frames = CHR_FRAMES[action]
        cell = 256
        columns = 4
        pivot = "feet-center"
    else:
        frames = MCH_FRAMES
        cell = 512
        columns = 4
        pivot = "machine-base-center"
    rows = math.ceil(frames / columns)
    return frames, cell, columns, rows, pivot


def items(kind: str):
    order = 0
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if not m:
            continue
        asset_id, name, description, runtime, status = [x.strip() for x in m.groups()]
        family = "CHR" if asset_id.startswith("CHR-") else "MCH" if asset_id.startswith("MCH-") else None
        if family is None or (kind != "ALL" and family != kind):
            continue
        stem = Path(runtime).stem
        candidate = INCOMING / f"{stem}.png"
        runtime_path = ROOT / runtime
        if status.upper() != "TODO" or candidate.exists() or runtime_path.exists():
            continue
        frames, cell, cols, rows, pivot = frame_contract(asset_id)
        yield {
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
            "padding": 4,
            "pivot": pivot,
            "loop": not asset_id.endswith("CELEB"),
            "order": order,
        }
        order += 1


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--kind", choices=["ALL", "CHR", "MCH"], default="ALL")
    p.add_argument("--count", type=int, default=8)
    args = p.parse_args()
    if not 1 <= args.count <= MAX_BATCH:
        raise SystemExit(f"count must be between 1 and {MAX_BATCH}")
    planned = list(items(args.kind))[: args.count]
    for item in planned:
        item.pop("order", None)
    print(json.dumps({"include": planned}, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
