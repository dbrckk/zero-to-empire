"""Shared pivot-preserving framing for small-screen TECH preview sprites.

A *single* crop applies to every frame and every action. This prevents fake
camera motion and gives all animations the same world-space foot pivot. The
original 512px frames and canonical 128/256px variants are never modified.

All outputs are review-only; framing is NOT an artistic quality approval.
"""
from __future__ import annotations

import math
from pathlib import Path
from PIL import Image

CANVAS = 512
PIVOT = (252, 449)


def shared_crop(bounds: list[tuple[int,int,int,int]], margin: int = 12,
                canvas: int = CANVAS, pivot: tuple[int,int] = PIVOT) -> tuple[int,int,int,int]:
    """Return a square alpha-safe view shared by *all* actions and poses.

    Bounds must cover nonzero alpha, not only opaque pixels; sparse transparent
    tool/VFX edges should not be cut to make a visually larger character.
    """
    if not bounds or canvas < 64 or not 0 <= margin <= 64:
        raise ValueError("Invalid frame bounds or crop parameters")
    x0=min(b[0] for b in bounds); y0=min(b[1] for b in bounds)
    x1=max(b[2] for b in bounds); y1=max(b[3] for b in bounds)
    if any(not (0<=a<b<=canvas) for a,b in ((x0,x1),(y0,y1))):
        raise ValueError("Invalid alpha bounds")
    side=math.ceil((max(x1-x0,y1-y0)+2*margin)/16)*16
    side=min(canvas,max(64,side))
    left=max(0,min(canvas-side,round(pivot[0]-side/2)))
    top=max(0,min(canvas-side,round((y0+y1-side)/2)))
    crop=(left,top,left+side,top+side)
    if not (left<=x0 and crop[2]>=x1 and top<=y0 and crop[3]>=y1):
        raise ValueError("Shared viewport would clip an action")
    if not (left<=pivot[0]<crop[2] and top<=pivot[1]<crop[3]):
        raise ValueError("Foot pivot outside shared view")
    return crop


def view_pivot(crop:tuple[int,int,int,int],size:int,
               pivot:tuple[int,int]=PIVOT)->list[float]:
    side=crop[2]-crop[0]
    if side<=0 or crop[3]-crop[1]!=side or size<=0:
        raise ValueError("Invalid crop or sprite size")
    if not(crop[0]<=pivot[0]<crop[2] and crop[1]<=pivot[1]<crop[3]):
        raise ValueError("Pivot outside crop")
    return [round((pivot[0]-crop[0])*size/side,3),
            round((pivot[1]-crop[1])*size/side,3)]


def framed_sprite(frame:Image.Image,crop:tuple[int,int,int,int],size:int)->Image.Image:
    if frame.size!=(CANVAS,CANVAS) or frame.mode!='RGBA':
        raise ValueError("Expected 512px RGBA sprite")
    if any(v<0 or v>CANVAS for v in crop):
        raise ValueError("Crop outside canvas")
    a=frame.getchannel('A').getbbox()
    if a is not None and not(crop[0]<=a[0] and crop[1]<=a[1] and
                             crop[2]>=a[2] and crop[3]>=a[3]):
        raise ValueError("Framing would clip nonzero character pixels")
    return frame.crop(crop).resize((size,size),Image.Resampling.LANCZOS)


def collect_frame_bounds(source:dict[str,dict],actions:tuple[str,...])->list:
    bounds=[]
    for action in actions:
        for path in source[action]['frames']:
            with Image.open(path) as im:
                if im.size!=(CANVAS,CANVAS) or im.mode!='RGBA':
                    raise ValueError("Source sprite not 512px RGBA: "+str(path))
                bbox=im.getchannel('A').getbbox()
                if bbox is None:
                    raise ValueError("Empty sprite: "+str(path))
                bounds.append(bbox)
    return bounds
