#!/usr/bin/env python3
"""Traceable *review-only* ENG IDLE reference for later GPU regeneration.

A technically QA-passing ENG-IDLE from the exact collector run in the current
canonical queue is a visual source, NOT a strict-DONE or runtime asset.
Preparing a seed never updates queue status or the application. The generator
independently runs its full subject/atlas checks before using these pixels.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path

from PIL import Image

SEED_DIR = Path("art/production/kaggle-provisional-idle-seed")
PNG_NAME = "zte_chr_eng_idle_final.png"
PROVENANCE = "provenance.json"
SOURCE_ID = "CHR-ENG-IDLE"
MAX_PNG_BYTES = 15 * 1024 * 1024
SINGLE_PERSON_MAX_RATIO = 0.90


def _single_person_source(blob: bytes) -> Image.Image:
    if len(blob) < 100 or len(blob) > MAX_PNG_BYTES or not blob.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("Invalid ENG-IDLE source PNG bytes")
    with Image.open(io.BytesIO(blob)) as source:
        source.load()
        if source.size != (1024, 1024) or source.mode != "RGBA":
            raise ValueError("ENG-IDLE source must be RGBA 1024x1024")
        cell = source.crop((0, 0, 256, 256))
    bbox = cell.getchannel("A").point(lambda alpha: 255 if alpha >= 64 else 0).getbbox()
    if bbox is None:
        raise ValueError("ENG-IDLE first frame is transparent")
    x0, y0, x1, y1 = bbox
    width, height = x1 - x0, y1 - y0
    if (height < 125 or width < 25 or width / height > SINGLE_PERSON_MAX_RATIO
            or x0 < 6 or y0 < 6 or x1 > 250 or y1 > 250):
        raise ValueError("ENG-IDLE source is clipped or not a tall single-subject seed")
    return cell.crop(bbox)


def prepare(master_path: Path, queue_path: Path, source_archive: Path,
            target_directory: Path, source_run_id: int) -> dict:
    """Pin a prior collector's technically passed PNG to its *current* queue ID."""
    if source_run_id <= 0:
        raise ValueError("source collector run id must be positive")
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    pending = {str(row.get("id") or "") for row in queue.get("targets", [])
               if str(row.get("status") or "").upper() == "PENDING_KAGGLE"}
    if SOURCE_ID not in pending or not ({"CHR-ENG-WORK", "CHR-ENG-REPAIR"} & pending):
        raise ValueError("ENG-IDLE seed may only accompany pending engineer action regeneration")
    master = json.loads(master_path.read_text(encoding="utf-8"))
    rows = [row for row in master["assets"] if row.get("id") == SOURCE_ID]
    if len(rows) != 1:
        raise ValueError("Canonical ENG-IDLE must have one queue entry")
    row = rows[0]
    if (str(row.get("strict_status") or "").upper() == "DONE"
            or str(row.get("pipeline_status") or "").upper() != "AWAITING_REVIEW"
            or row.get("review_artifact_run_id") != source_run_id):
        raise ValueError("Unapproved/incorrectly pinned canonical ENG-IDLE source")
    if not re.fullmatch(r"zte-characters-[1-9][0-9]*\.zip", source_archive.name):
        raise ValueError("Unexpected character source archive filename")
    if source_archive.name != f"zte-characters-{source_run_id}.zip":
        raise ValueError("Collector source archive does not match current IDLE provenance")
    with zipfile.ZipFile(source_archive) as archive:
        names = archive.namelist()
        if names.count("candidate-index.json") != 1 or names.count("candidates/" + PNG_NAME) != 1:
            raise ValueError("Missing or ambiguous archived engineer idle atlas")
        manifest = json.loads(archive.read("candidate-index.json"))
        items = [item for item in manifest.get("assets", [])
                 if item.get("filename") == PNG_NAME]
        if (manifest.get("source_collector_run_id") != source_run_id
                or manifest.get("automatic_semantic_approval") is not False
                or manifest.get("automatic_runtime_promotion") is not False
                or len(items) != 1 or items[0].get("strict_approved") is not False
                or items[0].get("runtime_promoted") is not False
                or items[0].get("deferred_art_warnings") not in (None, [])
                or manifest.get("candidate_count", 0) < 1):
            raise ValueError("Source ENG-IDLE is not a uniquely QA-passing review-only candidate")
        blob = archive.read("candidates/" + PNG_NAME)
        digest = hashlib.sha256(blob).hexdigest()
        if digest != items[0].get("sha256") or len(blob) != items[0].get("bytes"):
            raise ValueError("Archived ENG-IDLE does not match its verified SHA-256 provenance")
    _single_person_source(blob)
    provenance = {
        "schema_version": 1,
        "role": "ENG",
        "id": SOURCE_ID,
        "source_collector_run_id": source_run_id,
        "source_archive": source_archive.name,
        "file": PNG_NAME,
        "sha256": digest,
        "bytes": len(blob),
        "source_validation": "collector-technical-QA+canonical-run+SHA256+RGBA-single-subject",
        "review_only": True,
        "automatic_semantic_approval": False,
        "strict_approved": False,
        "runtime_promoted": False,
    }
    destination = target_directory / SEED_DIR
    destination.mkdir(parents=True, exist_ok=True)
    (destination / PNG_NAME).write_bytes(blob)
    (destination / PROVENANCE).write_text(json.dumps(provenance, indent=2) + "\n",
                                           encoding="utf-8")
    return provenance


def load_seed(role: str, root: Path) -> tuple[Image.Image | None, str]:
    """Load the original reviewed pixels into a neutral canvas, never approve."""
    if role.upper() != "ENG":
        return None, "provisional-engineer-only"
    folder = root / SEED_DIR
    atlas_path = folder / PNG_NAME
    evidence_path = folder / PROVENANCE
    if not atlas_path.is_file() or not evidence_path.is_file():
        return None, "provisional-seed-not-shipped"
    try:
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        if (evidence.get("id") != SOURCE_ID or evidence.get("role") != "ENG"
                or evidence.get("file") != PNG_NAME
                or not isinstance(evidence.get("source_collector_run_id"), int)
                or evidence["source_collector_run_id"] <= 0
                or evidence.get("source_archive") !=
                    f"zte-characters-{evidence['source_collector_run_id']}.zip"
                or evidence.get("review_only") is not True
                or evidence.get("automatic_semantic_approval") is not False
                or evidence.get("strict_approved") is not False
                or evidence.get("runtime_promoted") is not False):
            raise ValueError("Provisional ENG identity seed provenance is unsafe")
        blob = atlas_path.read_bytes()
        if hashlib.sha256(blob).hexdigest() != evidence.get("sha256") or len(blob) != evidence.get("bytes"):
            raise ValueError("Provisional ENG seed SHA-256 mismatch")
        crop = _single_person_source(blob)
        desired_height = 770
        width = round(crop.width * desired_height / crop.height)
        if width < 70 or width > 640:
            raise ValueError("ENG seed character proportions are implausible")
        resized = crop.resize((width, desired_height), Image.Resampling.LANCZOS)
        image = Image.new("RGB", (1024, 1024), (139, 139, 139))
        image.paste(resized.convert("RGB"), ((1024 - width) // 2, (1024 - desired_height) // 2),
                    resized.getchannel("A"))
        return image, f"review-only-{SOURCE_ID}-collector-{evidence['source_collector_run_id']}-sha256-{evidence['sha256'][:12]}"
    except (OSError, ValueError, KeyError, TypeError) as error:
        return None, "provisional-seed-rejected:" + str(error)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--master", type=Path, required=True)
    parser.add_argument("--queue", type=Path, required=True)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    parser.add_argument("--source-run-id", type=int, required=True)
    args = parser.parse_args()
    result = prepare(args.master, args.queue, args.archive,
                     args.output_directory, args.source_run_id)
    print("KAGGLE_ENG_PROVISIONAL_SEED=" + result["sha256"])
    print("KAGGLE_ENG_SOURCE_COLLECTOR=" + str(result["source_collector_run_id"]))
    print("KAGGLE_ENG_SEMANTIC_APPROVAL=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
