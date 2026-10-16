#!/usr/bin/env python3
"""Make safe, deterministic, review-only head/helmet continuity alternatives.

Never replace the canonical candidate bank, an Android resource, or a strict
approval. Reuse the SHA-verified first-frame role reference from the exact
published candidate bank; all modified poses must pass the existing
conservative full-body head-registration guard. One rejected pose rejects
that whole *alternative*, avoiding flickering mixed-identity animations.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont

from audit_character_bank_motion import FRAMES, head_difference, head_thumbnail, motion_stats
from character_head_identity_lock import lock_head_to_idle
from character_identity_polish_mobile_review import write_mobile_review

NAME = re.compile(r"^CHR-(OP|LOG|ENG|TECH)-(IDLE|WALK|WORK|CARRY|REPAIR|CELEB)$")
MAX_BLOB = 20 * 1024 * 1024
REQUIRED_FLAG = "CROSS_ACTION_HEAD_IDENTITY_REVIEW"
MAX_HEAD_AFTER = 8.0
MAX_REMAINING_ERROR_FRACTION = .65


def _atlas(blob: bytes, asset_id: str) -> Image.Image:
    if not 100 <= len(blob) <= MAX_BLOB:
        raise ValueError("Invalid atlas byte size: " + asset_id)
    with Image.open(io.BytesIO(blob)) as image:
        image.load()
        if image.size != (1024, 1024) or image.mode != "RGBA":
            raise ValueError("Invalid 1024x1024 RGBA atlas: " + asset_id)
        return image.copy()


def _frames(atlas: Image.Image, count: int) -> list[Image.Image]:
    return [
        atlas.crop(((i % 4) * 256, (i // 4) * 256,
                    (i % 4 + 1) * 256, (i // 4 + 1) * 256))
        for i in range(count)
    ]


def _pack(frames: list[Image.Image]) -> bytes:
    image = Image.new("RGBA", (1024, 1024))
    for i, frame in enumerate(frames):
        image.alpha_composite(frame, ((i % 4) * 256, (i // 4) * 256))
    result = io.BytesIO()
    image.save(result, "PNG", optimize=True)
    return result.getvalue()


def _font(size: int) -> ImageFont.ImageFont:
    for candidate in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                      "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            pass
    return ImageFont.load_default()


def _comparison(rows: list[dict], destination: Path) -> None:
    """Provide a lightweight visual comparison without modifying the source."""
    width, unit, header, height = 786, 242, 74, 266
    canvas = Image.new("RGB", (width, header + height * len(rows) + 12),
                       (13, 23, 36))
    pen = ImageDraw.Draw(canvas)
    font = _font(17)
    small = _font(12)
    pen.text((16, 12), "ZERO TO EMPIRE | RECHERCHE D'IDENTITE", fill=(241, 248, 255), font=font)
    pen.text((16, 39), "PROPOSITIONS DE REVUE UNIQUEMENT - aucune validation automatique",
             fill=(179, 198, 217), font=small)
    for n, row in enumerate(rows):
        y = header + n * height
        for j, (label, img) in enumerate((
            ("REFERENCE", row["reference_frame"]),
            ("ORIGINAL", row["original_frame"]),
            ("VISAGE AJUSTE", row["polished_frame"]),
        )):
            x = 16 + j * (unit + 12)
            pen.rounded_rectangle((x, y, x + unit, y + 254),
                                  radius=8, fill=(29, 46, 63), outline=(78, 106, 124))
            pen.text((x + 8, y + 7), label, fill=(223, 239, 248), font=small)
            background = Image.new("RGBA", (208, 208), (194, 207, 218, 255))
            background.alpha_composite(img.resize((208, 208), Image.Resampling.LANCZOS))
            canvas.paste(background.convert("RGB"), (x + 17, y + 30))
            pen.text((x + 8, y + 237), row["id"], fill=(190, 208, 223), font=small)
    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination, "PNG", optimize=True)


def build(bank_path: Path, audit_path: Path, destination: Path,
          report_path: Path, comparison_path: Path | None = None,
          mobile_review_path: Path | None = None) -> dict:
    """An all-or-nothing alternative per action, fail-closed on provenance."""
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    audit_rows = audit.get("assets")
    if (audit.get("review_only") is not True
            or audit.get("automatic_semantic_approval") is not False
            or audit.get("automatic_runtime_promotion") is not False
            or not isinstance(audit_rows, list)
            or audit.get("candidate_count") != len(audit_rows)):
        raise ValueError("Untrusted review-only identity audit")
    by_audit = {x.get("id"): x for x in audit_rows if isinstance(x, dict)}
    if len(by_audit) != len(audit_rows):
        raise ValueError("Duplicate or invalid audit IDs")

    with zipfile.ZipFile(bank_path) as bank:
        names = bank.namelist()
        if names.count("candidate-bank-index.json") != 1:
            raise ValueError("Missing or duplicated bank index")
        meta = json.loads(bank.read("candidate-bank-index.json"))
        entries = meta.get("bank_entries")
        if (not isinstance(entries, list)
                or len(entries) != meta.get("candidate_count")
                or meta.get("automatic_semantic_approval") is not False
                or meta.get("automatic_runtime_promotion") is not False):
            raise ValueError("Untrusted candidate bank")
        verified: dict[str, dict] = {}
        for entry in entries:
            asset_id = str(entry.get("id") or "")
            parsed = NAME.fullmatch(asset_id)
            if parsed is None or asset_id in verified:
                raise ValueError("Unknown or duplicate asset ID " + asset_id)
            fname = "zte_chr_" + parsed.group(1).lower() + "_" + parsed.group(2).lower() + "_final.png"
            if (entry.get("filename") != fname
                    or entry.get("strict_approved") is not False
                    or entry.get("runtime_promoted") is not False
                    or names.count("candidates/" + fname) != 1):
                raise ValueError("Missing or untrusted bank entry: " + asset_id)
            blob = bank.read("candidates/" + fname)
            sha = hashlib.sha256(blob).hexdigest()
            if sha != entry.get("sha256") or len(blob) != entry.get("bytes"):
                raise ValueError("Candidate SHA-256/size mismatch: " + asset_id)
            image = _atlas(blob, asset_id)
            audit_row = by_audit.get(asset_id)
            if (not audit_row or audit_row.get("sha256") != sha
                    or audit_row.get("strict_approved") is not False
                    or audit_row.get("runtime_promoted") is not False
                    or not isinstance(audit_row.get("new_identity_flags"), list)
                    or not isinstance(audit_row.get("head_identity_metrics"), dict)):
                raise ValueError("Missing/stale/unsafe identity audit for " + asset_id)
            verified[asset_id] = {
                "atlas": image, "blob": blob, "sha256": sha, "entry": entry,
                "audit": audit_row, "role": parsed.group(1),
                "action": parsed.group(2),
            }
    if set(verified) != set(by_audit):
        raise ValueError("Audit covers a different character candidate set")
    if not verified:
        raise ValueError("Empty candidate bank")
    # A plausible same-role atlas is not necessarily the intended reference.
    # Lock every polish proposal to the audit's declared canonical role anchor,
    # preventing stale or edited audit records from silently using another pose.
    anchors = audit.get("head_identity_reference")
    if not isinstance(anchors, dict):
        raise ValueError("Missing role identity anchors")
    for asset_id, record in verified.items():
        role = record["role"]
        reference_id = anchors.get(role)
        reference = verified.get(reference_id)
        metrics = record["audit"]["head_identity_metrics"]
        if (not isinstance(reference_id, str) or reference is None
                or reference["role"] != role
                or metrics.get("reference_id") != reference_id):
            raise ValueError("Invalid canonical role identity anchor: " + asset_id)
        if asset_id == reference_id:
            if (metrics.get("mean_head_rgb_change") != 0
                    or record["audit"]["new_identity_flags"]):
                raise ValueError("Invalid anchor self-comparison: " + asset_id)

    alternatives, skipped, previews, gallery_rows = [], [], [], []
    members: list[tuple[str, bytes]] = []
    for asset_id, record in sorted(verified.items()):
        flags = record["audit"]["new_identity_flags"]
        if REQUIRED_FLAG not in flags:
            continue
        reference_id = record["audit"]["head_identity_metrics"].get("reference_id")
        anchor = verified.get(reference_id)
        if (not isinstance(reference_id, str) or anchor is None
                or anchor["role"] != record["role"] or reference_id == asset_id):
            raise ValueError("Missing/inconsistent same-role visual reference " + asset_id)
        original = _frames(record["atlas"], FRAMES[record["action"]])
        reference_frame = _frames(anchor["atlas"], FRAMES[anchor["action"]])[0]
        before = head_difference(
            head_thumbnail(anchor["blob"]), head_thumbnail(record["blob"])
        )
        recorded_before = record["audit"]["head_identity_metrics"].get("mean_head_rgb_change")
        if (not isinstance(recorded_before, (float, int))
                or abs(before - recorded_before) > .035
                or before < 11):
            raise ValueError("Untrusted/stale head difference metrics: " + asset_id)
        fixed: list[Image.Image] = []
        skip_reason = None
        for number, frame in enumerate(original):
            corrected, applied, why = lock_head_to_idle(frame, reference_frame)
            if not applied:
                skip_reason = f"frame-{number}: {why}"
                break
            # Preserve feet, lower torso, arms and tools exactly. Head
            # transfer must not masquerade as full-action regeneration.
            box = frame.getchannel("A").getbbox()
            if box is None:
                skip_reason = f"frame-{number}: empty-alpha"
                break
            lower_y = min(255, box[1] + round((box[3] - box[1]) * .46))
            if ImageChops.difference(frame.crop((0, lower_y, 256, 256)),
                                     corrected.crop((0, lower_y, 256, 256))).getbbox():
                skip_reason = f"frame-{number}: lower-body-mutated"
                break
            fixed.append(corrected)
        if skip_reason:
            skipped.append({"id": asset_id, "reference_id": reference_id,
                            "reason": skip_reason,
                            "frames_applied_before_reject": len(fixed),
                            "original_sha256": record["sha256"]})
            continue
        blob = _pack(fixed)
        after = head_difference(head_thumbnail(anchor["blob"]), head_thumbnail(blob))
        if (after >= before * MAX_REMAINING_ERROR_FRACTION
                or after > MAX_HEAD_AFTER):
            skipped.append({"id": asset_id, "reference_id": reference_id,
                            "reason": f"insufficient-head-improvement={before:.2f}->{after:.2f}",
                            "frames_applied_before_reject": len(fixed),
                            "original_sha256": record["sha256"]})
            continue
        # Recheck real 42px animation readability after head retouch. A
        # head-color improvement cannot justify a newly static animation.
        # The motion audit is a conservative warning, not semantic approval.
        original_motion = motion_stats(record["blob"], len(original))
        polished_motion = motion_stats(blob, len(fixed))
        motion_warning = (
            polished_motion["mean_frame_change"] < original_motion["mean_frame_change"] * .65
            or polished_motion["low_change_pairs"] > original_motion["low_change_pairs"]
            or polished_motion["mean_lower_body_change"] < original_motion["mean_lower_body_change"] * .95
        )
        # A visually improved face cannot compensate for a regressed 42px
        # action. Reject the complete alternative, rather than publishing
        # a sprite known to have a motion regression for later selection.
        if motion_warning:
            skipped.append({
                "id": asset_id, "reference_id": reference_id,
                "reason": "mobile-motion-regression-after-head-polish",
                "frames_applied_before_reject": len(fixed),
                "original_sha256": record["sha256"],
                "mobile_motion_before": original_motion,
                "mobile_motion_after": polished_motion,
            })
            continue
        filename = asset_id.lower().replace("-", "_") + "_head-polish.png"
        destination_name = "review-alternatives/" + filename
        members.append((destination_name, blob))
        alternatives.append({
            "id": asset_id, "reference_id": reference_id,
            "source_sha256": record["sha256"],
            "reference_sha256": anchor["sha256"],
            "alternative_sha256": hashlib.sha256(blob).hexdigest(),
            "alternative_bytes": len(blob),
            "path": destination_name,
            "atlas_size": [1024, 1024],
            "frames": len(fixed), "frames_head_locked": len(fixed),
            "head_rgb_before": before, "head_rgb_after": after,
            "mobile_motion_before": original_motion,
            "mobile_motion_after": polished_motion,
            "mobile_motion_regression_review": motion_warning,
            "review_only": True, "strict_approved": False,
            "runtime_promoted": False,
            "full_character_action_regeneration": False,
            "semantic_review_required": True,
        })
        previews.append({"id": asset_id, "reference_frame": reference_frame,
                         "original_frame": original[0], "polished_frame": fixed[0]})
        gallery_rows.append({
            "id": asset_id, "frames": len(fixed), "reference_id": reference_id,
            "source_sha256": record["sha256"],
            "alternative_sha256": hashlib.sha256(blob).hexdigest(),
            "head_rgb_before": before, "head_rgb_after": after,
            "original_png": record["blob"], "alternative_png": blob,
        })

    report = {
        "schema_version": 1, "review_only": True,
        "automatic_semantic_approval": False,
        "automatic_runtime_promotion": False,
        "source_bank_candidate_count": len(verified),
        "strict_done_unchanged": meta["strict_done"],
        "identity_flags_to_review": sum(
            REQUIRED_FLAG in row["audit"]["new_identity_flags"]
            for row in verified.values()
        ),
        "alternatives_created": len(alternatives),
        "mobile_motion_regression_review_count": sum(
            row["mobile_motion_regression_review"] for row in alternatives
        ),
        "alternatives": alternatives, "not_safe_to_polish": skipped,
        "no_canonical_bank_change": True,
        "no_android_runtime_change": True,
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    destination_index = json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as out:
        out.writestr("polish-index.json", destination_index)
        out.writestr("README.txt",
                     "Review-only alternative character atlases. These are NOT QA-approved, "
                     "not strict DONE, and NOT promoted to Android runtime.\n"
                     "Compare carefully: head/neck transfer may not match clothing, "
                     "pose, lighting or character style. Reject any visible seam.\n")
        for filename, blob in members:
            out.writestr(filename, blob)
    report_path.write_text(destination_index, encoding="utf-8")
    if comparison_path is not None:
        _comparison(previews, comparison_path)
    if mobile_review_path is not None:
        mobile = write_mobile_review(gallery_rows, mobile_review_path, meta["strict_done"])
        if mobile["assets"] != len(alternatives) or mobile["strict_done_added"] != 0:
            raise ValueError("Mobile polish review count or strict boundary drifted")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--comparison", type=Path)
    parser.add_argument("--mobile-review", type=Path)
    args = parser.parse_args()
    report = build(args.bank, args.audit, args.output, args.report, args.comparison,
                   args.mobile_review)
    print("IDENTITY_POLISH_FLAGGED=" + str(report["identity_flags_to_review"]))
    print("IDENTITY_POLISH_REVIEW_ALTERNATIVES=" + str(report["alternatives_created"]))
    print("IDENTITY_POLISH_MOTION_REGRESSION_REVIEW=" +
          str(report["mobile_motion_regression_review_count"]))
    for row in report["not_safe_to_polish"]:
        print("IDENTITY_POLISH_SKIPPED=" + row["id"] + " reason=" + row["reason"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
