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

## Review-only far-leg depth grade and footfall proof — 2026-10-11

**Code change:** [87c759b](https://github.com/dbrckk/zero-to-empire/commit/87c759be364409b2538a5c959cb2b09bdd62aa99) adds a reversible, cooler steel-blue diffuse material grade to the far thigh and calf/boot pieces *after* the original graphite gamma map. Source skin and pose/IK/contact geometry are untouched; ALL six candidate actions are recolored consistently because they share the same rig and skin. It is a review candidate, **not** a production-material approval or a true camera rotation.

**Actual before/after atlas check:** Compared the canonical PNGs from the earlier [staging run 38134298854](https://github.com/dbrckk/zero-to-empire/actions/runs/38134298854) against [staging run 38136394210](https://github.com/dbrckk/zero-to-empire/actions/runs/38136394210). All 6 actions retain the **identical alpha channel on every pixel** across the 1024×1024 atlas. Nonidentical RGBA pixel counts: WALK 11,661 (1.112% of canvas), CARRY 11,638 (1.110%), IDLE 10,710, WORK 17,941, REPAIR 17,931 and CELEB 14,372. On the *source* 256×256 cells' lower-body crop x=55–214/y=135–239, WALK frame 1 mean (blue−red) over alpha≥128 rises from +0.71 to +12.98 levels; frame 7 +0.67 to +8.69. CARRY follows the same trend. These source-pixel statistics establish a color/material change without geometry corruption, **not a player's perception**.

**New inspection output:** [footfall review staging run 38136394210](https://github.com/dbrckk/zero-to-empire/actions/runs/38136394210) exports `build/tech-review-visual-evidence/tech-review-footfall-closeups.png`, showing unretouched WALK/CARRY frames 1, 3, 5, 7 at fixed cropped position and 2× NEAREST, plus literal 42-*pixel* night/day examples. The bottom three-quarters of the PNGs are shown without independently recentering the feet, which would conceal the gait crossover.

**Actual visual finding:** the far shin/boot is cooler and easier to distinguish at magnified scale, particularly in the crossing poses. At literal 42 pixels, both feet can still overlap and the 2.5D profile remains mostly lateral. The historical LOWER_LIMB_STRUCTURE_UNVERIFIED warning is **still not resolved**, and no semantic strict DONE can follow from this grading change. Next art step requires silhouette/perspective rework of the rig or newly authored consistently oriented skin pieces, evaluated as a unified set of six actions.

## Fixed 2.5D far-ground projection — 2026-10-11

- **Experiment (review only):** [c47f01f](https://github.com/dbrckk/zero-to-empire/commit/c47f01fd5c13878d810d7e0540556ef9471a55b4) introduces constant `FAR_FOOT_DEPTH_Y_PX=14` in addition to the existing 22px lateral offset for WALK/CARRY. The far knee re-solves via two-bone IK. Only the far-side ankle projection changes: the action phase, stance flags, near foot, hand contacts, one-identity skin and production sprites are untouched. The secondary stance invariant was synchronized in [0d38056](https://github.com/dbrckk/zero-to-empire/commit/0d38056f1e0dd823dfd4bf2f341f844cf4349991).
- **Controls:** [modular TECH CI 38136907106](https://github.com/dbrckk/zero-to-empire/actions/runs/38136907106) **SUCCESS**; [canonical review staging 38136907087](https://github.com/dbrckk/zero-to-empire/actions/runs/38136907087) **SUCCESS**; [repository standards 38136907973](https://github.com/dbrckk/zero-to-empire/actions/runs/38136907973) **SUCCESS**. All outputs are six-stage candidates and never overwrite the canonical masters.
- **Measured effect:** Compare actual atlas PNGs from [38136630692](https://github.com/dbrckk/zero-to-empire/actions/runs/38136630692) against [38136824930](https://github.com/dbrckk/zero-to-empire/actions/runs/38136824930). WALK: 17,657 RGBA canvas pixels differ (including 11,598 alpha pixels); CARRY: 17,678 RGBA pixels differ (including 11,580 alpha pixels). IDLE, WORK, REPAIR and CELEB are **pixel-identical** between these exports. This is a geometrical candidate revision, unlike the earlier material-only grade.
- **Remaining limitation:** The automated lower-limb risk remains **six of eight ambiguous frames** for WALK and CARRY, both before and after the depth offset. The static close-up suggests a deeper rear-foot lane but cannot establish a natural gait or better 2.5D camera match. Do **not** label the experiment an artistic pass, and do **not** promote strict DONE. Inspect the true animated close-up and real Android gallery before deciding whether to retain or revise the 14px depth parameter.
