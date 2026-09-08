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

## Strict completion gate
A sprite is strict DONE only after individual production, semantic correctness, technical/alpha validation, final runtime commit/reference, actual runtime visibility, manifest/progress reconciliation and green Android CI. Candidate count is never DONE count.

## Current trusted state — 2026-09-08
- Strict ledger remains **112 / 235 DONE**.
- Run 80 semantic delta +0; run 81 +0; run 82 +0; run 83 +0.

## Wave 83 — resolved: code failure, not semantic result
- Trigger commit `153ab7be267a8a1c8169b0374bac86a411795af0`.
- Original Actions run `34189278981` timed out its 135-minute collector while Kaggle was still running.
- Recovery run `34200649578` completed successfully and recovered artifact `10045663129`.
- Recovered evidence contains `branch-search-report.json` and the full Kaggle kernel log.
- Definitive root cause: v16.1 anchor-score recursion. Recovered log repeatedly reports `maximum recursion depth exceeded` after T0 renders.
- Final counters: 48 anchor attempts, 0 branches, 0 context attempts, 0 successful families, 0 fresh candidates.
- Therefore run83 is not a valid semantic-quality test of shape-first generation; no family reached actual branch evolution/export.
- No candidate promoted; strict delta +0.

## Building generator v16.2 — recursion-safe shape-first
File `tools/sprites/kaggle_building_family_factory_v16.py`.
- Fixed in commit `e69329d7fc97dbb02a003adbcd6a12e69c040f08`.
- Startup marker `KAGGLE_STARTUP=building-family-flux-v16.2-shape-first-recursion-safe`.
- Preserves `V15_ANCHOR_SCORE=v15.anchor_score` before override and calls that immutable scorer from `v16_anchor_score`.
- Positive wording also tightened: enclosed circular assembly chamber, compact attached reactor housings, compact enclosed luminous roof reactor cap.
- Shape-first T0, six anchors, silhouette filtering and conservative source-locked T1→T6 remain active.

## Wave 84 — ACTIVE
- Trigger commit `c51bb50d9e05e0498068b900844845a53585523e`.
- GitHub Actions run `34200990117`, job `101979474170`, run number 84.
- Latest check: `in_progress` at `Wait for Kaggle`.
- Checkout, credentials, dependency install, Kaggle authentication, kernel preparation and push/start are all green.
- Requested 56 tiers with `building-family-flux-v16.2-shape-first-recursion-safe`.
- This is the first valid intended empirical test of the shape-first architecture after the recursion repair.
- Do not launch a redundant building wave while run84 is queued/running.

## Run 82 baseline
Run `34145936891`, artifact `10030821750`, workflow SUCCESS.
- v15.2 requested 56 tiers; 28 technically validated exports across BLD-05/08/10/11.
- Semantic review rejected all 28 because cranes/gantries/booms and site/platform bases survived.
- Review: `docs/art/reviews/RUN_82_SEMANTIC_REVIEW.md`.

## Character lane
`tools/sprites/kaggle_character_sheet_factory_v1.py`, commit `4a48168166d47cbe47afc870aa8a8b65480e2b0b`.
- Fixed canonical 1024×1024 RGBA atlas, 4×4 256px cells.

## FX lane
`tools/sprites/kaggle_fx_sheet_factory_v1.py`, commit `8a837c11a37be85bad0f5380557e99089895f67f`.
- v1.1 temporal QA; one-shot attack/peak/decay checks; FX-07 includes polygonal ballistic debris.
- 2048×256 horizontal strips remain candidate-only until runtime integration is proven.

## Workflow reliability
- `.github/workflows/kaggle-recover-existing-run.yml` preserves outputs/logs from kernels that outlive the main GitHub collector.
- Main collector stops polling at 135 minutes to reserve evidence-recovery time.

## Immediate next actions
1. Query wave84 first on the next intervention.
2. When complete, verify startup marker `v16.2-shape-first-recursion-safe` and ensure `KAGGLE_V16_SILHOUETTE` lines appear without recursion errors.
3. Retrieve all candidates/reports/logs and perform full-resolution semantic review. Primary comparison: true complete-family semantic acceptance versus run82's 0/4.
4. Reject cranes/gantries/booms, broad site cards, people, vehicles, text, detached props, civic/monument drift, identity drift or fake tier progression.
5. Promote only complete genuinely valid families; then runtime references, manifest/progress reconciliation and green Android CI before strict increment.
6. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Operating principle
Generate the right asset first. Preserve evidence from long-running jobs, fix code blockers before spending another GPU batch, and optimize semantic acceptance rate × validated sprites/GPU-hour rather than raw output count.