#!/usr/bin/env python3
"""Repair AI-generated neutral ground shadows in an already collected atlas.

Produces an independent review-only candidate and a provenance JSON report.
Does not touch canonical runtime assets, queues, or strict DONE status.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from PIL import Image

from character_ground_shadow_cleanup import remove_baked_ground_shadow

ACTION_FRAMES = {"IDLE": 6, "WALK": 8, "WORK": 10, "CARRY": 8, "REPAIR": 10, "CELEB": 8}
CHARACTER_ID = re.compile(r"^CHR-(OP|TECH|LOG|ENG)-(IDLE|WALK|WORK|CARRY|REPAIR|CELEB)$")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--asset-id", required=True)
    parser.add_argument("--source-run-id", type=int, required=True)
    parser.add_argument("--min-removed", type=int, default=1)
    args = parser.parse_args()
    match = CHARACTER_ID.fullmatch(args.asset_id)
    if not match:
        parser.error("Only a manifest CHR-{role}-{action} ID is supported")
    if args.source_run_id <= 0 or args.min_removed < 0:
        parser.error("Invalid provenance or removal threshold")

    action = match.group(2)
    expected = ACTION_FRAMES[action]
    with Image.open(args.input) as image:
        if image.size != (1024, 1024):
            raise ValueError("Expected a canonical 1024x1024 atlas")
        source = image.convert("RGBA")
    result = Image.new("RGBA", (1024, 1024))
    details = []
    for frame_no in range(expected):
        x, y = (frame_no % 4) * 256, (frame_no // 4) * 256
        frame = source.crop((x, y, x + 256, y + 256))
        if not frame.getchannel("A").getbbox():
            raise ValueError(f"Expected occupied frame {frame_no+1}")
        fixed, removed = remove_baked_ground_shadow(frame)
        result.alpha_composite(fixed, (x, y))
        details.append({"frame": frame_no + 1, "removed_gray_pixels": removed})
    total = sum(item["removed_gray_pixels"] for item in details)
    if total < args.min_removed:
        raise RuntimeError(f"No evidenced ground shadow to repair: {total} pixels")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    result.save(args.output, "PNG", optimize=True)
    evidence = {
        "schema_version": 1,
        "asset_id": args.asset_id,
        "source_collector_run_id": args.source_run_id,
        "source_sha256": digest(args.input),
        "review_candidate_sha256": digest(args.output),
        "review_candidate_file": args.output.name,
        "frames": details,
        "pixels_removed_total": total,
        "technique": "conservative-neutral-shadow-alpha-erasure",
        "does_not_modify_original": True,
        "strict_status_changed": False,
        "semantic_approval": False,
        "android_runtime_approval": False,
        "review_required": True,
    }
    args.report.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(f"CHARACTER_GROUND_SHADOW_REPAIR_REVIEW_ONLY={args.asset_id}")
    print(f"CHARACTER_GROUND_SHADOW_PIXELS_REMOVED={total}")


if __name__ == "__main__":
    main()
