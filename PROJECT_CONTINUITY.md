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

## Current trusted state — 2026-09-07 17:36 +02:00
- Strict ledger remains **112 / 235 DONE** pending evidence-based reconciliation.
- BLD-03-T2..T6 from run 75 remain integrated but not added to strict count without canonical/CI proof.
- Run 77: 21 technical candidates, 21/21 semantic rejection.
- Runs 78 and 79: 0 accepted candidates.
- Run 80 (`34125123246`) completed SUCCESS and exported 21 technically valid sprites, but semantic review rejected 21/21; strict delta +0.

## High-throughput + real validation policy
- Workflow default: 56 manifest tiers.
- `cancel-in-progress: false` protects expensive active GPU runs.
- Every exported sprite must be represented in QA evidence.
- Full candidates, contact sheets, reports and logs retained for 90 days.
- Strict semantic review, runtime integration and green Android CI remain mandatory.

## Building generator — v15.1 live validation
The user explicitly requested that validation happen **while sprites are being generated**, not only after the complete batch.

Implemented in `tools/sprites/kaggle_building_family_factory_v15.py` commit `608ab41178a8080da1c30b7269b6c5d6c38da5d6`.
Startup marker: `KAGGLE_STARTUP=building-family-flux-v15.1-live-validation`.

Live validation behavior:
1. Up to 4 T0 anchors are still generated, but each anchor is immediately scored and rejected before branch evolution when its starter coverage, slab score or compactness is unacceptable.
2. Every T1→T6 render is validated immediately against the already-accepted previous branch frames.
3. Live contextual gates currently check broad slab contamination, adjacent-family IoU/identity, severe coverage collapse, horizontal center drift, lack of growth from T0 and late-tier growth trajectory.
4. A contextual failure triggers a fresh-seed regeneration of that tier rather than letting a bad image poison the rest of the family.
5. Up to 3 contextual attempts are allowed for a tier.
6. If all contextual attempts fail, the branch is **early-aborted** and later tiers are not generated, saving GPU time.
7. Final full-family QA still runs after all live passes; live QA is an additional filter, not a weaker replacement.
8. `branch-search-report.json` now records `context_attempts`, `live_rejections` and `early_aborts` so yield can be measured empirically.

This should improve validated-sprite yield per GPU-hour by spending compute on branches that remain viable instead of completing obviously doomed families.

## Wave 81 — active/current wave caveat
- Trigger commit: `bfd3ea0fea08c78fa36f0d3ab5c100a1608a2566`.
- GitHub Actions run: `34132705535`.
- Wave 81 was already cloned/launched before commit `608ab411...`, so its running Kaggle kernel uses the earlier v15 multi-branch code and cannot safely be hot-patched without discarding the active GPU run.
- Do not cancel it. The **next generation wave** will automatically use v15.1 live validation from `main`.

## Character production lane
- Dedicated factory: `tools/sprites/kaggle_character_sheet_factory_v1.py` (`5bec3b27922106c6d2120cf28b56a008aeb4b026`).
- Routing commit `8fc1a3571600edac9e41d8dd5a1cc8b9b72e7f36` distinguishes CHR and FX backlog and routes characters after buildings/statics.
- Character sheets use identity anchor + img2img pose evolution, edge-connected alpha isolation, fixed feet pivot and cycle/silhouette QA.
- `character-sheet-report.json` retained by workflow commit `009dce7efbd038d42362cf56e55039602a5d3962`.
- Dedicated FX lane remains unresolved.

## Immediate next actions
1. Query run `34132705535` first on the next intervention.
2. When wave 81 completes, retrieve logs, branch report, QA reports and every candidate PNG; perform strict full-resolution semantic review.
3. For the next user-approved generation wave, use v15.1 and inspect `KAGGLE_LIVE_PASS`, `KAGGLE_LIVE_REJECT`, `KAGGLE_BRANCH_EARLY_ABORT` and report metrics to verify that in-generation validation improves yield.
4. Tune live thresholds from measured false positives/false negatives rather than weakening final QA.
5. Promote only genuinely valid families; integrate runtime/references, reconcile manifest/progress and require green Android CI before incrementing strict DONE.
6. Build dedicated FX sheet factory.
7. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Known unresolved targets
- Remaining building families after BLD-03.
- `TER-07` Expansion energy conduit unless superseded by accepted promotion.
- Dedicated FX production lane.

## Operating principle
Maximize **validated sprites per GPU-hour**. Validate as early as possible, regenerate locally when a tier fails, abort doomed branches early, preserve evidence, and keep final semantic/runtime/CI gates strict.