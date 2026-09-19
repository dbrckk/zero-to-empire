#!/usr/bin/env python3
"""Author a candidate-only semantic replacement for TER-07.

TER-07 is an Expansion-era energy conduit connector, not a terrain platform.
The candidate stays isolated on transparency and is intentionally NOT copied to
runtime by this script. Semantic review remains required before replacement.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'art/production/ter07'
SIDE=1024

P0=(170,720)
P1=(854,322)

def add(p,q):
    return (p[0]+q[0],p[1]+q[1])

def mul(v,s):
    return (v[0]*s,v[1]*s)

def unit_and_normal(a,b):
    dx=b[0]-a[0];dy=b[1]-a[1]
    n=math.hypot(dx,dy)
    u=(dx/n,dy/n)
    normal=(-u[1],u[0])
    return u,normal

def point_at(t,u):
    return (P0[0]+u[0]*t,P0[1]+u[1]*t)

def polygon_strip(a,b,half_width):
    u,n=unit_and_normal(a,b)
    return [
        (a[0]+n[0]*half_width,a[1]+n[1]*half_width),
        (b[0]+n[0]*half_width,b[1]+n[1]*half_width),
        (b[0]-n[0]*half_width,b[1]-n[1]*half_width),
        (a[0]-n[0]*half_width,a[1]-n[1]*half_width),
    ]

def render():
    im=Image.new('RGBA',(SIDE,SIDE),(0,0,0,0))
    glow=Image.new('RGBA',(SIDE,SIDE),(0,0,0,0))
    gd=ImageDraw.Draw(glow,'RGBA')
    d=ImageDraw.Draw(im,'RGBA')

    u,n=unit_and_normal(P0,P1)
    length=math.hypot(P1[0]-P0[0],P1[1]-P0[1])

    # Restrained cyan under-glow. It follows only the connector, never a tile.
    gd.line([P0,P1],fill=(50,218,236,86),width=86)
    glow=glow.filter(ImageFilter.GaussianBlur(25))
    im.alpha_composite(glow)

    # Structural outer housing and inset trench.
    d.polygon(polygon_strip(P0,P1,56),fill=(37,44,52,255))
    d.polygon(polygon_strip(add(P0,mul(u,10)),add(P1,mul(u,-10)),45),fill=(74,84,92,255))
    d.polygon(polygon_strip(add(P0,mul(u,18)),add(P1,mul(u,-18)),34),fill=(18,25,31,255))

    # Two energy rails provide an unmistakable conduit read.
    for side in (-1,1):
        off=mul(n,18*side)
        a=add(add(P0,mul(u,28)),off)
        b=add(add(P1,mul(u,-28)),off)
        d.line([a,b],fill=(35,205,224,255),width=12)
        d.line([a,b],fill=(196,250,255,190),width=3)

    # Attached clamps/brackets. Every detail stays fused to the connector.
    for t in range(70,int(length)-50,86):
        c=point_at(t,u)
        a=add(c,mul(n,-53))
        b=add(c,mul(n,53))
        d.line([a,b],fill=(118,132,140,255),width=13)
        d.line([add(c,mul(n,-38)),add(c,mul(n,38))],fill=(205,216,220,145),width=3)

        # Small recessed energy node.
        r=11
        d.ellipse((c[0]-r,c[1]-r,c[0]+r,c[1]+r),fill=(30,224,238,235),outline=(224,255,255,190),width=3)

    # Compact inline junction block reinforces function without becoming a platform.
    c=point_at(length*.52,u)
    block=[
        add(add(c,mul(u,-45)),mul(n,45)),
        add(add(c,mul(u,45)),mul(n,45)),
        add(add(c,mul(u,45)),mul(n,-45)),
        add(add(c,mul(u,-45)),mul(n,-45)),
    ]
    d.polygon(block,fill=(53,61,70,255),outline=(139,154,164,235))
    inner=[
        add(add(c,mul(u,-27)),mul(n,27)),
        add(add(c,mul(u,27)),mul(n,27)),
        add(add(c,mul(u,27)),mul(n,-27)),
        add(add(c,mul(u,-27)),mul(n,-27)),
    ]
    d.polygon(inner,fill=(18,31,37,255),outline=(43,217,233,235))
    d.ellipse((c[0]-13,c[1]-13,c[0]+13,c[1]+13),fill=(82,236,244,235),outline=(235,255,255,210),width=3)

    # Shared upper-left highlight / lower-right shadow.
    d.line([add(P0,mul(n,-52)),add(P1,mul(n,-52))],fill=(232,239,242,105),width=4)
    d.line([add(P0,mul(n,52)),add(P1,mul(n,52))],fill=(5,9,13,135),width=7)

    return im

def validate(im):
    if im.mode!='RGBA' or im.size!=(SIDE,SIDE):
        raise RuntimeError('expected 1024x1024 RGBA')
    a=im.getchannel('A')
    bbox=a.getbbox()
    if not bbox:
        raise RuntimeError('empty candidate')
    margin=min(bbox[0],bbox[1],SIDE-bbox[2],SIDE-bbox[3])
    if margin<90:
        raise RuntimeError(f'safety margin too small: {margin}px')
    coverage=sum(a.histogram()[8:])/(SIDE*SIDE)
    if not .05<=coverage<=.24:
        raise RuntimeError(f'connector coverage outside semantic target: {coverage:.1%}')

    # Semantic geometry guard: connector should be long/narrow, never a square pad.
    w=bbox[2]-bbox[0];h=bbox[3]-bbox[1]
    aspect=max(w,h)/max(1,min(w,h))
    if aspect<1.45:
        raise RuntimeError(f'connector aspect too compact: {aspect:.2f}')

    return {'bbox':bbox,'margin':margin,'coverage':coverage,'long_axis_aspect':aspect}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    im=render()
    metrics=validate(im)
    png=OUT/'zte_terrain_07_candidate_v2.png'
    im.save(png,'PNG',optimize=True)
    report={
        'asset_id':'TER-07',
        'semantic_role':'Expansion energy conduit connector',
        'status':'CANDIDATE',
        'candidate':str(png.relative_to(ROOT)),
        'runtime_unchanged':'app/src/main/res/drawable-nodpi/zte_terrain_07_final.webp',
        'metrics':metrics,
        'semantic_requirements':[
            'isolated connector on transparency',
            'no terrain/platform slab',
            'continuous energy rails',
            'attached junction and brackets only',
            '2.5D diagonal connector read',
        ],
    }
    (OUT/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print('TER07_CANDIDATE='+str(png.relative_to(ROOT)))
    print('TER07_REPORT='+json.dumps(report))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
