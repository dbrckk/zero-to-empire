#!/usr/bin/env python3
"""Technical verification of locally authored character atlases.

Image/format checks cannot approve artistic semantics or mark strict DONE.
No network, GPU, image generation, repository mutation, or zip extraction.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath

from PIL import Image

FRAME_COUNTS = {"IDLE": 6, "WALK": 8, "WORK": 10, "CARRY": 8, "REPAIR": 10, "CELEB": 8}
IDS = {f"CHR-{role}-{action}" for role in ("OP", "LOG", "ENG") for action in FRAME_COUNTS}
ARCHIVE_LIMIT = 80 * 1024 * 1024
ENTRY_LIMIT = 12 * 1024 * 1024
TOTAL_LIMIT = 240 * 1024 * 1024


def verify(path: Path) -> dict:
    problems: list[str] = []
    detail: list[dict] = []
    if not path.is_file() or path.stat().st_size > ARCHIVE_LIMIT:
        raise ValueError("missing-or-oversized-zip")
    with zipfile.ZipFile(path) as archive:
        files: dict[str, zipfile.ZipInfo] = {}
        total = 0
        for info in archive.infolist():
            name = info.filename
            posix = PurePosixPath(name)
            if (not re.fullmatch(r"[A-Za-z0-9_./-]+", name)
                or posix.is_absolute() or ".." in posix.parts
                or "\\" in name or info.flag_bits & 1):
                raise ValueError(f"unsafe-zip-entry:{name}")
            if name in files:
                raise ValueError(f"duplicate-zip-entry:{name}")
            if (info.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError(f"symlink-zip-entry:{name}")
            total += info.file_size
            if info.file_size > ENTRY_LIMIT or total > TOTAL_LIMIT:
                raise ValueError(f"zip-decompression-limit:{name}")
            files[name] = info
        manifest = json.loads(archive.read("manifest.json"))
        entries = manifest.get("entries", [])
        actual_ids = [item.get("id") for item in entries]
        if set(actual_ids) != IDS or len(actual_ids) != 18 or len(set(actual_ids)) != 18:
            problems.append("wrong-canonical-role-action-id-set")
        if manifest.get("review_only") is not True or manifest.get("strict_done_increased") is not False:
            problems.append("unreviewed-pack-claims-approval")
        for item in entries:
            aid = item.get("id", "")
            if aid not in IDS:
                continue
            _, role, action = aid.split("-")
            frame_count = FRAME_COUNTS[action]
            name = f"zte_chr_{role.lower()}_{action.lower()}_final.png"
            errors = []
            if (item.get("filename") != name or item.get("frames") != frame_count
                or item.get("dimensions") != [1024, 1024] or item.get("cell") != [256, 256]):
                errors.append("manifest-geometry-or-filename")
            if (item.get("visual_semantic_approved") is not False
                or item.get("android_runtime_approved") is not False
                or item.get("strict_done_granted") is not False):
                errors.append("unreviewed-item-claims-approval")
            if item.get("context_only") != (action == "IDLE" and role in {"OP", "LOG"}):
                errors.append("invalid-role-idle-context-flag")
            data = archive.read("atlases/" + name)
            sha = hashlib.sha256(data).hexdigest()
            if sha != item.get("sha256"):
                errors.append("atlas-hash-mismatch")
            with Image.open(io.BytesIO(data)) as image:
                image.load()
                if image.format != "PNG" or image.size != (1024, 1024) or image.mode != "RGBA":
                    errors.append("invalid-png-size-or-alpha")
                rgba = image.convert("RGBA")
            frames = []
            margin = 256
            for index in range(16):
                x, y = index % 4 * 256, index // 4 * 256
                tile = rgba.crop((x, y, x + 256, y + 256))
                box = tile.getchannel("A").getbbox()
                if index >= frame_count:
                    if box:
                        errors.append(f"unexpected-padding-pixels:{index}")
                    continue
                if box is None:
                    errors.append(f"empty-frame:{index}")
                else:
                    margin = min(margin, box[0], box[1], 256 - box[2], 256 - box[3])
                    frames.append(hashlib.sha256(tile.tobytes()).digest())
                svg_name = f"svg_source/{role}/{action}/{index:02}.svg"
                if svg_name not in files:
                    errors.append(f"missing-editable-svg:{index}")
            if margin < 8:
                errors.append("unsafe-alpha-frame-border")
            if len(set(frames)) < 2:
                errors.append("no-distinct-animation-frames")
            detail.append({"id": aid, "technical_preflight_pass": not errors,
                           "errors": errors, "frames": frame_count,
                           "min_alpha_margin": margin, "sha256": sha,
                           "visual_semantic_approval": False,
                           "android_validation": False, "strict_done_granted": False})
            problems.extend(f"{aid}:{issue}" for issue in errors)
    return {"schema_version": 1, "technical_preflight_pass": not problems,
            "errors": problems, "total_candidates": len(detail),
            "expected_unresolved_count": 16, "reference_idle_count": 2,
            "visual_semantic_approval": False, "android_validation": False,
            "strict_done_granted": False, "assets": detail}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pack", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    try:
        result = verify(args.pack)
    except (ValueError, OSError, KeyError, RuntimeError, json.JSONDecodeError) as err:
        result = {"technical_preflight_pass": False, "errors": [str(err)],
                  "visual_semantic_approval": False, "android_validation": False,
                  "strict_done_granted": False}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2) + "\n")
    print("LOCAL_ATLAS_PREFLIGHT=" + ("PASS" if result["technical_preflight_pass"] else "FAIL"))
    print("STRICT_DONE_GRANTED=false")
    for issue in result["errors"][:20]:
        print("ERROR " + issue)
    return 0 if result["technical_preflight_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
