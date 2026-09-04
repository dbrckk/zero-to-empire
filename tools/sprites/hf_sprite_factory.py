#!/usr/bin/env python3
"""Zero -> Empire free sprite generation worker."""
from __future__ import annotations

import json
import os
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
    payload = {"data": [prompt, "1024x1024 ( 1:1 )", 42, 8, 3.0, True]}
    post = urllib.request.Request(f"{SPACE_URL}/gradio_api/call/generate", data=json.dumps(payload).encode(), headers=_headers(json_body=True), method="POST")
    response = json.loads(_request(post, timeout=60).decode())
    event_id = response.get("event_id")
    if not event_id:
        raise RuntimeError(f"Generator returned no event_id: {response!r}")
    get = urllib.request.Request(f"{SPACE_URL}/gradio_api/call/generate/{event_id}", headers=_headers(), method="GET")
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
        raise RuntimeError("Generator returned no downloadable image URL")
    suffix = Path(image_url.split("?", 1)[0]).suffix.lower()
    if suffix not in {".png", ".jpg", ".jpeg", ".webp"}:
        suffix = ".img"
    tmp = ROOT / ".sprite_factory_download"
    tmp.mkdir(exist_ok=True)
    out = tmp / f"hf_master{suffix}"
    out.write_bytes(_request(urllib.request.Request(image_url, headers=_headers(), method="GET"), timeout=120))
    if out.stat().st_size < 1024:
        raise RuntimeError("Downloaded generator image is unexpectedly small")
    with Image.open(out) as check:
        check.verify()
    return out


def black_to_alpha(src: Path) -> Image.Image:
    im = Image.open(src).convert("RGB")
    lum = im.convert("L")
    alpha = lum.point(lambda p: 0 if p < 12 else min(255, int((p - 12) * 1.35))).filter(ImageFilter.GaussianBlur(0.35))
    rgba = im.convert("RGBA")
    rgba.putalpha(alpha)
    return rgba


def _fit_frame(obj: Image.Image, target_side: int, scale: float, opacity: int, rotation: float = 0.0) -> Image.Image:
    factor = min(target_side / obj.width, target_side / obj.height) * scale
    frame = obj.resize((max(1, round(obj.width * factor)), max(1, round(obj.height * factor))), Image.Resampling.LANCZOS)
    if rotation:
        frame = frame.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True)
        if max(frame.size) > target_side:
            f = target_side / max(frame.size)
            frame = frame.resize((max(1, round(frame.width * f)), max(1, round(frame.height * f))), Image.Resampling.LANCZOS)
    frame.putalpha(frame.getchannel("A").point(lambda p, o=opacity: p * o // 255))
    return frame


def make_energy_pulse(master: Image.Image, label: str) -> Image.Image:
    bbox = master.getbbox()
    if not bbox:
        raise RuntimeError(f"{label} master is empty after alpha extraction")
    obj = master.crop(bbox)
    sheet = Image.new("RGBA", (512, 256), (0, 0, 0, 0))
    for i, (scale, opacity) in enumerate(zip([.38,.52,.68,.82,.90,.78,.58,.38], [90,145,205,255,235,185,125,55])):
        frame = _fit_frame(obj, 108, scale, opacity)
        x0, y0 = (i % 4) * 128, (i // 4) * 128
        sheet.alpha_composite(frame, (x0 + (128-frame.width)//2, y0 + (128-frame.height)//2))
    return sheet


def make_fx04(master: Image.Image) -> Image.Image:
    bbox = master.getbbox()
    if not bbox:
        raise RuntimeError("FX-04 master is empty after alpha extraction")
    obj = master.crop(bbox)
    sheet = Image.new("RGBA", (512, 256), (0,0,0,0))
    scales = [.34,.46,.60,.72,.82,.90,.96,1.0]
    opacities = [80,135,195,235,220,170,110,50]
    rotations = [-2,1,-1,2,-2,1,-1,0]
    y_offsets = [12,8,4,0,-4,-8,-11,-14]
    for i, values in enumerate(zip(scales, opacities, rotations, y_offsets)):
        scale, opacity, rotation, yoff = values
        frame = _fit_frame(obj, 100, scale, opacity, rotation)
        x0, y0 = (i % 4)*128, (i // 4)*128
        x = x0 + (128-frame.width)//2
        y = max(y0+6, min(y0+(128-frame.height)//2+yoff, y0+122-frame.height))
        sheet.alpha_composite(frame, (x,y))
    return sheet


def make_fx05(master): return make_energy_pulse(master, "FX-05")
def make_fx06(master): return make_energy_pulse(master, "FX-06")


def make_fx07(master: Image.Image) -> Image.Image:
    bbox = master.getbbox()
    if not bbox:
        raise RuntimeError("FX-07 master is empty after alpha extraction")
    obj = master.crop(bbox)
    sheet = Image.new("RGBA", (512,256), (0,0,0,0))
    for i, values in enumerate(zip([.28,.42,.58,.72,.84,.90,.94,.96], [95,155,220,255,220,165,105,50], [0,-3,3,-2,2,-1,1,0], [10,7,4,1,-2,-4,-6,-8])):
        scale, opacity, rotation, yoff = values
        frame = _fit_frame(obj, 104, scale, opacity, rotation)
        x0, y0 = (i%4)*128, (i//4)*128
        x = x0+(128-frame.width)//2
        y = max(y0+6, min(y0+(128-frame.height)//2+yoff, y0+122-frame.height))
        sheet.alpha_composite(frame,(x,y))
    return sheet


def validate_fx_sheet(sheet: Image.Image) -> None:
    if sheet.size != (512,256) or sheet.mode != "RGBA": raise RuntimeError("FX sheet contract failed: expected 512x256 RGBA")
    lo, hi = sheet.getchannel("A").getextrema()
    if hi == 0 or lo == 255: raise RuntimeError("FX sheet transparency contract failed")
    for i in range(8):
        x0,y0=(i%4)*128,(i//4)*128
        cell=sheet.crop((x0,y0,x0+128,y0+128))
        if cell.getbbox() is None: raise RuntimeError(f"FX sheet contract failed: empty frame {i}")
        a=cell.getchannel("A")
        edges=[a.crop((0,0,128,4)),a.crop((0,124,128,128)),a.crop((0,0,4,128)),a.crop((124,0,128,128))]
        if any(edge.getbbox() is not None for edge in edges): raise RuntimeError(f"FX sheet contract failed: frame {i} violates >=4 px padding")


def main() -> int:
    if not TOKEN: raise SystemExit("HF_TOKEN is required")
    INCOMING.mkdir(parents=True, exist_ok=True)
    target=os.getenv("SPRITE_TARGET","FX-04").upper()
    specs={
        "FX-04": ("AAA mobile game VFX asset, one single centered industrial steam vent plume, compact clean white silver cool-gray pressurized steam jet rising upward, soft turbulent vapor with crisp readable silhouette at tiny mobile size, premium industrial game effect, isolated effect only, large empty margin, pure solid black background, no pipe, no machine, no floor, no building, no fire, no smoke soot, no character, no text, no logo, no UI, no border, no frame, no sprite sheet, no multiple objects", "zte_fx_04_final.png", make_fx04),
        "FX-05": ("AAA mobile game VFX asset, one single centered cyan energy pulse, compact circular electric cyan blue plasma ring with a bright white-cyan core, crisp readable silhouette, premium industrial sci-fi game effect, isolated object only, large empty margin, pure solid black background, no floor, no smoke, no dust, no debris, no rocks, no character, no text, no logo, no UI, no border, no frame, no sprite sheet, no multiple objects", "zte_fx_05_final.png", make_fx05),
        "FX-06": ("AAA mobile game VFX asset, one single centered warm energy pulse, compact circular amber gold orange plasma ring with a bright white-gold core, crisp readable silhouette, premium industrial sci-fi game effect, isolated object only, large empty margin, pure solid black background, no floor, no smoke, no dust, no debris, no rocks, no character, no text, no logo, no UI, no border, no frame, no sprite sheet, no multiple objects", "zte_fx_06_final.png", make_fx06),
        "FX-07": ("AAA mobile game VFX asset, one single centered construction dust and debris burst, compact warm tan ochre dust cloud with a few small bright stone and metal fragments, energetic outward impact shape, crisp readable silhouette at tiny mobile size, premium industrial game effect, isolated effect only, large empty margin, pure solid black background, no floor, no building, no tools, no character, no text, no logo, no UI, no border, no frame, no sprite sheet, no multiple objects", "zte_fx_07_final.png", make_fx07),
    }
    if target not in specs: raise SystemExit(f"Unsupported target for this conservative worker: {target}")
    prompt, output_name, maker=specs[target]
    print(f"Generating {target} through {SPACE_URL}")
    sheet=maker(black_to_alpha(generate(prompt)))
    validate_fx_sheet(sheet)
    out=INCOMING/output_name
    sheet.save(out,"PNG",optimize=True)
    print(f"VALIDATED_CANDIDATE={out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
