#!/usr/bin/env python3
"""Author a candidate-only 2.5D semantic replacement for TER-07.

TER-07 is an Expansion-era energy conduit connector, not a terrain platform.
This v3 candidate adds material depth, bevels and an extruded junction while
remaining isolated on transparency. It never writes the runtime asset.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'art/production/ter07'
SIDE=1024

P0=(170.0,720.0)
P1=(854.0,322.0)
DEPTH=(18.0,25.0)

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def mul(v,s): return (v[0]*s,v[1]*s)

def unit_and_normal(a,b):
    dx=b[0]-a[0]; dy=b[1]-a[1]
    length=math.hypot(dx,dy)
    u=(dx/length,dy/length)
    n=(-u[1],u[0])
    return u,n,length

U,N,LENGTH=unit_and_normal(P0,P1)

def pt(t,side=0.0,depth=0.0):
    p=add(P0,mul(U,t))
    p=add(p,mul(N,side))
    p=add(p,mul(DEPTH,depth))
    return p

def strip_poly(start,end,half_width,depth=0.0):
    return [
        add(add(start,mul(N,half_width)),mul(DEPTH,depth)),
        add(add(end,mul(N,half_width)),mul(DEPTH,depth)),
        add(add(end,mul(N,-half_width)),mul(DEPTH,depth)),
        add(add(start,mul(N,-half_width)),mul(DEPTH,depth)),
    ]

def quad_extrude(poly,depth_vec):
    return [[p,add(p,depth_vec)] for p in poly]

def draw_side_faces(draw,top_poly,depth_vec,fill):
    lower=[add(p,depth_vec) for p in top_poly]
    # Only visible lower/right side faces in the shared 2.5D light.
    for i in (1,2):
        j=(i+1)%4
        draw.polygon([top_poly[i],top_poly[j],lower[j],lower[i]],fill=fill)
    draw.polygon(lower,fill=(15,20,25,220))

def render():
    im=Image.new('RGBA',(SIDE,SIDE),(0,0,0,0))

    # Controlled cyan bloom, restricted to the connector footprint.
    glow=Image.new('RGBA',(SIDE,SIDE),(0,0,0,0))
    gd=ImageDraw.Draw(glow,'RGBA')
    gd.line([P0,P1],fill=(43,215,235,95),width=78)
    glow=glow.filter(ImageFilter.GaussianBlur(23))
    im.alpha_composite(glow)

    d=ImageDraw.Draw(im,'RGBA')

    start=pt(16)
    end=pt(LENGTH-16)
    outer=strip_poly(start,end,58)
    draw_side_faces(d,outer,DEPTH,(20,28,34,255))
    d.polygon(outer,fill=(51,61,70,255))

    # Top bevel and recessed channel.
    bevel=strip_poly(pt(28),pt(LENGTH-28),49)
    d.polygon(bevel,fill=(111,125,136,255))
    trench=strip_poly(pt(38),pt(LENGTH-38),36)
    d.polygon(trench,fill=(18,26,33,255))

    # Lower-right channel lip adds depth without becoming a floor card.
    lip_a=[pt(38,-36),pt(LENGTH-38,-36),pt(LENGTH-38,-27),pt(38,-27)]
    d.polygon(lip_a,fill=(8,14,19,245))

    # Twin recessed energy rails, with shadow, emissive core and hot highlight.
    for side in (-18,18):
        a=pt(48,side)
        b=pt(LENGTH-48,side)
        shadow_a=add(a,(5,7)); shadow_b=add(b,(5,7))
        d.line([shadow_a,shadow_b],fill=(0,9,13,210),width=18)
        d.line([a,b],fill=(20,136,154,255),width=16)
        d.line([a,b],fill=(28,225,242,255),width=10)
        d.line([add(a,mul(N,-2)),add(b,mul(N,-2))],fill=(211,255,255,205),width=3)

    # Attached structural clamps. Their lower halves are darker to reinforce extrusion.
    for t in range(82,int(LENGTH)-62,88):
        c=pt(t)
        a=add(c,mul(N,-51)); b=add(c,mul(N,51))
        d.line([add(a,(6,8)),add(b,(6,8))],fill=(23,31,38,255),width=18)
        d.line([a,b],fill=(116,133,143,255),width=15)
        d.line([add(a,mul(U,-2)),add(b,mul(U,-2))],fill=(221,230,234,120),width=3)

        # Bolted energy coupler: dark socket -> cyan lens -> white pin highlight.
        r=13
        d.ellipse((c[0]-r+4,c[1]-r+6,c[0]+r+4,c[1]+r+6),fill=(8,18,23,230))
        d.ellipse((c[0]-r,c[1]-r,c[0]+r,c[1]+r),fill=(28,198,217,255),outline=(139,246,252,240),width=3)
        d.ellipse((c[0]-5,c[1]-7,c[0]+5,c[1]+3),fill=(230,255,255,225))

    # Inline junction box, integrated in the conduit and visibly extruded.
    c=pt(LENGTH*.52)
    hu=49; hn=49
    top=[
        add(add(c,mul(U,-hu)),mul(N,hn)),
        add(add(c,mul(U, hu)),mul(N,hn)),
        add(add(c,mul(U, hu)),mul(N,-hn)),
        add(add(c,mul(U,-hu)),mul(N,-hn)),
    ]
    depth=mul(DEPTH,1.15)
    lower=[add(p,depth) for p in top]
    # Visible junction side faces.
    d.polygon([top[1],top[2],lower[2],lower[1]],fill=(21,30,37,255))
    d.polygon([top[2],top[3],lower[3],lower[2]],fill=(12,19,24,255))
    d.polygon(top,fill=(66,78,88,255),outline=(153,169,178,255))

    inner_hu=31; inner_hn=30
    inner=[
        add(add(c,mul(U,-inner_hu)),mul(N,inner_hn)),
        add(add(c,mul(U, inner_hu)),mul(N,inner_hn)),
        add(add(c,mul(U, inner_hu)),mul(N,-inner_hn)),
        add(add(c,mul(U,-inner_hu)),mul(N,-inner_hn)),
    ]
    d.polygon(inner,fill=(17,29,35,255),outline=(42,215,232,245),width=4)

    # Recessed reactor lens and small material bolts.
    r=16
    d.ellipse((c[0]-r+4,c[1]-r+6,c[0]+r+4,c[1]+r+6),fill=(4,13,18,230))
    d.ellipse((c[0]-r,c[1]-r,c[0]+r,c[1]+r),fill=(49,220,233,255),outline=(218,255,255,245),width=4)
    d.ellipse((c[0]-6,c[1]-9,c[0]+5,c[1]+2),fill=(247,255,255,235))
    for du,dn in ((-37,37),(37,37),(37,-37),(-37,-37)):
        p=add(add(c,mul(U,du)),mul(N,dn))
        d.ellipse((p[0]-4,p[1]-4,p[0]+4,p[1]+4),fill=(177,190,198,210))

    # Shared upper-left key highlight and lower-right occlusion edge.
    d.line([pt(18,56),pt(LENGTH-18,56)],fill=(235,241,244,150),width=4)
    d.line([pt(18,-57),pt(LENGTH-18,-57)],fill=(4,8,12,180),width=8)

    # End caps make this a modular connector, not an arbitrary strip.
    for t in (24,LENGTH-24):
        c=pt(t)
        a=add(c,mul(N,-56)); b=add(c,mul(N,56))
        d.line([add(a,(5,7)),add(b,(5,7))],fill=(14,21,27,255),width=22)
        d.line([a,b],fill=(103,118,128,255),width=18)
        d.line([a,b],fill=(207,220,226,115),width=3)

    return im

def validate(im):
    if im.mode!='RGBA' or im.size!=(SIDE,SIDE):
        raise RuntimeError('expected 1024x1024 RGBA')
    a=im.getchannel('A')
    bbox=a.getbbox()
    if not bbox:
        raise RuntimeError('empty candidate')

    margin=min(bbox[0],bbox[1],SIDE-bbox[2],SIDE-bbox[3])
    if margin<78:
        raise RuntimeError(f'safety margin too small: {margin}px')

    coverage=sum(a.histogram()[8:])/(SIDE*SIDE)
    if not .06<=coverage<=.25:
        raise RuntimeError(f'connector coverage outside semantic target: {coverage:.1%}')

    w=bbox[2]-bbox[0]; h=bbox[3]-bbox[1]
    aspect=max(w,h)/max(1,min(w,h))
    if aspect<1.40:
        raise RuntimeError(f'connector aspect too compact: {aspect:.2f}')

    return {'bbox':bbox,'margin':margin,'coverage':coverage,'long_axis_aspect':aspect}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    im=render()
    metrics=validate(im)
    png=OUT/'zte_terrain_07_candidate_v3.png'
    im.save(png,'PNG',optimize=True)
    report={
        'asset_id':'TER-07',
        'semantic_role':'Expansion energy conduit connector',
        'status':'CANDIDATE',
        'revision':'v3-premium-2.5d',
        'candidate':str(png.relative_to(ROOT)),
        'runtime_unchanged':'app/src/main/res/drawable-nodpi/zte_terrain_07_final.webp',
        'previous_candidate':'art/production/ter07/zte_terrain_07_candidate_v2.png',
        'previous_verdict':'SEMANTIC_PASS_ART_REJECT',
        'metrics':metrics,
        'semantic_requirements':[
            'isolated connector on transparency',
            'no terrain/platform slab',
            'continuous twin energy rails',
            'attached junction, clamps and modular end caps only',
            '2.5D material depth with visible side faces',
            'upper-left key and lower-right occlusion consistent with world art',
        ],
    }
    (OUT/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print('TER07_CANDIDATE='+str(png.relative_to(ROOT)))
    print('TER07_REPORT='+json.dumps(report))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
