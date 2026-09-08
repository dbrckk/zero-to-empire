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

## Current trusted state — 2026-09-08 13:36 +02:00
- Strict ledger remains **112 / 235 DONE**.
- Run 80 semantic delta +0; run 81 +0; run 82 +0; run 83 +0.

## Wave 84 — Kaggle long-running, GitHub collector expired
- Trigger commit `c51bb50d9e05e0498068b900844845a53585523e`.
- GitHub Actions run `34200990117`, job `101979474170`, run number 84.
- GitHub collector expired after the intended 135-minute polling window while Kaggle still reported `KernelWorkerStatus.RUNNING` continuously through the final poll.
- No normal GitHub artifact was available at collector shutdown. This is not a semantic-quality verdict on v16.2.
- Existing-kernel recovery was triggered via `ops/kaggle-recovery-trigger.txt`; recovery workflows must never push a replacement Kaggle kernel.

## CircleCI long-run recovery lane — repo ready, trigger not observed
- User explicitly requested moving long-running recovery/monitoring to CircleCI because GitHub Actions reaches its collector limit.
- `.circleci/config.yml` added in commit `4433f9ec427e95e1018e2084aac7f57533659c66`.
- CircleCI job `recover-kaggle-sprite-run`:
  - checks `ops/circleci-recovery-trigger.txt` for `active=true`;
  - validates `KAGGLE_USERNAME` / `KAGGLE_KEY`;
  - monitors the **existing** Kaggle kernel for up to 270 minutes (4.5h), printing status every minute;
  - downloads existing Kaggle outputs/logs;
  - stores `/tmp/kaggle-recovery` as CircleCI artifacts;
  - contains no `kaggle kernels push`, so it cannot overwrite an active generation.
- CircleCI trigger marker committed in `792fae00548a5d69846e81f4c949d24f4babf48c` for wave84.
- GitHub combined-status checks on commits `4433f9ec...`, `792fae00...`, and `38fb0a89...` all returned **no CircleCI status entries** by 13:36 +02:00.
- Public CircleCI project/pipeline lookup also yielded no indexable result.
- Current evidence therefore indicates the repository-side CircleCI config is present, but a CircleCI pipeline trigger is not firing (or VCS status reporting is disabled). This cannot be solved purely by another repo commit if the CircleCI project has no active GitHub push trigger.
- Current CircleCI docs confirm GitHub App projects require a configured trigger to listen for push events; once a pipeline is triggered, CircleCI normally reports status back to GitHub unless VCS status updates are disabled.
- One-time external configuration if needed: CircleCI project → Project Settings → Triggers → add/enable a GitHub push trigger for this repository; ensure project environment contains `KAGGLE_USERNAME` and `KAGGLE_KEY`. After that, any push changing the trigger marker will start the long recovery job.

## Wave 83 — resolved code failure
- Recovery proved v16.1 anchor-score recursion (`maximum recursion depth exceeded`).
- 48 T0 anchor attempts, 0 branches, 0 successful families, 0 candidates.
- No semantic conclusion from run83; strict delta +0.

## Building generator v16.2
`tools/sprites/kaggle_building_family_factory_v16.py`, recursion-safe scorer preserved through `V15_ANCHOR_SCORE`.
- Shape-first T0, six anchors, silhouette filtering and conservative source-locked T1→T6.
- Positive wording tightened for family 10, family 13 and T6 roof form.
- Wave84 remains the first intended valid semantic experiment once actual Kaggle outputs/logs are recovered.

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

## Immediate next actions
1. Prefer CircleCI for Kaggle jobs/recovery that can exceed the GitHub collector window once its GitHub push trigger is confirmed active.
2. As soon as wave84 outputs are retrievable, inspect branch-search report, generated targets, QA/contact sheets, all candidates and kernel log.
3. Verify startup `building-family-flux-v16.2-shape-first-recursion-safe`, ensure silhouette scoring runs without recursion, and measure complete-family semantic acceptance versus run82's 0/4.
4. Reject cranes/gantries/booms, broad site cards, people, vehicles, text, detached props, civic/monument drift, identity drift or fake tier progression.
5. Promote only complete genuinely valid families; then runtime refs + manifest/progress reconciliation + green Android CI before strict increment.
6. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Operating principle
Generate the right asset first. Prefer CircleCI for genuinely long orchestration once its VCS trigger is active; do not misclassify an orchestration timeout as a generator-quality failure.