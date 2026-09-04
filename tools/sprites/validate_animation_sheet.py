#!/usr/bin/env python3
"""Validate one CHR/MCH animation sheet against the deterministic production contract."""
from __future__ import annotations

import argparse
import json
import math
from collections import deque
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]


def fail(msg: str) -> None:
    raise SystemExit(f"ERROR: {msg}")


def dominant_ratio(alpha: Image.Image) -> float:
    small = alpha.resize((96, 96), Image.Resampling.BILINEAR)
    px = small.load(); seen=set(); areas=[]
    for y in range(96):
        for x in range(96):
            if (x,y) in seen or px[x,y] < 32:
                continue
            q=deque([(x,y)]); seen.add((x,y)); area=0
            while q:
                cx,cy=q.popleft(); area += 1
                for nx,ny in ((cx-1,cy),(cx+1,cy),(cx,cy-1),(cx,cy+1)):
                    if 0<=nx<96 and 0<=ny<96 and (nx,ny) not in seen and px[nx,ny]>=32:
                        seen.add((nx,ny)); q.append((nx,ny))
            if area >= 8: areas.append(area)
    return max(areas)/sum(areas) if areas else 0.0


def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument("sheet", type=Path)
    p.add_argument("--frames", type=int, required=True)
    p.add_argument("--cell", type=int, choices=[256,512], required=True)
    p.add_argument("--columns", type=int, default=4)
    p.add_argument("--padding", type=int, default=4)
    p.add_argument("--family", choices=["CHR","MCH"], required=True)
    args=p.parse_args()
    rows=math.ceil(args.frames/args.columns)
    expected=(args.columns*args.cell, rows*args.cell)
    im=Image.open(args.sheet).convert("RGBA")
    if im.size != expected:
        fail(f"{args.sheet.name}: expected {expected[0]}x{expected[1]}, got {im.width}x{im.height}")
    alpha=im.getchannel("A")
    if alpha.getextrema()[0] == 255:
        fail(f"{args.sheet.name}: no transparent pixels")
    reports=[]
    pivots=[]
    for i in range(args.frames):
        x=(i%args.columns)*args.cell; y=(i//args.columns)*args.cell
        cell=alpha.crop((x,y,x+args.cell,y+args.cell))
        bbox=cell.getbbox()
        if not bbox:
            fail(f"{args.sheet.name}: frame {i} empty")
        x0,y0,x1,y1=bbox
        if min(x0,y0,args.cell-x1,args.cell-y1) < args.padding:
            fail(f"{args.sheet.name}: frame {i} violates {args.padding}px transparent padding")
        coverage=sum(cell.histogram()[8:])/(args.cell*args.cell)
        if coverage > .72:
            fail(f"{args.sheet.name}: frame {i} coverage too high ({coverage:.1%})")
        dom=dominant_ratio(cell)
        if dom < .72:
            fail(f"{args.sheet.name}: frame {i} fragmented subject ({dom:.1%} dominant)")
        pivot_x=(x0+x1)/2/args.cell
        pivot_y=y1/args.cell
        pivots.append((pivot_x,pivot_y))
        reports.append({"frame":i,"coverage":round(coverage,4),"dominant":round(dom,4),"bbox":[x0,y0,x1,y1]})
    # Character feet/base pivots must stay stable enough to avoid visible jitter.
    xs=[p[0] for p in pivots]; ys=[p[1] for p in pivots]
    max_jitter=max(max(xs)-min(xs), max(ys)-min(ys))
    limit=.12 if args.family=="CHR" else .16
    if max_jitter > limit:
        fail(f"{args.sheet.name}: pivot jitter {max_jitter:.1%} exceeds {limit:.0%}")
    result={"sheet":str(args.sheet),"family":args.family,"frames":args.frames,"cell":args.cell,"grid":[args.columns,rows],"pivot_jitter":round(max_jitter,4),"frames_report":reports}
    print(json.dumps(result,separators=(",",":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
