#!/usr/bin/env python3
"""Family-coherent FLUX building factory for Zero -> Empire.

Strict v3: each family is generated from one immutable architectural anchor. Tier
prompts describe additive upgrades only; the same family seed and the same exact
anchor sentence are reused for every tier. Automatic family QA rejects a batch
when silhouettes/camera drift too far, so unrelated buildings never reach the
candidate artifact.
"""
from __future__ import annotations
import argparse,gc,re
from collections import deque
from pathlib import Path
print('KAGGLE_STARTUP=building-family-flux-v3-anchored-family-qa',flush=True)
import torch
from PIL import Image,ImageFilter
from diffusers import FluxPipeline,FluxTransformer2DModel
from transformers import T5EncoderModel
ROOT=Path(__file__).resolve().parents[2];MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md';INCOMING=ROOT/'art/incoming/final-sprites';FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$");BLD=re.compile(r'^BLD-(\d{2})-T([0-6])$')
FAMILY_DNA={0:'street-side micro foundry kiosk; rust-dark steel frame, corrugated canopy, compact exposed workbench, amber furnace cue',1:'corner fabrication shop; chamfered L-shaped storefront shell, dark steel and concrete, sheltered loading bay, compact cyan service lights',2:'furnace works; squat heatproof masonry-and-steel shell, dominant orange-hot furnace chamber, twin exhaust stacks, heavy insulated piping',3:'assembly hub; LOW WIDE rectangular dark-steel production hall; central open robotic assembly spine; TWO symmetric side feeder bays; FOUR corner posts; flat ribbed roof frame; cyan status strips',4:'precision fabrication works; LOW WIDE graphite rectangular factory; THREE enclosed CNC bay modules across front; ribbed flat roof; right-side compact logistics dock; cyan corner strips',5:'energy-cell works; TALL SQUARE dark-alloy factory; central amber battery handling core visible through front; TWO symmetric side transfer bays; heavy square roof frame; cyan lower service strips',6:'coolant process plant; LOW WIDE silver-graphite rectangular pump house; TWO tall cylindrical reservoir towers fixed at rear-left and rear-right; central rigid coolant loop; cyan fluid pipes along base',7:'automation power works; WIDE rectangular high-tech factory; TWO overhead gantry rails; central power manifold; FOUR structural portal posts; cyan bus conduits',8:'heavy megastructure forge; massive armored rectangular base; central articulated forge bay; TWO reinforced side ribs; large front service aperture; warm forge core',9:'nanofabrication complex; sealed pearl-and-graphite square process block; central clean chamber; TWO smooth layered side shells; cyan routing ring',10:'orbital component works; dark-alloy rectangular logistics complex; central circular orbital assembly cradle embedded in roof; TWO cantilevered side bays; cyan levitation seams',11:'actuator megaworks; tall rectangular press tower; TWO symmetric articulated side frames; armored square base; central vertical orange press channel',12:'phase-matter foundry; pearl-alloy square facility; ONE luminous cyan containment ring fixed around central fabrication cradle; FOUR elegant vertical corner fins',13:'stellar precision works; dark-and-pearl square apex factory; crown-like FOUR-part roof geometry; bright contained central process core; warm stellar plus cyan accents'}
TIER={0:'Keep anchor geometry bare and small. Improvised cladding. Add NOTHING except one production cue.',1:'KEEP EVERY anchor position. Reinforce walls and roof only; add one attached machinery enclosure.',2:'KEEP EVERY anchor position. Extend side walls slightly; add one attached second subsystem.',3:'KEEP EVERY anchor position. Add one vertical automation module and attached logistics conduit.',4:'KEEP EVERY anchor position. Thicken and premium-finish the same shell; add dense ATTACHED machinery.',5:'KEEP EVERY anchor position. Add attached multi-stage machinery and energy routing; preserve the original shell clearly.',6:'KEEP EVERY anchor position. Add vertical prestige crown ABOVE the same shell; original footprint and anchor modules remain plainly visible.'}
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
def anchor(i):return f"FIXED ARCHITECTURAL ANCHOR F{i['family']:02d}: {FAMILY_DNA[i['family']]}."
def prompt(i):
 return (f"AAA premium mobile strategy BUILDING MASTER. {anchor(i)} THIS ANCHOR IS A HARD BLUEPRINT, NOT INSPIRATION. Tier {i['tier']} is the SAME physical building upgraded in place. DO NOT change footprint category, camera-facing facade, anchor module count, anchor module positions, structural frame positions, main roof geometry, production-core position, or base proportions. {TIER[i['tier']]} Never replace the building with another design. Exactly ONE connected self-contained building. Fixed 34 degree three-quarter orthographic-like 2.5D camera, identical framing, bottom-center grounding, upper-left key light, cool fill, restrained warm/cyan emissives. Isolated on pure black with generous margin. No detached props, neighboring structures, road, landscape, sky, city, floor rectangle, workers, vehicles, text, letters, numbers, currency, signage, badge, logo, watermark or UI.")
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
def silhouette_signature(im):
 a=im.getchannel('A').resize((64,64),Image.Resampling.BILINEAR);b=a.point(lambda p:255 if p>=32 else 0);box=b.getbbox()
 if not box:return None
 x0,y0,x1,y1=box;return (x1-x0,y1-y0,(x0+x1)/2,(y0+y1)/2)
def family_shape_ok(images):
 sig=[silhouette_signature(x[1]) for x in images]
 if any(s is None for s in sig):return False
 widths=[s[0] for s in sig];heights=[s[1] for s in sig];cx=[s[2] for s in sig]
 # Allow upgrades to grow, but reject camera/footprint class changes typical of unrelated generations.
 return min(widths)/max(widths)>=.62 and min(heights)/max(heights)>=.48 and max(cx)-min(cx)<=8
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
 del tr,diff,encoded;gc.collect();torch.cuda.empty_cache();dec=load_decode();decoded=[]
 for item,packed in latents:
  try:
   packed=packed.cuda();lat=dec._unpack_latents(packed,height=1024,width=1024,vae_scale_factor=dec.vae_scale_factor)/dec.vae.config.scaling_factor+dec.vae.config.shift_factor
   with torch.no_grad():tensor=dec.vae.decode(lat,return_dict=False)[0]
   image=dec.image_processor.postprocess(tensor)[0];final,cov=finish(image,item);decoded.append((item,final,cov))
  except Exception as exc:print(f"KAGGLE_REJECTED={item['id']} stage=decode reason={type(exc).__name__}: {exc}",flush=True)
  finally:gc.collect();torch.cuda.empty_cache()
 ok=rej=0;families={}
 for rec in decoded:families.setdefault(rec[0]['family'],[]).append(rec)
 for fam,recs in families.items():
  recs.sort(key=lambda x:x[0]['tier'])
  if len(recs)>=3 and not family_shape_ok(recs):
   for item,_,_ in recs:print(f"KAGGLE_REJECTED={item['id']} stage=family_qa reason=silhouette-camera-drift",flush=True);rej+=1
   continue
  for item,final,cov in recs:
   path=INCOMING/f"{item['stem']}.png";final.save(path,'PNG',optimize=True);ok+=1;print(f'KAGGLE_VALIDATED={path.relative_to(ROOT)} coverage={cov:.1%}',flush=True)
 print(f'KAGGLE_BUILDING_SUCCESS={ok} KAGGLE_BUILDING_REJECTED={rej} KAGGLE_BUILDING_ATTEMPTED={len(items)}',flush=True)
if __name__=='__main__':main()
