#!/usr/bin/env python3
"""Package actual Android emulator gameplay screenshots for Google Play.

Only crops existing screenshots; does not generate or alter in-game UI, edit
numbers or add promotional overlays. Output is 24-bit RGB PNG, 1080x2160
(exactly 2:1), the maximum Google Play phone screenshot aspect ratio.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image

SCREENSHOTS = {
    "01-empire": ("Empire city and first business", "Empire et première entreprise"),
    "02-managers": ("Hire managers to automate production", "Recrutement de responsables"),
    "03-upgrades": ("Permanent technology upgrades", "Améliorations technologiques permanentes"),
    "04-goals": ("Daily challenges and goals", "Défis et objectifs quotidiens"),
    "05-store": ("Optional in-game purchases", "Achats intégrés facultatifs"),
}
SOURCE_SIZE = (1080, 2400)
CROP = (0, 120, 1080, 2280)
TARGET_SIZE = (1080, 2160)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(source: Path, destination: Path, run_id: int, source_sha: str) -> dict:
    if not (run_id > 0 and len(source_sha) == 40 and all(x in "0123456789abcdef" for x in source_sha)):
        raise ValueError("Expected a specific verified Actions run and 40-character Git SHA")
    destination.mkdir(parents=True, exist_ok=True)
    result = []
    for name, (en, fr) in SCREENSHOTS.items():
        inp = source / (name + ".png")
        out = destination / (name + ".png")
        if not inp.is_file():
            raise FileNotFoundError(inp)
        with Image.open(inp) as original:
            original.load()
            if original.size != SOURCE_SIZE or original.format != "PNG":
                raise ValueError(f"Unexpected emulator screenshot {inp}: {original.size} {original.format}")
            if original.mode not in ("RGB", "RGBA"):
                raise ValueError(f"Unexpected screenshot color model {inp}: {original.mode}")
            if original.mode == "RGBA" and original.getchannel("A").getextrema() != (255, 255):
                raise ValueError(f"Refusing to composite a non-opaque screenshot: {inp}")
            cropped = original.crop(CROP).convert("RGB")
            if cropped.size != TARGET_SIZE:
                raise ValueError(f"Unexpected Play output dimensions: {cropped.size}")
            cropped.save(out, format="PNG", optimize=True)
        with Image.open(out) as verification:
            if verification.mode != "RGB" or verification.size != TARGET_SIZE or verification.format != "PNG":
                raise ValueError(f"Invalid 24-bit screenshot: {out}")
        if out.stat().st_size >= 8 * 1024 * 1024:
            raise ValueError(f"Screenshot exceeds recommended 8 MiB ceiling: {out}")
        result.append({
            "file": out.name,
            "source_path": f"play-store-preview/{name}.png",
            "source_sha256": digest(inp),
            "export_sha256": digest(out),
            "size": "1080x2160",
            "color_mode": "RGB",
            "alt_en": en,
            "alt_fr": fr,
        })
    manifest = {
        "schema_version": 1,
        "source_workflow": "Android Emulator Smoke",
        "source_run_id": run_id,
        "source_commit_sha": source_sha,
        "source_build_type": "debug",
        "store_format_validation": "PASS",
        "source_is_actual_emulator_gameplay": True,
        "pixels_edited": "cropped 120px from top and bottom, converted opaque RGB; no retouching",
        "play_console_approval": False,
        "signed_aab_installation_verified": False,
        "screenshot_count": len(result),
        "screenshots": result,
    }
    (destination / "screenshots-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"PLAY_PHONE_SCREENSHOTS_FORMAT_PASS={len(result)}")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--run-id", type=int, required=True)
    parser.add_argument("--source-sha", type=str, required=True)
    args = parser.parse_args()
    prepare(args.source_dir, args.out_dir, args.run_id, args.source_sha)


if __name__ == "__main__":
    main()
