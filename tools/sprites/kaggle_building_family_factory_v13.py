#!/usr/bin/env python3
"""Zero -> Empire FLUX building-family factory v13.

Goals: preserve family identity, force visible T0->T6 growth, and produce clean
transparent masters without deleting internal grey/metallic surfaces.
"""
from __future__ import annotations
import argparse, gc, re
from collections import deque
from pathlib import Path

print('KAGGLE_STARTUP=building-family-flux-v13-edge-segmentation', flush=True)

import torch
from PIL import Image, ImageFilter
from diffusers import FluxPipeline, FluxImg2ImgPipeline, FluxTransformer2DModel
from transformers import T5EncoderModel

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / 'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING = ROOT / 'art/incoming/final-sprites'
FLUX = 'aniketppanchal/flux.1-schnell-nf4-pkg'
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
BLD = re.compile(r'^BLD-(\d{2})-T([0-6])$')

DNA = {
    0:'street micro foundry kiosk, rust steel, corrugated canopy, amber furnace',
    1:'corner fabrication shop, chamfered storefront, loading bay',
    2:'furnace works, masonry steel shell, orange furnace, twin stacks',
    3:'assembly hub, wide dark-steel hall, robotic spine, symmetric feeder bays',
    4:'precision fabrication works, graphite factory, three CNC bays, logistics dock',
    5:'energy-cell works, square dark-alloy factory, amber battery core, transfer bays',
    6:'coolant process plant, silver graphite pump house, twin reservoirs, cyan pipes',
    7:'automation power works, wide high-tech factory, twin gantries, power manifold',
    8:'heavy forge, armored base, articulated forge bay, warm core',
    9:'nanofabrication complex, pearl graphite process block, clean chamber, cyan ring',
    10:'orbital component works, dark-alloy logistics base, circular orbital cradle, cantilever bays',
    11:'actuator works, press-house, symmetric articulated frames, orange press channel',
    12:'phase-matter foundry, pearl-alloy base, cyan containment ring, corner fins',
    13:'stellar precision works, dark pearl base, four-part crown geometry, stellar core',
}
DELTA = {
    0:'starter: tiny one-storey shell, low roofline, sparse machinery, no tower, crane, upper deck or landmark mass',
    1:'reinforced: same starter shell plus one attached machinery enclosure and roof ribs',
    2:'industrial: same structure with wider footprint, second attached subsystem and service deck',
    3:'automated: same anchors plus compact central automation tower and attached logistics conduit',
    4:'advanced: same base and tower plus two attached machinery wings and denser routing',
    5:'megastructure: preserve prior structure and add a large attached upper production assembly and energy routing',
    6:'ultimate: preserve the complete evolved structure and add a tall central prestige crown and heroic attached machinery',
}
# Start with families that showed some useful evolution in previous runs. Known
# pathological 04/06/07 remain late until the new segmentation path is proven.
PRIORITY = (13, 5, 8, 9, 10, 12, 11, 4, 6, 7, 3, 0, 1, 2)
STRENGTH = {1:.34, 2:.42, 3:.50, 4:.58, 5:.66, 6:.72}
STEPS = {0:5, 1:4, 2:4, 3:5, 4:5, 5:6, 6:6}
RETRIES = {0:4, 1:3, 2:3, 3:3, 4:3, 5:3, 6:3}


def rows():
    for order, line in enumerate(MANIFEST.read_text(encoding='utf-8').splitlines()):
        m = ROW.match(line)
        if not m:
            continue
        aid, name, desc, runtime, status = [x.strip() for x in m.groups()]
        bm = BLD.fullmatch(aid)
        if bm and status.upper() == 'TODO' and not (ROOT / runtime).is_file():
            yield {'id':aid, 'stem':Path(runtime).stem, 'family':int(bm.group(1)), 'tier':int(bm.group(2)), 'order':order}


def select(items, count):
    by = {}
    for item in items:
        by.setdefault(item['family'], []).append(item)
    rank = {f:n for n,f in enumerate(PRIORITY)}
    out = []
    for fam in sorted(by, key=lambda f:(rank.get(f,999), f)):
        group = sorted(by[fam], key=lambda x:x['tier'])
        if out and len(out) + len(group) > count:
            continue
        out += group
        if len(out) >= count:
            break
    return out or items[:count]


def prompts(i):
    identity = f"AAA premium mobile 2.5D strategy building. Same persistent family {i['family']:02d}. Fixed DNA: {DNA[i['family']]}. {DELTA[i['tier']]}. "
    camera = "Exactly one connected building, 34 degree three-quarter orthographic camera, same orientation and camera center at every tier, bottom-center grounding, upper-left key light, cool fill, restrained cyan or warm emissives. "
    isolation = "Studio cutout render on a perfectly flat uniform neutral medium-gray background touching every image edge. Background only, no visible floor. No platform card, terrain slab, road, horizon, scenery, vignette, gradient or cast ground plane. "
    integrity = "Preserve facade, production core, roof orientation and structural anchors from the previous tier. Every new part is physically attached to the main building. No people, workers, vehicles, arrows, signs, labels, readable text, pseudo-text, letters, numbers, logos, watermark, UI, detached props, particles, debris, loose cables or disconnected pieces. Materials are continuous and intact. "
    starter = "Tier zero is unmistakably early-game and compact: one storey, low silhouette, sparse machinery, no tower, crane, gantry, upper deck or megastructure mass. " if i['tier'] == 0 else ""
    return identity + isolation + starter, identity + camera + isolation + integrity + starter


def load_encode():
    t5 = T5EncoderModel.from_pretrained(FLUX, subfolder='text_encoder_2', torch_dtype=torch.float16, device_map='cuda')
    pipe = FluxPipeline.from_pretrained(FLUX, text_encoder_2=t5, transformer=None, vae=None, torch_dtype=torch.float16, device_map='cuda')
    return t5, pipe


def load_render():
    tr = FluxTransformer2DModel.from_pretrained(FLUX, subfolder='transformer', torch_dtype=torch.float16, device_map='cuda')
    base = FluxPipeline.from_pretrained(FLUX, text_encoder=None, text_encoder_2=None, tokenizer=None, tokenizer_2=None, transformer=tr, torch_dtype=torch.float16, device_map='cuda')
    base.vae.to(device='cuda', dtype=torch.float16)
    img = FluxImg2ImgPipeline.from_pipe(base)
    img.vae.to(device='cuda', dtype=torch.float16)
    return tr, base, img


def border_stats(im):
    rgb = im.convert('RGB'); w,h = rgb.size; step = max(1, min(w,h)//128); pts=[]
    for x in range(0,w,step): pts += [rgb.getpixel((x,0)), rgb.getpixel((x,h-1))]
    for y in range(0,h,step): pts += [rgb.getpixel((0,y)), rgb.getpixel((w-1,y))]
    vals = [sum(p)/3 for p in pts]; mean = sum(vals)/len(vals)
    sd = (sum((v-mean)**2 for v in vals)/len(vals))**.5
    q = sorted(pts, key=sum)[len(pts)//3:2*len(pts)//3]
    bg = tuple(sum(p[k] for p in q)//len(q) for k in range(3))
    return bg, sd, max(bg)-min(bg)


def edge_connected_alpha(im):
    """Remove only background-like pixels connected to image edges.

    Unlike global chroma-distance masking this cannot punch transparent holes into
    enclosed metallic surfaces merely because their colour resembles the studio bg.
    """
    rgb = im.convert('RGB'); w,h = rgb.size
    bg, sd, chroma = border_stats(rgb)
    if sd > 11 or chroma > 20:
        raise RuntimeError(f'bad border sd={sd:.1f} chroma={chroma}')
    # Segment on 256px proxy for speed and topology, then upscale softly.
    proxy = rgb.resize((256,256), Image.Resampling.BILINEAR)
    px = proxy.load(); W=H=256
    def dist(p):
        return ((p[0]-bg[0])**2 + (p[1]-bg[1])**2 + (p[2]-bg[2])**2) ** .5
    seen=set(); q=deque()
    for x in range(W): q.extend(((x,0),(x,H-1)))
    for y in range(H): q.extend(((0,y),(W-1,y)))
    # Local tolerance permits gentle background compression/noise while preventing
    # traversal through stronger object edges.
    while q:
        p=q.popleft()
        if p in seen: continue
        x,y=p
        if dist(px[x,y]) > 27: continue
        seen.add(p)
        for n in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            u,v=n
            if 0<=u<W and 0<=v<H and n not in seen: q.append(n)
    alpha = Image.new('L',(W,H),255); ap=alpha.load()
    for x,y in seen: ap[x,y]=0
    # Slight erosion of background boundary removes halos without eating internals.
    alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.55))
    alpha = alpha.resize((w,h), Image.Resampling.BILINEAR)
    out = rgb.convert('RGBA'); out.putalpha(alpha)
    return out


def components(alpha):
    sm=alpha.resize((128,128),Image.Resampling.BILINEAR); px=sm.load(); seen=set(); out=[]
    for y in range(128):
        for x in range(128):
            if (x,y) in seen or px[x,y] < 32: continue
            q=deque([(x,y)]); seen.add((x,y)); pts=[]
            while q:
                a,b=q.popleft(); pts.append((a,b))
                for n in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)):
                    u,v=n
                    if 0<=u<128 and 0<=v<128 and n not in seen and px[u,v]>=32:
                        seen.add(n); q.append(n)
            if len(pts)>=50: out.append(pts)
    return sorted(out,key=len,reverse=True)


def ground_slab_score(alpha):
    sm=alpha.resize((128,128),Image.Resampling.BILINEAR); px=sm.load(); rows=[]
    for y in range(76,124): rows.append(sum(1 for x in range(6,122) if px[x,y]>=32)/116)
    return sum(1 for v in rows if v>.72)/len(rows)


def internal_hole_score(alpha):
    sm=alpha.resize((96,96),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0); px=sm.load()
    exterior=set(); q=deque()
    for x in range(96): q.extend(((x,0),(x,95)))
    for y in range(96): q.extend(((0,y),(95,y)))
    while q:
        p=q.popleft()
        if p in exterior: continue
        x,y=p
        if px[x,y]>0: continue
        exterior.add(p)
        for n in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            u,v=n
            if 0<=u<96 and 0<=v<96 and n not in exterior: q.append(n)
    inner={(x,y) for y in range(96) for x in range(96) if px[x,y]==0}-exterior
    largest=0
    while inner:
        start=inner.pop(); comp={start}; q=deque([start])
        while q:
            x,y=q.popleft()
            for n in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if n in inner: inner.remove(n); comp.add(n); q.append(n)
        largest=max(largest,len(comp))
    return largest/(96*96)


def finish(raw,tier):
    m=edge_connected_alpha(raw); a0=m.getchannel('A'); cs=components(a0)
    if not cs: raise RuntimeError('empty isolation')
    dominance=len(cs[0])/sum(map(len,cs))
    if dominance < .955: raise RuntimeError(f'detached-structure dominance={dominance:.3f}')
    slab=ground_slab_score(a0)
    if slab>.30: raise RuntimeError(f'ground-slab-score={slab:.2f}')
    hole=internal_hole_score(a0)
    # Small windows/cavities are legitimate; only large accidental holes fail.
    if hole>.055: raise RuntimeError(f'internal-hole-score={hole:.3f}')
    xs=[p[0] for p in cs[0]]; ys=[p[1] for p in cs[0]]; w,h=m.size
    box=(max(0,int(min(xs)*w/128)-36),max(0,int(min(ys)*h/128)-36),min(w,int((max(xs)+1)*w/128)+36),min(h,int((max(ys)+1)*h/128)+36))
    crop=m.crop(box); bb=crop.getbbox()
    if not bb: raise RuntimeError('empty alpha')
    crop=crop.crop(bb); side=2048
    maxw=.70 if tier==0 else .78; maxh=.60 if tier==0 else .78
    scale=min(side*maxw/crop.width, side*maxh/crop.height)
    crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
    out=Image.new('RGBA',(side,side)); out.alpha_composite(crop,((side-crop.width)//2,side-int(side*.10)-crop.height))
    a=out.getchannel('A'); cov=sum(a.histogram()[8:])/(side*side)
    if cov < (.05 if tier==0 else .065) or cov>.58: raise RuntimeError(f'coverage {cov:.1%}')
    pad=int(side*.08)
    if any(e.getbbox() for e in (a.crop((0,0,side,pad)),a.crop((0,side-pad,side,side)),a.crop((0,0,pad,side)),a.crop((side-pad,0,side,side)))):
        raise RuntimeError('padding')
    return out,cov


def mask64(im): return im.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)

def iou(a,b):
    A=mask64(a);B=mask64(b);pa=A.load();pb=B.load();inter=union=0
    for y in range(64):
        for x in range(64):
            aa=pa[x,y]>0; bb=pb[x,y]>0; inter+=aa and bb; union+=aa or bb
    return inter/union if union else 0

def bbox_metrics(im):
    bb=mask64(im).getbbox()
    return (0,0,0,0) if not bb else (bb[2]-bb[0],bb[3]-bb[1],(bb[0]+bb[2])/2,(bb[1]+bb[3])/2)


def family_qa(recs):
    if len(recs)<2: return True,'single'
    adj=[iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
    if min(adj)<.33: return False,f'identity-iou={min(adj):.2f}'
    cov=[r[2] for r in recs]
    severe_drops=sum(1 for a,b in zip(cov,cov[1:]) if b<a*.90)
    if severe_drops>1: return False,f'nonmonotonic-coverage={cov}'
    growth=cov[-1]/max(cov[0],1e-9)
    if growth<1.40: return False,f'insufficient-growth={growth:.2f}x'
    boxes=[bbox_metrics(r[1]) for r in recs]; cx0=boxes[0][2]
    drift=max(abs(b[2]-cx0) for b in boxes)
    if drift>6.5: return False,f'horizontal-drift={drift:.1f}'
    if iou(recs[0][1],recs[-1][1])>.91: return False,'insufficient-evolution'
    return True,f'min-adj-iou={min(adj):.2f} growth={growth:.2f}x drift={drift:.1f}'


def render_with_retries(i, previous, pe, ppe, base, img, seed):
    errors=[]
    for attempt in range(RETRIES.get(i['tier'],3)):
        attempt_seed=seed + attempt*7919
        gen=torch.Generator(device='cuda').manual_seed(attempt_seed)
        try:
            with torch.inference_mode():
                if previous is None:
                    raw=base(height=1024,width=1024,num_inference_steps=STEPS[i['tier']],guidance_scale=0,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),output_type='pil',generator=gen).images[0]
                    mode='anchor'
                else:
                    strength=min(.78,max(.28,STRENGTH.get(i['tier'],.5)+(attempt-1)*.035))
                    raw=img(image=previous,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),strength=strength,num_inference_steps=STEPS[i['tier']],guidance_scale=0,output_type='pil',generator=gen).images[0]
                    mode=f'img2img-s{strength:.2f}'
            final,cov=finish(raw,i['tier'])
            print(f"KAGGLE_RENDERED={i['id']} mode={mode} attempt={attempt+1} coverage={cov:.1%}",flush=True)
            return raw.convert('RGB'),final,cov
        except Exception as e:
            errors.append(f'{type(e).__name__}:{e}')
            print(f"KAGGLE_RETRY={i['id']} attempt={attempt+1} reason={errors[-1]}",flush=True)
        finally:
            gc.collect(); torch.cuda.empty_cache()
    raise RuntimeError(' | '.join(errors[-3:]))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--count',type=int,default=28); ap.add_argument('--seed',type=int,default=43117); args=ap.parse_args()
    items=select(list(rows()),max(1,args.count)); print('KAGGLE_BUILDING_PLAN='+','.join(i['id'] for i in items),flush=True)
    if not items: return
    INCOMING.mkdir(parents=True,exist_ok=True)
    emb={}; t5,enc=load_encode()
    for i in items:
        try:
            short,long=prompts(i)
            with torch.no_grad(): pe,ppe,_=enc.encode_prompt(prompt=short,prompt_2=long,max_sequence_length=256)
            emb[i['id']]=(pe.cpu(),ppe.cpu())
        except Exception as e:
            print(f"KAGGLE_REJECTED={i['id']} stage=encode reason={e}",flush=True)
    del t5,enc; gc.collect(); torch.cuda.empty_cache()
    tr,base,img=load_render(); by={}
    for i in items:
        if i['id'] in emb: by.setdefault(i['family'],[]).append(i)
    accepted=[]; rejected=0
    for fam,group in sorted(by.items(),key=lambda kv:PRIORITY.index(kv[0]) if kv[0] in PRIORITY else 999):
        group.sort(key=lambda x:x['tier']); recs=[]; previous=None; failed=False
        for i in group:
            pe,ppe=emb[i['id']]
            try:
                previous,final,cov=render_with_retries(i,previous,pe,ppe,base,img,args.seed+fam*1000+i['tier']*101)
                recs.append((i,final,cov))
            except Exception as e:
                print(f"KAGGLE_REJECTED={i['id']} stage=render reason={e}",flush=True); failed=True; rejected+=1; break
        if failed or len(recs)!=len(group):
            rejected+=max(0,len(group)-len(recs)); continue
        ok,why=family_qa(recs)
        if not ok:
            for i,_,_ in recs: print(f"KAGGLE_REJECTED={i['id']} stage=family_qa reason={why}",flush=True)
            rejected+=len(recs); continue
        for i,final,cov in recs:
            p=INCOMING/f"{i['stem']}.png"; final.save(p,'PNG',optimize=True); accepted.append(i['id'])
            print(f"KAGGLE_VALIDATED={p.relative_to(ROOT)} coverage={cov:.1%} {why}",flush=True)
    print(f'KAGGLE_BUILDING_SUCCESS={len(accepted)} KAGGLE_BUILDING_REJECTED={rejected} KAGGLE_BUILDING_ATTEMPTED={len(items)}',flush=True)

if __name__=='__main__': main()
