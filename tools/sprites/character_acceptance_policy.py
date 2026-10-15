#!/usr/bin/env python3
"""Production-first admission policy for character *candidates*, not strict DONE.

Keep structural/technical defects blocking while recording artistic concerns as
advisories. A candidate accepted here is NOT approved for runtime promotion.
"""
from __future__ import annotations

PRODUCTION_FIRST_MODE = "production-first"

# Strict floors remain unchanged for the established review process. In the
# production-first lane an action must still have measurable nonzero motion.
STRICT_MEAN_FLOORS = {"WALK": 0.12, "WORK": 0.10, "CARRY": 0.12,
                      "REPAIR": 0.09, "CELEB": 0.10}
PRODUCTION_MEAN_FLOORS = {"WALK": 0.04, "WORK": 0.04, "CARRY": 0.04,
                          "REPAIR": 0.04, "CELEB": 0.04}
STRICT_LOWER_FLOORS = {"WALK": 0.22, "CARRY": 0.19}
PRODUCTION_LOWER_FLOORS = {"WALK": 0.05, "CARRY": 0.04}

# These are visual-quality warnings, not evidence of invalid files or missing
# actors. Unknown/new blocking flags are intentionally NOT waived.
DEFERRED_ART_FLAGS = frozenset({
    "ACTION_TRANSLATION_DOMINATES_POSE_RISK",
    "PALETTE_IDENTITY_DISCONTINUITY_RISK",
    "HEAD_FACE_HEADGEAR_COLOR_DISCONTINUITY_RISK",
    "FACE_HEADGEAR_STRUCTURE_DRIFT_RISK",
    "TOOL_CRATE_TORSO_COLOR_DISCONTINUITY_RISK",
    "BAKED_GROUND_SHADOW_RISK",
    "FRAME_SCALE_COLLAPSE_RISK",
})


def motion_floor(action: str, *, production_first: bool, lower_body: bool = False) -> float:
    action = action.upper()
    strict = STRICT_LOWER_FLOORS if lower_body else STRICT_MEAN_FLOORS
    relaxed = PRODUCTION_LOWER_FLOORS if lower_body else PRODUCTION_MEAN_FLOORS
    if action not in strict:
        raise ValueError(f"No motion floor for {action} (lower_body={lower_body})")
    return (relaxed if production_first else strict)[action]


def visual_risk_decision(risk: dict, *, production_first: bool) -> tuple[list[str], list[str]]:
    """Return (blocking_flags, deferred_review_flags) without approving art."""
    flags = list(dict.fromkeys(risk.get("flags") or []))
    if risk.get("risk_level") != "BLOCKING":
        return [], flags if production_first else []
    if not flags:  # Fail closed for an unknown blocking assessment.
        return ["UNKNOWN_BLOCKING_RISK"], []
    if not production_first:
        return flags, []
    return ([x for x in flags if x not in DEFERRED_ART_FLAGS],
            [x for x in flags if x in DEFERRED_ART_FLAGS])
