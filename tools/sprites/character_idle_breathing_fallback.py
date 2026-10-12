"""Identity-preserving emergency IDLE breathing from a validated 256px seed.

The six poses contain *only* pixels derived from the same isolated character.
No new face, helmet, costume, limbs, objects, or shadows are painted. This is a
candidate-only fallback for a failed stochastic IDLE, not semantic approval.
"""
from __future__ import annotations

import math
from PIL import Image

FRAME_SIZE=(256,256)
PHASES=(0.0,0.65,1.0,0.65,0.0,-0.35)


def build_idle_breathing_frames(seed: Image.Image) -> list[Image.Image]:
    """Subtly expand the mid-torso while leaving the face/feet untouched."""
    if seed.size != FRAME_SIZE:
        raise ValueError("IDLE fallback requires a 256x256 isolated seed")
    base=seed.convert("RGBA")
    bb=base.getchannel("A").getbbox()
    if not bb:
        raise ValueError("Empty IDLE fallback seed")
    left,top,right,bottom=bb
    if bottom-top<125 or right-left<25 or left<4 or right>252 or bottom>247:
        raise ValueError("Unsafe IDLE fallback body bounds")
    centre=(left+right)/2
    height=bottom-top
    mask=Image.new("L",FRAME_SIZE)
    mp=mask.load()
    for y in range(FRAME_SIZE[1]):
        fraction=(y-top)/height
        if .25<=fraction<=.81:
            weight=math.sin(math.pi*(fraction-.25)/.56)**1.5
            opacity=round(255*weight)
            for x in range(FRAME_SIZE[0]):
                mp[x,y]=opacity
    frames=[]
    for phase in PHASES:
        if phase==0:
            frames.append(base.copy())
            continue
        # The geometric warp uses fractional pixels; torso-only compositing
        # protects the helmet, face, boots, and the fixed Android foot pivot.
        scale=1.0+.017*phase
        warped=base.transform(
            FRAME_SIZE,Image.Transform.AFFINE,
            (1/scale,0,centre*(1-1/scale),0,1,0),
            resample=Image.Resampling.BICUBIC
        )
        frames.append(Image.composite(warped,base,mask))
    return frames
