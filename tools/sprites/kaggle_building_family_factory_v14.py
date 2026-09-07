#!/usr/bin/env python3
"""FLUX building-family factory v14: short prompts + monotonic tier envelopes."""
from __future__ import annotations
import argparse,gc,re
from collections import deque
from pathlib import Path
print('KAGGLE_STARTUP=building-family-flux-v14-prompt-safe-monotonic',flush=True)
import torch
from PIL import Image,ImageFilter
from diffusers import FluxPipeline,FluxImg2ImgPipeline,FluxTransformer2DModel
from transformers import T5EncoderModel
ROOT=Path(__file__).resolve().parents[2]; MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'; INCOMING=ROOT/'art/incoming/final-sprites'
FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'; ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$"); BLD=re.compile(r'^BLD-(\d{2})-T([0-6])$')
DNA={0:'micro foundry kiosk, rust steel, amber furnace',1:'fabrication shop, chamfered storefront, loading bay',2:'furnace works, steel shell, twin stacks',3:'assembly hub, dark hall, robotic spine, feeder bays',4:'precision factory, graphite shell, CNC bays',5:'energy-cell works, square alloy shell, amber core',6:'coolant plant, silver graphite shell, cyan pipes',7:'automation works, wide tech factory, twin gantries',8:'heavy forge, armored base, warm forge core',9:'nanofab complex, pearl graphite block, cyan ring',10:'orbital works, dark alloy base, circular cradle',11:'actuator works, press house, articulated frames',12:'phase foundry, pearl alloy base, containment ring',13:'stellar works, dark pearl base, four-part crown'}
TIER={0:'tiny one-storey starter; no tower or crane',1:'small reinforced upgrade; one attached module',2:'medium industrial upgrade; wider footprint',3:'large automated upgrade; compact central tower',4:'advanced upgrade; two attached wings',5:'megastructure; large upper assembly',6:'ultimate; tall prestige crown and heroic machinery'}
PRIORITY=(13,5,8,9,10,12,11,4,6,7,3,0,1,2); STRENGTH={1:.34,2:.42,3:.50,4:.58,5:.66,6:.72}; STEPS={0:5,1:4,2:4,3:5,4:5,5:6,6:6}; RETRIES={0:4,1:3,2:3,3:3,4:3,5:3,6:3}
ENV={0:(.50,.44),1:(.56,.50),2:(.62,.56),3:(.68,.62),4:(.74,.68),5:(.80,.74),6:(.84,.80)}
def rows():
 for order,line in enumerate(MANIFEST.read_text(encoding='utf-8').splitlines()):
  m=ROW.match(line)
  if not m: continue
  aid,_,_,runtime,status=[x.strip() for x in m.groups()]; bm=BLD.fullmatch(aid)
  if bm and status.upper()=='TODO' and not (ROOT/runtime).is_file(): yield {'id':aid,'stem':Path(runtime).stem,'family':int(bm.group(1)),'tier':int(bm.group(2)),'order':order}
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
 # Intentionally short: keep all semantic constraints inside CLIP/T5 limits.
 short=f"AAA 2.5D strategy building. {DNA[i['family']]}. {TIER[i['tier']]}. One connected isolated building. Gray studio background."
 detail=(f"Same family upgraded in place. {DNA[i['family']]}. {TIER[i['tier']]}. 34-degree orthographic view. "
         "Preserve facade, core and roof direction. All additions attached. Flat gray background to every edge. "
         "No floor slab, scenery, people, vehicles, text, signs, UI, loose props, particles or holes.")
 return short,detail
def load_encode():
 t=T5EncoderModel.from_pretrained(FLUX,subfolder='text_encoder_2',torch_dtype=torch.float16,device_map='cuda'); p=FluxPipeline.from_pretrained(FLUX,text_encoder_2=t,transformer=None,vae=None,torch_dtype=torch.float16,device_map='cuda'); return t,p
def load_render():
 tr=FluxTransformer2DModel.from_pretrained(FLUX,subfolder='transformer',torch_dtype=torch.float16,device_map='cuda'); base=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=tr,torch_dtype=torch.float16,device_map='cuda'); base.vae.to(device='cuda',dtype=torch.float16); img=FluxImg2ImgPipeline.from_pipe(base); img.vae.to(device='cuda',dtype=torch.float16); return tr,base,img
def border(im):
 rgb=im.convert('RGB');w,h=rgb.size;step=max(1,min(w,h)//128);pts=[]
 for x in range(0,w,step):pts += [rgb.getpixel((x,0)),rgb.getpixel((x,h-1))]
 for y in range(0,h,step):pts += [rgb.getpixel((0,y)),rgb.getpixel((w-1,y))]
 vals=[sum(p)/3 for p in pts];mean=sum(vals)/len(vals);sd=(sum((v-mean)**2 for v in vals)/len(vals))**.5;q=sorted(pts,key=sum)[len(pts)//3:2*len(pts)//3];bg=tuple(sum(p[k] for p in q)//len(q) for k in range(3));return bg,sd,max(bg)-min(bg)
def isolate(im):
 rgb=im.convert('RGB');w,h=rgb.size;bg,sd,chroma=border(rgb)
 if sd>11 or chroma>20:raise RuntimeError(f'bad border sd={sd:.1f} chroma={chroma}')
 px=rgb.load(); seen=set(); q=deque();
 for x in range(w):q.extend([(x,0),(x,h-1)])
 for y in range(h):q.extend([(0,y),(w-1,y)])
 def dist(p):return ((p[0]-bg[0])**2+(p[1]-bg[1])**2+(p[2]-bg[2])**2)**.5
 while q:
  p=q.popleft()
  if p in seen:continue
  x,y=p
  if dist(px[x,y])>27:continue
  seen.add(p)
  for n in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
   u,v=n
   if 0<=u<w and 0<=v<h and n not in seen:q.append(n)
 mask=Image.new('L',(w,h),255);mp=mask.load()
 for x,y in seen:mp[x,y]=0
 mask=mask.filter(ImageFilter.GaussianBlur(.7));out=rgb.convert('RGBA');out.putalpha(mask);return out
def comps(alpha):
 sm=alpha.resize((128,128),Image.Resampling.BILINEAR);px=sm.load();seen=set();out=[]
 for y in range(128):
  for x in range(128):
   if (x,y) in seen or px[x,y]<32:continue
   q=deque([(x,y)]);seen.add((x,y));pts=[]
   while q:
    a,b=q.popleft();pts.append((a,b))
    for n in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)):
     u,v=n
     if 0<=u<128 and 0<=v<128 and n not in seen and px[u,v]>=32:seen.add(n);q.append(n)
   if len(pts)>=50:out.append(pts)
 return sorted(out,key=len,reverse=True)
def slab_score(alpha):
 sm=alpha.resize((128,128),Image.Resampling.BILINEAR);px=sm.load();rows=[sum(px[x,y]>=32 for x in range(6,122))/116 for y in range(78,124)];return sum(v>.76 for v in rows)/len(rows)
def finish(raw,tier):
 m=isolate(raw);cs=comps(m.getchannel('A'))
 if not cs:raise RuntimeError('empty isolation')
 if len(cs)>1 and len(cs[0])/sum(map(len,cs))<.94:raise RuntimeError('detached structure')
 if slab_score(m.getchannel('A'))>.34:raise RuntimeError('ground slab')
 xs=[p[0] for p in cs[0]];ys=[p[1] for p in cs[0]];w,h=m.size;box=(max(0,int(min(xs)*w/128)-24),max(0,int(min(ys)*h/128)-24),min(w,int((max(xs)+1)*w/128)+24),min(h,int((max(ys)+1)*h/128)+24));crop=m.crop(box);bb=crop.getbbox()
 if not bb:raise RuntimeError('empty alpha')
 crop=crop.crop(bb);side=2048;mw,mh=ENV[tier];scale=min(side*mw/crop.width,side*mh/crop.height);crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS);out=Image.new('RGBA',(side,side));out.alpha_composite(crop,((side-crop.width)//2,side-int(side*.08)-crop.height));a=out.getchannel('A');cov=sum(a.histogram()[8:])/(side*side)
 if cov<.045 or cov>.66:raise RuntimeError(f'coverage {cov:.1%}')
 pad=int(side*.06)
 if any(e.getbbox() for e in (a.crop((0,0,side,pad)),a.crop((0,side-pad,side,side)),a.crop((0,0,pad,side)),a.crop((side-pad,0,side,side)))):raise RuntimeError('padding')
 return out,cov
def mask64(im):return im.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
def iou(a,b):
 A=mask64(a);B=mask64(b);pa=A.load();pb=B.load();inter=union=0
 for y in range(64):
  for x in range(64):aa=pa[x,y]>0;bb=pb[x,y]>0;inter+=aa and bb;union+=aa or bb
 return inter/union if union else 0
def bbox(im):
 b=mask64(im).getbbox();return (0,0,0,0) if not b else (b[2]-b[0],b[3]-b[1],(b[0]+b[2])/2,(b[1]+b[3])/2)
def family_qa(recs):
 if len(recs)<2:return True,'single'
 adj=[iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
 if min(adj)<.28:return False,f'identity-iou={min(adj):.2f}'
 cov=[r[2] for r in recs]
 if cov[-1]<cov[0]*1.75:return False,f'growth={cov[0]:.3f}->{cov[-1]:.3f}'
 drops=sum(b<a*.90 for a,b in zip(cov,cov[1:]))
 if drops>1:return False,f'nonmonotonic={cov}'
 boxes=[bbox(r[1]) for r in recs];cx=boxes[0][2]
 if max(abs(b[2]-cx) for b in boxes)>6.5:return False,'horizontal drift'
 return True,f'iou={min(adj):.2f} growth={cov[-1]/cov[0]:.2f}x'
def render(i,prev,pe,ppe,base,img,seed):
 errs=[]
 for attempt in range(RETRIES[i['tier']]):
  gen=torch.Generator(device='cuda').manual_seed(seed+attempt*7919)
  try:
   with torch.inference_mode():
    if prev is None:raw=base(height=1024,width=1024,num_inference_steps=STEPS[i['tier']],guidance_scale=0,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),output_type='pil',generator=gen).images[0];mode='anchor'
    else:
     s=min(.80,max(.30,STRENGTH[i['tier']]+(attempt-1)*.04));raw=img(image=prev,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),strength=s,num_inference_steps=STEPS[i['tier']],guidance_scale=0,output_type='pil',generator=gen).images[0];mode=f'img2img-s{s:.2f}'
   final,cov=finish(raw,i['tier']);print(f"KAGGLE_RENDERED={i['id']} mode={mode} attempt={attempt+1} coverage={cov:.1%}",flush=True);return raw.convert('RGB'),final,cov
  except Exception as e:errs.append(str(e));print(f"KAGGLE_RETRY={i['id']} attempt={attempt+1} reason={e}",flush=True)
 raise RuntimeError('; '.join(errs[-3:]))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=28);ap.add_argument('--seed',type=int,default=43117);args=ap.parse_args();items=select(list(rows()),max(1,args.count));print('KAGGLE_BUILDING_PLAN='+','.join(i['id'] for i in items),flush=True)
 if not items:return
 INCOMING.mkdir(parents=True,exist_ok=True);emb={};t,enc=load_encode()
 for i in items:
  s,d=prompts(i)
  with torch.no_grad():pe,ppe,_=enc.encode_prompt(prompt=s,prompt_2=d,max_sequence_length=192)
  emb[i['id']]=(pe.cpu(),ppe.cpu())
 del t,enc;gc.collect();torch.cuda.empty_cache();tr,base,img=load_render();by={}
 for i in items:by.setdefault(i['family'],[]).append(i)
 accepted=[];rejected=0
 for fam,group in sorted(by.items()):
  group.sort(key=lambda x:x['tier']);recs=[];prev=None;failed=False
  for i in group:
   pe,ppe=emb[i['id']]
   try:prev,final,cov=render(i,prev,pe,ppe,base,img,args.seed+fam*1000+i['tier']*97);recs.append((i,final,cov))
   except Exception as e:print(f"KAGGLE_REJECTED={i['id']} stage=render reason={e}",flush=True);failed=True;break
   finally:gc.collect();torch.cuda.empty_cache()
  if failed or len(recs)!=len(group):rejected+=len(group);continue
  ok,why=family_qa(recs)
  if not ok:
   for i,_,_ in recs:print(f"KAGGLE_REJECTED={i['id']} stage=family_qa reason={why}",flush=True)
   rejected+=len(recs);continue
  for i,final,cov in recs:
   p=INCOMING/f"{i['stem']}.png";final.save(p,'PNG',optimize=True);accepted.append(i['id']);print(f"KAGGLE_VALIDATED={p.relative_to(ROOT)} coverage={cov:.1%} {why}",flush=True)
 print(f'KAGGLE_BUILDING_SUCCESS={len(accepted)} KAGGLE_BUILDING_REJECTED={rejected} KAGGLE_BUILDING_ATTEMPTED={len(items)}',flush=True)
if __name__=='__main__':main()
