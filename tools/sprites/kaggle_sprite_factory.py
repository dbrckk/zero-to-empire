#!/usr/bin/env python3
"""Generate static Zero -> Empire candidates with a memory-safe FLUX.1-schnell NF4 pipeline."""
from __future__ import annotations
import argparse, gc, re
from collections import deque
from pathlib import Path
print('KAGGLE_STARTUP=flux', flush=True)
import torch
from PIL import Image, ImageFilter
from diffusers import FluxPipeline, FluxTransformer2DModel
from transformers import T5EncoderModel
ROOT=Path(__file__).resolve().parents[2]; MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'; INCOMING=ROOT/'art/incoming/final-sprites'
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
SUPPORTED=('PRP-','VEH-','CORE-'); PRIORITY={'PRP':0,'VEH':1,'CORE':2}; TARGET_SIDE={'CORE':1536,'VEH':1536,'PRP':1024}
FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'
def manifest_rows():
 order=0
 for line in MANIFEST.read_text(encoding='utf-8').splitlines():
  m=ROW.match(line)
  if not m:continue
  asset_id,name,description,runtime,status=[x.strip() for x in m.groups()]
  if not asset_id.startswith(SUPPORTED) or status.upper()!='TODO':continue
  stem=Path(runtime).stem;kind=asset_id.split('-',1)[0]
  yield {'id':asset_id,'name':name,'description':description,'runtime':runtime,'stem':stem,'kind':kind,'order':order};order+=1
def concrete_subject(i):
 if i['kind']=='PRP':
  m=re.fullmatch(r'PRP-(\d{2})-([AB])',i['id'])
  if not m:return i['name']
  idx=int(m.group(1));v=m.group(2)
  a=['rugged closed supply crate','compact closed retail stock crate','heatproof closed tool chest','closed assembly parts bin','closed industrial logistics crate','sealed component case','reinforced tool locker','closed automation parts crate','high-tech cargo case','energy-cell storage box','precision maintenance chest','orbital supply container','phase-tech component crate','prestige equipment case']
  b=['90-degree utility pipe elbow fitting','compact safety barrier','90-degree insulated service pipe elbow fitting','small control terminal','utility bollard','cable junction pedestal','compact pipe manifold','service terminal','90-degree coolant pipe elbow fitting','power distribution post','sensor bollard','orbital service terminal','90-degree phase conduit elbow fitting','prestige light bollard']
  return (a if v=='A' else b)[min(idx,13)]
 if i['kind']=='VEH':
  exact={
   'VEH-09':'ONE futuristic enclosed MAGLEV FREIGHT CAPSULE. It has ZERO wheels and ZERO circular wheel shapes. Its underside is a continuous smooth magnetic levitation hull with four glowing rectangular magnetic lift emitters. The entire capsule floats high above empty space with an unmistakable large visible air gap beneath every part of the hull. Long cargo-container proportions, no windshield-like car face, no road vehicle styling, no rail, no track, no platform',
   'VEH-16':'ONE premium terrestrial ANTI-GRAVITY EXECUTIVE TRANSPORT POD. The body is a single seamless flattened lozenge-shaped armored shell with an integrated panoramic dark-glass passenger canopy. It is NOT a car, limousine, sedan, sports car, yacht, boat, aircraft or road vehicle. ABSOLUTELY NO wheels, tires, wheel arches, landing gear, legs, feet, skids, struts, pylons, posts, supports, propellers, fins below the hull, or separate objects underneath. The complete lower silhouette is ONE smooth uninterrupted convex surface. Nothing protrudes downward. A thin continuous cyan levitation light is embedded flush along the lower hull edge. The pod visibly hangs in empty space with a large clean air gap below the entire body. Premium black, pearl-metal and smoked-glass materials, long executive passenger proportions, flush side access seams. It must read immediately as an expensive wheel-less floating city transport pod, never as a conventional automobile and never as a craft standing on supports',
   'VEH-17':'a tight coordinated swarm of five distinct small singularity logistics drones in one compact formation, all five drones fully visible, no mothership'}
  return exact.get(i['id'],i['name'])
 if i['kind']=='CORE':
  exact={'CORE-T0':'a salvaged mechanical power core mounted on an improvised welded scrap-metal cradle, exposed cables and conduits, patched casing, weak small amber pulse, visibly primitive and repaired','CORE-T1':'a reinforced industrial reactor with a clearly visible rotating mechanical ring and two exposed piston actuators, robust steel shell, strong warm amber core, industrial not futuristic','CORE-T2':'an automated district reactor with two clearly separate energy-routing channels, articulated service arms, central cyan energy chamber and organized industrial automation hardware','CORE-T3':'a clean premium neon-metropolitan reactor with one obvious holographic containment ring floating around the central core, polished shell and restrained cyan-magenta emissive accents','CORE-T4':'an orbital-grade power nexus with three visibly levitating concentric ring levels stacked vertically around a bright cyan core, strong cyan energy routing and a broad engineered base','CORE-T5':'a hero-scale stellar collector core with multiple nested containment rings around a bright star-like plasma sphere, stellar-corona motif and monumental premium silhouette','CORE-T6':'the Singularity Crown: an ultimate reality-bending black-hole power core enclosed by unmistakable crown-shaped geometry and several levitating orbital rings, prestige apex treatment'}
  return exact[i['id']]
 return i['name']
def prompt_for(i):
 s=concrete_subject(i); noun={'PRP':'prop','VEH':'vehicle composition','CORE':'reactor'}[i['kind']]
 return f"Create exactly {s}. Mandatory silhouette and mechanism. One centered {noun}, fully visible, isolated on pure black. No environment, scenery, floor slab, road, pedestal, text, logo, labels, UI, contact sheet or alternate variants. Premium stylized 2.5D mobile strategy-game asset, three-quarter isometric camera 34 degrees, upper-left key light, cool fill, restrained cyan and amber accents, crisp silhouette. Manifest intent: {i['description']} Preserve generous empty black space on every edge."
def flux_generate(prompt,seed):
 print('KAGGLE_FLUX_STAGE=encode',flush=True);text2=T5EncoderModel.from_pretrained(FLUX,subfolder='text_encoder_2',torch_dtype=torch.float16,device_map='cuda');pipe=FluxPipeline.from_pretrained(FLUX,text_encoder_2=text2,transformer=None,vae=None,torch_dtype=torch.float16,device_map='cuda')
 with torch.no_grad(): pe,ppe,_=pipe.encode_prompt(prompt=prompt,max_sequence_length=384)
 del text2,pipe;gc.collect();torch.cuda.empty_cache();print('KAGGLE_FLUX_STAGE=diffuse',flush=True);transformer=FluxTransformer2DModel.from_pretrained(FLUX,subfolder='transformer',torch_dtype=torch.float16,device_map='cuda');pipe=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=transformer,vae=None,torch_dtype=torch.float16,device_map='cuda');packed=pipe(height=1024,width=1024,num_inference_steps=4,guidance_scale=0.0,prompt_embeds=pe,pooled_prompt_embeds=ppe,output_type='latent',max_sequence_length=384,generator=torch.Generator(device='cuda').manual_seed(seed)).images
 del pe,ppe,transformer,pipe;gc.collect();torch.cuda.empty_cache();print('KAGGLE_FLUX_STAGE=decode',flush=True);pipe=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=None,torch_dtype=torch.float16,device_map='cuda');lat=(pipe._unpack_latents(packed,height=1024,width=1024,vae_scale_factor=pipe.vae_scale_factor)/pipe.vae.config.scaling_factor+pipe.vae.config.shift_factor)
 with torch.no_grad(): tensor=pipe.vae.decode(lat,return_dict=False)[0]
 image=pipe.image_processor.postprocess(tensor)[0];del packed,lat,tensor,pipe;gc.collect();torch.cuda.empty_cache();return image
def border_background(im):
 rgb=im.convert('RGB');w,h=rgb.size;pts=[];s=max(1,min(w,h)//128)
 for x in range(0,w,s):pts += [rgb.getpixel((x,0)),rgb.getpixel((x,h-1))]
 for y in range(0,h,s):pts += [rgb.getpixel((0,y)),rgb.getpixel((w-1,y))]
 pts.sort(key=sum);q=pts[:max(16,len(pts)//3)];return tuple(sum(p[i] for p in q)//len(q) for i in range(3))
def isolate(im):
 rgb=im.convert('RGB');w,h=rgb.size;bg=border_background(rgb);px=rgb.load();dist=Image.new('L',(w,h));dp=dist.load()
 for y in range(h):
  for x in range(w):
   r,g,b=px[x,y];dp[x,y]=min(255,int((((r-bg[0])**2+(g-bg[1])**2+(b-bg[2])**2)**.5)*3))
 mask=dist.point(lambda p:0 if p<20 else (255 if p>58 else int((p-20)*255/38)));mp=mask.load();seen=set();q=deque()
 for x in range(w):
  for y in (0,h-1):
   if mp[x,y]<180 and (x,y) not in seen:seen.add((x,y));q.append((x,y))
 for y in range(h):
  for x in (0,w-1):
   if mp[x,y]<180 and (x,y) not in seen:seen.add((x,y));q.append((x,y))
 while q:
  x,y=q.popleft();mp[x,y]=0
  for n in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
   nx,ny=n
   if 0<=nx<w and 0<=ny<h and n not in seen and mp[nx,ny]<180:seen.add(n);q.append(n)
 mask=mask.filter(ImageFilter.GaussianBlur(.6));rgba=rgb.convert('RGBA');rgba.putalpha(mask);return rgba
def components(alpha,threshold=32):
 small=alpha.resize((128,128),Image.Resampling.BILINEAR);px=small.load();seen=set();comps=[]
 for y in range(128):
  for x in range(128):
   if (x,y) in seen or px[x,y]<threshold:continue
   q=deque([(x,y)]);seen.add((x,y));pts=[]
   while q:
    cx,cy=q.popleft();pts.append((cx,cy))
    for n in ((cx-1,cy),(cx+1,cy),(cx,cy-1),(cx,cy+1)):
     nx,ny=n
     if 0<=nx<128 and 0<=ny<128 and n not in seen and px[nx,ny]>=threshold:seen.add(n);q.append(n)
   if len(pts)>=int(128*128*.003):comps.append(pts)
 return sorted(comps,key=len,reverse=True)
def single_subject_crop(master,allow_cluster=False):
 comps=components(master.getchannel('A'))
 if not comps:raise RuntimeError('empty isolated subject')
 total=sum(map(len,comps));dominant=len(comps[0])/total;important=sum(len(c)/total>=.08 for c in comps)
 if not allow_cluster and (important>=2 or (len(comps)>=3 and dominant<.88)):raise RuntimeError(f'multiple-object composition important={important} dominant={dominant:.2f}')
 selected=comps if allow_cluster else comps[:1];xs=[x for c in selected for x,y in c];ys=[y for c in selected for x,y in c];w,h=master.size;x0=max(0,int(min(xs)*w/128)-25);y0=max(0,int(min(ys)*h/128)-25);x1=min(w,int((max(xs)+1)*w/128)+25);y1=min(h,int((max(ys)+1)*h/128)+25);crop=master.crop((x0,y0,x1,y1));a=crop.getchannel('A');fill=sum(a.histogram()[32:])/(crop.width*crop.height)
 if fill<(.08 if allow_cluster else .20):raise RuntimeError(f'sparse silhouette fill={fill:.1%}')
 return crop
def normalize(crop,side):
 bbox=crop.getbbox()
 if not bbox:raise RuntimeError('empty alpha')
 crop=crop.crop(bbox);scale=min(side*.68/crop.width,side*.68/crop.height);crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS);out=Image.new('RGBA',(side,side));out.alpha_composite(crop,((side-crop.width)//2,side-int(side*.12)-crop.height));return out
def validate(im,kind,asset_id):
 a=im.getchannel('A');lo,hi=a.getextrema()
 if hi==0 or lo==255:raise RuntimeError('transparency validation failed')
 visible=sum(a.histogram()[8:])/(im.width*im.height);max_cov=.48 if kind=='PRP' else .70
 if visible<.04 or visible>max_cov:raise RuntimeError(f'invalid alpha coverage {visible:.1%}')
 pad=int(im.width*.06)
 if any(e.getbbox() for e in (a.crop((0,0,im.width,pad)),a.crop((0,im.height-pad,im.width,im.height)),a.crop((0,0,pad,im.height)),a.crop((im.width-pad,0,im.width,im.height)))):raise RuntimeError('transparent safety padding failed')
 comps=components(a);total=sum(map(len,comps)) or 1
 if asset_id!='VEH-17' and len(comps)>1 and len(comps[0])/total<.92:raise RuntimeError(f'{len(comps)} significant disconnected subjects')
 return visible
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--kind',choices=['ALL','PRP','VEH','CORE'],default='ALL');ap.add_argument('--count',type=int,default=1);ap.add_argument('--seed',type=int,default=12217);args=ap.parse_args();items=list(manifest_rows());items=[x for x in items if args.kind=='ALL' or x['kind']==args.kind];items.sort(key=lambda x:(PRIORITY[x['kind']],x['order']));items=items[:max(1,args.count)];print(f'KAGGLE_PLAN={len(items)} engine=FLUX.1-schnell-NF4',flush=True)
 if not items:return
 INCOMING.mkdir(parents=True,exist_ok=True);ok=rej=0
 for index,item in enumerate(items,1):
  try:
   image=flux_generate(prompt_for(item),args.seed+index);isolated=isolate(image);subject=single_subject_crop(isolated,item['id']=='VEH-17');final=normalize(subject,TARGET_SIDE[item['kind']]);cov=validate(final,item['kind'],item['id']);out=INCOMING/f"{item['stem']}.png";final.save(out,'PNG',optimize=True);ok+=1;print(f'KAGGLE_VALIDATED={out.relative_to(ROOT)} coverage={cov:.1%}',flush=True)
  except Exception as exc:rej+=1;print(f"KAGGLE_REJECTED={item['id']} reason={type(exc).__name__}: {exc}",flush=True)
  finally:gc.collect();torch.cuda.empty_cache()
 print(f'KAGGLE_BATCH_SUCCESS={ok} KAGGLE_BATCH_REJECTED={rej} KAGGLE_BATCH_ATTEMPTED={len(items)}',flush=True)
if __name__=='__main__':main()