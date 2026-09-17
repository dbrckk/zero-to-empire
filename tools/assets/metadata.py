from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
from pathlib import Path

from tools.assets.manifest import ManifestAsset


class MetadataError(ValueError):
    """Raised when candidate provenance or manifest binding is invalid."""


_ALLOWED_SOURCE_TYPES = frozenset({"generated", "external", "manual"})
_ALLOWED_REVIEWS = frozenset({"pending", "accepted", "rejected"})


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
                f"candidate manifest id {self.manifest_id!r} does not match {asset.id!r}"
            )
        if self.semantic_role != asset.description:
            raise MetadataError("candidate semantic role does not match manifest description")
        if self.runtime_path != asset.runtime_path:
            raise MetadataError("candidate runtime path does not match manifest mapping")
        if self.source_type not in _ALLOWED_SOURCE_TYPES:
            raise MetadataError(f"unsupported source type: {self.source_type}")
        if self.review not in _ALLOWED_REVIEWS:
            raise MetadataError(f"unsupported review state: {self.review}")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_metadata(path: Path, metadata: CandidateMetadata) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(asdict(metadata), indent=2, sort_keys=True) + "\n"
    path.write_text(payload, encoding="utf-8")
