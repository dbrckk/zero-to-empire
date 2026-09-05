#!/usr/bin/env python3
"""Kaggle entrypoint launched by GitHub Actions.
Clones the canonical repo outside /kaggle/working so Kaggle exports only QA/output
artifacts, generates a static sprite batch, and exports only fresh candidates.
"""
import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path

WORK = Path('/kaggle/working')
REPO = Path('/tmp/zero-to-empire')
OUT = WORK / 'output'
COUNT = int(os.getenv('SPRITE_COUNT', '60'))


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def ensure_gpu_compatible_torch() -> None:
    try:
        cap = subprocess.check_output(
            ['nvidia-smi', '--query-gpu=compute_cap', '--format=csv,noheader'],
            text=True,
        ).splitlines()[0].strip()
    except Exception as exc:
        print(f'KAGGLE_GPU_CAPABILITY=unknown reason={exc}', flush=True)
        return
    print(f'KAGGLE_GPU_CAPABILITY={cap}', flush=True)
    try:
        major = int(cap.split('.', 1)[0])
    except ValueError:
        return
    if major >= 7:
        print('KAGGLE_TORCH_COMPAT=current', flush=True)
        return
    print('KAGGLE_TORCH_COMPAT=install_p100_build', flush=True)
    subprocess.run([
        'python', '-m', 'pip', 'install', '--quiet', '--upgrade', '--force-reinstall',
        'torch==2.5.1', 'torchvision==0.20.1',
        '--index-url', 'https://download.pytorch.org/whl/cu121',
    ], check=True)
    probe = (
        "import torch; print('KAGGLE_TORCH_VERSION=' + torch.__version__); "
        "print('KAGGLE_TORCH_CUDA=' + str(torch.version.cuda)); "
        "print('KAGGLE_TORCH_CAP=' + str(torch.cuda.get_device_capability(0))); "
        "x=torch.ones(1, device='cuda'); print('KAGGLE_TORCH_GPU_PROBE=' + str(x.item()))"
    )
    subprocess.run(['python', '-c', probe], check=True)


WORK.mkdir(parents=True, exist_ok=True)
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
ensure_gpu_compatible_torch()

incoming = REPO / 'art/incoming/final-sprites'
before = {p.name: digest(p) for p in incoming.glob('*_final.png') if p.is_file()}
print(f'KAGGLE_EXISTING_CANDIDATES={len(before)}', flush=True)

subprocess.run(
    ['python', '-u', 'tools/sprites/kaggle_sprite_factory.py', '--kind', 'ALL', '--count', str(COUNT)],
    check=True,
)

fresh = []
for p in sorted(incoming.glob('*_final.png')):
    if p.is_file() and (p.name not in before or before[p.name] != digest(p)):
        fresh.append(p)

print(f'KAGGLE_FRESH_CANDIDATES={len(fresh)}', flush=True)
if not fresh:
    raise SystemExit('No fresh candidate sprites produced by this run')

qa = OUT / 'batch-contact-sheet.png'
report = OUT / 'batch-qa-report.json'
subprocess.run([
    'python', 'tools/sprites/build_sprite_contact_sheet.py',
    '--output', str(qa), '--report', str(report), '--files', *[str(x) for x in fresh],
], check=True)

candidate_dir = OUT / 'candidates'
candidate_dir.mkdir()
targets = []
for f in fresh:
    dst = candidate_dir / f.name
    shutil.copy2(f, dst)
    targets.append({'file': f.name, 'sha256': digest(dst), 'bytes': dst.stat().st_size})
(OUT / 'generated-targets.json').write_text(json.dumps({'count': len(targets), 'targets': targets}, indent=2), encoding='utf-8')
print(f'KAGGLE_EXPORT_COUNT={len(fresh)}', flush=True)
print('KAGGLE_OUTPUT_ONLY=1', flush=True)
