#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from collections import deque
from pathlib import Path
from PIL import Image

ALPHA=8
CHR_RE=re.compile(r"^CHR-(OP|TECH|LOG|ENG)-(IDLE|WALK|WORK|CARRY|REPAIR|CELEB)$")
CHR_FRAMES={"IDLE":6,"WALK":8,"WORK":10,"CARRY":8,"REPAIR":10,"CELEB":8}

def major_components(alpha: Image.Image)->int:
    small=alpha.resize((128,128),Image.Resampling.BILINEAR)
    px=small.load(); seen=set(); major=0; min_area=int(128*128*.012)
    for y in range(128):
        for x in range(128):
            if (x,y) in seen or px[x,y] < 32: continue
            q=deque([(x,y)]); seen.add((x,y)); area=0
            while q:
                cx,cy=q.popleft(); area+=1
                for nx,ny in ((cx-1,cy),(cx+1,cy),(cx,cy-1),(cx,cy+1)):
                    if 0<=nx<128 and 0<=ny<128 and (nx,ny) not in seen and px[nx,ny]>=32:
                        seen.add((nx,ny)); q.append((nx,ny))
            if area>=min_area: major+=1
    return major

def validate(asset_id:str,path:Path)->dict:
    issues=[]
    if not path.is_file() or path.stat().st_size==0:
        return {"id":asset_id,"file":str(path),"pass":False,"issues":["missing-runtime"]}
    try: im=Image.open(path).convert("RGBA")
    except Exception as e:
        return {"id":asset_id,"file":str(path),"pass":False,"issues":["decode-failed:"+str(e)]}
    a=im.getchannel("A"); lo,hi=a.getextrema()
    if hi==0: issues.append("empty-alpha")
    if lo==255: issues.append("no-transparency")

    if asset_id.startswith("FX-"):
        if im.size!=(512,256): issues.append(f"bad-size:{im.width}x{im.height}")
        if im.size==(512,256):
            for i in range(8):
                x0=(i%4)*128; y0=(i//4)*128
                cell=a.crop((x0,y0,x0+128,y0+128))
                if cell.getbbox() is None:
                    issues.append(f"frame-{i}-empty"); continue
                edges=(cell.crop((0,0,128,4)),cell.crop((0,124,128,128)),cell.crop((0,0,4,128)),cell.crop((124,0,128,128)))
                if any(e.getbbox() is not None for e in edges): issues.append(f"frame-{i}-padding")
    elif (m:=CHR_RE.fullmatch(asset_id)):
        if im.size!=(1024,1024): issues.append(f"bad-size:{im.width}x{im.height}")
        if im.size==(1024,1024):
            expected=CHR_FRAMES[m.group(2)]
            for i in range(16):
                x0=(i%4)*256; y0=(i//4)*256
                cell=a.crop((x0,y0,x0+256,y0+256)); bb=cell.getbbox()
                if i<expected:
                    if bb is None: issues.append(f"frame-{i}-empty"); continue
                    h=cell.histogram(); cov=sum(h[8:])/(256*256)
                    if not .10<=cov<=.48: issues.append(f"frame-{i}-coverage:{cov:.3f}")
                    edges=(cell.crop((0,0,256,8)),cell.crop((0,248,256,256)),cell.crop((0,0,8,256)),cell.crop((248,0,256,256)))
                    if any(e.getbbox() is not None for e in edges): issues.append(f"frame-{i}-padding")
                elif bb is not None:
                    issues.append(f"unused-cell-{i}-not-empty")
    else:
        if im.width!=im.height: issues.append("non-square-runtime")
        if min(im.size)<512 or max(im.size)>2048: issues.append(f"bad-size:{im.width}x{im.height}")
        hist=a.histogram(); coverage=sum(hist[ALPHA:])/(im.width*im.height)
        if coverage>.70: issues.append(f"coverage-too-high:{coverage:.3f}")
        comps=major_components(a)
        if comps>1: issues.append(f"multiple-major-components:{comps}")
        if any(a.getpixel(pt)!=0 for pt in ((0,0),(im.width-1,0),(0,im.height-1),(im.width-1,im.height-1))):
            issues.append("nontransparent-corner")
    return {"id":asset_id,"file":str(path),"size":list(im.size),"bytes":path.stat().st_size,"pass":not issues,"issues":issues}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--asset-id",required=True)
    ap.add_argument("--path",required=True,type=Path)
    ap.add_argument("--report",type=Path)
    a=ap.parse_args()
    result=validate(a.asset_id,a.path)
    print(json.dumps(result,indent=2))
    if a.report:
        a.report.parent.mkdir(parents=True,exist_ok=True)
        a.report.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    if not result["pass"]: raise SystemExit(1)

if __name__=="__main__": main()
