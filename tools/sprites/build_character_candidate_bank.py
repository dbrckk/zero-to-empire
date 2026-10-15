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

ASSET_NAME = re.compile(r"^zte_chr_(?:op|tech|log|eng)_(?:idle|walk|work|carry|repair|celeb)_final\.png$")
ARCHIVE_NAME = re.compile(r"^zte-characters-([1-9][0-9]*)\.zip$")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
PRODUCED_STATES = frozenset({
    "AWAITING_REVIEW", "CANDIDATE", "TECHNICAL_PASS", "VALIDATED",
    "APPROVED", "RUNTIME_READY", "DONE",
})
MAX_ATLAS_BYTES = 100 * 1024 * 1024


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
             report_file: Path | None = None) -> dict:
    data = json.loads(master.read_text(encoding="utf-8"))
    assets = data["assets"]
    target_total = data["target_total"]
    if target_total != 235 or len(assets) != 235:
        raise ValueError("Canonical production target drifted from 235")
    if len({asset["id"] for asset in assets}) != target_total:
        raise ValueError("Duplicate canonical asset IDs")
    sources = open_archives(archive_folder)
    strict_done = sum(x["strict_status"] == "DONE" for x in assets)
    review_targets = [
        item for item in assets
        if item["strict_status"] != "DONE" and item["id"].startswith("CHR-")
    ]
    remaining_noncharacters = [
        x["id"] for x in assets
        if x["strict_status"] != "DONE" and not x["id"].startswith("CHR-")
    ]
    included: list[tuple[str, bytes]] = []
    entries = []
    missing = []
    for asset in review_targets:
        asset_id = asset["id"]
        status = str(asset.get("pipeline_status") or "").upper()
        run_id = int(asset.get("review_artifact_run_id") or 0)
        name = Path(asset["runtime"]).with_suffix(".png").name
        source = sources.get(run_id)
        if status not in PRODUCED_STATES:
            missing.append({"id": asset_id, "reason": "not-technically-collected",
                            "pipeline_status": status})
            continue
        if not ASSET_NAME.fullmatch(name) or not source or name not in source["index"]:
            missing.append({"id": asset_id, "reason": "missing-exact-source-archive",
                            "source_collector_run_id": run_id})
            continue
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
        if any(entry["id"] == asset_id for entry in entries):
            raise ValueError(f"Duplicate candidate {asset_id}")
        warnings = sorted(set(
            str(w) for w in
            (recorded.get("deferred_art_warnings") or []) +
            (asset.get("deferred_art_warnings") or [])
            if str(w)
        ))
        entries.append({
            "id": asset_id,
            "filename": name,
            "source_collector_run_id": run_id,
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
        "candidate_count": len(entries),
        "production_processed": production_processed,
        "production_remaining": target_total - production_processed,
        "missing_character_candidates": missing,
        "missing_noncharacter_ids": remaining_noncharacters,
        "candidate_production_complete": complete,
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
    args = parser.parse_args()
    d = assemble(args.master, args.archives, args.output, args.report)
    print("CHARACTER_BANK_CANDIDATES=" + str(d["candidate_count"]))
    print("CHARACTER_BANK_PRODUCTION=" + str(d["production_processed"]) + "/235")
    print("CHARACTER_BANK_MISSING=" +
          ",".join(x["id"] for x in d["missing_character_candidates"]))
    print("CHARACTER_BANK_PRODUCTION_COMPLETE=" + str(d["candidate_production_complete"]).lower())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
