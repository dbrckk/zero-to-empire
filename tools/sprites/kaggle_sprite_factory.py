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
SUPPORTED=('PRP-','VEH-','CORE-','BLD-'); PRIORITY={'PRP':0,'VEH':1,'CORE':2,'BLD':3}; TARGET_SIDE={'BLD':2048,'CORE':1536,'VEH':1536,'PRP':1024}
FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'
def manifest_rows():
 order=0
 for line in MANIFEST.read_text(encoding='utf-8').splitlines():
  m=ROW.match(line)
  if not m:continue
  asset_id,name,description,runtime,status=[x.strip() for x in m.groups()]
  if not asset_id.startswith(SUPPORTED) or status.upper()!='TODO':continue
  stem=Path(runtime).stem
  if (ROOT/runtime).exists() or (INCOMING/f'{stem}.png').exists():continue
  kind=asset_id.split('-',1)[0];yield {'id':asset_id,'name':name,'description':description,'runtime':runtime,'stem':stem,'kind':kind,'order':order};order+=1
def concrete_subject(i):
 if i['kind']!='PRP':return i['name']
 m=re.fullmatch(r'PRP-(\d{2})-([AB])',i['id'])
 if not m:return i['name']
 idx=int(m.group(1));v=m.group(2)
 a=['rugged closed supply crate','compact closed retail stock crate','heatproof closed tool chest','closed assembly parts bin','closed industrial logistics crate','sealed component case','reinforced tool locker','closed automation parts crate','high-tech cargo case','energy-cell storage box','precision maintenance chest','orbital supply container','phase-tech component crate','prestige equipment case']
 b=['90-degree utility pipe elbow fitting','compact safety barrier','90-degree insulated service pipe elbow fitting','small control terminal','utility bollard','cable junction pedestal','compact pipe manifold','service terminal','90-degree coolant pipe elbow fitting','power distribution post','sensor bollard','orbital service terminal','90-degree phase conduit elbow fitting','prestige light bollard']
 return (a if v=='A' else b)[min(idx,13)]
def prompt_for(i):
 s=concrete_subject(i); noun={'PRP':'prop','VEH':'vehicle','CORE':'reactor','BLD':'building'}[i['kind']]
 return f"A single {s}. Exactly one {noun}, centered and fully visible, isolated against a uniform pure black background. Premium stylized 2.5D mobile strategy game asset, three-quarter isometric camera at 34 degrees, upper-left key light, cool fill, restrained cyan and amber industrial accents. One continuous subject with generous empty space around it. No collection, no variants, no contact sheet, no extra objects, no environment, no floor, no text, no logo."
def flux_generate(prompt,seed):
 """Three-stage split pipeline; documented checkpoint peak is ~7.7 GB VRAM."""
 print('KAGGLE_FLUX_STAGE=encode',flush=True)
 text2=T5EncoderModel.from_pretrained(FLUX,subfolder='text_encoder_2',torch_dtype=torch.float16,device_map='cuda')
 pipe=FluxPipeline.from_pretrained(FLUX,text_encoder_2=text2,transformer=None,vae=None,torch_dtype=torch.float16,device_map='cuda')
 with torch.no_grad(): pe,ppe,_=pipe.encode_prompt(prompt=prompt,max_sequence_length=256)
 del text2,pipe;gc.collect();torch.cuda.empty_cache()
 print('KAGGLE_FLUX_STAGE=diffuse',flush=True)
 transformer=FluxTransformer2DModel.from_pretrained(FLUX,subfolder='transformer',torch_dtype=torch.float16,device_map='cuda')
 pipe=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=transformer,vae=None,torch_dtype=torch.float16,device_map='cuda')
 packed=pipe(height=1024,width=1024,num_inference_steps=4,guidance_scale=0.0,prompt_embeds=pe,pooled_prompt_embeds=ppe,output_type='latent',max_sequence_length=256,generator=torch.Generator(device='cuda').manual_seed(seed)).images
 del pe,ppe,transformer,pipe;gc.collect();torch.cuda.empty_cache()
 print('KAGGLE_FLUX_STAGE=decode',flush=True)
 pipe=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=None,torch_dtype=torch.float16,device_map='cuda')
 lat=(pipe._unpack_latents(packed,height=1024,width=1024,vae_scale_factor=pipe.vae_scale_factor)/pipe.vae.config.scaling_factor+pipe.vae.config.shift_factor)
 with torch.no_grad(): tensor=pipe.vae.decode(lat,return_dict=False)[0]
 image=pipe.image_processor.postprocess(tensor)[0]
 del packed,lat,tensor,pipe;gc.collect();torch.cuda.empty_cache();return image
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
   if len(pts)>=int(128*128*.006):comps.append(pts)
 return sorted(comps,key=len,reverse=True)
def single_subject_crop(master):
 comps=components(master.getchannel('A'))
 if not comps:raise RuntimeError('empty isolated subject')
 total=sum(map(len,comps));dominant=len(comps[0])/total;important=sum(len(c)/total>=.08 for c in comps)
 if important>=2 or (len(comps)>=3 and dominant<.88):raise RuntimeError(f'multiple-object composition important={important} dominant={dominant:.2f}')
 xs=[x for x,y in comps[0]];ys=[y for x,y in comps[0]];w,h=master.size;x0=max(0,int(min(xs)*w/128)-25);y0=max(0,int(min(ys)*h/128)-25);x1=min(w,int((max(xs)+1)*w/128)+25);y1=min(h,int((max(ys)+1)*h/128)+25);crop=master.crop((x0,y0,x1,y1));a=crop.getchannel('A');fill=sum(a.histogram()[32:])/(crop.width*crop.height)
 if fill<.20:raise RuntimeError(f'sparse silhouette fill={fill:.1%}')
 return crop
def normalize(crop,side):
 bbox=crop.getbbox()
 if not bbox:raise RuntimeError('empty alpha')
 crop=crop.crop(bbox);scale=min(side*.68/crop.width,side*.68/crop.height);crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS);out=Image.new('RGBA',(side,side));out.alpha_composite(crop,((side-crop.width)//2,side-int(side*.12)-crop.height));return out
def validate(im,kind):
 a=im.getchannel('A');lo,hi=a.getextrema()
 if hi==0 or lo==255:raise RuntimeError('transparency validation failed')
 visible=sum(a.histogram()[8:])/(im.width*im.height);max_cov=.48 if kind=='PRP' else .70
 if visible<.04 or visible>max_cov:raise RuntimeError(f'invalid alpha coverage {visible:.1%}')
 pad=int(im.width*(.08 if kind=='BLD' else .06))
 if any(e.getbbox() for e in (a.crop((0,0,im.width,pad)),a.crop((0,im.height-pad,im.width,im.height)),a.crop((0,0,pad,im.height)),a.crop((im.width-pad,0,im.width,im.height)))):raise RuntimeError('transparent safety padding failed')
 comps=components(a);total=sum(map(len,comps)) or 1
 if len(comps)>1 and len(comps[0])/total<.92:raise RuntimeError(f'{len(comps)} significant disconnected subjects')
 return visible
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--kind',choices=['ALL','PRP','VEH','CORE','BLD'],default='ALL');ap.add_argument('--count',type=int,default=1);ap.add_argument('--seed',type=int,default=4242);args=ap.parse_args();items=list(manifest_rows());items=[x for x in items if args.kind=='ALL' or x['kind']==args.kind];items.sort(key=lambda x:(PRIORITY[x['kind']],x['order']));items=items[:max(1,args.count)];print(f'KAGGLE_PLAN={len(items)} engine=FLUX.1-schnell-NF4',flush=True)
 if not items:return
 INCOMING.mkdir(parents=True,exist_ok=True);ok=rej=0
 for index,item in enumerate(items,1):
  try:
   image=flux_generate(prompt_for(item),args.seed+index);isolated=isolate(image);subject=single_subject_crop(isolated);final=normalize(subject,TARGET_SIDE[item['kind']]);cov=validate(final,item['kind']);out=INCOMING/f"{item['stem']}.png";final.save(out,'PNG',optimize=True);ok+=1;print(f'KAGGLE_VALIDATED={out.relative_to(ROOT)} coverage={cov:.1%}',flush=True)
  except Exception as exc:rej+=1;print(f"KAGGLE_REJECTED={item['id']} reason={type(exc).__name__}: {exc}",flush=True)
  finally:gc.collect();torch.cuda.empty_cache()
 print(f'KAGGLE_BATCH_SUCCESS={ok} KAGGLE_BATCH_REJECTED={rej} KAGGLE_BATCH_ATTEMPTED={len(items)}',flush=True)
if __name__=='__main__':main()
