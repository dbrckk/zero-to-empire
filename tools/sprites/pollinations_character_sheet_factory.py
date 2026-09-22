#!/usr/bin/env python3
from pathlib import Path
import json, os, time, urllib.parse, urllib.request
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
OUT=ROOT/'art/production'
QUEUE=OUT/'controlled-character-regen-queue.json'

ROLES={
'OP':'foundry operator, dark graphite workwear, rust-orange utility accents, gloves, compact hard-hat',
'TECH':'industrial technician, graphite coveralls, cyan diagnostic accents, compact tool belt',
'LOG':'logistics worker, reinforced work jacket, amber safety accents, cargo gloves',
'ENG':'industrial engineer, clean graphite field suit, restrained cyan accents, utility harness'}
ACTIONS={
'IDLE':('idle breathing and subtle look-around',6),
'WALK':('walking cycle with alternating steps',8),
'WORK':('operating one compact industrial hand tool',10),
'CARRY':('carrying one identical compact industrial crate with both hands',8),
'REPAIR':('repairing with one compact diagnostic tool',10),
'CELEB':('short restrained milestone celebration',8)}
POSES={
'IDLE':['neutral','weight left','neutral recovery','weight right','head left','head right'],
'WALK':['left contact','left down','passing left','right contact','right down','passing right','left recovery','neutral passing'],
'WORK':['tool ready','reach','contact','work low','work center','work high','pull back','inspect','tool down','neutral'],
'CARRY':['carry neutral','left step','passing','right step','carry neutral recovery','left step recovery','passing recovery','right step recovery'],
'REPAIR':['reach','tool contact','repair low','inspect','tool contact high','adjust','inspect side','tool contact','rise','neutral repair'],
'CELEB':['neutral','arm starts up','arm half up','arm raised','small fist pump','arm half down','arm down','neutral recovery']}

def pending():
    manifest={}
    for line in MANIFEST.read_text(encoding='utf-8').splitlines():
        if not line.startswith('|') or 'CHR-' not in line or 'app/src/main/res/' not in line:
            continue
        p=[x.strip() for x in line.split('|')[1:-1]]
        if len(p)!=5:
            continue
        aid=p[0]; z=aid.split('-')
        if len(z)!=3 or z[0]!='CHR' or z[1] not in ROLES or z[2] not in ACTIONS:
            continue
        runtime=p[3].replace(chr(96),'')
        manifest[aid]={'id':aid,'role':z[1],'action':z[2],'stem':Path(runtime).stem,'status':p[4].upper()}

    if QUEUE.is_file():
        q=json.loads(QUEUE.read_text(encoding='utf-8'))
        out=[]
        for item in q.get('targets',[]):
            if str(item.get('status','')).upper() not in {'PENDING','PENDING_KAGGLE'}:
                continue
            aid=str(item.get('id','')).upper()
            if aid not in manifest:
                raise RuntimeError('queued character missing from manifest: '+aid)
            out.append(manifest[aid])
        if out:
            return out

    return [x for x in manifest.values() if x['status']=='TODO']

def mark_queue(aid,status,seed=None):
    if not QUEUE.is_file():
        return
    q=json.loads(QUEUE.read_text(encoding='utf-8'))
    for item in q.get('targets',[]):
        if str(item.get('id','')).upper()==aid:
            item['status']=status
            if seed is not None:
                item['seed']=seed
            break
    QUEUE.write_text(json.dumps(q,indent=2)+'\n',encoding='utf-8')

def fetch(prompt,seed):
    q=urllib.parse.quote(prompt,safe='')
    last=None
    for n,delay in enumerate((0,8,20,40)):
        if delay:
            time.sleep(delay)
        s=(seed+n*7919) % 2147483647
        url=f'https://image.pollinations.ai/prompt/{q}?model=flux&width=1024&height=1024&seed={s}&nologo=true&private=true&enhance=false&safe=true'
        req=urllib.request.Request(url,headers={'User-Agent':'zero-to-empire-github-actions/1.0','Accept':'image/*'})
        try:
            with urllib.request.urlopen(req,timeout=180) as r:
                data=r.read()
            if len(data)<10000:
                raise RuntimeError(f'small response {len(data)}')
            p=Path('/tmp')/f'chr-sheet-{s}.png'
            p.write_bytes(data)
            return Image.open(p).convert('RGBA')
        except Exception as e:
            last=e
            print(f'POLLINATIONS_CHR_HTTP_RETRY seed={s} try={n+1} reason={e}',flush=True)
    raise RuntimeError(f'pollinations request exhausted retries: {last}')

def cutout(raw):
    from rembg import remove
    im=remove(raw,alpha_matting=False).convert('RGBA')
    a=im.getchannel('A').point(lambda v:0 if v<24 else 255 if v>224 else v)
    im.putalpha(a)
    w,h=im.size
    mask=a.point(lambda v:255 if v>=64 else 0)
    px=mask.load(); seen=set(); comps=[]
    for y in range(h):
        for x in range(w):
            if not px[x,y] or (x,y) in seen:
                continue
            stack=[(x,y)]; seen.add((x,y)); comp=[]
            while stack:
                cx,cy=stack.pop(); comp.append((cx,cy))
                for nx,ny in ((cx-1,cy),(cx+1,cy),(cx,cy-1),(cx,cy+1)):
                    if 0<=nx<w and 0<=ny<h and px[nx,ny] and (nx,ny) not in seen:
                        seen.add((nx,ny)); stack.append((nx,ny))
            comps.append(comp)
    if not comps:
        raise RuntimeError('no subject')
    keep=set(max(comps,key=len))
    clean=Image.new('RGBA',(w,h),(0,0,0,0))
    src=im.load(); dst=clean.load()
    for x,y in keep:
        dst[x,y]=src[x,y]
    bb=clean.getchannel('A').getbbox()
    if not bb:
        raise RuntimeError('empty')
    crop=clean.crop(bb); cw,ch=crop.size
    if ch<cw*.92:
        raise RuntimeError('not full body')
    s=min(176/cw,218/ch)
    crop=crop.resize((max(1,round(cw*s)),max(1,round(ch*s))),Image.Resampling.LANCZOS)
    cell=Image.new('RGBA',(256,256),(0,0,0,0))
    x=(256-crop.width)//2; y=238-crop.height
    if x<8 or y<8:
        raise RuntimeError('padding')
    cell.alpha_composite(crop,(x,y))
    aa=cell.getchannel('A')
    cov=sum(aa.histogram()[8:])/(256*256)
    if not .10<=cov<=.48:
        raise RuntimeError(f'coverage={cov:.3f}')
    return cell,cov

def iou(a,b):
    A=a.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
    B=b.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
    pa,pb=A.load(),B.load(); inter=union=0
    for y in range(64):
        for x in range(64):
            aa=pa[x,y]>0; bb=pb[x,y]>0
            inter+=aa and bb; union+=aa or bb
    return inter/union if union else 0

def appearance_hist(frame):
    # Coarse foreground RGB histogram: catches role/wardrobe/identity drift that
    # silhouette IoU alone cannot detect.
    rgb=frame.convert('RGB'); alpha=frame.getchannel('A')
    bins=[0]*512; total=0
    for (r,g,b),a in zip(rgb.getdata(),alpha.getdata()):
        if a < 64:
            continue
        bins[(r//32)*64+(g//32)*8+(b//32)] += 1
        total += 1
    return [v/total for v in bins] if total else bins

def hist_similarity(a,b):
    # Histogram intersection in [0,1].
    return sum(min(x,y) for x,y in zip(a,b))

def sheetqa(frames):
    vals=[iou(frames[n-1],frames[n]) for n in range(1,len(frames))]
    if min(vals)<.25:
        return False,f'iou={min(vals):.2f}'
    if max(vals)>.99:
        return False,'duplicate'
    h0=appearance_hist(frames[0])
    sims=[hist_similarity(h0,appearance_hist(f)) for f in frames[1:]]
    if sims and min(sims)<.48:
        return False,f'identity-palette={min(sims):.2f}'
    bottoms=[]; centers=[]
    for frame in frames:
        bb=frame.getchannel('A').getbbox()
        bottoms.append(bb[3]); centers.append((bb[0]+bb[2])/2)
    if max(bottoms)-min(bottoms)>6:
        return False,'pivot'
    if max(centers)-min(centers)>36:
        return False,'drift'
    return True,f'min-iou={min(vals):.2f}'

def sheet_prompt(item):
    action=item['action']; fc=ACTIONS[action][1]
    poses=', '.join(POSES[action][:fc])
    return (
        f'AAA premium mobile 2.5D sprite-sheet production image. SAME EXACT SINGLE ADULT CHARACTER in every frame: {ROLES[item["role"]]}. '
        f'Animation: {ACTIONS[action][0]}. Required chronological poses: {poses}. '
        'Create one exact 4 columns by 4 rows animation atlas on a perfectly flat uniform neutral gray background. '
        'Each cell contains exactly one full-body view of the same worker, same face, same gender presentation, same hair, same helmet, same clothes, same colors, same body proportions, same tool or carried object. '
        '34-degree three-quarter orthographic camera, feet visible, centered in every cell, identical scale and foot pivot. '
        'Use only the first required cells in reading order left-to-right then top-to-bottom; leave unused cells empty neutral gray. '
        'No cell labels, no text, no numbers, no borders, no logos, no extra people, no duplicated limbs, no changing accessories, no changing carried object, no scenery, no floor, no building, no vehicle, no gradient, no vignette.'
    )

def extract_frames(raw,frame_count):
    if raw.size!=(1024,1024):
        raw=raw.resize((1024,1024),Image.Resampling.LANCZOS)
    frames=[]
    for n in range(frame_count):
        x=(n%4)*256; y=(n//4)*256
        cell_raw=raw.crop((x,y,x+256,y+256))
        frame,cov=cutout(cell_raw)
        frames.append(frame)
        print(f'POLLINATIONS_CHR_CELL n={n} cov={cov:.3f}',flush=True)
    return frames

def main():
    items=pending()[:max(1,min(int(os.getenv('POLLINATIONS_CHR_BATCH','1')),2))]
    if not items:
        print('POLLINATIONS_CHR_NOTHING=1')
        return
    attempts=max(1,min(int(os.getenv('POLLINATIONS_CHR_ATTEMPTS','2')),3))
    base=int(os.getenv('POLLINATIONS_CHR_SEED','19417'))
    INCOMING.mkdir(parents=True,exist_ok=True); OUT.mkdir(parents=True,exist_ok=True)
    rep=[]

    for ix,it in enumerate(items):
        fc=ACTIONS[it['action']][1]
        done=False; last=''
        for att in range(attempts):
            seed=(base+ix*100000+att*10007) % 2147483647
            try:
                raw=fetch(sheet_prompt(it),seed)
                frames=extract_frames(raw,fc)
                ok,why=sheetqa(frames)
                if not ok:
                    raise RuntimeError(why)
                sheet=Image.new('RGBA',(1024,1024),(0,0,0,0))
                for n,frame in enumerate(frames):
                    sheet.alpha_composite(frame,((n%4)*256,(n//4)*256))
                p=INCOMING/f"{it['stem']}.png"
                sheet.save(p,'PNG',optimize=True)
                mark_queue(it['id'],'CANDIDATE',seed)
                rep.append({'id':it['id'],'status':'CANDIDATE','file':p.name,'frames':fc,'qa':why,'generation':'single-sheet'})
                print(f"POLLINATIONS_CHR_VALIDATED={it['id']} {why}",flush=True)
                done=True
                break
            except Exception as e:
                last=str(e)
                print(f"POLLINATIONS_CHR_RETRY={it['id']} attempt={att+1} reason={e}",flush=True)

        if not done:
            mark_queue(it['id'],'BLOCKED')
            rep.append({'id':it['id'],'status':'REJECT','reason':last,'generation':'single-sheet'})

    (OUT/'pollinations-character-summary.json').write_text(json.dumps(rep,indent=2),encoding='utf-8')
    print('POLLINATIONS_CHR_CANDIDATES='+str(sum(x['status']=='CANDIDATE' for x in rep)),flush=True)

if __name__=='__main__':
    main()
