#!/usr/bin/env python3
"""Instant deterministic small-FX factory for Zero -> Empire.

Generates FX-00..FX-03 as native 8-frame 4x2 transparent sheets without GPU.
Supports one target via SPRITE_TARGET or a comma-separated batch via
SPRITE_TARGETS. Batch mode avoids repeated runner/process startup overhead.
"""
from __future__ import annotations

import math
import os
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[2]
INCOMING = ROOT / "art/incoming/final-sprites"
CELL = 128
COLS = 4
FRAMES = 8
SIZE = (512, 256)
PAD = 6
SUPPORTED = ("FX-00", "FX-01", "FX-02", "FX-03")


def layer() -> Image.Image:
    return Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))


def composite_glow(base: Image.Image, glow: Image.Image, radius: float) -> None:
    blurred = glow.filter(ImageFilter.GaussianBlur(radius))
    base.alpha_composite(blurred)
    base.alpha_composite(glow)


def sparks(frame: int) -> Image.Image:
    rng = random.Random(7000 + frame)
    im = layer()
    glow = layer()
    d = ImageDraw.Draw(glow)
    cx, cy = 64, 69
    phase = frame / 7.0
    core_r = max(2, round(3 + 4 * math.sin(math.pi * phase)))
    d.ellipse((cx-core_r, cy-core_r, cx+core_r, cy+core_r), fill=(255, 246, 190, 245))
    count = 8 + min(frame, 4) * 2
    reach = 18 + frame * 5
    for i in range(count):
        a = (2 * math.pi * i / count) + rng.uniform(-0.16, 0.16)
        r0 = 6 + rng.uniform(0, 6)
        r1 = reach * rng.uniform(0.55, 1.0)
        x0, y0 = cx + math.cos(a)*r0, cy + math.sin(a)*r0
        x1, y1 = cx + math.cos(a)*r1, cy + math.sin(a)*r1
        col = (255, rng.randint(155, 225), rng.randint(35, 80), max(35, 245 - frame*24))
        d.line((x0, y0, x1, y1), fill=col, width=2 if i % 3 else 3)
        rr = 1 if i % 2 else 2
        d.ellipse((x1-rr, y1-rr, x1+rr, y1+rr), fill=(255, 224, 120, col[3]))
    composite_glow(im, glow, 4.2)
    return im


def flame(frame: int, plasma: bool) -> Image.Image:
    rng = random.Random((9200 if plasma else 8100) + frame)
    im = layer()
    glow = layer()
    g = ImageDraw.Draw(glow)
    phase = frame / 7.0
    cx = 64 + math.sin(frame * 1.7) * (2.5 if plasma else 1.8)
    base_y = 94
    height = (78 if plasma else 58) * (0.82 + 0.18 * math.sin(math.pi * (phase + .15)))
    width = 30 if plasma else 22
    for j in range(11 if plasma else 8):
        t = j / (10 if plasma else 7)
        y = base_y - t * height
        wobble = math.sin(t * 7.0 + frame * .9) * (5.5 * t) + rng.uniform(-2.5, 2.5)
        rx = max(3, width * (1 - .62*t) * rng.uniform(.72, 1.08))
        ry = max(4, (14 if plasma else 11) * (1 - .30*t) * rng.uniform(.8, 1.2))
        if plasma and j % 4 == 0:
            c = (110, 230, 255, 185)
        elif t < .42:
            c = (255, 118, 18, 230)
        elif t < .78:
            c = (255, 194, 42, 235)
        else:
            c = (255, 245, 205, 230)
        g.ellipse((cx+wobble-rx, y-ry, cx+wobble+rx, y+ry), fill=c)
    core_w = 13 if plasma else 9
    core_h = 24 if plasma else 17
    g.ellipse((cx-core_w, base_y-core_h, cx+core_w, base_y+2), fill=(255, 252, 224, 245))
    composite_glow(im, glow, 5.0 if plasma else 4.0)
    return im


def smoke(frame: int) -> Image.Image:
    rng = random.Random(10300 + frame)
    im = layer()
    soft = layer()
    d = ImageDraw.Draw(soft)
    p = frame / 7.0
    cx = 64 + math.sin(frame * 0.8) * 3
    cy = 80 - 22 * p
    count = 7 + frame
    for i in range(count):
        a = rng.uniform(0, math.tau)
        radius = rng.uniform(5, 18 + 9*p)
        x = cx + math.cos(a) * radius * rng.uniform(.3, 1.0)
        y = cy + math.sin(a) * radius * .58
        rr = rng.uniform(8, 16) * (0.72 + .6*p)
        alpha = int((155 - frame*11) * rng.uniform(.65, 1.0))
        gray = rng.randint(105, 148)
        d.ellipse((x-rr, y-rr*.72, x+rr, y+rr*.72), fill=(gray, gray+4, gray+8, max(34, alpha)))
    blurred = soft.filter(ImageFilter.GaussianBlur(4.1 + p*2.2))
    im.alpha_composite(blurred)
    im.alpha_composite(soft.filter(ImageFilter.GaussianBlur(1.2)))
    return im


def ensure_padding(im: Image.Image) -> Image.Image:
    bbox = im.getbbox()
    if not bbox:
        raise RuntimeError("generated frame is empty")
    left, top, right, bottom = bbox
    if left < PAD or top < PAD or right > CELL-PAD or bottom > CELL-PAD:
        crop = im.crop(bbox)
        max_side = CELL - 2*PAD
        scale = min(max_side / crop.width, max_side / crop.height, 1.0)
        crop = crop.resize((max(1, round(crop.width*scale)), max(1, round(crop.height*scale))), Image.Resampling.LANCZOS)
        out = layer()
        out.alpha_composite(crop, ((CELL-crop.width)//2, (CELL-crop.height)//2))
        return out
    return im


def validate(sheet: Image.Image) -> None:
    if sheet.size != SIZE or sheet.mode != "RGBA":
        raise RuntimeError("expected 512x256 RGBA")
    for i in range(FRAMES):
        x0, y0 = (i % COLS)*CELL, (i // COLS)*CELL
        cell = sheet.crop((x0, y0, x0+CELL, y0+CELL))
        if cell.getbbox() is None:
            raise RuntimeError(f"empty frame {i}")
        a = cell.getchannel("A")
        edges = [a.crop((0,0,CELL,4)), a.crop((0,CELL-4,CELL,CELL)), a.crop((0,0,4,CELL)), a.crop((CELL-4,0,CELL,CELL))]
        if any(e.getbbox() is not None for e in edges):
            raise RuntimeError(f"frame {i} violates >=4px transparent padding")


def build(target: str) -> Image.Image:
    makers = {
        "FX-00": sparks,
        "FX-01": lambda i: flame(i, False),
        "FX-02": lambda i: flame(i, True),
        "FX-03": smoke,
    }
    if target not in makers:
        raise SystemExit(f"unsupported procedural target: {target}")
    sheet = Image.new("RGBA", SIZE, (0,0,0,0))
    for i in range(FRAMES):
        f = ensure_padding(makers[target](i))
        sheet.alpha_composite(f, ((i % COLS)*CELL, (i // COLS)*CELL))
    validate(sheet)
    return sheet


def targets_from_env() -> list[str]:
    raw = os.getenv("SPRITE_TARGETS", "").strip()
    if raw:
        targets = [part.strip().upper() for part in raw.split(",") if part.strip()]
    else:
        targets = [os.getenv("SPRITE_TARGET", "FX-03").upper()]
    invalid = [target for target in targets if target not in SUPPORTED]
    if invalid:
        raise SystemExit(f"unsupported procedural targets: {', '.join(invalid)}")
    return list(dict.fromkeys(targets))


def main() -> int:
    INCOMING.mkdir(parents=True, exist_ok=True)
    targets = targets_from_env()
    for target in targets:
        num = target.split("-")[-1]
        out = INCOMING / f"zte_fx_{num}_final.png"
        if out.is_file() and out.stat().st_size > 0:
            print(f"PROCEDURAL_REUSE={out.relative_to(ROOT)}")
            continue
        build(target).save(out, "PNG", optimize=True)
        print(f"PROCEDURAL_VALIDATED={out.relative_to(ROOT)}")
    print(f"PROCEDURAL_BATCH_COUNT={len(targets)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
