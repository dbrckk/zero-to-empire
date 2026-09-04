#!/usr/bin/env python3
"""Zero -> Empire free sprite generation worker.

Runs unattended in GitHub Actions. It deliberately generates one manifest asset per
run to conserve the free ZeroGPU allowance. The first supported production target
is FX-06. Generated art is staged under art/incoming/final-sprites and is never
marked DONE by this worker; the repository validation/runtime pipeline remains the
gatekeeper.
"""
from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

from gradio_client import Client
from PIL import Image, ImageChops, ImageFilter

ROOT = Path(__file__).resolve().parents[2]
INCOMING = ROOT / "art/incoming/final-sprites"
SPACE = os.getenv("HF_SPACE", "mcp-tools/Z-Image-Turbo")
TOKEN = os.environ.get("HF_TOKEN")


def generate(prompt: str) -> Path:
    kwargs = {"src": SPACE}
    if TOKEN:
        kwargs["hf_token"] = TOKEN
    client = Client(**kwargs)
    result = client.predict(
        prompt=prompt,
        resolution="1024x1024 ( 1:1 )",
        seed=42,
        steps=8,
        shift=3.0,
        random_seed=True,
        api_name="/generate",
    )
    raw = result[0] if isinstance(result, (tuple, list)) else result
    if isinstance(raw, dict):
        raw = raw.get("path") or raw.get("url")
    if not raw:
        raise RuntimeError(f"Generator returned no image: {result!r}")
    return Path(raw)


def black_to_alpha(src: Path) -> Image.Image:
    """Convert an intentionally pure-black FX backdrop into genuine alpha."""
    im = Image.open(src).convert("RGB")
    # Luminance drives alpha; very dark generator noise becomes transparent.
    lum = im.convert("L")
    alpha = lum.point(lambda p: 0 if p < 12 else min(255, int((p - 12) * 1.35)))
    alpha = alpha.filter(ImageFilter.GaussianBlur(0.35))
    rgba = im.convert("RGBA")
    rgba.putalpha(alpha)
    return rgba


def make_fx06(master: Image.Image) -> Image.Image:
    """Derive a deterministic 8-frame 4x2 warm pulse sheet from one clean master."""
    bbox = master.getbbox()
    if not bbox:
        raise RuntimeError("FX-06 master is empty after alpha extraction")
    obj = master.crop(bbox)
    sheet = Image.new("RGBA", (512, 256), (0, 0, 0, 0))
    scales = [0.38, 0.52, 0.68, 0.82, 0.90, 0.78, 0.58, 0.38]
    opacities = [90, 145, 205, 255, 235, 185, 125, 55]
    for i, (scale, opacity) in enumerate(zip(scales, opacities)):
        max_side = 108  # >=10 px safety inside each 128 cell
        factor = min(max_side / obj.width, max_side / obj.height) * scale
        w, h = max(1, round(obj.width * factor)), max(1, round(obj.height * factor))
        frame = obj.resize((w, h), Image.Resampling.LANCZOS)
        a = frame.getchannel("A").point(lambda p, o=opacity: p * o // 255)
        frame.putalpha(a)
        x0, y0 = (i % 4) * 128, (i // 4) * 128
        sheet.alpha_composite(frame, (x0 + (128 - w)//2, y0 + (128 - h)//2))
    return sheet


def validate_fx_sheet(sheet: Image.Image) -> None:
    if sheet.size != (512, 256) or sheet.mode != "RGBA":
        raise RuntimeError("FX sheet contract failed: expected 512x256 RGBA")
    for i in range(8):
        x0, y0 = (i % 4) * 128, (i // 4) * 128
        cell = sheet.crop((x0, y0, x0 + 128, y0 + 128))
        if cell.getbbox() is None:
            raise RuntimeError(f"FX sheet contract failed: empty frame {i}")
        # Required >=4 px transparent padding on all sides.
        a = cell.getchannel("A")
        edges = [a.crop((0,0,128,4)), a.crop((0,124,128,128)), a.crop((0,0,4,128)), a.crop((124,0,128,128))]
        if any(e.getbbox() is not None for e in edges):
            raise RuntimeError(f"FX sheet contract failed: frame {i} violates 4 px padding")


def main() -> int:
    INCOMING.mkdir(parents=True, exist_ok=True)
    target = os.getenv("SPRITE_TARGET", "FX-06").upper()
    if target != "FX-06":
        raise SystemExit(f"Unsupported target for this conservative worker: {target}")
    prompt = (
        "AAA mobile game VFX asset, one single centered warm energy pulse, compact circular "
        "amber gold orange plasma ring with a bright white-gold core, crisp readable silhouette, "
        "premium industrial sci-fi game effect, isolated object only, large empty margin, pure solid "
        "black background, no floor, no smoke, no dust, no debris, no rocks, no character, no text, "
        "no logo, no UI, no border, no frame, no sprite sheet, no multiple objects"
    )
    print(f"Generating {target} with {SPACE}")
    raw = generate(prompt)
    master = black_to_alpha(raw)
    sheet = make_fx06(master)
    validate_fx_sheet(sheet)
    out = INCOMING / "zte_fx_06_final.png"
    sheet.save(out, "PNG", optimize=True)
    print(f"VALIDATED_CANDIDATE={out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
