# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Verified current state — 2026-10-09 (authoritative)

- **Canonical strict DONE: 216/235**, production processed: **233/235**. The source of truth is `art/production/master-asset-queue.json`. Do not raise the number for production, technical QA, or mere manifest presence.
- **Remaining 19 (all CHR)**: OP WALK/WORK/CARRY/REPAIR/CELEB (5); TECH WALK/WORK/CARRY (3); LOG WALK/WORK/CARRY/REPAIR/CELEB (5); ENG IDLE/WALK/WORK/CARRY/REPAIR/CELEB (6). Technical states: 17 AWAITING_REVIEW, 1 REJECTED_SEMANTIC (TECH-WALK), 1 BLOCKED (LOG-CARRY).
- Full-sheet direct visual inspection on 2026-10-09 confirmed canonical `CHR-LOG-CARRY` has separate torso and leg rows with **no valid carrying action**; `CHR-ENG-IDLE` has only cropped portraits; `CHR-OP-WALK` and `CHR-TECH-WALK` visibly change identity/camera/clothes; `CHR-LOG-WORK` changes characters and tools. Existing `art/production/character-visual-review-findings-2026-10-09.md` records the wider 19-item visual audit. **No further strict promotions are justified without valid new source frames.**
- **Known contradictory records**: `docs/art/FINAL_AAA_SPRITE_MANIFEST.md` currently marks **236/236** rows DONE, including the separately excluded `ONB-00`, whereas the canonical 235 registry approves only 216. `docs/art/FINAL_AAA_SPRITE_PROGRESS.md` is stale. Historical promotion review remains **OPEN**. Do **not** confuse a manifest DONE label with canonical strict approval.
- `CHR-LOG-CARRY` repair is reserved to the Pollinations full-body-per-frame v3 lane until `2026-10-10T18:00:00Z`: `art/production/controlled-character-regen-queue.json` was requeued `PENDING_POLLINATIONS` on commit `d3b96eb`. Its candidate must be staged separately, preserving historical canonical PNG. The 2026-10-09 observed GitHub Action run `37979410539` was **in progress**; check current status and resulting QA on resume.
- Fixes landed on `main`: `6fe179a` character CI counts are dynamic; `ad0bf48` completion gate requires true 235 strict approvals, 236 matching manifest rows and historical review CLOSED; `2f51782` Pollinations cannot consume Kaggle-owned tasks; `d3b96eb` requeues reserved LOG-CARRY; `50108f4` full audit reconciles manifest with strict canonical queue. GitHub Actions **Character strict review matrix** run `37978989707` SUCCESS and **Asset Pipeline CI** run `37979322055` SUCCESS (including audit `--allow-pending`); **Sprite Completion Gate** run `37979322152` SUCCESS means guard execution passed, **not** that the final 236-sprite audit ran or completion was approved.
- Prior .ai/session-state.json, README and old progress figures are historical and MUST NOT overwrite the above canonical counts.

### Next action sequence

1. Collect Pollinations LOG-CARRY run and inspect every staged frame for complete full-body, one LOG identity and a crate gripped by **both hands** throughout the loop. Reject or regenerate if incomplete. Do not mark strict DONE from heuristic QA alone.
2. Regenerate the other 18 flawed action atlases using a **single identity reference per role**, per-frame full-body control, non-collage animation, stable camera, tools and foot pivot. For WALK inspect foot contacts/stride; for WORK/REPAIR inspect prop contact; for CARRY inspect bilateral grip; for IDLE/CELEB verify action.
3. For each approved new asset: preserve source provenance and semantic visual review, run technical/temporal QA, process exact WebP runtime, demonstrate live gameplay reference/visibility, get green Android CI on the exact commit; only then update canonical `strict_status=DONE`.
4. Reconcile manifest/progress/historical-review documents with canonical approvals. Audit all 236 runtime rows, ensuring 235/235 canonical strict DONE and `ONB-00` excluded from the target. Do not close review prematurely.

## Primary objective
Reach **235 / 235 canonical final sprites strict DONE**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI.

## Trusted state — 2026-10-03
- Strict DONE: 214 / 235**.
- Production processed to DONE/review after semantic audit: **222 / 235**.
- Seven technical-pass sheets were returned to `REJECTED_SEMANTIC`: TECH WALK/WORK/CARRY, LOG WALK/WORK, ENG WALK/WORK.
- LOG-IDLE remains awaiting review; no automatic semantic promotion was granted.

## Latest intervention — character generation v1.9
- Kaggle runs `37148361639` and `37149024371` produced no fresh candidates because v1.8 aborted on `CLIP core prompt too long: 39`.
- Logs also showed critical T5 prompt instructions truncated at 192 tokens.
- v1.9 shortens and safely trims CLIP cores, raises T5 budget to 256, and puts action-defining constraints early.
- WORK/CARRY/WALK now use action-specific prompts and img2img strengths to reduce semantic false positives.
- Epoch is `identity-lock-v1.9`; the per-epoch retry cap now takes precedence over legacy total attempts.
- Character batches can include all six role actions, and queue ordering is forced to match exact dispatched IDs.

## Current priority
1. Dispatch the six-action OP v1.9 wave.
2. Require technical QA, then visual semantic review before promotion.
3. Regenerate the seven explicit semantic rejects under v1.9.
4. Review remaining character candidates individually.
5. Preserve runtime visibility and green Android CI for every strict promotion.

- 2026-10-03: CHR-LOG-IDLE semantic review passed (stable identity/camera/palette, readable subtle idle); runtime QA passed and prior integrated Android CI is green. Strict DONE advanced to 214/235.
