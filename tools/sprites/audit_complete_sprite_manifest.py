#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
MASTER=ROOT/'art/production/master-asset-queue.json'
sys.path.insert(0,str((ROOT/'tools/sprites').resolve()))
from validate_runtime_asset import validate

EXPECTED_ROWS=236


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--allow-pending',action='store_true',help='Validate DONE rows while allowing planned non-DONE manifest targets.')
    args=ap.parse_args()

    rows=[]
    for line in MANIFEST.read_text(encoding='utf-8').splitlines():
        if not line.startswith('|') or 'app/src/main/res/' not in line: continue
        cols=[c.strip() for c in line.split('|')[1:-1]]
        if len(cols)==5: rows.append(cols)
    if len(rows)!=EXPECTED_ROWS:
        raise SystemExit(f'Expected {EXPECTED_ROWS} canonical sprite rows, got {len(rows)}')
    queue=json.loads(MASTER.read_text(encoding='utf-8'))
    assets=queue.get('assets',[])
    ids=[a.get('id') for a in assets]
    excluded=set(queue.get('excluded_from_target',[]))
    manifest_ids=[row[0] for row in rows]
    if (queue.get('target_total')!=235 or len(assets)!=235 or
            len(set(ids))!=235 or len(set(manifest_ids))!=EXPECTED_ROWS or
            excluded!={'ONB-00'} or
            set(manifest_ids)!=(set(ids)|excluded) or set(ids)&excluded):
        raise SystemExit('Canonical 235-target queue and 236-row runtime manifest disagree')
    strict_by_id={a['id']:a.get('strict_status') for a in assets}
    premature=[r[0] for r in rows
               if r[0] in strict_by_id and r[4].upper()=='DONE'
               and strict_by_id[r[0]]!='DONE']
    pending=[r[0] for r in rows
             if r[4].upper()!='DONE' or
             (r[0] in strict_by_id and strict_by_id[r[0]]!='DONE')]
    if pending:
        print(f'SPRITE_COMPLETION_PENDING={len(pending)}')
        print(f'MANIFEST_PREMATURE_DONE={len(premature)}')
        if not args.allow_pending:
            raise SystemExit(3)

    seen=set(); report=[]; failed=[]
    for aid,name,desc,runtime,status in rows:
        p=Path(runtime.replace(chr(96),''))
        if str(p) in seen:
            failed.append({'id':aid,'issues':['duplicate-runtime-path']});continue
        seen.add(str(p))
        if aid in pending:
            continue
        r=validate(aid,p)
        report.append(r)
        if not r['pass']: failed.append(r)
    out=ROOT/'art/production/final-sprite-completion-audit.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps({'total':len(rows),'strict_target':235,
                               'strict_done':sum(v=='DONE' for v in strict_by_id.values()),
                               'pending':pending,'premature_manifest_done':premature,
                               'failed':failed,'assets':report},indent=2),encoding='utf-8')
    if failed:
        for item in failed:
            print('FINAL_SPRITE_AUDIT_FAILURE='+json.dumps(item,sort_keys=True))
        raise SystemExit('Final sprite audit failures: '+','.join(r['id'] for r in failed))
    print(f'FINAL_SPRITE_AUDIT_PASS={len(rows)-len(pending)}/{len(rows)}')

if __name__=='__main__':main()
