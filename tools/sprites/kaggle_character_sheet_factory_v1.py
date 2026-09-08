#!/usr/bin/env python3
"""Dedicated FLUX character-sheet factory for Zero -> Empire.

Produces one coherent animation sheet per manifest CHR-* target. The first frame
is text-to-image; later frames are conservative img2img pose variations to keep
identity/clothing/camera stable. Output remains candidate-only until semantic QA.
"""
from __future__ import annotations
import argparse,gc,json,re
from collections import deque
from pathlib import Path
print('KAGGLE_STARTUP=character-sheet-flux-v1.1-identity-pivot-square-atlas',flush=True)
import torch
from PIL import Image,ImageFilter
from diffusers import FluxPipeline,FluxImg2ImgPipeline,FluxTransformer2DModel
from transformers import T5EncoderModel

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
REPORT=Path('/kaggle/working/output/character-sheet-report.json')
FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
CHR=re.compile(r'^CHR-(OP|TECH|LOG|ENG)-(IDLE|WALK|WORK|CARRY|REPAIR|CELEB)$')
ROLE={
 'OP':'foundry operator, practical dark workwear, rust-orange utility accents, gloves',
 'TECH':'industrial technician, graphite coveralls, cyan diagnostic accents, compact tool belt',
 'LOG':'logistics worker, reinforced work jacket, amber safety accents, cargo gloves',
 'ENG':'industrial engineer, clean graphite field suit, restrained cyan accents, utility harness',
}
ACTION={
 'IDLE':('idle breathing and subtle look-around',6),
 'WALK':('walking cycle, clear alternating steps',8),
 'WORK':('operating a compact industrial hand tool',10),
 'CARRY':('carrying one compact industrial crate with both hands',8),
 'REPAIR':('repairing with a compact diagnostic or welding tool',10),
 'CELEB':('short restrained milestone celebration, raised arm, no props',8),
}
POSE_HINT={
 'IDLE':['neutral stance','weight slightly left','neutral stance','weight slightly right','small head turn left','small head turn right'],
 'WALK':['left contact','left down','passing left','right contact','right down','passing right','left contact recovery','neutral passing'],
 'WORK':['tool ready','reach forward','tool contact','working low','working center','working high','pull back','inspect','tool down','neutral'],
 'CARRY':['carry neutral','left step','passing','right step','carry neutral','left step','passing','right step'],
 'REPAIR':['kneel/reach','tool contact','small spark-free repair pose','inspect','tool contact','adjust','inspect','tool contact','rise slightly','neutral repair'],
 'CELEB':['neutral','arm starts up','arm half up','arm raised','small fist pump','arm half down','arm down','neutral'],
}

def rows():
 out=[]
 for order,line in enumerate(MANIFEST.read_text(encoding='utf-8').splitlines()):
  m=ROW.match(line)
  if not m: continue
  aid,name,desc,runtime,status=[x.strip() for x in m.groups()]
  cm=CHR.fullmatch(aid)
  if cm and status.upper()=='TODO' and not (ROOT/runtime).is_file():
   out.append({'id':aid,'stem':Path(runtime).stem,'role':cm.group(1),'action':cm.group(2),'order':order})
 return out

def prompt(i,pose):
 return (f"AAA mobile 2.5D full-body {ROLE[i['role']]}. {ACTION[i['action']][0]}; {pose}. "
         "Same single adult worker, same face, same clothing, same proportions. 34-degree three-quarter orthographic game view. "
         "Feet fully visible. Isolated on flat neutral gray studio background touching all image edges. "
         "No floor card, scenery, text, logo, extra people, duplicated limbs, detached props, vehicle or building.")

def load_encode():
 t=T5EncoderModel.from_pretrained(FLUX,subfolder='text_encoder_2',torch_dtype=torch.float16,device_map='cuda')
 p=FluxPipeline.from_pretrained(FLUX,text_encoder_2=t,transformer=None,vae=None,torch_dtype=torch.float16,device_map='cuda')
 return t,p

def load_render():
 tr=FluxTransformer2DModel.from_pretrained(FLUX,subfolder='transformer',torch_dtype=torch.float16,device_map='cuda')
 base=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=tr,torch_dtype=torch.float16,device_map='cuda')
 base.vae.to(device='cuda',dtype=torch.float16)
 img=FluxImg2ImgPipeline.from_pipe(base); img.vae.to(device='cuda',dtype=torch.float16)
 return tr,base,img

def border_bg(im):
 rgb=im.convert('RGB');w,h=rgb.size;step=max(1,min(w,h)//96);pts=[]
 for x in range(0,w,step):pts += [rgb.getpixel((x,0)),rgb.getpixel((x,h-1))]
 for y in range(0,h,step):pts += [rgb.getpixel((0,y)),rgb.getpixel((w-1,y))]
 vals=[sum(p)/3 for p in pts];mean=sum(vals)/len(vals);sd=(sum((v-mean)**2 for v in vals)/len(vals))**.5
 q=sorted(pts,key=sum)[len(pts)//3:2*len(pts)//3];bg=tuple(sum(p[k] for p in q)//len(q) for k in range(3))
 if sd>12 or max(bg)-min(bg)>22:raise RuntimeError(f'bad border sd={sd:.1f}')
 return bg

def isolate(im):
 rgb=im.convert('RGB');w,h=rgb.size;bg=border_bg(rgb);px=rgb.load();seen=set();q=deque()
 for x in range(w):q.extend([(x,0),(x,h-1)])
 for y in range(h):q.extend([(0,y),(w-1,y)])
 def dist(p):return ((p[0]-bg[0])**2+(p[1]-bg[1])**2+(p[2]-bg[2])**2)**.5
 while q:
  p=q.popleft()
  if p in seen:continue
  x,y=p
  if dist(px[x,y])>28:continue
  seen.add(p)
  for n in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
   u,v=n
   if 0<=u<w and 0<=v<h and n not in seen:q.append(n)
 mask=Image.new('L',(w,h),255);mp=mask.load()
 for x,y in seen:mp[x,y]=0
 mask=mask.filter(ImageFilter.GaussianBlur(.65));out=rgb.convert('RGBA');out.putalpha(mask)
 return out

def finish_frame(raw):
 m=isolate(raw);a=m.getchannel('A');bb=a.getbbox()
 if not bb:raise RuntimeError('empty alpha')
 w,h=m.size;pad=max(8,w//40)
 if any(e.getbbox() for e in (a.crop((0,0,w,pad)),a.crop((0,h-pad,w,h)),a.crop((0,0,pad,h)),a.crop((w-pad,0,w,h)))):raise RuntimeError('edge contact')
 crop=m.crop(bb);cw,ch=crop.size
 if ch<cw*.95:raise RuntimeError('not full-body character silhouette')
 scale=min(176/cw,218/ch); crop=crop.resize((max(1,round(cw*scale)),max(1,round(ch*scale))),Image.Resampling.LANCZOS)
 cell=Image.new('RGBA',(256,256));x=(256-crop.width)//2;y=238-crop.height;cell.alpha_composite(crop,(x,y))
 aa=cell.getchannel('A');cov=sum(aa.histogram()[8:])/(256*256)
 if not .10<=cov<=.48:raise RuntimeError(f'coverage={cov:.2f}')
 return cell,cov

def alpha_iou(a,b):
 A=a.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
 B=b.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
 pa,pb=A.load(),B.load();inter=union=0
 for y in range(64):
  for x in range(64):
   aa=pa[x,y]>0;bb=pb[x,y]>0;inter+=aa and bb;union+=aa or bb
 return inter/union if union else 0

def sheet_qa(frames):
 if len(frames)<4:return False,'too-few-frames'
 ious=[alpha_iou(frames[n-1],frames[n]) for n in range(1,len(frames))]
 if min(ious)<.28:return False,f'identity/silhouette jump={min(ious):.2f}'
 if max(ious)>.985:return False,'duplicate-adjacent-frame'
 bottoms=[];centers=[]
 for f in frames:
  bb=f.getchannel('A').getbbox()
  bottoms.append(bb[3] if bb else 0);centers.append((bb[0]+bb[2])/2 if bb else 0)
 if max(bottoms)-min(bottoms)>5:return False,'feet-pivot-drift'
 if max(centers)-min(centers)>34:return False,'horizontal-drift'
 return True,f'min-iou={min(ious):.2f} pivot-drift={max(bottoms)-min(bottoms)}'

def make_sheet(frames):
 # Canonical character deliverable: fixed 1024x1024 transparent atlas.
 # 256px cells in a 4x4 grid preserve stable runtime slicing; unused cells stay transparent.
 if len(frames)>16:raise RuntimeError('character atlas supports at most 16 frames')
 out=Image.new('RGBA',(1024,1024),(0,0,0,0))
 for n,f in enumerate(frames):out.alpha_composite(f,((n%4)*256,(n//4)*256))
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=8);ap.add_argument('--seed',type=int,default=19417);args=ap.parse_args()
 items=rows()[:max(1,args.count)];print('KAGGLE_CHARACTER_PLAN='+','.join(i['id'] for i in items),flush=True)
 if not items:return
 INCOMING.mkdir(parents=True,exist_ok=True);REPORT.parent.mkdir(parents=True,exist_ok=True)
 encs={};t,enc=load_encode()
 for i in items:
  hints=POSE_HINT[i['action']][:ACTION[i['action']][1]]
  encs[i['id']]=[]
  for pose in hints:
   text=prompt(i,pose)
   with torch.no_grad():pe,ppe,_=enc.encode_prompt(prompt=text,prompt_2=text,max_sequence_length=192)
   encs[i['id']].append((pe.cpu(),ppe.cpu()))
 del t,enc;gc.collect();torch.cuda.empty_cache();tr,base,img=load_render();report=[]
 for idx,i in enumerate(items):
  frames=[];anchor_raw=None;fail=None
  for fi,(pe,ppe) in enumerate(encs[i['id']]):
   ok=False
   for attempt in range(3):
    gen=torch.Generator(device='cuda').manual_seed(args.seed+idx*10000+fi*211+attempt*7919)
    try:
     with torch.inference_mode():
      if fi==0:
       raw=base(height=1024,width=1024,num_inference_steps=5,guidance_scale=0,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),output_type='pil',generator=gen).images[0]
       anchor_raw=raw.convert('RGB')
      else:
       strength=min(.52,.32+fi*.018+attempt*.035)
       raw=img(image=anchor_raw,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),strength=strength,num_inference_steps=5,guidance_scale=0,output_type='pil',generator=gen).images[0]
     frame,cov=finish_frame(raw);frames.append(frame);ok=True;print(f"KAGGLE_CHR_FRAME={i['id']} frame={fi} attempt={attempt+1} cov={cov:.2f}",flush=True);break
    except Exception as e:print(f"KAGGLE_CHR_RETRY={i['id']} frame={fi} attempt={attempt+1} reason={e}",flush=True)
   if not ok:fail=f'frame-{fi}-failed';break
   gc.collect();torch.cuda.empty_cache()
  if fail:
   report.append({'id':i['id'],'status':'REJECT','reason':fail,'frames':len(frames)});continue
  ok,why=sheet_qa(frames)
  if not ok:
   print(f"KAGGLE_CHR_REJECTED={i['id']} reason={why}",flush=True);report.append({'id':i['id'],'status':'REJECT','reason':why,'frames':len(frames)});continue
  sheet=make_sheet(frames)
  if sheet.size!=(1024,1024):raise RuntimeError(f'bad atlas size {sheet.size}')
  p=INCOMING/f"{i['stem']}.png";sheet.save(p,'PNG',optimize=True)
  print(f"KAGGLE_CHR_VALIDATED={p.relative_to(ROOT)} {why} atlas=1024x1024",flush=True);report.append({'id':i['id'],'status':'CANDIDATE','reason':why,'frames':len(frames),'atlas':'1024x1024','cell':'256x256','file':p.name})
 REPORT.write_text(json.dumps(report,indent=2),encoding='utf-8')
 print(f"KAGGLE_CHARACTER_CANDIDATES={sum(r['status']=='CANDIDATE' for r in report)} ATTEMPTED={len(items)}",flush=True)
if __name__=='__main__':main()