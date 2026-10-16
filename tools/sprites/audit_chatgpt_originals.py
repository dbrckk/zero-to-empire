#!/usr/bin/env python3
"""Risk-only visual QA for the 18 locally authored Zero to Empire atlases.

Designed to report and reproduce defects without modifying any sprites or
promoting manifest progress. Passing never means premium/semantic approval.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from xml.etree import ElementTree as ET
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools/sprites"))
from character_semantic_gate import clip_risk, celebration_arm_reach_counts, palette_distance, _body_region_color_signature

FRAME_COUNTS = {"IDLE":6,"WALK":8,"WORK":10,"CARRY":8,"REPAIR":10,"CELEB":8}
ROLES = ("OP","LOG","ENG")
# In this authored atlas the fixed service console starts to the right of
# the worker. Its large horizontal footprint must not masquerade as a cropped
# portrait. The main actor (head, torso, legs) occupies the left 202px.
ENG_REPAIR_ACTOR_GEOMETRY_RIGHT = 202


def _verified_fixed_engineer_station(base: Path, count: int) -> bool:
    """Require every editable SVG to contain the identical fixed station.

    Without this provenance evidence we use the strict full-composite
    geometry assessment; imported or mismatched atlases get no exception.
    """
    reference = None
    for i in range(count):
        source = base / "src_svg" / "ENG" / "REPAIR" / f"{i:02d}.svg"
        try:
            root = ET.parse(source).getroot()
        except (OSError, ET.ParseError):
            return False
        stations = [
            element for element in root.iter()
            if element.get("data-repair-station") == "ENG"
            and element.get("data-fixed-socket") == "true"
        ]
        if len(stations) != 1:
            return False
        socket = [
            element for element in stations[0].iter()
            if element.tag.endswith("circle")
            and float(element.get("r", "0")) >= 6
        ]
        if len(socket) != 1 or not (216 <= float(socket[0].get("cx", "0")) <= 222):
            return False
        markup = ET.tostring(stations[0], encoding="utf-8")
        if reference is not None and markup != reference:
            return False
        reference = markup
    return reference is not None


def inspect(atlas: Path, role: str, action: str) -> dict:
    with Image.open(atlas) as source:
        if source.size != (1024,1024):
            raise ValueError(f"Wrong 1024 atlas: {atlas}")
        image = source.convert("RGBA")
    count = FRAME_COUNTS[action]
    frames = [
        image.crop(((i%4)*256,(i//4)*256,(i%4+1)*256,(i//4+1)*256))
        for i in range(count)
    ]
    # ENG REPAIR is a deliberately composite *scene*: a separately authored
    # fixed service console extends the overall width without clipping the
    # engineer. Only its full-body silhouette/feet geometry is isolated; the
    # entire atlas remains subject to palette, tool-motion and loop QA.
    # This exception requires the matching, stationary editable SVG fixture.
    station_verified = (
        role == "ENG" and action == "REPAIR"
        and _verified_fixed_engineer_station(atlas.parent.parent, count)
    )
    actor_frames = None
    if station_verified:
        actor_frames = []
        for frame in frames:
            isolated = Image.new("RGBA", frame.size, (0, 0, 0, 0))
            isolated.paste(
                frame.crop((0, 0, ENG_REPAIR_ACTOR_GEOMETRY_RIGHT, 256)),
                (0, 0),
            )
            actor_frames.append(isolated)
    flagged = clip_risk(frames, action, geometry_frames=actor_frames)
    evidence = {
        "id": f"CHR-{role}-{action}", "frame_count": count,
        "risk_level": flagged["risk_level"], "flags": flagged.get("flags", []),
        "image_only_semantic_approval": False,
        "explicit_visual_review_required": True,
        "runtime_approved": False, "strict_done_granted": False,
        "headgear_color_drift": flagged.get("max_headgear_adjacent_color_distance"),
        "body_prop_color_drift": flagged.get("max_mid_body_prop_adjacent_color_distance"),
        "head_shape_drift": flagged.get("max_head_structure_drift"),
        "min_relative_frame_height": flagged.get("min_relative_frame_height"),
        "action_pose_metrics": flagged.get("action_pose_metrics", {}),
    }
    if role == "ENG" and action == "REPAIR":
        evidence["fixed_service_station_svg_verified"] = station_verified
        evidence["actor_only_geometry_assessment"] = station_verified
        evidence["actor_geometry_right_px"] = (
            ENG_REPAIR_ACTOR_GEOMETRY_RIGHT if station_verified else None
        )
    if action == "CELEB":
        raised = celebration_arm_reach_counts(frames)
        evidence["raised_arm_frame_scores"] = raised
        evidence["clearly_raised_arm_frames"] = sum(score >= 28 for score in raised)
        if evidence["clearly_raised_arm_frames"] < 3:
            evidence["flags"].append("CELEBRATION_NO_CLEAR_OVERHEAD_ARM_GESTURE_RISK")
            evidence["risk_level"] = "BLOCKING"
    if action in {"WALK","CARRY"}:
        # The sprite can shift limbs even while its sprite bounding box stays
        # fixed. Record a lower-body alpha-change proxy as rejection evidence.
        lower = [
            f.getchannel("A").crop((0,140,256,250)).point(
                lambda value: 255 if value >= 80 else 0
            ) for f in frames
        ]
        scores = []
        for a,b in zip(lower, lower[1:]+lower[:1]):
            aa=list(a.getdata());bb=list(b.getdata())
            inter=sum(x and y for x,y in zip(aa,bb))
            union=sum(x or y for x,y in zip(aa,bb))
            scores.append(round(1-inter/union,4) if union else 0.0)
        # Include last-to-first transition: a sprite loop can be smooth
        # internally but visibly snap at its playback boundary.
        evidence["lower_body_adjacent_changes"] = scores
        evidence["lower_body_loop_seam_change"] = scores[-1]
        evidence["lower_body_mean_change"] = round(sum(scores)/len(scores),4)
        # Reject a large wraparound jump relative to ordinary frame motion.
        internal = sorted(scores[:-1])
        typical = internal[len(internal)//2]
        evidence["lower_body_typical_internal_change"] = typical
        if scores[-1] > max(.30, 2.5 * typical):
            evidence["flags"].append("LOCOMOTION_LOOP_SEAM_SNAP_RISK")
            evidence["risk_level"] = "BLOCKING"
        if evidence["lower_body_mean_change"] < .075:
            evidence["flags"].append("LOCOMOTION_LOWER_BODY_TOO_STATIC_RISK")
            evidence["risk_level"]="BLOCKING"
    if action in {"WORK", "REPAIR", "CARRY", "CELEB"}:
        # Detect a tool, raised arm or cargo handle popping at the wrap.
        # This is a rejection signal, not semantic or visual approval.
        upper = [
            f.getchannel("A").crop((0, 0, 256, 145)).point(
                lambda value: 255 if value >= 80 else 0
            ) for f in frames
        ]
        upper_changes = []
        for a, b in zip(upper, upper[1:] + upper[:1]):
            aa = list(a.getdata())
            bb = list(b.getdata())
            intersection = sum(x and y for x, y in zip(aa, bb))
            union = sum(x or y for x, y in zip(aa, bb))
            upper_changes.append(round(1 - intersection / union, 4) if union else 0.0)
        typical = sorted(upper_changes[:-1])[len(upper_changes[:-1]) // 2]
        evidence["upper_body_loop_seam_change"] = upper_changes[-1]
        evidence["upper_body_typical_internal_change"] = typical
        if upper_changes[-1] > max(.30, 3.0 * typical):
            evidence["flags"].append("UPPER_BODY_LOOP_SEAM_SNAP_RISK")
            evidence["risk_level"] = "BLOCKING"
    return evidence


def audit(base: Path) -> dict:
    candidates=base/"candidates"
    results=[]
    for role in ROLES:
        for action in FRAME_COUNTS:
            name=f"zte_chr_{role.lower()}_{action.lower()}_final.png"
            result=inspect(candidates/name,role,action)
            results.append(result)
    # Same-role cross-action identity must be audited, not just adjacent
    # frames within an action. All unfinished character art is authored here
    # with one fixed role rig, so compare every action against its local IDLE.
    # The comparison is reject-only and never grants strict approval.
    for role in ROLES:
        idle_path=candidates/f"zte_chr_{role.lower()}_idle_final.png"
        with Image.open(idle_path) as image:
            idle=image.convert("RGBA").crop((0,0,256,256))
        anchor=_body_region_color_signature(idle,0,.28)
        for row in results:
            if row["id"]==f"CHR-{role}-IDLE":
                row["same_role_idle_head_color_distance"]=0.0
                continue
            if not row["id"].startswith(f"CHR-{role}-"):
                continue
            action=row["id"].split("-")[-1]
            with Image.open(candidates/f"zte_chr_{role.lower()}_{action.lower()}_final.png") as image:
                atlas=image.convert("RGBA")
            frame=atlas.crop((0,0,256,256))
            delta=palette_distance(anchor,_body_region_color_signature(frame,0,.28))
            row["same_role_idle_head_color_distance"]=round(delta,4)
            if delta>.28:
                row["flags"].append("CROSS_ACTION_ROLE_HEAD_IDENTITY_RISK")
                row["risk_level"]="BLOCKING"
    blocked=sum(row["risk_level"]=="BLOCKING" for row in results)
    return {
        "schema_version": 1,
        "assessment": "technical_and_image_only_reject_risks",
        "source": "chatgpt_local_original_animated_atlases",
        "review_only": True, "semantically_approved": False,
        "automatic_strict_done": 0, "android_runtime_approved": False,
        "asset_count": len(results), "frames_checked": sum(r["frame_count"] for r in results),
        "blocking_risk_count": blocked,
        "requires_human_visual_review": len(results),
        "limitations": [
            "Image-only thresholds can reject candidates but cannot prove art quality",
            "Stable palettes and silhouettes do not prove physical tool contact",
            "Cross-action head palette similarity is not proof of the same character",
            "Mobile readability, animation fluidity and AAA visual style require review",
        ],
        "assets": results,
    }


def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--base",type=Path,default=Path("art/incoming/chatgpt-original"))
    args=parser.parse_args()
    report=audit(args.base)
    dest=args.base/"visual-risk-qa.json"
    dest.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print("CHATGPT_ORIGINAL_VISUAL_RISK_AUDIT=18")
    print(f"LOCAL_SPRITE_BLOCKING_RISK_COUNT={report['blocking_risk_count']}")
    print("VISUAL_SEMANTIC_APPROVAL=false")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
