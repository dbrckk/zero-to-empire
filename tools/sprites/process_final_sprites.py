#!/usr/bin/env python3
"""Technically finalize authored/generated Zero -> Empire sprite candidates.

Input: art/incoming/final-sprites/*.png
Output: app/src/main/res/drawable-nodpi/<same-stem>.webp

Single-sprite candidates are normalized onto a square runtime canvas. Small FX
sprite sheets use their manifest-native 4x2 / 512x256 layout and are validated
cell-by-cell instead of being mistaken for a contact sheet.
"""
from collections import deque
from pathlib import Path
from PIL import Image
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
INCOMING = ROOT / "art/incoming/final-sprites"
OUT = ROOT / "app/src/main/res/drawable-nodpi"
MIN_DIM = 512
MAX_DIM = 2048
MIN_PADDING_RATIO = 0.04
TARGET_PADDING_RATIO = 0.08
ALPHA_CLEAN_THRESHOLD = 8
MAX_ALPHA_COVERAGE = 0.70
MAX_MAJOR_COMPONENTS = 1
COARSE_SIZE = 128
FX_SHEET_RE = re.compile(r"^zte_fx_(?:0[0-9]|1[0-7])_final$")
FX_SHEET_SIZE = (512, 256)
FX_CELL = 128
FX_FRAMES = 8
FX_PADDING = 4


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def alpha_coverage(alpha: Image.Image) -> float:
    hist = alpha.histogram()
    visible = sum(hist[ALPHA_CLEAN_THRESHOLD:])
    return visible / float(alpha.width * alpha.height)


def major_components(alpha: Image.Image) -> int:
    """Count large disconnected visible regions on a coarse alpha mask."""
    small = alpha.resize((COARSE_SIZE, COARSE_SIZE), Image.Resampling.BILINEAR)
    px = small.load()
    seen = set()
    major = 0
    min_area = int(COARSE_SIZE * COARSE_SIZE * 0.012)

    for y in range(COARSE_SIZE):
        for x in range(COARSE_SIZE):
            if (x, y) in seen or px[x, y] < 32:
                continue
            q = deque([(x, y)])
            seen.add((x, y))
            area = 0
            while q:
                cx, cy = q.popleft()
                area += 1
                for nx, ny in ((cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1), (cx, cy - 1), (cx, cy + 1)):
                    if 0 <= nx < COARSE_SIZE and 0 <= ny < COARSE_SIZE and (nx, ny) not in seen:
                        if px[nx, ny] >= 32:
                            seen.add((nx, ny))
                            q.append((nx, ny))
            if area >= min_area:
                major += 1
    return major


def clean_alpha(im: Image.Image) -> Image.Image:
    rgba = im.convert("RGBA")
    alpha = rgba.getchannel("A")
    alpha = alpha.point(lambda a: 0 if a < ALPHA_CLEAN_THRESHOLD else a)
    rgba.putalpha(alpha)
    return rgba


def validate_fx_sheet(path: Path, im: Image.Image) -> None:
    if im.size != FX_SHEET_SIZE:
        fail(f"{path.name}: FX sheet must be 512x256 (4x2 of 128x128), got {im.width}x{im.height}")

    alpha = im.getchannel("A")
    lo, hi = alpha.getextrema()
    if hi == 0:
        fail(f"{path.name}: fully transparent FX sheet")
    if lo == 255:
        fail(f"{path.name}: no transparent pixels; likely baked background")

    for i in range(FX_FRAMES):
        x0 = (i % 4) * FX_CELL
        y0 = (i // 4) * FX_CELL
        cell_a = alpha.crop((x0, y0, x0 + FX_CELL, y0 + FX_CELL))
        if cell_a.getbbox() is None:
            fail(f"{path.name}: FX frame {i} is empty")
        edges = (
            cell_a.crop((0, 0, FX_CELL, FX_PADDING)),
            cell_a.crop((0, FX_CELL - FX_PADDING, FX_CELL, FX_CELL)),
            cell_a.crop((0, 0, FX_PADDING, FX_CELL)),
            cell_a.crop((FX_CELL - FX_PADDING, 0, FX_CELL, FX_CELL)),
        )
        if any(edge.getbbox() is not None for edge in edges):
            fail(f"{path.name}: FX frame {i} violates >=4 px transparent padding")

    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"{path.stem}.webp"
    im.save(out, "WEBP", lossless=True, method=6, exact=True)
    size_kib = out.stat().st_size / 1024.0
    print(
        f"OK {path.name} -> {out.relative_to(ROOT)} 512x256 "
        f"fx_frames=8 cell=128 padding>=4px coverage={alpha_coverage(alpha):.1%} size={size_kib:.1f}KiB"
    )


def process_single_sprite(path: Path, im: Image.Image) -> None:
    w, h = im.size
    if min(w, h) < MIN_DIM:
        fail(f"{path.name}: too small ({w}x{h}); minimum side is {MIN_DIM}px")

    alpha = im.getchannel("A")
    lo, hi = alpha.getextrema()
    if hi == 0:
        fail(f"{path.name}: fully transparent")
    if lo == 255:
        fail(f"{path.name}: no transparent pixels; likely baked background")

    coverage = alpha_coverage(alpha)
    if coverage > MAX_ALPHA_COVERAGE:
        fail(f"{path.name}: visible alpha covers {coverage:.1%}; likely baked background or sheet")

    components = major_components(alpha)
    if components > MAX_MAJOR_COMPONENTS:
        fail(f"{path.name}: {components} major disconnected subjects; submit one sprite per file")

    bbox = alpha.getbbox()
    if not bbox:
        fail(f"{path.name}: no visible subject after alpha cleanup")
    x0, y0, x1, y1 = bbox
    required_x = max(8, int(w * MIN_PADDING_RATIO))
    required_y = max(8, int(h * MIN_PADDING_RATIO))
    if x0 < required_x or y0 < required_y or (w - x1) < required_x or (h - y1) < required_y:
        fail(f"{path.name}: insufficient transparent safety padding")

    subject = im.crop(bbox)
    sw, sh = subject.size
    subject_max = max(sw, sh)
    target_pad = max(32, int(subject_max * TARGET_PADDING_RATIO))
    canvas_side = min(MAX_DIM, max(MIN_DIM, subject_max + 2 * target_pad))

    max_subject = int(canvas_side * 0.84)
    if max(sw, sh) > max_subject:
        scale = max_subject / max(sw, sh)
        subject = subject.resize(
            (max(1, round(sw * scale)), max(1, round(sh * scale))),
            Image.Resampling.LANCZOS,
        )
        sw, sh = subject.size

    canvas = Image.new("RGBA", (canvas_side, canvas_side), (0, 0, 0, 0))
    x = (canvas_side - sw) // 2
    bottom_pad = max(24, int(canvas_side * TARGET_PADDING_RATIO))
    y = max(0, canvas_side - bottom_pad - sh)
    canvas.alpha_composite(subject, (x, y))

    out_alpha = canvas.getchannel("A")
    if any(out_alpha.getpixel(pt) != 0 for pt in ((0, 0), (canvas_side - 1, 0), (0, canvas_side - 1), (canvas_side - 1, canvas_side - 1))):
        fail(f"{path.name}: non-transparent runtime corner after normalization")

    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"{path.stem}.webp"
    canvas.save(out, "WEBP", lossless=True, method=6, exact=True)

    size_kib = out.stat().st_size / 1024.0
    print(
        f"OK {path.name} -> {out.relative_to(ROOT)} "
        f"{canvas_side}x{canvas_side} coverage={coverage:.1%} components={components} size={size_kib:.1f}KiB"
    )


def process(path: Path) -> None:
    if not path.stem.endswith("_final"):
        fail(f"{path.name}: filename must end in _final.png")

    im = clean_alpha(Image.open(path))
    if FX_SHEET_RE.fullmatch(path.stem):
        validate_fx_sheet(path, im)
    else:
        process_single_sprite(path, im)


def main() -> None:
    files = sorted(INCOMING.glob("*.png")) if INCOMING.exists() else []
    if not files:
        print("No PNG candidates; nothing to process.")
        return
    for path in files:
        process(path)


if __name__ == "__main__":
    main()
