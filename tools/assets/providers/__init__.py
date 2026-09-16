from __future__ import annotations

from dataclasses import dataclass

from PIL import Image


@dataclass(frozen=True)
class ProviderResult:
    image: Image.Image
    provider: str
    source_url: str | None
    license: str
