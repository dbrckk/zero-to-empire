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
import time
from pathlib import Path

WORK = Path('/kaggle/working')
REPO = Path('/tmp/zero-to-empire')
OUT = WORK / 'output'
COUNT = int(os.getenv('SPRITE_COUNT', '60'))
SEED = int(os.getenv('SPRITE_SEED', str(int(time.time()) % 2_000_000_000)))


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def ensure_gpu_compatible_torch() -> None:
    try:
        cap = subprocess.check_output(
            ['nvidia-smi', '--query-gpu=compute_cap', '--format=csv,noheader'], text=True,
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


def ensure_flux_runtime() -> None:
    """Install the exact stack documented by the pre-quantized FLUX checkpoint.

    NF4 is supported by bitsandbytes on NVIDIA compute capability 6.0+, covering
    both Kaggle P100 and T4. The split FLUX pipeline peaks far below 16 GB VRAM.
    """
    print('KAGGLE_ENGINE=flux1-schnell-nf4-split', flush=True)
    subprocess.run([
        'python', '-m', 'pip', 'install', '--quiet', '--upgrade',
        'bitsandbytes==0.48.1', 'diffusers==0.35.1', 'peft==0.17.1',
        'protobuf==5.29.5', 'sentencepiece==0.2.1', 'transformers==4.56.1',
        'accelerate>=1.2', 'safetensors', 'Pillow',
    ], check=True)
    subprocess.run(['python', '-c',
        "import torch,bitsandbytes,diffusers,transformers; "
        "print('KAGGLE_FLUX_STACK=' + diffusers.__version__ + '/' + transformers.__version__ + '/' + bitsandbytes.__version__); "
        "print('KAGGLE_FLUX_GPU=' + torch.cuda.get_device_name(0))"], check=True)


WORK.mkdir(parents=True, exist_ok=True)
if REPO.exists(): shutil.rmtree(REPO)
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(parents=True)
subprocess.run(['git','clone','--depth','1','https://github.com/dbrckk/zero-to-empire.git',str(REPO)], check=True)
os.chdir(REPO)

# VEH-16 repeatedly regressed toward ordinary sedans despite negative wording.
# For the Kaggle production lane, replace the automotive-biased prompt with a
# spacecraft/hover-skimmer silhouette while preserving the manifest's executive
# prestige intent. Fail closed if the expected canonical phrase changes.
factory_path = REPO / 'tools/sprites/kaggle_sprite_factory.py'
factory_text = factory_path.read_text(encoding='utf-8')
old_veh16 = "'VEH-16':'ONE futuristic EXECUTIVE ANTI-GRAVITY HOVER LIMOUSINE. It has ZERO wheels, ZERO tires, ZERO wheel arches and ZERO circular wheel-like details. Replace all wheel positions with four bright rectangular anti-gravity lift emitters visibly attached under the corners. The entire sleek luxury cabin floats high above empty space with a large unmistakable air gap. Smooth continuous side skirts and levitation hull, futuristic spacecraft-like executive transport, NOT a sedan and NOT a conventional automobile'"
new_veh16 = "'VEH-16':'ONE premium executive anti-gravity PASSENGER SKIMMER, designed like a compact luxury spacecraft and hover yacht rather than any automobile. A single continuous boat-like levitation hull with a glass executive cabin on top. ZERO wheels, ZERO tires, ZERO wheel arches, ZERO hubs, ZERO circular wheel-like forms, ZERO grille, ZERO automotive headlights, ZERO road-car bumper, ZERO side mirrors. Four flat rectangular cyan anti-gravity emitters are recessed into the smooth underside, not mounted like wheels. The entire craft is visibly suspended high over empty space with a large clean air gap under the complete hull. Long elegant prestige silhouette, unmistakably futuristic airborne executive transport, not a car, sedan, SUV, wagon, van or limousine'"
if old_veh16 not in factory_text:
    raise SystemExit('Canonical VEH-16 prompt anchor changed; refusing unverified patch')
factory_path.write_text(factory_text.replace(old_veh16, new_veh16, 1), encoding='utf-8')
print('KAGGLE_VEH16_PROMPT_OVERRIDE=spacecraft-skimmer', flush=True)

ensure_gpu_compatible_torch()
ensure_flux_runtime()

incoming = REPO / 'art/incoming/final-sprites'
before = {p.name: digest(p) for p in incoming.glob('*_final.png') if p.is_file()}
print(f'KAGGLE_EXISTING_CANDIDATES={len(before)}', flush=True)
print(f'KAGGLE_BATCH_SEED={SEED}', flush=True)
subprocess.run([
    'python','-u','tools/sprites/kaggle_sprite_factory.py','--kind','ALL','--count',str(COUNT),'--seed',str(SEED)
], check=True)

fresh=[]
for p in sorted(incoming.glob('*_final.png')):
    if p.is_file() and (p.name not in before or before[p.name] != digest(p)): fresh.append(p)
print(f'KAGGLE_FRESH_CANDIDATES={len(fresh)}', flush=True)
if not fresh: raise SystemExit('No fresh candidate sprites produced by this run')
qa=OUT/'batch-contact-sheet.png'; report=OUT/'batch-qa-report.json'
subprocess.run(['python','tools/sprites/build_sprite_contact_sheet.py','--output',str(qa),'--report',str(report),'--files',*[str(x) for x in fresh]], check=True)
candidate_dir=OUT/'candidates'; candidate_dir.mkdir(); targets=[]
for f in fresh:
    dst=candidate_dir/f.name; shutil.copy2(f,dst); targets.append({'file':f.name,'sha256':digest(dst),'bytes':dst.stat().st_size})
(OUT/'generated-targets.json').write_text(json.dumps({'count':len(targets),'engine':'FLUX.1-schnell NF4 split','seed':SEED,'targets':targets},indent=2),encoding='utf-8')
print(f'KAGGLE_EXPORT_COUNT={len(fresh)}', flush=True); print('KAGGLE_OUTPUT_ONLY=1', flush=True)
