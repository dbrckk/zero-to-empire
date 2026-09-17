from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
from typing import Protocol

from PIL import Image

from tools.assets.manifest import ManifestAsset
from tools.assets.metadata import CandidateMetadata, sha256_file, write_metadata
from tools.assets.static_processing import isolate, normalize, validate


class AssetProvider(Protocol):
    name: str
    source_type: str
    license: str

    def generate(self, asset: ManifestAsset, prompt: str) -> Image.Image: ...


@dataclass(frozen=True)
class CandidateResult:
    image_path: Path
    metadata_path: Path
    coverage: float
    dominant_component: float


def build_candidate(
    *,
    asset: ManifestAsset,
    provider: AssetProvider,
    prompt: str,
    target_side: int,
    candidate_root: Path,
) -> CandidateResult:
    """Generate and QA a review candidate without publishing to runtime resources."""
    if asset.status != "TODO":
        raise ValueError(f"manifest asset {asset.id} is not TODO: {asset.status}")
    if target_side <= 0:
        raise ValueError("target_side must be positive")
    if not prompt.strip():
        raise ValueError("prompt must not be empty")

    generated = provider.generate(asset, prompt)
    candidate = normalize(isolate(generated), target_side)
    coverage, dominant = validate(candidate)

    output_dir = candidate_root / asset.id
    output_dir.mkdir(parents=True, exist_ok=True)
    image_path = output_dir / "candidate.png"
    metadata_path = output_dir / "metadata.json"
    candidate.save(image_path, "PNG", optimize=True)

    metadata = CandidateMetadata(
        manifest_id=asset.id,
        semantic_role=asset.description,
        runtime_path=asset.runtime_path,
        source_type=provider.source_type,
        provider=provider.name,
        source_url=None,
        license=provider.license,
        prompt_sha256=hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        asset_sha256=sha256_file(image_path),
        review="pending",
    )
    metadata.validate_against(asset)
    write_metadata(metadata_path, metadata)

    return CandidateResult(image_path, metadata_path, coverage, dominant)
