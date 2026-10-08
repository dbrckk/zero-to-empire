"""Deterministic, foot-locked character weight transfer for modular TECH sprites.

No image generation, no manual pose editing, no production queue mutation.
The support-weight envelope is continuous at contact transitions. Applying
pelvis sway never changes a foot target or the original footstep timeline.
"""
from __future__ import annotations
import math
from typing import Any

STANCE_FRACTION = 0.62
AMPLITUDES_PX = {'WALK': 4.0, 'CARRY': 2.2}


def stance_load(t: float, offset: float = 0.0, stance: float = STANCE_FRACTION) -> float:
    """Smooth loading/unloading of a planted foot, zero throughout its swing."""
    if not math.isfinite(t) or not 0.5 < stance < 0.75:
        raise ValueError('Invalid phase or stance fraction')
    u = (t + offset) % 1.0
    if u >= stance:
        return 0.0
    return math.sin(math.pi * u / stance) ** 2


def support_bias(t: float) -> float:
    """Signed loading right (+1) versus left (-1); periodic over one cycle."""
    right = stance_load(t)
    left = stance_load(t, 0.5)
    denom = left + right
    return (right - left) / denom if denom > 1e-10 else 0.0


def transfer_pose(source: dict[str, Any], t: float, action: str) -> dict[str, Any]:
    """Translate only hips/torso and both wrists, while feet remain world-locked.

    The renderer's two-bone knee IK compensates for the body's motion.
    Returns a fresh dictionary; does not mutate the input pose or skin.
    """
    if action not in AMPLITUDES_PX:
        raise ValueError(f'Unsupported weight-transfer action: {action}')
    bias = support_bias(t)
    dx = AMPLITUDES_PX[action] * bias
    if not -AMPLITUDES_PX[action] - 1e-7 <= dx <= AMPLITUDES_PX[action] + 1e-7:
        raise AssertionError('Unbounded weight shift')
    p = dict(source)
    for key in ('root', 'handL', 'handR'):
        a, b = p[key]
        p[key] = (a + dx, b)
    p['weight_transfer_px'] = dx
    p['support_bias'] = bias
    return p
