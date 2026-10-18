# Project state

Status: active — Android pipelines functional; original character art still requires premium visual-semantic and production approval.

## Working
- **2026-10-18**: [PR #215](https://github.com/dbrckk/zero-to-empire/pull/215) merged emulator `gfxinfo framestats` and PSS evidence; Android CI and Emulator Smoke passed. First software-rendered API35/debug sample: 22 eligible frames, p95 916.06 ms, total PSS 409108 KiB. These noisy, small-sample numbers are **not production FPS**. [PR #217](https://github.com/dbrckk/zero-to-empire/pull/217) corrects nonzero flag filtering per Android docs and increases the bounded sample; verification pending.
- **2026-10-16**: [PR #205](https://github.com/dbrckk/zero-to-empire/pull/205) corrected ENG REPAIR composite station/actor geometry; source-verified static console in all 10 SVG poses. PR targeted [38937726736](https://github.com/dbrckk/zero-to-empire/actions/runs/38937726736) and Asset Pipeline [38937727160](https://github.com/dbrckk/zero-to-empire/actions/runs/38937727160), main targeted [38937862782](https://github.com/dbrckk/zero-to-empire/actions/runs/38937862782), main Asset Pipeline [38937862630](https://github.com/dbrckk/zero-to-empire/actions/runs/38937862630) and original candidate regen [38937862598](https://github.com/dbrckk/zero-to-empire/actions/runs/38937862598) **SUCCESS**. Updated report now **0/18 technical blockers**. Strict remains **219/235**; 16 candidates not semantically or production-approved.
- Canonical master queue: **219/235 strict DONE**, with 16 pending CHR actions (OP ×5, LOG ×5, ENG ×6).
- ENG REPAIR source candidate includes physically anchored repair fastener (PR #149); actual SVG contact QA and isolated Android emulator review passed. Not approved.
- OP WALK has an original locally authored eight-frame walk rig with anti-phase legs, operator-specific support and constant-speed planted foot (PRs #150 and #152). Source atlas, SVGs and GIFs reproduce; **no production drawable has been promoted**.
- OP WALK **eight real Android frames** verified by isolated emulator [38770555377](https://github.com/dbrckk/zero-to-empire/actions/runs/38770555377), PR #154.
- Actual **city character layer motion** verified by isolated emulator [38774032853](https://github.com/dbrckk/zero-to-empire/actions/runs/38774032853), PR #155: 24/24 role/action captures, OP WALK frames 480–487, two real-stage screenshots 0.7s apart with 5,251 thresholded changed stage pixels in [32,129][1048,1757].
- Android CI on [PR #155](https://github.com/dbrckk/zero-to-empire/pull/155) run 38772335910 **SUCCESS** and [main](https://github.com/dbrckk/zero-to-empire/actions/runs/38773512852) run 38773512852 **SUCCESS**. Isolated review APK run 38773513009 **SUCCESS**.

## Blockers
- The 16 unfinished CHR actions are still original-art QA candidates, **not AAA-approved runtime sprites**. The isolated stage is a simplified dark gradient containing the real character renderer, not the final decorated city scene.
- OP WALK's moving body is confirmed onscreen, but full-speed slide/weight evaluation in the actual shipping city, explicit semantic approval, exact production WebP staging and release resource verification remain outstanding.
- Never infer strict DONE from frame hashes, code tests, screenshots or debug-only presentation alone.

## Priority
1. Review OP WALK movement/art against real production city context and approved visual identity. Fix meaningful visual defects one at a time.
2. Only after explicit semantic approval, stage the exact resource into production and verify Android release/runtime; then update the strict master ledger.
3. Continue LOG/ENG/OP remaining actions one by one, prioritizing real material/tool/body interaction and consistent role silhouettes.
4. Preserve all existing progress, privacy and separate production save data.

## Last manual verification
- **2026-10-16**: master queue re-counted: **219 DONE / 235**, 16 `NEEDS_REVIEW`. Local candidate risk report: **18 assets, 0 blocking**, no automatic promotion. PR #205 merged as `1c9693b6`; exact production and semantic review still pending.
- **2026-10-15**: strict **219/235**, 16 pending. Source-of-truth `art/production/master-asset-queue.json`.
- Android screenshot evidence artifact: **11992229467** from run **38774032853**.
- No new unit tests added; PR #153 was closed without merge.

<!-- AUTO:START -->
## Automatic repository state

Generated: 2026-10-18T21:30:16Z

### Git
- Branch: `main`
- Head: `cd8f8e6d362b`
- Commit date: 2026-10-18T17:29:47-04:00
- Commit: docs(art): record inspected Android role/action poses and eight-frame operator walk review (#230)
- Tracked files: 1823

### Recently changed files
- `docs/art/ANDROID_CHARACTER_SEMANTIC_REVIEW_20261018.md`
- `docs/art/ANDROID_CHARACTER_SCREENSHOT_INSPECTION_20261018.md`
- `.github/workflows/character-strict-approval-readiness.yml`
- `ops/chatgpt-original-handoff-trigger.txt`
- `ops/local-original-android-review-trigger.txt`

### Project signals
- `build.gradle.kts`
- `settings.gradle.kts`

> Generated by dbrckk/repo-standards. Keep manual priorities and blockers outside the AUTO markers.
<!-- AUTO:END -->
