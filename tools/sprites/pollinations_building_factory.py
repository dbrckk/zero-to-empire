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
    samples=[]
    for x in range(w):
        samples+=(px[x,0],px[x,h-1])
    for y in range(h):
        samples+=(px[0,y],px[w-1,y])
    med=tuple(sorted(v[i] for v in samples)[len(samples)//2] for i in range(3))
    dev=max(max(abs(v[i]-med[i]) for i in range(3)) for v in samples)
    if dev>32: fail(f'bad border variance={dev}')
    out=Image.new('RGBA',rgb.size,(0,0,0,0)); dst=out.load()
    for y in range(h):
        for x in range(w):
            p=px[x,y]; d=max(abs(p[i]-med[i]) for i in range(3))
            a=0 if d<=18 else 255 if d>=42 else round((d-18)*255/24)
            dst[x,y]=(p[0],p[1],p[2],a)
    a=out.getchannel('A').filter(ImageFilter.MedianFilter(3)); out.putalpha(a)
    if not a.getbbox(): fail('empty isolation')
    return out

def main():
    aid,name,desc,runtime,status=next_target()
    m=re.fullmatch(r'BLD-(\d{2})-T(\d)',aid)
    if not m: fail('bad target '+aid)
    fam,tier=m.groups()
    prompt=(
      f'AAA premium mobile strategy game industrial factory sprite, family {int(fam)}, tier {tier}. {desc}. '
      'single connected factory only, centered, orthographic three-quarter view, graphite steel, amber and cyan emissive accents, '
      'clean readable silhouette, no people, no vehicles, no text, no signs, no crane, no scenery, no road, no floor slab, no platform, '
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
