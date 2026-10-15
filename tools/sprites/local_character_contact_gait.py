"""Locally authored 2.5D contact-aware locomotion rig for OP / LOG / ENG.

No remote art generation. This is an editable candidate pose source and does
not approve sprites or replace Android resources.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

STANCE_FRACTION = .60
FLOOR_ANKLE_Y = 226.0
UPPER_LEG = 37.5
LOWER_LEG = 38.5

@dataclass(frozen=True)
class FootPose:
    hip_x: float
    hip_y: float
    knee_x: float
    knee_y: float
    ankle_x: float
    ankle_y: float
    boot_angle: float
    planted: bool
    cycle: float


def _ease(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t*t*(3.0-2.0*t)


def foot_pose(phase: float, side: str, action: str, bounce: float = 0.0, *, profile: str = "standard") -> FootPose:
    """Cyclic stance/swing path with locked stance Y and projected knee IK.

    Frame coordinates: 256x256, +Y downward. During the support fraction,
    the sole stays on a constant ground-height line; during recovery it lifts
    smoothly and advances. Feet alternate exactly half a stride apart. Knee
    lateral excursion is attenuated for a 3/4 projection, avoiding the bowed
    2D hinge produced by naïve screen-space IK.
    """
    if side not in ("L","R"):
        raise ValueError("side must be L or R")
    if action not in ("WALK","CARRY"):
        raise ValueError("contact gait is only for WALK/CARRY")
    if profile not in ("standard", "op-walk") or (profile == "op-walk" and action != "WALK"):
        raise ValueError("operator stride profile requires WALK")

    # OP-specific stance/swing profile. A small phase offset prevents eight
    # source frames from hiding heel lift behind a pair of flat planted boots.
    # Standard WALK and all CARRY geometry remain byte-for-byte equivalent.
    operator = profile == "op-walk"
    stance_fraction = .58 if operator else STANCE_FRACTION
    phase_offset = .10 if operator else 0.0
    cycle = (phase/(2*math.pi)+(0 if side == "L" else .5)+phase_offset) % 1.0
    reach = 19.0 if operator else (14.0 if action == "WALK" else 12.0)
    clearance = 21.0 if operator else (16.0 if action == "WALK" else 12.0)
    if cycle < stance_fraction:
        progress = _ease(cycle/stance_fraction)
        foot_dx = reach*(1.0-2.0*progress)
        lift = 0.0
        angle = 0.0 if operator else -4.0 + 8.0*progress
        planted = True
    else:
        progress = (cycle-stance_fraction)/(1.0-stance_fraction)
        foot_dx = reach*(-1.0+2.0*_ease(progress))
        lift = clearance*math.sin(math.pi*progress)**1.4
        angle = 4.0-8.0*_ease(progress)
        planted = False

    hip_x = (103.0 if side == "L" else 150.0) if operator else (106.0 if side == "L" else 146.0)
    hip_y = 155.0+bounce
    ankle_x = hip_x+foot_dx
    ankle_y = FLOOR_ANKLE_Y-lift
    dx,dy = ankle_x-hip_x,ankle_y-hip_y
    length = math.hypot(dx,dy)
    if not 1.0 < length < UPPER_LEG+LOWER_LEG:
        raise ValueError("Unreachable projected two-bone leg pose")

    along = (UPPER_LEG**2-LOWER_LEG**2+length**2)/(2.0*length)
    perpendicular = math.sqrt(max(0.0,UPPER_LEG**2-along**2))
    # In the airborne recovery the knee bends predominantly forward
    # (into depth), not sideways. A fully planar hinge previously pushed the
    # knee pads 20px outside the shin and looked like an exaggerated bow-leg.
    # This blend is periodic and smoothly returns to outward stance contour
    # at toe-off and heel-strike.
    contour = 1.0 if side == "L" else -1.0
    perspective_bend = .48 if planted else .48-.75*math.sin(math.pi*progress)
    knee_x = hip_x+dx*along/length+contour*(-dy/length)*perpendicular*perspective_bend
    knee_y = hip_y+dy*along/length+contour*(dx/length)*perpendicular*perspective_bend
    return FootPose(
        hip_x,hip_y,knee_x,knee_y,ankle_x,ankle_y,
        angle,planted,cycle
    )


def torso_weight_shift(phase: float, action: str) -> float:
    """Counter-sway toward the grounded stance foot, scaled for cargo."""
    if action == "WALK":
        return -2.6*math.sin(phase)
    if action == "CARRY":
        return -1.6*math.sin(phase)
    return 0.0
