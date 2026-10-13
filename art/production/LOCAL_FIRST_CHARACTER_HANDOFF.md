# Local-first character production (13 October 2026)

The user requested that all **new** art be created directly in the ChatGPT working environment, **without Kaggle**.

## Production decision

- Stop automatically scheduling `Asset Autofactory 235` and `Kaggle Async Character Collector`. The manual dispatch entrypoints remain for historical compatibility but are not part of the new production workflow.
- New art is generated locally as deterministic RGBA character sprites and assembled as **1024×1024, 4×4 grids of 256×256 cells**, matching `CanonicalCharacterRaster.kt`.
- Role silhouettes and costumes are fixed across actions: OP orange helmet/dark suit, LOG ivory helmet/amber jacket, ENG ivory helmet/graphite-cyan outfit.
- The first locally created candidate pack contains **16 atlases / 138 authored frames** covering every unresolved canonical character ID. Its exact source and PNGs are attached to the ChatGPT conversation as `zero_to_empire_local_characters_v1.zip`, with a `zero_to_empire_local_preview.png` contact sheet. These files are **not yet checked into GitHub or wired into Android resources**.
- These are **stylized 2D prototypes**, not approved AAA production assets. Technical drawing quality, animation smoothness, silhouette clarity, runtime compatibility and artistic review still need improvement.
- The master ledger's strict DONE count must **not** change on the basis of creating these candidate PNGs. Each asset requires review and Android integration first.

## Next steps

1. Iterate the local sprite renderer's anatomy, pose dynamics, shading and prop interaction; regenerate the atlases locally.
2. Import only reviewed candidate PNGs into `app/src/main/res/drawable-nodpi` and the canonical incoming-art directory.
3. Run full character motion and Android release validation before marking any of the 16 unresolved entries strict DONE.
4. Remove remaining Kaggle-only assumptions from the queue/orchestrator as the local pipeline is proven.

Do not automatically resume Kaggle or count candidate PNG files as strict DONE.

## Local authored rig v2 — 13 October 2026

A new **candidate-only** pack was generated entirely in the ChatGPT local working
environment, with no Kaggle, remote models, paid API, or GPU dependency.

- Artifact: `zero_to_empire_local_characters_v2.zip`; SHA-256
  `5a10cd25cbc815c2f3d06f62988effdd5360d25894bce7cc88f975f9513ea575`.
- Source in the same chat: `zte_local_rig_v2.py`; SHA-256
  `f56da2955936c49b75dd8913c96e351a4ea94791c06428fe89645ab24ee69622`.
- Contents: **18 transparent 1024x1024 PNG atlas candidates / 150 frames**,
  covering the **16 unresolved assets** plus OP-IDLE and LOG-IDLE reference
  atlases. All 256x256 frames and their SVG drawings are included as editable
  source, with GIF motion loops, JSON SHA-256 manifest and review poster.
- The local preflight completed with **zero file/geometry/alpha/padding errors**.
  This is a technical check, not a claim of animation or AAA artistic quality.
- This ZIP has **not been committed to GitHub** and has **not replaced Android
  drawable resources**. Its download link is attached in the conversation.
  Do not pretend GitHub Actions has inspected it until it is uploaded.
- Anatomical articulation and overall artistic fidelity are still stylized
  prototypes. Before release, check foot locking, hand/tool contact, carry
  grip, motion-loop seams, 42dp Android readability and visual consistency.

### GitHub handoff without automatic promotion

`tools/sprites/verify_local_character_bundle.py` validates a submitted local
ZIP without extracting arbitrary paths. It checks the 18 expected manifest IDs,
source hashes, RGBA 4x4 frame sheets, transparent padding, safe borders,
nonempty/unique frames, and the SVG source for every frame. Every output is
marked `visual_semantic_approval: false`, `android_validation: false`,
`strict_done_granted: false`.

The read-only `.github/workflows/local-character-review.yml` is triggered
when a candidate ZIP is uploaded directly into
`art/production/local-candidates/`, or on manual dispatch with
`bundle_path` set to that repository-relative ZIP path. It produces
full-resolution role review panels as GitHub artifacts but **cannot** modify
the canonical queue, grant strict DONE, or trigger Kaggle.

The current progress remains **219/235 strict DONE**. Do not count the 18
candidate PNG files or merely successful preflight checks as production art.
