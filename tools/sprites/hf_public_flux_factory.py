#!/usr/bin/env python3
from __future__ import annotations
import json, os, re, shutil, sys, tempfile
from pathlib import Path
from PIL import Image, ImageChops, ImageFilter

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
REPORT=ROOT/'art/production/hf-public-flux-report.json'

def fail(msg):
    print('HF_PUBLIC_FLUX_ERROR='+msg, file=sys.stderr)
    raise SystemExit(1)

def next_target():
    explicit=os.getenv('SPRITE_TARGET','').strip().upper()
    rows=[]
    for line in MANIFEST.read_text(encoding='utf-8').splitlines():
        if not line.startswith('|') or 'app/src/main/res/' not in line: continue
        cols=[c.strip() for c in line.split('|')[1:-1]]
        if len(cols)!=5 or cols[4].upper()!='TODO': continue
        if cols[0].startswith('BLD-'): rows.append(cols)
    if explicit:
        for r in rows:
            if r[0]==explicit: return r
        fail('requested target is not a TODO building: '+explicit)
    if not rows: fail('no TODO building targets remain')
    return rows[0]

def prompt_for(asset_id, desc):
    m=re.fullmatch(r'BLD-(\d{2})-T(\d)', asset_id)
    if not m: fail('unsupported target '+asset_id)
    fam,tier=int(m.group(1)),int(m.group(2))
    return (
      f'AAA premium mobile strategy game industrial factory sprite, family {fam}, evolution tier {tier}. '
      f'{desc}. Single connected factory building only, centered, 34-degree orthographic three-quarter view, '
      'graphite steel alloy architecture, restrained amber and cyan emissive accents, upper-left key light, '
      'clean readable silhouette, no people, no vehicles, no text, no signs, no crane, no scaffolding, '
      'no road, no terrain, no floor slab, no platform, no scenery, no loose props. '
      'Perfectly flat uniform neutral gray background reaching every image edge, no gradient, no vignette, no horizon.'
    )

def isolate(im: Image.Image) -> Image.Image:
    rgb=im.convert('RGB')
    # Estimate background from border pixels and require low-variance border.
    px=rgb.load(); w,h=rgb.size
    samples=[]
    for x in range(w):
        samples.append(px[x,0]); samples.append(px[x,h-1])
    for y in range(h):
        samples.append(px[0,y]); samples.append(px[w-1,y])
    med=tuple(sorted(v[i] for v in samples)[len(samples)//2] for i in range(3))
    dev=max(max(abs(v[i]-med[i]) for i in range(3)) for v in samples)
    if dev>28: fail(f'bad border variance={dev}')
    src=rgb.load()
    rgba=Image.new('RGBA',rgb.size,(0,0,0,0)); out=rgba.load()
    for y in range(h):
        for x in range(w):
            p=src[x,y]
            d=max(abs(p[i]-med[i]) for i in range(3))
            if d<=18: a=0
            elif d>=42: a=255
            else: a=round((d-18)*255/24)
            out[x,y]=(p[0],p[1],p[2],a)
    a=rgba.getchannel('A').filter(ImageFilter.MedianFilter(3))
    rgba.putalpha(a)
    if not a.getbbox(): fail('empty isolation')
    return rgba

def main():
    try:
        from gradio_client import Client
    except Exception as e:
        fail('gradio_client unavailable: '+str(e))
    row=next_target(); asset_id, name, desc, runtime, status=row
    prompt=prompt_for(asset_id,desc)
    token=os.getenv('HF_TOKEN') or None
    client=Client('black-forest-labs/FLUX.1-schnell', hf_token=token, verbose=False)
    api=client.view_api(return_format='dict')
    print('HF_PUBLIC_FLUX_API='+json.dumps(api)[:4000], flush=True)
    result=None; errors=[]
    calls=[
      dict(api_name='/infer', args=(prompt,73117,False,1024,1024,4)),
      dict(fn_index=0, args=(prompt,73117,False,1024,1024,4)),
    ]
    for call in calls:
        try:
            kwargs={k:v for k,v in call.items() if k!='args'}
            result=client.predict(*call['args'], **kwargs)
            break
        except Exception as e:
            errors.append(str(e))
    if result is None: fail('generation failed: '+' | '.join(errors))
    # Gradio commonly returns (image, seed) or a filepath.
    candidate=result[0] if isinstance(result,(list,tuple)) else result
    if isinstance(candidate,dict):
        candidate=candidate.get('path') or candidate.get('url')
    if not candidate: fail('no image path in Space response')
    src=Path(str(candidate))
    if not src.exists(): fail('returned image is not a local downloaded file: '+str(candidate))
    im=Image.open(src)
    isolated=isolate(im)
    m=re.fullmatch(r'BLD-(\d{2})-T(\d)',asset_id)
    stem=f'zte_business_{m.group(1)}_t{m.group(2)}_final'
    INCOMING.mkdir(parents=True,exist_ok=True)
    out=INCOMING/f'{stem}.png'
    isolated.save(out,'PNG',optimize=True)
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text(json.dumps({
      'provider':'black-forest-labs/FLUX.1-schnell Space',
      'target':asset_id,'prompt':prompt,'candidate':str(out.relative_to(ROOT))
    },indent=2),encoding='utf-8')
    print('HF_PUBLIC_FLUX_CANDIDATE='+str(out.relative_to(ROOT)))

if __name__=='__main__': main()
