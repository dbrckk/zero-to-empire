#!/usr/bin/env python3
"""Build candidate-only static GPU batches from the canonical sprite manifest.

Animation-heavy character/machine sheets and terrain stay outside this generic static lane.
The canonical manifest status is authoritative: a TODO row remains eligible even when stale
candidate/runtime files exist from an older pre-semantic-finalization workflow.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
SUPPORTED = ("BLD-", "CORE-", "VEH-", "PRP-")
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
FAST_PRIORITY = {"PRP": 0, "VEH": 1, "CORE": 2, "BLD": 3}
MAX_BATCH = 36


def rows():
    order = 0
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if not m:
            continue
        asset_id, name, description, runtime, status = [x.strip() for x in m.groups()]
        if not asset_id.startswith(SUPPORTED):
            continue
        kind = asset_id.split("-", 1)[0]
        yield {
            "id": asset_id,
            "name": name,
            "description": description,
            "runtime": runtime,
            "stem": Path(runtime).stem,
            "status": status.upper(),
            "kind": kind,
            "order": order,
        }
        order += 1


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--kind", default="ALL", choices=["ALL", "BLD", "CORE", "VEH", "PRP"])
    p.add_argument("--count", type=int, default=36)
    p.add_argument("--reverse", action="store_true")
    args = p.parse_args()
    if not 1 <= args.count <= MAX_BATCH:
        raise SystemExit(f"count must be between 1 and {MAX_BATCH}")

    items = [
        r for r in rows()
        if r["status"] == "TODO"
        and (args.kind == "ALL" or r["kind"] == args.kind)
    ]
    if args.kind == "ALL":
        items.sort(key=lambda r: (FAST_PRIORITY[r["kind"]], r["order"]))
    if args.reverse:
        items.reverse()
    items = items[: args.count]
    for item in items:
        item.pop("order", None)
    print(json.dumps({"include": items}, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
