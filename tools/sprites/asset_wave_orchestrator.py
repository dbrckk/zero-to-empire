#!/usr/bin/env python3
"""Plan the next safe asset-production wave toward 235/236 strict DONE.

This planner NEVER promotes art. It only chooses generation/reconciliation work.
Historical manifest DONE flags are intentionally ignored until strict evidence is normalized.
"""
from __future__ import annotations
import argparse,json,re
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
QUEUE=ROOT/'art/production/master-asset-queue.json'
PROGRESS=ROOT/'docs/art/FINAL_AAA_SPRITE_PROGRESS.md'
BUILDING_QUEUE=ROOT/'art/production/controlled-building-regen-queue.json'
CHAR_QUEUE=ROOT/'art/production/controlled-character-regen-queue.json'

STRICT_RE=re.compile(r'DONE:\s*\*\*(\d+)\s*/\s*(\d+)\*\*')

def strict_progress():
    m=STRICT_RE.search(PROGRESS.read_text(encoding='utf-8'))
    if not m: raise SystemExit('cannot parse trusted strict progress')
    return int(m.group(1)),int(m.group(2))

def controlled_ids(path):
    if not path.is_file(): return set()
    d=json.loads(path.read_text(encoding='utf-8'))
    return {str(x.get('id','')).upper() for x in d.get('targets',[]) if str(x.get('status','')).upper() not in {'DONE','APPROVED'}}

def choose(q):
    done,total=strict_progress()
    target=int(q.get('target_strict_done',235))
    if done>=target:
        return {'action':'STOP','reason':f'target reached: {done}/{total}','strict_done':done,'scope':total}

    active_build=controlled_ids(BUILDING_QUEUE)
    active_char=controlled_ids(CHAR_QUEUE)
    if active_build:
        fam=sorted({x.rsplit('-T',1)[0] for x in active_build if x.startswith('BLD-')})
        return {'action':'WAIT_OR_CONTINUE_EXISTING','lane':'building-family','families':fam,'strict_done':done,'target':target}
    if active_char:
        return {'action':'WAIT_OR_CONTINUE_EXISTING','lane':'character-atlas','assets':sorted(active_char),'strict_done':done,'target':target}

    pending=[a for a in q['assets'] if a.get('status') in {'PENDING','RECONCILE','REJECTED','BLOCKED'} and a.get('attempts',0)<a.get('max_attempts',5)]
    pending.sort(key=lambda a:(a.get('priority',99),a['id']))
    if not pending:
        return {'action':'STOP','reason':'no automatically eligible work remains','strict_done':done,'target':target}

    first=pending[0]
    lane=first['lane']
    if lane=='building-family':
        family=first['family']
        assets=[a['id'] for a in pending if a['lane']==lane and a.get('family')==family]
        return {'action':'QUEUE','lane':lane,'family':family,'assets':assets[:7],'strict_done':done,'target':target}
    if lane=='character-atlas':
        role=first.get('family')
        assets=[a['id'] for a in pending if a['lane']==lane and a.get('family')==role]
        return {'action':'QUEUE','lane':lane,'role':role,'assets':assets[:4],'strict_done':done,'target':target}
    assets=[a['id'] for a in pending if a['lane']==lane][:8]
    return {'action':'QUEUE','lane':lane,'assets':assets,'strict_done':done,'target':target}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--github-output',action='store_true');args=ap.parse_args()
    q=json.loads(QUEUE.read_text(encoding='utf-8'))
    plan=choose(q)
    print(json.dumps(plan,indent=2))
    if args.github_output:
        import os
        p=Path(os.environ['GITHUB_OUTPUT'])
        with p.open('a',encoding='utf-8') as f:
            f.write('plan='+json.dumps(plan,separators=(',',':'))+'\n')
            f.write('action='+plan['action']+'\n')
            f.write('lane='+str(plan.get('lane',''))+'\n')
            f.write('assets='+','.join(plan.get('assets',[]))+'\n')
            f.write('family='+str(plan.get('family',''))+'\n')
if __name__=='__main__': main()
