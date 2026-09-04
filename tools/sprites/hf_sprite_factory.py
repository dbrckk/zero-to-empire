#!/usr/bin/env python3
"""Zero -> Empire free sprite generation worker.

Runs unattended in GitHub Actions and generates at most one asset per run to
conserve the free ZeroGPU allowance. Generated art is technically validated
before it is staged under art/incoming/final-sprites. The separate repository
finalizer/runtime/CI gates remain authoritative; this worker never marks DONE.
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[2]
INCOMING = ROOT / "art/incoming/final-sprites"
SPACE_URL = os.getenv("HF_SPACE_URL", "https://mcp-tools-z-image-turbo.hf.space").rstrip("/")
TOKEN = os.environ.get("HF_TOKEN", "").strip()


def _headers(*, json_body: bool = False) -> dict[str, str]:
    headers = {"User-Agent": "zero-to-empire-sprite-factory/1.0"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    if json_body:
        headers["Content-Type"] = "application/json"
    return headers


def _request(req: urllib.request.Request, timeout: int = 180) -> bytes:
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        raise RuntimeError(f"HTTP {exc.code} from Hugging Face Space: {body[:800]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Hugging Face Space request failed: {exc}") from exc


def generate(prompt: str) -> Path:
    """Call the proven Gradio queue HTTP API and download the returned FileData URL."""
    payload = {
        "data": [
            prompt,
            "1024x1024 ( 1:1 )",
            42,
            8,
            3.0,
            True,
        ]
    }
    post = urllib.request.Request(
        f"{SPACE_URL}/gradio_api/call/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers=_headers(json_body=True),
        method="POST",
    )
    response = json.loads(_request(post, timeout=60).decode("utf-8"))
    event_id = response.get("event_id")
    if not event_id:
        raise RuntimeError(f"Generator returned no event_id: {response!r}")

    get = urllib.request.Request(
        f"{SPACE_URL}/gradio_api/call/generate/{event_id}",
        headers=_headers(),
        method="GET",
    )
    sse = _request(get, timeout=240).decode("utf-8", "replace")
    complete_data = None
    current_event = None
    for line in sse.splitlines():
        if line.startswith("event:"):
            current_event = line.split(":", 1)[1].strip()
        elif line.startswith("data:") and current_event == "complete":
            complete_data = json.loads(line.split(":", 1)[1].strip())
            break
    if complete_data is None:
        raise RuntimeError(f"Generation did not complete successfully. SSE tail: {sse[-1200:]}")

    def find_url(value):
        if isinstance(value, dict):
            url = value.get("url")
            if isinstance(url, str) and url.startswith("http"):
                return url
            for child in value.values():
                found = find_url(child)
                if found:
                    return found
        elif isinstance(value, list):
            for child in value:
                found = find_url(child)
                if found:
                    return found
        return None

    image_url = find_url(complete_data)
    if not image_url:
        raise RuntimeError(f"Generator returned no downloadable image URL: {complete_data!r}")

    suffix = Path(image_url.split("?", 1)[0]).suffix.lower()
    if suffix not in {".png", ".jpg", ".jpeg", ".webp"}:
        suffix = ".img"
    tmp = ROOT / ".sprite_factory_download"
    tmp.mkdir(exist_ok=True)
    out = tmp / f"hf_master{suffix}"
    download = urllib.request.Request(image_url, headers=_headers(), method="GET")
    out.write_bytes(_request(download, timeout=120))
    if out.stat().st_size < 1024:
        raise RuntimeError("Downloaded generator image is unexpectedly small")
    # Pillow verifies the real format regardless of extension.
    with Image.open(out) as check:
        check.verify()
    return out


def black_to_alpha(src: Path) -> Image.Image:
    """Convert an intentionally pure-black FX backdrop into genuine alpha."""
    im = Image.open(src).convert("RGB")
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
        max_side = 108
        factor = min(max_side / obj.width, max_side / obj.height) * scale
        w = max(1, round(obj.width * factor))
        h = max(1, round(obj.height * factor))
        frame = obj.resize((w, h), Image.Resampling.LANCZOS)
        a = frame.getchannel("A").point(lambda p, o=opacity: p * o // 255)
        frame.putalpha(a)
        x0, y0 = (i % 4) * 128, (i // 4) * 128
        sheet.alpha_composite(frame, (x0 + (128 - w) // 2, y0 + (128 - h) // 2))
    return sheet


def validate_fx_sheet(sheet: Image.Image) -> None:
    if sheet.size != (512, 256) or sheet.mode != "RGBA":
        raise RuntimeError("FX sheet contract failed: expected 512x256 RGBA")
    alpha = sheet.getchannel("A")
    lo, hi = alpha.getextrema()
    if hi == 0:
        raise RuntimeError("FX sheet contract failed: fully transparent")
    if lo == 255:
        raise RuntimeError("FX sheet contract failed: no transparent pixels")
    for i in range(8):
        x0, y0 = (i % 4) * 128, (i // 4) * 128
        cell = sheet.crop((x0, y0, x0 + 128, y0 + 128))
        if cell.getbbox() is None:
            raise RuntimeError(f"FX sheet contract failed: empty frame {i}")
        a = cell.getchannel("A")
        edges = [
            a.crop((0, 0, 128, 4)),
            a.crop((0, 124, 128, 128)),
            a.crop((0, 0, 4, 128)),
            a.crop((124, 0, 128, 128)),
        ]
        if any(edge.getbbox() is not None for edge in edges):
            raise RuntimeError(f"FX sheet contract failed: frame {i} violates >=4 px padding")


def main() -> int:
    if not TOKEN:
        raise SystemExit("HF_TOKEN is required")
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
    print(f"Generating {target} through {SPACE_URL}")
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
