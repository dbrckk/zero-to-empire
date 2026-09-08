#!/usr/bin/env python3
"""Validated procedural FX-sheet factory for Zero -> Empire.
Candidate-only: outputs must still pass semantic/runtime/CI gates before strict DONE.
"""
from __future__ import annotations
import argparse,json,math,random,re
from pathlib import Path
from PIL import Image,ImageDraw,ImageFilter
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'; OUT=Path('/kaggle/working/output')
ROW=re.compile(r'^\|\s*(FX-\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$')
FRAMES=8; CELL=256
ONE_SHOT={'FX-00','FX-05','FX-06','FX-07'}
LOOP={'FX-01','FX-02','FX-03','FX-04'}

def rows():
 for line in MANIFEST.read_text(encoding='utf-8').splitlines():
  m=ROW.match(line)
  if m and m.group(5).strip().upper()=='TODO':
   yield {'id':m.group(1),'name':m.group(2).strip(),'runtime':m.group(4).strip(),'stem':Path(m.group(4)).stem+'_final' if not Path(m.group(4)).stem.endswith('_final') else Path(m.group(4)).stem}

def rgba(): return Image.new('RGBA',(CELL,CELL),(0,0,0,0))
def glow(layer,r): return layer.filter(ImageFilter.GaussianBlur(r))
def add(dst,src): return Image.alpha_composite(dst,src)

def particle_frame(kind,t,rng,item_id=''):
 im=rgba();d=ImageDraw.Draw(im);cx=cy=CELL//2
 # One-shot envelope: fast attack, readable middle, clean decay.
 env=max(0.0,math.sin(math.pi*min(1.0,max(0.0,t))))
 if 'spark' in kind or 'welding' in kind:
  count=max(4,round(26*env))
  for _ in range(count):
   a=rng.uniform(-2.8,-.35); L=rng.uniform(18,70)*(0.45+0.55*env); x=cx+rng.uniform(-8,8); y=cy+rng.uniform(-4,8); x2=x+math.cos(a)*L; y2=y+math.sin(a)*L
   d.line((x,y,x2,y2),fill=(255,190+rng.randrange(55),70,round(235*env)),width=rng.choice((2,3)))
 elif 'flame' in kind:
  for j in range(7):
   phase=(j/7+t)%1; w=22+10*math.sin(phase*math.pi); h=72+34*math.sin(phase*math.pi); x=cx+rng.uniform(-18,18); y=cy+38-h*.55
   d.ellipse((x-w,y-h,x+w,y+h*.25),fill=((70,210,255,170) if 'plasma' in kind else (255,150,35,190)))
 elif 'dust' in kind:
  # Construction impact: expanding dust plus discrete ballistic rubble fragments.
  # The fragments are deliberately polygonal so FX-07 cannot collapse into generic smoke.
  dust_alpha=round(150*env)
  for j in range(max(4,round(14*env))):
   phase=min(1.0,j/14+t*.72); r=7+27*phase; x=cx+rng.uniform(-48,48)*(0.3+phase); y=cy+48-50*phase+rng.uniform(-8,8)
   d.ellipse((x-r,y-r,x+r,y+r),fill=(190,175,145,dust_alpha))
  for j in range(max(3,round(12*env))):
   direction=rng.uniform(math.pi*.12,math.pi*.88); speed=rng.uniform(30,82); flight=t
   x=cx+math.cos(direction)*speed*flight+rng.uniform(-8,8)
   y=cy+38-math.sin(direction)*speed*flight+58*(flight**2)
   rr=rng.randint(3,7); col=rng.choice(((116,105,88,round(230*env)),(145,126,96,round(220*env)),(91,91,88,round(220*env))))
   pts=[(x-rr,y),(x-rr*.25,y-rr),(x+rr,y-rr*.25),(x+rr*.55,y+rr),(x-rr*.5,y+rr*.65)]
   d.polygon(pts,fill=col)
 elif 'smoke' in kind or 'steam' in kind:
  for j in range(9):
   phase=(j/9+t)%1; r=10+34*phase; x=cx+rng.uniform(-35,35)*(0.4+phase); y=cy+55-95*phase+rng.uniform(-10,10)
   col=(210,225,235,110) if 'steam' in kind else (120,125,130,100)
   d.ellipse((x-r,y-r,x+r,y+r),fill=col)
 elif 'pulse' in kind or 'flare' in kind or 'shimmer' in kind or 'flash' in kind:
  rr=24+72*env; col=(70,225,255,round(220*env)) if 'cyan' in kind else (255,185,70,round(220*env))
  d.ellipse((cx-rr,cy-rr,cx+rr,cy+rr),outline=col,width=7)
  d.ellipse((cx-rr*.35,cy-rr*.35,cx+rr*.35,cy+rr*.35),fill=col)
 elif 'arc' in kind:
  pts=[(cx-78,cy+rng.uniform(-16,16))]
  for j in range(1,8):pts.append((cx-78+j*22,cy+rng.uniform(-38,38)))
  d.line(pts,fill=(120,230,255,235),width=5)
 elif 'scan' in kind:
  y=38+180*t; d.rectangle((34,y-4,222,y+4),fill=(80,235,255,190)); d.rectangle((54,42,202,214),outline=(80,235,255,75),width=2)
 elif 'thruster' in kind or 'trail' in kind:
  L=80+40*math.sin(math.pi*t); d.polygon([(cx-18,cy-35),(cx+18,cy-35),(cx+8,cy+L),(cx-8,cy+L)],fill=(80,210,255,165)); d.ellipse((cx-22,cy-42,cx+22,cy-15),fill=(210,250,255,230))
 elif 'distortion' in kind or 'singularity' in kind:
  for r in (28,46,66): d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=(120,110,255,150),width=5)
 else:
  rr=24+65*t; d.ellipse((cx-rr,cy-rr,cx+rr,cy+rr),outline=(255,220,120,180),width=6)
 return add(glow(im,8),im)

def metrics(im):
 a=im.getchannel('A'); box=a.getbbox()
 if not box:return {'ok':False,'reason':'empty','coverage':0.0,'alpha_mass':0}
 x0,y0,x1,y1=box; data=list(a.getdata());cov=sum(1 for v in data if v>12)/(CELL*CELL); mass=sum(data)
 edge=(x0<=2 or y0<=2 or x1>=CELL-2 or y1>=CELL-2)
 return {'ok':not edge and .001<=cov<=.50,'coverage':cov,'alpha_mass':mass,'bbox':box,'edge':edge}

def temporal_qa(item,report):
 masses=[m['alpha_mass'] for m in report]; peak=max(range(len(masses)),key=masses.__getitem__)
 if item['id'] in ONE_SHOT:
  # A one-shot must peak away from the ends and visibly decay by its final frame.
  if peak in (0,len(masses)-1): raise RuntimeError(f'one-shot-peak-at-edge={peak}')
  if masses[-1] > masses[peak]*.58: raise RuntimeError('one-shot-insufficient-decay')
  return {'mode':'one-shot','peak_frame':peak,'decay_ratio':round(masses[-1]/max(1,masses[peak]),3)}
 if item['id'] in LOOP:
  return {'mode':'loop','peak_frame':peak}
 return {'mode':'unspecified','peak_frame':peak}

def sheet_for(item,seed):
 frames=[]; report=[]
 for i in range(FRAMES):
  rng=random.Random(seed+i*7919+int(item['id'].split('-')[1])*100003); f=particle_frame(item['name'].lower(),i/(FRAMES-1),rng,item['id']); m=metrics(f)
  if not m['ok']: raise RuntimeError(f"frame-{i}:{m}")
  frames.append(f); report.append(m)
 sig=[]; centers=[]
 for f,m in zip(frames,report):
  a=f.getchannel('A').resize((32,32)); sig.append(bytes(a.getdata())); b=m['bbox']; centers.append(((b[0]+b[2])/2,(b[1]+b[3])/2))
 dup=sum(sig[i]==sig[i-1] for i in range(1,len(sig)))
 drift=max(math.hypot(x-CELL/2,y-CELL/2) for x,y in centers)
 if dup>1: raise RuntimeError(f'too-many-duplicate-frames={dup}')
 if drift>64: raise RuntimeError(f'center-drift={drift:.1f}')
 temporal=temporal_qa(item,report)
 sheet=Image.new('RGBA',(CELL*FRAMES,CELL),(0,0,0,0))
 for i,f in enumerate(frames): sheet.alpha_composite(f,(i*CELL,0))
 return sheet,{'frames':FRAMES,'cell':'256x256','layout':'horizontal-8','duplicate_adjacent':dup,'max_center_drift':round(drift,2),**temporal,'frame_metrics':report}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=18);ap.add_argument('--seed',type=int,default=90210);args=ap.parse_args()
 INCOMING.mkdir(parents=True,exist_ok=True); OUT.mkdir(parents=True,exist_ok=True)
 rep={'engine':'procedural-fx-v1.1-temporal-qa','attempted':0,'accepted':0,'rejected':0,'runtime_contract':'candidate-only horizontal-8; runtime integration required before strict DONE','items':[]}
 for item in list(rows())[:args.count]:
  rep['attempted']+=1; accepted=None; errors=[]
  for attempt in range(4):
   try:
    sheet,m=sheet_for(item,args.seed+attempt*104729); accepted=(sheet,m,attempt); print(f'KAGGLE_FX_LIVE_PASS={item["id"]} attempt={attempt+1} mode={m["mode"]}',flush=True);break
   except Exception as e: errors.append(str(e)); print(f'KAGGLE_FX_LIVE_REJECT={item["id"]} attempt={attempt+1} reason={e}',flush=True)
  if not accepted:
   rep['rejected']+=1;rep['items'].append({'id':item['id'],'accepted':False,'errors':errors});continue
  sheet,m,attempt=accepted; p=INCOMING/f"{item['stem']}.png"; sheet.save(p,'PNG',optimize=True); rep['accepted']+=1;rep['items'].append({'id':item['id'],'accepted':True,'attempt':attempt+1,**m}); print(f'KAGGLE_VALIDATED={p.relative_to(ROOT)}',flush=True)
 (OUT/'fx-sheet-report.json').write_text(json.dumps(rep,indent=2),encoding='utf-8')
 print(f'KAGGLE_FX_SUCCESS={rep["accepted"]} KAGGLE_FX_REJECTED={rep["rejected"]}',flush=True)
 if rep['accepted']==0: raise SystemExit('No validated FX sheets')
if __name__=='__main__':main()
