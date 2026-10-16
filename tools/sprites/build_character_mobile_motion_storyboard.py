#!/usr/bin/env python3
"""Actual-gameplay-size animation storyboard, verified source candidates only.

Every 42px frame is rendered first against both daytime and nighttime game
backgrounds, *then* enlarged with nearest-neighbor for human inspection.
This avoids judging movement from attractive but misleading 256px source art.
"""
from __future__ import annotations

import argparse
import io
import json
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw

from audit_character_bank_motion import DAY, NIGHT, FRAMES, MOBILE_SIZE, composite
from build_character_role_contact_sheet import _font, _load

SCALE = 3
PAD = 18
LABEL_WIDTH = 210
FRAME_GAP = 12
TILE_WIDTH = MOBILE_SIZE * SCALE
ROW_HEIGHT = 320
TITLE_HEIGHT = 104
BG = (12, 20, 33)
TEXT = (242, 248, 255)
MUTED = (173, 192, 212)
WARNING = (255, 173, 109)
FRAME_INDICES = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
DISPLAY_FRAMES = 4


def _selected_frames(count: int) -> tuple[int, ...]:
    """Representative early/mid/late frames, including first and final seam."""
    if count < DISPLAY_FRAMES:
        raise ValueError("Too few animation frames for gameplay storyboard")
    return (0, count // 3, (2 * count) // 3, count - 1)


def build(bank_path: Path, audit_path: Path, output_path: Path) -> dict:
    metadata, rows = _load(bank_path, audit_path)
    if not rows:
        raise ValueError("No candidate animations")
    rows.sort(key=lambda row: (("OP", "LOG", "ENG").index(row["role"]),
                               ("IDLE", "WALK", "WORK", "CARRY", "REPAIR", "CELEB").index(row["action"])))
    width = PAD * 2 + LABEL_WIDTH + (TILE_WIDTH + FRAME_GAP) * DISPLAY_FRAMES
    height = TITLE_HEIGHT + ROW_HEIGHT * len(rows) + PAD
    output = Image.new("RGB", (width, height), BG)
    painter = ImageDraw.Draw(output)
    title_font, label_font, detail_font = _font(20), _font(15), _font(12)
    painter.text((PAD, 18), "ZERO TO EMPIRE / ANIMATION A 42 PIXELS",
                 font=title_font, fill=TEXT)
    painter.text((PAD, 52), "4 images par action, JOUR et NUIT, x3 sans lissage",
                 font=detail_font, fill=MUTED)
    painter.text((PAD, 71), "Aucune approbation automatique ni integration Android",
                 font=detail_font, fill=MUTED)

    with zipfile.ZipFile(bank_path) as bank:
        for position, row in enumerate(rows):
            top = TITLE_HEIGHT + position * ROW_HEIGHT
            role, action = row["role"], row["action"]
            name = f"candidates/zte_chr_{role.lower()}_{action.lower()}_final.png"
            count = FRAMES[action]
            with Image.open(io.BytesIO(bank.read(name))) as atlas:
                atlas.load()
                selected = _selected_frames(count)
                frames = [
                    atlas.crop(((i % 4) * 256, (i // 4) * 256,
                                (i % 4 + 1) * 256, (i // 4 + 1) * 256))
                    for i in selected
                ]
            flagged = bool(row["identity_flags"] or row["motion_flags"])
            painter.rounded_rectangle(
                (PAD, top, width - PAD, top + ROW_HEIGHT - 9),
                radius=10, fill=(25, 39, 58),
                outline=WARNING if flagged else (61, 85, 110), width=2 if flagged else 1
            )
            painter.text((PAD + 12, top + 18), f"{role} / {action}",
                         font=label_font, fill=TEXT)
            notice = ("IDENTITE" if row["identity_flags"] else
                      "MOUVEMENT" if row["motion_flags"] else "REVUE MANUELLE")
            painter.text((PAD + 12, top + 45), notice,
                         font=detail_font, fill=WARNING if flagged else MUTED)
            if row["source_type"] == "repo-local-original":
                painter.text((PAD + 12, top + 70), "SOURCE LOCALE",
                             font=detail_font, fill=WARNING)
            for j, (index, frame) in enumerate(zip(selected, frames)):
                x = PAD + LABEL_WIDTH + j * (TILE_WIDTH + FRAME_GAP)
                painter.text((x, top + 9), f"F{index + 1:02d}",
                             font=detail_font, fill=MUTED)
                for k, (lighting, bg) in enumerate((("JOUR", DAY), ("NUIT", NIGHT))):
                    y = top + 31 + k * (TILE_WIDTH + 20)
                    rendered = composite(frame, bg)
                    zoomed = rendered.resize((TILE_WIDTH, TILE_WIDTH),
                                              Image.Resampling.NEAREST)
                    output.paste(zoomed, (x, y))
                    if j == 0:
                        painter.text((PAD + 12, y + 105), lighting,
                                     font=detail_font, fill=MUTED)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output.save(output_path, "PNG", optimize=True)
    return {
        "review_only": True, "strict_done_added": 0,
        "strict_done_unchanged": metadata["strict_done"],
        "candidate_count": len(rows), "frames_per_action": DISPLAY_FRAMES,
        "actual_render_px": MOBILE_SIZE, "nearest_neighbor_zoom": SCALE,
        "bytes": output_path.stat().st_size,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(build(args.bank, args.audit, args.output), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
