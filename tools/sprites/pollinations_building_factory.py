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

def isolate(im, session=None):
    # CPU background removal via U²-Net/rembg. This is deterministic post-
    # processing on the GitHub runner; downstream QA thresholds remain unchanged.
    try:
        from rembg import remove
    except Exception as e:
        fail('rembg unavailable: '+repr(e))

    src=im.convert('RGBA')
    try:
        cut=remove(src, session=session, alpha_matting=False)
    except Exception as e:
        fail('rembg failed: '+repr(e))
    if not isinstance(cut, Image.Image):
        cut=Image.open(cut).convert('RGBA')
    else:
        cut=cut.convert('RGBA')

    w,h=cut.size
    a=cut.getchannel('A')
    # Hard-clean tiny matte haze so component analysis reflects real subject.
    a=a.point(lambda v: 0 if v<24 else 255 if v>224 else v)
    cut.putalpha(a)

    # Keep the dominant connected alpha component; detached props/debris are
    # rejected at source rather than hidden by a relaxed QA gate.
    binary=a.point(lambda v:255 if v>=64 else 0)
    bp=binary.load()
    seen=set(); comps=[]
    for y in range(h):
        for x in range(w):
            if not bp[x,y] or (x,y) in seen:
                continue
            comp=[]; stack=[(x,y)]; seen.add((x,y))
            while stack:
                cx,cy=stack.pop(); comp.append((cx,cy))
                for nx,ny in ((cx-1,cy),(cx+1,cy),(cx,cy-1),(cx,cy+1)):
                    if 0<=nx<w and 0<=ny<h and bp[nx,ny] and (nx,ny) not in seen:
                        seen.add((nx,ny)); stack.append((nx,ny))
            comps.append(comp)
    if not comps:
        fail('rembg produced no subject')

    keep=set(max(comps,key=len))
    cleaned=Image.new('RGBA',(w,h),(0,0,0,0))
    srcpx=cut.load(); dst=cleaned.load()
    for x,y in keep:
        dst[x,y]=srcpx[x,y]

    bbox=cleaned.getchannel('A').getbbox()
    if not bbox:
        fail('empty isolation after component cleanup')

    subject=cleaned.crop(bbox)
    sw,sh=subject.size

    # Preserve enough detail while guaranteeing safe transparent margins.
    side=max(768, int(max(sw,sh)/0.68))
    side=min(2048, side)
    if max(sw,sh)>int(side*0.68):
        scale=(side*0.68)/max(sw,sh)
        subject=subject.resize((max(1,round(sw*scale)),max(1,round(sh*scale))),Image.Resampling.LANCZOS)
        sw,sh=subject.size
    canvas=Image.new('RGBA',(side,side),(0,0,0,0))
    canvas.alpha_composite(subject,((side-sw)//2,(side-sh)//2))
    return canvas

def generate(row, seed=73117, session=None, report_path: Path | None = None):
    aid,name,desc,runtime,status=row
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
    url=f'https://image.pollinations.ai/prompt/{q}?model=flux&width=1024&height=1024&seed={int(seed)}&nologo=true&private=true&enhance=false&safe=true'
    tmp=Path(f'/tmp/pollinations-{aid.lower()}-{int(seed)}.png')
    req=urllib.request.Request(url,headers={'User-Agent':'zero-to-empire-github-actions/1.0'})
    try:
        with urllib.request.urlopen(req,timeout=180) as r:
            data=r.read()
    except Exception as e:
        raise RuntimeError('request failed: '+repr(e))
    if len(data)<10000: raise RuntimeError(f'response too small: {len(data)} bytes')
    tmp.write_bytes(data)
    try: im=Image.open(tmp)
    except Exception as e: raise RuntimeError('decode failed: '+repr(e))
    isolated=isolate(im, session=session)
    stem=f'zte_business_{fam}_t{tier}_final'
    INCOMING.mkdir(parents=True,exist_ok=True)
    out=INCOMING/f'{stem}.png'
    isolated.save(out,'PNG',optimize=True)
    report={
      'provider':'pollinations-anonymous','target':aid,'seed':int(seed),
      'url_host':'image.pollinations.ai','candidate':str(out.relative_to(ROOT))
    }
    rp=report_path or REPORT
    rp.parent.mkdir(parents=True,exist_ok=True)
    rp.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print('POLLINATIONS_CANDIDATE='+str(out.relative_to(ROOT)))
    return out, report

def main():
    row=next_target()
    seed=int(os.getenv('POLLINATIONS_SEED','73117'))
    try:
        generate(row, seed=seed)
    except Exception as e:
        fail(str(e))

if __name__=='__main__': main()
