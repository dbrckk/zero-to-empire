from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
from pathlib import Path
import re

from tools.assets.manifest import ManifestAsset

_ALLOWED_SOURCE_TYPES = frozenset({"generated", "external", "manual"})
_ALLOWED_REVIEWS = frozenset({"pending", "accepted", "rejected"})
_SHA256 = re.compile(r"^[0-9a-f]{64}$")


class MetadataError(ValueError):
    """Raised when candidate provenance or semantic identity is invalid."""


@dataclass(frozen=True)
class CandidateMetadata:
    manifest_id: str
    semantic_role: str
    runtime_path: str
    source_type: str
    provider: str
    source_url: str | None
    license: str
    prompt_sha256: str
    asset_sha256: str
    review: str

    def validate_against(self, asset: ManifestAsset) -> None:
        if self.manifest_id != asset.id:
            raise MetadataError(
                f"manifest id mismatch: {self.manifest_id!r} != {asset.id!r}"
            )
        if self.semantic_role != asset.description:
            raise MetadataError("semantic role disagrees with authoritative manifest")
        if self.runtime_path != asset.runtime_path:
            raise MetadataError("runtime path disagrees with authoritative manifest")
        if self.source_type not in _ALLOWED_SOURCE_TYPES:
            raise MetadataError(f"invalid source type: {self.source_type!r}")
        if self.review not in _ALLOWED_REVIEWS:
            raise MetadataError(f"invalid review state: {self.review!r}")
        if not self.provider.strip():
            raise MetadataError("provider must be recorded")
        if not self.license.strip():
            raise MetadataError("license must be recorded")
        if not _SHA256.fullmatch(self.prompt_sha256):
            raise MetadataError("prompt_sha256 must be a lowercase SHA-256 digest")
        if not _SHA256.fullmatch(self.asset_sha256):
            raise MetadataError("asset_sha256 must be a lowercase SHA-256 digest")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_metadata(path: Path, metadata: CandidateMetadata) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(asdict(metadata), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
