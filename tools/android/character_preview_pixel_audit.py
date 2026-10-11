#!/usr/bin/env python3
"""Debug-only: prove six TECH action screenshots contain distinct actor pixels.

The gate is deliberately semantic-neutral: changing action text is NOT proof
that the rendered sprite changed. This script crops the real 42dp night
preview by locating its XML caption, outside all action labels/buttons, then
checks that there is a nonempty actor and that each action differs visibly.
It cannot grant strict DONE or visual release approval.
"""
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image

ACTIONS = ("IDLE", "WALK", "WORK", "CARRY", "REPAIR", "CELEBRATE")
LABEL = "NIGHT · 42 dp"
BOUNDS = re.compile(r"^\[(\d+),(\d+)\]\[(\d+),(\d+)\]$")
MIN_VISIBLE_PIXELS = 120
MIN_DIFFERENT_PIXELS = 150
TOLERANCE = 25


def review_crop(folder: Path, action: str, frame_label: str = "") -> tuple[Image.Image, int]:
    # The same real-size crop validator is used by single-action and
    # consecutive-frame Android screenshots, with identical clipping gates.
    suffix = f"-{frame_label}" if frame_label else ""
    xml = folder / f"tech-action-{action}{suffix}.xml"
    shot = folder / f"tech-stage-{action}{suffix}.png"
    root = ET.parse(xml).getroot()
    text_values = [n.attrib.get("text", "") for n in root.iter("node")]
    if f"TECH ACTION: {action}" not in text_values:
        raise ValueError(f"{action}: the selected action is not shown")
    frame_values = [v.split(":", 1)[1].strip() for v in text_values
                    if v.startswith("STAGE FRAME:")]
    if len(frame_values) != 1 or not frame_values[0].isdigit():
        raise ValueError(f"{action}: no unique visible stage frame counter")
    labels = [n for n in root.iter("node") if n.attrib.get("text") == LABEL]
    if len(labels) != 1:
        raise ValueError(f"{action}: real-scale preview is absent or duplicated")
    rect = BOUNDS.fullmatch(labels[0].attrib.get("bounds", ""))
    if not rect:
        raise ValueError(f"{action}: invalid QA caption bounds")
    x0, y0, x1, y1 = map(int, rect.groups())
    height = y1 - y0
    if height < 8 or x1 <= x0:
        raise ValueError(f"{action}: invalid screen density")
    with Image.open(shot) as source:
        rgb = source.convert("RGB")
    # A previously green emulator run had its 42dp actor cropped at the
    # waist by the LazyColumn viewport. The old crop also included the
    # Android navbar, which inflated the non-background pixel count.
    # Prove the NIGHT and DAY preview panes extend below the whole sprite
    # before comparing any action pixels. Coordinates scale with the actual
    # Android caption size, not hard-coded emulator resolution.
    for text, expected in (
        ("NIGHT · 42 dp", (16, 27, 36)),
        ("DAY · 39 dp", (186, 204, 214)),
    ):
        matches = [n for n in root.iter("node")
                   if n.attrib.get("text") == text]
        if len(matches) != 1:
            raise ValueError(f"{action}: missing full-body panel {text}")
        bounds = BOUNDS.fullmatch(matches[0].attrib.get("bounds", ""))
        if not bounds:
            raise ValueError(f"{action}: invalid panel bounds {text}")
        cx0, cy0, cx1, cy1 = map(int, bounds.groups())
        caption_px = cy1 - cy0
        # The avatar is 39-42dp tall beneath this 14sp caption.
        # The pane must still have its native background well below the
        # shoes. A screenshot captured mid-scroll / below the viewport
        # fails, even when it contains the actor's head and shoulders.
        probe_x = cx0 - max(8, round(caption_px * .35))
        probe_y = cy1 + round(caption_px * 3.25)
        if not (0 <= probe_x < rgb.width and 0 <= probe_y < rgb.height - 80):
            raise ValueError(f"{action}: {text} full-body preview is off-screen")
        sample = rgb.getpixel((probe_x, probe_y))
        if max(abs(sample[i] - expected[i]) for i in range(3)) > 18:
            raise ValueError(
                f"{action}: {text} full-body preview is vertically clipped "
                f"(foot-depth={probe_y}, got={sample}, expected={expected})")
    print(f"CHARACTER_PREVIEW_FULL_BODY_PANELS={action}:NIGHT+DAY")
    half_width = round(height * 2.14)
    left, right = (x0 + x1) // 2 - half_width, (x0 + x1) // 2 + half_width
    top, bottom = y1 + 5, y1 + 5 + round(height * 3.45)
    if not (0 <= left < right <= rgb.width and 0 <= top < bottom <= rgb.height):
        raise ValueError(f"{action}: actor pixels are outside the viewport")
    crop = rgb.crop((left, top, right, bottom))
    base = crop.getpixel((0, 0))
    visible = sum(
        max(abs(int(px[i]) - int(base[i])) for i in range(3)) > 30
        for px in crop.getdata()
    )
    if visible < MIN_VISIBLE_PIXELS:
        raise ValueError(f"{action}: background-only QA screenshot ({visible}px)")
    print(f"CHARACTER_PREVIEW_VISIBLE_ACTOR={action}:{visible}")
    return crop, int(frame_values[0])


def audit(folder: Path) -> None:
    renders = [review_crop(folder, action) for action in ACTIONS]
    if len({frame for _, frame in renders}) != 1:
        raise ValueError("Stage clock advanced across comparisons")
    for index, (first, _) in enumerate(renders):
        for other in range(index + 1, len(renders)):
            second = renders[other][0]
            if first.size != second.size:
                raise ValueError("Inconsistent actor crop dimensions")
            different = sum(
                max(abs(int(a[i]) - int(b[i])) for i in range(3)) > TOLERANCE
                for a, b in zip(first.getdata(), second.getdata())
            )
            if different < MIN_DIFFERENT_PIXELS:
                raise ValueError(
                    f"{ACTIONS[index]}/{ACTIONS[other]}: sprites identical "
                    f"or visually indistinguishable ({different}px)")
            print(f"CHARACTER_PREVIEW_DISTINCT_ACTIONS="
                  f"{ACTIONS[index]}/{ACTIONS[other]}:{different}")
    print("CHARACTER_PREVIEW_ALL_SIX_DISTINCT_GAME_SCALE_PASS=1")


def audit_temporal(folder: Path) -> None:
    """Real Android 42dp pixel motion: prove five animated actions change frames.

    This is a technical motion gate only. Plausible weight, foot contact and
    human recognition still require semantic visual review.
    """
    for action in ("WALK", "WORK", "CARRY", "REPAIR", "CELEBRATE"):
        samples = [review_crop(folder, action, f"frame-{i}") for i in range(4)]
        frames = [number for _, number in samples]
        if any(frames[i] != (frames[i - 1] + 1) % 1680
               for i in range(1, len(frames))):
            raise ValueError(f"{action}: frame counter did not advance: {frames}")
        changed_counts = []
        for (before, _), (after, _) in zip(samples, samples[1:]):
            if before.size != after.size:
                raise ValueError(f"{action}: changing Android actor crop")
            changed = sum(
                max(abs(int(a[c]) - int(b[c])) for c in range(3)) > TOLERANCE
                for a, b in zip(before.getdata(), after.getdata())
            )
            changed_counts.append(changed)
        print(f"CHARACTER_PREVIEW_TEMPORAL_MOTION={action}:"
              + ",".join(str(n) for n in changed_counts))
        if min(changed_counts) < 12 or sum(changed_counts) < 90:
            raise ValueError(
                f"{action}: insufficient real-size motion after frame steps "
                f"{changed_counts}")
        print(f"CHARACTER_PREVIEW_TEMPORAL_ACTION_PASS={action}")


if __name__ == "__main__":
    try:
        args = sys.argv[1:]
        if len(args) == 2 and args[0] == "--temporal":
            audit_temporal(Path(args[1]))
        elif len(args) <= 1:
            audit(Path(args[0]) if args else Path("/tmp/zte-character-preview"))
        else:
            raise ValueError("Usage: pixel_audit.py [folder] | --temporal folder")
    except (ValueError, OSError, ET.ParseError) as exc:
        print(f"CHARACTER_PREVIEW_FAIL=action-pixel-audit:{exc}", file=sys.stderr)
        raise SystemExit(1)
