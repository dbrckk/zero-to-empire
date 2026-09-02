#!/usr/bin/env python3
"""Validate and normalize candidate Zero -> Empire final sprites.

Input: art/incoming/final-sprites/*.png
Output: app/src/main/res/drawable-nodpi/<same-stem>.webp

This pipeline deliberately fails closed. Processing never makes artwork 'AAA'; it
only performs deterministic technical gates needed before an authored image can
be considered a runtime candidate.
"""
from pathlib import Path
from PIL import Image, ImageChops
import sys

ROOT = Path(__file__).resolve().parents[2]
INCOMING = ROOT / "art/incoming/final-sprites"
OUT = ROOT / "app/src/main/res/drawable-nodpi"
MIN_DIM = 512
MAX_DIM = 2048
PADDING_RATIO = 0.04


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def process(path: Path) -> None:
    im = Image.open(path).convert("RGBA")
    w, h = im.size
    if min(w, h) < MIN_DIM:
        fail(f"{path.name}: too small ({w}x{h}); minimum side is {MIN_DIM}px")
    alpha = im.getchannel("A")
    lo, hi = alpha.getextrema()
    if lo == 255:
        fail(f"{path.name}: no transparent pixels; likely baked background")
    bbox = alpha.getbbox()
    if not bbox:
        fail(f"{path.name}: fully transparent")
    x0, y0, x1, y1 = bbox
    required_x = max(8, int(w * PADDING_RATIO))
    required_y = max(8, int(h * PADDING_RATIO))
    if x0 < required_x or y0 < required_y or (w - x1) < required_x or (h - y1) < required_y:
        fail(f"{path.name}: insufficient transparent safety padding")

    # Crop to alpha bounds, then place on a square transparent runtime canvas.
    subject = im.crop(bbox)
    sw, sh = subject.size
    canvas_side = min(MAX_DIM, max(MIN_DIM, max(sw, sh) + 2 * max(32, int(max(sw, sh) * 0.08))))
    if max(sw, sh) > canvas_side:
        scale = canvas_side / max(sw, sh) * 0.84
        subject = subject.resize((max(1, int(sw * scale)), max(1, int(sh * scale))), Image.Resampling.LANCZOS)
        sw, sh = subject.size
    canvas = Image.new("RGBA", (canvas_side, canvas_side), (0, 0, 0, 0))
    # Bottom-center footprint bias: leave slightly more breathing room above.
    x = (canvas_side - sw) // 2
    bottom_pad = max(24, int(canvas_side * 0.08))
    y = max(0, canvas_side - bottom_pad - sh)
    canvas.alpha_composite(subject, (x, y))

    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"{path.stem}.webp"
    canvas.save(out, "WEBP", lossless=True, method=6)
    print(f"OK {path.name} -> {out.relative_to(ROOT)} {canvas_side}x{canvas_side}")


def main() -> None:
    files = sorted(INCOMING.glob("*.png")) if INCOMING.exists() else []
    if not files:
        fail("no PNG candidates in art/incoming/final-sprites")
    for path in files:
        process(path)


if __name__ == "__main__":
    main()
