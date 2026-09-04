#!/usr/bin/env python3
"""Mass-generate static Zero -> Empire sprite candidates on a Kaggle GPU.

Designed for Kaggle notebooks with a P100/T4-class accelerator. Generates only
BLD/CORE/VEH/PRP TODO assets and writes PNG candidates under
art/incoming/final-sprites/. Final runtime validation remains in GitHub Actions.

Default backend: ByteDance SDXL-Lightning 4-step UNet on SDXL base.
"""
from __future__ import annotations

import argparse
import os
import re
from collections import deque
from pathlib import Path

print("KAGGLE_STARTUP=python", flush=True)
print("KAGGLE_STARTUP=import_torch", flush=True)
import torch
print(f"KAGGLE_STARTUP=torch_ok cuda={torch.cuda.is_available()}", flush=True)
print("KAGGLE_STARTUP=import_pillow", flush=True)
from PIL import Image, ImageFilter
print("KAGGLE_STARTUP=import_diffusers", flush=True)
from diffusers import StableDiffusionXLPipeline, UNet2DConditionModel, EulerDiscreteScheduler
print("KAGGLE_STARTUP=import_huggingface_hub", flush=True)
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file
print("KAGGLE_STARTUP=imports_ok", flush=True)

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
INCOMING = ROOT / "art/incoming/final-sprites"
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
SUPPORTED = ("PRP-", "VEH-", "CORE-", "BLD-")
PRIORITY = {"PRP": 0, "VEH": 1, "CORE": 2, "BLD": 3}
TARGET_SIDE = {"BLD": 2048, "CORE": 1536, "VEH": 1536, "PRP": 1024}
BASE = os.getenv("KAGGLE_SPRITE_BASE", "stabilityai/stable-diffusion-xl-base-1.0")
LIGHTNING_REPO = os.getenv("KAGGLE_SPRITE_LIGHTNING_REPO", "ByteDance/SDXL-Lightning")
LIGHTNING_CKPT = os.getenv("KAGGLE_SPRITE_LIGHTNING_CKPT", "sdxl_lightning_4step_unet.safetensors")


def manifest_rows():
    order = 0
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if not m:
            continue
        asset_id, name, description, runtime, status = [x.strip() for x in m.groups()]
        if not asset_id.startswith(SUPPORTED) or status.upper() != "TODO":
            continue
        runtime_path = ROOT / runtime
        stem = Path(runtime).stem
        candidate = INCOMING / f"{stem}.png"
        if runtime_path.exists() or candidate.exists():
            continue
        kind = asset_id.split("-", 1)[0]
        yield {"id": asset_id,"name": name,"description": description,"runtime": runtime,"stem": stem,"kind": kind,"order": order}
        order += 1


def prompt_for(item):
    contract = {
        "BLD": "single complete industrial building, bottom-center pivot, 2.5D three-quarter 34 degree camera, iconic readable silhouette",
        "CORE": "single complete power reactor core on compact cradle, 2.5D three-quarter 34 degree camera, iconic readable silhouette",
        "VEH": "single complete vehicle, three-quarter side view, contact-center pivot, readable traffic direction, compact contact shadow",
        "PRP": "single complete industrial prop, three-quarter 2.5D view, clear readable silhouette at mobile size",
    }[item["kind"]]
    return ("AAA premium mobile strategy game production sprite, " + contract + ", " + item["name"] + ". " + item["description"] + " Upper-left key light, cool fill, restrained amber and cyan emissive accents, premium physically plausible materials. ONE isolated object only, centered on pure solid black background, large empty margin, no surrounding scene. No UI, no border, no frame, no watermark, no logo, no letters, no readable text, no numbers, no brand signage, no collage, no multiple objects.")


def load_pipe():
    token = os.getenv("HF_TOKEN") or None
    print(f"KAGGLE_MODEL=begin base={BASE} lightning={LIGHTNING_CKPT}", flush=True)
    print("KAGGLE_MODEL=load_unet_config", flush=True)
    unet = UNet2DConditionModel.from_config(BASE, subfolder="unet", token=token).to("cuda", torch.float16)
    print("KAGGLE_MODEL=download_lightning_checkpoint", flush=True)
    ckpt = hf_hub_download(LIGHTNING_REPO, LIGHTNING_CKPT, token=token)
    print(f"KAGGLE_MODEL=checkpoint_ready path={ckpt}", flush=True)
    print("KAGGLE_MODEL=load_lightning_weights", flush=True)
    unet.load_state_dict(load_file(ckpt, device="cuda"))
    print("KAGGLE_MODEL=load_sdxl_pipeline", flush=True)
    pipe = StableDiffusionXLPipeline.from_pretrained(BASE, unet=unet, torch_dtype=torch.float16, variant="fp16", token=token, use_safetensors=True).to("cuda")
    print("KAGGLE_MODEL=pipeline_on_cuda", flush=True)
    pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")
    pipe.set_progress_bar_config(disable=False)
    return pipe


def border_background(im: Image.Image):
    rgb = im.convert("RGB"); w, h = rgb.size; pts = []; stride = max(1, min(w, h) // 128)
    for x in range(0, w, stride): pts.append(rgb.getpixel((x, 0))); pts.append(rgb.getpixel((x, h - 1)))
    for y in range(0, h, stride): pts.append(rgb.getpixel((0, y))); pts.append(rgb.getpixel((w - 1, y)))
    pts.sort(key=lambda p: sum(p)); sample = pts[: max(16, len(pts) // 3)]
    return tuple(sum(p[i] for p in sample) // len(sample) for i in range(3))


def isolate(im: Image.Image):
    rgb = im.convert("RGB"); w, h = rgb.size; bg = border_background(rgb); px = rgb.load(); dist = Image.new("L", (w, h), 0); dp = dist.load()
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]; d = ((r-bg[0])**2 + (g-bg[1])**2 + (b-bg[2])**2) ** 0.5; dp[x, y] = min(255, int(d * 3.0))
    mask = dist.point(lambda p: 0 if p < 20 else (255 if p > 58 else int((p-20) * 255 / 38)))
    mp = mask.load(); seen = set(); q = deque()
    for x in range(w):
        for y in (0, h-1):
            if mp[x, y] < 180 and (x, y) not in seen: seen.add((x,y)); q.append((x,y))
    for y in range(h):
        for x in (0, w-1):
            if mp[x, y] < 180 and (x, y) not in seen: seen.add((x,y)); q.append((x,y))
    while q:
        x, y = q.popleft(); mp[x, y] = 0
        for nx, ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0 <= nx < w and 0 <= ny < h and (nx,ny) not in seen and mp[nx,ny] < 180: seen.add((nx,ny)); q.append((nx,ny))
    mask = mask.filter(ImageFilter.GaussianBlur(0.6)); rgba = rgb.convert("RGBA"); rgba.putalpha(mask); return rgba


def normalize(master: Image.Image, side: int):
    bbox = master.getbbox()
    if not bbox: raise RuntimeError("empty alpha")
    crop = master.crop(bbox); max_subject = int(side * .82); scale = min(max_subject / crop.width, max_subject / crop.height)
    crop = crop.resize((max(1, round(crop.width*scale)), max(1, round(crop.height*scale))), Image.Resampling.LANCZOS)
    out = Image.new("RGBA", (side, side), (0,0,0,0)); x = (side-crop.width)//2; bottom = int(side*.08); y = max(int(side*.08), side-bottom-crop.height); out.alpha_composite(crop, (x,y)); return out


def validate(im: Image.Image):
    a = im.getchannel("A"); lo, hi = a.getextrema()
    if hi == 0 or lo == 255: raise RuntimeError("transparency validation failed")
    visible = sum(a.histogram()[8:])/(im.width*im.height)
    if visible < .04 or visible > .70: raise RuntimeError(f"invalid alpha coverage {visible:.1%}")
    pad = int(im.width*.04); edges=(a.crop((0,0,im.width,pad)),a.crop((0,im.height-pad,im.width,im.height)),a.crop((0,0,pad,im.height)),a.crop((im.width-pad,0,im.width,im.height)))
    if any(e.getbbox() for e in edges): raise RuntimeError("transparent safety padding failed")
    return visible


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--kind", choices=["ALL", "PRP", "VEH", "CORE", "BLD"], default="ALL"); ap.add_argument("--count", type=int, default=60); ap.add_argument("--seed", type=int, default=4242); args = ap.parse_args()
    items = list(manifest_rows())
    if args.kind != "ALL": items = [x for x in items if x["kind"] == args.kind]
    items.sort(key=lambda x: (PRIORITY[x["kind"]], x["order"])); items = items[:max(1, args.count)]
    print(f"KAGGLE_PLAN={len(items)} kind={args.kind}", flush=True)
    if not items: print("No pending static manifest assets.", flush=True); return
    pipe = load_pipe(); INCOMING.mkdir(parents=True, exist_ok=True); ok = 0; rejected = 0
    for index, item in enumerate(items, 1):
        print(f"[{index}/{len(items)}] {item['id']} {item['name']}", flush=True); gen = torch.Generator(device="cuda").manual_seed(args.seed + index)
        try:
            image = pipe(prompt_for(item), num_inference_steps=4, guidance_scale=0.0, width=1024, height=1024, generator=gen).images[0]
            final = normalize(isolate(image), TARGET_SIDE[item["kind"]]); coverage = validate(final); out = INCOMING / f"{item['stem']}.png"; final.save(out, "PNG", optimize=True); ok += 1; print(f"KAGGLE_VALIDATED={out.relative_to(ROOT)} coverage={coverage:.1%}", flush=True)
        except Exception as exc:
            rejected += 1; print(f"KAGGLE_REJECTED={item['id']} reason={exc}", flush=True)
        finally: torch.cuda.empty_cache()
    print(f"KAGGLE_BATCH_SUCCESS={ok} KAGGLE_BATCH_REJECTED={rejected} KAGGLE_BATCH_ATTEMPTED={len(items)}", flush=True)


if __name__ == "__main__":
    main()
