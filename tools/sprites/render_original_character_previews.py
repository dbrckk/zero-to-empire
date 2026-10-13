#!/usr/bin/env python3
"""Android-friendly animated previews for original ChatGPT-authored sprites.

All evidence is review-only. This never reads or changes the canonical
235-row master queue or Android runtime assets, and never promotes PNGs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FRAMES = {"IDLE": 6, "WALK": 8, "WORK": 10, "CARRY": 8, "REPAIR": 10, "CELEB": 8}
ROLES = ("OP", "LOG", "ENG")
DURATION_MS = {"IDLE": 185, "WALK": 105, "WORK": 125, "CARRY": 115,
               "REPAIR": 120, "CELEB": 115}


def frames_from_atlas(path: Path, count: int) -> list[Image.Image]:
    with Image.open(path) as source:
        if source.size != (1024, 1024) or source.mode != "RGBA":
            raise ValueError(f"Invalid RGBA atlas geometry: {path}")
        result = [source.crop(((i % 4)*256, (i // 4)*256,
                              (i % 4+1)*256, (i // 4+1)*256))
                  for i in range(count)]
    if any(not im.getchannel("A").getbbox() for im in result):
        raise ValueError(f"Empty character animation frame: {path}")
    return result


def checker() -> Image.Image:
    im = Image.new("RGB", (256, 256), "#b0b6c1")
    d = ImageDraw.Draw(im)
    for y in range(0, 256, 20):
        for x in range(0, 256, 20):
            if (x//20+y//20) % 2:
                d.rectangle((x, y, x+19, y+19), fill="#9ca5b3")
    return im


def compose(frame: Image.Image, backdrop: Image.Image) -> Image.Image:
    cell = backdrop.copy()
    cell.paste(frame, (0, 0), frame)
    return cell


def fingerprint(frame: Image.Image) -> str:
    return hashlib.sha256(frame.tobytes()).hexdigest()


def change_ratio(a: Image.Image, b: Image.Image) -> float:
    # RGB plus silhouette activity, computed over the occupied image region
    # to distinguish a blink from identical idle frames.
    aa = a.resize((64, 64), Image.Resampling.BILINEAR).convert("RGBA")
    bb = b.resize((64, 64), Image.Resampling.BILINEAR).convert("RGBA")
    pa, pb = list(aa.getdata()), list(bb.getdata())
    activity = 0
    count = 0
    for left, right in zip(pa, pb):
        if left[3] < 32 and right[3] < 32:
            continue
        activity += sum(abs(left[i]-right[i]) for i in range(4))
        count += 4 * 255
    return round(activity/count, 6) if count else 0.0


def produce(source: Path) -> dict:
    manifest = json.loads((source/"creation-manifest.json").read_text(encoding="utf8"))
    expected = {f"CHR-{role}-{action}" for role in ROLES for action in FRAMES}
    if ({row["id"] for row in manifest["assets"]} != expected
        or len(manifest["assets"]) != 18
        or not manifest.get("review_only", False)):
        raise ValueError("Canonical original character candidate manifest mismatch")
    preview = source/"previews"
    preview.mkdir(parents=True, exist_ok=True)
    atlas = Image.new("RGB", (6*190, 3*223), "#202732")
    draw = ImageDraw.Draw(atlas)
    background = checker()
    analysis = []
    for row, role in enumerate(ROLES):
        for col, action in enumerate(FRAMES):
            asset_id = f"CHR-{role}-{action}"
            filename = f"zte_chr_{role.lower()}_{action.lower()}_final.png"
            cells = frames_from_atlas(source/"candidates"/filename, FRAMES[action])
            distinct = len({fingerprint(f) for f in cells})
            if distinct < 2:
                raise ValueError(f"Frozen animation: {asset_id}")
            # WALK/CARRY need eight physically different stride phases, not
            # a repeated sinusoidal snapshot with fake foot movement.
            if action in {"WALK", "CARRY"} and distinct != FRAMES[action]:
                raise ValueError(
                    f"Repeated motion pose: {asset_id} "
                    f"unique={distinct}/{FRAMES[action]}"
                )
            rendered = [compose(f, background) for f in cells]
            gif_path = preview/f"{role.lower()}-{action.lower()}.gif"
            rendered[0].save(gif_path, "GIF", save_all=True, append_images=rendered[1:],
                             duration=DURATION_MS[action], loop=0,
                             optimize=False, disposal=2)
            small = rendered[0].resize((186, 186), Image.Resampling.LANCZOS)
            pos = (col*190+2, row*223+30)
            atlas.paste(small, pos)
            draw.text((col*190+6, row*223+8), f"{role}  {action}", fill="#ffffff")
            all_frames = cells[1:] + cells[:1]
            ratios = [change_ratio(a, b) for a, b in zip(cells, all_frames)]
            boxes = [f.getchannel("A").getbbox() for f in cells]
            min_margin = min(min(x, y, 256-x2, 256-y2)
                             for x, y, x2, y2 in boxes)
            analysis.append({
                "id": asset_id,
                "source_atlas": filename,
                "animation_preview": f"previews/{gif_path.name}",
                "frames": len(cells),
                "distinct_frame_hashes": distinct,
                "min_alpha_margin": min_margin,
                "mean_adjacent_pixel_activity": round(sum(ratios)/len(ratios), 6),
                "max_adjacent_pixel_activity": max(ratios),
                "technical_geometry_pass": min_margin >= 10,
                "visual_semantic_approved": False,
                "android_runtime_approved": False,
                "strict_done_added": 0,
            })
    atlas.save(source/"original-review-contact-sheet.png", optimize=True)
    result = {
        "schema_version": 1,
        "review_only": True,
        "strict_done_added": 0,
        "generated_local_preview_count": len(analysis),
        "editable_source_frame_count": sum(FRAMES.values())*len(ROLES),
        "assets": analysis,
    }
    (source/"animation-review.json").write_text(json.dumps(result, indent=2)+"\n",
                                                  encoding="utf8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path,
                        default=Path("art/incoming/chatgpt-original"))
    args = parser.parse_args()
    result = produce(args.output_dir)
    print("CHATGPT_ORIGINAL_PREVIEW_GIFS="+str(result["generated_local_preview_count"]))
    print("CHATGPT_ORIGINAL_EDITABLE_FRAMES="+str(result["editable_source_frame_count"]))
    print("CHATGPT_ORIGINAL_SEMANTIC_APPROVAL=FALSE")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
