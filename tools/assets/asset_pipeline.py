#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import sys
from typing import Protocol

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.assets.manifest import ManifestAsset, load_manifest, require_asset
from tools.assets.metadata import CandidateMetadata, MetadataError, sha256_file, write_metadata
from tools.assets.providers import ProviderResult
from tools.assets.static_processing import isolate, normalize, validate

DEFAULT_MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"


class AssetProvider(Protocol):
    def generate(self, asset: ManifestAsset, prompt: str) -> ProviderResult: ...


def build_prompt(asset: ManifestAsset) -> str:
    """Build generation instructions only from the documented manifest semantics."""
    return (
        "AAA premium mobile strategy game authored production art. "
        f"Asset: {asset.name}. Documented role: {asset.description} "
        "Preserve a clear readable silhouette at mobile size, consistent upper-left key light, "
        "cool fill and selective warm/cyan accents. No readable text, no logo, no watermark, "
        "no UI labels, no border, no frame, no collage and no unrelated objects."
    )


def _candidate_side(image: Image.Image) -> int:
    side = min(image.size)
    if side <= 0:
        raise RuntimeError(f"invalid provider image dimensions: {image.size}")
    return side


def prepare_candidate(
    asset_id: str,
    provider: AssetProvider,
    root: Path = ROOT,
    manifest_path: Path = DEFAULT_MANIFEST,
) -> Path:
    asset = require_asset(load_manifest(manifest_path), asset_id)
    if asset.status == "DONE":
        raise MetadataError(
            f"{asset.id} is DONE; candidate regeneration requires a separate reviewed workflow"
        )

    prompt = build_prompt(asset)
    result = provider.generate(asset, prompt)
    final = normalize(isolate(result.image), _candidate_side(result.image))
    validate(final)

    candidate_dir = root / "art/incoming/assets" / asset.id
    candidate_dir.mkdir(parents=True, exist_ok=True)
    candidate_path = candidate_dir / "candidate.png"
    final.save(candidate_path, "PNG", optimize=True)

    metadata = CandidateMetadata(
        manifest_id=asset.id,
        semantic_role=asset.description,
        runtime_path=asset.runtime_path,
        source_type="generated",
        provider=result.provider,
        source_url=result.source_url,
        license=result.license,
        prompt_sha256=hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        asset_sha256=sha256_file(candidate_path),
        review="pending",
    )
    metadata.validate_against(asset)
    write_metadata(candidate_dir / "metadata.json", metadata)
    return candidate_dir


def _load_candidate_metadata(path: Path) -> CandidateMetadata:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return CandidateMetadata(**data)
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        raise MetadataError(f"invalid candidate metadata: {path}") from exc


def validate_candidate(
    asset_id: str,
    root: Path = ROOT,
    manifest_path: Path = DEFAULT_MANIFEST,
) -> tuple[float, float]:
    asset = require_asset(load_manifest(manifest_path), asset_id)
    candidate_dir = root / "art/incoming/assets" / asset.id
    candidate_path = candidate_dir / "candidate.png"
    metadata = _load_candidate_metadata(candidate_dir / "metadata.json")
    metadata.validate_against(asset)
    actual_sha = sha256_file(candidate_path)
    if metadata.asset_sha256 != actual_sha:
        raise MetadataError("candidate content hash disagrees with metadata")
    with Image.open(candidate_path) as image:
        metrics = validate(image.convert("RGBA"))
    return metrics


def inspect_asset(asset_id: str, manifest_path: Path = DEFAULT_MANIFEST) -> dict:
    asset = require_asset(load_manifest(manifest_path), asset_id)
    return asdict(asset)


def _provider(name: str) -> AssetProvider:
    if name == "hf-static":
        from tools.assets.providers.hf_static import HfStaticProvider

        return HfStaticProvider()
    raise SystemExit(f"unsupported provider: {name}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Zero -> Empire unified asset pipeline")
    sub = parser.add_subparsers(dest="command", required=True)

    inspect_parser = sub.add_parser("inspect")
    inspect_parser.add_argument("--id", required=True, dest="asset_id")

    prepare_parser = sub.add_parser("prepare")
    prepare_parser.add_argument("--id", required=True, dest="asset_id")
    prepare_parser.add_argument("--provider", default="hf-static")

    validate_parser = sub.add_parser("validate")
    validate_parser.add_argument("--id", required=True, dest="asset_id")

    args = parser.parse_args(argv)
    if args.command == "inspect":
        print(json.dumps(inspect_asset(args.asset_id), indent=2, sort_keys=True))
        return 0
    if args.command == "prepare":
        directory = prepare_candidate(args.asset_id, _provider(args.provider))
        print(f"CANDIDATE_DIR={directory.relative_to(ROOT)}")
        return 0
    if args.command == "validate":
        coverage, dominant = validate_candidate(args.asset_id)
        print(f"TECHNICAL_QA=pass coverage={coverage:.1%} dominant={dominant:.1%}")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
