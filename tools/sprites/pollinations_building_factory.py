#!/usr/bin/env python3
from __future__ import annotations
import json, os, re, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image, ImageFilter

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
REPORT=ROOT/'art/production/pollinations-report.json'

def fail(msg):
    print('POLLINATIONS_ERROR='+msg)
    raise SystemExit(1)

def next_target():
    explicit=os.getenv('SPRITE_TARGET','').strip().upper()
    rows=[]
    for line in MANIFEST.read_text(encoding='utf-8').splitlines():
        if not line.startswith('|') or 'app/src/main/res/' not in line: continue
        cols=[c.strip() for c in line.split('|')[1:-1]]
        if len(cols)==5 and cols[4].upper()=='TODO' and cols[0].startswith('BLD-'):
            rows.append(cols)
    if explicit:
        for r in rows:
            if r[0]==explicit:return r
        fail('requested target not TODO building: '+explicit)
    if not rows: fail('no TODO buildings')
    return rows[0]

def isolate(im):
    rgb=im.convert('RGB'); w,h=rgb.size; px=rgb.load()

    # Robust border reference: tolerate mild gradients, but classify subject by
    # distance from the median edge color instead of flooding through it.
    samples=[]
    for x in range(w):
        samples.append(px[x,0]); samples.append(px[x,h-1])
    for y in range(h):
        samples.append(px[0,y]); samples.append(px[w-1,y])
    med=tuple(sorted(v[i] for v in samples)[len(samples)//2] for i in range(3))

    def dist(a,b):
        return max(abs(a[i]-b[i]) for i in range(3))

    mask=Image.new('L',(w,h),0); mp=mask.load()
    for y in range(h):
        for x in range(w):
            d=dist(px[x,y],med)
            if d>=30:
                mp[x,y]=255
            elif d>=22:
                mp[x,y]=128

    mask=mask.filter(ImageFilter.MedianFilter(3))
    # Convert to binary for connectivity.
    binary=mask.point(lambda v:255 if v>=96 else 0)
    bp=binary.load()

    # Remove only components touching the image boundary: these are background
    # leakage/scenery by construction, never the centered isolated sprite.
    from collections import deque
    edge=set(); q=deque()
    for x in range(w):
        if bp[x,0]: q.append((x,0))
        if bp[x,h-1]: q.append((x,h-1))
    for y in range(h):
        if bp[0,y]: q.append((0,y))
        if bp[w-1,y]: q.append((w-1,y))
    while q:
        x,y=q.popleft()
        if (x,y) in edge or not bp[x,y]: continue
        edge.add((x,y))
        if x>0:q.append((x-1,y))
        if x+1<w:q.append((x+1,y))
        if y>0:q.append((x,y-1))
        if y+1<h:q.append((x,y+1))

    for x,y in edge:
        bp[x,y]=0

    # Score remaining components by area with a center preference so a detached
    # bright prop cannot beat the intended centered building.
    seen=set(); comps=[]
    cx0,cy0=w/2,h/2
    for y in range(h):
        for x in range(w):
            if not bp[x,y] or (x,y) in seen: continue
            comp=[]; qq=[(x,y)]; seen.add((x,y))
            while qq:
                cx,cy=qq.pop(); comp.append((cx,cy))
                for nx,ny in ((cx-1,cy),(cx+1,cy),(cx,cy-1),(cx,cy+1)):
                    if 0<=nx<w and 0<=ny<h and bp[nx,ny] and (nx,ny) not in seen:
                        seen.add((nx,ny)); qq.append((nx,ny))
            xs=[p[0] for p in comp]; ys=[p[1] for p in comp]
            ccx=sum(xs)/len(xs); ccy=sum(ys)/len(ys)
            center_penalty=1.0 + (((ccx-cx0)/(w/2))**2 + ((ccy-cy0)/(h/2))**2)
            comps.append((len(comp)/center_penalty,comp))
    if not comps:
        fail('no isolated subject after border-component cleanup')

    keep=set(max(comps,key=lambda z:z[0])[1])
    isolated=Image.new('RGBA',(w,h),(0,0,0,0)); dst=isolated.load()
    for x,y in keep:
        r,g,b=px[x,y]
        dst[x,y]=(r,g,b,255)

    bbox=isolated.getchannel('A').getbbox()
    if not bbox: fail('empty isolation')
    subject=isolated.crop(bbox)
    sw,sh=subject.size

    # Normalize to a canvas where the subject occupies at most 72% of a side.
    side=max(768,int(max(sw,sh)/0.72))
    side=min(2048,side)
    if max(sw,sh)>int(side*0.72):
        scale=(side*0.72)/max(sw,sh)
        subject=subject.resize((max(1,round(sw*scale)),max(1,round(sh*scale))),Image.Resampling.LANCZOS)
        sw,sh=subject.size
    canvas=Image.new('RGBA',(side,side),(0,0,0,0))
    canvas.alpha_composite(subject,((side-sw)//2,(side-sh)//2))
    return canvas

def main():
    aid,name,desc,runtime,status=next_target()
    m=re.fullmatch(r'BLD-(\d{2})-T(\d)',aid)
    if not m: fail('bad target '+aid)
    fam,tier=m.groups()
    prompt=(
      f'AAA premium mobile strategy game industrial factory sprite, family {int(fam)}, tier {tier}. {desc}. '
      'single connected factory only, centered, orthographic three-quarter view, graphite steel, amber and cyan emissive accents, '
      'clean readable silhouette occupying no more than 65 percent of the canvas, generous empty margin on every side, no people, no vehicles, no text, no signs, no crane, no scenery, no road, no floor slab, no platform, '
      'perfectly flat uniform neutral gray background, no gradient, no vignette, no horizon'
    )
    q=urllib.parse.quote(prompt,safe='')
    url=f'https://image.pollinations.ai/prompt/{q}?model=flux&width=1024&height=1024&seed=73117&nologo=true&private=true&enhance=false&safe=true'
    tmp=Path('/tmp/pollinations.png')
    req=urllib.request.Request(url,headers={'User-Agent':'zero-to-empire-github-actions/1.0'})
    try:
        with urllib.request.urlopen(req,timeout=180) as r:
            data=r.read()
    except Exception as e:
        fail('request failed: '+repr(e))
    if len(data)<10000: fail(f'response too small: {len(data)} bytes')
    tmp.write_bytes(data)
    try: im=Image.open(tmp)
    except Exception as e: fail('decode failed: '+repr(e))
    isolated=isolate(im)
    stem=f'zte_business_{fam}_t{tier}_final'
    INCOMING.mkdir(parents=True,exist_ok=True)
    out=INCOMING/f'{stem}.png'
    isolated.save(out,'PNG',optimize=True)
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text(json.dumps({'provider':'pollinations-anonymous','target':aid,'url_host':'image.pollinations.ai','candidate':str(out.relative_to(ROOT))},indent=2),encoding='utf-8')
    print('POLLINATIONS_CANDIDATE='+str(out.relative_to(ROOT)))

if __name__=='__main__':main()
