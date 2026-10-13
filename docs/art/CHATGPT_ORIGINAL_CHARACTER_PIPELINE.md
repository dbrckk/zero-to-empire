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
