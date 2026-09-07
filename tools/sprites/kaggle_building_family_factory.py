#!/usr/bin/env python3
"""High-yield sequential FLUX building-family factory."""
from __future__ import annotations
import argparse,gc,re
from collections import deque
from pathlib import Path
print('KAGGLE_STARTUP=building-family-flux-v9-fp16-safe',flush=True)
import torch
from PIL import Image,ImageFilter
from diffusers import FluxPipeline,FluxImg2ImgPipeline,FluxTransformer2DModel
from transformers import T5EncoderModel
ROOT=Path(__file__).resolve().parents[2]; MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'; INCOMING=ROOT/'art/incoming/final-sprites'
FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'; ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$"); BLD=re.compile(r'^BLD-(\d{2})-T([0-6])$')
DNA={0:'street micro foundry kiosk, rust steel, corrugated canopy, amber furnace',1:'corner fabrication shop, chamfered storefront, loading bay',2:'furnace works, masonry steel shell, orange furnace, twin stacks',3:'assembly hub, wide dark-steel hall, robotic spine, symmetric feeder bays',4:'precision fabrication works, graphite factory, three CNC bays, logistics dock',5:'energy-cell works, square dark-alloy factory, amber battery core, transfer bays',6:'coolant process plant, silver graphite pump house, twin reservoirs, cyan pipes',7:'automation power works, wide high-tech factory, twin gantries, power manifold',8:'heavy forge, armored base, articulated forge bay, warm core',9:'nanofabrication complex, pearl graphite process block, clean chamber, cyan ring',10:'orbital component works, dark-alloy logistics base, circular orbital cradle, cantilever bays',11:'actuator works, press-house, symmetric articulated frames, orange press channel',12:'phase-matter foundry, pearl-alloy base, cyan containment ring, corner fins',13:'stellar precision works, dark pearl base, four-part crown geometry, stellar core'}
DELTA={0:'starter: compact one-storey bare shell, no tower',1:'reinforced: retain shell, add attached machinery enclosure and roof ribs',2:'industrial: retain prior structure, widen sides, second subsystem and service deck',3:'automated: retain prior anchors, add central automation tower and logistics conduit',4:'advanced: retain base and tower, add two attached machinery wings and denser routing',5:'megastructure: retain all prior structure, add large upper production assembly and energy routing',6:'ultimate: retain entire evolved structure, add tall central prestige crown and heroic attached machinery'}
PRIORITY=(10,11,12,13,3,5,6,4,7,8,9,0,1,2); STRENGTH={1:.38,2:.48,3:.58,4:.66,5:.74,6:.82}
def rows():
 for order,line in enumerate(MANIFEST.read_text(encoding='utf-8').splitlines()):
  m=ROW.match(line)
  if not m: continue
  aid,name,desc,runtime,status=[x.strip() for x in m.groups()]; bm=BLD.fullmatch(aid)
  if bm and status.upper()=='TODO': yield {'id':aid,'stem':Path(runtime).stem,'family':int(bm.group(1)),'tier':int(bm.group(2)),'order':order}
def select(items,count):
 by={}
 for i in items: by.setdefault(i['family'],[]).append(i)
 rank={f:n for n,f in enumerate(PRIORITY)}; out=[]
 for fam in sorted(by,key=lambda f:(rank.get(f,999),f)):
  g=sorted(by[fam],key=lambda x:x['tier'])
  if out and len(out)+len(g)>count: continue
  out+=g
  if len(out)>=count: break
 return out or items[:count]
def prompts(i):
 s=f"AAA 2.5D strategy building family {i['family']:02d} tier {i['tier']}. Same building upgraded in place. {DELTA[i['tier']]}. One connected isolated building, uniform neutral background."
 d=f"Premium mobile strategy building master. Fixed family DNA: {DNA[i['family']]}. {DELTA[i['tier']]}. Preserve facade, production core, roof orientation and structural anchors; additions physically attached. 34 degree three-quarter orthographic camera, bottom-center grounding, upper-left key, cool fill, restrained cyan/warm emissives. Uniform achromatic background touching every edge. No gradient, scenery, floor card, detached props, people, vehicles, readable text, letters, numbers, logo, watermark or UI."
 return s,d
def load_encode():
 t=T5EncoderModel.from_pretrained(FLUX,subfolder='text_encoder_2',torch_dtype=torch.float16,device_map='cuda'); p=FluxPipeline.from_pretrained(FLUX,text_encoder_2=t,transformer=None,vae=None,torch_dtype=torch.float16,device_map='cuda'); return t,p
def load_render():
 tr=FluxTransformer2DModel.from_pretrained(FLUX,subfolder='transformer',torch_dtype=torch.float16,device_map='cuda')
 base=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=tr,torch_dtype=torch.float16,device_map='cuda')
 # Diffusers can leave VAE convolution biases in fp32 on this Kaggle image while
 # img2img feeds fp16 latents. Normalize VAE explicitly before any render.
 base.vae.to(device='cuda',dtype=torch.float16)
 img=FluxImg2ImgPipeline.from_pipe(base); img.vae.to(device='cuda',dtype=torch.float16)
 return tr,base,img
def border(im):
 rgb=im.convert('RGB'); w,h=rgb.size; step=max(1,min(w,h)//128); pts=[]
 for x in range(0,w,step): pts += [rgb.getpixel((x,0)),rgb.getpixel((x,h-1))]
 for y in range(0,h,step): pts += [rgb.getpixel((0,y)),rgb.getpixel((w-1,y))]
 vals=[sum(p)/3 for p in pts]; mean=sum(vals)/len(vals); sd=(sum((v-mean)**2 for v in vals)/len(vals))**.5; q=sorted(pts,key=sum)[len(pts)//3:2*len(pts)//3]; bg=tuple(sum(p[k] for p in q)//len(q) for k in range(3)); return bg,sd,max(bg)-min(bg)
def isolate(im):
 rgb=im.convert('RGB'); w,h=rgb.size; bg,sd,chroma=border(rgb)
 if sd>8 or chroma>14: raise RuntimeError(f'bad border sd={sd:.1f} chroma={chroma}')
 px=rgb.load(); mask=Image.new('L',(w,h)); mp=mask.load()
 for y in range(h):
  for x in range(w):
   p=px[x,y]; d=((p[0]-bg[0])**2+(p[1]-bg[1])**2+(p[2]-bg[2])**2)**.5; mp[x,y]=0 if d<7 else 255 if d>20 else int((d-7)*255/13)
 mask=mask.filter(ImageFilter.GaussianBlur(.6)); out=rgb.convert('RGBA'); out.putalpha(mask); return out
def components(alpha):
 sm=alpha.resize((128,128),Image.Resampling.BILINEAR); px=sm.load(); seen=set(); out=[]
 for y in range(128):
  for x in range(128):
   if (x,y) in seen or px[x,y]<32: continue
   q=deque([(x,y)]); seen.add((x,y)); pts=[]
   while q:
    a,b=q.popleft(); pts.append((a,b))
    for n in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)):
     u,v=n
     if 0<=u<128 and 0<=v<128 and n not in seen and px[u,v]>=32: seen.add(n); q.append(n)
   if len(pts)>=50: out.append(pts)
 return sorted(out,key=len,reverse=True)
def finish(raw):
 m=isolate(raw); cs=components(m.getchannel('A'))
 if not cs: raise RuntimeError('empty isolation')
 if len(cs)>1 and len(cs[0])/sum(map(len,cs))<.90: raise RuntimeError('detached structure')
 xs=[p[0] for p in cs[0]]; ys=[p[1] for p in cs[0]]; w,h=m.size; box=(max(0,int(min(xs)*w/128)-30),max(0,int(min(ys)*h/128)-30),min(w,int((max(xs)+1)*w/128)+30),min(h,int((max(ys)+1)*h/128)+30)); crop=m.crop(box); bb=crop.getbbox()
 if not bb: raise RuntimeError('empty alpha')
 crop=crop.crop(bb); side=2048; scale=min(side*.80/crop.width,side*.78/crop.height); crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS); out=Image.new('RGBA',(side,side)); out.alpha_composite(crop,((side-crop.width)//2,side-int(side*.10)-crop.height)); a=out.getchannel('A'); cov=sum(a.histogram()[8:])/(side*side)
 if cov<.07 or cov>.62: raise RuntimeError(f'coverage {cov:.1%}')
 pad=int(side*.08)
 if any(e.getbbox() for e in (a.crop((0,0,side,pad)),a.crop((0,side-pad,side,side)),a.crop((0,0,pad,side)),a.crop((side-pad,0,side,side)))): raise RuntimeError('padding')
 return out,cov
def mask64(im): return im.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
def iou(a,b):
 A=mask64(a);B=mask64(b);pa=A.load();pb=B.load(); inter=union=0
 for y in range(64):
  for x in range(64): aa=pa[x,y]>0;bb=pb[x,y]>0;inter+=aa and bb;union+=aa or bb
 return inter/union if union else 0
def family_qa(recs):
 if len(recs)<2:return True,'single'
 adj=[iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
 if min(adj)<.38:return False,f'identity-iou={min(adj):.2f}'
 if iou(recs[0][1],recs[-1][1])>.92:return False,'insufficient-evolution'
 return True,f'min-adj-iou={min(adj):.2f}'
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=42);ap.add_argument('--seed',type=int,default=43117);args=ap.parse_args();items=select(list(rows()),max(1,args.count));print('KAGGLE_BUILDING_PLAN='+','.join(i['id'] for i in items),flush=True)
 if not items:return
 INCOMING.mkdir(parents=True,exist_ok=True); emb={};t,enc=load_encode()
 for i in items:
  try:
   s,d=prompts(i)
   with torch.no_grad():pe,ppe,_=enc.encode_prompt(prompt=s,prompt_2=d,max_sequence_length=256)
   emb[i['id']]=(pe.cpu(),ppe.cpu())
  except Exception as e:print(f"KAGGLE_REJECTED={i['id']} stage=encode reason={e}",flush=True)
 del t,enc;gc.collect();torch.cuda.empty_cache();tr,base,img=load_render();by={}
 for i in items:
  if i['id'] in emb:by.setdefault(i['family'],[]).append(i)
 accepted=[];rejected=0
 for fam,group in sorted(by.items()):
  group.sort(key=lambda x:x['tier']);recs=[];previous=None;failed=False
  for i in group:
   pe,ppe=emb[i['id']];gen=torch.Generator(device='cuda').manual_seed(args.seed+fam*1000+i['tier']*17)
   try:
    with torch.inference_mode():
     if previous is None:raw=base(height=1024,width=1024,num_inference_steps=4,guidance_scale=0,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),output_type='pil',generator=gen).images[0];mode='anchor'
     else:raw=img(image=previous,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),strength=STRENGTH.get(i['tier'],.5),num_inference_steps=8,guidance_scale=0,output_type='pil',generator=gen).images[0];mode='img2img'
    final,cov=finish(raw);recs.append((i,final,cov));previous=raw.convert('RGB');print(f"KAGGLE_RENDERED={i['id']} mode={mode} coverage={cov:.1%}",flush=True)
   except Exception as e:print(f"KAGGLE_REJECTED={i['id']} stage=render reason={type(e).__name__}: {e}",flush=True);failed=True;rejected+=1;break
   finally:gc.collect();torch.cuda.empty_cache()
  if failed or len(recs)!=len(group):rejected+=max(0,len(group)-len(recs));continue
  ok,why=family_qa(recs)
  if not ok:
   for i,_,_ in recs:print(f"KAGGLE_REJECTED={i['id']} stage=family_qa reason={why}",flush=True)
   rejected+=len(recs);continue
  for i,final,cov in recs:
   p=INCOMING/f"{i['stem']}.png";final.save(p,'PNG',optimize=True);accepted.append(i['id']);print(f"KAGGLE_VALIDATED={p.relative_to(ROOT)} coverage={cov:.1%} {why}",flush=True)
 print(f'KAGGLE_BUILDING_SUCCESS={len(accepted)} KAGGLE_BUILDING_REJECTED={rejected} KAGGLE_BUILDING_ATTEMPTED={len(items)}',flush=True)
if __name__=='__main__':main()
