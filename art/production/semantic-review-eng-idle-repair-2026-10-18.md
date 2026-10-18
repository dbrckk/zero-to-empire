# ENG character candidates — semantic review (2026-10-18)

Evidence: [GitHub Actions run 38871322905](https://github.com/dbrckk/zero-to-empire/actions/runs/38871322905), artifact `kaggle-async-character-batch` (ID 12034630670). Inspected actual `review-mobile-eng-idle.png` (6 frames), `review-mobile-eng-repair.png` (10 frames) and the technical QA report. Technical pass is not semantic approval.

## CHR-ENG-IDLE — HOLD: cleanup required

Identity, helmet and uniform are broadly consistent. Extraneous marks near feet in some frames and limited readable idle movement warrant cleanup and full motion review. Do not mark DONE or promote.

## CHR-ENG-REPAIR — REJECT: regenerate

Footwear and repair tools change appearance and location across the ten frames; the engineer remains predominantly front-facing and standing, with no legible repair action. Consistent with the existing `TOOL_CRATE_TORSO_COLOR_DISCONTINUITY_RISK` warning. Do not mark DONE or promote.

## Replacement acceptance criteria

- Stable engineer identity, helmet, gloves, uniform, boots and proportions in every frame.
- Consistent tool and repair target, with coherent reach → tool engagement → repair → recovery.
- Planted feet, transparent background, complete body, legible Android-scale action and seamless loop.
- Run technical QA; visually inspect all frames and animated preview; explicitly approve before changing canonical queue or Android runtime.

Canonical strict completion remains **219/235**, with 16 pending animations. This document is an explicit **rejection/hold**, not approval.
