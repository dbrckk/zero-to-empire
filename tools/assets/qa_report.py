from __future__ import annotations

import json
from pathlib import Path

from tools.sprites.build_sprite_contact_sheet import inspect, make_sheet


def build_candidate_qa_artifacts(candidate_dir: Path) -> tuple[Path, Path]:
    """Build deterministic technical-QA artifacts for one reviewed candidate."""
    candidate_dir = Path(candidate_dir)
    image_path = candidate_dir / "candidate.png"
    metadata_path = candidate_dir / "metadata.json"

    if not image_path.is_file():
        raise FileNotFoundError(f"missing candidate.png: {image_path}")
    if not metadata_path.is_file():
        raise FileNotFoundError(f"missing metadata.json: {metadata_path}")

    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    manifest_id = metadata.get("manifest_id")
    if manifest_id != candidate_dir.name:
        raise ValueError(
            f"metadata manifest_id {manifest_id!r} does not match candidate directory {candidate_dir.name!r}"
        )

    checks = inspect(image_path)
    sheet_path = candidate_dir / "contact-sheet.png"
    report_path = candidate_dir / "qa-report.json"
    make_sheet([image_path], [checks], sheet_path, cols=1)

    report = {
        "manifest_id": manifest_id,
        "review": metadata.get("review"),
        "candidate_file": image_path.name,
        "metadata_file": metadata_path.name,
        "contact_sheet_file": sheet_path.name,
        "automatic_checks": checks,
        "semantic_review_required": True,
    }
    report_path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return report_path, sheet_path
