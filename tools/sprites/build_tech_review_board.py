#!/usr/bin/env python3
"""Deterministic review-only TECH atlases visualization; never promotes assets.

Reads canonical-format 4x4 transparent PNG review candidates. Produces a
static side-by-side 42px day/night comparison and an animated GIF; both are
labeled explicitly as candidates, not Android screenshots or approved art.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ACTIONS = ('IDLE', 'WALK', 'WORK', 'CARRY', 'REPAIR', 'CELEB')
FRAMES = {'IDLE': 6, 'WALK': 8, 'WORK': 10, 'CARRY': 8, 'REPAIR': 10, 'CELEB': 8}
BG = (13, 22, 34)
TILE = (26, 38, 54)
INK = (229, 239, 245)
MUTED = (149, 174, 190)
AQUA = (76, 222, 228)
AMBER = (246, 182, 86)


def font(n: int, bold: bool = False):
    name = 'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'
    for folder in ('/usr/share/fonts/truetype/dejavu', '/usr/share/fonts/truetype/liberation2'):
        path = Path(folder) / name
        if path.is_file():
            return ImageFont.truetype(str(path), n)
    return ImageFont.load_default()


def tiles(root: Path):
    report = json.loads((root / 'review-report.json').read_text(encoding='utf-8'))
    expected = [f'CHR-TECH-{a}' for a in ACTIONS]
    if report['target_ids'] != expected or report['candidate_count'] != 6:
        raise ValueError('The report does not contain six required actions in order')
    if report['semantic_approved_count'] != 0 or report['automatic_promotion_permitted']:
        raise ValueError('This renderer accepts unapproved review candidates only')
    records = {}
    for item in report['items']:
        action = item['asset_id'].split('-')[-1]
        if item['semantic_approved'] or item['visual_review_pass'] or item['strict_status'] != 'NEEDS_REVIEW':
            raise ValueError(f'{action}: forbidden review promotion')
        if item['frame_count'] != FRAMES[action] or item['atlas_size'] != [1024, 1024]:
            raise ValueError(f'{action}: invalid atlas geometry')
        with Image.open(root / item['staged_png']) as im:
            if im.size != (1024, 1024):
                raise ValueError(f'{action}: PNG geometry does not match metadata')
            rgba = im.convert('RGBA')
            frames = []
            for i in range(FRAMES[action]):
                x, y = (i % 4) * 256, (i // 4) * 256
                frame = rgba.crop((x, y, x + 256, y + 256))
                if frame.getchannel('A').getbbox() is None:
                    raise ValueError(f'{action}: empty frame {i}')
                frames.append(frame)
        records[action] = (item, frames)
    return records


def label(d, x, y, message, *, size=18, color=INK, bold=False):
    d.text((x, y), message, font=font(size, bold), fill=color)


def checker(surface: Image.Image, xy, side, night: bool):
    base = (19, 32, 46, 255) if night else (203, 222, 232, 255)
    alt = (24, 40, 55, 255) if night else (192, 214, 227, 255)
    squares = Image.new('RGBA', (side, side), base)
    d = ImageDraw.Draw(squares)
    step = max(8, side // 5)
    for i in range(0, side, step):
        for j in range(0, side, step):
            if (i//step + j//step) % 2:
                d.rectangle((i, j, i+step-1, j+step-1), fill=alt)
    surface.paste(squares, xy, squares)


def place(surface: Image.Image, frame: Image.Image, x, y, side):
    resized = frame.resize((side, side), Image.Resampling.LANCZOS)
    surface.paste(resized, (x, y), resized)


def board(records, out: Path):
    W, H = 1780, 1270
    im = Image.new('RGBA', (W, H), BG + (255,))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((24, 25, W-24, 150), radius=22, fill=(23, 36, 53), outline=(57, 79, 100), width=2)
    label(d, 52, 45, 'TECH / SIX ACTIONS · SOURCE ATLASES', size=38, bold=True)
    label(d, 54, 103, 'Review candidates • exact 42 px dark/day preview • source frames only • NOT Android screenshots', size=18, color=MUTED)
    cellW, cellH = 552, 500
    for idx, action in enumerate(ACTIONS):
        col, row = idx % 3, idx // 3
        x, y = 30 + col * 580, 172 + row * 524
        item, frames = records[action]
        d.rounded_rectangle((x, y, x+cellW, y+cellH), radius=18, fill=TILE, outline=(60, 83, 104), width=2)
        label(d, x+26, y+18, action, size=26, bold=True)
        label(d, x+cellW-155, y+24, f'{len(frames)} frames', size=16, color=MUTED)
        # Most discriminative frames of each rigged cycle, sampled without changing their order.
        order = [0, len(frames)//4, len(frames)//2, 3*len(frames)//4]
        for k,i in enumerate(order):
            fx = x+22+k*132
            checker(im, (fx, y+65), 112, night=True)
            place(im, frames[i], fx, y+65, 112)
            label(d, fx+4, y+181, f'F{i+1:02d}', size=15, color=MUTED)
        label(d, x+26, y+225, 'NIGHT · 42 px', size=16, color=AQUA, bold=True)
        label(d, x+298, y+225, 'DAY · 42 px', size=16, color=AMBER, bold=True)
        checker(im, (x+38, y+260), 146, night=True)
        checker(im, (x+310, y+260), 146, night=False)
        # Frame is rendered at a literal 42 px, centered on a 146 px test panel.
        place(im, frames[len(frames)//4], x+38+52, y+260+52, 42)
        place(im, frames[len(frames)//4], x+310+52, y+260+52, 42)
        ambiguity = item.get('automated_visual_risks', {}).get('foot_profile_ambiguous_frames', 0)
        note = (f'Leg visibility flagged: {ambiguity}/{len(frames)}' if action in ('WALK', 'CARRY')
                else 'Semantic / style review required')
        label(d, x+26, y+427, note, size=17, color=AMBER if ambiguity else MUTED)
        label(d, x+26, y+458, f'SHA-256  {item["staged_sha256"][:16]}…', size=14, color=MUTED)
    label(d, 39, 1233, 'SOURCE: art/production/character-rig-review-candidates  |  PRODUCTION STATUS UNCHANGED · 216/235 STRICT DONE', size=17, color=AQUA)
    im.convert('RGB').save(out, 'PNG', optimize=True)


def animated(records, out: Path):
    W, H = 1040, 390
    still = []
    for t in range(16):
        img = Image.new('RGB', (W,H), BG)
        d=ImageDraw.Draw(img)
        label(d, 24, 17, 'TECH · TRUE CANDIDATE FRAMES · 42 px · NIGHT / DAY', size=22,bold=True)
        label(d, 24, 48, f'Preview tick {t+1:02d}/16 • NOT release assets or game captures', size=15, color=MUTED)
        for i,a in enumerate(ACTIONS):
            _item, frames = records[a]
            x=18+i*170
            checker(img, (x, 95), 150, True)
            place(img, frames[t % len(frames)], x+54, 147, 42)
            label(d, x+15, 260, a, size=16, color=AQUA,bold=True)
            label(d, x+15, 291, f'{(t%len(frames))+1:02d}/{len(frames):02d}', size=15,color=MUTED)
        label(d, 24, 355, 'Source PNGs: deterministic 4×4 canonical review atlases • Motion on grid is not real in-city pathing', size=14,color=MUTED)
        still.append(img)
    still[0].save(out, format='GIF', save_all=True, append_images=still[1:], duration=125, loop=0, optimize=False)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    rec=tiles(args.source)
    board(rec,args.output/'tech-review-true-source-board.png')
    animated(rec,args.output/'tech-review-true-source-motion.gif')
    print('TECH_REVIEW_TRUE_SOURCE_PREVIEW_PASS=6 STRICT_PROMOTION=0')

if __name__ == '__main__':main()