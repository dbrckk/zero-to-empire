#!/usr/bin/env python3
"""Archive QA-passing character *candidates*, never strict runtime assets.

Input must be an artifact downloaded from a trusted completed collector run.
Only the actual PNG bytes present on disk and marked pass by the technical QA
are copied. Art warnings and exact SHA-256 hashes survive beyond artifact TTL.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

NAME = re.compile(r"zte_chr_(?:op|tech|log|eng)_(?:idle|walk|work|carry|repair|celeb)_final\.png")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_PNG_BYTES = 100 * 1024 * 1024
MAX_ARCHIVE_BYTES = 500 * 1024 * 1024


def archive_candidates(source: Path, destination: Path, source_run_id: int) -> dict:
    if source_run_id <= 0:
        raise ValueError("source run id must be positive")
    if not source.is_dir():
        raise ValueError("missing downloaded collector artifact")
    qa_files = list(source.rglob("github-qa-report.json"))
    if len(qa_files) == 0:
        # A successful collector can observe a genuinely clean, all-rejected
        # Kaggle batch. In that case it deliberately never ran frame QA:
        # there were no candidate PNGs to inspect. Reject this exception
        # unless the actual producer report proves every attempted target was
        # rejected AND the output manifest confirms zero produced sprites.
        # Never silently treat a missing QA report with real PNGs as success.
        if list(source.rglob("*_final.png")):
            raise ValueError("missing technical QA report for present candidate PNGs")
        producer_reports = list(source.rglob("character-sheet-report.json"))
        generated_manifests = list(source.rglob("generated-targets.json"))
        if len(producer_reports) != 1 or len(generated_manifests) != 1:
            raise ValueError("missing technical QA without complete rejection evidence")
        producer_rows = json.loads(producer_reports[0].read_text(encoding="utf-8"))
        generated = json.loads(generated_manifests[0].read_text(encoding="utf-8"))
        if not isinstance(producer_rows, list) or not producer_rows:
            raise ValueError("missing all-rejected producer target records")
        names = [str(r.get("id") or "") for r in producer_rows if isinstance(r, dict)]
        if (len(names) != len(producer_rows) or len(set(names)) != len(names)
                or any(not re.fullmatch(r"CHR-(?:OP|TECH|LOG|ENG)-(?:IDLE|WALK|WORK|CARRY|REPAIR|CELEB)", name)
                       for name in names)
                or any(str(row.get("status") or "").upper() != "REJECT" for row in producer_rows)
                or not isinstance(generated, dict)
                or generated.get("lane") != "CONTROLLED_CHARACTER_SHEETS"
                or generated.get("count") != 0
                or generated.get("targets") != []):
            raise ValueError("missing QA report but batch was not cleanly rejected")
        return {
            "schema_version": 1,
            "source_collector_run_id": source_run_id,
            "candidate_count": 0,
            "technical_qa_report": "not-generated:clean-all-rejected-batch",
            "rejected_target_ids": names,
            "automatic_semantic_approval": False,
            "automatic_runtime_promotion": False,
            "assets": [],
        }
    if len(qa_files) != 1:
        raise ValueError(f"expected one technical QA report, got {len(qa_files)}")
    qa = json.loads(qa_files[0].read_text(encoding="utf-8"))
    rows = qa.get("assets") if isinstance(qa, dict) else None
    if not isinstance(rows, list):
        raise ValueError("technical QA report has no assets rows")
    accepted: list[tuple[Path, dict]] = []
    seen: set[str] = set()
    total_bytes = 0
    for row in rows:
        name = Path(str(row.get("file") or "")).name
        if not NAME.fullmatch(name) or row.get("pass") is not True:
            continue
        if name in seen:
            raise ValueError(f"duplicate QA record {name}")
        seen.add(name)
        found = [p for p in source.rglob(name) if p.parent.name == "candidates" and p.is_file()]
        if len(found) != 1:
            raise ValueError(f"missing or ambiguous QA-passing sprite bytes: {name}")
        path = found[0]
        size = path.stat().st_size
        if size < len(PNG_SIGNATURE) or size > MAX_PNG_BYTES:
            raise ValueError(f"sprite has invalid file size: {name}")
        with path.open("rb") as file:
            if file.read(len(PNG_SIGNATURE)) != PNG_SIGNATURE:
                raise ValueError(f"sprite is not PNG: {name}")
        total_bytes += size
        if total_bytes > MAX_ARCHIVE_BYTES:
            raise ValueError("archive exceeds bounded total source size")
        accepted.append((path, {
            "filename": name,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "bytes": size,
            "deferred_art_warnings": sorted({
                str(w) for w in row.get("deferred_art_warnings") or [] if w
            }),
            "strict_approved": False,
            "runtime_promoted": False,
        }))
    manifest = {
        "schema_version": 1,
        "source_collector_run_id": source_run_id,
        "candidate_count": len(accepted),
        "technical_qa_report": "included QA-passing rows only",
        "automatic_semantic_approval": False,
        "automatic_runtime_promotion": False,
        "assets": [meta for _, meta in accepted],
    }
    if accepted:
        destination.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as bundle:
            bundle.writestr("candidate-index.json", json.dumps(manifest, indent=2) + "\n")
            for path, meta in accepted:
                bundle.write(path, "candidates/" + meta["filename"])
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-run-id", type=int, required=True)
    args = parser.parse_args()
    manifest = archive_candidates(args.source, args.output, args.source_run_id)
    print("CHARACTER_CANDIDATES_ARCHIVED=" + str(manifest["candidate_count"]))
    print("CHARACTER_ARCHIVE_RUN=" + str(args.source_run_id))
    if args.output.is_file():
        print("CHARACTER_ARCHIVE_SHA256=" + hashlib.sha256(args.output.read_bytes()).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
