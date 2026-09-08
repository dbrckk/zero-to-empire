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

## Current trusted state — 2026-09-08 13:10 +02:00
- Strict ledger remains **112 / 235 DONE**.
- Run 80 semantic delta +0; run 81 +0; run 82 +0; run 83 +0.

## Wave 84 — collector timed out; recovery triggered
- Trigger commit `c51bb50d9e05e0498068b900844845a53585523e`.
- GitHub Actions run `34200990117`, job `101979474170`, run number 84.
- Main GitHub collector finished `failure` only because the 135-minute polling window expired while Kaggle still reported `KernelWorkerStatus.RUNNING` continuously through the final poll.
- No normal `kaggle-sprite-batch` artifact was available at collector shutdown; do not classify v16.2 semantic quality from this alone.
- Recovery trigger updated in commit `8a3e49a2072f5782b98110e14ec3875a9a19b31d` for wave84/source run `34200990117` in `recover-existing-only` mode.
- Recovery workflow never pushes a new Kaggle kernel and therefore cannot replace the existing long-running generation.
- At the immediate post-trigger check no recovery Actions run had appeared yet; query the trigger commit/run list first on next intervention.

## Wave 83 — resolved code failure
- Recovery proved v16.1 anchor-score recursion (`maximum recursion depth exceeded`).
- 48 T0 anchor attempts, 0 branches, 0 successful families, 0 candidates.
- No semantic conclusion from run83; strict delta +0.

## Building generator v16.2
`tools/sprites/kaggle_building_family_factory_v16.py`, recursion-safe scorer preserved through `V15_ANCHOR_SCORE`.
- Shape-first T0, six anchors, silhouette filtering and conservative source-locked T1→T6.
- Positive wording tightened for family 10, family 13 and T6 roof form.
- Wave84 remains the first intended valid semantic experiment once its actual Kaggle outputs/logs are recovered.

## Character lane
`tools/sprites/kaggle_character_sheet_factory_v1.py`, commit `4a48168166d47cbe47afc870aa8a8b65480e2b0b`.
- Fixed canonical 1024×1024 RGBA atlas, 4×4 256px cells.

## FX lane — proven runtime contract and v1.2 factory
Concrete runtime evidence:
- `app/src/main/java/com/zerotoempire/game/ElectricArc.kt`
- `app/src/main/java/com/zerotoempire/game/DroneThruster.kt`
Both use Compose `Canvas.drawImage` with 8 frames, 4×2 grid, 128×128 source frames => 512×256 atlas.

FX factory commit `f22f4769aaef97a6ef19933c1a699461de6c00b9`:
- engine `procedural-fx-v1.2-runtime-atlas`;
- renders internally at 256×256, downsamples to 128×128;
- packs exactly 4×2 => 512×256 RGBA;
- preserves one-shot/loop temporal QA and FX-07 ballistic polygonal debris.
- Runtime visibility and green CI remain mandatory before strict DONE.

## Run 82 baseline
Run `34145936891`, artifact `10030821750`: 28 technical exports, 28 semantic rejects due cranes/site contamination.

## Workflow reliability
- `.github/workflows/kaggle-recover-existing-run.yml` preserves outputs/logs from Kaggle kernels that outlive the 135-minute main collector.
- Main collector failure at the 135-minute boundary is not itself a model/generator failure if Kaggle remains RUNNING.

## Immediate next actions
1. Query Actions runs for head SHA `8a3e49a2072f5782b98110e14ec3875a9a19b31d` and find the recovery run.
2. If recovery succeeds, download `kaggle-recovered-sprite-batch` and inspect `branch-search-report.json`, generated-targets, QA reports/contact sheets, candidates and kernel log.
3. Verify startup `building-family-flux-v16.2-shape-first-recursion-safe`, ensure silhouette scoring runs without recursion, and measure complete-family semantic acceptance versus run82's 0/4.
4. Reject cranes/gantries/booms, broad site cards, people, vehicles, text, detached props, civic/monument drift, identity drift or fake tier progression.
5. Promote only complete genuinely valid families; then runtime refs + manifest/progress reconciliation + green Android CI before strict increment.
6. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Operating principle
Generate the right asset first. Prefer evidence from existing runtime code over assumed formats. Preserve evidence from long-running jobs and optimize semantic acceptance rate × validated sprites/GPU-hour.