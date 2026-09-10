#!/usr/bin/env python3
"""Generate one static manifest sprite with provider failover.

Order:
1. Hugging Face ZeroGPU when available.
2. Cloudflare Workers AI FLUX.1 Schnell when HF quota/network is unavailable.

The existing isolation, normalization and technical QA contract stays authoritative.
"""
from __future__ import annotations

import base64
import io
import json
import os
import urllib.error
import urllib.request
from pathlib import Path

from PIL import Image

import hf_static_manifest_factory as factory

CF_ACCOUNT_ID = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "").strip()
CF_API_TOKEN = os.environ.get("CLOUDFLARE_API_TOKEN", "").strip()
CF_MODEL = os.environ.get("CLOUDFLARE_IMAGE_MODEL", "@cf/black-forest-labs/flux-1-schnell").strip()


def cloudflare_generate(prompt: str) -> Image.Image:
    if not CF_ACCOUNT_ID or not CF_API_TOKEN:
        raise RuntimeError("Cloudflare fallback credentials unavailable")

    model_path = CF_MODEL.replace("@cf/", "@cf/")
    url = f"https://api.cloudflare.com/client/v4/accounts/{CF_ACCOUNT_ID}/ai/run/{model_path}"
    payload = json.dumps({"prompt": prompt[:2048], "steps": 8}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {CF_API_TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "zero-to-empire-multiprovider-factory/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")
        # Cloudflare returns HTTP 429 / Workers AI code 4006 when the daily free
        # neuron allocation is exhausted. This is a provider-availability state,
        # not an asset rejection. Preserve the same rc=75 contract used by HF so
        # the shard stops immediately instead of spending requests on every target.
        low = detail.lower()
        if exc.code == 429 and (
            "daily free allocation" in low
            or "used up" in low
            or '"code":4006' in low
            or '"code": 4006' in low
        ):
            print("CLOUDFLARE_QUOTA_EXHAUSTED: daily Workers AI allocation unavailable")
            raise SystemExit(factory.QUOTA_EXIT) from exc
        raise RuntimeError(f"Cloudflare HTTP {exc.code}: {detail[:600]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Cloudflare request failed: {exc}") from exc

    image_b64 = (body.get("result") or {}).get("image")
    if not image_b64:
        raise RuntimeError(f"Cloudflare response contained no image: {str(body)[:600]}")
    return Image.open(io.BytesIO(base64.b64decode(image_b64))).convert("RGB")


def generate_with_failover(prompt: str) -> Image.Image:
    hf_error = None
    if factory.TOKEN:
        try:
            return factory.generate(prompt)
        except SystemExit as exc:
            if exc.code != factory.QUOTA_EXIT:
                raise
            hf_error = "HF quota exhausted"
        except Exception as exc:  # provider/network failure -> secondary provider
            hf_error = str(exc)

    if CF_ACCOUNT_ID and CF_API_TOKEN:
        print(f"PROVIDER_FAILOVER=cloudflare reason={hf_error or 'HF unavailable'}")
        return cloudflare_generate(prompt)

    if hf_error:
        print(f"NO_SECONDARY_PROVIDER: {hf_error}")
        raise SystemExit(factory.QUOTA_EXIT)
    raise SystemExit("No image provider credentials available")


def main() -> None:
    asset_id = factory.ASSET_ID
    if not asset_id or not asset_id.startswith(factory.SUPPORTED):
        raise SystemExit("SPRITE_TARGET must be BLD/CORE/VEH/PRP/TER")

    rid, name, desc, runtime, status = factory.manifest_item(asset_id)
    if status != "TODO":
        raise SystemExit(f"{rid} is {status}, refusing duplicate generation")

    kind = rid.split("-", 1)[0]
    raw = generate_with_failover(factory.prompt_for(rid, name, desc))
    final = factory.normalize(factory.isolate(raw), factory.TARGET_SIDE[kind])
    coverage, dominant = factory.validate(final)

    factory.INCOMING.mkdir(parents=True, exist_ok=True)
    out = factory.INCOMING / (Path(runtime).stem + ".png")
    final.save(out, "PNG", optimize=True)
    print(
        f"VALIDATED_CANDIDATE={out.relative_to(factory.ROOT)} "
        f"coverage={coverage:.1%} dominant={dominant:.1%}"
    )


if __name__ == "__main__":
    main()
