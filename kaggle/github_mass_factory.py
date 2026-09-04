#!/usr/bin/env python3
"""Kaggle entrypoint launched by GitHub Actions.
Clones the canonical repo, generates a static sprite batch, QA-checks it,
and exports candidates + QA files into /kaggle/working/output.
"""
import os, shutil, subprocess
from pathlib import Path

WORK = Path('/kaggle/working')
REPO = WORK / 'zero-to-empire'
OUT = WORK / 'output'
COUNT = int(os.getenv('SPRITE_COUNT', '60'))

os.chdir(WORK)
if REPO.exists(): shutil.rmtree(REPO)
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(parents=True)

subprocess.run(['git','clone','--depth','1','https://github.com/dbrckk/zero-to-empire.git',str(REPO)], check=True)
os.chdir(REPO)
subprocess.run(['python','-u','tools/sprites/kaggle_sprite_factory.py','--kind','ALL','--count',str(COUNT)], check=True)

incoming = REPO / 'art/incoming/final-sprites'
files = sorted(incoming.glob('*_final.png'))
if not files:
    raise SystemExit('No candidate sprites produced')

qa = OUT / 'batch-contact-sheet.png'
report = OUT / 'batch-qa-report.json'
cmd = ['python','tools/sprites/build_sprite_contact_sheet.py','--output',str(qa),'--report',str(report),'--files',*[str(x) for x in files]]
subprocess.run(cmd, check=True)

candidate_dir = OUT / 'candidates'
candidate_dir.mkdir()
for f in files:
    shutil.copy2(f, candidate_dir / f.name)
print(f'KAGGLE_EXPORT_COUNT={len(files)}', flush=True)
