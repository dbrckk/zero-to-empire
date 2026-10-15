# Original character assets authored directly in the project

This is the first-party, deterministic character creation pipeline for the
remaining strict-review work in **Zero to Empire**. It is independent of Kaggle,
Pollinations, and paid inference APIs. The artwork is created from editable code
in this repository, not from outsourced generated images.

## Existing files

- Creator: `tools/sprites/render_chatgpt_originals.py` (Pillow + CairoSVG).
- Animated preview creator: `tools/sprites/render_original_character_previews.py`.
- Canonical output: `art/incoming/chatgpt-original/candidates/`
  (18 PNG RGBA atlases, each **1024 × 1024**, 4 columns of **256 × 256** frames).
- Editable per-pose source: `art/incoming/chatgpt-original/src_svg/<ROLE>/<ACTION>/<NN>.svg`
  (**150 individual SVG sources**).
- 18 mobile-friendly GIFs: `art/incoming/chatgpt-original/previews/`.
- First-frame gallery: `art/incoming/chatgpt-original/original-review-contact-sheet.png`.
- Evidence: `art/incoming/chatgpt-original/creation-manifest.json`,
  `candidate-qa.json` and `animation-review.json`.

The roles are OP, LOG and ENG; every role has IDLE, WALK, WORK, CARRY,
REPAIR and CELEB. That is 18 atlas outputs: **all 16 unresolved manifest
actions plus two extra IDLE identity references** for already-strict-DONE
OP and LOG role families.

## Run and examine on Android

The files are committed to GitHub. Open the `previews` directory and tap any
GIF for its looping animation; open the gallery PNG to compare costumes and
faces across roles/actions. A phone can also download the latest
`chatgpt-original-character-atlases` ZIP from the [GitHub Actions workflow]
(../../.github/workflows/art-chatgpt-original-candidates.yml).
Unzip it in Android's Files application to inspect individual 1024px PNGs
and editable SVGs. No PC or Kaggle session is required to view the results.

To rerender from GitHub, run the **ChatGPT Original Character Candidates**
workflow or update `ops/chatgpt-original-trigger.txt`. The workflow
verifies all 18 IDs, canonical frame counts, alpha margins, editability of
all 150 SVGs and nonempty animations, and then commits changed files and
uploads a 90-day review artifact. No secret keys are needed.

For a manual offline rebuild, in an environment with Python, Pillow 11.3.0
and CairoSVG 2.7.1:

```bash
python tools/sprites/render_chatgpt_originals.py \
  --output-dir art/incoming/chatgpt-original --save-svg
python tools/sprites/render_original_character_previews.py \
  --output-dir art/incoming/chatgpt-original
```

## Quality gate and current limitations

This is **original editable game art**, not a claim that the art is already
premium AAA. The vector rigs guarantee a consistent face, helmet, outfit and
rigged limbs across role actions, avoid diffusion-induced morphing and support
frame-level refinements. They do not themselves prove correct physical
weight transfer, tool contact, gameplay legibility on real devices, visual
polish or premium art direction.

All 18 outputs are `review_only`, add **zero strict DONE**, and remain
outside canonical Android runtime resources. In particular, do not copy
original candidate files over a strict-DONE IDLE sprite. Promoting a
reviewed role family still requires action-level visual review, proven
same-identity role-wide animations, the actual Android runtime conversion
and validation, debug/runtime build evidence, and the dedicated
explicit-approval promotion workflow.

The master queue in `art/production/master-asset-queue.json` is the only
source of truth for strict progress. A technically verified PNG/GIF/SVG
does not change that count.


## v4 — locally authored contact-light animation details (15 October 2026)

The complete source for **all 16 unresolved canonical character actions** is
still authored and versioned inside this repository; the 18 original role
atlases include the two OP/LOG context IDLE references. No GPU/Kaggle,
third-party image model or remote provider is needed to rebuild these assets.

- `tools/sprites/local_character_action_fx.py` is an editable original SVG
  effect module. WORK/REPAIR now emit short role-colored light at the
  hand-held tool tip, with brightness synchronized to the wrist cycle.
  CARRY lights stay attached to case rivets. CELEB lights follow both
  wrists rather than adding floating/confetti sprites.
- `render_chatgpt_originals.py` assembles each effect into the original
  action SVG **after the physically attached hand**; the same source still
  creates all 18 1024px RGBA atlases and 150 editable SVG frames.
- The 15 October candidate build
  [38701107514](https://github.com/dbrckk/zero-to-empire/actions/runs/38701107514)
  succeeded and committed the v4 source and raster results.
- The corresponding pipeline regression checks passed in
  [38701390311](https://github.com/dbrckk/zero-to-empire/actions/runs/38701390311).
  Technical PNG QA found **18 complete atlases, 150 frames, zero automatic
  blocking visual-risk flags and no abrupt last-to-first loop resets**.
- The user-facing offline viewer can compare the same role/action/animation
  before and after this localized lighting pass at both 256px and 39–42px
  mobile presentation size. The source of truth remains this repository.
- The separate Android-only review build was requested in
  [38701447773](https://github.com/dbrckk/zero-to-empire/actions/runs/38701447773).
  Inspect its run and the downstream emulator evidence independently;
  compilation, screen captures, production authorization and art acceptance
  are distinct checks.

**Limit:** these are restrained refinements to original stylized 2.5D vectors,
not proof of premium AAA output. WORK/REPAIR, carry contact, foot planting and
small-screen game feel still require frame-by-frame human judgement. The
canonical count stays **219/235 strict DONE** until those artistic and
runtime gates actually pass.

## v6 — authored planted-foot WALK/CARRY rig (15 October 2026)

The six role/actions OP/LOG/ENG × WALK/CARRY have been **redrawn
in this repository** with a deterministic contact-aware foot rig
(`tools/sprites/local_character_contact_gait.py`); all 18 role/action
atlases are rebuilt from first-party editable SVG source. No Kaggle,
remote image service, outside stock illustration, or paid API is used.

- Each foot has an explicit 60% stance / 40% aerial recovery cycle;
  planted ankle height remains at 226 pixels while the upper body moves.
- The two legs run half a cycle apart, with smoothstep horizontal
  translation and sinusoidal swing clearance. Loaded CARRY uses smaller
  steps, lower foot clearance and less upper-body sway than WALK.
- The projected knee now bends forward in the swing phase rather than
  splaying sideways; boots roll about the ankle during heel strike and
  toe-off.
- Every torso element, head, arm, held tool and carried crate shares a
  single subtle weight-shift group, so this extra movement cannot detach
  hand-held equipment.
- `tools/sprites/test_local_character_contact_gait.py` protects foot
  contact, alternating feet, leg ranges, loop closure and controlled
  forward knee swing in the local renderer and CI.

The first revision was generated in
[workflow 38709967873](https://github.com/dbrckk/zero-to-empire/actions/runs/38709967873);
its bow-leg swing issue was inspected visually and revised. The revised
atlases, SVG frames and GIFs were generated successfully in
[workflow 38710288088](https://github.com/dbrckk/zero-to-empire/actions/runs/38710288088).
[Asset Pipeline CI 38710307817](https://github.com/dbrckk/zero-to-empire/actions/runs/38710307817)
passed the revised independent stance and gait checks.

The animation review evidence permits an objective, limited comparison.
The metric below is **last→first pixel activity divided by median
adjacent-frame pixel activity** (closer to 1 means a smoother loop seam,
not better artistic quality):

| Original atlas | Before | Contact-rig revision |
|---|---:|---:|
| OP-WALK | 1.6895 | 1.1309 |
| OP-CARRY | 1.5150 | 1.0092 |
| LOG-WALK | 1.7141 | 1.1480 |
| LOG-CARRY | 1.5468 | 1.0400 |
| ENG-WALK | 1.7099 | 1.1530 |
| ENG-CARRY | 1.5584 | 1.0449 |

All six have eight distinct authored poses and remain candidate-only. The
improved seam and transparent margins **do not prove** heel-to-toe ground
contact in actual scrolling gameplay, biomechanical realism, native
Android readability or premium AAA visual acceptance. The vector style
is still flatter than the existing canonical TECH visual standard.

An isolated Android review APK build and emulator capture must be
validated independently before any proposal to replace production
resources. **The canonical strict count is still 219/235**, with 16
assets unapproved pending visual acceptance and native runtime proof.

### Verified native Android review of local contact gait

The exact checked-in v6 planted-foot revision was compiled as an isolated
installable review APK, not as a production promotion:

- [Review APK build 38710545814](https://github.com/dbrckk/zero-to-empire/actions/runs/38710545814):
  **SUCCESS**; imports all 18 locally authored atlases, validates the
  lossless Android runtime raster output, builds the debug APK, runs
  the existing debug tests and Android lint, and checks its
  `com.zerotoempire.game.originalreview` package identity.
- [Android emulator review 38711070775](https://github.com/dbrckk/zero-to-empire/actions/runs/38711070775):
  **SUCCESS**; installs the isolated APK, launches the Compose
  gallery, selects ENGINEER and captures the actual 39/42 dp
  nighttime/daytime character preview. Its screenshot and UI hierarchy
  are available in `local-original-android-emulator-visual-evidence`.
- Candidate bundle:
  [ChatGPT Original Character Candidates 38710288088](https://github.com/dbrckk/zero-to-empire/actions/runs/38710288088),
  containing 18 atlases, 150 editable SVG poses and 18 animation GIFs.

A successful Android launch is real runtime-rendering evidence, **not**
proof that the animation has AAA visual quality or realistic weight
transfer in a scrolling level. No canonical production drawable,
master status or existing game install/save was modified by these
review-only workflows. The strict queue remains **219/235 DONE**.
