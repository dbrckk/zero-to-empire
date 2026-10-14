"""Deterministic alpha-safe material lighting for ChatGPT original sprite rig.

All work is local, editable and repeatable. The operation does not change
pixel alpha, silhouette, timing, frame pivots or candidate review status.
"""
from __future__ import annotations
from functools import lru_cache
from PIL import Image, ImageChops, ImageFilter

CELL=256

@lru_cache(maxsize=1)
def _lighting_fields():
    warm=Image.new("RGB",(CELL,CELL))
    cool=Image.new("RGB",(CELL,CELL))
    top=Image.new("L",(CELL,CELL))
    wp=[];cp=[];tp=[]
    for y in range(CELL):
        for x in range(CELL):
            lx=(CELL-1-x)/(CELL-1)
            ly=(CELL-1-y)/(CELL-1)
            w=max(0.0,1.0-((x-63)**2/(210**2)+(y-31)**2/(276**2)))
            c=max(0.0,(x-124)/150)*.7
            wp.append((round(17*w),round(10*w),round(4*w)))
            cp.append((round(1*c),round(6*c),round(12*c)))
            tp.append(round(248-24*(1-lx)-13*(1-ly)))
    warm.putdata(wp)
    cool.putdata(cp)
    top.putdata(tp)
    return warm,cool,top

def finish_frame(frame:Image.Image)->Image.Image:
    """Apply restrained warm key, cool bounce and alpha-edge rim to RGBA frame."""
    if frame.size!=(CELL,CELL):
        raise ValueError("Expected RGBA 256x256 frame")
    src=frame.convert("RGBA")
    alpha=src.getchannel("A")
    if not alpha.getbbox():
        return src.copy()
    warm,cool,top=_lighting_fields()
    rgb=src.convert("RGB")
    light=ImageChops.multiply(rgb,Image.merge("RGB",(top,top,top)))
    light=ImageChops.add(light,warm,scale=1.0,offset=0)
    light=ImageChops.add(light,cool,scale=1.0,offset=0)
    displaced=ImageChops.offset(alpha,2,1)
    rim=ImageChops.subtract(alpha,displaced).filter(ImageFilter.GaussianBlur(.75))
    rim=rim.point(lambda px:min(255,round(px*.23)))
    rim_color=Image.new("RGB",(CELL,CELL),(246,210,169))
    light=Image.composite(rim_color,light,rim)
    out=light.convert("RGBA")
    out.putalpha(alpha)
    return out
