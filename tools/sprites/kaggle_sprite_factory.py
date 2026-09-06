#!/usr/bin/env python3
"""High-throughput static Zero -> Empire FLUX candidate factory.

The factory deliberately handles only manifest assets that can be reviewed as one
isolated static master. Character and FX sheets stay on their dedicated animation
pipelines; building tiers require a separate family-coherent generator.
"""
from __future__ import annotations
import argparse,gc,re
from collections import deque
from pathlib import Path
print('KAGGLE_STARTUP=flux-batched-v2',flush=True)
import torch
from PIL import Image,ImageFilter
from diffusers import FluxPipeline,FluxTransformer2DModel
from transformers import T5EncoderModel
ROOT=Path(__file__).resolve().parents[2];MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md';INCOMING=ROOT/'art/incoming/final-sprites'
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
SUPPORTED=('MCH-','TER-','PRP-','VEH-','CORE-');PRIORITY={'MCH':0,'TER':1,'PRP':2,'VEH':3,'CORE':4};TARGET_SIDE={'MCH':1024,'TER':1024,'CORE':1536,'VEH':1536,'PRP':1024};FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'
MACHINE_PRIMARY=[
 'compact hand-fed stamping press with exposed flywheel and guarded ram',
 'compact retail packaging and sealing press with small articulated pusher',
 'heatproof induction furnace pot with mechanical tilting crucible and orange hot core',
 'compact robotic assembly arm on a rigid rotary base with precision gripper',
 'clean CNC fabrication cell with enclosed cutting head and compact rotary table',
 'industrial laser cutting head over a compact material fixture',
 'precision automated component assembler with twin synchronized tool heads',
 'autonomous overhead gantry manipulator with compact suspended gripper',
 'heavy automated forging manipulator with massive articulated clamp',
 'sealed nanofabrication chamber with visible central process vessel',
 'orbital component assembler with levitating concentric tool ring around a work cradle',
 'monumental automated actuator press with articulated side arms',
 'phase-matter fabricator with luminous cyan containment ring and central build cradle',
 'stellar precision assembler with crown-like articulated tool arms around a bright process core']
MACHINE_SECONDARY=[
 'short rugged belt feeder with two visible rollers and mechanical drive housing',
 'compact parcel sorting conveyor with one diverter arm and roller bed',
 'industrial heat exchanger with twin pipes, pump housing and cooling fins',
 'compact parts conveyor with rotary indexing table and feeder bins integrated into one machine',
 'smart logistics transfer gate with enclosed roller bed and sensor mast integrated into the chassis',
 'battery handling carousel with four enclosed energy-cell sockets and robotic transfer arm',
 'compact coolant circulation pump with manifold, transparent reservoir and rigid pipe loop',
 'industrial power distribution manifold with three insulated bus conduits and switching housing',
 'maglev cargo feeder with one continuous levitation trough and cyan guide seam',
 'plasma energy routing manifold with insulated conduits converging on a bright central chamber',
 'levitation transfer ring mounted to a compact orbital logistics cradle',
 'high-capacity energy manifold with multiple rigid conduits and central distribution hub',
 'phase-energy routing ring with three cyan conduits and a compact containment pedestal',
 'singularity-safe energy distributor with concentric containment hoops around a dark central node']
TERRAIN_SUBJECTS={
 'TER-00':'one square cracked industrial concrete ground tile, worn dark steel patches and subtle grime, straight seam-safe edges',
 'TER-01':'one square industrial road and curb connector tile, asphalt lane strip with concrete curb, no painted letters or symbols',
 'TER-02':'one square embedded cargo rail strip tile, twin steel rails in rugged industrial decking, straight seamless connectors',
 'TER-03':'one square recessed conduit trench tile with removable steel grates and visible insulated utility pipes',
 'TER-04':'one square clean commercial pavement tile, premium concrete panels with restrained metal expansion joints',
 'TER-05':'one square clean multi-lane road connector tile, dark asphalt with raised curb modules, no arrows or text markings',
 'TER-06':'one square industrial loading pad tile with reinforced metal corners and clean heavy-duty surface',
 'TER-07':'one square energy conduit infrastructure tile with a flush cyan power channel embedded through the center',
 'TER-08':'one square reinforced megastructure platform tile, layered dark alloy deck plates and structural edge ribs',
 'TER-09':'one square maglev rail connector tile with twin flush cyan magnetic guide channels in a premium alloy deck',
 'TER-10':'one square elevated service deck module with structural underside lip, access panels and clean connector edges',
 'TER-11':'one square megastructure energy-spine tile with a broad flush cyan conduit embedded in armored decking',
 'TER-12':'one square apex phase platform tile with pearl alloy panels and a restrained flush cyan-violet phase ring pattern without symbols',
 'TER-13':'one square apex stellar connector tile with dark premium alloy, embedded warm stellar energy seam and cyan containment accents'}
def manifest_rows():
 order=0
 for line in MANIFEST.read_text(encoding='utf-8').splitlines():
  m=ROW.match(line)
  if not m:continue
  asset_id,name,description,runtime,status=[x.strip() for x in m.groups()]
  if not asset_id.startswith(SUPPORTED) or status.upper()!='TODO':continue
  yield {'id':asset_id,'name':name,'description':description,'runtime':runtime,'stem':Path(runtime).stem,'kind':asset_id.split('-',1)[0],'order':order};order+=1
def concrete_subject(i):
 if i['kind']=='MCH':
  m=re.fullmatch(r'MCH-(\d{2})-([01])',i['id']);idx=int(m.group(1));variant=int(m.group(2));return (MACHINE_PRIMARY if variant==0 else MACHINE_SECONDARY)[idx]
 if i['kind']=='TER':return TERRAIN_SUBJECTS[i['id']]
 if i['kind']=='PRP':
  m=re.fullmatch(r'PRP-(\d{2})-([AB])',i['id']);idx=int(m.group(1));v=m.group(2)
  a=['rugged closed supply crate','compact closed retail stock crate','heatproof closed tool chest','closed assembly parts bin','closed industrial logistics crate','sealed component case','reinforced tool locker','closed automation parts crate','high-tech cargo case','energy-cell storage box','precision maintenance chest','orbital supply container','phase-tech component crate','prestige equipment case'];b=['90-degree utility pipe elbow fitting','compact safety barrier','90-degree insulated service pipe elbow fitting','small control terminal','utility bollard','cable junction pedestal','compact pipe manifold','service terminal','90-degree coolant pipe elbow fitting','power distribution post','sensor bollard','orbital service terminal','90-degree phase conduit elbow fitting','prestige light bollard'];return (a if v=='A' else b)[min(idx,13)]
 if i['kind']=='VEH':
  exact={'VEH-09':'ONE futuristic enclosed MAGLEV FREIGHT CAPSULE, ZERO wheels, continuous smooth magnetic levitation hull, four flush glowing rectangular magnetic lift emitters, large visible air gap beneath the entire hull, long cargo-container proportions, no road styling, rail, track or platform','VEH-16':'one compact two-passenger prestige anti-gravity coupe, low sleek teardrop capsule, panoramic dark glass canopy, completely blank unbranded featureless nose with no ornament at all, one continuous smooth rounded belly, thin cyan levitation light seam painted flush into the lower hull, large open empty air gap beneath the complete hull, pearl white and glossy black premium finish, zero wheels, wheel arches, legs, feet, struts, landing gear, skids, rails, blades, bars or pods','VEH-17':'a tight coordinated swarm of five distinct small singularity logistics drones in one compact formation, all five drones fully visible, no mothership'};return exact.get(i['id'],i['name'])
 if i['kind']=='CORE':return i['name']
 return i['name']
def prompt_for(i):
 s=concrete_subject(i)
 if i['kind']=='MCH':return f"AAA premium mobile strategy production sprite of {s}. Exactly ONE self-contained industrial machine assembly, fully visible, isolated on pure black with generous empty margin. 34 degree three-quarter 2.5D camera, compact readable silhouette, upper-left key light, cool fill, era-appropriate restrained amber/cyan emissive accents. Show mechanical joints and moving mechanism clearly but keep every part physically attached to the single machine. No worker, building, room, floor slab, loose props, text, numbers, badge, logo, UI or background rectangle. Manifest intent: {i['description']}"
 if i['kind']=='TER':return f"AAA premium mobile strategy infrastructure sprite of {s}. Exactly ONE complete square modular tile, fully visible in 34 degree three-quarter 2.5D view, centered on pure black with generous empty margin. Four outer tile edges must be straight, clean and connector-friendly; no surrounding scene, buildings, vehicles, people, loose props, text, letters, numbers, arrows, logos, UI or border. Upper-left key light, cool fill. Manifest intent: {i['description']}"
 if i['id']=='VEH-16':return f"AAA mobile strategy sprite of {s}. ONE personal luxury hover coupe, fully visible, 34 degree three-quarter view, floating high, isolated on pure black. Completely smooth blank nose panel with ZERO emblem, ornament, badge, grille or symbol. Underside is a continuous closed hull; cyan light is flush paint/emission, never a separate object. Empty black air below every part. Upper-left key, cool fill. No road, floor, pedestal, detached underside object, text, symbol, badge, logo or UI."
 noun={'PRP':'prop','VEH':'vehicle composition','CORE':'reactor'}[i['kind']];return f"Create exactly {s}. One centered {noun}, fully visible, isolated on pure black. No environment, floor, road, pedestal, text, logo, labels or UI. Premium stylized 2.5D mobile strategy asset, 34 degree three-quarter camera, upper-left key, cool fill, restrained cyan/amber accents. Manifest intent: {i['description']}. Generous empty black edge space."
def load_encode():
 print('KAGGLE_FLUX_LOAD=encoder',flush=True);text2=T5EncoderModel.from_pretrained(FLUX,subfolder='text_encoder_2',torch_dtype=torch.float16,device_map='cuda');pipe=FluxPipeline.from_pretrained(FLUX,text_encoder_2=text2,transformer=None,vae=None,torch_dtype=torch.float16,device_map='cuda');return text2,pipe
def load_diffuse():
 print('KAGGLE_FLUX_LOAD=transformer',flush=True);tr=FluxTransformer2DModel.from_pretrained(FLUX,subfolder='transformer',torch_dtype=torch.float16,device_map='cuda');pipe=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=tr,vae=None,torch_dtype=torch.float16,device_map='cuda');return tr,pipe
def load_decode():
 print('KAGGLE_FLUX_LOAD=vae',flush=True);return FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=None,torch_dtype=torch.float16,device_map='cuda')
def border_background(im):
 rgb=im.convert('RGB');w,h=rgb.size;s=max(1,min(w,h)//128);pts=[]
 for x in range(0,w,s):pts += [rgb.getpixel((x,0)),rgb.getpixel((x,h-1))]
 for y in range(0,h,s):pts += [rgb.getpixel((0,y)),rgb.getpixel((w-1,y))]
 pts.sort(key=sum);q=pts[:max(16,len(pts)//3)];return tuple(sum(p[i] for p in q)//len(q) for i in range(3))
def isolate(im):
 rgb=im.convert('RGB');w,h=rgb.size;bg=border_background(rgb);px=rgb.load();dist=Image.new('L',(w,h));dp=dist.load()
 for y in range(h):
  for x in range(w):
   r,g,b=px[x,y];dp[x,y]=min(255,int((((r-bg[0])**2+(g-bg[1])**2+(b-bg[2])**2)**.5)*3))
 mask=dist.point(lambda p:0 if p<20 else 255 if p>58 else int((p-20)*255/38));mp=mask.load();seen=set();q=deque()
 for x in range(w):
  for y in (0,h-1):
   if mp[x,y]<180 and (x,y) not in seen:seen.add((x,y));q.append((x,y))
 for y in range(h):
  for x in (0,w-1):
   if mp[x,y]<180 and (x,y) not in seen:seen.add((x,y));q.append((x,y))
 while q:
  x,y=q.popleft();mp[x,y]=0
  for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
   if 0<=nx<w and 0<=ny<h and (nx,ny) not in seen and mp[nx,ny]<180:seen.add((nx,ny));q.append((nx,ny))
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
def finish(image,item):
 master=isolate(image);comps=components(master.getchannel('A'))
 if not comps:raise RuntimeError('empty isolated subject')
 total=sum(map(len,comps));allow=item['id']=='VEH-17';dominant=len(comps[0])/total;important=sum(len(c)/total>=.08 for c in comps)
 if not allow and (important>=2 or (len(comps)>=3 and dominant<.88)):raise RuntimeError('multiple-object composition')
 selected=comps if allow else comps[:1];xs=[x for c in selected for x,y in c];ys=[y for c in selected for x,y in c];w,h=master.size
 crop=master.crop((max(0,int(min(xs)*w/128)-25),max(0,int(min(ys)*h/128)-25),min(w,int((max(xs)+1)*w/128)+25),min(h,int((max(ys)+1)*h/128)+25)));bbox=crop.getbbox()
 if not bbox:raise RuntimeError('empty alpha')
 crop=crop.crop(bbox);side=TARGET_SIDE[item['kind']];subject_fraction=.76 if item['kind']=='TER' else .68;scale=min(side*subject_fraction/crop.width,side*subject_fraction/crop.height);crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS);out=Image.new('RGBA',(side,side));bottom=.12 if item['kind']!='TER' else .10;out.alpha_composite(crop,((side-crop.width)//2,side-int(side*bottom)-crop.height));a=out.getchannel('A');lo,hi=a.getextrema();visible=sum(a.histogram()[8:])/(side*side)
 maxcov=.58 if item['kind'] in ('MCH','TER','PRP') else .70
 if hi==0 or lo==255 or visible<.04 or visible>maxcov:raise RuntimeError(f'alpha coverage {visible:.1%}')
 pad=int(side*.06)
 if any(e.getbbox() for e in (a.crop((0,0,side,pad)),a.crop((0,side-pad,side,side)),a.crop((0,0,pad,side)),a.crop((side-pad,0,side,side)))):raise RuntimeError('padding failed')
 return out,visible
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--kind',choices=['ALL','MCH','TER','PRP','VEH','CORE'],default='ALL');ap.add_argument('--count',type=int,default=30);ap.add_argument('--seed',type=int,default=12217);args=ap.parse_args();items=[x for x in manifest_rows() if args.kind=='ALL' or x['kind']==args.kind];items.sort(key=lambda x:(PRIORITY[x['kind']],x['order']));items=items[:max(1,args.count)];print(f'KAGGLE_PLAN={len(items)} targets={",".join(x["id"] for x in items)} engine=FLUX.1-schnell-NF4-batched-v2',flush=True)
 if not items:return
 INCOMING.mkdir(parents=True,exist_ok=True);encoded=[];text2,enc=load_encode()
 for index,item in enumerate(items,1):
  try:
   with torch.no_grad():pe,ppe,_=enc.encode_prompt(prompt=prompt_for(item),max_sequence_length=384)
   encoded.append((item,index,pe.cpu(),ppe.cpu()))
  except Exception as exc:print(f"KAGGLE_REJECTED={item['id']} stage=encode reason={exc}",flush=True)
 del text2,enc;gc.collect();torch.cuda.empty_cache();tr,diff=load_diffuse();latents=[]
 for item,index,pe,ppe in encoded:
  try:
   pe=pe.cuda();ppe=ppe.cuda();packed=diff(height=1024,width=1024,num_inference_steps=4,guidance_scale=0.0,prompt_embeds=pe,pooled_prompt_embeds=ppe,output_type='latent',max_sequence_length=384,generator=torch.Generator(device='cuda').manual_seed(args.seed+index)).images;latents.append((item,packed.cpu()));print(f"KAGGLE_DIFFUSED={item['id']}",flush=True)
  except Exception as exc:print(f"KAGGLE_REJECTED={item['id']} stage=diffuse reason={exc}",flush=True)
  finally:gc.collect();torch.cuda.empty_cache()
 del tr,diff,encoded;gc.collect();torch.cuda.empty_cache();dec=load_decode();ok=rej=0
 for item,packed in latents:
  try:
   packed=packed.cuda();lat=dec._unpack_latents(packed,height=1024,width=1024,vae_scale_factor=dec.vae_scale_factor)/dec.vae.config.scaling_factor+dec.vae.config.shift_factor
   with torch.no_grad():tensor=dec.vae.decode(lat,return_dict=False)[0]
   image=dec.image_processor.postprocess(tensor)[0];final,cov=finish(image,item);out=INCOMING/f"{item['stem']}.png";final.save(out,'PNG',optimize=True);ok+=1;print(f'KAGGLE_VALIDATED={out.relative_to(ROOT)} coverage={cov:.1%}',flush=True)
  except Exception as exc:rej+=1;print(f"KAGGLE_REJECTED={item['id']} stage=decode reason={type(exc).__name__}: {exc}",flush=True)
  finally:gc.collect();torch.cuda.empty_cache()
 print(f'KAGGLE_BATCH_SUCCESS={ok} KAGGLE_BATCH_REJECTED={rej} KAGGLE_BATCH_ATTEMPTED={len(items)}',flush=True)
if __name__=='__main__':main()
