#!/usr/bin/env python3
"""Google Colab high-throughput entrypoint for Zero -> Empire sprite production.

Designed for an interactive Colab GPU runtime. It clones/updates the repository,
routes to the highest-priority remaining sprite lane, and exports only fresh
candidates plus technical QA evidence. It never promotes assets to DONE.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path

WORK = Path('/content')
REPO = WORK / 'zero-to-empire'
OUT = WORK / 'sprite-output'
COUNT = int(os.getenv('SPRITE_COUNT', '56'))
SEED = int(os.getenv('SPRITE_SEED', str(int(time.time()) % 2_000_000_000)))
REPO_URL = os.getenv('ZERO_TO_EMPIRE_REPO', 'https://github.com/dbrckk/zero-to-empire.git')
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()


def sh(*args):
    subprocess.run(list(args), check=True)


def ensure_repo():
    if not (REPO / '.git').is_dir():
        shutil.rmtree(REPO, ignore_errors=True)
        sh('git', 'clone', '--depth', '1', REPO_URL, str(REPO))
    else:
        sh('git', '-C', str(REPO), 'fetch', '--depth', '1', 'origin', 'main')
        sh('git', '-C', str(REPO), 'reset', '--hard', 'origin/main')


def ensure_gpu():
    try:
        gpu = subprocess.check_output(
            ['nvidia-smi', '--query-gpu=name,memory.total,compute_cap', '--format=csv,noheader'],
            text=True,
        ).strip()
    except Exception as exc:
        raise SystemExit(f'COLAB_GPU_REQUIRED: {exc}')
    print('COLAB_GPU=' + gpu, flush=True)


def ensure_flux():
    required = ['diffusers', 'transformers', 'accelerate', 'safetensors', 'torch', 'PIL']
    missing = []
    for name in required:
        try:
            __import__(name)
        except Exception:
            missing.append(name)
    if missing:
        print('COLAB_INSTALLING=' + ','.join(missing), flush=True)
        sh(
            'python', '-m', 'pip', 'install', '--quiet',
            'diffusers==0.35.1', 'transformers==4.56.1', 'accelerate>=1.2',
            'safetensors', 'Pillow<12'
        )


def runtime_exists(runtime: str) -> bool:
    return (REPO / runtime).is_file()


def backlog():
    counts = {'BLD': 0, 'STATIC': 0, 'CHR': 0, 'FX': 0, 'SKIPPED_RUNTIME': 0}
    manifest = REPO / 'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
    for line in manifest.read_text(encoding='utf-8').splitlines():
        m = ROW.match(line)
        if not m or m.group(5).strip().upper() != 'TODO':
            continue
        asset_id = m.group(1).strip()
        runtime = m.group(4).strip()
        if runtime_exists(runtime):
            counts['SKIPPED_RUNTIME'] += 1
            continue
        if asset_id.startswith('BLD-'):
            counts['BLD'] += 1
        elif asset_id.startswith(('MCH-', 'TER-', 'PRP-', 'VEH-', 'CORE-')):
            counts['STATIC'] += 1
        elif asset_id.startswith('CHR-'):
            counts['CHR'] += 1
        elif asset_id.startswith('FX-'):
            counts['FX'] += 1
    return counts


def main():
    ensure_repo()
    ensure_gpu()
    ensure_flux()
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir(parents=True, exist_ok=True)
    os.chdir(REPO)

    incoming = REPO / 'art/incoming/final-sprites'
    incoming.mkdir(parents=True, exist_ok=True)
    before = {p.name: digest(p) for p in incoming.glob('*_final.png') if p.is_file()}
    q = backlog()
    print('COLAB_BACKLOG=' + json.dumps(q, separators=(',', ':')), flush=True)
    print(f'COLAB_BATCH_SEED={SEED}', flush=True)

    if q['BLD'] >= 5:
        lane = 'BUILDING_FAMILIES'
        effective = max(7, min(COUNT, 56))
        cmd = ['python', '-u', 'tools/sprites/kaggle_building_family_factory_v16.py', '--count', str(effective), '--seed', str(SEED)]
    elif q['STATIC']:
        lane = 'STATIC'
        effective = max(14, min(COUNT, 56))
        cmd = ['python', '-u', 'tools/sprites/kaggle_sprite_factory.py', '--kind', 'ALL', '--count', str(effective), '--seed', str(SEED)]
    elif q['CHR']:
        lane = 'CHARACTER_SHEETS'
        effective = max(4, min(COUNT, 8))
        cmd = ['python', '-u', 'tools/sprites/kaggle_character_sheet_factory_v1.py', '--count', str(effective), '--seed', str(SEED)]
    elif q['FX']:
        lane = 'FX_SHEETS'
        effective = max(1, min(COUNT, 18))
        cmd = ['python', '-u', 'tools/sprites/kaggle_fx_sheet_factory_v1.py', '--count', str(effective), '--seed', str(SEED)]
    else:
        raise SystemExit('No supported GPU backlog')

    print(f'COLAB_LANE={lane} COLAB_EFFECTIVE_COUNT={effective}', flush=True)
    subprocess.run(cmd, check=True)

    fresh = [
        p for p in sorted(incoming.glob('*_final.png'))
        if p.is_file() and (p.name not in before or before[p.name] != digest(p))
    ]
    print(f'COLAB_FRESH_CANDIDATES={len(fresh)}', flush=True)
    if not fresh:
        raise SystemExit('No fresh candidate sprites produced by this run')

    qa = OUT / 'batch-contact-sheet.png'
    report = OUT / 'batch-qa-report.json'
    subprocess.run([
        'python', 'tools/sprites/build_sprite_contact_sheet.py',
        '--output', str(qa), '--report', str(report), '--files', *[str(x) for x in fresh]
    ], check=True)

    cdir = OUT / 'candidates'
    cdir.mkdir()
    targets = []
    for f in fresh:
        dst = cdir / f.name
        shutil.copy2(f, dst)
        targets.append({'file': f.name, 'sha256': digest(dst), 'bytes': dst.stat().st_size})

    (OUT / 'generated-targets.json').write_text(json.dumps({
        'count': len(targets),
        'engine': 'colab-yield-router-v1',
        'lane': lane,
        'seed': SEED,
        'backlog': q,
        'targets': targets,
    }, indent=2), encoding='utf-8')

    archive = shutil.make_archive(str(WORK / 'zero-to-empire-colab-sprites'), 'zip', OUT)
    print(f'COLAB_EXPORT_COUNT={len(fresh)}', flush=True)
    print(f'COLAB_ARCHIVE={archive}', flush=True)
    print('COLAB_OUTPUT_ONLY=1', flush=True)


if __name__ == '__main__':
    main()
