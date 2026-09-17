from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Mapping
import re

ROW = re.compile(
    r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$"
)


class ManifestError(ValueError):
    """Raised when the authoritative art manifest cannot resolve safely."""


@dataclass(frozen=True)
class ManifestAsset:
    id: str
    name: str
    description: str
    runtime_path: str
    status: str


def load_manifest(path: Path) -> dict[str, ManifestAsset]:
    assets: dict[str, ManifestAsset] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = ROW.match(line)
        if not match:
            continue
        asset_id, name, description, runtime_path, status = (
            part.strip() for part in match.groups()
        )
        if asset_id.upper() == "ID" or set(asset_id) == {"-"}:
            continue
        normalized_id = asset_id.upper()
        if normalized_id in assets:
            raise ManifestError(f"duplicate manifest id: {normalized_id}")
        assets[normalized_id] = ManifestAsset(
            normalized_id, name, description, runtime_path, status.upper()
        )
    if not assets:
        raise ManifestError(f"no manifest assets parsed from {path}")
    return assets


def require_asset(
    assets: Mapping[str, ManifestAsset], asset_id: str
) -> ManifestAsset:
    key = asset_id.strip().upper()
    try:
        return assets[key]
    except KeyError as exc:
        raise ManifestError(f"manifest asset not found: {key}") from exc
