"""Same-person ten-frame mechanical repair cycle: bounded poses, fixed stance.

This describes GPU *candidate generation* only, never QA approval or runtime.
The previous deep-kneel-to-standing pose sequence produced extreme silhouette
changes, failing the unchanged adjacent-alpha-IoU >= 0.28 structural gate.
The new poses focus action on arms/tool/torso while preserving scale, feet,
identity and the connected repair point throughout the animation.
"""
from __future__ import annotations

REPAIR_POSES = (
    "medium crouch, BOTH FEET PLANTED at fixed positions, right hand tool touching waist-height repair fixture, left elbow near torso",
    "same planted stance, right elbow flexes inward, tool remains touching the SAME waist-height repair fixture",
    "same planted stance, right forearm extends along repair point, torso leans forward slightly, no standing up",
    "same planted stance, right hand presses the tool against the SAME point, left hand braces the near panel",
    "same planted stance, right elbow withdraws one hand length, torso moves back slightly while keeping repair point in view",
    "same planted stance, right hand rotates diagnostic tool for inspection, free hand steadies equipment, knees unchanged",
    "same planted stance, right forearm extends again for second tool contact at the SAME fixed repair point",
    "same planted stance, torso leans forward slightly, right wrist twists the attached compact tool, both feet remain fixed",
    "same planted stance, right hand retracts from repair point, left hand returns near torso, feet unchanged",
    "return to first medium crouch, right hand tool touching original waist-height repair fixture, seamless loop",
)


def repair_strength(frame_index: int, attempt: int, mode: str) -> float:
    """Bounded img2img denoising; preserve one subject across adjacent frames.

    The hand/tool scaffold supplies much of the pose, so reducing FLUX
    redraw strength should preserve consistent face/body silhouette. This
    does not waive the source, action, sheet or semantic review QA gates.
    """
    if not 0 <= frame_index < len(REPAIR_POSES):
        raise ValueError("Invalid REPAIR frame index")
    if attempt not in (0, 1, 2):
        raise ValueError("Invalid REPAIR retry attempt")
    if mode not in ("default", "framing", "single", "identity"):
        raise ValueError("Unexpected REPAIR retry mode")
    if frame_index == 0:
        strength = .49 + attempt * .018
    else:
        strength = .48 + frame_index * .012 + attempt * .017
    if mode in ("identity", "single"):
        strength -= .025
    elif mode == "framing":
        strength -= .015
    return round(min(.63, max(.43, strength)), 4)
