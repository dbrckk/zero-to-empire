#!/usr/bin/env python3
from __future__ import annotations
import json, math, os, re, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image
from rembg import remove, new_session

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
PROD=ROOT/'art/production'
CHR=re.compile(r'^CHR-(OP|TECH|LOG|ENG)-(IDLE|WALK|WORK|CARRY|REPAIR|CELEB)$')
ROLE={'OP':'foundry operator, practical dark workwear, rust-orange utility accents, gloves','TECH':'industrial technician, graphite coveralls, cyan diagnostic accents, compact tool belt','LOG':'logistics worker, reinforced work jacket, amber safety accents, cargo gloves','ENG':'industrial engineer, clean graphite field suit, restrained cyan accents, utility harness'}
ACTION={'IDLE':('idle breathing and subtle look-around',6),'WALK':('walking cycle, clear alternating steps',8),'WORK':('operating a compact industrial hand tool',10),'CARRY':('carrying one compact industrial crate with both hands',8),'REPAIR':('repairing with a compact diagnostic or welding tool',10),'CELEB':('short restrained milestone celebration, raised arm, no props',8)}
POSE_HINT={'IDLE':['neutral stance','weight slightly left','neutral stance','weight slightly right','small head turn left','small head turn right'],'WALK':['left contact','left down','passing left','right contact','right down','passing right','left contact recovery','neutral passing'],'WORK':['tool ready','reach forward','tool contact','working low','working center','working high','pull back','inspect','tool down','neutral'],'CARRY':['carry neutral','left step','passing','right step','carry neutral','left step','passing','right step'],'REPAIR':['kneel or reach','tool contact','repair pose','inspect','tool contact','adjust','inspect','tool contact','rise slightly','neutral repair'],'CELEB':['neutral','arm starts up','arm half up','arm raised','small fist pump','arm half down','arm down','neutral']}

def pending_rows():
    out=[]; bld=0
    for line in MANIFEST.read_text(encoding='utf-8').splitlines():
        if not line.startswith('|') or 'app/src/main/res/' not in line: continue
        cols=[c.strip() for c in line.split('|')[1:-1]]
        if len(cols)!=5 or cols[4].upper()!='TODO': continue
        if cols[0].startswith('BLD-'): bld+=1
        if CHR.fullmatch(cols[0]): out.append(cols)
    return bld,out

def prompt(role,action,pose):
    return (f'AAA mobile 2.5D full-body {ROLE[role]}. Same single adult worker, same face, same clothing, same body proportions. '
            f'{ACTION[action][0]}; animation phase: {pose}. 34-degree three-quarter orthographic game view. '
            'Full body and feet fully visible, centered, compact readable silhouette, no crop. '
            'Flat uniform neutral gray background to every edge. No floor, scenery, text, logo, extra people, duplicate limbs, vehicle, building.')

def fetch(prompt_text,seed):
    q=urllib.parse.quote(prompt_text,safe='')
    url=f'https://image.pollinations.ai/prompt/{q}?model=flux&width=512&height=512&seed={int(seed)}&nologo=true&private=true&enhance=false&safe=true'
    req=urllib.request.Request(url,headers={'User-Agent':'zero-to-empire-github-actions/1.0'})
    with urllib.request.urlopen(req,timeout=90) as r: data=r.read()
    if len(data)<8000: raise RuntimeError(f'response too small: {len(data)}')
    p=Path('/tmp/chr-frame.png'); p.write_bytes(data)
    return Image.open(p).convert('RGBA')

def finish_frame(raw,session):
    cut=remove(raw,session=session,alpha_matting=False)
    if not isinstance(cut,Image.Image): cut=Image.open(cut).convert('RGBA')
    cut=cut.convert('RGBA'); a=cut.getchannel('A').point(lambda v:0 if v<24 else 255 if v>224 else v);cut.putalpha(a)
    bb=a.getbbox()
    if not bb: raise RuntimeError('empty alpha')
    crop=cut.crop(bb); cw,ch=crop.size
    if ch<cw*.90: raise RuntimeError('not full-body silhouette')
    scale=min(176/max(1,cw),218/max(1,ch))
    crop=crop.resize((max(1,round(cw*scale)),max(1,round(ch*scale))),Image.Resampling.LANCZOS)
    cell=Image.new('RGBA',(256,256),(0,0,0,0))
    x=(256-crop.width)//2; y=238-crop.height
    if y<8: raise RuntimeError('insufficient top padding')
    cell.alpha_composite(crop,(x,y))
    aa=cell.getchannel('A'); cov=sum(aa.histogram()[8:])/(256*256)
    if not .10<=cov<=.48: raise RuntimeError(f'coverage={cov:.3f}')
    edges=(aa.crop((0,0,256,8)),aa.crop((0,248,256,256)),aa.crop((0,0,8,256)),aa.crop((248,0,256,256)))
    if any(e.getbbox() is not None for e in edges): raise RuntimeError('unsafe cell padding')
    return cell,cov

def alpha_iou(a,b):
    A=a.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
    B=b.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
    pa,pb=A.load(),B.load();inter=union=0
    for y in range(64):
        for x in range(64):
            aa=pa[x,y]>0;bb=pb[x,y]>0;inter+=aa and bb;union+=aa or bb
    return inter/union if union else 0

def mean_color(frame):
    rgb=frame.convert('RGB');a=frame.getchannel('A');rp=rgb.load();ap=a.load();s=[0,0,0];n=0
    for y in range(0,256,2):
        for x in range(0,256,2):
            if ap[x,y]>=64:
                p=rp[x,y];s[0]+=p[0];s[1]+=p[1];s[2]+=p[2];n+=1
    return tuple(v/max(1,n) for v in s)

def sheet_qa(frames):
    ious=[alpha_iou(frames[i-1],frames[i]) for i in range(1,len(frames))]
    if min(ious)<.24:return False,f'silhouette-jump={min(ious):.2f}'
    if max(ious)>.992:return False,'duplicate-adjacent-frame'
    bottoms=[];centers=[];heights=[]
    for f in frames:
        bb=f.getchannel('A').getbbox()
        if not bb:return False,'empty-frame'
        bottoms.append(bb[3]);centers.append((bb[0]+bb[2])/2);heights.append(bb[3]-bb[1])
    if max(bottoms)-min(bottoms)>5:return False,'feet-pivot-drift'
    if max(centers)-min(centers)>34:return False,'horizontal-drift'
    if max(heights)/max(1,min(heights))>1.28:return False,'scale-drift'
    cols=[mean_color(f) for f in frames];base=cols[0]
    dmax=max(math.sqrt(sum((c[i]-base[i])**2 for i in range(3))) for c in cols)
    if dmax>95:return False,f'palette-drift={dmax:.1f}'
    return True,f'min-iou={min(ious):.2f} pivot={max(bottoms)-min(bottoms)} palette={dmax:.1f}'

def main():
    bld,rows=pending_rows()
    if bld:
        print(f'CHARACTER_DEFER_BUILDINGS_REMAIN={bld}')
        raise SystemExit(3)
    if not rows:
        print('CHARACTER_ALL_DONE=1');return
    aid,name,desc,runtime,status=rows[0]
    role,action=CHR.fullmatch(aid).groups()
    base=int(os.getenv('POLLINATIONS_CHR_SEED','19417'))
    attempts=max(1,min(int(os.getenv('POLLINATIONS_CHR_ATTEMPTS','3')),4))
    session=new_session('u2net'); failures=[]
    for attempt in range(attempts):
        seed=(base+attempt*7919)%2147483647;frames=[]
        try:
            for fi,pose in enumerate(POSE_HINT[action][:ACTION[action][1]]):
                frame,cov=finish_frame(fetch(prompt(role,action,pose),seed+fi*211),session)
                frames.append(frame);print(f'CHR_FRAME={aid} frame={fi} cov={cov:.3f}',flush=True)
            ok,why=sheet_qa(frames)
            if not ok: raise RuntimeError(why)
            sheet=Image.new('RGBA',(1024,1024),(0,0,0,0))
            for n,f in enumerate(frames): sheet.alpha_composite(f,((n%4)*256,(n//4)*256))
            stem=Path(runtime.replace(chr(96),'')).stem
            INCOMING.mkdir(parents=True,exist_ok=True);p=INCOMING/f'{stem}.png';sheet.save(p,'PNG',optimize=True)
            PROD.mkdir(parents=True,exist_ok=True)
            (PROD/'pollinations-character-report.json').write_text(json.dumps({'target':aid,'seed':seed,'frames':len(frames),'qa':why,'candidate':str(p.relative_to(ROOT))},indent=2),encoding='utf-8')
            print('CHARACTER_CANDIDATE='+str(p.relative_to(ROOT)));return
        except Exception as e:
            failures.append({'attempt':attempt+1,'seed':seed,'error':repr(e)})
            print(f'CHR_RETRY={aid} attempt={attempt+1} reason={e}',flush=True)
    PROD.mkdir(parents=True,exist_ok=True)
    (PROD/'pollinations-character-report.json').write_text(json.dumps({'target':aid,'failures':failures},indent=2),encoding='utf-8')
    raise SystemExit(2)

if __name__=='__main__':main()
