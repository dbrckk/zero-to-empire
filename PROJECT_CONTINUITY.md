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

## Current trusted state — 2026-09-08 11:35 +02:00
- Strict ledger remains **112 / 235 DONE**.
- Run 80 semantic delta +0; run 81 +0; run 82 +0; run 83 +0.

## Wave 84 — ACTIVE
- Trigger commit `c51bb50d9e05e0498068b900844845a53585523e`.
- GitHub Actions run `34200990117`, job `101979474170`, run number 84.
- Latest check at 11:35 +02:00: still `in_progress` at `Wait for Kaggle`.
- Checkout, credentials, dependency install, Kaggle auth, preparation and launch all green.
- Requested 56 tiers with `building-family-flux-v16.2-shape-first-recursion-safe`.
- Live job log endpoint currently returns 404 while job is active; do not interpret as failure.
- Do not launch a redundant building wave while run84 is active.

## Wave 83 — resolved code failure
- Recovery proved v16.1 anchor-score recursion (`maximum recursion depth exceeded`).
- 48 T0 anchor attempts, 0 branches, 0 successful families, 0 candidates.
- No semantic conclusion from run83; strict delta +0.

## Building generator v16.2
`tools/sprites/kaggle_building_family_factory_v16.py`, recursion-safe scorer preserved through `V15_ANCHOR_SCORE`.
- Shape-first T0, six anchors, silhouette filtering and conservative source-locked T1→T6.
- Positive wording tightened for family 10, family 13 and T6 roof form.

## Character lane
`tools/sprites/kaggle_character_sheet_factory_v1.py`, commit `4a48168166d47cbe47afc870aa8a8b65480e2b0b`.
- Fixed canonical 1024×1024 RGBA atlas, 4×4 256px cells.

## FX lane — proven runtime contract and v1.2 factory
Concrete runtime evidence found in:
- `app/src/main/java/com/zerotoempire/game/ElectricArc.kt`
- `app/src/main/java/com/zerotoempire/game/DroneThruster.kt`
Both use Compose `Canvas.drawImage` with:
- 8 frames,
- 4 columns × 2 rows,
- 128×128 source frame,
- resulting atlas 512×256.
Therefore the previous 2048×256 horizontal candidate format was incompatible with the project's proven runtime convention.

FX factory updated in commit `f22f4769aaef97a6ef19933c1a699461de6c00b9`:
- engine `procedural-fx-v1.2-runtime-atlas`;
- renders internally at 256×256 for quality;
- downsamples each validated frame to 128×128;
- packs exactly 4×2 => 512×256 RGBA;
- hard assertion on atlas size;
- report records `render_cell`, `runtime_cell`, `layout`, `atlas`;
- preserves v1.1 temporal one-shot/loop QA and FX-07 polygonal debris.
Runtime visibility and CI remain required before strict DONE, but atlas-format ambiguity is now resolved using existing production code rather than a new invented loader.

## Run 82 baseline
Run `34145936891`, artifact `10030821750`: 28 technical exports, 28 semantic rejects due cranes/site contamination.

## Workflow reliability
- `.github/workflows/kaggle-recover-existing-run.yml` preserves outputs/logs from long-running Kaggle kernels.
- Main collector polls 135 minutes to reserve recovery time.

## Immediate next actions
1. Query wave84 first.
2. When complete, retrieve all candidates/reports/logs and verify v16.2 startup, silhouette scoring without recursion, and full semantic quality.
3. Compare semantic complete-family acceptance versus run82's 0/4.
4. Promote only complete genuinely valid families, then runtime refs + manifest/progress reconciliation + green Android CI before strict increment.
5. After building backlog is sufficiently reduced, exercise FX v1.2 against the proven 512×256 / 4×2 runtime contract and integrate only after actual visibility proof.
6. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Operating principle
Generate the right asset first. Prefer evidence from existing runtime code over assumed formats. Preserve evidence from long-running jobs and optimize semantic acceptance rate × validated sprites/GPU-hour.