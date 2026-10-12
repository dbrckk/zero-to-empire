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
from character_semantic_gate import clip_risk

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


def face_center_x(frame: Image.Image, bbox: tuple[int, int, int, int]) -> int:
    """Locate the dominant head/helmet mass, not the wider tool/crate bbox.

    Looking at the top 6%-24% of the visible character reduces false shifts
    when an action adds a large prop beside the hands. This is only a crop
    heuristic; it never classifies identity or automatically approves a sheet.
    """
    top = bbox[1] + round((bbox[3] - bbox[1]) * .06)
    bottom = bbox[1] + round((bbox[3] - bbox[1]) * .24)
    alpha = frame.getchannel("A")
    if bottom <= top:
        return (bbox[0] + bbox[2]) // 2
    region = alpha.crop((0, max(0, top), CELL, min(CELL, bottom)))
    pixels = region.load()
    weighted_sum = 0
    weight = 0
    for y in range(region.height):
        for x in range(region.width):
            if pixels[x, y] >= 64:
                weighted_sum += x
                weight += 1
    return round(weighted_sum / weight) if weight else (bbox[0] + bbox[2]) // 2


def create_head_panel(role: str, assets: dict[str, Path], output: Path) -> None:
    """Magnify each frame's face/headgear for cross-action identity review.

    Visual evidence only: a matching crop does not prove animation or identity
    correctness. It is easier to read on Android than the wide full-frame sheet.
    """
    tile_width, cell_width, row_height = 172, 144, 194
    header, label_width = 70, 130
    width = label_width + 10 * tile_width
    height = header + len(ACTIONS) * row_height
    panel = Image.new("RGB", (width, height), (26, 29, 36))
    draw = ImageDraw.Draw(panel)
    title_font = readable_font(20)
    font = readable_font(14)
    label_font = readable_font(18)
    draw.text((14, 12), f"{role.upper()} - FACE + HEADGEAR CONTINUITY REVIEW", font=title_font,
              fill=(245, 245, 250))
    draw.text((14, 40), "Enlarged 256px sprite crops. Visual review only; not automatic approval.",
              font=font, fill=(194, 204, 222))
    for row, (action, frames) in enumerate(ACTIONS.items()):
        y = header + row * row_height
        draw.line((0, y, width, y), fill=(68, 75, 86), width=1)
        draw.text((12, y + 12), action.upper(), font=label_font, fill=(228, 234, 246))
        path = assets.get(action)
        if path is None:
            draw.text((12, y + 38), "NO CANDIDATE", font=font, fill=(191, 194, 203))
            continue
        try:
            with Image.open(path) as src:
                if src.size != (1024, 1024):
                    raise ValueError("Expected a 1024x1024 character atlas")
                atlas = src.convert("RGBA")
            for index in range(frames):
                f = atlas.crop(((index % 4) * CELL, (index // 4) * CELL,
                                ((index % 4) + 1) * CELL, ((index // 4) + 1) * CELL))
                bbox = f.getchannel("A").getbbox()
                if bbox is None:
                    continue
                xmid = face_center_x(f, bbox)
                x0 = min(CELL - 96, max(0, xmid - 48))
                y0 = min(CELL - 96, max(0, bbox[1] - 5))
                head = f.crop((x0, y0, x0 + 96, y0 + 96)).resize(
                    (cell_width, cell_width), Image.Resampling.NEAREST)
                background = checkerboard().resize((cell_width, cell_width))
                background.paste(head, (0, 0), head)
                x = label_width + index * tile_width + 7
                panel.paste(background, (x, y + 12))
                draw.text((x + 2, y + 164), f"Frame {index + 1:02d}", font=font,
                          fill=(215, 221, 230))
        except (OSError, ValueError) as exc:
            draw.text((label_width + 8, y + 30), f"REVIEW ERROR: {exc}"[:90],
                      font=font, fill=(236, 158, 148))
    output.parent.mkdir(parents=True, exist_ok=True)
    panel.save(output, "PNG", optimize=True)


def create_mobile_action_panel(role: str, action: str, path: Path,
                               output: Path, qa: dict[str, dict]) -> None:
    """Portrait 2-column contact sheet readable on an Android smartphone.

    Every frame retains its original 256x256 pixels, not a tiny thumbnail.
    Only review evidence is produced; a QA PASS is not semantic approval.
    """
    frame_count = ACTIONS[action]
    columns, stride, header = 2, 290, 112
    width = columns * stride + 18
    height = header + ((frame_count + columns - 1) // columns) * 308
    image = Image.new("RGB", (width, height), (23, 27, 33))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, header - 2), fill=(43, 50, 61))
    draw.text((18, 13), f"{role.upper()}  /  {action.upper()}",
              font=readable_font(27), fill=(248, 250, 253))
    record = qa.get(path.name, {})
    status = "TECHNICAL PASS - VISUAL REVIEW REQUIRED" if record.get("pass") is True else (
        "TECHNICAL REVIEW REQUIRED")
    draw.text((18, 55), status, font=readable_font(15),
              fill=(245, 202, 146) if record.get("pass") is True else (245, 159, 151))
    draw.text((18, 79), "No automatic semantic approval", font=readable_font(15),
              fill=(199, 210, 226))
    with Image.open(path) as src:
        if src.size != (1024, 1024):
            raise ValueError(f"Invalid mobile review atlas: {path}")
        atlas = src.convert("RGBA")
    background = checkerboard()
    for index in range(frame_count):
        x = 15 + (index % columns) * stride
        y = header + (index // columns) * 308 + 8
        tile = atlas.crop(((index % 4) * CELL, (index // 4) * CELL,
                           ((index % 4) + 1) * CELL, ((index // 4) + 1) * CELL))
        opaque = background.copy()
        opaque.paste(tile, (0, 0), tile)
        image.paste(opaque, (x, y))
        draw.text((x + 2, y + CELL + 8), f"Frame {index+1:02d} / {frame_count:02d}",
                  font=readable_font(18), fill=(223, 231, 242))
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, "PNG", optimize=True)


def _frame_alpha_iou(left: Image.Image, right: Image.Image) -> float:
    """Downsampled alpha overlap only; not an identity or action verdict."""
    a = left.getchannel("A").resize((64, 64), Image.Resampling.BILINEAR)
    b = right.getchannel("A").resize((64, 64), Image.Resampling.BILINEAR)
    left_mask = [v >= 32 for v in a.getdata()]
    right_mask = [v >= 32 for v in b.getdata()]
    overlap = sum(x and y for x, y in zip(left_mask, right_mask))
    union = sum(x or y for x, y in zip(left_mask, right_mask))
    return overlap / union if union else 1.0


def motion_review_evidence(frames: list[Image.Image], action: str) -> dict:
    """Measure animation loop cuts separately from the generator's frame QA.

    The closing transition (last -> first) is rendered continuously in the
    Android loop but was absent from previous adjacent-frame QA. A bad seam
    is flagged for human review, *never* promoted or auto-approved.
    """
    if len(frames) < 2:
        return {"status": "INSUFFICIENT_EVIDENCE", "flags": ["TOO_FEW_FRAMES"]}
    steps = [1 - _frame_alpha_iou(a, b) for a, b in zip(frames[:-1], frames[1:])]
    loop_step = 1 - _frame_alpha_iou(frames[-1], frames[0])
    mean_step = sum(steps) / len(steps)
    seam_ratio = loop_step / max(.015, mean_step)
    flags = []
    if action != "idle" and loop_step > .28 and seam_ratio > 1.6:
        flags.append("ANIMATION_LOOP_SEAM_REVIEW")
    if max(steps) > .5:
        flags.append("SUDDEN_ADJACENT_SILHOUETTE_CHANGE_REVIEW")
    if action not in {"idle"} and mean_step < .08:
        flags.append("LOW_VISIBLE_MOTION_REVIEW")
    return {
        "status": "REVIEW_ONLY",
        "mean_adjacent_alpha_change": round(mean_step, 4),
        "max_adjacent_alpha_change": round(max(steps), 4),
        "last_to_first_alpha_change": round(loop_step, 4),
        "loop_seam_to_mean_step_ratio": round(seam_ratio, 3),
        "flags": flags,
        "automatic_semantic_approval": False,
    }


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
            raw_frames = [
                rgba.crop(((idx % 4) * CELL, (idx // 4) * CELL,
                           ((idx % 4) + 1) * CELL, ((idx // 4) + 1) * CELL))
                for idx in range(frame_count)
            ]
            diagnostics = motion_review_evidence(raw_frames, action)
            # Review candidates with the newest image-only risk rules, even
            # when their GPU run used an older generator. These signals cannot
            # alter an asset's canonical review or strict DONE state.
            try:
                visual_risk = clip_risk(raw_frames, action.upper())
            except (ValueError, IndexError, OSError) as exc:
                visual_risk = {
                    "risk_level": "BLOCKING",
                    "flags": ["VISUAL_RISK_CHECK_UNAVAILABLE"],
                    "error": str(exc),
                    "image_only_semantic_approval": False,
                }
            if visual_risk["risk_level"] == "BLOCKING":
                draw.text((10, y + 196), "IMAGE RISK", font=font,
                          fill=(231, 142, 127))
                draw.text((10, y + 218),
                          ",".join(visual_risk.get("flags", []))[:21],
                          font=font, fill=(226, 158, 151))
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
            status[action] = {
                "candidate": True, "expected_frames": frame_count,
                "qa_pass": is_pass, "issues": issues,
                "temporal_evidence": diagnostics,
                "image_only_risk": visual_risk,
            }
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
    results = []
    for role, assets in sorted(by_role.items()):
        item = create_panel(role, assets, args.output_dir / f"review-frames-{role}.png", qa)
        create_head_panel(role, assets, args.output_dir / f"review-heads-{role}.png")
        item["head_detail_file"] = f"review-heads-{role}.png"
        mobile_files = {}
        for action, path in sorted(assets.items()):
            filename = f"review-mobile-{role}-{action}.png"
            create_mobile_action_panel(role, action, path, args.output_dir / filename, qa)
            mobile_files[action] = filename
        item["mobile_action_files"] = mobile_files
        results.append(item)
    summary = {"schema_version": 1, "review_only": True, "roles": results}
    (args.output_dir / "review-panels.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"CHARACTER_REVIEW_PANELS={len(results)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
