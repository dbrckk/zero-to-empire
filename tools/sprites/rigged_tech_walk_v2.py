#!/usr/bin/env python3
"""Produce a single-identity, modular-textured animated TECH walk, with joint caps.

Self-contained apart from a packed RGBA skin atlas and Pillow/numpy. Never writes
master queues or strict DONE. Uses deterministic foot trajectories and two-bone IK.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import statistics
import zipfile
from pathlib import Path
from typing import Any
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

CANVAS, GROUND, ROOT_X, HIP_Y = 512, 449, 252, 270
STRIDE, CLEARANCE, STANCE = 92.0, 36.0, 0.62
PART_NAMES = ('head', 'torso', 'pelvis', 'backpack', 'upper_arm_far',
 'forearm_far','upper_arm_near','forearm_near','thigh_far','shin_boot_far',
 'thigh_near','shin_boot_near')


def foot_local(t: float):
    t %= 1.0
    if t < STANCE:
        return STRIDE/2 - STRIDE*t/STANCE, GROUND, True
    u = (t-STANCE)/(1-STANCE)
    slope = -STRIDE/STANCE*(1-STANCE)
    # Hermite recovers stance velocity at both ends of swing.
    h00, h10 = 2*u**3-3*u*u+1, u**3-2*u*u+u
    h01, h11 = -2*u**3+3*u*u, u**3-u*u
    return (h00*(-STRIDE/2)+h10*slope+h01*(STRIDE/2)+h11*slope,
            GROUND-CLEARANCE*max(0,math.sin(math.pi*u))**1.3, False)


def foot_roll(t: float) -> float:
    t %= 1.0
    if t < STANCE:
        u=t/STANCE
        if u < .17: return -.18*(1-u/.17)
        if u > .8: return .22*(u-.8)/.2
        return 0.0
    u=(t-STANCE)/(1-STANCE)
    return .22*(1-u)-.18*u


def pose(t: float) -> dict[str,Any]:
    t%=1.0
    root=(ROOT_X,HIP_Y+3.5*math.cos(4*math.pi*t))
    xr,yr,lr=foot_local(t)
    xl,yl,ll=foot_local(t+.5)
    swing=30*math.cos(2*math.pi*t)
    return {'root':root, 'left':(ROOT_X+xl,yl),'right':(ROOT_X+xr,yr),
            'handL':(ROOT_X-19+swing,root[1]-18-5*math.sin(2*math.pi*t)),
            'handR':(ROOT_X+43-swing,root[1]-21+5*math.sin(2*math.pi*t)),
            'lockL':ll,'lockR':lr,'rollL':foot_roll(t+.5),'rollR':foot_roll(t)}


def ik(a,b,l1,l2,sign=1):
    dx,dy=b[0]-a[0],b[1]-a[1]
    length=math.hypot(dx,dy) or 1.e-5
    d=max(abs(l1-l2)+.001,min(l1+l2-.001,length))
    ux,uy=dx/length,dy/length
    along=(l1*l1-l2*l2+d*d)/(2*d)
    h=math.sqrt(max(0,l1*l1-along*along))
    return (a[0]+ux*along+uy*h*sign,a[1]+uy*along-ux*h*sign)


def load_kit(atlas:Path) -> dict[str,Image.Image]:
    if not atlas.exists(): raise FileNotFoundError(atlas)
    with Image.open(atlas) as image:
        if image.size != (1024,768): raise ValueError('skin atlas must be 1024x768')
        rgba=image.convert('RGBA')
    kit={}
    for i,name in enumerate(PART_NAMES):
        tile=rgba.crop(((i%4)*256,(i//4)*256,(i%4+1)*256,(i//4+1)*256))
        bbox=tile.getchannel('A').getbbox()
        if bbox is None: raise ValueError(f'Empty texture part {name}')
        kit[name]=tile.crop(bbox)
    for name in ('shin_boot_far','shin_boot_near'):
        image=kit[name]
        cut=round(image.height*.72)
        kit[name+'_calf']=image.crop((0,0,image.width,cut))
        kit[name+'_boot']=image.crop((0,cut-7,image.width,image.height))
    return kit


def paste(layer,img,x,y):
    layer.alpha_composite(img,(round(x),round(y)))


def rotated_limb(layer,img,a,b,occupancy=.87,width_mul=1):
    """Warp proximal-to-distal textured rigid piece around an exact IK bone."""
    dist=math.dist(a,b)
    height=max(1,round(dist/occupancy))
    width=max(1,round(height*img.width/img.height*width_mul))
    sprite=img.resize((width,height),Image.Resampling.LANCZOS)
    # generous rotation canvas prevents cut-offs for all joint orientations
    side=max(184,round(height*3.5))
    center=side//2
    stage=Image.new('RGBA',(side,side))
    stage.alpha_composite(sprite,(round(center-width*.5),round(center-height*.07)))
    angle=90-math.degrees(math.atan2(b[1]-a[1],b[0]-a[0]))
    stage=stage.rotate(angle,resample=Image.Resampling.BICUBIC)
    paste(layer,stage,a[0]-center,a[1]-center)


def fabric_hinge(layer, start, hinge, end, radius=12, near=True):
    """Flexible cloth gusset behind the rigid knee/elbow cap.

    Each fold follows the exact IK bone vectors; no free-floating redraw.
    Kept optional to preserve the proven legacy WALK pixels.
    """
    ux,uy=hinge[0]-start[0],hinge[1]-start[1]
    vx,vy=end[0]-hinge[0],end[1]-hinge[1]
    lu,lv=math.hypot(ux,uy),math.hypot(vx,vy)
    if lu<1e-6 or lv<1e-6:return
    ux,uy,vx,vy=ux/lu,uy/lu,vx/lv,vy/lv
    tx,ty=ux+vx,uy+vy
    d=math.hypot(tx,ty)
    if d<.08:tx,ty=ux,uy
    else:tx,ty=tx/d,ty/d
    cross=ux*vy-uy*vx
    bend=math.acos(max(-1.,min(1.,ux*vx+uy*vy)))
    scale=2;r=float(radius)
    side=round((r*2.8+12)*scale)*2
    local=Image.new('RGBA',(side,side))
    draw=ImageDraw.Draw(local,'RGBA')
    cx=cy=side//2
    def xy(x,y):return (round(cx+x*scale),round(cy+y*scale))
    cloth=(35,45,55,245) if near else (23,31,40,225)
    draw.polygon([xy(-r*.82,-r*1.43),xy(r*.73,-r*1.43),
                  xy(r*.92,r*1.48),xy(-r*.7,r*1.47)],
                 fill=(15,23,33,245) if near else (12,19,27,215))
    draw.rounded_rectangle((cx-round(.67*r*scale),cy-round(1.4*r*scale),
                            cx+round(.67*r*scale),cy+round(1.4*r*scale)),
                           radius=round(.5*r*scale),fill=cloth)
    for i in range(2 if bend<.27 else 3):
        yy=(-.70+i*.53)*r;slope=cross*.30*r
        draw.line([xy(-r*.49,yy-slope),xy(r*.47,yy+slope)],
                  fill=(7,13,21,125+min(70,int(bend*48))),width=round(1.6*scale))
        draw.line([xy(-r*.36,yy-slope-2.4),xy(r*.33,yy+slope-2.4)],
                  fill=(116,132,143,55),width=round(scale))
    draw.line([xy(-r*.56,-r*1.15),xy(-r*.55,r*1.17)],
              fill=(100,115,129,105),width=round(1.1*scale))
    draw.line([xy(r*.55,-r*1.15),xy(r*.54,r*1.16)],
              fill=(5,12,19,175),width=round(1.3*scale))
    theta=math.degrees(math.atan2(ty,tx))-90
    rotated=local.rotate(-theta,resample=Image.Resampling.BICUBIC)
    rotated=rotated.resize((side//scale,side//scale),Image.Resampling.LANCZOS)
    paste(layer,rotated,hinge[0]-rotated.width/2,hinge[1]-rotated.height/2)


def ankle_gaiter(layer,knee,ankle,near=True):
    """Short boot/cloth overlap beneath the sole-aligned rigid shoe."""
    dx,dy=ankle[0]-knee[0],ankle[1]-knee[1]
    norm=math.hypot(dx,dy)
    if norm<.001:return
    dx,dy=dx/norm,dy/norm
    x=ankle[0]-dx*19;y=ankle[1]-dy*19;r=9 if near else 8
    pts=[(x+dy*r,y-dx*r),(x-dy*r,y+dx*r),
         (x-dx*14-dy*r*.82,y-dy*14+dx*r*.82),
         (x-dx*14+dy*r*.82,y-dy*14-dx*r*.82)]
    draw=ImageDraw.Draw(layer,'RGBA')
    draw.polygon(pts,fill=(16,23,32,195) if near else (13,20,28,175))
    a=(x-dx*12+dy*r*.75,y-dy*12-dx*r*.75)
    b=(x-dx*12-dy*r*.75,y-dy*12+dx*r*.75)
    draw.line([a,b],fill=(123,135,143,150),width=2)


def joint_cap(layer,p,r=14,depth='near'):
    """Soft metallic overlap at hinge hides segment gaps without redrawing identity."""
    size=2*round(r+7)
    yy,xx=np.mgrid[:size,:size].astype('float32')
    cx=cy=(size-1)/2
    d=((xx-cx)/r)**2+((yy-cy)/(r*.79))**2
    feather=np.clip((1-d)*12,0,1)
    light=np.clip((cy-yy)/size+.3,0,1)
    main=np.zeros((size,size,4),dtype='uint8')
    tint=1.0 if depth=='near' else .8
    main[:,:,0]=np.clip((19+35*light)*tint,0,255)
    main[:,:,1]=np.clip((27+42*light)*tint,0,255)
    main[:,:,2]=np.clip((35+51*light)*tint,0,255)
    main[:,:,3]=(feather*255).astype('uint8')
    cap=Image.fromarray(main,'RGBA')
    draw=ImageDraw.Draw(cap,'RGBA')
    draw.ellipse((cx-r*.57,cy-r*.45,cx+r*.54,cy+r*.41),outline=(88,104,121,155),width=2)
    draw.arc((cx-r*.6,cy-r*.58,cx+r*.58,cy+r*.54),190,318,fill=(127,144,153,135),width=2)
    draw.ellipse((cx-2,cy-2,cx+2,cy+2),fill=(67,100,117,125))
    paste(layer,cap,p[0]-cx,p[1]-cy)


def render_boot(layer,img,foot,angle) -> dict[str,float]:
    """Place sole at demanded contact Y, instead of guessing boot ankle offset."""
    width=69
    height=round(width*img.height/img.width)
    shoe=img.resize((width,height),Image.Resampling.LANCZOS)
    pivot=(round(width*.26),round(height*.30))
    side=max(160,round(max(width,height)*2.5))
    base=Image.new('RGBA',(side,side))
    center=side//2
    base.alpha_composite(shoe,(center-pivot[0],center-pivot[1]))
    turn=base.rotate(-math.degrees(angle),resample=Image.Resampling.BICUBIC)
    bbox=turn.getchannel('A').getbbox()
    if bbox is None: raise ValueError('Empty boot')
    # Anchor visually consistent ankle X while sole follows the foot path.
    px=round(foot[0]-center)
    py=round(foot[1]-bbox[3])
    paste(layer,turn,px,py)
    return {'sole_y':py+bbox[3],'foot_target_y':foot[1],
            'sole_error_px':abs(py+bbox[3]-foot[1]), 'toe_x':px+bbox[2]}


def draw_frame(t:float,kit:dict,pose_override=None,prop_underlay=None,prop_overlay=None,joint_fabric=False):
    p=pose(t) if pose_override is None else pose_override
    x,y=p['root']
    canvas=Image.new('RGBA',(CANVAS,CANVAS))
    lhip,rhip=(x-13,y),(x+13,y)
    kneeL=ik(lhip,p['left'],94,99,1)
    kneeR=ik(rhip,p['right'],94,99,1)
    # Small, deterministic spine flexion rotates all upper-body parts around
    # one hip pivot while planted feet stay fixed in world space.
    lean=float(p.get('torso_lean_rad',0.0))
    if not math.isfinite(lean) or abs(lean)>.085:
        raise ValueError('torso lean exceeds approved range')
    cos_a,sin_a=math.cos(lean),math.sin(lean)
    def spine(dx,dy):return (x+dx*cos_a-dy*sin_a,y+dx*sin_a+dy*cos_a)
    def torso_piece(sprite,size,local_center,rotate=True):
        img=sprite.resize(size,Image.Resampling.LANCZOS)
        if rotate and abs(lean)>1e-6:
            img=img.rotate(-math.degrees(lean),expand=True,resample=Image.Resampling.BICUBIC)
        cx,cy=spine(*local_center)
        paste(canvas,img,cx-img.width/2,cy-img.height/2)
    shoulderL,shoulderR=spine(-24,-86),spine(23,-85)
    elbowL=ik(shoulderL,p['handL'],59,59,-1)
    elbowR=ik(shoulderR,p['handR'],59,59,-1)
    rotated_limb(canvas,kit['thigh_far'],lhip,kneeL,.87,.88)
    rotated_limb(canvas,kit['shin_boot_far_calf'],kneeL,p['left'],.91,.83)
    if joint_fabric: fabric_hinge(canvas,lhip,kneeL,p['left'],12,False)
    joint_cap(canvas,kneeL,10,'far')
    if joint_fabric: ankle_gaiter(canvas,kneeL,p['left'],False)
    bootL=render_boot(canvas,kit['shin_boot_far_boot'],p['left'],p['rollL'])
    rotated_limb(canvas,kit['upper_arm_far'],shoulderL,elbowL,.88,.88)
    rotated_limb(canvas,kit['forearm_far'],elbowL,p['handL'],.87,.88)
    if joint_fabric: fabric_hinge(canvas,shoulderL,elbowL,p['handL'],9,False)
    joint_cap(canvas,elbowL,8,'far')
    torso_piece(kit['backpack'],(72,94),(-41,-82))
    torso_piece(kit['torso'],(104,117),(10,-75.5))
    paste(canvas,kit['pelvis'].resize((78,68),Image.Resampling.LANCZOS),x-38,y-43)
    if prop_underlay is not None: prop_underlay(canvas,p,t)
    rotated_limb(canvas,kit['thigh_near'],rhip,kneeR,.87,.95)
    rotated_limb(canvas,kit['shin_boot_near_calf'],kneeR,p['right'],.91,.9)
    if joint_fabric: fabric_hinge(canvas,rhip,kneeR,p['right'],14,True)
    joint_cap(canvas,kneeR,12,'near')
    if joint_fabric: ankle_gaiter(canvas,kneeR,p['right'],True)
    bootR=render_boot(canvas,kit['shin_boot_near_boot'],p['right'],p['rollR'])
    rotated_limb(canvas,kit['upper_arm_near'],shoulderR,elbowR,.88,.95)
    rotated_limb(canvas,kit['forearm_near'],elbowR,p['handR'],.87,.94)
    if joint_fabric: fabric_hinge(canvas,shoulderR,elbowR,p['handR'],10,True)
    joint_cap(canvas,elbowR,9,'near')
    # Counter-rotated head avoids unnatural nodding when the chest leans.
    torso_piece(kit['head'],(85,111),(20.5,-163.5),rotate=False)
    if prop_overlay is not None: prop_overlay(canvas,p,t)
    return canvas,p,{'left':bootL,'right':bootR}


def check(frames:list[Image.Image],poses:list[dict],boots:list[dict]):
    arr=[np.array(f.getchannel('A'))>=128 for f in frames]
    diff=[]
    for i,a in enumerate(arr):
        b=arr[(i+1)%len(arr)]
        union=np.count_nonzero(a|b)
        diff.append(round(float(np.count_nonzero(a^b)/union) if union else 1.,5))
    median=statistics.median(diff)
    bounds=[f.getchannel('A').getbbox() for f in frames]
    clip=[i for i,b in enumerate(bounds) if b is None or b[0]<6 or b[1]<6 or b[2]>CANVAS-6 or b[3]>CANVAS-6]
    soles=[b[s]['sole_error_px'] for b in boots for s in ('left','right')]
    penetration=[i for i,p in enumerate(poses) if p['left'][1]>GROUND+1e-5 or p['right'][1]>GROUND+1e-5]
    ratio=diff[-1]/median if median else 999
    pass_geometry=not clip and not penetration and max(soles)<=1.0 and .40<ratio<1.9
    return {'alpha_bounds':bounds,'edge_touch_frames':clip,'foot_penetration_frames':penetration,
            'max_sole_alignment_error_px':max(soles),'mean_sole_alignment_error_px':round(statistics.mean(soles),4),
            'silhouette_transition_disagreement':diff,'seam_to_median_ratio':round(ratio,4),
            'alpha_channel_present':all(f.mode=='RGBA' and f.getpixel((0,0))[3]==0 for f in frames),
            'technical_pass':bool(pass_geometry),'visual_review_pass':False,
            'semantic_review_pass':False,'strict_status':'NEEDS_REVIEW'}


def build(atlas:Path,out:Path,frames=24,fps=12):
    if not (8<=frames<=64 and frames%2==0 and 3<=fps<=24):
        raise ValueError('frames must be even, 8–64; fps 3–24')
    kit=load_kit(atlas)
    out.mkdir(parents=True,exist_ok=True)
    (out/'frames').mkdir(exist_ok=True)
    images=[]; poses=[]; boots=[]
    for i in range(frames):
        im,p,b=draw_frame(i/frames,kit)
        im.save(out/'frames'/f'CHR-TECH-WALK-{i:02d}.png',optimize=True)
        images.append(im);poses.append(p);boots.append(b)
    cols=6; rows=math.ceil(frames/cols)
    atlas_img=Image.new('RGBA',(CANVAS*cols,CANVAS*rows))
    thumbs=[]
    for i,im in enumerate(images):
        atlas_img.alpha_composite(im,((i%cols)*CANVAS,(i//cols)*CANVAS))
        bg=Image.new('RGBA',(CANVAS,CANVAS),(26,34,45,255))
        bg.alpha_composite(im)
        thumbs.append(bg.convert('RGB').resize((192,192),Image.Resampling.LANCZOS))
    atlas_img.save(out/'atlas.png',optimize=True)
    contact=Image.new('RGB',(192*cols,192*rows),(27,34,45))
    for i,im in enumerate(thumbs): contact.paste(im,((i%cols)*192,(i//cols)*192))
    contact.save(out/'contact.jpg',quality=94)
    thumbs[0].save(out/'preview.gif',save_all=True,append_images=thumbs[1:],duration=round(1000/fps),loop=0,optimize=False)
    qa=check(images,poses,boots)
    events=[{'frame':i,'footstep':('right' if i==0 else 'left' if i==frames//2 else None),
             'left_ground_contact':p['lockL'],'right_ground_contact':p['lockR']} for i,p in enumerate(poses)]
    manifest={'asset_id':'CHR-TECH-WALK','build':'modular-skin-v2-IK-joint-guards',
              'rig':'deterministic_two_bone_ik','render_source':'single-texture-atlas',
              'source_skin_sha256':hashlib.sha256(atlas.read_bytes()).hexdigest(),
              'frames':frames,'fps':fps,'frame_size':[CANVAS,CANVAS],
              'atlas_columns':cols,'atlas_rows':rows,'pivot':{'x':ROOT_X,'y':GROUND},
              'strict_status':'NEEDS_REVIEW','human_visual_review_required':True,
              'qa':qa,'limits':['Rigid 2D parts: inspect arms and knee seam for realism',
                'Automatic geometric QA is not a semantic approval','Review in the actual game camera before release']}
    (out/'qa-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    (out/'footstep-events.json').write_text(json.dumps(events,indent=2),encoding='utf-8')
    (out/'frame-poses.json').write_text(json.dumps(poses,indent=2),encoding='utf-8')
    (out/'REVIEW_REQUIRED.txt').write_text('NO STRICT DONE: genuine visual + semantic review required.\n',encoding='utf-8')
    bundle=out.parent/'CHR-TECH-WALK-modular-v2-review.zip'
    with zipfile.ZipFile(bundle,'w',zipfile.ZIP_DEFLATED) as z:
        for path in sorted(out.rglob('*')):
            if path.is_file():z.write(path,path.relative_to(out))
    return manifest,bundle


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skin',type=Path,default=Path(__file__).resolve().parent/'skin-tech-v1.webp')
    parser.add_argument('--output',type=Path,default=Path('build/tech-walk-modular-v2'))
    parser.add_argument('--frames',type=int,default=24)
    parser.add_argument('--fps',type=int,default=12)
    args=parser.parse_args()
    manifest,path=build(args.skin,args.output,args.frames,args.fps)
    print(json.dumps({'bundle':str(path),'technical_pass':manifest['qa']['technical_pass'],
                       'seam_ratio':manifest['qa']['seam_to_median_ratio'],
                       'max_sole_alignment_error_px':manifest['qa']['max_sole_alignment_error_px'],
                       'strict_status':manifest['strict_status']}))
    if not manifest['qa']['technical_pass']:
        raise SystemExit('Technical QA rejected this candidate')

if __name__=='__main__':main()
