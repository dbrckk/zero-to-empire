#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
sys.path.insert(0,str((ROOT/'tools/sprites').resolve()))
from validate_runtime_asset import validate

def main():
    rows=[]
    for line in MANIFEST.read_text(encoding='utf-8').splitlines():
        if not line.startswith('|') or 'app/src/main/res/' not in line: continue
        cols=[c.strip() for c in line.split('|')[1:-1]]
        if len(cols)==5: rows.append(cols)
    if len(rows)!=235:
        raise SystemExit(f'Expected 235 canonical sprite rows, got {len(rows)}')
    pending=[r[0] for r in rows if r[4].upper()!='DONE']
    if pending:
        print(f'SPRITE_COMPLETION_PENDING={len(pending)}')
        raise SystemExit(3)
    seen=set(); report=[]; failed=[]
    for aid,name,desc,runtime,status in rows:
        p=Path(runtime.replace(chr(96),''))
        if str(p) in seen:
            failed.append({'id':aid,'issues':['duplicate-runtime-path']});continue
        seen.add(str(p))
        r=validate(aid,p)
        report.append(r)
        if not r['pass']: failed.append(r)
    out=ROOT/'art/production/final-sprite-completion-audit.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps({'total':len(rows),'failed':failed,'assets':report},indent=2),encoding='utf-8')
    if failed:
        raise SystemExit('Final sprite audit failures: '+','.join(r['id'] for r in failed))
    print('FINAL_SPRITE_AUDIT_PASS=235')

if __name__=='__main__':main()
