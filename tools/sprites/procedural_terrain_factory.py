#!/usr/bin/env python3
"""Deterministically author the 14 terrain/infrastructure masters without GPU.

These are 1024x1024 RGBA isometric world tiles/connectors. The factory keeps a
large transparent exterior margin, a consistent 34-degree-ish 2.5D read and
category-specific industrial details. Technical validation is strict; semantic
AAA acceptance remains a separate inspection gate.
"""
from __future__ import annotations

import math
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[2]
INCOMING = ROOT / "art/incoming/final-sprites"
RUNTIME = ROOT / "app/src/main/res/drawable-nodpi"
SIDE = 1024
CX, CY = 512, 520
RX, RY = 400, 225
MARGIN = 64

NAMES = {
    0: "cracked industrial ground tile",
    1: "road curb connector",
    2: "rail cargo strip",
    3: "conduit trench",
    4: "clean commercial pavement",
    5: "multi lane road connector",
    6: "loading pad",
    7: "energy conduit",
    8: "reinforced platform",
    9: "maglev rail connector",
    10: "elevated service deck",
    11: "energy spine",
    12: "phase platform",
    13: "singularity stellar connector",
}

ERA = {
    0: ((72, 68, 62), (103, 94, 81), (197, 118, 48)),
    1: ((64, 68, 72), (112, 122, 128), (53, 181, 205)),
    2: ((49, 55, 65), (96, 112, 130), (39, 211, 227)),
    3: ((37, 41, 54), (85, 92, 126), (104, 225, 255)),
}


def diamond() -> list[tuple[int, int]]:
    return [(CX, CY-RY), (CX+RX, CY), (CX, CY+RY), (CX-RX, CY)]


def era_for(i: int) -> int:
    return min(3, i // 4)


def inside_diamond(x: int, y: int) -> bool:
    return abs(x-CX)/RX + abs(y-CY)/RY <= 1.0


def add_texture(base: Image.Image, i: int, base_rgb: tuple[int,int,int]) -> None:
    rng = random.Random(7100+i)
    px = base.load()
    for _ in range(17000):
        x = rng.randrange(CX-RX, CX+RX)
        y = rng.randrange(CY-RY, CY+RY)
        if not inside_diamond(x, y):
            continue
        delta = rng.randint(-13, 13)
        r,g,b = base_rgb
        a = rng.randint(16, 42)
        px[x,y] = (max(0,min(255,r+delta)), max(0,min(255,g+delta)), max(0,min(255,b+delta)), a)


def iso_line(draw: ImageDraw.ImageDraw, p1, p2, fill, width=8):
    draw.line([p1,p2], fill=fill, width=width)


def render(i: int) -> Image.Image:
    era = era_for(i)
    dark, mid, accent = ERA[era]
    im = Image.new("RGBA", (SIDE,SIDE), (0,0,0,0))
    d = ImageDraw.Draw(im, "RGBA")
    poly = diamond()
    d.polygon(poly, fill=(*dark,255))
    d.line(poly+[poly[0]], fill=(180,190,200,150), width=5, joint="curve")
    add_texture(im, i, dark)
    d = ImageDraw.Draw(im, "RGBA")

    # Shared inset border improves tile readability without baked UI semantics.
    inset = [(CX, CY-RY+28),(CX+RX-50,CY),(CX,CY+RY-28),(CX-RX+50,CY)]
    d.line(inset+[inset[0]], fill=(*mid,135), width=5, joint="curve")

    if i in (0,4):
        rng=random.Random(900+i)
        for _ in range(22 if i==0 else 11):
            x=rng.randint(CX-290,CX+290); y=rng.randint(CY-130,CY+130)
            if inside_diamond(x,y):
                pts=[(x,y),(x+rng.randint(-35,35),y+rng.randint(8,28)),(x+rng.randint(-55,55),y+rng.randint(20,45))]
                d.line(pts, fill=(25,25,27,150), width=3)
        for off in range(-240,241,80):
            iso_line(d,(CX-330,CY+off//3),(CX+330,CY+off//3),(*mid,45),2)
    elif i in (1,5):
        road=(48,50,53,255) if era<2 else (40,47,56,255)
        d.polygon([(CX-330,CY-75),(CX+210,CY-165),(CX+330,CY-75),(CX-210,CY+165)], fill=road)
        for off in (-42,42) if i==5 else (0,):
            iso_line(d,(CX-250,CY+off+80),(CX+250,CY+off-80),(220,210,150,180),8)
        iso_line(d,(CX-330,CY+85),(CX+205,CY-95),(*mid,220),16)
    elif i in (2,9):
        for off in (-48,48):
            iso_line(d,(CX-315,CY+off+95),(CX+315,CY+off-95),(*mid,255),13)
            iso_line(d,(CX-315,CY+off+95),(CX+315,CY+off-95),(*accent,100 if i==9 else 35),4)
        for k in range(-260,281,55):
            x1=CX+k; y1=CY-k//3
            iso_line(d,(x1-35,y1-45),(x1+35,y1+45),(70,65,58,220),9)
    elif i in (3,7,11,13):
        wide=38 if i in (11,13) else 26
        iso_line(d,(CX-310,CY+105),(CX+310,CY-105),(20,25,32,240),wide+18)
        iso_line(d,(CX-310,CY+105),(CX+310,CY-105),(*accent,235),wide)
        iso_line(d,(CX-310,CY+105),(CX+310,CY-105),(230,250,255,135),5)
        for k in range(-240,241,80):
            x=CX+k; y=CY-k//3
            d.ellipse((x-15,y-15,x+15,y+15), fill=(*accent,220), outline=(240,255,255,180), width=3)
        if i==13:
            glow=Image.new("RGBA", im.size,(0,0,0,0)); gd=ImageDraw.Draw(glow,"RGBA")
            gd.ellipse((CX-120,CY-72,CX+120,CY+72), outline=(*accent,180), width=20)
            glow=glow.filter(ImageFilter.GaussianBlur(15)); im.alpha_composite(glow)
    elif i==6:
        pad=[(CX,CY-150),(CX+265,CY-5),(CX,CY+150),(CX-265,CY+5)]
        d.polygon(pad, fill=(*mid,210)); d.line(pad+[pad[0]], fill=(*accent,190), width=9)
        for off in (-110,0,110):
            iso_line(d,(CX-220+off//2,CY+80),(CX+110+off//2,CY-80),(225,190,95,150),6)
    elif i in (8,10,12):
        pad=[(CX,CY-165),(CX+290,CY-10),(CX,CY+165),(CX-290,CY+10)]
        d.polygon(pad, fill=(*mid,210))
        d.line(pad+[pad[0]], fill=(*accent,170), width=8)
        for k in range(-200,201,80):
            x=CX+k; y=CY-k//3
            d.ellipse((x-9,y-9,x+9,y+9), fill=(205,215,225,180))
        if i==10:
            for off in (-85,85): iso_line(d,(CX-250,CY+off),(CX+250,CY+off-160),(*accent,100),7)
        if i==12:
            for r in (48,92,138):
                d.ellipse((CX-r,CY-r//2,CX+r,CY+r//2), outline=(*accent,125), width=6)

    # Upper-left highlight + lower-right shadow preserve shared lighting contract.
    iso_line(d,(CX-RX+48,CY-8),(CX,CY-RY+27),(235,240,245,95),5)
    iso_line(d,(CX+RX-48,CY+8),(CX,CY+RY-27),(10,12,18,120),7)
    return im


def validate(im: Image.Image, i: int) -> None:
    if im.mode != "RGBA" or im.size != (SIDE,SIDE):
        raise RuntimeError(f"TER-{i:02d}: expected 1024x1024 RGBA")
    a=im.getchannel("A")
    bbox=a.getbbox()
    if not bbox: raise RuntimeError(f"TER-{i:02d}: empty")
    if bbox[0] < MARGIN or bbox[1] < MARGIN or SIDE-bbox[2] < MARGIN or SIDE-bbox[3] < MARGIN:
        raise RuntimeError(f"TER-{i:02d}: transparent safety margin failed: {bbox}")
    coverage=sum(a.histogram()[8:])/(SIDE*SIDE)
    if coverage > .58: raise RuntimeError(f"TER-{i:02d}: coverage too high {coverage:.1%}")


def main() -> int:
    INCOMING.mkdir(parents=True,exist_ok=True); RUNTIME.mkdir(parents=True,exist_ok=True)
    for i in range(14):
        im=render(i); validate(im,i)
        stem=f"zte_terrain_{i:02d}_final"
        png=INCOMING/f"{stem}.png"; webp=RUNTIME/f"{stem}.webp"
        im.save(png,"PNG",optimize=True)
        im.save(webp,"WEBP",lossless=True,method=4,exact=True)
        print(f"TERRAIN_VALIDATED=TER-{i:02d} {NAMES[i]} png={png.relative_to(ROOT)} webp={webp.relative_to(ROOT)}")
    print("TERRAIN_BATCH_COUNT=14")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
