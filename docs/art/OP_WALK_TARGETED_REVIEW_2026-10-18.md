# OP WALK — targeted asset review (2026-10-18)

Status: REVIEW ONLY. No production promotion.

## Inventory reconciliation
- Canonical queue: 235/235 candidates produced; 219/235 strict DONE.
- Outstanding: 16 character action approvals (OP 5, LOG 5, ENG 6).
- Do not generate new buildings, scenery, vehicles, UI, or generic asset sheets: they are not missing from the canonical queue.
- Original candidate sources: `art/incoming/chatgpt-original/src_svg/OP/WALK/00.svg` through `07.svg`.
- Canonical authority: `docs/art/AAA_WORLD_SPRITE_BIBLE.md`.

## Confirmed source geometry
Frame 00 SVG is a 256×256 source with a shared graphite jacket/pants, amber helmet and restrained amber trim. It contains explicit `data-op-walk-foot`, `data-planted`, `data-ankle-x` and `data-ankle-y` metadata.
- Left foot: planted=true, ankle (115.45, 226.00).
- Right foot: planted=false, ankle (131.25, 224.54).

## Acceptance work, in order
1. Inspect all eight existing SVGs and rendered candidate atlas at original size and literal 39–42dp.
2. Compare planted ankle world-space positions across successive frames after character translation; diagnose true foot sliding rather than screen-space pose variation.
3. Inspect complete decorated shipping-city footage (not the simplified debug gradient), both day and night; verify ground visibility and consistent contact shadow.
4. If a concrete defect is observed, edit the existing source generator / SVGs minimally, preserve identity and material palette, and regenerate only OP WALK candidate outputs.
5. Run existing asset pipeline and Android CI, lint, emulator smoke; review full-speed animation. Never create new unit tests.
6. Leave strict status unchanged until explicit semantic approval and exact runtime WebP linkage.

## Explicit exclusions
- No changes to economy, save files, billing, or production drawables.
- No automatic semantic acceptance.
- Do not treat an illustrative concept sheet as a production sprite.
