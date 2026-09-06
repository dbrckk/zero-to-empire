#!/usr/bin/env python3
"""Family-coherent FLUX building factory for Zero -> Empire.

Generates only TODO BLD rows from the canonical manifest. Every tier of a family
uses the SAME latent seed and an explicit immutable architectural blueprint so
tiers read as upgrades of one building instead of unrelated structures.
"""
from __future__ import annotations
import argparse,gc,re
from collections import deque
from pathlib import Path
print('KAGGLE_STARTUP=building-family-flux-v2-same-latent',flush=True)
import torch
from PIL import Image,ImageFilter
from diffusers import FluxPipeline,FluxTransformer2DModel
from transformers import T5EncoderModel
ROOT=Path(__file__).resolve().parents[2];MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md';INCOMING=ROOT/'art/incoming/final-sprites';FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$");BLD=re.compile(r'^BLD-(\d{2})-T([0-6])$')
FAMILY_DNA={0:'street-side micro foundry kiosk; rust-dark steel frame, corrugated canopy, compact exposed workbench, amber furnace cue',1:'corner fabrication shop; chamfered L-shaped storefront shell, dark steel and concrete, sheltered loading bay, compact cyan service lights',2:'furnace works; squat heatproof masonry-and-steel shell, dominant orange-hot furnace chamber, twin exhaust stacks, heavy insulated piping',3:'assembly hub; modular dark-steel production hall, central robotic assembly spine, side feeder bays, overhead gantry language, cyan status lights',4:'precision fabrication works; clean graphite alloy factory, enclosed CNC bays, ribbed roof modules, compact logistics dock, restrained cyan accents',5:'energy-cell works; dark premium alloy shell, integrated battery handling carousel motif, insulated amber energy conduits, protected transfer bay',6:'coolant and process plant; silver-graphite industrial shell, integrated reservoir towers, rigid coolant loops, pump-house silhouette, cyan fluid accents',7:'automation and power works; rectangular high-tech factory, overhead gantry rails, integrated power manifold, strong structural portal frame, cyan bus conduits',8:'heavy megastructure forge; massive armored alloy base, monumental articulated production bay, reinforced ribs, large service apertures, warm forge accents',9:'nanofabrication complex; sealed pearl-and-graphite process blocks, central clean chamber, smooth layered shells, precision cyan energy routing',10:'orbital component works; dark alloy logistics complex, concentric orbital assembly motif embedded into structure, cantilevered bays, cyan levitation seams',11:'actuator megaworks; monumental vertical press-tower architecture, symmetric articulated side structures, armored base, dense power routing',12:'phase-matter foundry; pearl alloy apex facility, integrated luminous cyan containment-ring architecture, central fabrication cradle, elegant vertical fins',13:'stellar precision works; prestige dark-and-pearl apex factory, crown-like articulated roof geometry, bright contained process core, warm stellar plus cyan accents'}
TIER={0:'starter footprint, improvised materials, low verticality, exactly one obvious production cue; small and humble but functional',1:'reinforce the SAME base shell; add dedicated machinery enclosure; only modest growth',2:'expand the SAME base shell laterally; add exactly one second integrated active subsystem',3:'upgrade the SAME shell with automation, visible logistics and one additional vertical module',4:'scale the SAME recognizable shell into a district facility; denser attached machinery and premium materials',5:'extend the SAME recognizable shell into a megastructure; multi-stage production, attached moving assemblies and energy routing',6:'ultimate evolution of the SAME recognizable shell; preserve its base geometry while adding maximum verticality and a prestige crown'}
def rows():
 for order,line in enumerate(MANIFEST.read_text(encoding='utf-8').splitlines()):
  m=ROW.match(line)
  if not m:continue
  asset_id,name,desc,runtime,status=[x.strip() for x in m.groups()];bm=BLD.fullmatch(asset_id)
  if bm and status.upper()=='TODO':yield {'id':asset_id,'name':name,'description':desc,'runtime':runtime,'stem':Path(runtime).stem,'family':int(bm.group(1)),'tier':int(bm.group(2)),'order':order}
def select(items,count):
 by={}
 for i in items:by.setdefault(i['family'],[]).append(i)
 chosen=[]
 for fam in sorted(by):
  group=sorted(by[fam],key=lambda x:x['tier'])
  if chosen and len(chosen)+len(group)>count:break
  chosen.extend(group)
  if len(chosen)>=count:break
 return chosen or items[:count]
def prompt(i):
 return (f"AAA premium mobile strategy BUILDING MASTER, {i['name']}. IMMUTABLE FAMILY BLUEPRINT: {FAMILY_DNA[i['family']]}. This is tier {i['tier']} of ONE upgrade sequence. It MUST look like the exact same building being upgraded in place, not a redesign, not another building. Preserve the same base footprint shape, facade orientation, main roofline, structural frame positions, production-core position, camera, proportions and material palette across all seven tiers. Tier change may ONLY add or reinforce attached modules while retaining the underlying blueprint. UPGRADE FOR THIS TIER: {TIER[i['tier']]}. Exactly ONE connected self-contained building. Portrait-friendly fixed 34 degree three-quarter orthographic-like 2.5D camera, bottom-center grounding, upper-left key light, cool fill, restrained warm/cyan emissives. Fully visible isolated building on pure black with generous margin. No detached props, neighboring structures, road, landscape, sky, city, floor rectangle, workers, vehicles, text, letters, numbers, currency, signage, badge, logo, watermark or UI. Manifest intent: {i['description']}")
def load_encode():
 t=T5EncoderModel.from_pretrained(FLUX,subfolder='text_encoder_2',torch_dtype=torch.float16,device_map='cuda');p=FluxPipeline.from_pretrained(FLUX,text_encoder_2=t,transformer=None,vae=None,torch_dtype=torch.float16,device_map='cuda');return t,p
def load_diffuse():
 t=FluxTransformer2DModel.from_pretrained(FLUX,subfolder='transformer',torch_dtype=torch.float16,device_map='cuda');p=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=t,vae=None,torch_dtype=torch.float16,device_map='cuda');return t,p
def load_decode():return FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=None,torch_dtype=torch.float16,device_map='cuda')
def border_bg(im):
 rgb=im.convert('RGB');w,h=rgb.size;s=max(1,min(w,h)//128);pts=[]
 for x in range(0,w,s):pts += [rgb.getpixel((x,0)),rgb.getpixel((x,h-1))]
 for y in range(0,h,s):pts += [rgb.getpixel((0,y)),rgb.getpixel((w-1,y))]
 pts.sort(key=sum);q=pts[:max(16,len(pts)//3)];return tuple(sum(p[k] for p in q)//len(q) for k in range(3))
def isolate(im):
 rgb=im.convert('RGB');w,h=rgb.size;bg=border_bg(rgb);px=rgb.load();dist=Image.new('L',(w,h));dp=dist.load()
 for y in range(h):
  for x in range(w):
   r,g,b=px[x,y];dp[x,y]=min(255,int((((r-bg[0])**2+(g-bg[1])**2+(b-bg[2])**2)**.5)*3))
 mask=dist.point(lambda p:0 if p<20 else 255 if p>58 else int((p-20)*255/38)).filter(ImageFilter.GaussianBlur(.6));rgba=rgb.convert('RGBA');rgba.putalpha(mask);return rgba
def comps(alpha,threshold=32):
 sm=alpha.resize((128,128),Image.Resampling.BILINEAR);px=sm.load();seen=set();out=[]
 for y in range(128):
  for x in range(128):
   if (x,y) in seen or px[x,y]<threshold:continue
   q=deque([(x,y)]);seen.add((x,y));pts=[]
   while q:
    cx,cy=q.popleft();pts.append((cx,cy))
    for n in ((cx-1,cy),(cx+1,cy),(cx,cy-1),(cx,cy+1)):
     nx,ny=n
     if 0<=nx<128 and 0<=ny<128 and n not in seen and px[nx,ny]>=threshold:seen.add(n);q.append(n)
   if len(pts)>=50:out.append(pts)
 return sorted(out,key=len,reverse=True)
def finish(image,item):
 master=isolate(image);cs=comps(master.getchannel('A'))
 if not cs:raise RuntimeError('empty isolated building')
 total=sum(map(len,cs));dominant=len(cs[0])/total
 if len(cs)>1 and dominant<.90:raise RuntimeError('detached secondary structure')
 xs=[x for x,y in cs[0]];ys=[y for x,y in cs[0]];w,h=master.size;box=(max(0,int(min(xs)*w/128)-30),max(0,int(min(ys)*h/128)-30),min(w,int((max(xs)+1)*w/128)+30),min(h,int((max(ys)+1)*h/128)+30));crop=master.crop(box);bbox=crop.getbbox()
 if not bbox:raise RuntimeError('empty alpha')
 crop=crop.crop(bbox);side=2048;scale=min(side*.80/crop.width,side*.78/crop.height);crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS);out=Image.new('RGBA',(side,side));out.alpha_composite(crop,((side-crop.width)//2,side-int(side*.10)-crop.height));a=out.getchannel('A');lo,hi=a.getextrema();visible=sum(a.histogram()[8:])/(side*side)
 if hi==0 or lo==255 or visible<.07 or visible>.62:raise RuntimeError(f'alpha coverage {visible:.1%}')
 pad=int(side*.08)
 if any(e.getbbox() for e in (a.crop((0,0,side,pad)),a.crop((0,side-pad,side,side)),a.crop((0,0,pad,side)),a.crop((side-pad,0,side,side)))):raise RuntimeError('8-percent safety padding failed')
 return out,visible
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=30);ap.add_argument('--seed',type=int,default=43117);args=ap.parse_args();items=select(list(rows()),max(1,args.count));print('KAGGLE_BUILDING_PLAN='+','.join(i['id'] for i in items),flush=True)
 if not items:return
 INCOMING.mkdir(parents=True,exist_ok=True);encoded=[];t,enc=load_encode()
 for index,item in enumerate(items,1):
  try:
   with torch.no_grad():pe,ppe,_=enc.encode_prompt(prompt=prompt(item),max_sequence_length=384)
   encoded.append((item,index,pe.cpu(),ppe.cpu()))
  except Exception as exc:print(f"KAGGLE_REJECTED={item['id']} stage=encode reason={exc}",flush=True)
 del t,enc;gc.collect();torch.cuda.empty_cache();tr,diff=load_diffuse();latents=[]
 for item,index,pe,ppe in encoded:
  try:
   family_seed=args.seed+item['family']*1000
   packed=diff(height=1024,width=1024,num_inference_steps=4,guidance_scale=0.0,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),output_type='latent',max_sequence_length=384,generator=torch.Generator(device='cuda').manual_seed(family_seed)).images;latents.append((item,packed.cpu()));print(f"KAGGLE_DIFFUSED={item['id']} family_seed={family_seed}",flush=True)
  except Exception as exc:print(f"KAGGLE_REJECTED={item['id']} stage=diffuse reason={exc}",flush=True)
  finally:gc.collect();torch.cuda.empty_cache()
 del tr,diff,encoded;gc.collect();torch.cuda.empty_cache();dec=load_decode();ok=rej=0
 for item,packed in latents:
  try:
   packed=packed.cuda();lat=dec._unpack_latents(packed,height=1024,width=1024,vae_scale_factor=dec.vae_scale_factor)/dec.vae.config.scaling_factor+dec.vae.config.shift_factor
   with torch.no_grad():tensor=dec.vae.decode(lat,return_dict=False)[0]
   image=dec.image_processor.postprocess(tensor)[0];final,cov=finish(image,item);path=INCOMING/f"{item['stem']}.png";final.save(path,'PNG',optimize=True);ok+=1;print(f'KAGGLE_VALIDATED={path.relative_to(ROOT)} coverage={cov:.1%}',flush=True)
  except Exception as exc:rej+=1;print(f"KAGGLE_REJECTED={item['id']} stage=decode reason={type(exc).__name__}: {exc}",flush=True)
  finally:gc.collect();torch.cuda.empty_cache()
 print(f'KAGGLE_BUILDING_SUCCESS={ok} KAGGLE_BUILDING_REJECTED={rej} KAGGLE_BUILDING_ATTEMPTED={len(items)}',flush=True)
if __name__=='__main__':main()
