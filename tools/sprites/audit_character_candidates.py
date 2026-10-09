#!/usr/bin/env python3
"""Audit actual canonical character sprite sheets and render contact evidence.

Never grants artistic approval. Uses original PNG candidates in art/incoming;
a TECH preview from a separate generator cannot overwrite canonical evidence.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
from PIL import Image, ImageDraw
from character_review_matrix import build

ROOT=Path(__file__).resolve().parents[2]
ACTION_FRAMES={"IDLE":8,"WALK":8,"WORK":12,"CARRY":8,"REPAIR":12,"CELEB":10}


def inspect(path:Path,asset_id:str)->dict:
    role,action=asset_id.split("-")[1:]
    expected=ACTION_FRAMES[action]
    result={"asset_id":asset_id,"source_path":str(path),"exists":path.is_file(),
            "expected_frames":expected,"strict_status":"NEEDS_REVIEW",
            "semantic_approved":False,"visual_approved":False,
            "technical_pass":False,"findings":[]}
    if not path.is_file():
        result["findings"].append("MISSING_CANONICAL_CANDIDATE")
        return result
    result["source_sha256"]=hashlib.sha256(path.read_bytes()).hexdigest()
    try:
        with Image.open(path) as img:
            img.load()
            result["dimensions"]=list(img.size)
            result["mode"]=img.mode
            result["format"]=img.format
            if img.mode not in ("RGBA","LA","P"):
                result["findings"].append("NO_ALPHA_MODE")
            w,h=img.size
            if w%4 or w<4*64 or h<64:
                result["findings"].append("INVALID_GRID_GEOMETRY")
                return result
            cell=w//4
            if h%cell:
                result["findings"].append("NON_SQUARE_CELLS")
                return result
            rows=h//cell
            capacity=4*rows
            result["cell_size"]=cell
            result["capacity"]=capacity
            if capacity<expected or capacity>=expected+4:
                result["findings"].append("FRAME_CAPACITY_MISMATCH")
            rgba=img.convert("RGBA")
            alpha=rgba.getchannel("A")
            result["alpha_extrema"]=list(alpha.getextrema())
            metrics=[]
            for i in range(expected):
                if i>=capacity:break
                x=(i%4)*cell;y=(i//4)*cell
                frame=rgba.crop((x,y,x+cell,y+cell))
                mask=frame.getchannel("A")
                box=mask.getbbox()
                if not box:
                    result["findings"].append(f"EMPTY_FRAME_{i}")
                    continue
                l,t,r,b=box
                margin=min(l,t,cell-r,cell-b)
                metrics.append({"frame":i,"bbox":[l,t,r,b],"margin":margin,
                                "width_ratio":round((r-l)/cell,4),
                                "height_ratio":round((b-t)/cell,4)})
                if margin<2:result["findings"].append(f"EDGE_CLIPPING_RISK_{i}")
            result["frame_metrics"]=metrics
            result["technical_pass"]=not result["findings"] and len(metrics)==expected
    except Exception as exc:
        result["findings"].append("UNREADABLE_IMAGE_"+type(exc).__name__)
    return result


def contact(rows:list[dict],output:Path)->None:
    thumb=112
    canvas=Image.new("RGB",(800,len(rows)*148+50),(19,27,39))
    d=ImageDraw.Draw(canvas)
    d.text((14,14),"CANONICAL CHARACTER CANDIDATES — REVIEW ONLY",fill=(227,239,251))
    for i,row in enumerate(rows):
        y=50+i*148
        d.text((10,y+8),row["asset_id"],fill=(224,232,243))
        d.text((10,y+27),("TECHNICAL PASS" if row["technical_pass"] else
                           ", ".join(row["findings"])[:31]),fill=(166,195,216))
        if not row["exists"]:continue
        try:
            with Image.open(row["source_path"]) as original:
                img=original.convert("RGBA")
                cell=img.width//4
                for n in range(min(5,row["expected_frames"],row.get("capacity",0))):
                    x=n%4*cell;y0=n//4*cell
                    tile=img.crop((x,y0,x+cell,y0+cell))
                    tile.thumbnail((thumb,thumb),Image.Resampling.LANCZOS)
                    ox=195+n*120+(thumb-tile.width)//2
                    oy=y+15+(thumb-tile.height)//2
                    canvas.paste(tile,(ox,oy),tile)
        except Exception:
            pass
    output.parent.mkdir(parents=True,exist_ok=True)
    canvas.save(output,optimize=True)


def main()->int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--queue",type=Path,default=ROOT/"art/production/master-asset-queue.json")
    parser.add_argument("--out",type=Path,default=Path("/tmp/character-visual-audit"))
    args=parser.parse_args()
    report=build(json.loads(args.queue.read_text(encoding="utf-8")))
    rows=[]
    for row in report["items"]:
        asset_id=row["asset_id"]
        stem="zte_chr_"+asset_id[4:].lower().replace("-","_")+"_final.png"
        source=ROOT/"art/incoming/final-sprites"/stem
        rows.append(inspect(source,asset_id))
    args.out.mkdir(parents=True,exist_ok=True)
    contact(rows,args.out/"canonical-character-contact.png")
    result={"format":"zte-canonical-character-visual-audit-v1",
            "strict_done":report["strict_done"],"pending":len(rows),
            "all_semantic_approved":False,
            "all_technical_pass":all(x["technical_pass"] for x in rows),
            "items":rows}
    (args.out/"canonical-character-audit.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("AUDIT="+str(args.out)+" PASS="+str(sum(x["technical_pass"] for x in rows))+
          "/"+str(len(rows))+" STRICT_DONE="+str(report["strict_done"]))
    return 0


if __name__=="__main__":raise SystemExit(main())
