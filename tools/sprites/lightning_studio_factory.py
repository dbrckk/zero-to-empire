#!/usr/bin/env python3
"""Run one strict candidate-generation wave inside a Lightning AI Studio.

This script never promotes assets into the canonical manifest. It only exports
fresh generated candidates plus technical QA evidence for later semantic review.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".lightning-output"
INCOMING = ROOT / "art/incoming/final-sprites"
COUNT = int(os.getenv("SPRITE_COUNT", "56"))
SEED = int(os.getenv("SPRITE_SEED", str(int(time.time()) % 2_000_000_000)))
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def require_gpu() -> None:
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=name,memory.total,compute_cap", "--format=csv,noheader"],
            text=True,
        ).strip()
    except Exception as exc:
        raise SystemExit(f"LIGHTNING_GPU_REQUIRED: {exc}")
    print("LIGHTNING_GPU=" + out, flush=True)


def ensure_deps() -> None:
    required = ["diffusers", "transformers", "accelerate", "safetensors", "torch", "PIL"]
    missing = []
    for name in required:
        try:
            __import__(name)
        except Exception:
            missing.append(name)
    if missing:
        print("LIGHTNING_MISSING_PACKAGES=" + ",".join(missing), flush=True)
        subprocess.run(
            [
                "python", "-m", "pip", "install", "--quiet",
                "diffusers==0.35.1", "transformers==4.56.1", "accelerate>=1.2",
                "safetensors", "Pillow<12",
            ],
            check=True,
        )


def backlog() -> dict[str, int]:
    counts = {"BLD": 0, "STATIC": 0, "CHR": 0, "FX": 0, "SKIPPED_RUNTIME": 0}
    manifest = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
    for line in manifest.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if not m or m.group(5).strip().upper() != "TODO":
            continue
        asset_id = m.group(1).strip()
        runtime = m.group(4).strip()
        if (ROOT / runtime).is_file():
            counts["SKIPPED_RUNTIME"] += 1
            continue
        if asset_id.startswith("BLD-"):
            counts["BLD"] += 1
        elif asset_id.startswith(("MCH-", "TER-", "PRP-", "VEH-", "CORE-")):
            counts["STATIC"] += 1
        elif asset_id.startswith("CHR-"):
            counts["CHR"] += 1
        elif asset_id.startswith("FX-"):
            counts["FX"] += 1
    return counts


def choose_command(q: dict[str, int]) -> tuple[str, int, list[str]]:
    if q["BLD"] >= 5:
        n = max(7, min(COUNT, 56))
        return "BUILDING_FAMILIES", n, ["python", "-u", "tools/sprites/kaggle_building_family_factory_v16.py", "--count", str(n), "--seed", str(SEED)]
    if q["STATIC"]:
        n = max(14, min(COUNT, 56))
        return "STATIC", n, ["python", "-u", "tools/sprites/kaggle_sprite_factory.py", "--kind", "ALL", "--count", str(n), "--seed", str(SEED)]
    if q["CHR"]:
        n = max(4, min(COUNT, 8))
        return "CHARACTER_SHEETS", n, ["python", "-u", "tools/sprites/kaggle_character_sheet_factory_v1.py", "--count", str(n), "--seed", str(SEED)]
    if q["FX"]:
        n = max(1, min(COUNT, 18))
        return "FX_SHEETS", n, ["python", "-u", "tools/sprites/kaggle_fx_sheet_factory_v1.py", "--count", str(n), "--seed", str(SEED)]
    raise SystemExit("No supported GPU backlog")


def main() -> None:
    os.chdir(ROOT)
    require_gpu()
    ensure_deps()
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir(parents=True)
    INCOMING.mkdir(parents=True, exist_ok=True)

    before = {p.name: digest(p) for p in INCOMING.glob("*_final.png") if p.is_file()}
    q = backlog()
    lane, effective, cmd = choose_command(q)
    print("LIGHTNING_BACKLOG=" + json.dumps(q, separators=(",", ":")), flush=True)
    print(f"LIGHTNING_LANE={lane} LIGHTNING_EFFECTIVE_COUNT={effective} LIGHTNING_SEED={SEED}", flush=True)
    subprocess.run(cmd, check=True)

    fresh = [
        p for p in sorted(INCOMING.glob("*_final.png"))
        if p.is_file() and (p.name not in before or before[p.name] != digest(p))
    ]
    print(f"LIGHTNING_FRESH_CANDIDATES={len(fresh)}", flush=True)
    if not fresh:
        raise SystemExit("No fresh candidate sprites produced by this run")

    qa = OUT / "batch-contact-sheet.png"
    report = OUT / "batch-qa-report.json"
    subprocess.run(
        ["python", "tools/sprites/build_sprite_contact_sheet.py", "--output", str(qa), "--report", str(report), "--files", *[str(x) for x in fresh]],
        check=True,
    )

    cdir = OUT / "candidates"
    cdir.mkdir()
    targets = []
    for src in fresh:
        dst = cdir / src.name
        shutil.copy2(src, dst)
        targets.append({"file": src.name, "sha256": digest(dst), "bytes": dst.stat().st_size})

    (OUT / "generated-targets.json").write_text(
        json.dumps({"count": len(targets), "engine": "lightning-ai-studio", "lane": lane, "seed": SEED, "backlog": q, "targets": targets}, indent=2),
        encoding="utf-8",
    )
    print(f"LIGHTNING_EXPORT_COUNT={len(fresh)}", flush=True)
    print("LIGHTNING_OUTPUT_ONLY=1", flush=True)


if __name__ == "__main__":
    main()
