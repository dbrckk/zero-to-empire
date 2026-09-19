#!/usr/bin/env python3
"""Master queue mutations used by the asset autofactory."""
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
Q=ROOT/'art/production/master-asset-queue.json'

def main():
 p=argparse.ArgumentParser();p.add_argument('--status',required=True);p.add_argument('--assets',required=True);p.add_argument('--increment-attempts',action='store_true');a=p.parse_args()
 d=json.loads(Q.read_text(encoding='utf-8')); ids={x for x in a.assets.split(',') if x}
 found=set()
 for x in d['assets']:
  if x['id'] in ids:
   x['status']=a.status
   if a.increment_attempts:x['attempts']=int(x.get('attempts',0))+1
   found.add(x['id'])
 missing=ids-found
 if missing:raise SystemExit('unknown assets: '+','.join(sorted(missing)))
 Q.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
 print(f'MASTER_QUEUE_UPDATED={len(found)} status={a.status}')
if __name__=='__main__':main()
