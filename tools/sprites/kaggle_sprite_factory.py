#!/usr/bin/env python3
"""Mass-generate static Zero -> Empire sprite candidates on a Kaggle GPU."""
from __future__ import annotations
import argparse, os, re
from collections import deque
from pathlib import Path
print("KAGGLE_STARTUP=python", flush=True)
import torch
from PIL import Image, ImageFilter
from diffusers import StableDiffusionXLPipeline, UNet2DConditionModel, EulerDiscreteScheduler
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file
ROOT=Path(__file__).resolve().parents[2]; MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'; INCOMING=ROOT/'art/incoming/final-sprites'
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
SUPPORTED=('PRP-','VEH-','CORE-','BLD-'); PRIORITY={'PRP':0,'VEH':1,'CORE':2,'BLD':3}; TARGET_SIDE={'BLD':2048,'CORE':1536,'VEH':1536,'PRP':1024}
BASE=os.getenv('KAGGLE_SPRITE_BASE','stabilityai/stable-diffusion-xl-base-1.0'); LIGHTNING_REPO='ByteDance/SDXL-Lightning'; LIGHTNING_CKPT='sdxl_lightning_4step_unet.safetensors'
def manifest_rows():
 order=0
 for line in MANIFEST.read_text(encoding='utf-8').splitlines():
  m=ROW.match(line)
  if not m: continue
  asset_id,name,description,runtime,status=[x.strip() for x in m.groups()]
  if not asset_id.startswith(SUPPORTED) or status.upper()!='TODO': continue
  stem=Path(runtime).stem
  if (ROOT/runtime).exists() or (INCOMING/f'{stem}.png').exists(): continue
  kind=asset_id.split('-',1)[0]; yield {'id':asset_id,'name':name,'description':description,'runtime':runtime,'stem':stem,'kind':kind,'order':order}; order+=1
def concrete_subject(i):
 if i['kind']!='PRP': return i['name']
 m=re.fullmatch(r'PRP-(\d{2})-([AB])',i['id'])
 if not m: return i['name']
 idx=int(m.group(1)); variant=m.group(2)
 if variant=='A':
  names=['closed rugged supply crate','closed compact retail stock crate','closed heatproof tool chest','closed assembly parts bin','closed industrial logistics crate','closed sealed component case','closed reinforced tool locker','closed automation parts crate','closed high-tech cargo case','closed energy-cell storage box','closed precision maintenance chest','closed orbital supply container','closed phase-tech component crate','closed prestige equipment case']
 else:
  names=['short utility pipe junction','compact safety barrier','insulated service pipe','small control terminal','utility bollard','cable junction pedestal','compact pipe manifold','service terminal','coolant pipe junction','power distribution post','sensor bollard','orbital service terminal','phase conduit junction','prestige light bollard']
 return names[min(idx,len(names)-1)]
def prompt_for(i):
 subject=concrete_subject(i)
 prefix={'BLD':'ONE industrial building','CORE':'ONE power reactor core','VEH':'ONE vehicle','PRP':'ONE standalone prop'}[i['kind']]
 # Keep this deliberately short: SDXL CLIP is a 77-token family and long negative lists
 # were both truncated and encouraged concept-sheet compositions.
 return f"{prefix}, {subject}, centered product render, isolated, 2.5D isometric 34 degree view, complete object fully visible, black empty background, no floor, no scene, no other objects, no variants, no collage, no sheet, no text, AAA mobile game asset, upper-left studio light, cyan amber details"
def load_pipe():
 token=os.getenv('HF_TOKEN') or None; print(f'KAGGLE_MODEL=begin base={BASE}',flush=True)
 unet=UNet2DConditionModel.from_config(BASE,subfolder='unet',token=token).to('cuda',torch.float16); ckpt=hf_hub_download(LIGHTNING_REPO,LIGHTNING_CKPT,token=token); unet.load_state_dict(load_file(ckpt,device='cuda'))
 pipe=StableDiffusionXLPipeline.from_pretrained(BASE,unet=unet,torch_dtype=torch.float16,variant='fp16',token=token,use_safetensors=True).to('cuda'); pipe.scheduler=EulerDiscreteScheduler.from_config(pipe.scheduler.config,timestep_spacing='trailing'); return pipe
def border_background(im):
 rgb=im.convert('RGB'); w,h=rgb.size; pts=[]; s=max(1,min(w,h)//128)
 for x in range(0,w,s): pts += [rgb.getpixel((x,0)),rgb.getpixel((x,h-1))]
 for y in range(0,h,s): pts += [rgb.getpixel((0,y)),rgb.getpixel((w-1,y))]
 pts.sort(key=sum); q=pts[:max(16,len(pts)//3)]; return tuple(sum(p[i] for p in q)//len(q) for i in range(3))
def isolate(im):
 rgb=im.convert('RGB'); w,h=rgb.size; bg=border_background(rgb); px=rgb.load(); dist=Image.new('L',(w,h)); dp=dist.load()
 for y in range(h):
  for x in range(w):
   r,g,b=px[x,y]; dp[x,y]=min(255,int((((r-bg[0])**2+(g-bg[1])**2+(b-bg[2])**2)**.5)*3))
 mask=dist.point(lambda p:0 if p<20 else (255 if p>58 else int((p-20)*255/38))); mp=mask.load(); seen=set(); q=deque()
 for x in range(w):
  for y in (0,h-1):
   if mp[x,y]<180 and (x,y) not in seen: seen.add((x,y)); q.append((x,y))
 for y in range(h):
  for x in (0,w-1):
   if mp[x,y]<180 and (x,y) not in seen: seen.add((x,y)); q.append((x,y))
 while q:
  x,y=q.popleft(); mp[x,y]=0
  for n in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
   nx,ny=n
   if 0<=nx<w and 0<=ny<h and n not in seen and mp[nx,ny]<180: seen.add(n); q.append(n)
 mask=mask.filter(ImageFilter.GaussianBlur(.6)); rgba=rgb.convert('RGBA'); rgba.putalpha(mask); return rgba
def components(alpha, threshold=32):
 small=alpha.resize((128,128),Image.Resampling.BILINEAR); px=small.load(); seen=set(); comps=[]
 for y in range(128):
  for x in range(128):
   if (x,y) in seen or px[x,y]<threshold: continue
   q=deque([(x,y)]); seen.add((x,y)); pts=[]
   while q:
    cx,cy=q.popleft(); pts.append((cx,cy))
    for n in ((cx-1,cy),(cx+1,cy),(cx,cy-1),(cx,cy+1)):
     nx,ny=n
     if 0<=nx<128 and 0<=ny<128 and n not in seen and px[nx,ny]>=threshold: seen.add(n); q.append(n)
   if len(pts)>=int(128*128*.006): comps.append(pts)
 return sorted(comps,key=len,reverse=True)
def reject_concept_sheet(master,kind):
 comps=components(master.getchannel('A'))
 if len(comps)<=1:return
 total=sum(len(c) for c in comps); ratios=[len(c)/total for c in comps]
 # Several similarly important islands are a strong concept-sheet/multi-object signal.
 if kind=='PRP' and len([r for r in ratios if r>=.10])>=2: raise RuntimeError(f'concept sheet/multiple props detected ({len(comps)} components)')
 if len(comps)>=3 and ratios[0]<.78: raise RuntimeError(f'multiple subjects detected ({len(comps)} components)')
def keep_dominant_subject(master):
 """Remove tiny detached generation debris, never merge separate candidate objects."""
 a=master.getchannel('A'); comps=components(a)
 if not comps:return master
 if len(comps)>1:
  total=sum(len(c) for c in comps)
  if len(comps[0])/total<.82:return master
 # Map dominant 128px component back to full resolution and keep a padded bounding region.
 xs=[p[0] for p in comps[0]]; ys=[p[1] for p in comps[0]]; w,h=master.size
 x0=max(0,int(min(xs)*w/128)-int(w*.03)); y0=max(0,int(min(ys)*h/128)-int(h*.03)); x1=min(w,int((max(xs)+1)*w/128)+int(w*.03)); y1=min(h,int((max(ys)+1)*h/128)+int(h*.03))
 crop=master.crop((x0,y0,x1,y1)); return crop
def normalize(master,side):
 bbox=master.getbbox()
 if not bbox: raise RuntimeError('empty alpha')
 crop=master.crop(bbox); scale=min(side*.72/crop.width,side*.72/crop.height); crop=crop.resize((max(1,round(crop.width*scale)),max(1,round(crop.height*scale))),Image.Resampling.LANCZOS); out=Image.new('RGBA',(side,side)); out.alpha_composite(crop,((side-crop.width)//2,max(int(side*.12),side-int(side*.12)-crop.height))); return out
def validate(im,kind):
 a=im.getchannel('A'); lo,hi=a.getextrema()
 if hi==0 or lo==255: raise RuntimeError('transparency validation failed')
 visible=sum(a.histogram()[8:])/(im.width*im.height); max_cov=.52 if kind=='PRP' else .70
 if visible<.025 or visible>max_cov: raise RuntimeError(f'invalid alpha coverage {visible:.1%}')
 pad=int(im.width*.06)
 if any(e.getbbox() for e in (a.crop((0,0,im.width,pad)),a.crop((0,im.height-pad,im.width,im.height)),a.crop((0,0,pad,im.height)),a.crop((im.width-pad,0,im.width,im.height)))): raise RuntimeError('transparent safety padding failed')
 comps=components(a)
 if len(comps)>1:
  total=sum(len(c) for c in comps)
  if len(comps[0])/total<.88: raise RuntimeError(f'{len(comps)} significant disconnected subjects')
 return visible
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--kind',choices=['ALL','PRP','VEH','CORE','BLD'],default='ALL'); ap.add_argument('--count',type=int,default=60); ap.add_argument('--seed',type=int,default=4242); args=ap.parse_args(); items=list(manifest_rows()); items=[x for x in items if args.kind=='ALL' or x['kind']==args.kind]; items.sort(key=lambda x:(PRIORITY[x['kind']],x['order'])); items=items[:max(1,args.count)]; print(f'KAGGLE_PLAN={len(items)}',flush=True)
 if not items:return
 pipe=load_pipe(); INCOMING.mkdir(parents=True,exist_ok=True); ok=rej=0
 for index,item in enumerate(items,1):
  try:
   image=pipe(prompt_for(item),num_inference_steps=4,guidance_scale=0,width=1024,height=1024,generator=torch.Generator(device='cuda').manual_seed(args.seed+index)).images[0]
   isolated=isolate(image); reject_concept_sheet(isolated,item['kind']); isolated=keep_dominant_subject(isolated); final=normalize(isolated,TARGET_SIDE[item['kind']]); cov=validate(final,item['kind']); out=INCOMING/f"{item['stem']}.png"; final.save(out,'PNG',optimize=True); ok+=1; print(f'KAGGLE_VALIDATED={out.relative_to(ROOT)} coverage={cov:.1%}',flush=True)
  except Exception as exc: rej+=1; print(f"KAGGLE_REJECTED={item['id']} reason={exc}",flush=True)
  finally: torch.cuda.empty_cache()
 print(f'KAGGLE_BATCH_SUCCESS={ok} KAGGLE_BATCH_REJECTED={rej} KAGGLE_BATCH_ATTEMPTED={len(items)}',flush=True)
if __name__=='__main__': main()
