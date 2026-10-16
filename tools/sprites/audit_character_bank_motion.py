#!/usr/bin/env python3
"""Heuristic 42px character motion audit, never a semantic approval gate.

Rank review effort using actual rendered animation changes rather than file
existence. Source atlas bytes, hashes and review-only provenance are verified.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import statistics
import zipfile
from pathlib import Path

from PIL import Image, ImageChops, ImageStat

FRAMES = {"IDLE": 6, "WALK": 8, "WORK": 10, "CARRY": 8, "REPAIR": 10, "CELEB": 8}
MOBILE_SIZE = 42
DAY = (189, 203, 211, 255)
NIGHT = (16, 27, 41, 255)
HEAD_ANCHOR_ACTION = {"OP": "WALK", "LOG": "WALK", "ENG": "IDLE", "TECH": "IDLE"}
# Conservative pre-screening: a distance is not proof that two faces differ.
HEAD_REVIEW_THRESHOLD = 11.0
HEAD_EXTREME_THRESHOLD = 30.0



def composite(tile: Image.Image, color: tuple[int, ...]) -> Image.Image:
    surface = Image.new("RGBA", tile.size, color)
    surface.alpha_composite(tile)
    return surface.convert("RGB").resize(
        (MOBILE_SIZE, MOBILE_SIZE), Image.Resampling.LANCZOS
    )


def change(first: Image.Image, second: Image.Image) -> float:
    means = ImageStat.Stat(ImageChops.difference(first, second)).mean
    return sum(means) / (len(means) * 255)


def motion_stats(blob: bytes, count: int) -> dict:
    with Image.open(io.BytesIO(blob)) as source:
        source.load()
        if source.size != (1024, 1024) or source.mode != "RGBA":
            raise ValueError("Expected a decoded 1024x1024 RGBA atlas")
        tiles = [
            source.crop(((i % 4) * 256, (i // 4) * 256,
                         (i % 4 + 1) * 256, (i // 4 + 1) * 256))
            for i in range(count)
        ]
    scores, lower_scores, seams = [], [], []
    for background in (DAY, NIGHT):
        images = [composite(tile, background) for tile in tiles]
        scores.extend(change(images[i - 1], images[i]) for i in range(1, count))
        seams.append(change(images[-1], images[0]))
        lower_scores.extend(
            change(
                images[i - 1].crop((0, 23, 42, 42)),
                images[i].crop((0, 23, 42, 42)),
            ) for i in range(1, count)
        )
    return {
        "mobile_render_px": MOBILE_SIZE,
        "mean_frame_change": round(statistics.mean(scores), 5),
        "median_frame_change": round(statistics.median(scores), 5),
        "min_frame_change": round(min(scores), 5),
        "mean_lower_body_change": round(statistics.mean(lower_scores), 5),
        "low_change_pairs": sum(value < 0.004 for value in scores) // 2,
        "loop_seam_change": round(statistics.mean(seams), 5),
    }


def head_thumbnail(blob: bytes) -> Image.Image:
    """Normalized first-frame helmet/face crop for review, not recognition.

    Foreground-based head positioning avoids treating a large handheld crate as
    the person's face. A fixed neutral composite makes alpha-crop edges
    comparable. A 64px color difference is merely a triage signal.
    """
    with Image.open(io.BytesIO(blob)) as source:
        source.load()
        if source.mode != "RGBA" or source.size != (1024, 1024):
            raise ValueError("Expected a decoded RGBA 1024x1024 atlas")
        frame = source.crop((0, 0, 256, 256))
    alpha = frame.getchannel("A")
    bounds = alpha.getbbox()
    if bounds is None:
        raise ValueError("Empty first frame has no head to review")
    _, top, _, bottom = bounds
    span = bottom - top
    if span < 70:
        raise ValueError("First-frame subject too small for a head comparison")
    upper = alpha.crop((0, top, 256, min(256, top + max(1, round(span * .28)))))
    width, height = upper.size
    pixels = upper.load()
    weighted_x, total = 0, 0
    for y in range(height):
        for x in range(width):
            if pixels[x, y] >= 80:
                weighted_x += x
                total += 1
    if total < 30:
        raise ValueError("First-frame head has insufficient visible pixels")
    xmid = round(weighted_x / total)
    cropped = frame.crop((xmid - 47, max(0, top - 5),
                          xmid + 47, min(256, top + max(1, round(span * .33)))))
    canvas = Image.new("RGBA", cropped.size, (170, 181, 193, 255))
    canvas.alpha_composite(cropped)
    return canvas.convert("RGB").resize((64, 64), Image.Resampling.BILINEAR)


def head_difference(first: Image.Image, second: Image.Image) -> float:
    """RGB mean absolute difference of centered head thumbnails (0..255)."""
    return round(statistics.mean(
        ImageStat.Stat(ImageChops.difference(first, second)).mean
    ), 2)


def analyze(bank_path: Path, output_path: Path) -> dict:
    with zipfile.ZipFile(bank_path) as bank:
        if bank.namelist().count("candidate-bank-index.json") != 1:
            raise ValueError("Missing candidate bank index")
        metadata = json.loads(bank.read("candidate-bank-index.json"))
        entries = metadata.get("bank_entries")
        if (not isinstance(entries, list)
                or len(entries) != metadata.get("candidate_count")
                or metadata.get("automatic_semantic_approval") is not False
                or metadata.get("automatic_runtime_promotion") is not False):
            raise ValueError("Untrusted candidate bank review state")
        results, seen, first_heads = [], set(), {}
        for row in entries:
            asset_id = str(row.get("id") or "")
            parts = asset_id.split("-")
            if (len(parts) != 3 or parts[0] != "CHR"
                    or parts[1] not in {"OP", "LOG", "ENG", "TECH"}
                    or parts[2] not in FRAMES or asset_id in seen):
                raise ValueError("Unexpected or duplicate character ID " + asset_id)
            seen.add(asset_id)
            filename = "zte_chr_" + parts[1].lower() + "_" + parts[2].lower() + "_final.png"
            if (row.get("filename") != filename
                    or bank.namelist().count("candidates/" + filename) != 1
                    or row.get("strict_approved") is not False
                    or row.get("runtime_promoted") is not False):
                raise ValueError("Untrusted candidate source: " + asset_id)
            blob = bank.read("candidates/" + filename)
            if (len(blob) != row.get("bytes")
                    or hashlib.sha256(blob).hexdigest() != row.get("sha256")):
                raise ValueError("Candidate PNG SHA-256 mismatch: " + asset_id)
            metrics = motion_stats(blob, FRAMES[parts[2]])
            first_heads[asset_id] = head_thumbnail(blob)
            flags = []
            if parts[2] != "IDLE" and metrics["mean_frame_change"] < 0.012:
                flags.append("LOW_MOBILE_FRAME_CHANGE_REVIEW")
            if parts[2] == "WALK" and metrics["mean_lower_body_change"] < 0.007:
                flags.append("WALK_LOWER_BODY_MOTION_REVIEW")
            if parts[2] != "IDLE" and metrics["low_change_pairs"] >= 2:
                flags.append("NEAR_STATIC_TRANSITIONS_REVIEW")
            if (parts[2] != "IDLE"
                    and metrics["loop_seam_change"] >= 3 * max(metrics["median_frame_change"], 0.003)
                    and metrics["loop_seam_change"] > 0.025):
                flags.append("VISIBLE_LOOP_SEAM_REVIEW")
            prior_flags = [str(x) for x in row.get("deferred_art_warnings") or []]
            results.append({
                "id": asset_id,
                "source_type": row.get("source_type"),
                "sha256": row["sha256"],
                "frames": FRAMES[parts[2]],
                "motion_metrics": metrics,
                "new_motion_flags": flags,
                "review_flags": sorted(set(flags + prior_flags)),
                "needs_motion_attention": bool(flags),
                "strict_approved": False,
                "runtime_promoted": False,
            })
    # Compare each role with its coherent visual reference. OP/LOG usually
    # have no unfinished IDLE in the bank; their WALK is the review reference.
    # A technically accepted engineer IDLE is a baseline, not an approval.
    role_anchor = {}
    for role, preferred_action in HEAD_ANCHOR_ACTION.items():
        candidates = sorted(asset_id for asset_id in first_heads
                            if asset_id.startswith("CHR-" + role + "-"))
        if candidates:
            preferred = "CHR-" + role + "-" + preferred_action
            role_anchor[role] = preferred if preferred in first_heads else candidates[0]
    for row in results:
        role = row["id"].split("-")[1]
        reference_id = role_anchor[role]
        distance = head_difference(first_heads[reference_id], first_heads[row["id"]])
        identity_flags = []
        if reference_id != row["id"] and distance >= HEAD_REVIEW_THRESHOLD:
            identity_flags.append("CROSS_ACTION_HEAD_IDENTITY_REVIEW")
        if reference_id != row["id"] and distance >= HEAD_EXTREME_THRESHOLD:
            identity_flags.append("CROSS_ACTION_VISUAL_STYLE_REVIEW")
        row["head_identity_metrics"] = {
            "reference_id": reference_id,
            "mean_head_rgb_change": distance,
            "heuristic_only": True,
        }
        row["new_identity_flags"] = identity_flags
        row["needs_identity_attention"] = bool(identity_flags)
        row["review_flags"] = sorted(set(row["review_flags"] + identity_flags))
    ranked = sorted(
        results, key=lambda row: (
            not (row["needs_motion_attention"] or row["needs_identity_attention"]),
            -len(row["new_identity_flags"]),
            row["motion_metrics"]["mean_frame_change"],
            row["id"],
        )
    )
    audit = {
        "schema_version": 1,
        "review_only": True,
        "automatic_semantic_approval": False,
        "automatic_runtime_promotion": False,
        "target_total": metadata["target_total"],
        "strict_done": metadata["strict_done"],
        "candidate_count": len(results),
        "mobile_render_px": MOBILE_SIZE,
        "heuristic_only_notice": (
            "Frame differences are not semantic quality or AAA approval. "
            "Visual review and gameplay validation are still required."
        ),
        "motion_attention_count": sum(bool(row["new_motion_flags"]) for row in results),
        "identity_attention_count": sum(bool(row["new_identity_flags"]) for row in results),
        "head_identity_reference": role_anchor,
        "assets": ranked,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8")
    return audit


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = analyze(args.bank, args.output)
    print("MOBILE_AUDIT_CANDIDATES=" + str(data["candidate_count"]))
    print("MOBILE_AUDIT_NEED_MOTION_REVIEW=" + str(data["motion_attention_count"]))
    print("MOBILE_AUDIT_NEED_IDENTITY_REVIEW=" + str(data["identity_attention_count"]))
    for item in data["assets"]:
        if item["new_motion_flags"]:
            print("MOBILE_AUDIT_RISK=" + item["id"] + ":" +
                  ",".join(item["new_motion_flags"]))
        if item["new_identity_flags"]:
            print("MOBILE_AUDIT_IDENTITY_RISK=" + item["id"] + ":" +
                  ",".join(item["new_identity_flags"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
