#!/usr/bin/env python3
"""Kaggle entrypoint launched by GitHub Actions.
Clones the canonical repo, generates a static sprite batch, QA-checks it,
and exports only candidates created or changed by this run into
/kaggle/working/output.
"""
import hashlib
import os
import shutil
import subprocess
from pathlib import Path

WORK = Path('/kaggle/working')
REPO = WORK / 'zero-to-empire'
OUT = WORK / 'output'
COUNT = int(os.getenv('SPRITE_COUNT', '60'))


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


os.chdir(WORK)
if REPO.exists():
    shutil.rmtree(REPO)
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

subprocess.run(
    ['git', 'clone', '--depth', '1', 'https://github.com/dbrckk/zero-to-empire.git', str(REPO)],
    check=True,
)
os.chdir(REPO)

incoming = REPO / 'art/incoming/final-sprites'
before = {p.name: digest(p) for p in incoming.glob('*_final.png') if p.is_file()}
print(f'KAGGLE_EXISTING_CANDIDATES={len(before)}', flush=True)

subprocess.run(
    ['python', '-u', 'tools/sprites/kaggle_sprite_factory.py', '--kind', 'ALL', '--count', str(COUNT)],
    check=True,
)

fresh = []
for p in sorted(incoming.glob('*_final.png')):
    if not p.is_file():
        continue
    current = digest(p)
    if p.name not in before or before[p.name] != current:
        fresh.append(p)

print(f'KAGGLE_FRESH_CANDIDATES={len(fresh)}', flush=True)
if not fresh:
    raise SystemExit('No fresh candidate sprites produced by this run')

qa = OUT / 'batch-contact-sheet.png'
report = OUT / 'batch-qa-report.json'
subprocess.run(
    [
        'python',
        'tools/sprites/build_sprite_contact_sheet.py',
        '--output',
        str(qa),
        '--report',
        str(report),
        '--files',
        *[str(x) for x in fresh],
    ],
    check=True,
)

candidate_dir = OUT / 'candidates'
candidate_dir.mkdir()
for f in fresh:
    shutil.copy2(f, candidate_dir / f.name)
print(f'KAGGLE_EXPORT_COUNT={len(fresh)}', flush=True)
