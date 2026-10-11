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
