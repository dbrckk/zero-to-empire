"""Deterministic bend-aware texture deformation for 2D IK character limbs.

Inverse mapping of an atlas piece onto a mildly curved strip. No generative calls,
no identity drift and no changes to the rig's hard anatomical joint positions.
Requires Pillow and NumPy only.
"""
from __future__ import annotations
import math
from PIL import Image
import numpy as np


def signed_joint_bend(start, hinge, end, maximum=5.0):
    """Signed lateral offset in pixels, bounded by hinge deflection."""
    ux, uy = hinge[0]-start[0], hinge[1]-start[1]
    vx, vy = end[0]-hinge[0], end[1]-hinge[1]
    lu, lv = math.hypot(ux, uy), math.hypot(vx, vy)
    if lu < 1e-5 or lv < 1e-5:
        return 0.0
    cross = (ux*vy - uy*vx) / (lu*lv)
    return max(-maximum, min(maximum, cross*maximum))


def soft_limb(layer: Image.Image, texture: Image.Image, start, end,
              occupancy: float=.87, width_mul: float=1.0,
              bend_px: float=0.0, taper: float=.035) -> None:
    """Draw atlas texture along a gently curved IK bone with bilinear sampling.

    The lateral bend is zero at both skeletal endpoints and largest mid-bone.
    Unlike a straight rigid sprite this curves *the original texture pixels*.
    No source image is changed and the path is deterministic.
    """
    if layer.mode != 'RGBA' or texture.mode != 'RGBA':
        raise ValueError('Both layer and texture must be RGBA')
    if not .65 <= occupancy <= 1.1 or not .4 <= width_mul <= 1.5:
        raise ValueError('Invalid limb dimensions')
    if not math.isfinite(bend_px) or abs(bend_px) > 7:
        raise ValueError('Unsafe texture bend')
    dx,dy=end[0]-start[0],end[1]-start[1]
    dist=math.hypot(dx,dy)
    if not math.isfinite(dist) or dist < 3:
        raise ValueError('Zero/invalid IK segment')
    ux,uy=dx/dist,dy/dist
    nx,ny=uy,-ux
    height=max(2,round(dist/occupancy))
    width=max(2,round(height*texture.width/texture.height*width_mul))
    scaled=np.asarray(texture.resize((width,height),Image.Resampling.LANCZOS),dtype=np.float32)/255.0
    # Original rigid layout places top of the image 7% above joint A.
    head=-.07*height
    tail=.93*height
    p0=(start[0]+ux*head,start[1]+uy*head)
    p1=(start[0]+ux*tail,start[1]+uy*tail)
    pad=width/2+abs(bend_px)+3
    x0=max(0,math.floor(min(p0[0],p1[0])-pad));x1=min(layer.width,math.ceil(max(p0[0],p1[0])+pad))
    y0=max(0,math.floor(min(p0[1],p1[1])-pad));y1=min(layer.height,math.ceil(max(p0[1],p1[1])+pad))
    if x0>=x1 or y0>=y1:
        return
    yy,xx=np.mgrid[y0:y1,x0:x1].astype(np.float32)
    xx+=.5-start[0];yy+=.5-start[1]
    along=xx*ux+yy*uy
    side=xx*nx+yy*ny
    t=along/dist
    along_clipped=np.clip(t,0,1)
    bulge=bend_px*np.sin(np.pi*along_clipped)
    width_factor=1-taper*(2*along_clipped-1)**2
    src_x=(side-bulge)/width_factor+(width-1)/2
    src_y=along-head
    valid=(src_x>=0)&(src_x<=width-1)&(src_y>=0)&(src_y<=height-1)
    xi=np.clip(np.floor(src_x).astype(np.int32),0,width-1)
    yi=np.clip(np.floor(src_y).astype(np.int32),0,height-1)
    xj=np.minimum(xi+1,width-1)
    yj=np.minimum(yi+1,height-1)
    wx=np.clip(src_x-xi,0,1)[...,None]
    wy=np.clip(src_y-yi,0,1)[...,None]
    # Premultiplied-alpha bilinear filtering avoids dark seams/haloes.
    rgba=scaled.copy()
    rgba[...,:3]*=rgba[...,3:4]
    sampled=((1-wx)*(1-wy)*rgba[yi,xi]+wx*(1-wy)*rgba[yi,xj]
             +(1-wx)*wy*rgba[yj,xi]+wx*wy*rgba[yj,xj])
    alpha=sampled[...,3:4]
    rgb=np.divide(sampled[...,:3],np.maximum(alpha,1e-6))
    sampled=np.concatenate((rgb,alpha),axis=-1)
    sampled*=valid[...,None]
    pixels=np.uint8(np.clip(np.round(sampled*255),0,255))
    patch=Image.fromarray(pixels,'RGBA')
    layer.alpha_composite(patch,(x0,y0))
