#!/usr/bin/env python3
"""Sequential FLUX img2img building-family factory for Zero -> Empire.

v8 prioritizes untouched late-game families, strengthens monotonic tier morphology,
and keeps strict isolation/family QA before a candidate can leave Kaggle. Isolation
accepts a uniform neutral black/white/gray edge field because FLUX can invert the
requested studio background while still producing a clean, safely detachable master.
"""
from __future__ import annotations
import argparse, gc, re
from collections import deque
from pathlib import Path
print('KAGGLE_STARTUP=building-family-flux-v8-neutral-background-isolation', flush=True)
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

FAMILY_DNA = {
 0:'street-side micro foundry kiosk; rust-dark steel frame, corrugated canopy, compact exposed workbench, amber furnace cue',
 1:'corner fabrication shop; chamfered L-shaped storefront shell, dark steel and concrete, sheltered loading bay, compact cyan service lights',
 2:'furnace works; squat heatproof masonry-and-steel shell, dominant orange-hot furnace chamber, twin exhaust stacks, heavy insulated piping',
 3:'assembly hub; low wide rectangular dark-steel production hall; central open robotic assembly spine; two symmetric side feeder bays; four corner posts; flat ribbed roof frame; cyan status strips',
 4:'precision fabrication works; low wide graphite rectangular factory; three enclosed CNC bay modules across front; ribbed flat roof; right-side compact logistics dock; cyan corner strips',
 5:'energy-cell works; square dark-alloy factory; central amber battery handling core visible through front; two symmetric side transfer bays; heavy square roof frame; cyan lower service strips',
 6:'coolant process plant; low wide silver-graphite rectangular pump house; two cylindrical reservoir anchors at rear-left and rear-right; central rigid coolant loop; cyan fluid pipes along base',
 7:'automation power works; wide rectangular high-tech factory; two overhead gantry anchors; central power manifold; four structural portal posts; cyan bus conduits',
 8:'heavy forge; armored rectangular base; central articulated forge bay; two reinforced side ribs; large front service aperture; warm forge core',
 9:'nanofabrication complex; sealed pearl-and-graphite square process block; central clean chamber; two smooth layered side shells; cyan routing ring',
 10:'orbital component works; dark-alloy rectangular logistics base; central circular orbital assembly cradle embedded in roof; two cantilevered side bays; cyan levitation seams',
 11:'actuator works; rectangular press-house base; two symmetric articulated side frames; armored square plinth; central vertical orange press channel',
 12:'phase-matter foundry; pearl-alloy square base; luminous cyan containment ring around central fabrication cradle; four elegant corner-fin anchors',
 13:'stellar precision works; dark-and-pearl square base; four-part crown anchor geometry; bright contained central process core; warm stellar plus cyan accents',
}
TIER_DELTA = {
 0:'STARTER ONLY: one-storey compact low building, bare shell, improvised cladding, one production cue, no tower, no crown, no megastructure scale',
 1:'REINFORCED: keep the full T0 shell; add one attached machinery enclosure and roof ribs; remain mostly one-storey and only modestly taller',
 2:'INDUSTRIAL: keep T0 and T1 readable; widen both sides, add a second attached subsystem and a partial upper service deck; clearly broader than T1',
 3:'AUTOMATED: preserve every prior anchor; add one central automation tower rising about one base-storey above the roof and one attached logistics conduit',
 4:'ADVANCED: preserve the same base and tower; add two attached side machinery wings, denser routing and premium cladding; visibly larger than T3',
 5:'MEGASTRUCTURE: preserve all lower tiers; add a large upper production assembly spanning the center, multi-stage machinery and explicit energy routing; substantially taller and broader than T4',
 6:'ULTIMATE: preserve the entire evolved structure; add a tall prestige crown directly above the central axis plus heroic attached machinery; unmistakably tallest, densest and most iconic tier',
}
# Advance fresh families first so a failed family cannot monopolize every GPU batch.
PRIORITY = (10,11,12,13,3,5,6,4,7,8,9,0,1,2)
STRENGTH = {1:.38, 2:.48, 3:.58, 4:.66, 5:.74, 6:.82}

def rows():
    for order,line in enumerate(MANIFEST.read_text(encoding='utf-8').splitlines()):
        m=ROW.match(line)
        if not m: continue
        asset_id,name,desc,runtime,status=[x.strip() for x in m.groups()]
        bm=BLD.fullmatch(asset_id)
        if bm and status.upper()=='TODO':
            yield {'id':asset_id,'name':name,'description':desc,'runtime':runtime,'stem':Path(runtime).stem,
                   'family':int(bm.group(1)),'tier':int(bm.group(2)),'order':order}

def select(items,count):
    by={}
    for i in items: by.setdefault(i['family'],[]).append(i)
    rank={fam:n for n,fam in enumerate(PRIORITY)}; chosen=[]
    for fam in sorted(by,key=lambda f:(rank.get(f,999),f)):
        group=sorted(by[fam],key=lambda x:x['tier'])
        if chosen and len(chosen)+len(group)>count: continue
        chosen.extend(group)
        if len(chosen)>=count: break
    return chosen or items[:count]

def prompts(i):
    short=(
      f"AAA 2.5D strategy building F{i['family']:02d} tier {i['tier']}. SAME building upgraded in place. "
      f"{TIER_DELTA[i['tier']]}. Preserve facade and anchors. One connected isolated building on a perfectly uniform neutral studio background. No text, logo, people, vehicles or UI."
    )
    detailed=(
      f"AAA premium mobile strategy BUILDING MASTER. FIXED FAMILY DNA F{i['family']:02d}: {FAMILY_DNA[i['family']]}. "
      f"TIER {i['tier']} MORPHOLOGY: {TIER_DELTA[i['tier']]}. This is the SAME physical building upgraded in place, never a redesign. "
      "MONOTONIC EVOLUTION IS MANDATORY: every tier must retain all prior structural anchors and add visibly more footprint, machinery and vertical hierarchy; never shrink back to an earlier silhouette. "
      "Same camera-facing facade, same production-core position, same main roof orientation. Additions must be physically attached to the existing structure. Exactly one connected self-contained building. "
      "Fixed 34 degree three-quarter orthographic-like 2.5D camera, bottom-center grounding, upper-left key light, cool fill, restrained warm/cyan emissives. "
      "ISOLATION MANDATORY: perfectly uniform neutral achromatic background touching every edge; pure black, white or gray is acceptable; no gradient, vignette, halo, pedestal, backdrop rectangle, studio panel, horizon, road, landscape, sky or floor card. "
      "No detached props, workers, vehicles, readable text, letters, numbers, currency, signage, badge, logo, watermark or UI."
    )
    return short,detailed

def load_encode():
    t=T5EncoderModel.from_pretrained(FLUX,subfolder='text_encoder_2',torch_dtype=torch.float16,device_map='cuda')
    p=FluxPipeline.from_pretrained(FLUX,text_encoder_2=t,transformer=None,vae=None,torch_dtype=torch.float16,device_map='cuda')
    return t,p

def load_render():
    tr=FluxTransformer2DModel.from_pretrained(FLUX,subfolder='transformer',torch_dtype=torch.float16,device_map='cuda')
    base=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,
                                      transformer=tr,torch_dtype=torch.float16,device_map='cuda')
    try:
        img=FluxImg2ImgPipeline.from_pipe(base)
    except Exception:
        img=FluxImg2ImgPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,
                                                transformer=tr,vae=base.vae,torch_dtype=torch.float16,device_map='cuda')
    return tr,base,img

def border_stats(im):
    rgb=im.convert('RGB'); w,h=rgb.size; s=max(1,min(w,h)//128); pts=[]
    for x in range(0,w,s): pts += [rgb.getpixel((x,0)),rgb.getpixel((x,h-1))]
    for y in range(0,h,s): pts += [rgb.getpixel((0,y)),rgb.getpixel((w-1,y))]
    vals=[sum(p)/3 for p in pts]; mean=sum(vals)/len(vals); var=sum((v-mean)**2 for v in vals)/len(vals)
    # Median-ish border estimate is robust for both near-black and near-white generations.
    ordered=sorted(pts,key=sum); q=ordered[len(ordered)//3: max(len(ordered)//3+1, 2*len(ordered)//3)]
    bg=tuple(sum(p[k] for p in q)//len(q) for k in range(3))
    chroma=max(bg)-min(bg)
    return bg,mean,var**.5,chroma

def isolate(im):
    rgb=im.convert('RGB'); w,h=rgb.size; bg,mean,sd,chroma=border_stats(rgb)
    # Background brightness is irrelevant after alpha extraction. What matters is a
    # uniform, neutral edge field: gradients/scenery and tinted halos remain rejected.
    if sd>8 or chroma>14:
        raise RuntimeError(f'non-uniform/non-neutral border mean={mean:.1f} sd={sd:.1f} chroma={chroma}')
    px=rgb.load(); dist=Image.new('L',(w,h)); dp=dist.load()
    for y in range(h):
        for x in range(w):
            r,g,b=px[x,y]; dp[x,y]=min(255,int((((r-bg[0])**2+(g-bg[1])**2+(b-bg[2])**2)**.5)*3))
    mask=dist.point(lambda p:0 if p<20 else 255 if p>58 else int((p-20)*255/38)).filter(ImageFilter.GaussianBlur(.6))
    rgba=rgb.convert('RGBA'); rgba.putalpha(mask); return rgba

def comps(alpha,threshold=32):
    sm=alpha.resize((128,128),Image.Resampling.BILINEAR); px=sm.load(); seen=set(); out=[]
    for y in range(128):
        for x in range(128):
            if (x,y) in seen or px[x,y]<threshold: continue
            q=deque([(x,y)]); seen.add((x,y)); pts=[]
            while q:
                cx,cy=q.popleft(); pts.append((cx,cy))
                for n in ((cx-1,cy),(cx+1,cy),(cx,cy-1),(cx,cy+1)):
                    nx,ny=n
                    if 0<=nx<128 and 0<=ny<128 and n not in seen and px[nx,ny]>=threshold:
                        seen.add(n); q.append(n)
            if len(pts)>=50: out.append(pts)
    return sorted(out,key=len,reverse=True)

def finish(image):
    master=isolate(image); cs=comps(master.getchannel('A'))
    if not cs: raise RuntimeError('empty isolated building')
    total=sum(map(len,cs)); dominant=len(cs[0])/total
    if len(cs)>1 and dominant<.90: raise RuntimeError('detached secondary structure')
    xs=[x for x,y in cs[0]]; ys=[y for x,y in cs[0]]; w,h=master.size
    box=(max(0,int(min(xs)*w/128)-30),max(0,int(min(ys)*h/128)-30),min(w,int((max(xs)+1)*w/128)+30),min(h,int((max(ys)+1)*h/128)+30))
    crop=master.crop(box); bbox=crop.getbbox()
    if not bbox: raise RuntimeError('empty alpha')
    crop=crop.crop(bbox); side=2048; scale=min(side*.80/crop.width,side*.78/crop.height)
    crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
    out=Image.new('RGBA',(side,side)); out.alpha_composite(crop,((side-crop.width)//2,side-int(side*.10)-crop.height))
    a=out.getchannel('A'); lo,hi=a.getextrema(); visible=sum(a.histogram()[8:])/(side*side)
    if hi==0 or lo==255 or visible<.07 or visible>.62: raise RuntimeError(f'alpha coverage {visible:.1%}')
    pad=int(side*.08)
    if any(e.getbbox() for e in (a.crop((0,0,side,pad)),a.crop((0,side-pad,side,side)),a.crop((0,0,pad,side)),a.crop((side-pad,0,side,side)))):
        raise RuntimeError('8-percent safety padding failed')
    return out,visible

def mask64(im):
    return im.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)

def sig(im):
    b=mask64(im); box=b.getbbox()
    if not box:return None
    x0,y0,x1,y1=box; return (x1-x0,y1-y0,(x0+x1)/2,(y0+y1)/2,(x1-x0)*(y1-y0))

def iou(a,b):
    A=mask64(a); B=mask64(b); pa=A.load(); pb=B.load(); inter=union=0
    for y in range(64):
        for x in range(64):
            aa=pa[x,y]>0; bb=pb[x,y]>0; inter += aa and bb; union += aa or bb
    return inter/union if union else 0.0

def family_qa(recs):
    if len(recs)<2: return True,'single'
    ss=[sig(r[1]) for r in recs]
    if any(s is None for s in ss): return False,'empty-silhouette'
    if max(s[2] for s in ss)-min(s[2] for s in ss)>6: return False,'camera-center-drift'
    adj=[iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
    if min(adj)<.40: return False,f'identity-iou={min(adj):.2f}'
    first_last=iou(recs[0][1],recs[-1][1])
    if first_last>.90: return False,f'insufficient-tier-evolution-iou={first_last:.2f}'
    return True,f'min_adj_iou={min(adj):.2f},first_last_iou={first_last:.2f}'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--count',type=int,default=30); ap.add_argument('--seed',type=int,default=43117); args=ap.parse_args()
    items=select(list(rows()),max(1,args.count)); print('KAGGLE_BUILDING_PLAN='+','.join(i['id'] for i in items),flush=True)
    if not items:return
    INCOMING.mkdir(parents=True,exist_ok=True)
    embeddings={}; t,enc=load_encode()
    for item in items:
        try:
            short,detailed=prompts(item)
            with torch.no_grad(): pe,ppe,_=enc.encode_prompt(prompt=short,prompt_2=detailed,max_sequence_length=384)
            embeddings[item['id']] = (pe.cpu(),ppe.cpu())
        except Exception as exc: print(f"KAGGLE_REJECTED={item['id']} stage=encode reason={exc}",flush=True)
    del t,enc; gc.collect(); torch.cuda.empty_cache()
    tr,base,imgpipe=load_render(); by={}
    for i in items:
        if i['id'] in embeddings: by.setdefault(i['family'],[]).append(i)
    accepted=[]; rejected=0
    for fam,group in sorted(by.items()):
        group.sort(key=lambda x:x['tier']); recs=[]; previous=None; failed=False
        family_seed=args.seed+fam*1000
        for item in group:
            pe,ppe=embeddings[item['id']]
            try:
                gen=torch.Generator(device='cuda').manual_seed(family_seed + item['tier']*17)
                if previous is None:
                    raw=base(height=1024,width=1024,num_inference_steps=4,guidance_scale=0.0,
                             prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),output_type='pil',
                             max_sequence_length=384,generator=gen).images[0]
                    mode='anchor'
                else:
                    raw=imgpipe(image=previous,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),
                                strength=STRENGTH.get(item['tier'],.50),num_inference_steps=8,guidance_scale=0.0,
                                output_type='pil',max_sequence_length=384,generator=gen).images[0]
                    mode='img2img'
                final,cov=finish(raw); recs.append((item,final,cov)); previous=raw.convert('RGB')
                print(f"KAGGLE_RENDERED={item['id']} mode={mode} strength={STRENGTH.get(item['tier'],0):.2f} coverage={cov:.1%}",flush=True)
            except Exception as exc:
                print(f"KAGGLE_REJECTED={item['id']} stage=render reason={type(exc).__name__}: {exc}",flush=True); failed=True; rejected+=1; break
            finally:
                gc.collect(); torch.cuda.empty_cache()
        if failed or len(recs)!=len(group):
            rejected += max(0,len(group)-len(recs)); continue
        ok,why=family_qa(recs)
        if not ok:
            for item,_,_ in recs: print(f"KAGGLE_REJECTED={item['id']} stage=family_qa reason={why}",flush=True)
            rejected += len(recs); continue
        for item,final,cov in recs:
            path=INCOMING/f"{item['stem']}.png"; final.save(path,'PNG',optimize=True); accepted.append(item['id'])
            print(f"KAGGLE_VALIDATED={path.relative_to(ROOT)} coverage={cov:.1%} family_qa={why}",flush=True)
    print(f"KAGGLE_BUILDING_SUCCESS={len(accepted)} KAGGLE_BUILDING_REJECTED={rejected} KAGGLE_BUILDING_ATTEMPTED={len(items)}",flush=True)

if __name__=='__main__': main()
