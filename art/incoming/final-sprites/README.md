# Final sprite intake

Place only isolated PNG sprite candidates in this directory.

The `Final Sprite Pipeline` GitHub Action validates transparency, minimum resolution and safety padding, normalizes the sprite to a square bottom-centred transparent canvas, converts it to lossless WebP, and publishes the processed runtime candidates as a workflow artifact.

This is a technical production gate, not an automatic artistic-quality claim. A generated image is not `DONE` in `docs/art/FINAL_AAA_SPRITE_MANIFEST.md` until it also has the correct identity, no baked text/logo/UI/background, passes visual review, is committed at its declared runtime path, is referenced and visible in-game, and Android CI is green.

Naming must match the manifest runtime stem, for example:

`zte_business_00_t0_final.png` -> `zte_business_00_t0_final.webp`

Composite sheets, dashboards and reference boards are forbidden from this intake directory.
