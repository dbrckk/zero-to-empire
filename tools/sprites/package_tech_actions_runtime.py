#!/usr/bin/env python3
"""Package six TECH animation candidates as pivot-stable preview atlases.

This is a staging/export step. It NEVER alters canonical queues or approves art.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ACTIONS=('WALK','CARRY','IDLE','WORK','REPAIR','CELEB')
SIDE=512
SIZES=(128,256)


def sha(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ensure(ok:bool,message:str)->None:
    if not ok: raise ValueError(message)


def verify(root:Path):
    index=json.loads((root/'production-index.json').read_text(encoding='utf-8'))
    ensure(index.get('format')=='zte-modular-actions-v3','Wrong source index')
    ensure(index.get('review_required') is True and index.get('strict_status')=='NEEDS_REVIEW',
           'Source review gate missing')
    items=index.get('actions',[])
    ensure(len(items)==6 and set(x.get('action') for x in items)==set(ACTIONS),'Six unique actions required')
    by_action={x['action']:x for x in items}
    shared=index['source_skin_sha256']
    validated={}
    for action in ACTIONS:
        asset='CHR-TECH-'+action
        record=by_action[action]
        ensure(record.get('asset_id')==asset and record.get('strict_status')=='NEEDS_REVIEW',
               'Source asset status invalid: '+action)
        ensure(record.get('technical_pass') is True and record.get('source_skin_sha256')==shared,
               'Source candidate QA/skin mismatch: '+action)
        folder=root/action
        m=json.loads((folder/'qa-manifest.json').read_text(encoding='utf-8'))
        qa=m['qa']
        ensure(m.get('asset_id')==asset and m.get('source_skin_sha256')==shared,
               'Manifest identity mismatch: '+action)
        ensure(m.get('strict_status')=='NEEDS_REVIEW' and m.get('human_visual_review_required') is True,
               'Manifest review gate missing: '+action)
        ensure(qa.get('technical_pass') is True and qa.get('visual_review_pass') is False and
               qa.get('semantic_review_pass') is False,'QA gate invalid: '+action)
        ensure(m.get('frame_size')==[SIDE,SIDE] and m.get('pivot')=={'x':252,'y':449},
               'Unexpected frame coordinate system: '+action)
        count=int(m['frames']); fps=int(m['fps'])
        ensure(8<=count<=64 and count%2==0 and 3<=fps<=24,'Invalid timing: '+action)
        ensure((folder/'REVIEW_REQUIRED.txt').is_file(),'Missing review marker: '+action)
        poses=json.loads((folder/'frame-poses.json').read_text(encoding='utf-8'))
        events=json.loads((folder/'footstep-events.json').read_text(encoding='utf-8'))
        ensure(len(poses)==count and len(events)==count,'Pose/event count mismatch: '+action)
        frames=sorted((folder/'frames').glob('*.png'))
        ensure(len(frames)==count and all(f.name==f'{asset}-{i:02d}.png' for i,f in enumerate(frames)),
               'Missing/extra/misordered frames: '+action)
        validated[action]={'frames':frames,'fps':fps,'count':count,'events':events,'poses':poses}
    return index,validated


def review_html(data:dict)->str:
    sources=json.dumps({name:{'src':a['variants']['128']['path'],
                'shadow_src':a['optional_shadow_layer']['variants']['128']['path'],'frames':a['frames'],
                'cols':a['columns'],'fps':a['fps']} for name,a in data['animations'].items()})
    template='''<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>TECH · Six actions — REVIEW ONLY</title><style>
:root{color-scheme:dark}*{box-sizing:border-box}body{background:#101824;color:#e2edf7;font:14px system-ui,sans-serif;margin:0;padding:20px}
h1{font-size:22px}.warn{color:#f8d18b}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}
article{background:#1c2939;border:1px solid #36465a;border-radius:12px;padding:12px}
header{display:flex;justify-content:space-between;margin-bottom:8px}
canvas{width:100%;background:repeating-conic-gradient(#263444 0 25%,#314459 0 50%) 0 0/28px 28px;border-radius:8px}
select{background:#172538;color:inherit;padding:5px}footer{color:#97abc1;margin-top:18px}
</style></head><body><h1>TECH · six animations</h1>
<p class="warn">Candidats non validés — revue visuelle obligatoire, aucun strict DONE.</p>
<label>Vitesse <select id="speed"><option value=".5">0,5×</option><option selected value="1">1×</option>
<option value="1.5">1,5×</option><option value="2">2×</option></select></label>
<div class="grid" id="grid"></div><footer>Prévisualisation seulement. Aucune modification du jeu ou de la file de production.</footer>
<script>const animations=__SOURCES__,nodes=[],grid=document.querySelector('#grid');
for(const [name,c] of Object.entries(animations)){
const card=document.createElement('article'),h=document.createElement('header');
const title=document.createElement('strong');title.textContent=name;
const count=document.createElement('span');count.textContent=c.frames+' frames';h.append(title,count);
const canvas=document.createElement('canvas');canvas.width=256;canvas.height=256;
const img=new Image();img.onload=()=>c.ready=true;img.src=c.src;
const shadow=new Image();shadow.onload=()=>c.shadowReady=true;shadow.src=c.shadow_src;
card.append(h,canvas);grid.append(card);nodes.push({c,img,shadow,ctx:canvas.getContext('2d')});}
const begin=performance.now();
function draw(t){const speed=Number(document.querySelector('#speed').value);
for(const {c,img,shadow,ctx} of nodes){ctx.clearRect(0,0,256,256);if(!c.ready)continue;
const frame=Math.floor((t-begin)*c.fps*speed/1000)%c.frames;
if(c.shadowReady)ctx.drawImage(shadow,(frame%c.cols)*128,Math.floor(frame/c.cols)*128,128,128,0,0,256,256);
ctx.drawImage(img,(frame%c.cols)*128,Math.floor(frame/c.cols)*128,128,128,0,0,256,256);}
requestAnimationFrame(draw)}requestAnimationFrame(draw);</script></body></html>'''
    return template.replace('__SOURCES__',sources)


def render_contact_shadow(p:dict)->Image.Image:
    """Optional frame-aligned ground-shadow atlas, isolated from character pixels."""
    layer=Image.new('RGBA',(SIDE,SIDE))
    for side,contact in [('left','lockL'),('right','lockR')]:
        x,y=p[side]
        locked=p.get(contact,False)
        height=max(0,449-y)
        strength=100 if locked else max(18,round(62-height*.65))
        radius=34 if locked else max(20,round(30-height*.13))
        mask=Image.new('RGBA',(SIDE,SIDE))
        ImageDraw.Draw(mask,'RGBA').ellipse(
            (round(x-radius),448,round(x+radius),469),fill=(7,16,26,strength))
        layer=Image.alpha_composite(layer,mask.filter(ImageFilter.GaussianBlur(4)))
    return layer



def game_scale_metrics(frame:Image.Image, side:int=96)->dict:
    """Objective 96px silhouette sanity check, NOT an artistic approval."""
    tiny=frame.resize((side,side),Image.Resampling.LANCZOS)
    alpha=tiny.getchannel('A')
    opaque=sum(alpha.histogram()[128:])
    binary=alpha.point(lambda v: 255 if v>=128 else 0)
    bbox=binary.getbbox()
    if bbox is None:
        return {'opaque_pixels':0,'bounds':None,'min_edge_margin':0,
                'silhouette_width':0,'silhouette_height':0,'pass':False}
    x0,y0,x1,y1=bbox
    margin=min(x0,y0,side-x1,side-y1)
    return {'opaque_pixels':opaque,'bounds':[x0,y0,x1,y1],
            'min_edge_margin':margin,'silhouette_width':x1-x0,
            'silhouette_height':y1-y0,
            'pass':bool(opaque>=500 and x1-x0>=20 and y1-y0>=56 and margin>=3)}


def package(source:Path,output:Path)->dict:
    index,records=verify(source)
    output.mkdir(parents=True,exist_ok=True)
    exported={'format':'zte-tech-actions-runtime-v1','strict_status':'NEEDS_REVIEW',
              'visual_review_pass':False,'semantic_review_pass':False,
              'review_required':True,'approved_for_release':False,'integrated_into_game':False,
              'reference_canvas_px':SIDE,'source_skin_sha256':index['source_skin_sha256'],
              'animations':{}}
    overview=Image.new('RGB',(900,672),(23,29,40))
    draw=ImageDraw.Draw(overview)
    contact96=Image.new('RGB',(120+96*8,40+108*6),(25,33,45))
    contact_draw=ImageDraw.Draw(contact96)
    contact_draw.text((120,12),'1       4       7      10      13      16      19      22  / 24',fill=(190,208,224))
    for idx,action in enumerate(ACTIONS):
        rec=records[action]; count=rec['count'];cols=6;rows=math.ceil(count/cols)
        pics=[];bounds=[];game_scale=[]
        for path in rec['frames']:
            with Image.open(path) as image:
                ensure(image.size==(SIDE,SIDE) and image.mode=='RGBA','Source not 512px RGBA: '+str(path))
                frame=image.copy()
            alpha=frame.getchannel('A')
            b=alpha.point(lambda px:255 if px>=128 else 0).getbbox()
            ensure(b is not None and b[0]>=6 and b[1]>=6 and b[2]<=SIDE-6 and b[3]<=SIDE-6,
                   'Frame empty/clipped: '+str(path))
            ensure(alpha.getpixel((0,0))==0,'Missing transparent corner: '+str(path))
            pics.append(frame);bounds.append(b)
            game_scale.append(game_scale_metrics(frame))
        ensure(all(metric['pass'] for metric in game_scale),
               '96px game-scale silhouette collapsed/clipped: '+action)
        contact_draw.text((10,36+idx*108+42),action,fill=(218,234,245))
        for j in range(8):
            img=pics[(j*count)//8].resize((96,96),Image.Resampling.LANCZOS)
            contact96.paste(img,(120+j*96,36+idx*108),img.getchannel('A'))
        variants={};shadow_variants={}
        shadow_frames=[render_contact_shadow(p) for p in rec['poses']]
        for size in SIZES:
            folder=output/'atlases';folder.mkdir(exist_ok=True)
            atlas=Image.new('RGBA',(size*cols,size*rows))
            for i,im in enumerate(pics):
                scaled=im.resize((size,size),Image.Resampling.LANCZOS)
                atlas.alpha_composite(scaled,((i%cols)*size,(i//cols)*size))
            path=folder/f'{action.lower()}-{size}.png'
            atlas.save(path,optimize=True)
            shadow_atlas=Image.new('RGBA',(size*cols,size*rows))
            for i,shadow in enumerate(shadow_frames):
                shadow_atlas.alpha_composite(shadow.resize((size,size),Image.Resampling.LANCZOS),
                                             ((i%cols)*size,(i//cols)*size))
            shadow_path=folder/f'{action.lower()}-shadow-{size}.png'
            shadow_atlas.save(shadow_path,optimize=True)
            shadow_variants[str(size)]={'path':shadow_path.relative_to(output).as_posix(),
                'sha256':sha(shadow_path),'atlas_size':[size*cols,size*rows]}
            variants[str(size)]={'path':path.relative_to(output).as_posix(),'sha256':sha(path),
                'sprite_size':[size,size],'atlas_size':[size*cols,size*rows],
                'pivot_px':[round(252*size/SIDE,3),round(449*size/SIDE,3)]}
        xx=450*(idx%2);yy=224*(idx//2)
        icon=pics[0].resize((190,190),Image.Resampling.LANCZOS)
        overview.paste(icon,(xx+112,yy+30),icon.getchannel('A'))
        draw.text((xx+18,yy+10),action,fill=(218,232,243))
        draw.text((xx+18,yy+200),f'{count} frames / {rec["fps"]} FPS',fill=(162,184,202))
        union=[min(b[0] for b in bounds),min(b[1] for b in bounds),
               max(b[2] for b in bounds),max(b[3] for b in bounds)]
        events_dir=output/'events';events_dir.mkdir(exist_ok=True)
        events_file=events_dir/f'{action.lower()}.json'
        events_file.write_text(json.dumps(rec['events'],indent=2),encoding='utf-8')
        exported['animations'][action]={'asset_id':'CHR-TECH-'+action,'frames':count,
            'fps':rec['fps'],'loop':True,'columns':cols,'rows':rows,
            'frame_rect_order':'row-major','reference_pivot_px':[252,449],
            'visual_union_bounds_px':union,'per_frame_visual_bounds_px':[list(b) for b in bounds],
            'game_scale_96px_technical_pass':all(metric['pass'] for metric in game_scale),
            'game_scale_96px_metrics':game_scale,
            'collision_boxes_status':'NOT_DEFINED_REQUIRES_GAMEPLAY_REVIEW',
            'events_file':events_file.relative_to(output).as_posix(),
            'optional_shadow_layer':{'default_enabled':False,'variants':shadow_variants},
            'variants':variants,'strict_status':'NEEDS_REVIEW','review_required':True}
    overview.save(output/'game-scale-overview.jpg',quality=93)
    contact96.save(output/'review-all-actions-96.png',optimize=True)
    (output/'runtime-manifest.json').write_text(json.dumps(exported,indent=2),encoding='utf-8')
    (output/'REVIEW_REQUIRED.txt').write_text(
        'Review-only animated candidates; no strict DONE and no final game assets.\n',
        encoding='utf-8')
    (output/'review-player.html').write_text(review_html(exported),encoding='utf-8')
    return exported


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,default=Path('build/tech-actions-v3'))
    parser.add_argument('--output',type=Path,default=Path('build/tech-actions-runtime-review'))
    args=parser.parse_args()
    result=package(args.source,args.output)
    print(json.dumps({'animations':list(result['animations']),
        'total_frames':sum(a['frames'] for a in result['animations'].values()),
        'strict_status':result['strict_status'],'output':str(args.output)},indent=2))


if __name__=='__main__':main()
