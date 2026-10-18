#!/usr/bin/env python3
"""Export verified Play listing artwork from the game's owned vector sources.

Never edits gameplay resources; produces store-only 512px icon and 1024x500
feature graphic. SVG previews are NOT phone gameplay screenshots.
"""
from __future__ import annotations

import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
A = "{http://schemas.android.com/apk/res/android}"
OUT = ROOT / "marketing/play-store-assets"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def android_vector_svg() -> bytes:
    src = ROOT / "app/src/main/res/drawable/ic_empire_foreground.xml"
    root = ET.fromstring(src.read_text(encoding="utf-8"))
    assert root.tag == "vector", "Expected Android VectorDrawable"
    width = float(root.get(A + "viewportWidth", "0"))
    height = float(root.get(A + "viewportHeight", "0"))
    assert (width, height) == (108.0, 108.0)
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 108 108">',
        '<defs><linearGradient id="icon-bg" x1="0" y1="0" x2="0" y2="1">',
        '<stop offset="0" stop-color="#050914"/>',
        '<stop offset="0.5" stop-color="#0D1C34"/>',
        '<stop offset="1" stop-color="#172943"/>',
        '</linearGradient></defs>',
        '<rect width="108" height="108" fill="url(#icon-bg)"/>',
    ]
    for node in root:
        if node.tag != "path":
            raise ValueError(f"Unsupported launcher vector node {node.tag}")
        path = node.get(A + "pathData")
        assert path is not None and '<' not in path and '"' not in path
        fill = node.get(A + "fillColor", "none")
        if fill == "@android:color/transparent":
            fill = "none"
        assert fill == "none" or (fill.startswith("#") and len(fill) in (7, 9)), fill
        stroke = node.get(A + "strokeColor", "none")
        if stroke == "@android:color/transparent":
            stroke = "none"
        assert stroke == "none" or stroke.startswith("#"), stroke
        sw = float(node.get(A + "strokeWidth", "0"))
        parts.append(f'<path d="{path}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" />')
    parts.append("</svg>")
    return "".join(parts).encode("utf-8")


def export() -> dict:
    OUT.mkdir(parents=True, exist_ok=True)
    icon_path = OUT / "zero-to-empire-icon-512.png"
    feature_path = OUT / "zero-to-empire-feature-1024x500.png"
    cairosvg.svg2png(bytestring=android_vector_svg(), write_to=str(icon_path))
    # CairoSVG may emit RGB when the artwork is fully opaque. Google Play
    # specifically requires a 32-bit icon, so force RGBA before validation.
    with Image.open(icon_path) as image:
        image.convert("RGBA").save(icon_path, "PNG", optimize=True)
    source_feature = ROOT / "marketing/play-store-feature-graphic.svg"
    cairosvg.svg2png(url=str(source_feature), write_to=str(feature_path))
    # Play requires 24-bit RGB, explicitly remove the PNG alpha channel.
    with Image.open(feature_path) as image:
        rgb = Image.new("RGB", image.size, "#050914")
        rgb.paste(image.convert("RGBA"), mask=image.convert("RGBA").getchannel("A"))
        rgb.save(feature_path, "PNG", optimize=True)
    with Image.open(icon_path) as image:
        assert image.size == (512, 512) and image.mode == "RGBA", "Play icon must be RGBA 512²"
    with Image.open(feature_path) as image:
        assert image.size == (1024, 500) and image.mode == "RGB", "Play feature must be RGB 1024×500"
    assert icon_path.stat().st_size <= 1024 * 1024, "Play icon size exceeds 1024 KiB"
    manifest = {
        "format": "zte-store-assets-v1",
        "source": "repository-owned Android vector launcher and feature graphic",
        "artifacts": [
            {"path": str(icon_path.relative_to(ROOT)), "size": "512x512", "mode": "RGBA", "sha256": sha256(icon_path)},
            {"path": str(feature_path.relative_to(ROOT)), "size": "1024x500", "mode": "RGB", "sha256": sha256(feature_path)}
        ],
        "note": "Store artwork, not gameplay screenshots; screenshots must be captured from the current build on Android."
    }
    (OUT / "store-artwork-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return manifest


if __name__ == "__main__":
    export()
