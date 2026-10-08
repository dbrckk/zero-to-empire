"""Deterministic 512px rig-space interaction targets for TECH WORK and REPAIR.

No prompt-by-frame regeneration, remote model calls, or automatic art approval.
"""
from __future__ import annotations
import math

WORK_SCREEN_LOCAL = (34.0, -75.0, 107.0, -41.0)
REPAIR_TIP_LOCAL = (94.0, -72.0)


def work_hands(t: float, root: tuple[float, float]):
    """Independent cyclic touch trajectories constrained to one screen."""
    if not math.isfinite(t):
        raise ValueError('Non-finite phase')
    x, y = root
    phase = 2 * math.pi * (t % 1.0)
    return ((x + 48 + 10 * math.sin(phase), y - 55 + 9 * math.cos(phase)),
            (x + 84 + 15 * math.sin(2 * phase), y - 56 + 12 * math.cos(2 * phase)))


def screen_bounds(root):
    x, y = root
    a, b, c, d = WORK_SCREEN_LOCAL
    return x+a, y+b, x+c, y+d


def work_contact(p: dict) -> dict:
    bounds = screen_bounds(p['root'])
    def within(hand):
        x, y = p[hand]
        return bounds[0] <= x <= bounds[2] and bounds[1] <= y <= bounds[3]
    return {'handL_on_screen': within('handL'),
            'handR_on_screen': within('handR'),
            'panel_bounds': bounds}


def work_pulse(t: float) -> float:
    """Phase-locked emissive touch feedback, never random pixels."""
    return .30 + .70 * (math.sin(4 * math.pi * (t % 1.0)) ** 2)


def repair_tip(root):
    return root[0]+REPAIR_TIP_LOCAL[0], root[1]+REPAIR_TIP_LOCAL[1]


def repair_contact(p: dict) -> dict:
    distance = math.dist(p['handR'], repair_tip(p['root']))
    return {'torch_length_px': distance, 'torch_reachable': 18 <= distance <= 70}


def repair_spark_intensity(t: float) -> float:
    if not math.isfinite(t):
        raise ValueError('Non-finite phase')
    strength = max(0., math.sin(2 * math.pi * (t % 1.0)))
    return strength ** 3 if strength > .5 else 0.
