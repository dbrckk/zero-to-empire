#!/usr/bin/env python3
"""Promote the explicitly reviewed TER-07 v3 candidate to Android runtime.

This script is intentionally single-purpose. It refuses to generate art and only
converts the already reviewed candidate to the canonical lossless WebP target.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'art/production/ter07/zte_terrain_07_candidate_v3.png'
REPORT=ROOT/'art/production/ter07/report.json'
TARGET=ROOT/'app/src/main/res/drawable-nodpi/zte_terrain_07_final.webp'
SIDE=1024

def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):
            h.update(chunk)
    return h.hexdigest()

def validate(im:Image.Image):
    if im.mode!='RGBA' or im.size!=(SIDE,SIDE):
        raise RuntimeError(f'Unexpected TER-07 source format: {im.mode} {im.size}')
    a=im.getchannel('A')
    bbox=a.getbbox()
    if not bbox:
        raise RuntimeError('TER-07 source is empty')
    coverage=sum(a.histogram()[8:])/(SIDE*SIDE)
    margin=min(bbox[0],bbox[1],SIDE-bbox[2],SIDE-bbox[3])
    w=bbox[2]-bbox[0];h=bbox[3]-bbox[1]
    aspect=max(w,h)/max(1,min(w,h))
    if margin<78:
        raise RuntimeError(f'TER-07 safety margin regressed: {margin}')
    if not .06<=coverage<=.25:
        raise RuntimeError(f'TER-07 coverage regressed: {coverage:.3f}')
    if aspect<1.40:
        raise RuntimeError(f'TER-07 no longer reads as a connector: aspect={aspect:.2f}')
    return {'bbox':bbox,'coverage':coverage,'margin':margin,'aspect':aspect}

def main():
    if not SOURCE.is_file() or not REPORT.is_file():
        raise SystemExit('Reviewed TER-07 v3 evidence is missing')
    report=json.loads(REPORT.read_text(encoding='utf-8'))
    if report.get('revision')!='v3-premium-2.5d':
        raise SystemExit('TER-07 report does not identify reviewed v3 candidate')
    if report.get('candidate')!=str(SOURCE.relative_to(ROOT)):
        raise SystemExit('TER-07 report/source mismatch')

    im=Image.open(SOURCE).convert('RGBA')
    metrics=validate(im)
    TARGET.parent.mkdir(parents=True,exist_ok=True)
    im.save(TARGET,'WEBP',lossless=True,method=6,exact=True)

    with Image.open(TARGET) as runtime:
        runtime=runtime.convert('RGBA')
        runtime_metrics=validate(runtime)
        if runtime.tobytes()!=im.tobytes():
            raise SystemExit('Lossless TER-07 runtime bytes differ after decode')

    evidence={
        'asset_id':'TER-07',
        'source':str(SOURCE.relative_to(ROOT)),
        'source_sha256':sha256(SOURCE),
        'runtime':str(TARGET.relative_to(ROOT)),
        'runtime_sha256':sha256(TARGET),
        'source_metrics':metrics,
        'runtime_metrics':runtime_metrics,
        'status':'RUNTIME_PENDING_ANDROID_CI',
    }
    out=ROOT/'art/production/ter07/runtime-promotion-v3.json'
    out.write_text(json.dumps(evidence,indent=2),encoding='utf-8')
    print('TER07_RUNTIME_PROMOTED='+str(TARGET.relative_to(ROOT)))
    print('TER07_RUNTIME_SHA256='+evidence['runtime_sha256'])

if __name__=='__main__':
    main()
