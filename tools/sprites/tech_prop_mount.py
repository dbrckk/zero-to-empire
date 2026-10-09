"""Physical support brackets for TECH interaction props (512px rig coordinates).

WORK's console and REPAIR's service panel were visually floating. Both
now have deterministic folding mounts running from the technician's belt
to a socket *inside* the associated prop.

This is lightweight 2D staging, not a simulated rig or visual approval.
"""
from __future__ import annotations

import math
from PIL import Image, ImageDraw

SUPPORTS = {
    "WORK": ((11.0, -47.0), (28.0, -25.0), (38.0, -39.0)),
    "REPAIR": ((11.0, -44.0), (43.0, -20.0), (77.0, -32.0)),
}
# Bounds of the static graphics as painted in rigged_tech_actions_v3.py.
PANEL_BOUNDS = {
    "WORK": (26.0, -83.0, 115.0, -32.0),
    "REPAIR": (62.0, -105.0, 123.0, -26.0),
}


def mount_geometry(action: str, root: tuple[float,float]) -> dict:
    """Expose geometry for scene/contact assertions and compositor reuse."""
    if action not in SUPPORTS:
        raise ValueError("Unsupported prop support")
    if len(root) != 2 or not all(math.isfinite(v) for v in root):
        raise ValueError("Non-finite body pivot")
    x,y=root
    offsets=SUPPORTS[action]
    points=tuple((x+dx,y+dy) for dx,dy in offsets)
    distances=[math.dist(a,b) for a,b in zip(points,points[1:])]
    if any(not 9 <= d <= 65 for d in distances):
        raise ValueError("Unreachable support bracket")
    lo_x,lo_y,hi_x,hi_y=PANEL_BOUNDS[action]
    end=points[-1]
    if not(x+lo_x<=end[0]<=x+hi_x and y+lo_y<=end[1]<=y+hi_y):
        raise ValueError("Mount socket outside device")
    if math.dist(points[0],(x+11,y-47 if action=="WORK" else y-44))>.001:
        raise ValueError("Mount disconnected from belt")
    return {
        "action":action,
        "belt_socket":points[0],
        "hinge":points[1],
        "device_socket":points[2],
        "segment_lengths_px":tuple(round(d,3) for d in distances),
        "all_links_connected":True,
        "same_rig_origin":True,
    }


def draw_mount(layer:Image.Image,pose:dict,action:str)->dict:
    """Draw as prop underlay so the torso naturally occludes its belt socket."""
    if layer.mode!="RGBA" or layer.size!=(512,512):
        raise ValueError("Mount requires a 512px RGBA underlay")
    geo=mount_geometry(action,pose["root"])
    p0,p1,p2=(geo[k] for k in ("belt_socket","hinge","device_socket"))
    def pix(p):return (round(p[0]),round(p[1]))
    d=ImageDraw.Draw(layer,"RGBA")
    coords=[pix(p0),pix(p1),pix(p2)]
    d.line(coords,fill=(7,16,26,240),width=14,joint="curve")
    d.line(coords,fill=(54,70,84,245),width=9,joint="curve")
    d.line(coords,fill=(137,156,170,180),width=2,joint="curve")
    # Parallel power conductor with a limited cyan reflection.
    for a,b in zip(coords,coords[1:]):
        d.line([(a[0],a[1]-3),(b[0],b[1]-3)],
               fill=(15,96,120,150),width=2)
    for n,p in enumerate(coords):
        r=9 if n==1 else 7
        d.ellipse((p[0]-r,p[1]-r,p[0]+r,p[1]+r),
                  fill=(29,44,56,248),
                  outline=(113,140,155,235),width=2)
        d.ellipse((p[0]-2,p[1]-2,p[0]+2,p[1]+2),
                  fill=(39,200,221,215) if n==1 else (124,140,153,210))
    return geo
