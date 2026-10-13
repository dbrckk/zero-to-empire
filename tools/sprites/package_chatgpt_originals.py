#!/usr/bin/env python3
"""Package first-party editable role sprites for *read-only* Android review.

Only the 18 already-committed original candidate atlases are consumed. No new
images or external model calls, no copies to Android res/, no strict promotion.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path
import zipfile

from PIL import Image

ROLES = ("OP", "LOG", "ENG")
ACTIONS = {"IDLE": 6, "WALK": 8, "WORK": 10, "CARRY": 8, "REPAIR": 10, "CELEB": 8}


def make_bundle(source: Path, output: Path) -> dict:
    original=json.loads((source/"creation-manifest.json").read_text(encoding="utf8"))
    expected={f"CHR-{role}-{action}" for role in ROLES for action in ACTIONS}
    if (not original.get("review_only")
        or original.get("strict_done_added")!=0
        or {row.get("id") for row in original.get("assets",[])}!=expected
        or len(original.get("assets",[]))!=18):
        raise ValueError("Unsafe original candidate manifest: exact 18 review-only IDs required")
    output.parent.mkdir(parents=True,exist_ok=True)
    rows=[]
    svg_count=0
    with zipfile.ZipFile(output,"w",zipfile.ZIP_DEFLATED,compresslevel=8) as archive:
        for role in ROLES:
            for action,count in ACTIONS.items():
                ident=f"CHR-{role}-{action}"
                name=f"zte_chr_{role.lower()}_{action.lower()}_final.png"
                p=source/"candidates"/name
                data=p.read_bytes()
                with Image.open(io.BytesIO(data)) as image:
                    image.load()
                    if image.format!="PNG" or image.size!=(1024,1024) or image.mode!="RGBA":
                        raise ValueError(f"Bad atlas: {ident}")
                archive.writestr("atlases/"+name,data)
                for frame in range(count):
                    svg=source/"src_svg"/role/action/f"{frame:02d}.svg"
                    payload=svg.read_bytes()
                    if len(payload)<200 or b"<svg" not in payload[:400]:
                        raise ValueError(f"Missing editable SVG: {ident} #{frame}")
                    archive.writestr(f"svg_source/{role}/{action}/{frame:02d}.svg",payload)
                    svg_count+=1
                rows.append({
                    "id":ident,"filename":name,"frames":count,
                    "dimensions":[1024,1024],"cell":[256,256],
                    "sha256":hashlib.sha256(data).hexdigest(),
                    "context_only":action=="IDLE" and role in ("OP","LOG"),
                    "visual_semantic_approved":False,
                    "android_runtime_approved":False,
                    "strict_done_granted":False,
                })
        report={"schema_version":1,"review_only":True,"strict_done_increased":False,
                "producer":"chatgpt-original-editable-vector-rig","entries":rows}
        archive.writestr("manifest.json",json.dumps(report,indent=2)+"\n")
        for name in ("animation-review.json","candidate-qa.json",
                     "original-review-contact-sheet.png"):
            archive.writestr(name,(source/name).read_bytes())
        for preview in sorted((source/"previews").glob("*.gif")):
            archive.writestr("previews/"+preview.name,preview.read_bytes())
    if svg_count!=150 or len(rows)!=18:
        raise ValueError("Did not archive all 18 atlases/150 source frames")
    return {"review_only":True,"atlases":len(rows),"editable_svgs":svg_count,
            "strict_done_added":0,"zip":str(output),"bytes":output.stat().st_size}


def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--source",type=Path,
                        default=Path("art/incoming/chatgpt-original"))
    parser.add_argument("--output",type=Path,required=True)
    a=parser.parse_args()
    result=make_bundle(a.source,a.output)
    print("LOCAL_CHATGPT_CANDIDATE_PACKAGE="+json.dumps(result,sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
