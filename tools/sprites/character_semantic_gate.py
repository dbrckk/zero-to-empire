"""Image-only risk screening for full-body character animation candidates.

This detects obvious portrait/fragments and palette identity jumps, not artistry.
Even zero detected risks NEVER implies semantic or human visual approval.
"""
from __future__ import annotations

import math
import statistics
from PIL import Image, ImageChops


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


def celebration_arm_reach_counts(frames:list[Image.Image])->list[int]:
    """Count raised-limb silhouette away from the upper torso per frame.

    Avoid mistaking a changing head, costume or a final-frame sparkle for a
    progressive cheering gesture. Detect actual visible outward/raised arms
    in at least three action frames; this is still NOT semantic approval.
    """
    counts=[]
    for frame in frames:
        alpha=frame.convert('RGBA').getchannel('A')
        bb=alpha.getbbox()
        if bb is None:
            counts.append(0)
            continue
        left,top,right,bottom=bb
        height=bottom-top
        centre=(left+right)/2
        y0=max(0,top+int(height*.18))
        y1=min(frame.height,top+int(height*.34))
        pixels=alpha.load()
        count=0
        for y in range(y0,y1):
            for x in range(frame.width):
                if abs(x-centre)>34 and pixels[x,y]>=120:
                    count+=1
        counts.append(count)
    return counts


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


def head_structure_drift(frames:list[Image.Image])->float:
    """Pixel-structure drift of aligned face/headgear texture from frame zero.

    Plain RGB histograms miss cases where the entire face/helmet changes shape
    while retaining orange/white/graphite colors. Crop only the upper head
    instead of shoulders, hands or accessories; avoid model dependencies.
    This is a rejection risk, NOT face recognition or automatic approval.
    """
    heads=[]
    for frame in frames:
        rgba=frame.convert('RGBA')
        if rgba.size!=(256,256):
            raise ValueError('Character head structural QA expects 256x256 frames')
        alpha=rgba.getchannel('A')
        bb=alpha.getbbox()
        if bb is None:
            return 1.0
        left,top,right,bottom=bb
        band=alpha.crop((0,top,256,top+max(1,int((bottom-top)*.23))))
        weighted=count=0
        px=band.load()
        for y in range(band.height):
            for x in range(256):
                if px[x,y]>=128:
                    weighted+=x
                    count+=1
        centre=round(weighted/count) if count else (left+right)//2
        crop_x=max(0,min(188,centre-34))
        crop_y=max(0,min(188,top-2))
        heads.append(list(rgba.crop((crop_x,crop_y,crop_x+68,crop_y+68))
                     .resize((48,48),Image.Resampling.BILINEAR).getdata()))
    reference=heads[0]
    result=0.0
    for current in heads[1:]:
        error=total=0
        for p,q in zip(reference,current):
            if max(p[3],q[3])<32:
                continue
            error+=sum(abs(p[channel]-q[channel]) for channel in range(4))
            total+=1020
        if total:
            result=max(result,error/total)
    return result


def lower_ground_band_ratio(frame:Image.Image)->float:
    """Look for a suspicious solid ground bar beneath two narrower legs.

    A baked oval floor shadow often spans the full base of the character even
    when shoes are separated. A wide *connected horizontal run* near the bottom
    distinguishes it from naturally spread feet. This is a risk heuristic:
    passing this check is not proof of transparency or visual acceptability.
    """
    alpha=frame.convert('RGBA').getchannel('A')
    bounds=alpha.getbbox()
    if not bounds:
        return 0.0
    left,top,right,bottom=bounds
    height=bottom-top
    if height<96:
        return 0.0
    pixels=alpha.load()
    reference_top=max(top,bottom-round(height*.20))
    reference_bottom=max(reference_top+2,bottom-round(height*.10))
    needed=max(2,round((reference_bottom-reference_top)*.18))
    leg_columns=[
        x for x in range(left,right)
        if sum(pixels[x,y]>=96 for y in range(reference_top,reference_bottom))>=needed
    ]
    if len(leg_columns)<12:
        return 0.0
    leg_span=max(leg_columns)-min(leg_columns)+1
    # Connected dark shoes can have the *same alpha silhouette* as a cast
    # floor shadow. The prior alpha-only heuristic blocked valid-looking ENG
    # idle anchors, cascading into five skipped actions. Count only broad,
    # nearly neutral, low-contrast ground-colored bands below the ankles.
    # Preserve the strict rejection of genuine gray shadows; this is not an
    # automatic semantic acceptance of the full sheet.
    rgb=frame.convert('RGBA').load()
    longest=0
    for y in range(max(top,bottom-round(height*.075)),bottom):
        run=0
        for x in range(left,right):
            red,green,blue,a=rgb[x,y]
            neutral=(a>=96 and 70<=min(red,green,blue)<=235
                     and max(red,green,blue)-min(red,green,blue)<=21)
            if neutral:
                run+=1
                longest=max(longest,run)
            else:
                run=0
    if longest<50:
        return 0.0
    return longest/max(leg_span,1)


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


def idle_distinct_head_clusters(frame:Image.Image)->int:
    """Count well-separated opaque heads in the top 2%-14% of the sprite.

    This detects two side-by-side workers whose shoulders touch into one
    connected silhouette. The whole-character connected-component and aspect
    checks previously missed these (LOG IDLE collector 38281126201). Limit
    this check to IDLE: raised arms or props can add upper clusters in actions.
    """
    alpha=frame.convert('RGBA').getchannel('A')
    bbox=alpha.getbbox()
    if not bbox:
        return 0
    left,top,right,bottom=bbox
    height=bottom-top
    y0=top+round(height*.02)
    y1=min(frame.height,top+round(height*.14))
    if y1<=y0:
        return 0
    pixels=alpha.load()
    occupancy=[
        sum(pixels[x,y]>=64 for y in range(y0,y1))
        for x in range(frame.width)
    ]
    cutoff=max(3,round((y1-y0)*.20))
    runs=[]
    start=None
    for x,count in enumerate(occupancy):
        present=count>=cutoff
        if present and start is None:
            start=x
        if not present and start is not None:
            if x-start>=8:
                runs.append((start,x-1))
            start=None
    if start is not None and frame.width-start>=8:
        runs.append((start,frame.width-1))
    for index,left_run in enumerate(runs):
        for right_run in runs[index+1:]:
            center_a=(left_run[0]+left_run[1])/2
            center_b=(right_run[0]+right_run[1])/2
            if right_run[0]-left_run[1]>=8 and center_b-center_a>=24:
                return 2
    return 1 if runs else 0


def _upper_head_centroid(frame:Image.Image):
    """Approximate actor registration from the upper opaque head silhouette."""
    rgba=frame.convert('RGBA')
    alpha=rgba.getchannel('A')
    bbox=alpha.getbbox()
    if bbox is None:
        return None
    height=bbox[3]-bbox[1]
    y0=max(0,bbox[1]+round(height*.04))
    y1=min(frame.height,max(y0+1,bbox[1]+round(height*.25)))
    region=alpha.crop((0,y0,frame.width,y1))
    pixels=region.load()
    sum_x=sum_y=count=0
    for y in range(region.height):
        for x in range(region.width):
            if pixels[x,y]>=120:
                sum_x+=x
                sum_y+=y+y0
                count+=1
    if count<60:
        return None
    return round(sum_x/count),round(sum_y/count)


def _binary_alpha_iou(a:Image.Image,b:Image.Image)->float:
    aa=a.getchannel('A').point(lambda v:255 if v>=32 else 0)
    bb=b.getchannel('A').point(lambda v:255 if v>=32 else 0)
    overlap=ImageChops.darker(aa,bb).histogram()[255]
    union=ImageChops.lighter(aa,bb).histogram()[255]
    return overlap/union if union else 1.0


def action_translation_metrics(frames:list[Image.Image])->dict:
    """Detect apparent action motion due mainly to shifting the whole actor.

    A 256px WORK/REPAIR atlas can exceed the alpha-change threshold if the
    standing character slides horizontally, even with no raised forearms.
    Register the upper head silhouette and measure the pose-change remainder.
    This is a reject-only risk signal, never a semantic quality approval.
    """
    if len(frames)<4:
        raise ValueError('At least four frames are needed for action motion')
    rgba=[f.convert('RGBA') for f in frames]
    if any(f.size!=(256,256) for f in rgba):
        raise ValueError('Expected 256x256 character action frames')
    anchors=[_upper_head_centroid(f) for f in rgba]
    if any(anchor is None for anchor in anchors):
        return {'translation_dominated':False,
                'insufficient_registration_evidence':True}
    first=anchors[0]
    aligned=[]
    for frame,(x,y) in zip(rgba,anchors):
        registered=Image.new('RGBA',frame.size,(0,0,0,0))
        registered.paste(frame,(first[0]-x,first[1]-y))
        aligned.append(registered)
    raw=sum(1-_binary_alpha_iou(a,b) for a,b in zip(rgba,rgba[1:]))/(len(rgba)-1)
    residual=sum(1-_binary_alpha_iou(a,b)
                 for a,b in zip(aligned,aligned[1:]))/(len(aligned)-1)
    head_excursion=max(x for x,y in anchors)-min(x for x,y in anchors)
    ratio=residual/max(raw,.001)
    dominated=raw>=.15 and head_excursion>=12 and ratio<.43
    return {'mean_raw_alpha_motion':round(raw,4),
            'mean_registered_alpha_motion':round(residual,4),
            'retained_pose_motion_ratio':round(ratio,4),
            'head_horizontal_excursion_px':head_excursion,
            'translation_dominated':dominated,
            'insufficient_registration_evidence':False}


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
    head_shape_drift=(head_structure_drift(frames)
                      if str(action or '').upper() in {'WALK','WORK','CARRY','REPAIR'}
                      else 0.0)
    ground_band_ratios=[lower_ground_band_ratio(frame) for frame in frames]
    ground_band_count=sum(value>=1.27 for value in ground_band_ratios)
    idle_head_clusters=(
        [idle_distinct_head_clusters(frame) for frame in frames]
        if str(action or '').upper()=='IDLE' else []
    )
    double_head_frames=sum(value>=2 for value in idle_head_clusters)
    flags=[]
    action_pose_metrics={}
    if str(action or '').upper() in {'WORK','REPAIR'}:
        action_pose_metrics=action_translation_metrics(frames)
        if action_pose_metrics.get('translation_dominated'):
            flags.append('ACTION_TRANSLATION_DOMINATES_POSE_RISK')
    if double_head_frames>=2:
        flags.append('MULTIPLE_IDLE_HEADS_RISK')
    if ground_band_count>=math.ceil(len(frames)*.5):
        flags.append('BAKED_GROUND_SHADOW_RISK')
    if head_max>.24:
        flags.append('HEAD_FACE_HEADGEAR_COLOR_DISCONTINUITY_RISK')
    if head_shape_drift>.19:
        flags.append('FACE_HEADGEAR_STRUCTURE_DRIFT_RISK')
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
    # A single mysteriously shortened frame was accepted in LOG-WORK even
    # though its neighbors retained normal full-body framing. Reject per-frame
    # collapses instead of waiting for >=2 portrait fragments or a 2x jump.
    min_relative_height=min(sizes)/max(statistics.median(sizes),.01)
    if (str(action or '').upper() in {'WALK','WORK','CARRY','REPAIR','CELEB'}
        and min_relative_height<.82):
        flags.append('FRAME_SCALE_COLLAPSE_RISK')
    if max(sizes)/max(min(sizes),.01)>2:
        flags.append('CHARACTER_SCALE_DISCONTINUITY_RISK')
    areas=[f['visible_alpha_area'] for f in dims]
    mass_ratio=max(areas)/max(min(areas),1)
    if mass_ratio>1.80:
        flags.append('SILHOUETTE_MASS_DISCONTINUITY_RISK')
    blockers={'ACTION_TRANSLATION_DOMINATES_POSE_RISK',
              'MULTIPLE_IDLE_HEADS_RISK',
              'MULTIPLE_NON_FULL_BODY_FRAMES',
              'MEDIAN_SILHOUETTE_NOT_FULL_BODY',
              'PALETTE_IDENTITY_DISCONTINUITY_RISK',
              'CHARACTER_SCALE_DISCONTINUITY_RISK',
              'FRAME_SCALE_COLLAPSE_RISK',
              'SILHOUETTE_MASS_DISCONTINUITY_RISK',
              'HEAD_FACE_HEADGEAR_COLOR_DISCONTINUITY_RISK',
              'FACE_HEADGEAR_STRUCTURE_DRIFT_RISK',
              'BAKED_GROUND_SHADOW_RISK',
              'TOOL_CRATE_TORSO_COLOR_DISCONTINUITY_RISK'}
    blocking=bool(blockers.intersection(flags))
    return {'risk_level':'BLOCKING' if blocking else
            ('REVIEW' if flags else 'NOT_DETECTED'),
            'flags':flags,
            'action_pose_metrics':action_pose_metrics,
            'max_palette_adjacent_distance':round(biggest,4),
            'max_headgear_adjacent_color_distance':round(head_max,4),
            'max_face_headgear_structural_drift':round(head_shape_drift,4),
            'max_mid_body_prop_adjacent_color_distance':round(mid_max,4),
            'median_palette_adjacent_distance':round(statistics.median(adjacent),4),
            'median_aspect_ratio':round(median_aspect,4),
            'median_height_fraction':round(median_height,4),
            'min_relative_frame_height':round(min_relative_height,4),
            'max_silhouette_mass_ratio':round(mass_ratio,3),
            'baked_ground_band_suspected_frames':ground_band_count,
            'two_head_idle_frames':double_head_frames,
            'max_ground_band_to_leg_width':round(max(ground_band_ratios),3),
            'non_full_body_frames':flat,
            'foot_profile_ambiguous_frames':no_feet,
            'image_only_semantic_approval':False,'frames':dims}
