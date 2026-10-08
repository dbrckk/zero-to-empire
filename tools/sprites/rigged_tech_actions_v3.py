#!/usr/bin/env python3
"""Automated multi-action TECH sprite production with a single textured IK rig.

All outputs remain technical review candidates. This script cannot mark DONE.
No Kaggle, generative frame redraw, interaction, or remote model is required.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import statistics
import zipfile
from pathlib import Path
from PIL import Image, ImageDraw
import rigged_tech_walk_v2 as core

ACTIONS = ("WALK", "CARRY", "IDLE", "WORK", "REPAIR", "CELEB")
GROUND = core.GROUND
CANVAS = core.CANVAS
ROOT_X = core.ROOT_X
HIP_Y = core.HIP_Y


def spine_lean(t: float, action: str) -> float:
    """Cyclic, phase-coupled spine bend in radians. Foot/hip world anchors
    are not modified, so contact geometry stays deterministic and reversible.
    """
    phase = 2 * math.pi * (t % 1.0)
    if action == "WALK":
        return .045 * math.sin(2 * phase + .3) + .012 * math.sin(phase)
    if action == "CARRY":
        return .028 * math.sin(2 * phase + .3) + .010 * math.sin(phase)
    if action == "IDLE":
        return .012 * math.sin(phase + .2)
    if action == "WORK":
        return .025 * math.sin(phase + .4) + .012 * math.sin(2 * phase)
    if action == "REPAIR":
        return .018 * math.sin(phase + .3) + .007 * math.sin(2 * phase)
    if action == "CELEB":
        return .050 * math.sin(phase + .2) + .015 * math.sin(2 * phase)
    raise ValueError(f"Unsupported action: {action}")


def pose_for(t: float, action: str) -> dict:
    if action not in ACTIONS:
        raise ValueError(f"Unsupported action: {action}")
    t %= 1.0
    phase = 2 * math.pi * t
    if action in ("WALK", "CARRY"):
        p = core.pose(t)
        p["torso_lean_rad"] = spine_lean(t, action)
        if action == "CARRY":
            x, y = p["root"]
            p["handL"] = (x + 29, y - 55)
            p["handR"] = (x + 103, y - 55)
        return p
    x, y = ROOT_X, HIP_Y + 1.8 * math.sin(phase)
    hands = {
        "IDLE": ((x - 33 - 3 * math.sin(phase), y - 17 + 1.4 * math.cos(phase)),
                 (x + 45 + 3 * math.sin(phase), y - 21 + 1.4 * math.cos(phase))),
        "WORK": ((x + 29 + 12 * math.sin(phase), y - 50 + 6 * math.cos(phase)),
                 (x + 93 + 17 * math.sin(2 * phase), y - 56 + 14 * math.cos(2 * phase))),
        "REPAIR": ((x + 36 + 8 * math.sin(phase), y - 42 + 7 * math.cos(phase)),
                   (x + 58 + 12 * math.sin(phase), y - 54 + 11 * math.cos(phase))),
        "CELEB": ((x - 26 - 19 * math.sin(phase), y - 144 + 12 * math.cos(phase)),
                  (x + 45 + 19 * math.sin(phase), y - 146 - 12 * math.cos(phase))),
    }
    hand_l, hand_r = hands[action]
    return {
        "root": (x, y), "left": (x - 29, GROUND), "right": (x + 32, GROUND),
        "handL": hand_l, "handR": hand_r, "lockL": True, "lockR": True,
        "rollL": 0.0, "rollR": 0.0,
        "torso_lean_rad": spine_lean(t, action),
    }


def draw_cargo(layer: Image.Image, p: dict, t: float) -> None:
    x, y = p["root"]
    x, y = round(x + 20), round(y - 82)
    d = ImageDraw.Draw(layer, "RGBA")
    d.rounded_rectangle((x + 1, y + 5, x + 93, y + 56), radius=8,
                        fill=(21, 34, 45, 250), outline=(107, 128, 144, 250), width=3)
    d.polygon(((x + 9, y + 4), (x + 82, y + 4),
               (x + 91, y + 10), (x + 17, y + 10)), fill=(91, 108, 124, 238))
    d.rounded_rectangle((x + 11, y + 13, x + 82, y + 45), radius=5,
                        fill=(37, 54, 67, 250), outline=(120, 137, 148, 230), width=2)
    for i in range(6):
        xx = x + 17 + 10 * i
        d.line((xx, y + 16, xx, y + 42), fill=(16, 29, 39, 205), width=2)
        d.line((xx + 2, y + 18, xx + 2, y + 41), fill=(84, 111, 129, 130), width=1)
    d.rounded_rectangle((x + 33, y + 23, x + 62, y + 34), radius=3,
                        fill=(10, 31, 39, 248), outline=(79, 175, 191, 230), width=2)
    d.line((x + 37, y + 28, x + 57, y + 28), fill=(41, 215, 235, 205), width=2)
    for xx in (x + 9, x + 85):
        for yy in (y + 14, y + 46):
            d.ellipse((xx - 2, yy - 2, xx + 2, yy + 2), fill=(172, 188, 195, 245))


def draw_console(layer: Image.Image, p: dict, t: float) -> None:
    x, y = p["root"]
    x, y = round(x + 26), round(y - 83)
    d = ImageDraw.Draw(layer, "RGBA")
    d.rounded_rectangle((x, y, x + 89, y + 51), radius=8,
                        fill=(17, 31, 43, 246), outline=(107, 139, 156, 245), width=3)
    d.rounded_rectangle((x + 8, y + 8, x + 81, y + 42), radius=5,
                        fill=(9, 28, 40, 249), outline=(30, 145, 168, 235), width=2)
    d.line((x + 13, y + 32, x + 76, y + 32), fill=(28, 85, 104, 240), width=2)
    for n in range(5):
        h = 8 + round(7 * (.5 + .5 * math.sin(2 * math.pi * t + n)))
        d.rectangle((x + 15 + n * 12, y + 30 - h,
                     x + 20 + n * 12, y + 30), fill=(21, 172 + n * 7, 192, 230))
    d.ellipse((x + 71, y + 12, x + 77, y + 18), fill=(108, 232, 244, 240))


def draw_repair(layer: Image.Image, p: dict, t: float) -> None:
    x, y = p["root"]
    x, y = round(x + 62), round(y - 105)
    d = ImageDraw.Draw(layer, "RGBA")
    d.rounded_rectangle((x, y, x + 61, y + 79), radius=7,
                        fill=(22, 35, 48, 248), outline=(115, 136, 149, 249), width=3)
    d.rounded_rectangle((x + 8, y + 9, x + 52, y + 62), radius=5,
                        fill=(31, 49, 61, 245), outline=(70, 102, 120, 245), width=2)
    for n in range(5):
        xx = x + 12 + n * 10
        d.line((xx, y + 16, xx, y + 56), fill=(11, 29, 44, 230), width=3)
    d.ellipse((x + 18, y + 23, x + 45, y + 50),
              fill=(22, 43, 53, 250), outline=(128, 160, 168, 245), width=3)
    d.ellipse((x + 26, y + 31, x + 37, y + 43),
              fill=(10, 92, 111, 245), outline=(48, 207, 220, 245), width=2)
    tip = (x + 32, y + 33)
    # Keep the welding torch physically attached to the animated wrist.
    hand = (round(p["handR"][0]), round(p["handR"][1]))
    d.line((hand[0], hand[1], tip[0], tip[1]), fill=(39, 55, 65, 250), width=7)
    d.line((hand[0], hand[1]-2, tip[0]-2, tip[1]-1),
           fill=(128, 157, 164, 240), width=2)
    intensity = max(0.0, math.sin(2 * math.pi * t)) ** 3
    if intensity > .01:
        for n in range(7):
            a = 2 * math.pi * n / 7 + .1 * math.sin(2 * math.pi * t)
            radius = (7 + 13 * intensity) * (1 + ((n * 7) % 5) / 12)
            dest = (round(tip[0] + math.cos(a) * radius),
                    round(tip[1] + math.sin(a) * radius))
            d.line((tip, dest), fill=(69, 204, 241, round(195 * intensity)), width=2)
        d.ellipse((tip[0] - 5, tip[1] - 5, tip[0] + 5, tip[1] + 5),
                  fill=(103, 223, 252, round(230 * intensity)))


def draw_celebration(layer: Image.Image, p: dict, t: float) -> None:
    d = ImageDraw.Draw(layer, "RGBA")
    x, y = p["root"]
    for n in range(12):
        a = 2 * math.pi * (n / 12 + t)
        xx = round(x + (-34 if n % 2 == 0 else 47) + 26 * math.cos(a))
        yy = round(y - 144 + 31 * math.sin(a))
        alpha = round(125 + 90 * (.5 + .5 * math.sin(a * 2)))
        color = (74, 219, 245, alpha) if n % 3 else (252, 188, 101, alpha)
        d.line((xx - 2, yy - 4, xx + 2, yy + 4), fill=color, width=3)
        d.ellipse((xx - 2, yy - 2, xx + 2, yy + 2), fill=color)


def draw_idle_readout(layer: Image.Image, p: dict, t: float) -> None:
    x, y = p["root"]
    x, y = round(x + 14), round(y - 96)
    energy = .5 + .5 * math.sin(2 * math.pi * t)
    d = ImageDraw.Draw(layer, "RGBA")
    d.rounded_rectangle((x, y, x + 18, y + 9), radius=2,
                        fill=(14, 30, 40, 233), outline=(83, 134, 151, 240), width=1)
    d.rectangle((x + 3, y + 3, x + 3 + round(12 * energy), y + 6),
                fill=(46, 165, 203, 240))


def draw_frame(action: str, t: float, kit: dict):
    p = pose_for(t, action)
    under = {
        "CARRY": draw_cargo,
        "WORK": draw_console,
        "REPAIR": draw_repair,
        "IDLE": draw_idle_readout,
    }.get(action)
    overlay = draw_celebration if action == "CELEB" else None
    return core.draw_frame(t, kit, p, under, overlay, joint_fabric=True)


def action_qa(action: str, poses: list, base_qa: dict) -> dict:
    violations = []
    for index, p in enumerate(poses):
        x, y = p["root"]
        a = float(p.get("torso_lean_rad", 0.0))
        if not math.isfinite(a) or abs(a) > .085:
            violations.append({"frame": index, "spine_lean_rad": a})
            continue
        cs, sn = math.cos(a), math.sin(a)
        def rotated_shoulder(dx, dy):
            return (x + dx * cs - dy * sn, y + dx * sn + dy * cs)
        shoulders = {"handL": rotated_shoulder(-24, -86),
                     "handR": rotated_shoulder(23, -85)}
        for hand, shoulder in shoulders.items():
            distance = math.dist(shoulder, p[hand])
            if distance > 118:
                violations.append({"frame": index, "hand": hand,
                                   "distance": round(distance, 3)})
    motion = {
        hand: round(max(math.dist(poses[0][hand], q[hand]) for q in poses), 3)
        for hand in ("handL", "handR")
    }
    stationary = action in ("IDLE", "WORK", "REPAIR", "CELEB")
    grounded = all(q["lockL"] and q["lockR"] for q in poses) if stationary else True
    grip_ok = (all(
        math.dist(p["handL"], (p["root"][0] + 29, p["root"][1] - 55)) < .001
        and math.dist(p["handR"], (p["root"][0] + 103, p["root"][1] - 55)) < .001
        for p in poses) if action == "CARRY" else True)
    legible_motion = (action not in ("WORK", "REPAIR", "CELEB")
                      or motion["handR"] >= 18)
    kinetic = (not violations and grounded and grip_ok and legible_motion)
    base_qa.update({
        "action_kinematic_pass": kinetic, "hand_reach_violations": violations,
        "action_motion_range_px": motion, "stationary_ground_contact_pass": grounded,
        "fixed_cargo_grip_pass": grip_ok,
        "game_scale_motion_pass": legible_motion,
        "spine_lean_max_degrees": round(max(abs(math.degrees(p.get("torso_lean_rad",0.0))) for p in poses),3),
        "spine_lean_in_range": not any("spine_lean_rad" in v for v in violations),
        "technical_pass": bool(base_qa["technical_pass"] and kinetic),
        "visual_review_pass": False, "semantic_review_pass": False,
        "strict_status": "NEEDS_REVIEW",
    })
    return base_qa


def build_action(skin: Path, out: Path, action: str, frames: int = 24, fps: int = 12):
    if action not in ACTIONS:
        raise ValueError(f"Unsupported action: {action}")
    if not (8 <= frames <= 64 and frames % 2 == 0 and 3 <= fps <= 24):
        raise ValueError("frames must be even 8-64, fps 3-24")
    kit = core.load_kit(skin)
    out.mkdir(parents=True, exist_ok=True)
    (out / "frames").mkdir(exist_ok=True)
    images, poses, boots = [], [], []
    asset_id = f"CHR-TECH-{action}"
    for i in range(frames):
        im, p, b = draw_frame(action, i / frames, kit)
        im.save(out / "frames" / f"{asset_id}-{i:02d}.png", optimize=True)
        images.append(im)
        poses.append(p)
        boots.append(b)
    cols = 6
    rows = math.ceil(frames / cols)
    atlas = Image.new("RGBA", (CANVAS * cols, CANVAS * rows))
    sheet = Image.new("RGB", (192 * cols, 192 * rows), (27, 34, 45))
    game_sheet = Image.new("RGB", (96 * cols, 96 * rows), (27, 34, 45))
    thumbs = []
    for i, im in enumerate(images):
        atlas.alpha_composite(im, ((i % cols) * CANVAS, (i // cols) * CANVAS))
        bg = Image.new("RGBA", (CANVAS, CANVAS), (26, 34, 45, 255))
        bg.alpha_composite(im)
        preview = bg.convert("RGB")
        thumb = preview.resize((192, 192), Image.Resampling.LANCZOS)
        thumbs.append(thumb)
        sheet.paste(thumb, ((i % cols) * 192, (i // cols) * 192))
        game_sheet.paste(preview.resize((96, 96), Image.Resampling.LANCZOS),
                         ((i % cols) * 96, (i // cols) * 96))
    atlas.save(out / "atlas.png", optimize=True)
    sheet.save(out / "contact.jpg", quality=91)
    game_sheet.save(out / "contact-game-scale.jpg", quality=90)
    thumbs[0].save(out / "preview.gif", save_all=True, append_images=thumbs[1:],
                   duration=round(1000 / fps), loop=0, optimize=False)
    qa = action_qa(action, poses, core.check(images, poses, boots))
    footfalls = action in ("WALK", "CARRY")
    events = [{
        "frame": i,
        "footstep": ("right" if i == 0 else "left" if i == frames // 2 else None)
                    if footfalls else None,
        "left_ground_contact": p["lockL"],
        "right_ground_contact": p["lockR"],
        "vfx_event": (
            "weld-sparks" if action == "REPAIR" and math.sin(2 * math.pi * i / frames) > .5
            else "celebration-particles" if action == "CELEB"
            else "data-update" if action == "WORK" and i % max(1, frames // 4) == 0
            else None),
    } for i, p in enumerate(poses)]
    manifest = {
        "asset_id": asset_id, "action": action, "build": "modular-tech-actions-v3",
        "rig": "one-textured-character-with-two-bone-IK",
        "source_skin_sha256": hashlib.sha256(skin.read_bytes()).hexdigest(),
        "frames": frames, "fps": fps, "frame_size": [CANVAS, CANVAS],
        "atlas_columns": cols, "atlas_rows": rows,
        "pivot": {"x": ROOT_X, "y": GROUND},
        "strict_status": "NEEDS_REVIEW", "human_visual_review_required": True,
        "qa": qa,
        "limitations": [
            "Rigid 2D body parts may look mechanical or overlap",
            "Action props and limb contacts require semantic and visual review",
            "Technical QA is not evidence of AAA artistic approval",
            "Inspect the 96px previews in actual gameplay camera",
        ],
    }
    (out / "qa-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (out / "frame-poses.json").write_text(json.dumps(poses, indent=2), encoding="utf-8")
    (out / "animation-events.json").write_text(json.dumps(events, indent=2), encoding="utf-8")
    # Shared runtime-pack contract; preserve legacy filename for existing consumers.
    (out / "footstep-events.json").write_text(json.dumps(events, indent=2), encoding="utf-8")
    (out / "REVIEW_REQUIRED.txt").write_text(
        "Technical review candidate only. Never mark strict DONE without visual/semantic approval.\n",
        encoding="utf-8")
    bundle = out.parent / f"{asset_id}-modular-v3-review.zip"
    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as z:
        for file in sorted(out.rglob("*")):
            if file.is_file():
                z.write(file, file.relative_to(out))
    return manifest, bundle


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skin", type=Path, default=Path(__file__).with_name("skin-tech-v1.webp"))
    parser.add_argument("--output", type=Path, default=Path("build/tech-actions-v3"))
    parser.add_argument("--frames", type=int, default=24)
    parser.add_argument("--fps", type=int, default=12)
    parser.add_argument("--action", choices=ACTIONS, default="WALK")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    actions = ACTIONS if args.all else (args.action,)
    summaries = []
    for action in actions:
        out = args.output / action if args.all else args.output
        manifest, bundle = build_action(args.skin, out, action, args.frames, args.fps)
        summaries.append({
            "asset_id": manifest["asset_id"], "action": action,
            "technical_pass": manifest["qa"]["technical_pass"],
            "seam_ratio": manifest["qa"]["seam_to_median_ratio"],
            "bundle": bundle.name, "source_skin_sha256": manifest["source_skin_sha256"],
            "strict_status": "NEEDS_REVIEW",
        })
    index = {
        "format": "zte-modular-actions-v3", "review_required": True,
        "strict_status": "NEEDS_REVIEW",
        "source_skin_sha256": summaries[0]["source_skin_sha256"],
        "actions": summaries,
    }
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "production-index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
    print(json.dumps(index, indent=2))
    if not all(s["technical_pass"] for s in summaries):
        raise SystemExit("At least one animation failed technical QA; keep review gate closed")


if __name__ == "__main__":
    main()
