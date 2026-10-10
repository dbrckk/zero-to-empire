#!/usr/bin/env python3
"""Stage all six canonical-format TECH animations from one deterministic textured rig.

These are visual-review CANDIDATES, never replacements for canonical PNG/WebP
or automatic strict-DONE promotions. The 24-frame articulated source is
downsampled to the existing Android 4x4 / action-frame-count contract.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw

from audit_character_candidates import inspect
from package_tech_actions_runtime import game_scale_metrics

ACTIONS = {"IDLE": 6, "WALK": 8, "WORK": 10, "CARRY": 8, "REPAIR": 10, "CELEB": 8}
SOURCE_FRAMES = 24
CELL = 256


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def selected_indices(count: int, source_count: int = SOURCE_FRAMES) -> list[int]:
    if count < 4 or source_count < count or source_count % 2 or count > 16:
        raise ValueError("Invalid canonical/source frame budget")
    result = [i * source_count // count for i in range(count)]
    if len(set(result)) != count or max(result) >= source_count:
        raise ValueError("Duplicate or missing selected phase")
    return result


def validate_index(source: Path, skin: Path) -> dict:
    index = json.loads((source / "production-index.json").read_text(encoding="utf-8"))
    if (index.get("format") != "zte-modular-actions-v3"
            or index.get("strict_status") != "NEEDS_REVIEW"
            or index.get("review_required") is not True):
        raise ValueError("Rig source is not explicitly review-only")
    if index.get("source_skin_sha256") != digest(skin):
        raise ValueError("Skin provenance hash differs from source rig")
    actions = {row.get("action"): row for row in index.get("actions", [])}
    if set(actions) != {"WALK", "CARRY", "IDLE", "WORK", "REPAIR", "CELEB"}:
        raise ValueError("Rig action index is incomplete")
    for action in ACTIONS:
        row = actions[action]
        if (row.get("asset_id") != f"CHR-TECH-{action}"
                or row.get("technical_pass") is not True
                or row.get("strict_status") != "NEEDS_REVIEW"
                or row.get("source_skin_sha256") != digest(skin)):
            raise ValueError(f"Unverified rig action: {action}")
    return index


def stage_action(source: Path, output: Path, action: str, skin_sha: str) -> dict:
    if action not in ACTIONS:
        raise ValueError(f"Unknown action: {action}")
    folder = source / action
    manifest = json.loads((folder / "qa-manifest.json").read_text(encoding="utf-8"))
    if (manifest.get("asset_id") != f"CHR-TECH-{action}"
            or manifest.get("strict_status") != "NEEDS_REVIEW"
            or manifest.get("human_visual_review_required") is not True
            or manifest.get("source_skin_sha256") != skin_sha):
        raise ValueError(f"Stale or unreviewable action metadata: {action}")
    qa = manifest.get("qa", {})
    if (qa.get("technical_pass") is not True
            or qa.get("visual_review_pass") is not False
            or qa.get("semantic_review_pass") is not False):
        raise ValueError(f"Rig QA status invalid: {action}")
    if int(manifest.get("frames", 0)) != SOURCE_FRAMES:
        raise ValueError("Only 24-frame source rigs are supported")
    if not (folder / "REVIEW_REQUIRED.txt").is_file():
        raise ValueError("Explicit source review marker is missing")

    chosen = selected_indices(ACTIONS[action])
    atlas = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
    frame_hashes = []
    preview = []
    for cell_index, index in enumerate(chosen):
        path = folder / "frames" / f"CHR-TECH-{action}-{index:02d}.png"
        if not path.is_file():
            raise ValueError("Missing source frame: " + str(path))
        with Image.open(path) as src:
            if src.mode != "RGBA" or src.size != (512, 512):
                raise ValueError("Unexpected rig frame shape")
            frame = src.copy()
        if not game_scale_metrics(frame)["pass"]:
            raise ValueError(f"{action} source frame {index} fails 96px visibility")
        frame_hashes.append(digest(path))
        scaled = frame.resize((CELL, CELL), Image.Resampling.LANCZOS)
        atlas.alpha_composite(scaled, ((cell_index % 4) * CELL,
                                      (cell_index // 4) * CELL))
        tile = Image.new("RGBA", (96, 96), (29, 37, 49, 255))
        tile.alpha_composite(frame.resize((96, 96), Image.Resampling.LANCZOS))
        preview.append(tile.convert("RGB"))

    stem = f"zte_chr_tech_{action.lower()}_final"
    output.mkdir(parents=True, exist_ok=True)
    png = output / (stem + ".png")
    atlas.save(png, optimize=True)
    technical = inspect(png, f"CHR-TECH-{action}")
    if not technical["technical_pass"]:
        png.unlink(missing_ok=True)
        raise ValueError(f"Canonical atlas structural QA rejected {action}: "
                         + ",".join(technical.get("findings", [])))

    contact = Image.new("RGB", (96 * len(preview), 128), (29, 37, 49))
    d = ImageDraw.Draw(contact)
    for i, tile in enumerate(preview):
        contact.paste(tile, (i * 96, 22))
        d.text((i * 96 + 5, 4), str(chosen[i]), fill=(207, 224, 239))
    contact.save(output / (stem + "-contact.png"), optimize=True)
    preview[0].save(output / (stem + "-preview.gif"),
                    save_all=True, append_images=preview[1:],
                    loop=0, duration=round(1000 * SOURCE_FRAMES
                                           / (manifest["fps"] * len(preview))),
                    optimize=False)
    return {
        "asset_id": f"CHR-TECH-{action}",
        "source_skin_sha256": skin_sha,
        "source_format": "articulated-24-frame-512px-single-identity",
        "source_indices": chosen,
        "source_frame_sha256": frame_hashes,
        "staged_png": png.name,
        "staged_sha256": digest(png),
        "frame_count": len(chosen),
        "atlas_size": [1024, 1024],
        "canonical_frame_size": [CELL, CELL],
        "canonical_geometry_pass": technical["technical_pass"],
        "automated_visual_risks": technical.get("visual_risk", {}),
        "semantic_approved": False,
        "visual_review_pass": False,
        "strict_status": "NEEDS_REVIEW",
        "runtime_integrated": False,
        "android_ci_for_candidate": False,
        "release_eligible": False,
    }


def stage(source: Path, skin: Path, output: Path) -> dict:
    index = validate_index(source, skin)
    items = [stage_action(source, output, action, index["source_skin_sha256"])
             for action in ACTIONS]
    result = {
        "format": "zte-canonical-tech-review-v1",
        "target_ids": [item["asset_id"] for item in items],
        "candidate_count": len(items),
        "semantic_approved_count": 0,
        "automatic_promotion_permitted": False,
        "canonical_queue_mutated": False,
        "android_runtime_mutated": False,
        "source_skin_sha256": index["source_skin_sha256"],
        "items": items,
    }
    (output / "review-report.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8")
    (output / "REVIEW_REQUIRED.txt").write_text(
        "Visual inspection of all frames and moving cycle at game scale is mandatory. "
        "No strict DONE, canonical-source replacement or Android promotion.\n",
        encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("build/tech-actions-v3"))
    parser.add_argument("--skin", type=Path, default=Path("tools/sprites/skin-tech-v1.webp"))
    parser.add_argument("--output", type=Path,
                        default=Path("art/production/character-rig-review-candidates"))
    args = parser.parse_args()
    result = stage(args.source, args.skin, args.output)
    print(json.dumps({"candidate_count": result["candidate_count"],
                      "review_required": True,
                      "strict_done_changes": 0,
                      "assets": result["target_ids"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
