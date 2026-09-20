#!/usr/bin/env python3
"""Kaggle high-throughput entrypoint for Zero -> Empire final sprite production.

The GitHub orchestrator deliberately uses short P100 batches; completed candidates
are checkpointed continuously so an interrupted kernel does not discard GPU work.
"""
import hashlib,json,os,re,shutil,subprocess,time,tarfile,zipfile
from pathlib import Path
WORK=Path('/kaggle/working');REPO=Path('/tmp/zero-to-empire');OUT=WORK/'output';COUNT=int(os.getenv('SPRITE_COUNT','7'));SEED=int(os.getenv('SPRITE_SEED',str(int(time.time())%2_000_000_000)));EXPECTED_GENERATOR_SHA=os.getenv('EXPECTED_GENERATOR_SHA','').strip()
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
 if cap.startswith('6.'):
  probe=subprocess.run(['python','-c',"import torch; print(' '.join(torch.cuda.get_arch_list()))"],capture_output=True,text=True)
  arches=(probe.stdout or '').strip();print('KAGGLE_TORCH_ARCHES='+arches,flush=True)
  if 'sm_60' not in arches:
   print('KAGGLE_PASCAL_TORCH_COMPAT_INSTALL=1',flush=True)
   subprocess.run(['python','-m','pip','install','--quiet','--force-reinstall','--no-cache-dir','torch==2.6.0','torchvision==0.21.0','--index-url','https://download.pytorch.org/whl/cu124'],check=True)
   verify=subprocess.check_output(['python','-c',"import torch; print(torch.__version__); print(' '.join(torch.cuda.get_arch_list()))"],text=True).strip();print('KAGGLE_PASCAL_TORCH_VERIFY='+verify.replace('\\n',' | '),flush=True)
def ensure_flux():
 print('KAGGLE_ENGINE=yield-router-v12-positive-source-locked',flush=True)
 required=['diffusers','transformers','accelerate','safetensors','torch','torchvision','PIL','bitsandbytes'];missing=[]
 for name in required:
  try:__import__(name)
  except Exception:missing.append(name)
 if missing:
  print('KAGGLE_MISSING_PACKAGES='+','.join(missing),flush=True)
  subprocess.run(['python','-m','pip','install','--quiet','diffusers==0.35.1','transformers==4.56.1','accelerate>=1.2','safetensors','bitsandbytes>=0.46.1','Pillow<12'],check=True)
def runtime_exists(runtime): return (REPO/runtime).is_file()
def controlled_queue_backlog(path):
 p=REPO/path
 if not p.is_file(): return 0
 try:q=json.loads(p.read_text(encoding='utf-8'))
 except Exception:return 0
 return sum(1 for x in q.get('targets',[]) if str(x.get('status','')).upper()=='PENDING_KAGGLE')
def controlled_character_backlog(): return controlled_queue_backlog('art/production/controlled-character-regen-queue.json')
def controlled_building_backlog(): return controlled_queue_backlog('art/production/controlled-building-regen-queue.json')
def backlog():
 c={'BLD':0,'STATIC':0,'CHR':0,'FX':0,'SKIPPED_RUNTIME':0,'CONTROLLED_CHR':controlled_character_backlog(),'CONTROLLED_BLD':controlled_building_backlog()}
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
def valid_tree(root):
 return (root/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md').is_file() and (root/'tools/sprites').is_dir()
def resolve_source():
 roots=[Path('/kaggle/input'),Path('/kaggle/src'),Path('/kaggle/working'),Path.cwd()]
 # The tarball is the immutable payload uploaded for this exact source fingerprint.
 # Kaggle can also expose a stale unpacked repo_bundle/ tree from an older dataset
 # version, so archives must win whenever both representations are mounted.
 direct=[]
 for root in roots:
  if root.exists():direct.extend(root.glob('**/repo_bundle.tar.gz'))
 if direct:
  direct.sort(key=lambda p:p.stat().st_mtime,reverse=True)
  print(f'KAGGLE_BUNDLE_ARCHIVE={direct[0]}',flush=True);return 'tar',direct[0]
 scratch=WORK/'bundle-unwrapped';shutil.rmtree(scratch,ignore_errors=True);scratch.mkdir(parents=True,exist_ok=True)
 archives=[]
 for root in roots:
  if root.exists():archives.extend(root.glob('**/*.zip'))
 for z in archives:
  try:
   with zipfile.ZipFile(z) as f:
    names=f.namelist();hit=next((n for n in names if Path(n).name=='repo_bundle.tar.gz'),None)
    if not hit:continue
    dst=scratch/'repo_bundle.tar.gz'
    with f.open(hit) as src,dst.open('wb') as out:shutil.copyfileobj(src,out)
    print(f'KAGGLE_BUNDLE_UNWRAPPED={z}:{hit}',flush=True);return 'tar',dst
  except Exception as e:print(f'KAGGLE_ARCHIVE_SKIP={z}:{e}',flush=True)
 # Native trees are a compatibility fallback only when Kaggle did not retain
 # either the tarball or a zip containing it.
 for base in roots:
  if not base.exists():continue
  candidates=[base]
  try:candidates.extend(p for p in base.iterdir() if p.is_dir())
  except Exception:pass
  try:candidates.extend(p for p in base.glob('*/*') if p.is_dir())
  except Exception:pass
  for candidate in candidates:
   if valid_tree(candidate):
    print(f'KAGGLE_BUNDLE_TREE_FALLBACK={candidate}',flush=True);return 'tree',candidate
 for root in roots:
  if root.exists():
   for p in list(root.glob('**/*'))[:200]:
    if p.is_file():print(f'KAGGLE_INPUT_FILE={p} bytes={p.stat().st_size}',flush=True)
 return None,None
WORK.mkdir(parents=True,exist_ok=True);shutil.rmtree(REPO,ignore_errors=True);shutil.rmtree(OUT,ignore_errors=True);OUT.mkdir(parents=True)
source_kind,source=resolve_source()
if source is None:raise SystemExit('sprite repository source missing from Kaggle inputs')
if source_kind=='tree':shutil.copytree(source,REPO,dirs_exist_ok=True)
else:
 REPO.mkdir(parents=True,exist_ok=True)
 with tarfile.open(source,'r:gz') as t:t.extractall(REPO)
print(f'KAGGLE_REPO_SOURCE={source_kind}:{source}',flush=True)
# The Kaggle dataset mount can lag behind the published dataset version. Ship the
# critical building generator chain with the kernel itself and overlay it onto
# the mounted repository before validating/running it.
overlay_names=(
 'kaggle_building_family_factory_v16.py',
 'kaggle_building_family_factory_v16_10.py',
 'kaggle_building_family_factory_v15.py',
 'kaggle_building_family_factory_v14.py',
)
overlay_applied=False
for overlay_root in (Path('/kaggle/src'),Path('/kaggle/working'),Path.cwd()):
 candidate=overlay_root/'tools/sprites/kaggle_building_family_factory_v16.py'
 if not candidate.is_file():continue
 if EXPECTED_GENERATOR_SHA and digest(candidate)!=EXPECTED_GENERATOR_SHA:continue
 dst_dir=REPO/'tools/sprites';dst_dir.mkdir(parents=True,exist_ok=True)
 for name in overlay_names:
  src=overlay_root/'tools/sprites'/name
  if not src.is_file():raise SystemExit(f'KAGGLE_KERNEL_OVERLAY_MISSING:{name}')
  shutil.copy2(src,dst_dir/name)
 print(f'KAGGLE_KERNEL_GENERATOR_OVERLAY={overlay_root}',flush=True)
 overlay_applied=True
 break
if EXPECTED_GENERATOR_SHA and not overlay_applied:
 print('KAGGLE_KERNEL_GENERATOR_OVERLAY=not-found',flush=True)
generator_path=REPO/'tools/sprites/kaggle_building_family_factory_v16.py'
if EXPECTED_GENERATOR_SHA:
 if not generator_path.is_file():raise SystemExit('KAGGLE_STALE_BUNDLE: generator file missing from mounted bundle')
 actual_generator_sha=digest(generator_path)
 print(f'KAGGLE_EXPECTED_GENERATOR_SHA={EXPECTED_GENERATOR_SHA}',flush=True)
 print(f'KAGGLE_MOUNTED_GENERATOR_SHA={actual_generator_sha}',flush=True)
 if actual_generator_sha!=EXPECTED_GENERATOR_SHA:
  raise SystemExit(f'KAGGLE_STALE_BUNDLE: mounted generator {actual_generator_sha} != expected {EXPECTED_GENERATOR_SHA}')
os.chdir(REPO);ensure_gpu();ensure_flux()
incoming=REPO/'art/incoming/final-sprites';incoming.mkdir(parents=True,exist_ok=True);before={p.name:digest(p) for p in incoming.glob('*_final.png') if p.is_file()};q=backlog();print('KAGGLE_BACKLOG='+json.dumps(q,separators=(',',':')),flush=True);print(f'KAGGLE_BATCH_SEED={SEED}',flush=True)
if q.get('CONTROLLED_BLD',0)>0:
 lane='CONTROLLED_BUILDING_FAMILY';effective=max(7,min(q['CONTROLLED_BLD'],max(COUNT,7)));cmd=['python','-u','tools/sprites/kaggle_building_family_factory_v16.py','--count',str(effective),'--seed',str(SEED)]
elif q.get('CONTROLLED_CHR',0)>0:
 lane='CONTROLLED_CHARACTER_SHEETS';effective=max(1,min(q['CONTROLLED_CHR'],min(COUNT,2)));cmd=['python','-u','tools/sprites/kaggle_character_sheet_factory_v1.py','--count',str(effective),'--seed',str(SEED)]
elif q['BLD']>=5:
 lane='BUILDING_FAMILIES';effective=max(7,min(COUNT,56));cmd=['python','-u','tools/sprites/kaggle_building_family_factory_v16.py','--count',str(effective),'--seed',str(SEED)]
elif q['STATIC']:
 lane='STATIC';effective=max(4,min(COUNT,7));cmd=['python','-u','tools/sprites/kaggle_sprite_factory.py','--kind','ALL','--count',str(effective),'--seed',str(SEED)]
elif q['CHR']:
 lane='CHARACTER_SHEETS';effective=max(1,min(COUNT,2));cmd=['python','-u','tools/sprites/kaggle_character_sheet_factory_v1.py','--count',str(effective),'--seed',str(SEED)]
elif q['FX']:
 lane='FX_SHEETS';effective=max(1,min(COUNT,7));cmd=['python','-u','tools/sprites/kaggle_fx_sheet_factory_v1.py','--count',str(effective),'--seed',str(SEED)]
else:raise SystemExit('No supported GPU backlog')
print(f'KAGGLE_LANE={lane} KAGGLE_EFFECTIVE_COUNT={effective}',flush=True)
cdir=OUT/'candidates';cdir.mkdir(parents=True,exist_ok=True)
def current_fresh():return [p for p in sorted(incoming.glob('*_final.png')) if p.is_file() and (p.name not in before or before[p.name]!=digest(p))]
def checkpoint_fresh():
 fresh=current_fresh();exported=0
 for f in fresh:
  try:
   from PIL import Image
   with Image.open(f) as im:im.verify()
   dst=cdir/f.name
   if not dst.exists() or digest(dst)!=digest(f):shutil.copy2(f,dst)
   exported+=1
  except Exception as e:print(f'KAGGLE_CHECKPOINT_SKIP={f.name}:{e}',flush=True)
 if exported:print(f'KAGGLE_CHECKPOINT_COUNT={exported}',flush=True)
 return fresh
proc=subprocess.Popen(cmd)
while proc.poll() is None:
 checkpoint_fresh();time.sleep(20)
checkpoint_fresh()
if proc.returncode!=0:raise SystemExit(f'generator exited {proc.returncode}')
fresh=current_fresh();print(f'KAGGLE_FRESH_CANDIDATES={len(fresh)}',flush=True)
for srcname in ('branch-search-report.json',):
 src=incoming/srcname
 if src.is_file():shutil.copy2(src,OUT/srcname)
if not fresh:raise SystemExit('No fresh candidate sprites produced by this run')
qa=OUT/'batch-contact-sheet.png';report=OUT/'batch-qa-report.json';subprocess.run(['python','tools/sprites/build_sprite_contact_sheet.py','--output',str(qa),'--report',str(report),'--files',*[str(x) for x in fresh]],check=True)
cdir=OUT/'candidates';cdir.mkdir(parents=True,exist_ok=True);targets=[]
for f in fresh:
 dst=cdir/f.name;shutil.copy2(f,dst);targets.append({'file':f.name,'sha256':digest(dst),'bytes':dst.stat().st_size})
(OUT/'generated-targets.json').write_text(json.dumps({'count':len(targets),'engine':'yield-router-v12-positive-source-locked','lane':lane,'seed':SEED,'backlog':q,'targets':targets},indent=2),encoding='utf-8');print(f'KAGGLE_EXPORT_COUNT={len(fresh)}',flush=True);print('KAGGLE_OUTPUT_ONLY=1',flush=True)
