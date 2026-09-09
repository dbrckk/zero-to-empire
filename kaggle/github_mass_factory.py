#!/usr/bin/env python3
"""Kaggle high-throughput entrypoint for Zero -> Empire final sprite production."""
import hashlib,json,os,re,shutil,subprocess,time,tarfile
from pathlib import Path
WORK=Path('/kaggle/working');REPO=Path('/tmp/zero-to-empire');OUT=WORK/'output';COUNT=int(os.getenv('SPRITE_COUNT','56'));SEED=int(os.getenv('SPRITE_SEED',str(int(time.time())%2_000_000_000)))
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def ensure_gpu():
 try:cap=subprocess.check_output(['nvidia-smi','--query-gpu=compute_cap','--format=csv,noheader'],text=True).splitlines()[0].strip()
 except Exception as e:print('KAGGLE_GPU_CAPABILITY=unknown',e,flush=True);return
 print('KAGGLE_GPU_CAPABILITY='+cap,flush=True)
def ensure_flux():
 print('KAGGLE_ENGINE=yield-router-v12-positive-source-locked',flush=True)
 required=['diffusers','transformers','accelerate','safetensors','torch','PIL']
 missing=[]
 for name in required:
  try:__import__(name)
  except Exception:missing.append(name)
 if missing:
  print('KAGGLE_MISSING_PACKAGES='+','.join(missing),flush=True)
  subprocess.run(['python','-m','pip','install','--quiet','diffusers==0.35.1','transformers==4.56.1','accelerate>=1.2','safetensors','Pillow<12'],check=True)
def runtime_exists(runtime): return (REPO/runtime).is_file()
def backlog():
 c={'BLD':0,'STATIC':0,'CHR':0,'FX':0,'SKIPPED_RUNTIME':0}
 for line in (REPO/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md').read_text(encoding='utf-8').splitlines():
  m=ROW.match(line)
  if not m or m.group(5).strip().upper()!='TODO':continue
  a=m.group(1).strip();runtime=m.group(4).strip()
  if runtime_exists(runtime):c['SKIPPED_RUNTIME']+=1;continue
  if a.startswith('BLD-'):c['BLD']+=1
  elif a.startswith(('MCH-','TER-','PRP-','VEH-','CORE-')):c['STATIC']+=1
  elif a.startswith('CHR-'):c['CHR']+=1
  elif a.startswith('FX-'):c['FX']+=1
 return c
WORK.mkdir(parents=True,exist_ok=True);shutil.rmtree(REPO,ignore_errors=True);shutil.rmtree(OUT,ignore_errors=True);OUT.mkdir(parents=True)
bundles=[Path('/kaggle/src/repo_bundle.tar.gz'),Path('/kaggle/working/repo_bundle.tar.gz'),Path.cwd()/'repo_bundle.tar.gz']
bundle=next((p for p in bundles if p.is_file()),None)
if bundle is None:raise SystemExit('repo_bundle.tar.gz missing from Kaggle kernel payload')
REPO.mkdir(parents=True,exist_ok=True)
with tarfile.open(bundle,'r:gz') as t:t.extractall(REPO)
print(f'KAGGLE_REPO_SOURCE=bundled:{bundle}',flush=True)
os.chdir(REPO);ensure_gpu();ensure_flux()
incoming=REPO/'art/incoming/final-sprites';incoming.mkdir(parents=True,exist_ok=True);before={p.name:digest(p) for p in incoming.glob('*_final.png') if p.is_file()};q=backlog();print('KAGGLE_BACKLOG='+json.dumps(q,separators=(',',':')),flush=True);print(f'KAGGLE_BATCH_SEED={SEED}',flush=True)
if q['BLD']>=5:
 lane='BUILDING_FAMILIES';effective=max(7,min(COUNT,56));cmd=['python','-u','tools/sprites/kaggle_building_family_factory_v16.py','--count',str(effective),'--seed',str(SEED)]
elif q['STATIC']:
 lane='STATIC';effective=max(14,min(COUNT,56));cmd=['python','-u','tools/sprites/kaggle_sprite_factory.py','--kind','ALL','--count',str(effective),'--seed',str(SEED)]
elif q['CHR']:
 lane='CHARACTER_SHEETS';effective=max(4,min(COUNT,8));cmd=['python','-u','tools/sprites/kaggle_character_sheet_factory_v1.py','--count',str(effective),'--seed',str(SEED)]
elif q['FX']:
 lane='FX_SHEETS';effective=max(1,min(COUNT,18));cmd=['python','-u','tools/sprites/kaggle_fx_sheet_factory_v1.py','--count',str(effective),'--seed',str(SEED)]
else:raise SystemExit('No supported GPU backlog')
print(f'KAGGLE_LANE={lane} KAGGLE_EFFECTIVE_COUNT={effective}',flush=True);subprocess.run(cmd,check=True)
fresh=[p for p in sorted(incoming.glob('*_final.png')) if p.is_file() and (p.name not in before or before[p.name]!=digest(p))];print(f'KAGGLE_FRESH_CANDIDATES={len(fresh)}',flush=True)
for srcname in ('branch-search-report.json',):
 src=incoming/srcname
 if src.is_file():shutil.copy2(src,OUT/srcname)
if not fresh:raise SystemExit('No fresh candidate sprites produced by this run')
qa=OUT/'batch-contact-sheet.png';report=OUT/'batch-qa-report.json';subprocess.run(['python','tools/sprites/build_sprite_contact_sheet.py','--output',str(qa),'--report',str(report),'--files',*[str(x) for x in fresh]],check=True)
cdir=OUT/'candidates';cdir.mkdir();targets=[]
for f in fresh:
 dst=cdir/f.name;shutil.copy2(f,dst);targets.append({'file':f.name,'sha256':digest(dst),'bytes':dst.stat().st_size})
(OUT/'generated-targets.json').write_text(json.dumps({'count':len(targets),'engine':'yield-router-v12-positive-source-locked','lane':lane,'seed':SEED,'backlog':q,'targets':targets},indent=2),encoding='utf-8');print(f'KAGGLE_EXPORT_COUNT={len(fresh)}',flush=True);print('KAGGLE_OUTPUT_ONLY=1',flush=True)