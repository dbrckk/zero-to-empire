# Parallel asset production plan — 2026-09-21

Strict baseline after BLD-06 review: **176 / 235**.
Strict remaining: **59** = 35 building tiers + 24 character sheets.

## Lane ownership

- Kaggle controlled building lane: **BLD-05 T0–T6**.
- Kaggle controlled character lane: **CHR-OP-IDLE / CHR-OP-WALK** retry; CHR-OP-WORK/CARRY remain paused until identity-lock is reliable.
- ChatGPT/manual parallel lane must not duplicate the active Kaggle building family.

## Manual generation backlog

1. **BLD-10 T0–T6** — portal-only family. Existing ChatGPT portal sheets are source candidates, not strict runtime assets. Extract and verify each portal independently; reject labels, board backgrounds and non-portal scenery.
2. **BLD-08 T0–T6** — coherent Dyson/energy-harvesting family with one persistent hub and incremental structure.
3. **BLD-07 T0–T6** — site-card/platform contamination is historically severe and Kaggle is already at 7/8 attempts; prefer manual isolated-object generation before spending the last automated attempt.
4. **BLD-04 T0–T6** — replace scale-clone cyan office family with meaningful structural evolution and no landscaping/platform.
5. **Characters not actively owned by Kaggle** — CHR-TECH, CHR-LOG, CHR-ENG (6 actions each), plus CHR-OP-REPAIR/CELEB. Identity-lock and single-subject framing are mandatory.

## Sprite-atlas work

Atlas production starts from reviewed isolated sources only. A concept sheet is never itself a runtime atlas.

For every atlas source:
1. isolate each cell/object;
2. remove labels, gutters and board background;
3. preserve alpha;
4. normalize pivot/canvas;
5. run edge, component, crop and text-risk checks;
6. visually review each cell;
7. emit atlas PNG/WebP plus machine-readable JSON frame metadata;
8. promote only frames tied to an approved manifest asset.

Current atlas seed: BLD-10 portal-only sources and detached portal VFX variants. They remain **candidate-only** until individual semantic review.
