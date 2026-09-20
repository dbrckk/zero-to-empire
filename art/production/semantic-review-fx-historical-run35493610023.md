# Historical FX semantic review — run 35493610023

Date: 2026-09-20
Result: **APPROVE FX-00..FX-08 and FX-17 for strict reconciliation after runtime-coverage CI**

## Exact runtime evidence
Workflow run `35493610023` reviewed the exact Android WebP resources currently referenced by the app.

- runtime contract: 10 / 10 PASS
- dimensions: 512×256 RGBA sheets
- contact sheet generated from exact runtime files
- runtime metadata and SHA-256 hashes persisted in the workflow artifact

## Semantic review
The exact runtime sheets match their manifest roles:

- `FX-00`: warm welding sparks
- `FX-01`: small furnace flame
- `FX-02`: large furnace / plasma flame
- `FX-03`: industrial smoke puff
- `FX-04`: steam vent
- `FX-05`: cyan energy pulse
- `FX-06`: warm energy pulse
- `FX-07`: construction dust / debris
- `FX-08`: upgrade construction flash
- `FX-17`: mastery crown shimmer

No baked text, watermark, opaque background, unrelated object, or manifest-role mismatch was observed.

## Runtime coverage
Existing gameplay already uses FX-00, FX-04, FX-05, FX-06, FX-07 and FX-08.

This PR adds visible active-world coverage for:
- FX-01 in early industrial eras;
- FX-02 in mid industrial/advanced eras;
- FX-03 as ambient production smoke;
- FX-17 in late/mastery eras.

The new mapping is deterministic and unit-tested. It uses the existing shared world clock and respects reduced-motion behavior.

## Promotion gate
Strict DONE may only be applied after:
1. this runtime-coverage PR has green Android CI;
2. Android Emulator Smoke is green;
3. the strict queue/progress reconciliation PR is itself green.

No count is incremented by this review document alone.
