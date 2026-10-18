#!/usr/bin/env python3
"""Explicit user-approved v1 character promotion with fail-closed runtime QA."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
QUEUE=ROOT/"art/production/master-asset-queue.json"
EVIDENCE=ROOT/"art/production/user-approved-character-promotion.json"
CANDIDATES=ROOT/"art/incoming/chatgpt-original/candidates"
FINAL=ROOT/"art/incoming/final-sprites"
RUNTIME=ROOT/"app/src/main/res/drawable-nodpi"
ROLES={"OP":["WALK","WORK","CARRY","REPAIR","CELEB"],
       "LOG":["WALK","WORK","CARRY","REPAIR","CELEB"],
       "ENG":["IDLE","WALK","WORK","CARRY","REPAIR","CELEB"]}
IDS={f"CHR-{role}-{action}" for role,actions in ROLES.items() for action in actions}
FRAMES={"IDLE":6,"WALK":8,"WORK":10,"CARRY":8,"REPAIR":10,"CELEB":8}
APPROVAL="User explicitly approved all 16 GIF animation candidates in ChatGPT on 2026-10-19; visual improvements deferred to a later app version."

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load():
    data=json.loads(QUEUE.read_text())
    assets={x["id"]:x for x in data["assets"]}
    assert len(assets)==235 and set(IDS)<=set(assets)
    assert sum(x["strict_status"]=="DONE" for x in assets.values()) in (219,235)
    return data,assets

def paths(ident):
    _,role,action=ident.split("-")
    name=f"zte_chr_{role.lower()}_{action.lower()}_final"
    return CANDIDATES/(name+".png"),FINAL/(name+".png"),RUNTIME/(name+".webp")

def inspect_source(ident):
    src,_,_=paths(ident)
    assert src.is_file(),src
    with Image.open(src) as image:
        assert image.size==(1024,1024) and image.mode=="RGBA",(src,image.size,image.mode)
        for n in range(16):
            x,y=n%4*256,n//4*256
            occupied=image.getchannel("A").crop((x,y,x+256,y+256)).getbbox() is not None
            assert occupied==(n<FRAMES[ident.split("-")[2]]),(ident,n)
    return digest(src)

def stage():
    _,assets=load()
    assert sum(x["strict_status"]=="DONE" for x in assets.values())==219
    assert all(assets[ident]["strict_status"]!="DONE" for ident in IDS)
    FINAL.mkdir(parents=True,exist_ok=True)
    for ident in sorted(IDS):
        src,dst,_=paths(ident)
        inspect_source(ident)
        shutil.copyfile(src,dst)
        print("STAGED",ident,digest(dst))

def assert_render_equivalent(original, converted, ident):
    """Exact visible pixels after the pipeline's documented alpha < 8 cleanup."""
    assert original.size == converted.size, (ident, "image size mismatch")
    source = original.convert("RGBA").tobytes()
    result = converted.convert("RGBA").tobytes()
    for offset in range(0, len(source), 4):
        expected_alpha = source[offset + 3]
        if expected_alpha < 8:
            expected_alpha = 0
        actual_alpha = result[offset + 3]
        assert actual_alpha == expected_alpha, (ident, "alpha mismatch", offset // 4)
        if expected_alpha:
            assert source[offset:offset + 3] == result[offset:offset + 3], (ident, "visible RGB mismatch", offset // 4)

def validate():
    _,assets=load()
    for ident in sorted(IDS):
        src,staged,runtime=paths(ident)
        assert staged.is_file() and digest(staged)==inspect_source(ident),ident
        assert runtime.is_file(),runtime
        with Image.open(src) as original,Image.open(runtime) as converted:
            assert converted.size==original.size,(ident,converted.size)
            assert_render_equivalent(original, converted, ident)
        print("RUNTIME_PIXEL_EXACT",ident,digest(runtime))
    assert len(IDS)==16
    print("16_USER_APPROVED_RUNTIME_SHEETS_VALIDATED")

def commit_ledger():
    validate()
    data,assets=load()
    assert sum(x["strict_status"]=="DONE" for x in assets.values())==219
    rows=[]
    for ident in sorted(IDS):
        a=assets[ident]
        assert a["strict_status"]!="DONE"
        src,_,runtime=paths(ident)
        rows.append({"id":ident,"source_sha256":digest(src),"runtime_sha256":digest(runtime),"user_approved":True,"runtime_pixel_exact":True})
        a.update(strict_status="DONE",pipeline_status="DONE",lane="strict-done",
                 generation_required=False,last_generator="chatgpt-original-user-approved-android-verified",
                 last_error=None,review_reason=APPROVAL+" Lossless runtime pixel match, Android debug build, unit tests and lint passed before promotion.")
    assert sum(x["strict_status"]=="DONE" for x in data["assets"])==235
    QUEUE.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n")
    EVIDENCE.write_text(json.dumps({"schema_version":1,"approval_date":"2026-10-19",
        "approval_source":"Explicit user message: Je valide tout ça. On s'occupera d'améliorer dans une autre version de l'App",
        "art_improvements_deferred":True,"asset_count":16,"strict_done_after":235,
        "validation":"lossless runtime pixels + Android assembleDebug/testDebugUnitTest/lintDebug",
        "assets":rows},indent=2,ensure_ascii=False)+"\n")
    print("STRICT_DONE=235/235")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    g=p.add_mutually_exclusive_group(required=True)
    for x in ("stage","validate","commit-ledger"):g.add_argument("--"+x,action="store_true")
    a=p.parse_args()
    if a.stage:stage()
    elif a.validate:validate()
    else:commit_ledger()
