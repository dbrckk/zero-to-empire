# OP WALK — planted-foot stride review (15 October 2026)

## Latest contact-speed intervention (PR #152)

- **Cause of first CI failure:** the initial `art/op-walk-stance-drift-20261015` patch introduced a malformed Python indent in `local_character_contact_gait.py`. Workflow `38753268106` failed while compiling generators. This was fixed on the same branch before merge; do not treat initial code as passing.
- **Merged source:** PR [#152](https://github.com/dbrckk/zero-to-empire/pull/152) on `main`, squash commit `808f29a4`. OP WALK's stance-only ankle translation is now linear in the relative stride cycle (constant apparent ground speed), instead of applying smoothstep throughout support. The original swing/recovery easing is retained. LOG/ENG normal gait and every CARRY use the prior implementation.
- **Validation:** corrected PR Asset Pipeline CI [38762145864](https://github.com/dbrckk/zero-to-empire/actions/runs/38762145864) **SUCCESS**; mainline Asset Pipeline CI [38762241985](https://github.com/dbrckk/zero-to-empire/actions/runs/38762241985) **SUCCESS**; 18 candidate atlas and SVG/GIF generation [38762242160](https://github.com/dbrckk/zero-to-empire/actions/runs/38762242160) **SUCCESS** including the OP WALK emitted-frame geometry gate. Inspected the new 8-frame `zte_chr_op_walk_final.png` atlas: consistent face/costume and alternating footwear, but artistic quality at gameplay animation speed still needs review.
- **After regeneration:** eight distinct poses, mean adjacent pixel activity **0.086641** (previous **0.086847**), loop seam / median **0.7428** (previous **0.5769**), `abrupt_loop_reset_risk=false`; these numerical diagnostics do not prove the animation improved semantically. The objective of this patch is steadier *stance velocity*, not maximized frame-to-frame activity.
- **Review-only Android build:** new workflow [38762436053](https://github.com/dbrckk/zero-to-empire/actions/runs/38762436053) was started after generated candidates were committed. Confirm successful APK and subsequent emulator run before citing Android device screenshots for this exact revision.
- **Strict status:** unmodified at **219/235**. This update does not constitute acceptance of `CHR-OP-WALK` for production, and does not change release drawables.

## Scope and source

Canonical item: `CHR-OP-WALK`, still **NEEDS_REVIEW**. The existing mainline update `7383a38d` introduces the `op-walk` gait profile only for the operator. Local first-party assets are regenerated through `tools/sprites/render_chatgpt_originals.py` and the `ChatGPT Original Character Candidates` workflow. Default LOG/ENG walking and loaded carrying retain their former profile; shipping Android drawables and economy/save logic are untouched.

An independently prepared parallel alternative (PR #151) was **closed without merge** after main acquired this overlapping, already-CI-verified improvement. Do not resurrect or merge its divergent `op-walk-v2` profile.

## Actual evidence

- Before the update, at main `c603ee41`, the eight-frame OP walk mean adjacent pixel activity was **0.075364**, last-to-first loop seam / median ratio **1.1309**.
- After regeneration, the authoritative `art/incoming/chatgpt-original/animation-review.json` reports mean activity **0.086847** (**+15.2%**) and loop seam / median ratio **0.5769**. Both are diagnostic technical metrics, not a subjective AAA rating.
- `op-walk` configuration uses **19px reach / 21px clearance** instead of **14px / 16px**. It deliberately offsets the stride phase for more readable sampled poses while retaining planted Y=226 support and anti-phase left/right legs.
- Current original atlas at `art/incoming/chatgpt-original/candidates/zte_chr_op_walk_final.png` was inspected at the native 256px frame resolution and 39/42px presentation; it shows eight different full-body poses, consistent uniform/helmet, a visible airborne foot and reciprocal arms.
- Asset Pipeline CI [38744789050](https://github.com/dbrckk/zero-to-empire/actions/runs/38744789050) **SUCCESS**.
- Original character candidate run [38744789685](https://github.com/dbrckk/zero-to-empire/actions/runs/38744789685) **SUCCESS**, including explicit live-SVG `Validate actual OP walking contacts and reciprocal leg travel`.
- Isolated Android review APK runs [38744963714](https://github.com/dbrckk/zero-to-empire/actions/runs/38744963714) and [38745033106](https://github.com/dbrckk/zero-to-empire/actions/runs/38745033106) both **SUCCESS**: debug package compilation, existing Android unit checks, lint and production-save-package isolation.
- Android emulator run [38745543878](https://github.com/dbrckk/zero-to-empire/actions/runs/38745543878) **SUCCESS**, with GitHub artifact `11979140579` (`local-original-android-emulator-visual-evidence`). The downloaded `24-stage-coverage.txt` confirms **24/24 actual role/action captures**; screenshot `atlas-OPERATOR-WALK.png` was inspected and shows the complete operator on **42dp night / 39dp day** backgrounds.
- These prove the **isolated QA UI renders the proposed asset**, not that its animation meets premium art standards in the shipping game. One screenshot does not prove the 8-frame loop is free of sliding at real speed.

## Acceptance gate before strict DONE

1. Confirm one isolated review APK and its 24-role/action Android emulator captures completed successfully on the exact new original atlas, with OPERATOR/WALK visible at 39/42dp.
2. Review the actual 8-frame GIF at loop speed for planted contacts, foot recovery, torso counter-sway and absence of silhouette pops or sliding. At real scale movement must be legible, not just different frame hashes.
3. Compare art quality to the approved runtime style; obtain an explicit semantic review. The reviewed candidate is **not** the shipping sprite merely because QA and the review app passed.
4. Convert approved exact source to runtime WebP, show actual production gameplay reference/visibility and green Android build/lint/release checks before touching `master-asset-queue.json`.
5. Keep canonical **219/235 strict DONE** until all evidence above is observed and attached. Do not batch-promote the other 15 unresolved assets.

## Reproduce

```bash
python -m pip install Pillow==11.3.0 CairoSVG==2.7.1
python tools/sprites/render_chatgpt_originals.py --output-dir art/incoming/chatgpt-original --save-svg
python tools/sprites/render_original_character_previews.py --output-dir art/incoming/chatgpt-original
```

The original authored source, PNG, SVG, GIF, review HTML and independent APK artifact are kept in this repository/Actions pipeline for reproducibility. No new unit tests were added.
