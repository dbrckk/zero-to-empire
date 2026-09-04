#!/usr/bin/env python3
"""Build small GPU batches directly from the canonical sprite manifest.

The planner deliberately excludes animation-heavy character/machine sheets and
terrain connectors from the generic static lane. Those keep dedicated pipelines.
Already-materialized candidates/runtime files are skipped even if the manifest
ledger has not yet been reconciled, preventing duplicate GPU work.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
INCOMING = ROOT / "art/incoming/final-sprites"
SUPPORTED = ("BLD-", "CORE-", "VEH-", "PRP-")
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")


def rows():
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if not m:
            continue
        asset_id, name, description, runtime, status = [x.strip() for x in m.groups()]
        if not asset_id.startswith(SUPPORTED):
            continue
        runtime_path = ROOT / runtime
        stem = Path(runtime).stem
        candidate = INCOMING / f"{stem}.png"
        yield {
            "id": asset_id,
            "name": name,
            "description": description,
            "runtime": runtime,
            "stem": stem,
            "status": status.upper(),
            "kind": asset_id.split("-", 1)[0],
            "materialized": candidate.exists() or runtime_path.exists(),
        }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--kind", default="BLD", choices=["ALL", "BLD", "CORE", "VEH", "PRP"])
    p.add_argument("--count", type=int, default=4)
    p.add_argument("--reverse", action="store_true")
    args = p.parse_args()
    if not 1 <= args.count <= 12:
        raise SystemExit("count must be between 1 and 12")
    items = [
        r for r in rows()
        if r["status"] == "TODO"
        and not r["materialized"]
        and (args.kind == "ALL" or r["kind"] == args.kind)
    ]
    if args.reverse:
        items.reverse()
    items = items[: args.count]
    for item in items:
        item.pop("materialized", None)
    print(json.dumps({"include": items}, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
