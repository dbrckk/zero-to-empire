"""Conservative recovery of one full-body subject from two-person role anchors.

Works only on a known foreground segmentation mask. Never guesses a person's
identity, invents limbs or marks assets approved. Ambiguous overlaps remain
rejected and recorded rather than silently generating unusable role families.
"""
from __future__ import annotations

from collections import deque
from PIL import Image


def _components(mask: Image.Image):
    thumb=mask.convert("L").resize((256,256),Image.Resampling.NEAREST)
    data=thumb.load()
    seen=set()
    found=[]
    for y in range(256):
        for x in range(256):
            if data[x,y]<48 or (x,y) in seen:
                continue
            queue=deque([(x,y)])
            seen.add((x,y))
            area=0
            bounds=[x,y,x+1,y+1]
            while queue:
                px,py=queue.popleft()
                area+=1
                bounds[0]=min(bounds[0],px)
                bounds[1]=min(bounds[1],py)
                bounds[2]=max(bounds[2],px+1)
                bounds[3]=max(bounds[3],py+1)
                for xx,yy in ((px-1,py),(px+1,py),(px,py-1),(px,py+1)):
                    if 0<=xx<256 and 0<=yy<256 and data[xx,yy]>=48 and (xx,yy) not in seen:
                        seen.add((xx,yy))
                        queue.append((xx,yy))
            found.append((area,tuple(bounds)))
    return sorted(found,key=lambda pair:pair[0],reverse=True)


def salvage_two_full_body_subjects(raw:Image.Image, isolated:Image.Image):
    """Return (RGB isolated character, evidence) or (None, rejection reason).

    This is deliberately narrow: two similarly sized, distinct, tall and
    horizontally separated foreground components must be visible. An
    overlapping double person or a disconnected machine is not recoverable.
    """
    rgb=raw.convert("RGB")
    if rgb.size!=(1024,1024) or isolated.size!=rgb.size:
        return None,"unsupported-anchor-size"
    pairs=_components(isolated.getchannel("A"))
    if len(pairs)<2:
        return None,"no-independent-full-body-pair"
    (first_n,first),(second_n,second)=pairs[:2]
    if first_n<1500 or second_n<first_n*.35:
        return None,"secondary-component-not-a-full-body-person"
    for box in (first,second):
        width=box[2]-box[0]
        height=box[3]-box[1]
        if height<130 or width<14 or width/max(height,1)>1.08:
            return None,"multi-subject-parts-not-two-tall-figures"
    # Avoid cropping a second worker or important overlapping object.
    if not (first[2]+3<second[0] or second[2]+3<first[0]):
        return None,"overlapping-two-subjects-unsafe-to-split"

    # Keep only the dominant full-height connected figure (ties go to the
    # leftmost subject). Preserve its painterly pixels with no new synthesis.
    chosen=first if first_n>second_n else min(first,second,key=lambda b:b[0])
    scale=4
    pad=12
    left=max(0,chosen[0]*scale-pad)
    top=max(0,chosen[1]*scale-pad)
    right=min(1024,chosen[2]*scale+pad)
    bottom=min(1024,chosen[3]*scale+pad)
    if left<18 or top<18 or right>1006 or bottom>1006:
        return None,"source-figure-clipped-at-image-border"
    region=rgb.crop((left,top,right,bottom))
    if region.width>850 or region.height>850:
        return None,"source-figure-lacks-safe-framing"

    # Median-of-corners neutral background approximates the original source
    # without adding a second actor, halo, or painted prop.
    corners=(rgb.getpixel((0,0)),rgb.getpixel((1023,0)),
             rgb.getpixel((0,1023)),rgb.getpixel((1023,1023)))
    bg=tuple(sorted(pixel[k] for pixel in corners)[1:3][0] for k in range(3))
    canvas=Image.new("RGB",(1024,1024),bg)
    x=(1024-region.width)//2
    y=(1024-region.height)//2
    canvas.paste(region,(x,y))
    return canvas,{
        "strategy":"one-connected-full-body-figure-from-side-by-side-pair",
        "discarded_second_subject":True,
        "largest_component_pixels":first_n,
        "second_component_pixels":second_n,
        "chosen_source_bbox":list(chosen),
        "semantic_approval":False,
    }
