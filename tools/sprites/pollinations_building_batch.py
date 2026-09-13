#!/usr/bin/env python3
from __future__ import annotations
import json, os, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
PROD=ROOT/'art/production'
INCOMING=ROOT/'art/incoming/final-sprites'
RUNTIME=ROOT/'app/src/main/res/drawable-nodpi'

sys.path.insert(0,str((ROOT/'tools/sprites').resolve()))
import pollinations_building_factory as pf  # noqa

def rows():
    out=[]
    for line in MANIFEST.read_text(encoding='utf-8').splitlines():
        if not line.startswith('|') or 'app/src/main/res/' not in line: continue
        cols=[c.strip() for c in line.split('|')[1:-1]]
        if len(cols)==5 and cols[4].upper()=='TODO' and cols[0].startswith('BLD-'):
            out.append(cols)
    return out

def mark_done(asset_id:str):
    lines=MANIFEST.read_text(encoding='utf-8').splitlines()
    out=[]; changed=0
    for line in lines:
        if line.startswith('|'):
            cols=[c.strip() for c in line.split('|')[1:-1]]
            if len(cols)==5 and cols[0]==asset_id and cols[4].upper()=='TODO':
                cols[4]='DONE'; line='| '+' | '.join(cols)+' |'; changed+=1
        out.append(line)
    if changed!=1: raise RuntimeError(f'expected one TODO row for {asset_id}, changed={changed}')
    MANIFEST.write_text('\n'.join(out)+'\n',encoding='utf-8')

def run(cmd,env=None):
    return subprocess.run(cmd,cwd=ROOT,env=env,text=True,capture_output=True)

def main():
    count=max(1,min(int(os.getenv('POLLINATIONS_BATCH_COUNT','4')),6))
    attempts=max(1,min(int(os.getenv('POLLINATIONS_ATTEMPTS','3')),4))
    base=int(os.getenv('POLLINATIONS_BASE_SEED','73117'))
    PROD.mkdir(parents=True,exist_ok=True)
    summary={'requested':count,'attempts_per_target':attempts,'successes':[],'failures':[]}

    try:
        from rembg import new_session
        session=new_session('u2net')
    except Exception as e:
        raise SystemExit('rembg session init failed: '+repr(e))

    for slot in range(count):
        pending=rows()
        if not pending: break
        row=pending[0]; aid=row[0]
        ok=False
        attempts_log=[]
        for attempt in range(attempts):
            seed=(base + slot*1009 + attempt*7919) % 2147483647
            stem=None
            try:
                rp=PROD/f'pollinations-{aid.lower()}-report.json'
                out,rep=pf.generate(row,seed=seed,session=session,report_path=rp)
                stem=out.stem
                qa=PROD/f'pollinations-{aid.lower()}-qa.json'
                contact=PROD/f'pollinations-{aid.lower()}-contact.png'
                q=run([sys.executable,'tools/sprites/build_sprite_contact_sheet.py','--files',str(out.relative_to(ROOT)),'--output',str(contact.relative_to(ROOT)),'--report',str(qa.relative_to(ROOT))])
                qd=json.loads(qa.read_text()) if qa.exists() else {}
                qrows=qd.get('assets',[])
                if q.returncode or len(qrows)!=1 or not qrows[0].get('pass'):
                    attempts_log.append({'attempt':attempt+1,'seed':seed,'stage':'technical-qa','issues':qrows})
                    continue
                env=os.environ.copy(); env['SPRITE_TARGETS']=stem
                fin=run([sys.executable,'tools/sprites/process_final_sprites.py'],env=env)
                runtime=RUNTIME/f'{stem}.webp'
                if fin.returncode!=0 or not runtime.is_file():
                    attempts_log.append({'attempt':attempt+1,'seed':seed,'stage':'finalizer','stderr':fin.stderr[-1200:]})
                    continue
                rqa=PROD/f'pollinations-{aid.lower()}-runtime-qa.json'
                rv=run([sys.executable,'tools/sprites/validate_runtime_asset.py','--asset-id',aid,'--path',str(runtime.relative_to(ROOT)),'--report',str(rqa.relative_to(ROOT))])
                if rv.returncode!=0:
                    data=json.loads(rqa.read_text()) if rqa.exists() else {'issues':['runtime-validator-failed']}
                    attempts_log.append({'attempt':attempt+1,'seed':seed,'stage':'runtime-qa','issues':data.get('issues',[])})
                    runtime.unlink(missing_ok=True)
                    continue
                mark_done(aid)
                summary['successes'].append({'id':aid,'seed':seed,'candidate':str(out.relative_to(ROOT)),'runtime':str(runtime.relative_to(ROOT))})
                print(f'BATCH_DONE={aid} seed={seed}',flush=True)
                ok=True
                break
            except Exception as e:
                attempts_log.append({'attempt':attempt+1,'seed':seed,'stage':'exception','error':repr(e)})
                if stem:
                    (RUNTIME/f'{stem}.webp').unlink(missing_ok=True)
        if not ok:
            summary['failures'].append({'id':aid,'attempts':attempts_log})
            print(f'BATCH_BLOCKED={aid}',flush=True)
            break

    (PROD/'pollinations-batch-summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps(summary,indent=2))
    if not summary['successes']:
        raise SystemExit(2)

if __name__=='__main__': main()
