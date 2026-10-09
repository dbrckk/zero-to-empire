#!/usr/bin/env python3
"""Deterministic identity-preserving WALK alternative, NOT approved game art.

Reuses one canonical FULL-BODY source frame for the entire 8-frame loop.
Conservative, smoothed gait mesh motion changes boots/legs and counter-swings
sleeves without asking an independent text-to-image generator to redraw faces.
All output goes to build/; never overwrite the canonical sprite or runtime.
This is an experimental review candidate: geometry is not skeletal animation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw
from character_semantic_gate import clip_risk

ROLES={"OP":2,"LOG":0,"ENG":0,"TECH":0}
SIZE=256
N_FRAMES=8


def sample_premultiplied(source:np.ndarray, src_x:np.ndarray,
                        src_y:np.ndarray)->np.ndarray:
    """Vectorized bilinear sampling without transparent-edge dark fringes."""
    height,width=source.shape[:2]
    sx=np.clip(src_x,0,width-1)
    sy=np.clip(src_y,0,height-1)
    x0=np.floor(sx).astype(np.int32);y0=np.floor(sy).astype(np.int32)
    x1=np.minimum(x0+1,width-1);y1=np.minimum(y0+1,height-1)
    u=(sx-x0)[...,None];v=(sy-y0)[...,None]
    prem=source.astype(np.float32)/255.
    prem[:,:,:3]*=prem[:,:,3:4]
    interp=(prem[y0,x0]*(1-u)*(1-v)+prem[y0,x1]*u*(1-v)
            +prem[y1,x0]*(1-u)*v+prem[y1,x1]*u*v)
    alpha=interp[:,:,3:4]
    rgb=np.where(alpha>1e-5,interp[:,:,:3]/np.maximum(alpha,1e-5),0)
    return np.uint8(np.clip(np.concatenate([rgb,alpha],axis=2)*255,0,255))


def warp(anchor:Image.Image,t:float,amplitude:float=12)->Image.Image:
    """Cyclic paired-leg warp and tiny sleeve counter-motion, same identity."""
    if anchor.mode!='RGBA' or anchor.size!=(SIZE,SIZE):
        raise ValueError("Expected an isolated 256x256 RGBA source frame")
    if not math.isfinite(t) or not 2<=amplitude<=18:
        raise ValueError("Invalid animation phase or displacement")
    array=np.asarray(anchor)
    yy,xx=np.mgrid[:SIZE,:SIZE].astype(np.float32)
    phase=math.tau*(t%1.)
    lower=np.clip((yy-138)/94,0,1)
    side=np.tanh((xx-128)/5)
    lateral=amplitude*math.sin(phase)*lower*side
    swing=np.maximum(0,np.sin(phase)*(-side))
    foot_lift=2.5*swing*lower
    upper=np.clip((yy-58)/60,0,1)*np.clip((155-yy)/43,0,1)
    outward=np.clip((np.abs(xx-128)-21)/16,0,1)
    arms=-4*math.sin(phase)*side*upper*outward
    rgba=sample_premultiplied(array,xx-lateral-arms,yy+foot_lift)
    return Image.fromarray(rgba,'RGBA')


def source_frame(path:Path,source_index:int)->Image.Image:
    with Image.open(path) as atlas:
        if atlas.size!=(1024,1024) or atlas.mode!='RGBA':
            raise ValueError("Expected canonical 4-column 1024x1024 RGBA sheet")
        if not 0<=source_index<8:
            raise ValueError("Reference frame out of range")
        x=source_index%4*SIZE;y=source_index//4*SIZE
        frame=atlas.crop((x,y,x+SIZE,y+SIZE))
    bounds=frame.getchannel('A').getbbox()
    if bounds is None or min(bounds[0],bounds[1],SIZE-bounds[2],SIZE-bounds[3])<8:
        raise ValueError("Unsafe or missing reference silhouette")
    return frame


def render(source:Path,role:str,out:Path,amplitude:float=12)->dict:
    role=role.upper()
    if role not in ROLES:
        raise ValueError("Unknown role")
    anchor=source_frame(source,ROLES[role])
    frames=[warp(anchor,n/N_FRAMES,amplitude) for n in range(N_FRAMES)]
    risk=clip_risk(frames)
    if risk["risk_level"]=="BLOCKING":
        raise ValueError("Generated candidate failed identity/full-body risk screen: "+
                         ",".join(risk["flags"]))
    if len({hashlib.sha256(im.tobytes()).digest() for im in frames})<6:
        raise ValueError("Insufficient gait motion")
    sheet=Image.new("RGBA",(1024,512))
    for n,im in enumerate(frames):
        sheet.alpha_composite(im,((n%4)*SIZE,(n//4)*SIZE))
    out.mkdir(parents=True,exist_ok=True)
    dest=out/f"CHR-{role}-WALK-identity-locked-REVIEW.png"
    sheet.save(dest,optimize=True)
    grid=Image.new("RGB",(SIZE*N_FRAMES,SIZE),(25,34,46))
    for n,im in enumerate(frames):
        grid.paste(im,(n*SIZE,0),im)
    grid.save(out/f"CHR-{role}-WALK-contact.png",optimize=True)
    source_digest=hashlib.sha256(source.read_bytes()).hexdigest()
    candidate_digest=hashlib.sha256(dest.read_bytes()).hexdigest()
    report={
        "asset_id":f"CHR-{role}-WALK",
        "source":str(source),"source_sha256":source_digest,
        "reference_frame":ROLES[role],"frame_count":N_FRAMES,
        "candidate_path":str(dest),"candidate_sha256":candidate_digest,
        "animation_mode":"identity-locked-continuous-mesh-experimental-v1",
        "identity_source_count":1,"inferred_art_quality":"NOT_CERTIFIED",
        "visual_risk_screen":risk,"motion_quality":"UNVERIFIED_MECHANICAL_WARP",
        "semantic_review_pass":False,"visual_review_pass":False,
        "strict_status":"NEEDS_REVIEW","integrated_into_game":False,
        "canonical_source_overwritten":False
    }
    (out/f"CHR-{role}-WALK-review.json").write_text(
        json.dumps(report,indent=2)+"\n",encoding="utf-8")
    return report


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--role",required=True,choices=list(ROLES))
    parser.add_argument("--source",type=Path)
    parser.add_argument("--out",type=Path,default=Path("build/identity-locked-walk-review"))
    args=parser.parse_args()
    path=args.source or Path("art/incoming/final-sprites")/f"zte_chr_{args.role.lower()}_walk_final.png"
    print(json.dumps(render(path,args.role,args.out),indent=2))


if __name__=="__main__":
    main()
