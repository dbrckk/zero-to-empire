# FLUX run 65 — strict semantic review

Run `34071797399` (`Kaggle Mass Sprite Factory`, run 65) completed successfully and emitted 21 technically passing 2048×2048 building candidates covering `BLD-10`, `BLD-11`, and `BLD-13`.

## Verdict

**Reject the complete run from promotion.** Technical transparency/padding acceptance is not sufficient for canonical progress.

### BLD-10 — reject family
- T0–T3 are near-duplicate compact blocks with insufficient controlled tier growth.
- T4 contains large baked tier-like text (`...ER 4`) plus readable facade lettering, violating the no-text contract.
- T5 contains large baked `TIER 5` text.
- T6 contains tier-like annotation contamination and does not establish a clean monotonic family evolution.

### BLD-11 — reject family
- T0–T3 start as already-large crane-equipped industrial facilities rather than controlled low-complexity early tiers.
- T4–T6 change architectural identity too aggressively instead of preserving one evolving family anchor.
- T6 contains an unrelated human/worker figure and loose scene detail, violating the isolated-building-master requirement.

### BLD-13 — reject family
- T0–T4 remain structurally too similar for the required apex tier progression.
- T5 contains multiple large baked annotation labels and callout lines (`MODSTRUCTURE`, `BUILDING...`, `EVERY ROOF`, `PRODUCTION`, etc.) plus detached glow/background remnants.
- T6 changes back to a lower, cleaner block instead of completing a monotonic ultimate-tier progression.

## Canonical consequence

No run-65 candidate may advance to `ART`, `CLEAN`, `RUNTIME`, or `DONE`. Strict progress remains unchanged until a replacement passes semantic review, runtime integration, visibility, and green Android CI.

## Generator corrections required for the next dedicated building run
1. Explicitly forbid annotation arrows, callout lines, tier labels, pseudo-technical labels, signage, workers, vehicles, flags, and loose scene props.
2. Reject any candidate containing detached bright callout blobs/leader lines or secondary figures.
3. Enforce monotonic silhouette/footprint/height growth across T0→T6 while preserving a stable family anchor.
4. T0 must remain genuinely starter-scale; T6 must be the largest/most vertical member of the family.
