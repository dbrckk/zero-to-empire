#!/usr/bin/env python3
"""Generate one static manifest asset through the free HF Space.

Supported fast GPU lane: buildings, Power Core, vehicles, props and static
terrain/infrastructure modules. Animation sheets remain on dedicated workers.

Exit code 75 means the free GPU quota is exhausted. Batch workflows use this to
stop immediately instead of wasting runner time retrying every remaining asset.
"""
from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from collections import deque
from pathlib import Path

from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
INCOMING = ROOT / "art/incoming/final-sprites"
SPACE_URL = os.getenv("HF_SPACE_URL", "https://mcp-tools-z-image-turbo.hf.space").rstrip("/")
TOKEN = os.environ.get("HF_TOKEN", "").strip()
ASSET_ID = os.environ.get("SPRITE_TARGET", "").strip().upper()
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
SUPPORTED = ("BLD-", "CORE-", "VEH-", "PRP-", "TER-")
TARGET_SIDE = {"BLD": 2048, "CORE": 1536, "VEH": 1536, "PRP": 1024, "TER": 1024}
QUOTA_EXIT = 75


def headers(json_body=False):
    h = {"User-Agent": "zero-to-empire-manifest-factory/1.3"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    if json_body:
        h["Content-Type"] = "application/json"
    return h


def request(req, timeout=240):
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        low = body.lower()
        if exc.code == 429 or any(term in low for term in ("quota", "zerogpu quota", "gpu quota", "daily limit")):
            print(f"FREE_GPU_QUOTA_EXHAUSTED: HTTP {exc.code}")
            raise SystemExit(QUOTA_EXIT) from exc
        raise RuntimeError(f"HF HTTP {exc.code}: {body[:600]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"HF request failed: {exc}") from exc


def manifest_item(asset_id: str):
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if not m:
            continue
        rid, name, desc, runtime, status = [x.strip() for x in m.groups()]
        if rid.upper() == asset_id:
            return rid, name, desc, runtime, status.upper()
    raise SystemExit(f"manifest asset not found: {asset_id}")


def prompt_for(asset_id, name, description):
    kind = asset_id.split("-", 1)[0]
    contract = {
        "BLD": "single complete industrial building, bottom-center visual pivot, clear 2.5D three-quarter 34 degree camera, strong readable silhouette",
        "CORE": "single complete power reactor core on compact cradle, clear 2.5D three-quarter 34 degree camera, iconic readable silhouette",
        "VEH": "single complete vehicle, three-quarter side view, contact-center pivot, readable traffic direction, compact soft contact shadow",
        "PRP": "single complete industrial prop, three-quarter 2.5D view, clear readable silhouette at mobile size",
        "TER": "single seamless terrain or infrastructure module, fixed 2.5D three-quarter 34 degree camera, clean connector geometry and readable edge treatment, no surrounding scene",
    }[kind]
    return (
        "AAA premium mobile strategy game production sprite, " + contract + ", "
        + name + ". " + description + " "
        "Consistent upper-left key light, cool fill, selective warm amber and cyan emissive accents, physically plausible premium materials. "
        "Isolated asset only on pure solid black background with large empty margin. No scene, no floor plane beyond the requested terrain module, no environment backdrop, "
        "no UI, no border, no frame, no watermark, no logo, no letters, no readable text, no numbers, no brand signage, no multiple objects."
    )


def generate(prompt: str) -> Image.Image:
    payload = {"data": [prompt, "1024x1024 ( 1:1 )", 42, 8, 3.0, True]}
    req = urllib.request.Request(f"{SPACE_URL}/gradio_api/call/generate", data=json.dumps(payload).encode(), headers=headers(True), method="POST")
    event_id = json.loads(request(req, 60).decode()).get("event_id")
    if not event_id:
        raise RuntimeError("HF generator returned no event_id")
    req = urllib.request.Request(f"{SPACE_URL}/gradio_api/call/generate/{event_id}", headers=headers(), method="GET")
    sse = request(req, 240).decode("utf-8", "replace")
    data = None
    event = None
    for line in sse.splitlines():
        if line.startswith("event:"):
            event = line.split(":", 1)[1].strip()
        elif line.startswith("data:") and event == "complete":
            data = json.loads(line.split(":", 1)[1].strip())
            break
    if data is None:
        low = sse.lower()
        if any(term in low for term in ("quota", "zerogpu quota", "gpu quota", "daily limit")):
            print("FREE_GPU_QUOTA_EXHAUSTED: SSE response")
            raise SystemExit(QUOTA_EXIT)
        raise RuntimeError("HF generation did not complete")

    def find_url(v):
        if isinstance(v, dict):
            u = v.get("url")
            if isinstance(u, str) and u.startswith("http"):
                return u
            for child in v.values():
                r = find_url(child)
                if r:
                    return r
        if isinstance(v, list):
            for child in v:
                r = find_url(child)
                if r:
                    return r
        return None

    url = find_url(data)
    if not url:
        raise RuntimeError("HF result has no downloadable URL")
    raw = request(urllib.request.Request(url, headers=headers(), method="GET"), 120)
    tmp = ROOT / ".sprite_factory_download"
    tmp.mkdir(exist_ok=True)
    safe_id = re.sub(r"[^A-Za-z0-9_.-]+", "_", ASSET_ID or "static")
    p = tmp / f"{safe_id}.img"
    p.write_bytes(raw)
    return Image.open(p).convert("RGB")


def isolate(im: Image.Image) -> Image.Image:
    lum = im.convert("L")
    alpha = lum.point(lambda p: 0 if p < 10 else min(255, int((p - 10) * 1.42))).filter(ImageFilter.GaussianBlur(.3))
    rgba = im.convert("RGBA")
    rgba.putalpha(alpha)
    return rgba


def components(alpha: Image.Image) -> tuple[int, float]:
    small = alpha.resize((128, 128), Image.Resampling.BILINEAR)
    px = small.load(); seen=set(); areas=[]
    for y in range(128):
        for x in range(128):
            if (x,y) in seen or px[x,y] < 40: continue
            q=deque([(x,y)]); seen.add((x,y)); area=0
            while q:
                cx,cy=q.popleft(); area+=1
                for nx,ny in ((cx-1,cy),(cx+1,cy),(cx,cy-1),(cx,cy+1)):
                    if 0<=nx<128 and 0<=ny<128 and (nx,ny) not in seen and px[nx,ny]>=40:
                        seen.add((nx,ny)); q.append((nx,ny))
            if area >= 24: areas.append(area)
    if not areas: return 0, 0.0
    total=sum(areas)
    return len(areas), max(areas)/total


def normalize(master: Image.Image, side: int) -> Image.Image:
    bbox = master.getbbox()
    if not bbox:
        raise RuntimeError("empty alpha after background isolation")
    crop = master.crop(bbox)
    max_subject = int(side * .82)
    scale = min(max_subject / crop.width, max_subject / crop.height)
    crop = crop.resize((max(1, round(crop.width*scale)), max(1, round(crop.height*scale))), Image.Resampling.LANCZOS)
    out = Image.new("RGBA", (side, side), (0,0,0,0))
    x = (side-crop.width)//2
    bottom = int(side*.08)
    y = side-bottom-crop.height
    if y < int(side*.08):
        y = (side-crop.height)//2
    out.alpha_composite(crop, (x,y))
    return out


def validate(im: Image.Image):
    a = im.getchannel("A")
    lo,hi=a.getextrema()
    if hi == 0 or lo == 255: raise RuntimeError("transparency validation failed")
    visible = sum(a.histogram()[8:])/(im.width*im.height)
    if visible > .70: raise RuntimeError(f"alpha coverage too high: {visible:.1%}")
    pad = int(im.width*.04)
    edges=(a.crop((0,0,im.width,pad)),a.crop((0,im.height-pad,im.width,im.height)),a.crop((0,0,pad,im.height)),a.crop((im.width-pad,0,im.width,im.height)))
    if any(e.getbbox() for e in edges): raise RuntimeError("transparent safety padding failed")
    count, dominant = components(a)
    if count == 0 or dominant < .88: raise RuntimeError(f"subject isolation failed: components={count}, dominant={dominant:.1%}")
    return visible, dominant


def main():
    if not TOKEN: raise SystemExit("HF_TOKEN is required")
    if not ASSET_ID or not ASSET_ID.startswith(SUPPORTED): raise SystemExit("SPRITE_TARGET must be BLD/CORE/VEH/PRP/TER")
    rid,name,desc,runtime,status = manifest_item(ASSET_ID)
    if status != "TODO":
        raise SystemExit(f"{rid} is {status}, refusing duplicate generation")
    kind=rid.split("-",1)[0]
    final = normalize(isolate(generate(prompt_for(rid,name,desc))), TARGET_SIDE[kind])
    coverage,dominant=validate(final)
    INCOMING.mkdir(parents=True, exist_ok=True)
    out=INCOMING/(Path(runtime).stem+".png")
    final.save(out,"PNG",optimize=True)
    print(f"VALIDATED_CANDIDATE={out.relative_to(ROOT)} coverage={coverage:.1%} dominant={dominant:.1%}")


if __name__ == "__main__":
    main()
