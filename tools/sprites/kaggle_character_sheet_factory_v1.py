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
print('KAGGLE_STARTUP=character-sheet-flux-v1.6-action-motion-gates',flush=True)
import torch
from PIL import Image,ImageFilter
from diffusers import FluxPipeline,FluxImg2ImgPipeline,FluxTransformer2DModel
from transformers import T5EncoderModel

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
REPORT=Path('/kaggle/working/output/character-sheet-report.json')
QUEUE=ROOT/'art/production/controlled-character-regen-queue.json'
REJECTION_LEDGER=ROOT/'art/production/generation-rejection-ledger.json'
FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
CHR=re.compile(r'^CHR-(OP|TECH|LOG|ENG)-(IDLE|WALK|WORK|CARRY|REPAIR|CELEB)$')
ROLE={
 'OP':'foundry operator, practical dark workwear, rust-orange utility accents, gloves, one rust-orange safety hard hat worn in every frame and every animation',
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
 'WALK':['left foot far forward, right foot far back, arms counter-swing','left knee bent under body, right leg extended back','legs crossing in mid-stride, opposite arm forward','right foot far forward, left foot far back, arms counter-swing','right knee bent under body, left leg extended back','legs crossing in opposite mid-stride, opposite arm forward','left foot forward recovery stride, right heel raised','right foot forward recovery stride, left heel raised'],
 'WORK':['tool held at chest, neutral stance','left arm reaches tool forward, torso leans slightly','tool contacting waist-height machine point','knees bent, tool working low near knee height','tool centered with both hands, torso forward','tool raised toward shoulder-height work point','upper body pulls tool back from contact','lean in and inspect repaired point','tool lowered beside thigh','return to neutral work stance'],
 'CARRY':['crate held with both hands at waist, feet apart','left foot forward carrying stride, crate stable','legs passing under body, crate stable at waist','right foot forward carrying stride, crate stable','short recovery stance with crate centered','left foot forward longer carrying stride','opposite passing step, elbows fixed around crate','right foot forward recovery, crate centered'],
 'REPAIR':['half-kneel and reach tool toward low repair point','tool pressed to low repair point, free hand bracing','tool moves horizontally across repair point, no sparks','lean closer and inspect repair point','tool contacts mid-height repair point','free hand adjusts component while tool stays ready','pull back and inspect with torso upright','second tool contact at mid height','rise from half-kneel while lowering tool','neutral repair-ready stance'],
 'CELEB':['neutral stance both arms down','right arm begins lifting, elbow bent','right fist reaches shoulder height, torso opens','right fist fully overhead, weight shifts to left leg','small overhead fist pump with opposite arm bent','arm lowers to shoulder height, weight recenters','arm lowers beside body','return to neutral stance'],
}

def rows():
 catalog={}
 for order,line in enumerate(MANIFEST.read_text(encoding='utf-8').splitlines()):
  m=ROW.match(line)
  if not m: continue
  aid,name,desc,runtime,status=[x.strip() for x in m.groups()]
  cm=CHR.fullmatch(aid)
  if not cm: continue
  catalog[aid]={
   'id':aid,
   'stem':Path(runtime).stem,
   'role':cm.group(1),
   'action':cm.group(2),
   'order':order,
   'manifest_status':status.upper(),
   'runtime':runtime,
  }

 if QUEUE.is_file():
  q=json.loads(QUEUE.read_text(encoding='utf-8'))
  controlled=[]
  for item in q.get('targets',[]):
   if str(item.get('status','')).upper()!='PENDING_KAGGLE': continue
   aid=str(item.get('id','')).upper()
   if aid not in catalog:
    raise RuntimeError('controlled Kaggle character missing from manifest: '+aid)
   controlled.append(catalog[aid])
  if controlled:
   print('KAGGLE_CHARACTER_CONTROLLED_QUEUE='+','.join(x['id'] for x in controlled),flush=True)
   return controlled

 return [
  x for x in catalog.values()
  if x['manifest_status']=='TODO' and not (ROOT/x['runtime']).is_file()
 ]

def rejection_hints(i):
 hints=[]
 if REJECTION_LEDGER.is_file():
  try:
   data=json.loads(REJECTION_LEDGER.read_text(encoding='utf-8'))
   for row in data.get('entries',[]):
    prefix=str(row.get('target_prefix','')).upper()
    role=str(row.get('role','')).upper()
    if (prefix and i['id'].startswith(prefix)) or (role and role==i['role']):
     hint=str(row.get('prompt_hint','')).strip()
     if hint and hint not in hints:hints.append(hint)
  except Exception as e:
   print('KAGGLE_CHR_REJECTION_MEMORY_SKIP='+str(e),flush=True)
 merged=' '.join(hints[-2:])
 words=merged.split()
 return ' '.join(words[:48])

def prompt_pair(i,pose,mode='default'):
 # Keep CLIP deliberately tiny: tokenizer expansion makes word-count estimates
 # optimistic. T5 carries the descriptive detail and rejection-memory hints.
 role=i['role'];action=i['action']
 role_short={
  'OP':'orange-hardhat foundry operator in dark coveralls',
  'TECH':'cyan-accent industrial technician in graphite coveralls',
  'LOG':'amber-accent logistics worker in work jacket',
  'ENG':'cyan-accent industrial engineer in graphite field suit',
 }[role]
 core=(f"stylized 2.5D game sprite, one {role_short}, full body, "
       f"three-quarter orthographic view, {pose}, isolated")
 if mode=='framing':
  core += ", smaller centered subject, generous empty border"
 elif mode=='single':
  core += ", one person only, single connected human silhouette"
 elif mode=='identity':
  core += ", preserve exact face headgear clothing colors proportions"
 if len(core.split())>38:
  raise RuntimeError('CLIP core prompt too long: '+str(len(core.split())))
 detail=(f"AAA stylized painterly 2.5D mobile game character. {ROLE[role]}. "
         f"{ACTION[action][0]}; {pose}. One adult only. Preserve face, hardhat or hair, clothing, palette and proportions. "
         "Full body centered on flat neutral gray; feet visible; safe border. "
         "No second body, clone, crowd, scenery, text, vehicle or building. " + rejection_hints(i))
 if mode=='framing':
  detail += " Keep the full figure clearly inside frame with at least ten percent empty margin on every side."
 elif mode=='single':
  detail += " Render one worker only; never depict a second body, reflection, duplicate or companion."
 elif mode=='identity':
  detail += " Do not redesign the person; preserve headgear, face, jacket, gloves and accent colors exactly."
 return core,detail

def retry_mode(reason,attempt):
 if attempt==0:return 'default'
 r=(reason or '').lower()
 if 'edge contact' in r or 'coverage=' in r or 'full-body' in r:return 'framing'
 if 'too-wide' in r or 'multiple-subject' in r:return 'single'
 return 'identity'

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
 # Two side-by-side people produce an abnormally wide full-body silhouette.
 # Allow wide action poses/gear up to 1.08; downstream identity/coverage QA still rejects real duplicates.
 # Reject before resizing so technical QA cannot normalize a multi-person frame into a valid-looking cell.
 if cw/ch>1.08:raise RuntimeError(f'too-wide/multiple-subject silhouette ratio={cw/ch:.2f}')
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

def lower_body_motion(frames):
 vals=[]
 for n in range(1,len(frames)):
  A=frames[n-1].getchannel('A')
  B=frames[n].getchannel('A')
  ba=A.getbbox();bb=B.getbbox()
  if not ba or not bb:continue
  top=max(0,min(ba[1]+int((ba[3]-ba[1])*.55),bb[1]+int((bb[3]-bb[1])*.55)))
  a=A.crop((0,top,256,256)).resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
  b=B.crop((0,top,256,256)).resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
  pa,pb=a.load(),b.load();inter=union=0
  for y in range(64):
   for x in range(64):
    aa=pa[x,y]>0;bbb=pb[x,y]>0;inter+=aa and bbb;union+=aa or bbb
  vals.append(1-(inter/union if union else 1))
 return sum(vals)/len(vals) if vals else 0.0

def action_qa(frames,action):
 # Per-action motion floor prevents technically valid but visually frozen atlases
 # from reaching manual semantic review.
 ious=[alpha_iou(frames[n-1],frames[n]) for n in range(1,len(frames))]
 mean_change=(sum(1-x for x in ious)/len(ious)) if ious else 0.0
 if action=='WALK':
  motion=lower_body_motion(frames)
  if motion<.22:return False,f'walk-too-static lower-motion={motion:.3f}'
  if mean_change<.12:return False,f'walk-too-static mean-change={mean_change:.3f}'
  return True,f'walk-motion={motion:.3f} mean-change={mean_change:.3f}'
 floors={'WORK':.075,'CARRY':.10,'REPAIR':.075,'CELEB':.09,'IDLE':.025}
 floor=floors.get(action,.05)
 if mean_change<floor:
  return False,f'{action.lower()}-too-static mean-change={mean_change:.3f}<{floor:.3f}'
 return True,f'{action.lower()}-motion={mean_change:.3f}'

def appearance_signature(cell):
 rgba=cell.convert('RGBA');a=rgba.getchannel('A');bb=a.getbbox()
 if not bb:return (0.0,)*6
 x0,y0,x1,y1=bb;h=max(1,y1-y0)
 bands=((y0,y0+int(.38*h)),(y0+int(.38*h),y0+int(.78*h)))
 out=[]
 for ya,yb in bands:
  crop=rgba.crop((x0,ya,x1,max(ya+1,yb)))
  ca=crop.getchannel('A');pix=list(crop.convert('RGB').getdata());mask=list(ca.getdata())
  vals=[p for p,m in zip(pix,mask) if m>=48]
  if not vals:out.extend((0.0,0.0,0.0));continue
  out.extend(sum(p[k] for p in vals)/len(vals) for k in range(3))
 return tuple(out)

def appearance_distance(a,b):
 return sum(abs(x-y) for x,y in zip(appearance_signature(a),appearance_signature(b)))/6.0

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
   variants={}
   for mode in ('default','framing','single','identity'):
    clip_text,t5_text=prompt_pair(i,pose,mode)
    with torch.no_grad():pe,ppe,_=enc.encode_prompt(prompt=clip_text,prompt_2=t5_text,max_sequence_length=192)
    variants[mode]=(pe.cpu(),ppe.cpu())
   encs[i['id']].append(variants)
 del t,enc;gc.collect();torch.cuda.empty_cache();tr,base,img=load_render();report=[];role_anchor={};role_reference_cell={}
 for idx,i in enumerate(items):
  frames=[];anchor_raw=None;fail=None;retry_reasons=[]
  for fi,variants in enumerate(encs[i['id']]):
   ok=False;last_reason=''
   for attempt in range(3):
    mode=retry_mode(last_reason,attempt)
    pe,ppe=variants[mode]
    gen=torch.Generator(device='cuda').manual_seed(args.seed+idx*10000+fi*211+attempt*7919)
    try:
     with torch.inference_mode():
      if fi==0:
       shared=role_anchor.get(i['role'])
       if shared is None:
        raw=base(height=1024,width=1024,num_inference_steps=5,guidance_scale=0,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),output_type='pil',generator=gen).images[0]
        anchor_raw=raw.convert('RGB')
        role_anchor[i['role']]=anchor_raw.copy()
        print('KAGGLE_CHR_IDENTITY_ANCHOR='+i['role']+' source='+i['id'],flush=True)
       else:
        # Start every later animation for this role from the exact same person.
        # Moderate img2img freedom changes pose while preserving face/headgear/clothes.
        strength=(min(.62,.54+attempt*.035) if i['action']=='WALK' else min(.44,.32+attempt*.03))
        if mode=='identity' and i['action']!='WALK':strength=max(.28,strength-.04)
        raw=img(image=shared,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),strength=strength,num_inference_steps=6,guidance_scale=0,output_type='pil',generator=gen).images[0]
        anchor_raw=raw.convert('RGB')
        print('KAGGLE_CHR_SHARED_IDENTITY='+i['id']+' role='+i['role']+f' strength={strength:.2f}',flush=True)
      else:
       strength=(min(.64,.50+fi*.018+attempt*.025) if i['action']=='WALK' else min(.48,.29+fi*.015+attempt*.025))
       if mode in {'single','identity'} and i['action']!='WALK':strength=max(.24,strength-.035)
       raw=img(image=anchor_raw,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),strength=strength,num_inference_steps=6,guidance_scale=0,output_type='pil',generator=gen).images[0]
     frame,cov=finish_frame(raw);frames.append(frame);ok=True;print(f"KAGGLE_CHR_FRAME={i['id']} frame={fi} attempt={attempt+1} mode={mode} cov={cov:.2f}",flush=True);break
    except Exception as e:
     last_reason=str(e);retry_reasons.append(last_reason);print(f"KAGGLE_CHR_RETRY={i['id']} frame={fi} attempt={attempt+1} mode={mode} reason={e}",flush=True)
   if not ok:fail=f'frame-{fi}-failed';break
   gc.collect();torch.cuda.empty_cache()
  if fail:
   report.append({'id':i['id'],'status':'REJECT','reason':fail,'frames':len(frames),'retry_reasons':retry_reasons});continue
  ok,why=sheet_qa(frames)
  if not ok:
   print(f"KAGGLE_CHR_REJECTED={i['id']} reason={why}",flush=True);report.append({'id':i['id'],'status':'REJECT','reason':why,'frames':len(frames),'retry_reasons':retry_reasons});continue
  action_ok,action_why=action_qa(frames,i['action'])
  if not action_ok:
   print(f"KAGGLE_CHR_REJECTED={i['id']} reason={action_why}",flush=True)
   report.append({'id':i['id'],'status':'REJECT','reason':action_why,'frames':len(frames),'retry_reasons':retry_reasons});continue
  why=why+' '+action_why
  identity_distance=0.0
  ref=role_reference_cell.get(i['role'])
  if ref is None:
   role_reference_cell[i['role']]=frames[0].copy()
  else:
   identity_distance=appearance_distance(ref,frames[0])
   print(f"KAGGLE_CHR_CROSS_ANIM_IDENTITY={i['id']} distance={identity_distance:.1f}",flush=True)
   if identity_distance>48:
    why=f'cross-animation-appearance-drift={identity_distance:.1f}'
    print(f"KAGGLE_CHR_REJECTED={i['id']} reason={why}",flush=True)
    report.append({'id':i['id'],'status':'REJECT','reason':why,'frames':len(frames),'retry_reasons':retry_reasons});continue
  sheet=make_sheet(frames)
  if sheet.size!=(1024,1024):raise RuntimeError(f'bad atlas size {sheet.size}')
  p=INCOMING/f"{i['stem']}.png";sheet.save(p,'PNG',optimize=True)
  print(f"KAGGLE_CHR_VALIDATED={p.relative_to(ROOT)} {why} atlas=1024x1024",flush=True);report.append({'id':i['id'],'status':'CANDIDATE','reason':why,'frames':len(frames),'atlas':'1024x1024','cell':'256x256','file':p.name,'cross_animation_appearance_distance':round(identity_distance,2),'retry_reasons':retry_reasons})
 REPORT.write_text(json.dumps(report,indent=2),encoding='utf-8')
 print(f"KAGGLE_CHARACTER_CANDIDATES={sum(r['status']=='CANDIDATE' for r in report)} ATTEMPTED={len(items)}",flush=True)
if __name__=='__main__':main()