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
  `96c9b2c1bb8a0ce4034f94df7e16fb0a2362d284692c723bf269a09c6bfc2b24`.
- Source in the same chat: `zte_local_rig_v2.py`; SHA-256
  `f56da2955936c49b75dd8913c96e351a4ea94791c06428fe89645ab24ee69622`.
- Contents: **18 transparent 1024x1024 PNG atlas candidates / 150 frames**,
  covering the **16 unresolved assets** plus OP-IDLE and LOG-IDLE reference
  atlases. All 256x256 frames and their SVG drawings are included as editable
  source, with GIF motion loops, JSON SHA-256 manifest and review poster.
- The bundled `review.html` is an **offline, mobile-friendly animation player**:
  choose role/action, pause, adjust playback speed, scrub exact frames, compare
  against the same-role IDLE, and check actual 42px game readability. After
  unzipping, preserve the `atlases/` directory beside `review.html`.
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

## Checkpoint 14 October 2026 — local originals and Android

The first-party vector rig and its 18 RGBA atlases were revised directly in the
ChatGPT work, then reproduced from source in GitHub. The local generator
[`render_chatgpt_originals.py`](../../tools/sprites/render_chatgpt_originals.py)
commits **150 editable SVG animation frames** and 18 1024×1024 RGBA atlases
to `art/incoming/chatgpt-original`. The authored changes include reinforced
workwear, helmet/boot details, equipment consistency and larger physically
connected WORK/REPAIR motion. Generation workflow
[38572255542](https://github.com/dbrckk/zero-to-empire/actions/runs/38572255542)
and Asset Pipeline CI [38572255480](https://github.com/dbrckk/zero-to-empire/actions/runs/38572255480)
both succeeded.

The later reject-only visual audit produced
[`visual-risk-qa.json`](../incoming/chatgpt-original/visual-risk-qa.json)
in workflow [38573935196](https://github.com/dbrckk/zero-to-empire/actions/runs/38573935196):
**18 atlas checked, 150 frames checked, 0 automatically detected blocking risks,
0 semantic approvals and 0 strict DONE changes.** Machine thresholds detect
only specific silhouette/motion/color risks, not premium/AAA visual fidelity.

The isolated Android review APK is built using all 18 current original atlases
with `applicationId=com.zerotoempire.game.originalreview` and a strict
`released_to_production=false` provenance report. Build
[38573961240](https://github.com/dbrckk/zero-to-empire/actions/runs/38573961240)
succeeded. The emulator workflow
[38574480192](https://github.com/dbrckk/zero-to-empire/actions/runs/38574480192)
then succeeded while installing the APK, launching the app, scrolling the
four-role gallery, selecting ENGINEER and capturing the **actual full-body
39dp/42dp night/day game-size character**, not merely its heading. The PNG and
UI hierarchy are contained in artifact `local-original-android-emulator-visual-evidence`
for that run.

**Important visual shortfall:** although local sprites are original,
reproducible, motion-tested and runtime-renderable, their 2.5D vector/flat
rendering does not yet match the more realistically rendered canonical TECH
role. Reviewers must compare face, anatomy, material detail, movement and
gameplay readability across all roles before granting any strict approval.
The exact production master remains **219/235 strict DONE** with **16 unresolved**;
the original candidates must not be promoted by CI merely because all PNGs
pass automatic gates.

For users who only have Android, the current workflow supplies both an
installable **review-only APK** and a compact, fully offline HTML player for
the authored atlas candidates. The HTML player can choose role/action, pause,
scrub, change FPS and compare day/night 39px/42px presentation. The ZIP and
APK are provided in the corresponding ChatGPT session; they are not production
releases.

Next gate: explicit visual review of each of the 16 outstanding IDs, any
required art revisions to match TECH style, then approved-only Android runtime
integration, release validation and a manifest/queue update based on real
evidence. Do not resume remote Kaggle-based art creation by default; all
remaining artwork is to be authored directly in the ChatGPT working environment.


## 14 October 2026 evening — v3 local material finish

This iteration produces **all 18 role/action candidate atlases directly in the
ChatGPT-authored local pipeline**, covering 16 unresolved character IDs plus
two OP/LOG reference-IDLE sheets. It is fully separate from the old Kaggle
producer. The source now includes
[`local_character_material_finish.py`](../../tools/sprites/local_character_material_finish.py):
a deterministic warm/cool directional-light and alpha-edge material pass
applied after CairoSVG rasterization to each of 150 original editable SVG
frames, before composing the fixed 1024×1024 atlas. The code restores each
source alpha plane exactly and preserves the same coordinates, action frame
count, pose identity, pivots and 256×256 cells.

The generator records
`chatgpt-original-character-rig-v3-material-finish` and
`local-alpha-safe-directional-light-v1` in
`art/incoming/chatgpt-original/creation-manifest.json`.
The local creation workflow
[38624450028](https://github.com/dbrckk/zero-to-empire/actions/runs/38624450028)
succeeded, uploaded reviewed-candidate evidence and committed the 18 v3
atlas files and 150 frame SVGs into `art/incoming/chatgpt-original`.
The repository's
[Asset Pipeline CI 38624512306](https://github.com/dbrckk/zero-to-empire/actions/runs/38624512306)
passed after introducing the material module.

The corresponding ChatGPT-generated ZIP
`zero_to_empire_local_characters_v3.zip` contains the 18 atlas PNGs,
150 SVG frames, 18 animation GIFs, offline Android-friendly `review.html`,
`local_character_material_finish.py`, `rebuild_from_svg.py`, the review
poster and a SHA-256 creation manifest. The standalone viewer is *not*
evidence of native Android runtime approval. Gameplay-size 42px visual
comparison reveals that small tools, expressions and material details
remain difficult to discern. **This material polish does not bring flat
2.5D illustrations to the desired AAA quality by itself.**

A new isolated Android review build was requested using
`ops/local-original-android-review-trigger.txt` (run
[38624730867](https://github.com/dbrckk/zero-to-empire/actions/runs/38624730867)).
Its compilation, emulator screenshots and any approval outcomes must be
verified independently; no results are presumed here.

As before, all original v3 sprites remain `review_only`; the authoritative
ledger stays **219/235 strict DONE, 16 unresolved** until explicit semantic
review and production-grade Android validation. Keep all future art
creation in this first-party ChatGPT/local workflow, not remote Kaggle.
