#!/usr/bin/env python3
from pathlib import Path
import json, os, time, urllib.parse, urllib.request
import hashlib
from PIL import Image
# Support both execution as a script and importlib-based tooling from tools/assets.
try:
    from character_semantic_gate import clip_risk, frame_geometry
except ModuleNotFoundError as exc:
    if exc.name != 'character_semantic_gate':
        raise
    from tools.sprites.character_semantic_gate import clip_risk, frame_geometry

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
OUT=ROOT/'art/production'
QUEUE=OUT/'controlled-character-regen-queue.json'
# Each generation strategy owns its own cache: never reuse pre-v3 body
# fragments/identity-drifts as successful images of a different strategy.
STANDALONE_CACHE_EPOCH='full-body-per-frame-v3'

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
    requested={x.strip().upper() for x in os.getenv('POLLINATIONS_CHR_TARGET_IDS','').split(',') if x.strip()}
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
            if str(item.get('status','')).upper() not in {'PENDING','PENDING_POLLINATIONS'}:
                continue
            aid=str(item.get('id','')).upper()
            if requested and aid not in requested:
                continue
            if aid not in manifest:
                raise RuntimeError('queued character missing from manifest: '+aid)
            out.append(manifest[aid])
        # A controlled queue is authoritative, including when all targets are
        # BLOCKED, already reviewed, or reserved by another provider. Falling
        # through to unrelated manifest TODOs would bypass the reservation.
        return out

    return [x for x in manifest.values() if x['status']=='TODO' and (not requested or x['id'] in requested)]

def candidate_destination(item):
    """Controlled semantic repairs are immutable staged candidates, not runtime art.

    The original Kaggle/legacy sheet remains untouched until an explicit
    accepted review and separately verified runtime promotion.
    """
    q=json.loads(QUEUE.read_text(encoding='utf-8')) if QUEUE.is_file() else {}
    if q.get('mode')=='pollinations-controlled-repair':
        return OUT/'character-repair-candidates'/f"{item['stem']}.png"
    return INCOMING/f"{item['stem']}.png"


def mark_queue(aid,status,seed=None,producer=None,producer_run_id=None):
    if not QUEUE.is_file():
        return
    q=json.loads(QUEUE.read_text(encoding='utf-8'))
    for item in q.get('targets',[]):
        if str(item.get('id','')).upper()==aid:
            item['status']=status
            if seed is not None:
                item['seed']=seed
            if producer:
                item['producer']=producer
            if producer_run_id:
                item['producer_run_id']=int(producer_run_id)
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

def validate_source_full_body(bb,w,h,action=None,standalone=False):
    left,top,right,bottom=bb
    cw=max(0,right-left); ch=max(0,bottom-top)
    if cw<=0 or ch<=0:
        raise RuntimeError('empty')
    # Cropped head/torso fragments were historically normalized into plausible
    # 256px cells. Reject source crops before resizing can hide the defect.
    edge=max(4,round(h*.018))
    if top <= edge or bottom >= h-edge:
        raise RuntimeError(f'not full body: source edge top={top} bottom={bottom} cell_h={h}')
    min_height=.65 if standalone else (.42 if action=='REPAIR' else .55)
    if ch < h*min_height:
        raise RuntimeError(f'not full body: source short h={ch} cell_h={h} min={min_height:.2f}')
    if action!='REPAIR' and ch<cw*.92:
        raise RuntimeError('not full body: silhouette too wide')
    return True

def safe_source_margin(image):
    """Pad an *already complete* source, never hallucinate missing body parts.

    A fully isolated sprite may have only 8px of empty source margin,
    though both feet are visibly present. Reframe its existing pixels on
    transparent space before imposing conservative full-body constraints.
    If ANY actual alpha touches an edge, fail instead of hiding truncation.
    """
    if image.mode!='RGBA':
        raise ValueError('Expected RGBA source')
    w,h=image.size
    bb=image.getchannel('A').getbbox()
    if not bb:
        raise RuntimeError('empty')
    l,t,r,b=bb
    if min(l,t,w-r,h-b)<4:
        raise RuntimeError('cropped full-body source touches edge')
    soft=max(4,round(h*.018))
    if min(t,h-b)>=soft:
        return image
    pad=round(min(w,h)*.075)
    padded=Image.new('RGBA',(w+2*pad,h+2*pad))
    padded.alpha_composite(image,(pad,pad))
    return padded


def cutout(raw, action=None, standalone=False):
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
    if standalone:
        clean=safe_source_margin(clean)
        w,h=clean.size
    bb=clean.getchannel('A').getbbox()
    if not bb:
        raise RuntimeError('empty')
    crop=clean.crop(bb); cw,ch=crop.size
    validate_source_full_body(bb,w,h,action,standalone)
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

def lower_body_motion(frames):
    vals=[]
    for n in range(1,len(frames)):
        A=frames[n-1].getchannel('A')
        B=frames[n].getchannel('A')
        ba=A.getbbox(); bb=B.getbbox()
        if not ba or not bb:
            continue
        top=max(0,min(ba[1]+int((ba[3]-ba[1])*.55),bb[1]+int((bb[3]-bb[1])*.55)))
        a=A.crop((0,top,256,256)).resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
        b=B.crop((0,top,256,256)).resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
        pa,pb=a.load(),b.load(); inter=union=0
        for y in range(64):
            for x in range(64):
                aa=pa[x,y]>0; bbb=pb[x,y]>0
                inter+=aa and bbb; union+=aa or bbb
        vals.append(1-(inter/union if union else 1))
    return sum(vals)/len(vals) if vals else 0.0

def actionqa(frames,action):
    vals=[iou(frames[n-1],frames[n]) for n in range(1,len(frames))]
    mean_change=(sum(1-x for x in vals)/len(vals)) if vals else 0.0
    if action=='WALK':
        motion=lower_body_motion(frames)
        if motion<.22:
            return False,f'walk-too-static lower-motion={motion:.3f}'
        if mean_change<.12:
            return False,f'walk-too-static mean-change={mean_change:.3f}'
        return True,f'walk-motion={motion:.3f} mean-change={mean_change:.3f}'
    floors={'WORK':.10,'CARRY':.12,'REPAIR':.09,'CELEB':.10,'IDLE':.025}
    floor=floors.get(action,.05)
    if mean_change<floor:
        return False,f'{action.lower()}-too-static mean-change={mean_change:.3f}<{floor:.3f}'
    return True,f'{action.lower()}-motion={mean_change:.3f}'

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
    if sims:
        print('POLLINATIONS_CHR_IDENTITY_SIMS='+','.join(f'{n+1}:{v:.3f}' for n,v in enumerate(sims)),flush=True)
    if sims and min(sims)<.58:
        bad=[n+1 for n,v in enumerate(sims) if v<.58]
        return False,f'identity-palette={min(sims):.2f} frames={",".join(map(str,bad))}'
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
    framing = (
        ' CRITICAL REPAIR FRAMING: every occupied 256x256 cell must show the complete character from helmet/head to both boot soles. '
        'Keep at least 20 pixels of plain neutral-gray empty margin above the head and at least 20 pixels below the lowest boot sole in EVERY occupied cell, plus clear side margins. '
        'Scale the worker smaller inside each cell if necessary. Never let any body part or tool touch a cell edge; never crop head, arms, tool, knees, legs, boots, or feet. '
        'Keep the diagnostic tool compact and beside the torso so it never obscures the legs or extends toward the bottom edge. '
        if action == 'REPAIR' else
        ' CRITICAL WALK FRAMING: every occupied 256x256 cell must show the complete walking character from helmet/head through both boot soles. '
        'Keep at least 18 pixels of plain neutral-gray empty margin above the head and below the lowest boot in EVERY occupied cell, with clear side margins for the forward/back stride. '
        'Scale the worker smaller if needed. Never crop the head, arms, hands, knees, legs, heels, toes, or boots; no limb may touch a cell edge. '
        if action == 'WALK' else ''
    )
    return (
        f'AAA premium mobile 2.5D sprite-sheet production image. SAME EXACT SINGLE ADULT CHARACTER in every frame: {ROLES[item["role"]]}. '
        f'Animation: {ACTIONS[action][0]}. Required chronological poses: {poses}. '
        f'{framing}'
        'Create one exact 4 columns by 4 rows animation atlas on a perfectly flat uniform neutral gray background. '
        'Each cell contains exactly one full-body view of the same worker, same face, same gender presentation, same hair, same helmet, same clothes, same colors, same body proportions, same tool or carried object. '
        '34-degree three-quarter orthographic camera, feet visible, centered in every cell, identical scale and foot pivot. '
        'Use only the first required cells in reading order left-to-right then top-to-bottom; leave unused cells empty neutral gray. '
        'No cell labels, no text, no numbers, no borders, no logos, no extra people, no duplicated limbs, no changing accessories, no changing carried object, no scenery, no floor, no building, no vehicle, no gradient, no vignette.'
    )

def repair_frame_prompt(item, pose):
    return (
        f'AAA premium mobile 2.5D game character animation frame. SAME EXACT SINGLE ADULT CHARACTER identity: {ROLES[item["role"]]}. '
        f'Action frame: repairing with one compact diagnostic tool, pose: {pose}. '
        'One character only, complete full body from helmet/head through both boot soles, centered and slightly small in frame. '
        'At least 12 percent empty neutral-gray margin above head and below boots and clear side margins. '
        '34-degree three-quarter orthographic camera, consistent body proportions, face, hair, helmet, clothing, colors and tool. '
        'Perfectly flat uniform neutral gray background. No floor, no shadow, no scenery, no text, no border, no extra people, '
        'no duplicated limbs, no crop, no body part or tool touching any image edge.'
    )

def walk_frame_prompt(item, pose):
    return (
        f'AAA premium mobile 2.5D game character animation frame. SAME EXACT SINGLE ADULT CHARACTER identity: {ROLES[item["role"]]}. '
        f'Action frame: convincing walk cycle, pose: {pose}. '
        'One character only, complete full body from helmet/head through both boot soles, centered and slightly small in frame. '
        'At least 12 percent empty neutral-gray margin above head and below boots and clear side margins for stride. '
        '34-degree three-quarter orthographic camera, same face, helmet, clothing, colors and body proportions in every frame. '
        'Strong readable alternating leg stride and arm counter-swing appropriate to the requested pose. '
        'Perfectly flat uniform neutral gray background. No floor, no shadow, no scenery, no text, no border, no extra people, '
        'no duplicated limbs, no crop, no body part touching any image edge.'
    )

def generate_walk_frames(item, seed):
    frames=[]
    cache_dir=OUT/'pollinations-frame-cache'/item['id']
    cache_dir.mkdir(parents=True,exist_ok=True)
    for n,pose in enumerate(POSES['WALK'][:ACTIONS['WALK'][1]]):
        cache_file=cache_dir/f'{n:02d}.png'
        if cache_file.is_file():
            frame=Image.open(cache_file).convert('RGBA')
            cov=sum(frame.getchannel('A').histogram()[8:])/(256*256)
            print(f'POLLINATIONS_CHR_WALK_CACHE_HIT n={n} pose={pose} cov={cov:.3f}',flush=True)
        else:
            rev_file=cache_dir/f'{n:02d}.rev'
            try:
                revision=int(rev_file.read_text(encoding='utf-8').strip()) if rev_file.is_file() else 0
            except ValueError:
                revision=0
            frame_seed=(27191 + sum((i+1)*ord(ch) for i,ch in enumerate(item['id']))*1013 + n*104729 + revision*1000003) % 2147483647
            raw=fetch(walk_frame_prompt(item,pose),frame_seed)
            frame,cov=cutout(raw,'WALK',standalone=True)
            frame.save(cache_file,'PNG',optimize=True)
            print(f'POLLINATIONS_CHR_WALK_CACHE_SAVE n={n} pose={pose} revision={revision}',flush=True)
        frames.append(frame)
        print(f'POLLINATIONS_CHR_WALK_FRAME n={n} pose={pose} cov={cov:.3f}',flush=True)
    return frames

def generate_repair_frames(item, seed):
    frames=[]
    cache_dir=OUT/'pollinations-frame-cache'/item['id']
    cache_dir.mkdir(parents=True,exist_ok=True)
    for n,pose in enumerate(POSES['REPAIR'][:ACTIONS['REPAIR'][1]]):
        cache_file=cache_dir/f'{n:02d}.png'
        if cache_file.is_file():
            frame=Image.open(cache_file).convert('RGBA')
            cov=sum(frame.getchannel('A').histogram()[8:])/(256*256)
            print(f'POLLINATIONS_CHR_REPAIR_CACHE_HIT n={n} pose={pose} cov={cov:.3f}',flush=True)
        else:
            rev_file=cache_dir/f'{n:02d}.rev'
            try:
                revision=int(rev_file.read_text(encoding='utf-8').strip()) if rev_file.is_file() else 0
            except ValueError:
                revision=0
            frame_seed=(19417 + sum((i+1)*ord(ch) for i,ch in enumerate(item['id']))*1009 + n*104729 + revision*1000003) % 2147483647
            raw=fetch(repair_frame_prompt(item,pose),frame_seed)
            frame,cov=cutout(raw,'REPAIR',standalone=True)
            frame.save(cache_file,'PNG',optimize=True)
            print(f'POLLINATIONS_CHR_REPAIR_CACHE_SAVE n={n} pose={pose} revision={revision}',flush=True)
        frames.append(frame)
        print(f'POLLINATIONS_CHR_REPAIR_FRAME n={n} pose={pose} cov={cov:.3f}',flush=True)
    return frames

# Explicit immutable appearance descriptors for independent remote requests.
# Opaque face protection deliberately reduces identity drift between poses.
ROLE_IDENTITY_ANCHORS={
    'OP':'One orange hard hat, black face mask, charcoal work shirt and rust-orange bib overalls, black gloves and black work boots.',
    'TECH':'One matte graphite helmet with cyan visor, dark graphite mechanic coveralls, cyan trim on both cuffs, black gloves and black boots.',
    'LOG':'One matte charcoal helmet with dark visor, amber-orange sleeveless safety vest with two white reflective stripes, charcoal jacket, charcoal trousers, black cargo gloves, brown safety boots.',
    'ENG':'One teal helmet with opaque teal safety visor, clean deep-blue technical coat, one silver chest badge, dark-teal trousers, black gloves and dark boots.',
}


def independent_frame_prompt(item,pose):
    """Explicitly request ONE complete subject, never a sheet or sprite atlas."""
    action=item['action']
    props={
        'IDLE':'hands relaxed and no tool or crate',
        'WORK':'one small industrial tool gripped by the same visible hand while interacting with a compact work point',
        'CARRY':'CARRYING a large unmistakable rectangular orange cargo crate centered over the waist; BOTH gloved hands grasp the LEFT and RIGHT external handles, arms bent around the same crate, the box occludes part of the stomach; never empty handed',
        'CELEB':'one open, expressive arm-raised cheer with no tool or carried object',
    }
    if action not in props:
        raise ValueError('Use specialized walking/repair prompt')
    return (
        f'ONE single standalone game character animation frame, NOT a sprite sheet, '
        f'NOT a collage and NOT a character reference board. '
        f'Professional painterly 2.5D premium mobile game character: '
        f'{ROLES[item["role"]]}. '
        f'IMMUTABLE CHARACTER LOOK: {ROLE_IDENTITY_ANCHORS[item["role"]]} '
        f'Action: {ACTIONS[action][0]}, pose: {pose}. '
        f'{props[action]}. '
        'Exactly ONE human, fully visible head to toe including BOTH boots, '
        'one consistent adult identity, same face, one helmet, same clothes and '
        'same proportions in every frame. Fixed 34-degree three-quarter camera, '
        'full body standing centered inside a plain neutral gray 1024x1024 canvas '
        'with at least 12 percent empty space above head and below both feet. '
        'All limbs and tools entirely within the margins. One pose only, '
        'NO multiple people, NO detached body parts, NO close-up portrait, '
        'NO head shot, NO duplicated characters, NO panels, NO grid, '
        'NO text, NO labels, NO numbers, NO logos, NO watermark, '
        'NO gradient, NO floor and NO scene.'
    )


def require_standalone_body(frame):
    """Do not cache obvious portrait/torso fragments as valid whole-body poses.

    Risk screening only: cannot detect missing props or grant semantic approval.
    """
    geometry=frame_geometry(frame)
    bad=set(geometry.get('risk_flags',[])) & {
        'NOT_TALL_FULL_BODY_SILHOUETTE',
        'PORTRAIT_OR_SOLID_TORSO_RISK',
        'EMPTY_VISIBLE_FRAME',
    }
    if geometry.get('bbox_height_fraction',0)<.45:
        bad.add('CHARACTER_TOO_SMALL_FOR_CELL')
    if bad:
        raise RuntimeError('standalone-fragment: '+','.join(sorted(bad)))
    return geometry


def generate_independent_frames(item,seed):
    """Produce each pose separately; never split one tall image into limbs."""
    action=item['action']
    if action not in {'IDLE','WORK','CARRY','CELEB'}:
        raise ValueError('Unsupported generic per-frame action')
    frames=[]
    cache_dir=OUT/'pollinations-frame-cache'/item['id']/STANDALONE_CACHE_EPOCH
    cache_dir.mkdir(parents=True,exist_ok=True)
    for n,pose in enumerate(POSES[action][:ACTIONS[action][1]]):
        cache_file=cache_dir/f'{n:02d}.png'
        if cache_file.is_file():
            frame=Image.open(cache_file).convert('RGBA')
            try:
                require_standalone_body(frame)
            except RuntimeError as exc:
                # Old v3 caches can still contain cropped torsos. Never
                # trust them on restart or retry the exact same bad seed.
                cache_file.unlink()
                rev_file=cache_dir/f'{n:02d}.rev'
                try:
                    current=int(rev_file.read_text(encoding='utf-8')) if rev_file.is_file() else 0
                except ValueError:
                    current=0
                rev_file.write_text(str(current+1),encoding='utf-8')
                print(f'POLLINATIONS_CHR_CACHE_REJECT n={n} reason={exc}',flush=True)
            else:
                cov=sum(frame.getchannel('A').histogram()[8:])/(256*256)
                print(f'POLLINATIONS_CHR_FRAME_CACHE_HIT action={action} n={n}',flush=True)
        if not cache_file.is_file():
            rev_file=cache_dir/f'{n:02d}.rev'
            try:
                revision=int(rev_file.read_text(encoding='utf-8').strip()) if rev_file.is_file() else 0
            except ValueError:
                revision=0
            frame_seed=(seed+sum((i+1)*ord(ch) for i,ch in enumerate(item['id']))*1009+
                        n*104729+revision*1000003)%2147483647
            raw=fetch(independent_frame_prompt(item,pose),frame_seed)
            frame,cov=cutout(raw,action,standalone=True)
            require_standalone_body(frame)
            frame.save(cache_file,'PNG',optimize=True)
            print(f'POLLINATIONS_CHR_FRAME_CACHE_SAVE action={action} n={n} '
                  f'revision={revision}',flush=True)
        frames.append(frame)
        print(f'POLLINATIONS_CHR_FRAME action={action} n={n} cov={cov:.3f}',flush=True)
    return frames


def extract_frames(raw,frame_count,action=None):
    if raw.size!=(1024,1024):
        raw=raw.resize((1024,1024),Image.Resampling.LANCZOS)
    frames=[]
    for n in range(frame_count):
        x=(n%4)*256; y=(n//4)*256
        cell_raw=raw.crop((x,y,x+256,y+256))
        frame,cov=cutout(cell_raw, action)
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
            screen=None
            try:
                if it['action'] == 'REPAIR':
                    frames=generate_repair_frames(it,seed)
                elif it['action'] == 'WALK':
                    frames=generate_walk_frames(it,seed)
                else:
                    frames=generate_independent_frames(it,seed)
                # The atlas may be formed ONLY after each standalone frame
                # passes full-body risk screening and continuity checks.
                screen=clip_risk(frames)
                if screen['risk_level']=='BLOCKING':
                    raise RuntimeError('semantic-risk: '+','.join(screen['flags']))
                ok,why=sheetqa(frames)
                if not ok:
                    raise RuntimeError(why)
                action_ok,action_why=actionqa(frames,it['action'])
                if not action_ok:
                    raise RuntimeError(action_why)
                why=f'{why} {action_why}'
                sheet=Image.new('RGBA',(1024,1024),(0,0,0,0))
                for n,frame in enumerate(frames):
                    sheet.alpha_composite(frame,((n%4)*256,(n//4)*256))
                p=candidate_destination(it)
                p.parent.mkdir(parents=True,exist_ok=True)
                canonical=INCOMING/f"{it['stem']}.png"
                original_sha256=(
                    hashlib.sha256(canonical.read_bytes()).hexdigest()
                    if canonical.is_file() else None)
                sheet.save(p,'PNG',optimize=True)
                producer_run_id=os.getenv('GITHUB_RUN_ID') or None
                mark_queue(it['id'],'CANDIDATE',seed,'pollinations-character-atlas',producer_run_id)
                rep.append({'id':it['id'],'status':'CANDIDATE','file':p.name,'frames':fc,
                            'qa':why,'semantic_risk':screen,'semantic_approved':False,
                            'candidate_path':p.relative_to(ROOT).as_posix(),
                            'historical_candidate_sha256':original_sha256,
                            'staged_for_manual_review':p!=canonical,
                            'generation':'individual-full-body-frames-v3',
                            'producer':'pollinations-character-atlas',
                            'producer_run_id':int(producer_run_id) if producer_run_id else None})
                print(f"POLLINATIONS_CHR_VALIDATED={it['id']} {why}",flush=True)
                done=True
                break
            except Exception as e:
                last=str(e)
                # Never retry the same known-bad cached pixels. A producer
                # outage mid-sequence is different: retain the valid prefix.
                bad_frames=[]
                if last.startswith('identity-palette=') and ' frames=' in last:
                    try:
                        bad_frames=[int(x) for x in last.rsplit(' frames=',1)[1].split(',') if x.strip()]
                    except ValueError:
                        pass
                elif last.startswith('semantic-risk:') and screen is not None:
                    bad_frames=[i for i,entry in enumerate(screen.get('frames',[]))
                                if entry.get('risk_flags')]
                    if not bad_frames:
                        bad_frames=list(range(1,fc))
                elif last.startswith(('iou=','pivot','drift','duplicate',
                                      'walk-too-static','carry-too-static',
                                      'work-too-static','repair-too-static',
                                      'celeb-too-static','idle-too-static')):
                    bad_frames=list(range(1,fc))
                if bad_frames:
                    try:
                        for bad in sorted(set(bad_frames)):
                            cache_dir=OUT/'pollinations-frame-cache'/it['id']
                            if it['action'] in {'IDLE','WORK','CARRY','CELEB'}:
                                cache_dir=cache_dir/STANDALONE_CACHE_EPOCH
                            cache_file=cache_dir/f'{bad:02d}.png'
                            if cache_file.is_file():
                                cache_file.unlink()
                            rev_file=cache_file.with_suffix('.rev')
                            try:
                                revision=int(rev_file.read_text(encoding='utf-8').strip())+1 if rev_file.is_file() else 1
                            except ValueError:
                                revision=1
                            rev_file.write_text(str(revision),encoding='utf-8')
                            print(f'POLLINATIONS_CHR_{it["action"]}_CACHE_INVALIDATE n={bad} revision={revision} reason=identity-palette',flush=True)
                    except (ValueError,OSError):
                        pass
                print(f"POLLINATIONS_CHR_RETRY={it['id']} attempt={att+1} reason={e}",flush=True)

        if not done:
            provider_error = (
                'pollinations request exhausted retries:' in last
                or 'HTTP Error 402:' in last
                or 'HTTP Error 429:' in last
                or 'HTTP Error 500:' in last
                or 'HTTP Error 502:' in last
                or 'HTTP Error 503:' in last
            )
            mark_queue(it['id'],'PROVIDER_ERROR' if provider_error else 'BLOCKED')
            rep.append({
                'id':it['id'],
                'status':'PROVIDER_ERROR' if provider_error else 'REJECT',
                'reason':last,
                'generation':'individual-full-body-frames-v2'
            })

    (OUT/'pollinations-character-summary.json').write_text(json.dumps(rep,indent=2),encoding='utf-8')
    print('POLLINATIONS_CHR_CANDIDATES='+str(sum(x['status']=='CANDIDATE' for x in rep)),flush=True)

if __name__=='__main__':
    main()
