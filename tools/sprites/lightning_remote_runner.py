#!/usr/bin/env python3
"""Control a Lightning AI Studio from CI and retrieve strict QA-only outputs."""
from __future__ import annotations

import os
import shutil
from pathlib import Path

from lightning_sdk import Machine, Studio

STUDIO_NAME = os.getenv("LIGHTNING_STUDIO_NAME", "zero-to-empire-sprites")
TEAMSPACE = os.environ["LIGHTNING_TEAMSPACE"]
USERNAME = os.environ["LIGHTNING_USERNAME"]
REMOTE_REPO = "zero-to-empire"
LOCAL_OUT = Path("lightning-output")


def main() -> None:
    studio = Studio(
        name=STUDIO_NAME,
        teamspace=TEAMSPACE,
        user=USERNAME,
        create_ok=True,
    )

    print(f"LIGHTNING_STUDIO={STUDIO_NAME}", flush=True)
    try:
        if str(studio.status).lower().endswith("running"):
            if studio.machine != Machine.T4:
                print(f"LIGHTNING_SWITCH_MACHINE={studio.machine}->T4", flush=True)
                studio.switch_machine(Machine.T4)
        else:
            print("LIGHTNING_START_MACHINE=T4", flush=True)
            studio.start(Machine.T4)

        prep = r'''set -euo pipefail
if [ -d zero-to-empire/.git ]; then
  cd zero-to-empire
  git fetch origin main
  git reset --hard origin/main
else
  rm -rf zero-to-empire
  git clone --depth 1 https://github.com/dbrckk/zero-to-empire.git zero-to-empire
  cd zero-to-empire
fi
python -m pip install --quiet 'diffusers==0.35.1' 'transformers==4.56.1' 'accelerate>=1.2' safetensors 'Pillow<12'
python -u tools/sprites/lightning_studio_factory.py
'''
        output, code = studio.run_with_exit_code(f"bash -lc {prep!r}")
        print(output, flush=True)
        if code != 0:
            raise SystemExit(f"Lightning sprite factory failed with exit code {code}")

        shutil.rmtree(LOCAL_OUT, ignore_errors=True)
        studio.download_folder(f"{REMOTE_REPO}/.lightning-output", str(LOCAL_OUT))
        print(f"LIGHTNING_DOWNLOAD={LOCAL_OUT}", flush=True)
    finally:
        if os.getenv("LIGHTNING_STOP_AFTER", "1") == "1":
            try:
                studio.stop()
                print("LIGHTNING_STUDIO_STOPPED=1", flush=True)
            except Exception as exc:
                print(f"LIGHTNING_STOP_WARNING={exc}", flush=True)


if __name__ == "__main__":
    main()
