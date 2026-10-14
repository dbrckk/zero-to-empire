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
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools/sprites"))
from character_semantic_gate import clip_risk, celebration_arm_reach_counts

FRAME_COUNTS = {"IDLE":6,"WALK":8,"WORK":10,"CARRY":8,"REPAIR":10,"CELEB":8}
ROLES = ("OP","LOG","ENG")


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
    flagged = clip_risk(frames, action)
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
        for a,b in zip(lower, lower[1:]):
            aa=list(a.getdata());bb=list(b.getdata())
            inter=sum(x and y for x,y in zip(aa,bb))
            union=sum(x or y for x,y in zip(aa,bb))
            scores.append(round(1-inter/union,4) if union else 0.0)
        evidence["lower_body_adjacent_changes"] = scores
        evidence["lower_body_mean_change"] = round(sum(scores)/len(scores),4)
        if evidence["lower_body_mean_change"] < .075:
            evidence["flags"].append("LOCOMOTION_LOWER_BODY_TOO_STATIC_RISK")
            evidence["risk_level"]="BLOCKING"
    return evidence


def audit(base: Path) -> dict:
    candidates=base/"candidates"
    results=[]
    for role in ROLES:
        for action in FRAME_COUNTS:
            name=f"zte_chr_{role.lower()}_{action.lower()}_final.png"
            result=inspect(candidates/name,role,action)
            results.append(result)
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
