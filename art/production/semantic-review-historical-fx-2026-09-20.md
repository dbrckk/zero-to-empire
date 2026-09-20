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

## Final resolution — FX-01 / FX-02 / FX-03

The final missing requirement is now satisfied: active gameplay visibility is explicit in `IndustrialBusinessFx.kt` merged at commit `74c2a8a47742cb6d63b7a05d94398c4f81e7b60b`.

- FX-01 `zte_fx_01_final.webp` — Git blob `1886f681ded8b62af29581b23e2e505eb5988832`; visible on Workshop (business 2) from tier 2.
- FX-02 `zte_fx_02_final.webp` — Git blob `2741b134d99ec03cafb7ff8c64d0a4581d9ea5c0`; visible on Factory (business 3) from tier 4.
- FX-03 `zte_fx_03_final.webp` — Git blob `204916cf36abe663c0d1114af5cf3bcd0b9e8642`; visible on Factory (business 3) from tier 2.

Runtime code blob: `7821ab7a81f83642b5841b29725f268cd0d22ff3`.

Reduced-motion behavior is explicit: each effect selects a stable representative frame and does not enter the animation loop when reduced motion is active; low-power mode uses a slower cadence.

Validation on the merged runtime:
- Android CI `35499825411`: success.
- Android Emulator Smoke `35499825403`: success.

Verdict: **FX-01, FX-02 and FX-03 are strict DONE.**
