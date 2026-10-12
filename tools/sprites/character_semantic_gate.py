"""Image-only risk screening for full-body character animation candidates.

This detects obvious portrait/fragments and palette identity jumps, not artistry.
Even zero detected risks NEVER implies semantic or human visual approval.
"""
from __future__ import annotations

import math
import statistics
from PIL import Image


def _runs(occupancy):
    count=0; active=False
    for value in occupancy:
        if value and not active:
            count+=1
        active=value
    return count


def frame_geometry(frame:Image.Image)->dict:
    if frame.width!=frame.height or frame.width<48:
        raise ValueError('Expected square sprite-cell frame')
    rgba=frame.convert('RGBA')
    alpha=rgba.getchannel('A')
    opaque=alpha.point(lambda a:255 if a>=64 else 0)
    bounds=opaque.getbbox()
    if bounds is None:
        return {'valid':False,'risk_flags':['EMPTY_VISIBLE_FRAME']}
    left,top,right,bottom=bounds
    width=right-left; height=bottom-top
    pixels=opaque.load()
    y0=bottom-max(3,round(height*.18))
    band_h=bottom-y0
    occupancy=[
        sum(pixels[x,y]>=128 for y in range(y0,bottom))
        >=max(2,math.ceil(band_h*.22))
        for x in range(left,right)
    ]
    for i in range(1,len(occupancy)-2):
        if occupancy[i-1] and occupancy[i+2] and not occupancy[i] and not occupancy[i+1]:
            occupancy[i]=occupancy[i+1]=True
    runs=_runs(occupancy)
    opaque_area=sum(pixels[x,y]>=128 for y in range(top,bottom)
                    for x in range(left,right))
    ratio=height/max(width,1)
    fill=opaque_area/max(width*height,1)
    flags=[]
    if ratio<1.30:
        flags.append('NOT_TALL_FULL_BODY_SILHOUETTE')
    if fill>.69 and ratio<1.8:
        flags.append('PORTRAIT_OR_SOLID_TORSO_RISK')
    if runs<2:
        flags.append('FEET_SEPARATION_NOT_EVIDENT')
    return {'valid':True,'bbox':[left,top,right,bottom],
            'aspect_ratio':round(ratio,4),
            'bbox_height_fraction':round(height/frame.height,4),
            'alpha_fill_ratio':round(fill,4),
            'visible_alpha_area':opaque_area,
            'bottom_segment_count':runs,'risk_flags':flags}


def color_signature(frame:Image.Image):
    rgba=frame.convert('RGBA')
    hist=[[0]*8 for _ in range(3)]
    count=0
    for r,g,b,a in rgba.getdata():
        if a<128:
            continue
        count+=1
        for channel,value in enumerate((r,g,b)):
            hist[channel][min(value//32,7)]+=1
    if count<20:
        raise ValueError('Too few opaque pixels')
    return tuple(tuple(value/count for value in ch) for ch in hist)


def palette_distance(a,b)->float:
    return sum(sum(abs(v-w) for v,w in zip(aa,bb))/2
               for aa,bb in zip(a,b))/3


def idle_visual_activity(frames:list[Image.Image])->float:
    """Measure subtle blink/breathing changes without requiring body motion.

    Silhouette-only alpha overlap falsely rejects excellent six-frame IDLE
    animations with a fixed body and tiny facial or uniform detail changes.
    RGB + alpha differences are normalized over the visible character region.
    An exact repeated sprite still scores 0.0 and is rejected upstream.
    This is evidence of image activity only, never an artistic approval.
    """
    if len(frames)<2:
        return 0.0
    sampled=[
        list(f.convert('RGBA').resize((64,64),Image.Resampling.BILINEAR).getdata())
        for f in frames
    ]
    diff=0
    total=0
    for previous,current in zip(sampled,sampled[1:]):
        for a,b in zip(previous,current):
            if max(a[3],b[3])<32:
                continue
            diff+=sum(abs(a[k]-b[k]) for k in range(4))
            total+=4*255
    return diff/total if total else 0.0


def _body_region_color_signature(frame:Image.Image,start:float,end:float):
    """Masked RGB histogram of a stable vertical region relative to the sprite.

    The top 28% targets headgear/face; the 40%-73% region targets hands,
    equipment and carried cargo. This reports visual risk, not semantic truth.
    """
    rgba=frame.convert('RGBA')
    bounds=rgba.getchannel('A').getbbox()
    if not bounds:
        raise ValueError('Empty character frame')
    height=bounds[3]-bounds[1]
    top=max(0,bounds[1]+round(height*start))
    bottom=min(rgba.height,max(top+1,bounds[1]+round(height*end)))
    return color_signature(rgba.crop((0,top,rgba.width,bottom)))


def clip_risk(frames:list[Image.Image],action:str|None=None)->dict:
    if len(frames)<4:
        raise ValueError('At least four images needed')
    dims=[frame_geometry(f) for f in frames]
    if any(not item['valid'] for item in dims):
        return {'risk_level':'BLOCKING','flags':['EMPTY_FRAME'],
                'image_only_semantic_approval':False,'frames':dims}
    signatures=[color_signature(frame) for frame in frames]
    adjacent=[
        palette_distance(signatures[i],signatures[(i+1)%len(frames)])
        for i in range(len(frames))
    ]
    median_aspect=statistics.median(f['aspect_ratio'] for f in dims)
    median_height=statistics.median(f['bbox_height_fraction'] for f in dims)
    flat=sum(f['aspect_ratio']<1.30 for f in dims)
    no_feet=sum(f['bottom_segment_count']<2 for f in dims)
    biggest=max(adjacent)
    head_signatures=[_body_region_color_signature(f,0,.28) for f in frames]
    head_changes=[
        palette_distance(head_signatures[i-1],head_signatures[i])
        for i in range(1,len(frames))
    ]
    head_max=max(head_changes,default=0.0)
    mid_signatures=[_body_region_color_signature(f,.40,.73) for f in frames]
    mid_changes=[
        palette_distance(mid_signatures[i-1],mid_signatures[i])
        for i in range(1,len(frames))
    ]
    mid_max=max(mid_changes,default=0.0)
    flags=[]
    if head_max>.24:
        flags.append('HEAD_FACE_HEADGEAR_COLOR_DISCONTINUITY_RISK')
    if (str(action or '').upper() in {'WORK','CARRY','REPAIR'}
        and mid_max>.30):
        flags.append('TOOL_CRATE_TORSO_COLOR_DISCONTINUITY_RISK')
    if flat>=max(2,math.ceil(len(frames)*.25)):
        flags.append('MULTIPLE_NON_FULL_BODY_FRAMES')
    if median_aspect<1.40:
        flags.append('MEDIAN_SILHOUETTE_NOT_FULL_BODY')
    if median_height<.40:
        flags.append('CHARACTER_TOO_SMALL_FOR_CELL')
    if no_feet>=math.ceil(len(frames)*.75):
        flags.append('LOWER_LIMB_STRUCTURE_UNVERIFIED')
    if biggest>.31:
        flags.append('PALETTE_IDENTITY_DISCONTINUITY_RISK')
    sizes=[f['bbox_height_fraction'] for f in dims]
    if max(sizes)/max(min(sizes),.01)>2:
        flags.append('CHARACTER_SCALE_DISCONTINUITY_RISK')
    areas=[f['visible_alpha_area'] for f in dims]
    mass_ratio=max(areas)/max(min(areas),1)
    if mass_ratio>1.80:
        flags.append('SILHOUETTE_MASS_DISCONTINUITY_RISK')
    blockers={'MULTIPLE_NON_FULL_BODY_FRAMES',
              'MEDIAN_SILHOUETTE_NOT_FULL_BODY',
              'PALETTE_IDENTITY_DISCONTINUITY_RISK',
              'CHARACTER_SCALE_DISCONTINUITY_RISK',
              'SILHOUETTE_MASS_DISCONTINUITY_RISK',
              'HEAD_FACE_HEADGEAR_COLOR_DISCONTINUITY_RISK',
              'TOOL_CRATE_TORSO_COLOR_DISCONTINUITY_RISK'}
    blocking=bool(blockers.intersection(flags))
    return {'risk_level':'BLOCKING' if blocking else
            ('REVIEW' if flags else 'NOT_DETECTED'),
            'flags':flags,
            'max_palette_adjacent_distance':round(biggest,4),
            'max_headgear_adjacent_color_distance':round(head_max,4),
            'max_mid_body_prop_adjacent_color_distance':round(mid_max,4),
            'median_palette_adjacent_distance':round(statistics.median(adjacent),4),
            'median_aspect_ratio':round(median_aspect,4),
            'median_height_fraction':round(median_height,4),
            'max_silhouette_mass_ratio':round(mass_ratio,3),
            'non_full_body_frames':flat,
            'foot_profile_ambiguous_frames':no_feet,
            'image_only_semantic_approval':False,'frames':dims}
