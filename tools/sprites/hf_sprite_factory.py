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
    headers = {"User-Agent": "zero-to-empire-sprite-factory/2.0"}
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


def _animated_sheet(master: Image.Image, *, label: str, target_side: int, scales, opacities, rotations, y_offsets) -> Image.Image:
    bbox = master.getbbox()
    if not bbox:
        raise RuntimeError(f"{label} master is empty after alpha extraction")
    obj = master.crop(bbox)
    sheet = Image.new("RGBA", (512, 256), (0, 0, 0, 0))
    for i, (scale, opacity, rotation, yoff) in enumerate(zip(scales, opacities, rotations, y_offsets)):
        frame = _fit_frame(obj, target_side, scale, opacity, rotation)
        x0, y0 = (i % 4) * 128, (i // 4) * 128
        x = x0 + (128 - frame.width) // 2
        y = max(y0 + 6, min(y0 + (128 - frame.height) // 2 + yoff, y0 + 122 - frame.height))
        sheet.alpha_composite(frame, (x, y))
    return sheet


def make_fx00(master):
    return _animated_sheet(master, label="FX-00", target_side=106, scales=[.36,.50,.70,.92,1.0,.82,.58,.34], opacities=[75,130,210,255,230,165,95,40], rotations=[-8,5,-4,3,-2,2,-1,0], y_offsets=[6,4,2,0,-2,-4,-6,-8])


def make_fx01(master):
    return _animated_sheet(master, label="FX-01", target_side=96, scales=[.48,.62,.76,.90,1.0,.92,.76,.56], opacities=[110,165,220,255,240,200,140,70], rotations=[-2,2,-1,1,-2,2,-1,0], y_offsets=[8,5,2,0,-2,-4,-5,-6])


def make_fx02(master):
    return _animated_sheet(master, label="FX-02", target_side=108, scales=[.44,.58,.72,.88,1.0,.94,.78,.60], opacities=[105,160,215,255,245,205,145,75], rotations=[-3,2,-2,2,-1,1,-1,0], y_offsets=[10,7,4,1,-2,-5,-7,-9])


def make_fx03(master):
    return _animated_sheet(master, label="FX-03", target_side=100, scales=[.30,.42,.58,.72,.84,.92,.98,1.0], opacities=[70,125,185,230,215,165,105,45], rotations=[-2,1,-1,2,-2,1,-1,0], y_offsets=[12,9,5,1,-3,-7,-10,-13])


def make_fx04(master):
    return _animated_sheet(master, label="FX-04", target_side=100, scales=[.34,.46,.60,.72,.82,.90,.96,1.0], opacities=[80,135,195,235,220,170,110,50], rotations=[-2,1,-1,2,-2,1,-1,0], y_offsets=[12,8,4,0,-4,-8,-11,-14])


def make_energy_pulse(master: Image.Image, label: str) -> Image.Image:
    return _animated_sheet(master, label=label, target_side=108, scales=[.38,.52,.68,.82,.90,.78,.58,.38], opacities=[90,145,205,255,235,185,125,55], rotations=[0,0,0,0,0,0,0,0], y_offsets=[0,0,0,0,0,0,0,0])


def make_fx05(master): return make_energy_pulse(master, "FX-05")
def make_fx06(master): return make_energy_pulse(master, "FX-06")


def make_fx07(master):
    return _animated_sheet(master, label="FX-07", target_side=104, scales=[.28,.42,.58,.72,.84,.90,.94,.96], opacities=[95,155,220,255,220,165,105,50], rotations=[0,-3,3,-2,2,-1,1,0], y_offsets=[10,7,4,1,-2,-4,-6,-8])


def validate_fx_sheet(sheet: Image.Image) -> None:
    if sheet.size != (512, 256) or sheet.mode != "RGBA":
        raise RuntimeError("FX sheet contract failed: expected 512x256 RGBA")
    lo, hi = sheet.getchannel("A").getextrema()
    if hi == 0 or lo == 255:
        raise RuntimeError("FX sheet transparency contract failed")
    for i in range(8):
        x0, y0 = (i % 4) * 128, (i // 4) * 128
        cell = sheet.crop((x0, y0, x0 + 128, y0 + 128))
        if cell.getbbox() is None:
            raise RuntimeError(f"FX sheet contract failed: empty frame {i}")
        a = cell.getchannel("A")
        edges = [a.crop((0,0,128,4)), a.crop((0,124,128,128)), a.crop((0,0,4,128)), a.crop((124,0,128,128))]
        if any(edge.getbbox() is not None for edge in edges):
            raise RuntimeError(f"FX sheet contract failed: frame {i} violates >=4 px padding")


SPECS = {
    "FX-00": ("AAA mobile game VFX asset, one single centered warm welding spark burst, bright white-yellow core with short amber orange metal sparks radiating outward, crisp readable silhouette at tiny mobile size, isolated effect only, large empty margin, pure solid black background, no welder, no tool, no machine, no floor, no smoke cloud, no text, no logo, no UI, no border, no frame, no sprite sheet, no multiple objects", "zte_fx_00_final.png", make_fx00),
    "FX-01": ("AAA mobile game VFX asset, one single centered small furnace flame, compact hot orange yellow flame with white-hot center and subtle red edge, crisp readable silhouette at tiny mobile size, isolated effect only, large empty margin, pure solid black background, no furnace, no fuel, no floor, no smoke, no text, no logo, no UI, no border, no frame, no sprite sheet, no multiple objects", "zte_fx_01_final.png", make_fx01),
    "FX-02": ("AAA mobile game VFX asset, one single centered large industrial furnace plasma flame, intense white-hot core with orange amber outer flame and slight cyan plasma accent, tall energetic flame silhouette, crisp readable shape at tiny mobile size, isolated effect only, large empty margin, pure solid black background, no furnace, no machine, no floor, no smoke, no text, no logo, no UI, no border, no frame, no sprite sheet, no multiple objects", "zte_fx_02_final.png", make_fx02),
    "FX-03": ("AAA mobile game VFX asset, one single centered industrial smoke puff, compact medium gray charcoal vapor cloud expanding upward, soft turbulent edges with readable silhouette at tiny mobile size, isolated effect only, large empty margin, pure solid black background, no chimney, no pipe, no machine, no floor, no flame, no text, no logo, no UI, no border, no frame, no sprite sheet, no multiple objects", "zte_fx_03_final.png", make_fx03),
    "FX-04": ("AAA mobile game VFX asset, one single centered industrial steam vent plume, compact clean white silver cool-gray pressurized steam jet rising upward, soft turbulent vapor with crisp readable silhouette at tiny mobile size, premium industrial game effect, isolated effect only, large empty margin, pure solid black background, no pipe, no machine, no floor, no building, no fire, no smoke soot, no character, no text, no logo, no UI, no border, no frame, no sprite sheet, no multiple objects", "zte_fx_04_final.png", make_fx04),
    "FX-05": ("AAA mobile game VFX asset, one single centered cyan energy pulse, compact circular electric cyan blue plasma ring with a bright white-cyan core, crisp readable silhouette, premium industrial sci-fi game effect, isolated object only, large empty margin, pure solid black background, no floor, no smoke, no dust, no debris, no rocks, no character, no text, no logo, no UI, no border, no frame, no sprite sheet, no multiple objects", "zte_fx_05_final.png", make_fx05),
    "FX-06": ("AAA mobile game VFX asset, one single centered warm energy pulse, compact circular amber gold orange plasma ring with a bright white-gold core, crisp readable silhouette, premium industrial sci-fi game effect, isolated object only, large empty margin, pure solid black background, no floor, no smoke, no dust, no debris, no rocks, no character, no text, no logo, no UI, no border, no frame, no sprite sheet, no multiple objects", "zte_fx_06_final.png", make_fx06),
    "FX-07": ("AAA mobile game VFX asset, one single centered construction dust and debris burst, compact warm tan ochre dust cloud with a few small bright stone and metal fragments, energetic outward impact shape, crisp readable silhouette at tiny mobile size, premium industrial game effect, isolated effect only, large empty margin, pure solid black background, no floor, no building, no tools, no character, no text, no logo, no UI, no border, no frame, no sprite sheet, no multiple objects", "zte_fx_07_final.png", make_fx07),
}


def main() -> int:
    if not TOKEN:
        raise SystemExit("HF_TOKEN is required")
    INCOMING.mkdir(parents=True, exist_ok=True)
    target = os.getenv("SPRITE_TARGET", "FX-03").upper()
    if target not in SPECS:
        raise SystemExit(f"Unsupported target for this worker: {target}")
    prompt, output_name, maker = SPECS[target]
    print(f"Generating {target} through {SPACE_URL}")
    sheet = maker(black_to_alpha(generate(prompt)))
    validate_fx_sheet(sheet)
    out = INCOMING / output_name
    sheet.save(out, "PNG", optimize=True)
    print(f"VALIDATED_CANDIDATE={out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
