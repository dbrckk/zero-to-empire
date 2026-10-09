#!/usr/bin/env python3
"""Audit real rendered TECH animation frames at gameplay scale.

Objective regression signals only, NEVER artistic or semantic approval.
No canonical queue mutations; strict DONE is expressly forbidden.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import math
import statistics
from pathlib import Path
from PIL import Image, ImageDraw
import numpy as np

ACTIONS=('WALK','CARRY','IDLE','WORK','REPAIR','CELEB')
SIDE=96


def inspect_clip(root:Path,action:str,frames_expected:int=24) -> dict:
    directory=root/action
    manifest=json.loads((directory/'qa-manifest.json').read_text(encoding='utf-8'))
    if manifest.get('strict_status')!='NEEDS_REVIEW' or manifest.get('human_visual_review_required') is not True:
        raise ValueError('Review gate missing: '+action)
    qa=manifest.get('qa',{})
    if qa.get('visual_review_pass') is not False or qa.get('semantic_review_pass') is not False:
        raise ValueError('Premature visual/semantic approval: '+action)
    if manifest.get('asset_id')!='CHR-TECH-'+action:
        raise ValueError('Wrong asset: '+action)
    frames=[directory/'frames'/f'CHR-TECH-{action}-{i:02d}.png' for i in range(frames_expected)]
    extra=list((directory/'frames').glob('*.png'))
    if len(extra)!=frames_expected or not all(f.is_file() for f in frames):
        raise ValueError('Missing, unordered or extra frames: '+action)
    masks=[];areas=[];bbox=[];digests=[];rgba_frames=[]
    for i,path in enumerate(frames):
        with Image.open(path) as source:
            if source.mode!='RGBA' or source.size!=(512,512):
                raise ValueError(f'Unexpected frame format: {action}:{i}')
            img=source.resize((SIDE,SIDE),Image.Resampling.LANCZOS)
            rgba=np.asarray(img.convert('RGBA'),dtype=np.uint8)
            alpha=rgba[:,:,3]
            original_bounds=source.getchannel('A').getbbox()
            if original_bounds is None:
                raise ValueError(f'Empty silhouette: {action}:{i}')
            if min(original_bounds[0],original_bounds[1],512-original_bounds[2],512-original_bounds[3])<5:
                raise ValueError(f'Clipped frame: {action}:{i}')
            digests.append(hashlib.sha256(source.tobytes()).hexdigest())
        mask=alpha>=128
        yy,xx=np.nonzero(mask)
        if len(xx)==0:
            raise ValueError(f'Empty silhouette: {action}:{i}')
        b=(int(xx.min()),int(yy.min()),int(xx.max()+1),int(yy.max()+1))
        if min(b[0],b[1],SIDE-b[2],SIDE-b[3])<2:
            raise ValueError(f'Clipped 96px sprite: {action}:{i}')
        masks.append(mask)
        rgba_frames.append(rgba)
        areas.append(int(mask.sum()))
        bbox.append(list(b))
    ordered_digest=hashlib.sha256(''.join(digests).encode('ascii')).hexdigest()
    if len(set(digests))<int(math.ceil(frames_expected*.8)):
        raise ValueError('Excessive duplicate frames: '+action)
    differences=[];area_jump=[];color_jumps=[]
    for i,a in enumerate(masks):
        j=(i+1)%frames_expected
        b=masks[j]
        union=int(np.count_nonzero(a|b))
        diff=float(np.count_nonzero(a^b)/union) if union else 1.0
        differences.append(diff)
        area_jump.append(abs(areas[i]-areas[j])/max(areas[i],areas[j],1))
        # Robust chromatic continuity across the overlapping opaque interior.
        # This distinguishes a texture/color flash from legitimate pose motion,
        # and ignores detached transparent VFX/background pixels.
        stable=(rgba_frames[i][:,:,3]>=220)&(rgba_frames[j][:,:,3]>=220)
        if np.count_nonzero(stable)<200:
            raise ValueError('Too little stable character overlap: '+action)
        rgb_a=rgba_frames[i][:,:,:3].astype(np.int16)
        rgb_b=rgba_frames[j][:,:,:3].astype(np.int16)
        changed=np.mean(np.abs(rgb_a-rgb_b),axis=2)[stable]
        color_jumps.append(float(np.median(changed)))
    median=statistics.median(differences)
    if median<.002:
        raise ValueError('Near-static or duplicated animation: '+action)
    seam_ratio=differences[-1]/median
    max_ratio=max(differences)/median
    color_baseline=statistics.median(color_jumps)
    max_color_jump=max(color_jumps)
    # Empirically calibrated on the six source clips at 96px; genuine
    # intentional tiny glow changes affect a minority of stable pixels.
    rgb_limit=max(42.,color_baseline*6.+15.)
    problems=[]
    if seam_ratio>2.5:problems.append('discontinuous-loop-seam')
    if max_ratio>4.5:problems.append('isolated-silhouette-jump')
    if max(area_jump)>.20:problems.append('sudden-alpha-area-change')
    if max_color_jump>rgb_limit:problems.append('global-rgb-flash-or-texture-drift')
    if problems:
        raise ValueError(f'Temporal QA failed {action}: {", ".join(problems)}')
    return {'asset_id':manifest['asset_id'],'frames':frames_expected,
            'unique_frame_count':len(set(digests)),
            'ordered_frame_digest_sha256':ordered_digest,
            'source_skin_sha256':manifest['source_skin_sha256'],
            'alpha_opaque_pixel_range_96px':[min(areas),max(areas)],
            'frame_bounds_96px':bbox,
            'median_transition_disagreement':round(median,5),
            'max_transition_disagreement':round(max(differences),5),
            'loop_seam_disagreement':round(differences[-1],5),
            'loop_seam_ratio':round(seam_ratio,4),
            'largest_motion_spike_ratio':round(max_ratio,4),
            'largest_alpha_area_jump':round(max(area_jump),4),
            'median_opaque_rgb_change':round(color_baseline,3),
            'largest_opaque_rgb_change':round(max_color_jump,3),
            'opaque_rgb_flash_threshold':round(rgb_limit,3),
            'per_transition_opaque_rgb_change':[round(v,3) for v in color_jumps],
            'per_transition_disagreement':[round(v,5) for v in differences],
            'temporal_technical_pass':True,
            'visual_review_pass':False,'semantic_review_pass':False,
            'strict_status':'NEEDS_REVIEW'}


def audit(root:Path,output:Path,skin:Path|None=None)->dict:
    index=json.loads((root/'production-index.json').read_text(encoding='utf-8'))
    if index.get('strict_status')!='NEEDS_REVIEW' or index.get('review_required') is not True:
        raise ValueError('Master review-only index gate missing')
    items=index.get('actions',[])
    if len(items)!=6 or {r.get('action') for r in items}!=set(ACTIONS):
        raise ValueError('Six distinct TECH animations required')
    frames={}
    for a in ACTIONS:
        m=json.loads((root/a/'qa-manifest.json').read_text())
        frames[a]=int(m['frames'])
        if frames[a]<8 or frames[a]>64 or frames[a]%2:
            raise ValueError('Invalid frame count '+a)
    results={a:inspect_clip(root,a,frames[a]) for a in ACTIONS}
    source_hashes={r['source_skin_sha256'] for r in results.values()}
    if len(source_hashes)!=1 or index.get('source_skin_sha256') not in source_hashes:
        raise ValueError('Character identity source hash mismatch')
    if skin is not None:
        if not skin.is_file():
            raise FileNotFoundError('Source skin missing: '+str(skin))
        actual=hashlib.sha256(skin.read_bytes()).hexdigest()
        if actual!=next(iter(source_hashes)):
            raise ValueError('Actual skin atlas SHA-256 mismatch')
    report={'format':'zte-temporal-qa-v1','strict_status':'NEEDS_REVIEW',
            'review_required':True,'visual_review_pass':False,
            'semantic_review_pass':False,'technical_pass':True,
            'source_skin_sha256':next(iter(source_hashes)),'actions':results,
            'limitations':['Silhouette metrics do not certify AAA quality',
                'No automatic visual or semantic approval',
                'Foot contact and props require gameplay review']}
    output.mkdir(parents=True,exist_ok=True)
    (output/'temporal-qa.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    with (output/'frame-transition-metrics.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerow(['action','from_frame','to_frame','silhouette_disagreement'])
        for a in ACTIONS:
            vals=results[a]['per_transition_disagreement']
            for i,v in enumerate(vals):writer.writerow([a,i,(i+1)%len(vals),v])
    image=Image.new('RGB',(1160,80+len(ACTIONS)*102),(23,31,43))
    d=ImageDraw.Draw(image)
    d.text((20,17),'TECH temporal QA — 96px silhouette transitions (REVIEW ONLY)',fill=(222,237,247))
    for index,a in enumerate(ACTIONS):
        y=67+index*102
        info=results[a]
        vals=info['per_transition_disagreement']
        maximum=max(.16,max(vals)*1.12)
        d.text((24,y+25),a,fill=(228,235,245))
        for i,v in enumerate(vals):
            x=130+i*41
            h=max(2,round((v/maximum)*67))
            d.rectangle((x,y+70-h,x+29,y+70),
                        fill=(67,190,220) if i<len(vals)-1 else (240,182,91))
        d.text((130,y+78),'seam / median: '+str(info['loop_seam_ratio']),fill=(159,176,192))
    image.save(output/'motion-timeline.png',optimize=True)
    (output/'REVIEW_REQUIRED.txt').write_text(
        'TECHNICAL AUDIT ONLY. Strict DONE and visual approval prohibited.\n')
    return report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,default=Path('build/tech-actions-v3'))
    parser.add_argument('--output',type=Path,default=Path('build/tech-temporal-review'))
    parser.add_argument('--skin',type=Path,default=None,help='Verify actual source texture hash')
    args=parser.parse_args()
    report=audit(args.source,args.output,args.skin)
    print(json.dumps({'technical_pass':report['technical_pass'],
           'strict_status':report['strict_status'],
           'actions':{a:dict(seam_ratio=r['loop_seam_ratio'],
                             max_jump=r['largest_motion_spike_ratio'])
                      for a,r in report['actions'].items()}},indent=2))

if __name__=='__main__':main()
