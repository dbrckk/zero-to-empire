from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path
from typing import Mapping, Any

from PIL import Image

from tools.assets.manifest import ManifestAsset
from tools.assets.metadata import CandidateMetadata, MetadataError, sha256_file
from tools.assets.static_processing import validate


def _read_metadata(path: Path) -> CandidateMetadata:
    try:
        return CandidateMetadata(**json.loads(path.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        raise MetadataError(f"invalid candidate metadata: {path}") from exc


def build_report(asset: ManifestAsset, candidate_dir: Path) -> dict[str, Any]:
    candidate_path = candidate_dir / "candidate.png"
    metadata = _read_metadata(candidate_dir / "metadata.json")
    metadata.validate_against(asset)

    actual_sha = sha256_file(candidate_path)
    if actual_sha != metadata.asset_sha256:
        raise MetadataError("candidate content hash disagrees with metadata")

    with Image.open(candidate_path) as image:
        coverage, dominant = validate(image.convert("RGBA"))

    semantic_review = metadata.review
    return {
        "manifest_id": asset.id,
        "runtime_path": asset.runtime_path,
        "technical_status": "pass",
        "semantic_review": semantic_review,
        "approved": semantic_review == "accepted",
        "asset_sha256": actual_sha,
        "source": {
            "source_type": metadata.source_type,
            "provider": metadata.provider,
            "source_url": metadata.source_url,
            "license": metadata.license,
        },
        "metrics": {
            "alpha_coverage": coverage,
            "dominant_component": dominant,
        },
    }


def write_report(candidate_dir: Path, report: Mapping[str, Any]) -> Path:
    path = candidate_dir / "qa-report.json"
    path.write_text(
        json.dumps(dict(report), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path
