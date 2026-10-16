# PROJECT CONTINUITY — Zero → Empire

## 2026-10-16 verified — ENG REPAIR fixed-station risk-audit correction

- **PR [#205](https://github.com/dbrckk/zero-to-empire/pull/205)** squash-merged into `main` as `1c9693b682741cf74578d21cff4c88646cdff6b0`. The original `CHR-ENG-REPAIR` candidate includes a deliberate stationary service console that made the generic composite bounding-box classifier incorrectly flag a portrait/wide character silhouette. No released Android drawables or gameplay code changed.
- Risk QA now examines the engineer-only region for **frame geometry**, and only after checking all **10 editable ENG/REPAIR SVGs** for the identical fixed service station and its large socket. Original composite frames remain subject to palette, head/prop, action and temporal-risk checks. No false exemption for imports or other roles.
- **PR Character Motion Audit [38937726736](https://github.com/dbrckk/zero-to-empire/actions/runs/38937726736) SUCCESS** with the **real 18-atlas audit** reporting zero image-only blocking risks; **PR Asset Pipeline [38937727160](https://github.com/dbrckk/zero-to-empire/actions/runs/38937727160) SUCCESS**. Following merge, **main Character Motion Gate [38937862782](https://github.com/dbrckk/zero-to-empire/actions/runs/38937862782)**, **Asset Pipeline [38937862630](https://github.com/dbrckk/zero-to-empire/actions/runs/38937862630)**, **Character strict review matrix [38937862662](https://github.com/dbrckk/zero-to-empire/actions/runs/38937862662)**, and **original 18 atlas generator [38937862598](https://github.com/dbrckk/zero-to-empire/actions/runs/38937862598)** all **SUCCESS**.
- The generated `art/incoming/chatgpt-original/visual-risk-qa.json` was committed to `main` by the source regeneration in `04925f8a`: **18 inspected, 0 blocking risks**, `CHR-ENG-REPAIR.fixed_service_station_svg_verified=true`, `actor_only_geometry_assessment=true`. This is **technical rejection screening**, not visual/semantic acceptance. **Canonical strict remains 219/235 DONE, 16 NEEDS_REVIEW** (authoritative `art/production/master-asset-queue.json` re-counted).
- **Next:** revisit `CHR-OP-WALK` in a realistically composed *shipping* city at true motion speed; assess foot contact, weight, consistency with already approved assets and small-screen legibility. Correct meaningful defects one at a time. Promote an action only after explicit semantic review, exact production WebP linkage and successful Android release/runtime/device checks. Then proceed to remaining CHR actions individually. No automatic strict promotion, save/economy change or new unit tests in this intervention.

## 2026-10-15 verified — OP WALK city-stage Android motion

- **PR #154** merged as `a0664b99`: functional Android stepping proof of eight OP WALK frames; emulator run **38770555377 SUCCESS**, artifact **11991227425**, recorded consecutive frames **531–538** in real 39/42dp QA preview. Those earlier screenshots did not show the full city stage, which was below the fold.
- **PR #155** merged as `1b339da3`: debug-only Compose semantic marker and isolated emulator visual-integrity gate. It scrolls to the actual 620dp city character renderer, requires a useful viewport and compares two live screenshots *inside that stage*. PR Android CI **38772335910**, main Android CI **38773512852**, review APK **38773513009**, and actual emulator **38774032853** all **SUCCESS**.
- Actual isolated Android output verified: **24/24** role/action captures; eight successive OP WALK UI frames **480–487**; city stage bounds **[32,129][1048,1757]**; **5,251** pixels changed by more than 14 on at least one RGB channel in 0.7 seconds. Both OP actors are visible in the actual character layer. Emulator evidence artifact: **11992229467**. Screenshots were downloaded and visually inspected.
- Scope: this is a genuine runtime-character-layer check in a **debug-only gradient stage**, not proof of art quality in the complete shipping city. No new unit tests were added: PR #153 was closed for conflict with the 88-rule standard. No automatic sprite approval or production resource replacement. Strict queue **219/235**, 16 unresolved, unchanged.
- Next priority: OP WALK full-speed foot-slide/weight and style review in a realistically composed city scene, followed by exact approved WebP production references and Android release evidence before any strict promotion. Then continue other CHR action reviews one by one.

## OP WALK planted stance — PR #152 (2026-10-15)

- PR **#152** merged on `main` as `808f29a4`, after resolving an initial **Python indentation failure** (`38753268106`). The corrected PR Asset Pipeline run **38762145864** succeeded, as did main Asset Pipeline **38762241985** and original character candidate regeneration **38762242160**.
- Isolated OP WALK stance now uses a *linear ground-relative foot speed* while planted; existing eased swing recovery and all LOG/ENG/CARRY gait profiles remain unchanged. Regenerated eight-frame first-party atlas visually inspected, technical loop diagnostics show **0.086641** mean pixel activity and **0.7428** seam/median with no abrupt-reset flag. This is candidate evidence, not final artistic acceptance.
- Android isolated debug QA APK **38762436053 SUCCESS** (build/lint/existing checks). Android emulator **38762944605 SUCCESS**, artifact **11987210646** with `24-stage-coverage.txt` (24/24 views) and `atlas-OPERATOR-WALK.png` directly inspected at **42dp night / 39dp day**. This proves isolated app-scale rendering, not shipping gameplay or animation-loop semantic approval.
- Strict queue still **219/235** with **16 character actions pending**; no production asset or save/economy changes. Details: `docs/art/OP_WALK_STRIDE_REVIEW_2026-10-15.md` and `.ai/session-state.json`.

## Verified OP WALK intervention — 2026-10-15

- **PR #150** merged at `7383a38d`, isolating an `op-walk` contact gait to the operator and correcting previously simultaneous arm swing. No release character asset was promoted.
- **GitHub Actions green**: Asset Pipeline CI `38744789050`; original candidate generation `38744789685` (including all eight actual SVG foot/boot pose integration checks); isolated Android review APK runs `38744963714` and `38745033106`; 24-role/action Android emulator verification `38745543878`.
- Review artifact `11979140579` contains `atlas-OPERATOR-WALK.png` screenshot and `24-stage-coverage.txt`, both downloaded and inspected. The **OPERATOR/WALK** candidate displays full-body on **42dp night / 39dp day** emulator backgrounds. Technical mean adjacent motion increased `0.075364 -> 0.086847` (+15.2%); this remains motion evidence, not artistic approval.
- Next unresolved gate: visual quality at animation speed within the *production* world, semantic approval, exact final runtime WebP linkage and release build checks. All 16 original character actions, including this improved one, remain **NEEDS_REVIEW** until those conditions pass.
- **Canonical strict count remains 219/235**. No game economy, saves, released runtime atlas or production manifest was altered. See `docs/art/OP_WALK_STRIDE_REVIEW_2026-10-15.md` and `.ai/session-state.json` for exact run IDs and follow-up.

## Current verified action — 2026-10-15 (ENG REPAIR fixed socket)

- **PR #149** merged as `7dadb8b9`: locally authored `CHR-ENG-REPAIR` now includes a stationary, ground-mounted service console with a defined bolt contact at **(218,129)** in its 256px cell. Wrist, prop, and VFX share an inverse-rotated rigid tool tip so the ratchet stays on the same bolt through all 10 frames.
- **GitHub Actions 38740750108** (PR asset CI), **38740866078** (main asset CI), and **38740866046** (original character renderer) all **SUCCESS**. The renderer's actual ten generated SVG frames passed the new workflow integration audit, checking identical fixed console geometry and tool-endpoint error below 0.08px. The production candidate atlas, SVGs and previews regenerated on main in `c7920bb`; direct inspection confirms a full-body stable ENG model and visible service console.
- **Android isolated visual-review APK run 38741077306 SUCCESS**, with build, existing tests, lint, separate non-production app and provenance. Emulator **38741556309 SUCCESS**, uploading artifact **11975429234** with 24 role/action screenshots. Directly inspected `atlas-ENGINEER-REPAIR.png`; the engineer and fixed service console are visible together at 42dp night / 39dp day. This is isolated app-scale proof, not shipping game integration or a strict AAA art approval.
- **Strict DONE remains 219/235 (16 outstanding)**. Original art is only a candidate; no production Android drawable, economy engine, save data, master queue or strict-status approval was changed. Next: review final art semantics at animation speed in full gameplay context, obtain explicit approval, and verify exact production runtime/Android CI before promoting even this one asset.
- After ENG REPAIR is individually finished, prioritize OP WALK foot contact/weight transfer. Do not restart legacy remote provider batches blindly.

## Verified latest — 2026-10-15 (PR #148 completed)

- **PR #148 merged** at `6194c1b3`: the local, self-contained original-art reviewer now renders a single selected atlas frame simultaneously in its large canvas and true game-size **42px night / 39px day** previews. Animated GIFs are shown only while playback mode is active; switching roles/actions resets playback consistently.
- Exact inline-JavaScript interaction smoke check **PASS (7 cases)**. PR Asset Pipeline CI run **38739375267**, main Asset Pipeline CI run **38739530704**, Original Character Candidates generator run **38739530573**, and Repository standards run **38739532721** all **SUCCESS**. The generator committed regenerated `original-offline-review.html` to main on `cbd35665`, preserving independent, non-production art status.
- Directly inspected original atlas candidate frames for `CHR-OP-WALK` (gait amplitude still limited), `CHR-LOG-CARRY` (crate aligned with both grips, locomotion still requires review), and `CHR-ENG-REPAIR` (right-hand equipment visible, no convincing fixed repair target). These observations do **not** constitute an Android animation semantic approval or a strict promotion.
- Master queue re-counted on main: **219/235 strict DONE; 16 outstanding CHR actions**. Next work: finish meaningful action/contact/identity polish on one role at a time, visually inspect at Android gameplay size, then run runtime and CI verification before any promotion. 

## Current intervention — 2026-10-15 (after PR #147 merge)

- PR **#147** merged on `main` (`edbdfb76`); exact-main Asset Pipeline CI **38737302273** and Android CI **38737302024** both completed **SUCCESS**. Subsequent reconciliation advanced `main` to `4fbd8c34` without changing the strict backlog.
- Canonical strict remains **219/235**; **16 CHR actions** are unresolved. Original first-party SVG/PNG/GIF art is *review-only* and must not be promoted without exact semantic and Android evidence.
- The self-contained Android-friendly reviewer previously paused only its 256px atlas canvas: night/day game-size GIF previews kept moving out of sync. Branch `fix/offline-frame-scale-sync-20261015` changes still mode to draw the **same selected atlas frame** on all three canvases (256px, 42px night, 39px day), then restores all animated previews on exit.
- An interactive JavaScript DOM smoke exercise of the exact updated inline script passed seven scenarios, including manual frame stepping, scrubbing frame seven, role switching and restoration of GIF playback. **Asset Pipeline CI and device visual inspection for this fix remain to be confirmed.** No shipping runtime code, sprites or canonical approvals were changed.

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Verified current state — 2026-10-15 (authoritative; supersedes historical snapshot below)

- Canonical master queue: **219/235 strict DONE** and **16 CHR actions NEEDS_REVIEW** (12 REJECTED_SEMANTIC; 4 AWAITING_REVIEW). This is counted directly from `art/production/master-asset-queue.json` on main `fda91ff481b9f3af130c6c561b5cf45273e4dfc8`.
- The 18 locally authored original character atlas candidates are **review-only**; their existence is not semantic approval. Do not promote any CHR or claim 235/235 until exact art, live runtime/Android and CI evidence all pass.
- 2026-10-15 GitHub Actions Asset Pipeline CI run **38720992796** and ChatGPT Original Character Candidates run **38720992762** both failed at `test_renderer_invokes_attached_effects_after_hand`: a test pinned obsolete `local-attached-tool-and-wrist-highlights-v1`, while the renderer advertises versioned `action_vfx` metadata for a v2 ratcheting tool/wrist rig. Existing geometry and draw-order checks were otherwise present.
- Pull request **#147** on `fix/character-vfx-ci-metadata-20261015` updates that stale assertion while preserving VFX and tool/wrist ordering verification. **CI status is pending at this checkpoint**; do not claim the regression is resolved until a green complete run is observed. No Android/runtime sprite changes are included.
- Next: validate PR CI, merge only after green, then check the next original candidate workflow and inspect remaining 16 CHR atlases visually at game scale. The dated historical snapshot below is retained only for provenance.

## Historical state — 2026-10-09 (superseded)

- **Canonical strict DONE: 216/235**, production processed: **233/235**. The source of truth is `art/production/master-asset-queue.json`. Do not raise the number for production, technical QA, or mere manifest presence.
- **Remaining 19 (all CHR)**: OP WALK/WORK/CARRY/REPAIR/CELEB (5); TECH WALK/WORK/CARRY (3); LOG WALK/WORK/CARRY/REPAIR/CELEB (5); ENG IDLE/WALK/WORK/CARRY/REPAIR/CELEB (6). Technical states: 17 AWAITING_REVIEW, 1 REJECTED_SEMANTIC (TECH-WALK), 1 BLOCKED (LOG-CARRY).
- Full-sheet direct visual inspection on 2026-10-09 confirmed canonical `CHR-LOG-CARRY` has separate torso and leg rows with **no valid carrying action**; `CHR-ENG-IDLE` has only cropped portraits; `CHR-OP-WALK` and `CHR-TECH-WALK` visibly change identity/camera/clothes; `CHR-LOG-WORK` changes characters and tools. Existing `art/production/character-visual-review-findings-2026-10-09.md` records the wider 19-item visual audit. **No further strict promotions are justified without valid new source frames.**
- **Ledger corrected on 2026-10-09**: the 236-row manifest now has **217 DONE** (216 canonical strict + separately excluded ONB-00), **17 RUNTIME awaiting review**, **2 BLOCKED**, matching the authoritative 235 queue. The progress header is also reconciled. Historical promotion review remains **OPEN**. Do **not** confuse an installed runtime resource with strict approval.
- `CHR-LOG-CARRY` repair is reserved to the Pollinations full-body-per-frame v3 lane until `2026-10-10T18:00:00Z`: `art/production/controlled-character-regen-queue.json` was requeued `PENDING_POLLINATIONS` on commit `d3b96eb`. Its candidate must be staged separately, preserving historical canonical PNG. GitHub Action run `37979410539` completed **workflow SUCCESS but art REJECTED** (no approved candidate): source portraits were cropped, image endpoint intermittently returned **HTTP 402 Payment Required**, three early per-frame cache PNGs were retained, and the controlled queue reverted to **BLOCKED**. Do not requeue blind while the provider is charge-restricted; inspect QA/partial frames and choose a reliable free identity-preserving alternative.
- Fixes landed on `main`: `6fe179a` dynamic review CI; `ad0bf48` completion gate; `2f51782` provider ownership; `d3b96eb` controlled repair attempt; `50108f4` canonical full-audit reconciliation; `5000a2b` 19 manifest statuses corrected; `09b05ab` production planning excludes ONB-00 and routes character candidates to semantic review; `5990ea7` robust progress reconciliation; `837421e` rejects portrait fragments before caching. `87fa083`, `08e2db8` and `d65c64b` persist project state. GitHub Actions **Character strict review matrix** run `37978989707` SUCCESS and **Asset Pipeline CI** run `37979322055` SUCCESS (including audit `--allow-pending`); **Sprite Completion Gate** run `37979322152` SUCCESS means guard execution passed, **not** that the final 236-sprite audit ran or completion was approved.
- Prior .ai/session-state.json, README and old progress figures are historical and MUST NOT overwrite the above canonical counts.

### Next action sequence

1. LOG-CARRY provider attempt ended without a successful candidate. Keep canonical and runtime unchanged. The provider returned HTTP 402 and cropped frame fragments; do not use the three retained cached frames as production art. Resolve provider access or favor an existing free deterministic identity-preserving rig before another cost-bearing batch. Inspect every candidate frame for complete full-body, one LOG identity and a crate gripped by **both hands**. Do not mark strict DONE from heuristic QA alone.
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
