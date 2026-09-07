#!/usr/bin/env python3
"""Kaggle high-throughput entrypoint for Zero -> Empire final sprite production.

Routes each expensive GPU run to the largest useful backlog instead of repeatedly
spending a whole kernel on a single static straggler. Buildings are generated in
complete coherent families; static assets remain the fallback lane.
"""
import hashlib, json, os, re, shutil, subprocess, time
from pathlib import Path

WORK=Path('/kaggle/working'); REPO=Path('/tmp/zero-to-empire'); OUT=WORK/'output'
COUNT=int(os.getenv('SPRITE_COUNT','60')); SEED=int(os.getenv('SPRITE_SEED',str(int(time.time())%2_000_000_000)))
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")

def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1024*1024),b''): h.update(c)
 return h.hexdigest()

def ensure_gpu():
 try: cap=subprocess.check_output(['nvidia-smi','--query-gpu=compute_cap','--format=csv,noheader'],text=True).splitlines()[0].strip()
 except Exception as e: print('KAGGLE_GPU_CAPABILITY=unknown',e,flush=True); return
 print('KAGGLE_GPU_CAPABILITY='+cap,flush=True)
 if int(cap.split('.')[0])>=7: return
 subprocess.run(['python','-m','pip','install','--quiet','--upgrade','--force-reinstall','torch==2.5.1','torchvision==0.20.1','--index-url','https://download.pytorch.org/whl/cu121'],check=True)

def ensure_flux():
 print('KAGGLE_ENGINE=flux1-schnell-nf4-yield-router',flush=True)
 subprocess.run(['python','-m','pip','install','--quiet','--upgrade','bitsandbytes==0.48.1','diffusers==0.35.1','peft==0.17.1','protobuf==5.29.5','sentencepiece==0.2.1','transformers==4.56.1','accelerate>=1.2','safetensors','Pillow'],check=True)

def backlog():
 counts={'BLD':0,'STATIC':0}
 for line in (REPO/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md').read_text(encoding='utf-8').splitlines():
  m=ROW.match(line)
  if not m or m.group(5).strip().upper()!='TODO': continue
  aid=m.group(1).strip()
  if aid.startswith('BLD-'): counts['BLD']+=1
  elif aid.startswith(('MCH-','TER-','PRP-','VEH-','CORE-')): counts['STATIC']+=1
 return counts

WORK.mkdir(parents=True,exist_ok=True); shutil.rmtree(REPO,ignore_errors=True); shutil.rmtree(OUT,ignore_errors=True); OUT.mkdir(parents=True)
subprocess.run(['git','clone','--depth','1','https://github.com/dbrckk/zero-to-empire.git',str(REPO)],check=True); os.chdir(REPO)
ensure_gpu(); ensure_flux()
incoming=REPO/'art/incoming/final-sprites'; before={p.name:digest(p) for p in incoming.glob('*_final.png') if p.is_file()}
q=backlog(); print('KAGGLE_BACKLOG='+json.dumps(q,separators=(',',':')),flush=True); print(f'KAGGLE_BATCH_SEED={SEED}',flush=True)
# Throughput policy: a GPU run must attack a sizeable coherent backlog. A lone
# semantic straggler must not monopolize the mass-production lane.
if q['BLD']>=7:
 lane='BUILDING_FAMILIES'; cmd=['python','-u','tools/sprites/kaggle_building_family_factory.py','--count',str(COUNT),'--seed',str(SEED)]
else:
 lane='STATIC'; cmd=['python','-u','tools/sprites/kaggle_sprite_factory.py','--kind','ALL','--count',str(COUNT),'--seed',str(SEED)]
print('KAGGLE_LANE='+lane,flush=True); subprocess.run(cmd,check=True)
fresh=[p for p in sorted(incoming.glob('*_final.png')) if p.is_file() and (p.name not in before or before[p.name]!=digest(p))]
print(f'KAGGLE_FRESH_CANDIDATES={len(fresh)}',flush=True)
if not fresh: raise SystemExit('No fresh candidate sprites produced by this run')
qa=OUT/'batch-contact-sheet.png'; report=OUT/'batch-qa-report.json'
subprocess.run(['python','tools/sprites/build_sprite_contact_sheet.py','--output',str(qa),'--report',str(report),'--files',*[str(x) for x in fresh]],check=True)
cdir=OUT/'candidates'; cdir.mkdir(); targets=[]
for f in fresh:
 dst=cdir/f.name; shutil.copy2(f,dst); targets.append({'file':f.name,'sha256':digest(dst),'bytes':dst.stat().st_size})
(OUT/'generated-targets.json').write_text(json.dumps({'count':len(targets),'engine':'FLUX.1-schnell NF4 yield-routed batch','lane':lane,'seed':SEED,'backlog':q,'targets':targets},indent=2),encoding='utf-8')
print(f'KAGGLE_EXPORT_COUNT={len(fresh)}',flush=True); print('KAGGLE_OUTPUT_ONLY=1',flush=True)
