#!/usr/bin/env python3
"""Assemble a traceable, review-only character bank from persistent Releases.

Every selected atlas must have the *same collector run* recorded on the
canonical queue and in the candidate archive, with matching SHA-256 bytes.
This is NOT automatic Android promotion or strict semantic approval.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
import zipfile
from pathlib import Path

from build_sprite_contact_sheet import inspect as inspect_sprite

ASSET_NAME = re.compile(r"^zte_chr_(?:op|tech|log|eng)_(?:idle|walk|work|carry|repair|celeb)_final\.png$")
ARCHIVE_NAME = re.compile(r"^zte-characters-([1-9][0-9]*)\.zip$")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
PRODUCED_STATES = frozenset({
    "AWAITING_REVIEW", "CANDIDATE", "TECHNICAL_PASS", "VALIDATED",
    "APPROVED", "RUNTIME_READY", "DONE",
})
MAX_ATLAS_BYTES = 100 * 1024 * 1024
FRAME_COUNTS = {"IDLE": 6, "WALK": 8, "WORK": 10,
                "CARRY": 8, "REPAIR": 10, "CELEB": 8}
CANONICAL_PRODUCED_STATES = PRODUCED_STATES


def load_local_originals(source: Path | None) -> dict[str, dict]:
    """Validate 18 local authored originals, including per-frame editable SVG.

    This independent source is explicitly labelled as provisional. It is not
    used to mutate Kaggle/controlled queues or advance strict DONE.
    """
    if source is None:
        return {}
    manifest = json.loads((source / "creation-manifest.json").read_text(encoding="utf-8"))
    qa = json.loads((source / "candidate-qa.json").read_text(encoding="utf-8"))
    if (manifest.get("review_only") is not True
            or manifest.get("strict_done_added") != 0
            or qa.get("review_only") is not True):
        raise ValueError("Locally authored sprites are not marked review-only")
    original_rows = manifest.get("assets")
    qa_rows = qa.get("assets")
    if not isinstance(original_rows, list) or not isinstance(qa_rows, list):
        raise ValueError("Malformed local original manifest or QA")
    by_id = {row["id"]: row for row in original_rows}
    by_qa = {row["id"]: row for row in qa_rows}
    expected = {
        f"CHR-{role}-{action}"
        for role in ("OP", "LOG", "ENG") for action in FRAME_COUNTS
    }
    if (len(original_rows) != 18 or len(qa_rows) != 18
            or set(by_id) != expected or set(by_qa) != expected):
        raise ValueError("Local originals must cover 18 distinct role/action IDs")
    return {
        asset_id: {"source": source, "manifest": by_id[asset_id],
                   "qa": by_qa[asset_id]}
        for asset_id in expected
    }


def validated_local_candidate(asset: dict, record: dict) -> tuple[bytes, dict]:
    """Verify actual raster geometry, manifest claims and editable SVG count."""
    asset_id = asset["id"]
    row = record["manifest"]
    qa = record["qa"]
    role, action = asset_id.split("-")[1:]
    frame_count = FRAME_COUNTS[action]
    name = Path(asset["runtime"]).with_suffix(".png").name
    if (row.get("file") != name or row.get("frames") != frame_count
            or row.get("role") != role or row.get("action") != action
            or row.get("strict_approved") is not False
            or row.get("context_only") is not False
            or qa.get("frames") != frame_count
            or qa.get("technical_geometry_pass") is not True
            or qa.get("semantic_approved") is not False
            or qa.get("android_validated") is not False
            or qa.get("strict_done_added") != 0):
        raise ValueError(f"Untrusted local manifest/QA for {asset_id}")
    source = record["source"]
    path = source / "candidates" / name
    if not path.is_file():
        raise ValueError(f"Missing locally authored PNG: {asset_id}")
    results = inspect_sprite(path)
    if results["pass"] is not True or results["width"] != 1024 or results["height"] != 1024:
        raise ValueError(f"Local PNG failed independent frame/alpha QA {asset_id}: {results['issues']}")
    svg_folder = source / "src_svg" / role / action
    svgs = sorted(svg_folder.glob("*.svg"))
    if len(svgs) != frame_count or any(p.stat().st_size == 0 for p in svgs):
        raise ValueError(f"Missing editable authored SVG poses: {asset_id}")
    blob = path.read_bytes()
    if not 24 <= len(blob) <= MAX_ATLAS_BYTES:
        raise ValueError(f"Incorrect local PNG size: {asset_id}")
    return blob, {
        "source_type": "repo-local-original",
        "source_file": "art/incoming/chatgpt-original/candidates/" + name,
        "editable_source": "art/incoming/chatgpt-original/src_svg/" + role + "/" + action,
        "editable_pose_count": len(svgs),
        "source_validation": "original-manifest+original-qa+independent-atlas-geometry",
    }


def open_archives(folder: Path) -> dict[int, dict]:
    """Read indexes only; candidate bytes are verified when actually selected."""
    sources = {}
    for path in sorted(folder.glob("zte-characters-*.zip")):
        match = ARCHIVE_NAME.fullmatch(path.name)
        if match is None:
            continue
        run_id = int(match.group(1))
        if run_id in sources:
            raise ValueError("duplicate source archive run")
        with zipfile.ZipFile(path) as container:
            if container.namelist().count("candidate-index.json") != 1:
                raise ValueError(f"Missing or duplicate provenance index: {path.name}")
            index = json.loads(container.read("candidate-index.json"))
            if int(index.get("source_collector_run_id") or 0) != run_id:
                raise ValueError(f"Wrong source run provenance: {path.name}")
            if index.get("automatic_semantic_approval") is not False:
                raise ValueError(f"Not a review-only archive: {path.name}")
            by_name = {}
            for record in index.get("assets", []):
                name = str(record.get("filename") or "")
                if not ASSET_NAME.fullmatch(name) or name in by_name:
                    raise ValueError(f"Duplicate or unrecognized source atlas {name!r}")
                if record.get("strict_approved") is not False:
                    raise ValueError(f"Unexpected strict-approved source {name!r}")
                if container.namelist().count("candidates/" + name) != 1:
                    raise ValueError(f"Missing or ambiguous archive atlas {name!r}")
                by_name[name] = record
        sources[run_id] = {"path": path, "index": by_name}
    return sources


def assemble(master: Path, archive_folder: Path, output: Path,
             report_file: Path | None = None,
             local_original: Path | None = None) -> dict:
    data = json.loads(master.read_text(encoding="utf-8"))
    assets = data["assets"]
    target_total = data["target_total"]
    if target_total != 235 or len(assets) != 235:
        raise ValueError("Canonical production target drifted from 235")
    if len({asset["id"] for asset in assets}) != target_total:
        raise ValueError("Duplicate canonical asset IDs")
    sources = open_archives(archive_folder)
    originals = load_local_originals(local_original)
    strict_done = sum(x["strict_status"] == "DONE" for x in assets)
    review_targets = [
        item for item in assets
        if item["strict_status"] != "DONE" and item["id"].startswith("CHR-")
    ]
    remaining_noncharacters = [
        x["id"] for x in assets
        if x["strict_status"] != "DONE" and not x["id"].startswith("CHR-")
    ]
    canonical_queue_produced = sum(
        a["strict_status"] == "DONE" or
        str(a.get("pipeline_status") or "").upper() in CANONICAL_PRODUCED_STATES
        for a in assets
    )
    included: list[tuple[str, bytes]] = []
    entries = []
    missing = []
    for asset in review_targets:
        asset_id = asset["id"]
        status = str(asset.get("pipeline_status") or "").upper()
        run_id = int(asset.get("review_artifact_run_id") or 0)
        name = Path(asset["runtime"]).with_suffix(".png").name
        source = sources.get(run_id)
        source_details: dict
        if status in PRODUCED_STATES and source and name in source["index"]:
            recorded = source["index"][name]
            with zipfile.ZipFile(source["path"]) as container:
                blob = container.read("candidates/" + name)
            if not 24 <= len(blob) <= MAX_ATLAS_BYTES:
                raise ValueError(f"Invalid candidate byte length: {name}")
            if blob[:8] != PNG_SIGNATURE or blob[12:16] != b"IHDR":
                raise ValueError(f"Not a PNG with IHDR: {name}")
            if struct.unpack(">II", blob[16:24]) != (1024, 1024):
                raise ValueError(f"Wrong character atlas dimensions: {name}")
            digest = hashlib.sha256(blob).hexdigest()
            if digest != recorded.get("sha256") or len(blob) != recorded.get("bytes"):
                raise ValueError(f"Candidate checksum/size mismatch: {name}")
            source_details = {
                "source_type": "collected-kaggle",
                "source_collector_run_id": run_id,
                "source_validation": "collector-technical-qa+exact-run+sha256",
            }
            source_warnings = recorded.get("deferred_art_warnings") or []
        elif asset_id in originals:
            # A real on-repo, authored 1024px/4-column/transparent source
            # is preferable to an uncollected async GPU job. It is clearly
            # identified as a local review candidate, not as Kaggle output.
            blob, source_details = validated_local_candidate(asset, originals[asset_id])
            digest = hashlib.sha256(blob).hexdigest()
            source_warnings = []
        else:
            missing.append({
                "id": asset_id,
                "reason": ("not-technically-collected" if status not in PRODUCED_STATES
                           else "missing-exact-source-archive"),
                "pipeline_status": status, "source_collector_run_id": run_id,
            })
            continue
        if any(entry["id"] == asset_id for entry in entries):
            raise ValueError(f"Duplicate candidate {asset_id}")
        warnings = sorted(set(
            str(w) for w in
            source_warnings + (asset.get("deferred_art_warnings") or [])
            if str(w)
        ))
        entries.append({
            "id": asset_id,
            "filename": name,
            **source_details,
            "sha256": digest,
            "bytes": len(blob),
            "runtime_target_for_later_approval": asset["runtime"],
            "deferred_art_warnings": warnings,
            "acceptance_mode": asset.get("candidate_acceptance_mode", "strict"),
            "strict_approved": False,
            "runtime_promoted": False,
        })
        included.append((name, blob))
    production_processed = strict_done + len(entries)
    complete = not missing and not remaining_noncharacters and production_processed == target_total
    report = {
        "schema_version": 1,
        "target_total": target_total,
        "strict_done": strict_done,
        "canonical_queue_production_processed": canonical_queue_produced,
        "canonical_queue_production_remaining": target_total - canonical_queue_produced,
        "candidate_count": len(entries),
        "production_processed": production_processed,
        "production_remaining": target_total - production_processed,
        "missing_character_candidates": missing,
        "missing_noncharacter_ids": remaining_noncharacters,
        "candidate_production_complete": complete,
        "local_original_fallback_ids": [
            entry["id"] for entry in entries
            if entry["source_type"] == "repo-local-original"
        ],
        "automatic_semantic_approval": False,
        "automatic_runtime_promotion": False,
        "bank_entries": entries,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as packed:
        packed.writestr("candidate-bank-index.json", json.dumps(report, indent=2) + "\n")
        packed.writestr("README.txt",
            "Zero to Empire - review-only character atlas bank.\n"
            "All candidate PNGs need later semantic review and Android integration.\n"
            "A complete candidate bank is NOT equivalent to strict DONE.\n")
        for name, blob in included:
            packed.writestr("candidates/" + name, blob)
    if report_file is not None:
        report_file.parent.mkdir(parents=True, exist_ok=True)
        report_file.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--master", type=Path, default=Path("art/production/master-asset-queue.json"))
    parser.add_argument("--archives", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--local-original", type=Path,
                        help="Optional 18-atlas in-repository original SVG/PNG review source")
    args = parser.parse_args()
    d = assemble(args.master, args.archives, args.output, args.report, args.local_original)
    print("CHARACTER_BANK_CANDIDATES=" + str(d["candidate_count"]))
    print("CHARACTER_BANK_PRODUCTION=" + str(d["production_processed"]) + "/235")
    print("CHARACTER_BANK_CANONICAL_QUEUE=" +
          str(d["canonical_queue_production_processed"]) + "/235")
    print("CHARACTER_BANK_LOCAL_FALLBACK=" +
          ",".join(d["local_original_fallback_ids"]))
    print("CHARACTER_BANK_MISSING=" +
          ",".join(x["id"] for x in d["missing_character_candidates"]))
    print("CHARACTER_BANK_PRODUCTION_COMPLETE=" + str(d["candidate_production_complete"]).lower())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
