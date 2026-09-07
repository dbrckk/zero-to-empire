# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read this file before any new work on this repository and update it at every assistant intervention that changes goals, state, decisions, blockers, or next actions.

## Global continuity rule
- Keep a recent concrete record of changes, evidence, blockers and next objectives.
- Update this file at every material assistant intervention.
- Do not rely on chat history alone.
- Apply the same `PROJECT_CONTINUITY.md` convention to every actively worked repository.
- Never mark completion from intent or candidate generation alone.

## Primary objective
Bring **Zero → Empire** to full production completion. Immediate art objective: **235 / 235 canonical final sprites strict DONE**.

Canonical sources:
- `docs/art/FINAL_AAA_SPRITE_MANIFEST.md`
- `docs/art/FINAL_AAA_SPRITE_PROGRESS.md`

## Strict completion gate
A sprite is strict DONE only after individual production, semantic correctness, technical/alpha validation, final runtime commit/reference, actual runtime visibility, manifest/progress reconciliation and green Android CI. Candidate count is never DONE count.

## Current trusted state — 2026-09-07 17:20 +02:00
- Strict ledger remains **112 / 235 DONE** pending evidence-based reconciliation.
- BLD-03-T2..T6 from run 75 remain integrated but not added to strict count without canonical/CI proof.
- Run 77: 21 technical candidates, 21/21 semantic rejection.
- Runs 78 and 79: 0 accepted candidates; their evidence drove retry, segmentation, prompt-length and monotonic-growth improvements.
- Run 80 (`34125123246`) completed SUCCESS and exported **21 technically valid sprites** across BLD-08, BLD-09 and BLD-13.
- Full-resolution semantic review rejected **21 / 21**; review: `docs/art/reviews/RUN_80_SEMANTIC_REVIEW.md`. Strict DONE delta: +0.

## High-throughput + real validation policy
The user explicitly wants many more sprites produced and tested while preserving genuine validation.
- Workflow default: **56 manifest tiers**.
- `cancel-in-progress: false` prevents expensive active GPU runs from being destroyed by the next approved pulse.
- Every exported sprite must be represented in QA evidence; mismatched coverage fails QA.
- Full candidates, contact sheets, reports and logs are retained for 90 days.
- Strict semantic review, runtime integration and green Android CI remain mandatory.

## Generator evolution — v15 branch search
`tools/sprites/kaggle_building_family_factory_v15.py` (`73a534056135670fe212e0b4906cede7dc00555f`) uses multi-anchor branch search:
1. Up to 4 T0 anchors per family.
2. Early technical rejection of weak/contaminated anchors.
3. Up to 2 surviving full T0→T6 branches.
4. Branch scoring for identity, growth, compactness, slab contamination and drift.
5. Export only the strongest complete branch plus `branch-search-report.json`.
6. Stronger semantic negatives against people, flags, cranes, vehicles, roads, platforms, civic/religious/monument architecture.

## Wave 81 — active checkpoint
- Trigger commit: `bfd3ea0fea08c78fa36f0d3ab5c100a1608a2566`.
- GitHub Actions run: **`34132705535`**.
- Workflow job: `101776405808`.
- Generator: `building-family-flux-v15-multibranch-semantic-safe`.
- Requested count: **56** manifest tiers.
- At 17:20 +02:00 the job remains `in_progress` at **Wait for Kaggle**; setup/auth/kernel launch are green and artifact/QA steps are pending.
- Do not interfere with the active Kaggle kernel.

## Character production lane — prepared while wave 81 runs
The previous future blocker where CHR/FX could not be routed has been partially removed.

Created `tools/sprites/kaggle_character_sheet_factory_v1.py` in commit `5bec3b27922106c6d2120cf28b56a008aeb4b026`.
Character factory design:
1. Parses all 24 manifest `CHR-*` sheets (operator, technician, logistics worker, engineer × idle/walk/work/carry/repair/celebration).
2. Generates a text-to-image identity anchor then conservative img2img pose frames to preserve face, clothing, proportions and camera.
3. Uses edge-connected neutral-background alpha isolation.
4. Normalizes every frame to a 256×256 cell with fixed feet baseline/pivot.
5. Assembles complete 1024-wide sheets with action-specific frame counts (6–10 in v1).
6. Rejects edge contact, non-full-body silhouettes, bad coverage, abrupt silhouette/identity jumps, duplicate adjacent frames, feet-pivot drift and excessive horizontal drift.
7. Emits `character-sheet-report.json`; output remains candidate-only until full semantic review.

Routing commit `8fc1a3571600edac9e41d8dd5a1cc8b9b72e7f36` updates `kaggle/github_mass_factory.py` to distinguish `CHR` and `FX` backlog and route character backlog to the dedicated factory when buildings/statics are exhausted. FX remains explicitly unsupported pending a dedicated FX factory.
Workflow commit `009dce7efbd038d42362cf56e55039602a5d3962` now retains `character-sheet-report.json` in the 90-day QA artifact.

## Immediate next actions
1. Query run `34132705535` first on the next intervention.
2. When complete, retrieve logs, branch-search report, QA reports and every candidate PNG.
3. Review every exported family at full resolution; promote only genuinely valid families.
4. Integrate accepted assets/references, reconcile manifest/progress and require green Android CI before incrementing strict DONE.
5. Use wave-81 rejection reasons to improve semantic yield rather than weaken gates.
6. Build a dedicated FX sheet factory so the final 18 FX sheets cannot block 235/235.
7. Test the character factory on Kaggle before relying on it for strict completion.
8. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Known unresolved targets
- Remaining building families after BLD-03.
- `TER-07` Expansion energy conduit unless superseded by accepted promotion.
- Dedicated FX production lane still required.

## Operating principle
Maximize **validated sprites per GPU-hour**, not raw images. Generate broadly, reject aggressively, preserve evidence, and only increase strict DONE after full integration and CI proof.