#!/usr/bin/env python3
from __future__ import annotations
import json, os, re, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image, ImageFilter

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
REPORT=ROOT/'art/production/pollinations-report.json'

FAMILY_IDENTITY={
    0:'Street Stand, compact improvised street-production kiosk',
    1:'Corner Shop, small neighborhood retail-production storefront',
    2:'Workshop, compact mechanical fabrication workshop',
    3:'Factory, industrial production plant',
    4:'Tech Company, premium technology headquarters and R&D production campus',
    5:'Megacity, dense futuristic urban production district',
    6:'Moon Colony, pressurized lunar industrial colony',
    7:'Mars Empire, monumental Martian industrial-government complex',
    8:'Dyson Network, stellar-energy collection and routing complex',
    9:'Galactic Exchange, interstellar trade and finance hub',
    10:'Intergalactic Gateway, deep-space transit gateway complex',
    11:'Cosmic Foundry, cosmic-scale fabrication facility',
    12:'Reality Engine, exotic-physics reality-processing machine complex',
    13:'Transcendent Nexus, apex civilization energy nexus',
}

TIER_LANGUAGE={
    0:'starter version: smallest footprint, low verticality, one obvious core function, improvised but intentional construction',
    1:'reinforced version: same base silhouette lineage, slightly larger footprint, stronger structure, one dedicated subsystem',
    2:'expanded version: preserve the same family architecture while adding a second visible subsystem and more technical detail',
    3:'automated version: same family DNA, visibly larger and taller, logistics/automation modules, controlled emissive accents',
    4:'district-scale version: same unmistakable family identity, larger footprint and vertical landmark massing, dense machinery and premium materials',
    5:'megastructure version: same architecture evolved upward, multi-stage production, major energy routing, substantially larger and more prestigious',
    6:'mastered ultimate version: same family silhouette lineage at maximum scale and verticality, iconic crown/hero element, richest materials and systems',
}


def fetch_image(prompt:str, seed:int, width:int=1024, height:int=1024):
    q=urllib.parse.quote(prompt,safe='')
    url=f'https://image.pollinations.ai/prompt/{q}?model=flux&width={width}&height={height}&seed={int(seed)}&nologo=true&private=true&enhance=false&safe=true'
    tmp=Path(f'/tmp/pollinations-board-{int(seed)}-{width}x{height}.png')
    req=urllib.request.Request(url,headers={'User-Agent':'zero-to-empire-github-actions/1.0'})
    with urllib.request.urlopen(req,timeout=120) as r:
        data=r.read()
    if len(data)<10000:
        raise RuntimeError(f'response too small: {len(data)} bytes')
    tmp.write_bytes(data)
    return Image.open(tmp).convert('RGBA')

def generate_family(rows, seed=73117, session=None):
    if not rows:
        raise RuntimeError('empty family rows')
    parsed=[]
    family=None
    for row in rows:
        aid=row[0]
        m=re.fullmatch(r'BLD-(\d{2})-T(\d)',aid)
        if not m:
            raise RuntimeError('bad target '+aid)
        fam,tier=m.groups()
        if family is None:
            family=int(fam)
        if int(fam)!=family:
            raise RuntimeError('mixed building families in family-board generation')
        parsed.append((int(tier),row))
    parsed.sort(key=lambda x:x[0])
    identity=FAMILY_IDENTITY.get(family,f'industrial business family {family}')
    tiers='; '.join(f'T{tier}: {TIER_LANGUAGE[tier]}' for tier,_ in parsed)
    prompt=(
        f'AAA premium mobile tycoon game architectural evolution board for ONE canonical family: {identity}. '
        'Show exactly seven versions of the SAME building lineage in chronological progression T0 through T6. '
        f'{tiers}. '
        'Compose a clean 4-column by 2-row contact sheet: first seven cells are T0,T1,T2,T3,T4,T5,T6 in reading order; eighth cell empty. '
        'Every occupied cell uses the same 34-degree three-quarter orthographic camera, same upper-left warm-neutral key light, same cool fill, same material palette and same core architectural DNA. '
        'Progression must be strictly monotonic: each next tier is visibly larger, taller, denser, more automated and more prestigious than the previous tier while preserving recognizable base massing. '
        'Graphite/dark premium structure, restrained cyan and warm amber emissive accents. One connected building per cell only. '
        'No people, no vehicles, no text, no labels, no numbers, no logos, no detached props, no roads, no scenery, no floor slabs, no floating platforms, no background architecture, no borders. '
        'Perfectly flat uniform neutral gray behind every cell.'
    )
    raw=fetch_image(prompt,seed,1024,1024)
    outputs=[]
    for idx,(tier,row) in enumerate(parsed):
        col=idx%4; r=idx//4
        crop=raw.crop((col*256,r*512,(col+1)*256,(r+1)*512))
        isolated=isolate(crop,session=session)
        aid=row[0]
        fam=f'{family:02d}'
        stem=f'zte_business_{fam}_t{tier}_final'
        INCOMING.mkdir(parents=True,exist_ok=True)
        out=INCOMING/f'{stem}.png'
        isolated.save(out,'PNG',optimize=True)
        report={
            'provider':'pollinations-anonymous',
            'target':aid,
            'seed':int(seed),
            'generation':'single-family-board',
            'family':family,
            'candidate':str(out.relative_to(ROOT))
        }
        rp=ROOT/'art/production'/f'pollinations-{aid.lower()}-report.json'
        rp.write_text(json.dumps(report,indent=2),encoding='utf-8')
        outputs.append((row,out,report))
        print('POLLINATIONS_FAMILY_CANDIDATE='+aid+' '+str(out.relative_to(ROOT)))
    return outputs

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
    fam_i=int(fam); tier_i=int(tier)
    identity=FAMILY_IDENTITY.get(fam_i,f'industrial business family {fam_i}')
    tier_language=TIER_LANGUAGE[tier_i]
    prompt=(
      f'AAA premium mobile tycoon game building sprite. Canonical family: {identity}. '
      f'Tier {tier_i} of 6; {tier_language}. '
      'This must look like an evolved version of the SAME architectural family across all tiers, not a different building type. '
      'Maintain a consistent 34-degree three-quarter orthographic camera, upper-left warm-neutral key light, cool fill, graphite/dark premium massing with restrained cyan and warm amber emissive accents. '
      'Single connected building only, centered, readable silhouette, subject occupies 58 to 66 percent of canvas, generous transparent-safe margin. '
      'No people, no vehicles, no readable text, no signs, no logo, no detached props, no crane, no scenery, no road, no floor slab, no floating platform, no background architecture. '
      'Perfectly flat uniform neutral gray background, no gradient, no vignette, no horizon.'
    )
    q=urllib.parse.quote(prompt,safe='')
    url=f'https://image.pollinations.ai/prompt/{q}?model=flux&width=1024&height=1024&seed={int(seed)}&nologo=true&private=true&enhance=false&safe=true'
    tmp=Path(f'/tmp/pollinations-{aid.lower()}-{int(seed)}.png')
    req=urllib.request.Request(url,headers={'User-Agent':'zero-to-empire-github-actions/1.0'})
    try:
        with urllib.request.urlopen(req,timeout=90) as r:
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
