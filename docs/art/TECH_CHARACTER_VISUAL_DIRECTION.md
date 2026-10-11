# Zero to Empire — TECH art direction (review-only)

This brief specifies the next *creative* pass. It does not approve or replace any canonical sprite. Strict DONE remains determined by the master queue and frame-by-frame review.

## Identity and rendering

Design one expressive technician shared across IDLE/WALK/WORK/CARRY/REPAIR/CELEBRATE: same face, proportions, workwear, equipment and color hierarchy. Move away from the difficult-to-read dark side-profile toward a coherent three-quarter 2.5D city camera. Use broad graphite/steel surfaces, readable cyan service trim and restrained amber practical lights. Avoid bright "neon shoes" as a substitute for correct leg topology.

The two AI-generated day/night concepts created on 2026-10-11 are **exploratory mockups, not game screenshots or importable atlases**. They show useful silhouette/costume simplification but do not authorize replacing existing reviewed assets.

## Action-specific artistic acceptance

| Action | Must be readable at 39–42dp | Existing weakness |
|---|---|---|
| IDLE | grounded stance, stable headgear, restrained breathing | identity must match all other actions |
| WALK | separate rear and near leg, alternating grounded footfall, continuous motion | lower-limb readability flagged in six of eight review frames |
| WORK | hands genuinely contact animated cyan diagnostic console | gesture too close to REPAIR in small view |
| CARRY | two-hand amber crate grip and counterbalanced walk | cargo weight/contact not obvious |
| REPAIR | physical welding torch and brief warm seam sparks | action still resembles WORK without motion |
| CELEBRATE | two raised arms, expressive body arc and restrained particles | side view reduces silhouette impact |

## Review gates

Render six source loops using the same character; export separate RGBA 4×4 atlases (1024×1024, 256px cells; 6/8/10/8/10/8 active frames). Inspect frame continuity, perspective, feet, prop contact, and loop seams. Validate real Android gallery and world renderer **day and night at 39–42dp**, not just enlarged contact sheets. The TECH candidate workflow is a preview only: never change strict DONE or canonical masters without semantic acceptance and Android evidence.

Source-derived, reproducible art evidence: GitHub Actions workflow `TECH canonical review staging`, artifact `tech-six-canonical-review-not-approved`, including `tech-review-true-source-board.png` and `tech-review-true-source-motion.gif`.

## Bounded night material grading — 2026-10-11

Code: `tools/sprites/rigged_tech_actions_v3.py`, `TECH_REVIEW_MATERIAL_GAMMA=0.76`. In the **review-only** exporter, the character's kit RGB material channels are mapped through a deterministic gamma LUT before drawing. Raw source texture and alpha are unchanged, and rendered WORK/REPAIR/VFX props are drawn after the character.

Measured on **actual before/after canonical candidate atlas pixels**, downsampled to 42×42 with LANCZOS and only counting pixels with alpha ≥0.5:

| Action | Median luma before→after (0–255) | Pixels below luma 80 before→after |
|---|---|---|
| IDLE | 49.6 → 69.2 | 89.2% → 66.6% |
| WALK | 50.4 → 70.1 | 88.7% → 65.5% |
| WORK | 52.5 → 70.0 | 87.1% → 65.1% |
| CARRY | 57.0 → 76.1 | 75.9% → 55.5% |
| REPAIR | 53.0 → 68.9 | 88.2% → 67.5% |
| CELEBRATE | 49.9 → 70.0 | 87.2% → 64.6% |

Every active frame's alpha mask matched **pixel-for-pixel** across the before/after exported atlases. These are measurable source-preview improvements, **not** proof of semantic action quality, in-game 3/4 projection or release eligibility. The automated 6/8 lower-limb warning for WALK and CARRY remains unresolved.
