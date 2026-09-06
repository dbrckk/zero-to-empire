#!/usr/bin/env python3
"""Family-coherent FLUX building factory for Zero -> Empire.

Generates only TODO BLD rows from the canonical manifest. The same family DNA is
reused across all tiers so each seven-tier business reads as one architecture
that evolves rather than seven unrelated buildings.
"""
from __future__ import annotations
import argparse,gc,re
from collections import deque
from pathlib import Path
print('KAGGLE_STARTUP=building-family-flux-v1',flush=True)
import torch
from PIL import Image,ImageFilter
from diffusers import FluxPipeline,FluxTransformer2DModel
from transformers import T5EncoderModel

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
BLD=re.compile(r'^BLD-(\d{2})-T([0-6])$')

FAMILY_DNA={
 0:'street-side micro foundry kiosk; rust-dark steel frame, corrugated canopy, compact exposed workbench, amber furnace cue',
 1:'corner fabrication shop; chamfered L-shaped storefront shell, dark steel and concrete, sheltered loading bay, compact cyan service lights',
 2:'furnace works; squat heatproof masonry-and-steel shell, dominant orange-hot furnace chamber, twin exhaust stacks, heavy insulated piping',
 3:'assembly hub; modular dark-steel production hall, central robotic assembly spine, side feeder bays, overhead gantry language, cyan status lights',
 4:'precision fabrication works; clean graphite alloy factory, enclosed CNC bays, ribbed roof modules, compact logistics dock, restrained cyan accents',
 5:'energy-cell works; dark premium alloy shell, integrated battery handling carousel motif, insulated amber energy conduits, protected transfer bay',
 6:'coolant and process plant; silver-graphite industrial shell, integrated reservoir towers, rigid coolant loops, pump-house silhouette, cyan fluid accents',
 7:'automation and power works; rectangular high-tech factory, overhead gantry rails, integrated power manifold, strong structural portal frame, cyan bus conduits',
 8:'heavy megastructure forge; massive armored alloy base, monumental articulated production bay, reinforced ribs, large service apertures, warm forge accents',
 9:'nanofabrication complex; sealed pearl-and-graphite process blocks, central clean chamber, smooth layered shells, precision cyan energy routing',
 10:'orbital component works; dark alloy logistics complex, concentric orbital assembly motif embedded into structure, cantilevered bays, cyan levitation seams',
 11:'actuator megaworks; monumental vertical press-tower architecture, symmetric articulated side structures, armored base, dense power routing',
 12:'phase-matter foundry; pearl alloy apex facility, integrated luminous cyan containment-ring architecture, central fabrication cradle, elegant vertical fins',
 13:'stellar precision works; prestige dark-and-pearl apex factory, crown-like articulated roof geometry, bright contained process core, warm stellar plus cyan accents',
}
TIER={
 0:'starter footprint, improvised materials, low verticality, exactly one obvious production cue; small and humble but functional',
 1:'same footprint DNA reinforced with cleaner structure, dedicated machinery enclosure and stronger silhouette; modest growth',
 2:'same architecture commercially expanded with a larger footprint and a second integrated active subsystem; clearly more capable than T1',
 3:'same architecture automated with visible internal logistics path, extra verticality and restrained emissive systems; medium industrial complex',
 4:'same architecture scaled to advanced district facility with dense integrated machinery, premium materials and landmark silhouette; large but coherent',
 5:'same architecture evolved into late-game megastructure with multi-stage production, large attached moving assemblies and visible energy routing',
 6:'ultimate mastered evolution of the same building DNA, iconic hero silhouette, maximal verticality, prestige crown treatment and apex production identity',
}

def rows():
 order=0
 for line in MANIFEST.read_text(encoding='utf-8').splitlines():
  m=ROW.match(line)
  if not m:continue
  asset_id,name,desc,runtime,status=[x.strip() for x in m.groups()]
  bm=BLD.fullmatch(asset_id)
  if not bm or status.upper()!='TODO':continue
  family=int(bm.group(1));tier=int(bm.group(2))
  yield {'id':asset_id,'name':name,'description':desc,'runtime':runtime,'stem':Path(runtime).stem,'family':family,'tier':tier,'order':order}
  order+=1

def select(items,count):
 """Prefer complete pending families; never split a family merely to fill count."""
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
 dna=FAMILY_DNA[i['family']]
 return (
  f"AAA premium mobile strategy BUILDING MASTER for {i['name']}. "
  f"Family architectural DNA that MUST remain recognizable across every tier: {dna}. "
  f"Tier evolution: {TIER[i['tier']]}. "
  "Exactly ONE complete self-contained building, no detached props or neighboring structures. "
  "Portrait-friendly 34 degree three-quarter 2.5D camera, consistent orthographic-like view, bottom-center grounding, upper-left key light, cool fill, restrained warm/cyan emissive accents. "
  "Fully visible isolated building on pure black with generous empty margin around roof, sides and base. Preserve a readable mobile-game silhouette and physically plausible attached machinery. "
  "No road, landscape, sky, city background, floor rectangle, workers, vehicles, text, letters, numbers, currency, signage, badge, logo, watermark or UI. "
  f"Canonical manifest intent: {i['description']}"
 )

def load_encode():
 print('KAGGLE_FLUX_LOAD=encoder',flush=True)
 t=T5EncoderModel.from_pretrained(FLUX,subfolder='text_encoder_2',torch_dtype=torch.float16,device_map='cuda')
 p=FluxPipeline.from_pretrained(FLUX,text_encoder_2=t,transformer=None,vae=None,torch_dtype=torch.float16,device_map='cuda')
 return t,p

def load_diffuse():
 print('KAGGLE_FLUX_LOAD=transformer',flush=True)
 t=FluxTransformer2DModel.from_pretrained(FLUX,subfolder='transformer',torch_dtype=torch.float16,device_map='cuda')
 p=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=t,vae=None,torch_dtype=torch.float16,device_map='cuda')
 return t,p

def load_decode():
 print('KAGGLE_FLUX_LOAD=vae',flush=True)
 return FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=None,torch_dtype=torch.float16,device_map='cuda')

def border_bg(im):
 rgb=im.convert('RGB');w,h=rgb.size;s=max(1,min(w,h)//128);pts=[]
 for x in range(0,w,s):pts += [rgb.getpixel((x,0)),rgb.getpixel((x,h-1))]
 for y in range(0,h,s):pts += [rgb.getpixel((0,y)),rgb.getpixel((w-1,y))]
 pts.sort(key=sum);q=pts[:max(16,len(pts)//3)]
 return tuple(sum(p[k] for p in q)//len(q) for k in range(3))

def isolate(im):
 rgb=im.convert('RGB');w,h=rgb.size;bg=border_bg(rgb);px=rgb.load();dist=Image.new('L',(w,h));dp=dist.load()
 for y in range(h):
  for x in range(w):
   r,g,b=px[x,y];dp[x,y]=min(255,int((((r-bg[0])**2+(g-bg[1])**2+(b-bg[2])**2)**.5)*3))
 mask=dist.point(lambda p:0 if p<20 else 255 if p>58 else int((p-20)*255/38)).filter(ImageFilter.GaussianBlur(.6))
 rgba=rgb.convert('RGBA');rgba.putalpha(mask);return rgba

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
 xs=[x for x,y in cs[0]];ys=[y for x,y in cs[0]];w,h=master.size
 box=(max(0,int(min(xs)*w/128)-30),max(0,int(min(ys)*h/128)-30),min(w,int((max(xs)+1)*w/128)+30),min(h,int((max(ys)+1)*h/128)+30))
 crop=master.crop(box);bbox=crop.getbbox()
 if not bbox:raise RuntimeError('empty alpha')
 crop=crop.crop(bbox)
 side=2048;maxw=side*.80;maxh=side*.78;scale=min(maxw/crop.width,maxh/crop.height)
 crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
 out=Image.new('RGBA',(side,side));x=(side-crop.width)//2;y=side-int(side*.10)-crop.height;out.alpha_composite(crop,(x,y))
 a=out.getchannel('A');lo,hi=a.getextrema();visible=sum(a.histogram()[8:])/(side*side)
 if hi==0 or lo==255 or visible<.07 or visible>.62:raise RuntimeError(f'alpha coverage {visible:.1%}')
 pad=int(side*.08)
 if any(e.getbbox() for e in (a.crop((0,0,side,pad)),a.crop((0,side-pad,side,side)),a.crop((0,0,pad,side)),a.crop((side-pad,0,side,side)))):raise RuntimeError('8-percent safety padding failed')
 return out,visible

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=30);ap.add_argument('--seed',type=int,default=43117);args=ap.parse_args()
 items=select(list(rows()),max(1,args.count));print('KAGGLE_BUILDING_PLAN='+','.join(i['id'] for i in items),flush=True)
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
   # Family-stable seed prefix plus tier offset keeps related structures stylistically close without cloning them.
   family_seed=args.seed+item['family']*1000+item['tier']*37
   packed=diff(height=1024,width=1024,num_inference_steps=4,guidance_scale=0.0,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),output_type='latent',max_sequence_length=384,generator=torch.Generator(device='cuda').manual_seed(family_seed)).images
   latents.append((item,packed.cpu()));print(f"KAGGLE_DIFFUSED={item['id']} seed={family_seed}",flush=True)
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
