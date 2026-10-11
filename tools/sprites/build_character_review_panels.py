#!/usr/bin/env python3
"""Make lossless action-by-action frame sheets for human character review.

Outputs are review evidence only. This tool never promotes or edits sprites.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ACTIONS = {"idle": 6, "walk": 8, "work": 10, "carry": 8, "repair": 10, "celeb": 8}
PATTERN = re.compile(r"^zte_chr_(op|tech|log|eng)_(idle|walk|work|carry|repair|celeb)_final\.png$")
CELL = 256
TILE = 276
ROW_HEIGHT = 306
LABEL_WIDTH = 154
HEADER_HEIGHT = 76


def checkerboard() -> Image.Image:
    result = Image.new("RGB", (CELL, CELL), (221, 225, 232))
    draw = ImageDraw.Draw(result)
    for y in range(0, CELL, 16):
        for x in range(0, CELL, 16):
            if (x // 16 + y // 16) % 2:
                draw.rectangle((x, y, x + 15, y + 15), fill=(193, 200, 211))
    return result


def readable_font(size: int) -> ImageFont.ImageFont:
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    except OSError:
        return ImageFont.load_default()


def create_panel(role: str, assets: dict[str, Path], output: Path, qa: dict[str, dict]) -> dict:
    font = readable_font(15)
    heading = readable_font(21)
    labels = readable_font(18)
    width = LABEL_WIDTH + 10 * TILE
    height = HEADER_HEIGHT + len(ACTIONS) * ROW_HEIGHT
    sheet = Image.new("RGB", (width, height), (24, 27, 34))
    draw = ImageDraw.Draw(sheet)
    draw.rectangle((0, 0, width, HEADER_HEIGHT - 1), fill=(43, 50, 61))
    draw.text((18, 15), f"ZERO TO EMPIRE  |  {role.upper()} CHARACTER IDENTITY", font=heading, fill=(246, 248, 250))
    draw.text((18, 47), "Original 256x256 frames. Compare face, outfit, body scale and pose across ALL actions.", font=font, fill=(187, 202, 220))
    base = checkerboard()
    status: dict = {}
    for row, (action, frame_count) in enumerate(ACTIONS.items()):
        y = HEADER_HEIGHT + row * ROW_HEIGHT
        draw.rectangle((0, y, width, y + ROW_HEIGHT - 2), outline=(72, 79, 92), width=1)
        path = assets.get(action)
        qa_row = qa.get(path.name, {}) if path else {}
        is_pass = qa_row.get("pass") is True
        label_color = (105, 202, 157) if is_pass else (236, 184, 97) if path else (166, 170, 179)
        draw.text((14, y + 12), action.upper(), font=labels, fill=label_color)
        if path is None:
            status[action] = {"candidate": False, "expected_frames": frame_count, "qa_pass": None}
            draw.text((14, y + 36), "NOT GENERATED", font=font, fill=(183, 189, 199))
            continue
        issues = list(qa_row.get("issues", []) or [])
        draw.text((14, y + 34), "QA PASS" if is_pass else "QA REVIEW", font=font, fill=label_color)
        for idx, issue in enumerate(issues[:6]):
            draw.text((10, y + 60 + idx * 18), str(issue)[:22], font=font, fill=(226, 158, 151))
        try:
            with Image.open(path) as src:
                if src.size != (1024, 1024):
                    raise ValueError(f"Expected atlas 1024x1024, got {src.size}")
                rgba = src.convert("RGBA")
            for frame_idx in range(frame_count):
                fx = (frame_idx % 4) * CELL
                fy = (frame_idx // 4) * CELL
                tile = rgba.crop((fx, fy, fx + CELL, fy + CELL))
                bx = LABEL_WIDTH + frame_idx * TILE + 10
                by = y + 23
                background = base.copy()
                background.paste(tile, (0, 0), tile)
                sheet.paste(background, (bx, by))
                draw.text((bx + 2, by + CELL + 8), f"Frame {frame_idx + 1:02d}", font=font, fill=(212, 216, 223))
            status[action] = {"candidate": True, "expected_frames": frame_count, "qa_pass": is_pass, "issues": issues}
        except Exception as exc:
            status[action] = {"candidate": True, "expected_frames": frame_count, "qa_pass": False,
                              "issues": issues + [f"review-panel-error:{exc}"]}
            draw.text((LABEL_WIDTH + 12, y + 45), str(exc)[:90], font=font, fill=(231, 145, 132))
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, "PNG", optimize=True)
    return {"role": role.upper(), "file": output.name, "actions": status,
            "context_only": True, "automatically_approved": False}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--qa-report", type=Path)
    args = parser.parse_args()
    qa: dict[str, dict] = {}
    if args.qa_report and args.qa_report.is_file():
        data = json.loads(args.qa_report.read_text(encoding="utf-8"))
        rows = data if isinstance(data, list) else data.get("assets", [])
        qa = {str(row.get("file", "")): row for row in rows}
    by_role: dict[str, dict[str, Path]] = {}
    if args.candidates.is_dir():
        for path in sorted(args.candidates.iterdir()):
            match = PATTERN.fullmatch(path.name)
            if match and path.is_file() and path.stat().st_size:
                role, action = match.groups()
                by_role.setdefault(role, {})[action] = path
    args.output_dir.mkdir(parents=True, exist_ok=True)
    results = [create_panel(role, assets, args.output_dir / f"review-frames-{role}.png", qa)
               for role, assets in sorted(by_role.items())]
    summary = {"schema_version": 1, "review_only": True, "roles": results}
    (args.output_dir / "review-panels.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"CHARACTER_REVIEW_PANELS={len(results)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
