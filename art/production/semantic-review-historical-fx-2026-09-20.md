# Historical FX semantic reconciliation — 2026-09-20

Evidence workflow: `35493610023`

## Approved strict DONE
- FX-00 — warm welding sparks
- FX-04 — steam vent
- FX-05 — cyan energy pulse
- FX-06 — warm energy pulse
- FX-07 — construction dust/debris
- FX-08 — upgrade construction flash
- FX-17 — mastery crown shimmer

## Evidence
All seven visually match their manifest roles on the historical contact sheet. The sheet-aware runtime contract passes the exact 512×256 WebP resources as 4×2 / 8-frame assets.

Runtime usage is explicit:
- FX-00 / FX-05 / FX-06: Power Core authored burst/pulse rendering;
- FX-04 / FX-06 / FX-07: purchase impact rendering;
- FX-08: `UpgradeConstructionFlash` on business-level changes;
- FX-17: `MasteryCrownShimmer` when mastery is active.

Reduced-motion behavior is explicit in the runtime: Power Core bursts are suppressed under reduced motion; purchase/upgrade effects select a static/peak frame; mastery freezes to frame zero.

The canonical resolver maps these semantic effects to their exact final runtime resources.

## Still unresolved
FX-01, FX-02 and FX-03 are semantically plausible and technically valid sheets, but strict promotion is withheld until active gameplay visibility is explicitly demonstrated.
