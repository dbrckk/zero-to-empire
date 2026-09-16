from __future__ import annotations

import os

from tools.assets.manifest import ManifestAsset
from tools.assets.providers import ProviderResult
from tools.sprites import hf_static_manifest_factory as legacy


class HfStaticProvider:
    """Thin adapter around the existing HF image provider.

    The provider receives an already-resolved manifest asset and prompt. It has
    no authority to choose or mutate the runtime path.
    """

    def generate(self, asset: ManifestAsset, prompt: str) -> ProviderResult:
        del asset  # Semantic/runtime identity remains owned by the orchestrator.
        return ProviderResult(
            image=legacy.generate(prompt),
            provider=os.getenv("HF_ASSET_PROVIDER_NAME", "hf-z-image-turbo").strip()
            or "hf-z-image-turbo",
            source_url=legacy.SPACE_URL,
            license=os.getenv(
                "HF_ASSET_LICENSE", "generated-provider-terms"
            ).strip()
            or "generated-provider-terms",
        )
