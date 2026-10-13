# ChatGPT original character candidates — 13 October 2026

These graphics were **created in this ChatGPT conversation** from an original,
deterministic role rig, then committed to this repository. Do not confuse their
creation with strict visual approval, Android runtime integration, or release.

## Location and provenance

- Source: [render_chatgpt_originals.py](../../../tools/sprites/render_chatgpt_originals.py)
- Candidate atlases: [candidates/](candidates/)
- Per-frame editable original SVG art: [src_svg/](src_svg/) — **150 SVG files**
- Animated phone previews: [previews/](previews/) — **18 GIFs**
- First-frame comparison: [original-review-contact-sheet.png](original-review-contact-sheet.png)
- Per-action motion evidence: [animation-review.json](animation-review.json)
- Machine-readable list: [creation-manifest.json](creation-manifest.json)
- Technical geometry report: [candidate-qa.json](candidate-qa.json)
- Creation workflow: [ChatGPT Original Character Candidates](../../../.github/workflows/art-chatgpt-original-candidates.yml)
- Read-only canonical technical review: [Review ChatGPT Original Character Pack](../../../.github/workflows/review-chatgpt-original-pack.yml)
- Full first-party workflow: [Documentation](../../../docs/art/CHATGPT_ORIGINAL_CHARACTER_PIPELINE.md)

There are **18 atlas sheets (1024×1024 RGBA)**, one sheet per action and role
(OP, LOG, ENG). Each contains **6–10 frames at 256×256**, on a 4-column atlas.
The initial strict backlog had **16 unresolved targets**; two additional OP/LOG
IDLE sheets are *context-only* role references. Generated assets are under
`art/incoming`, intentionally outside shipping Android resources.

Source and PNG files are owned by **this repository**; Kaggle/Pollinations
workers are optional external producers and should never become the sole
source of original art, acceptance evidence, or approved runtime files.

## Local-first requirement for every unfinished asset

All 16 unfinished manifest assets must be created and maintained in this repository using the committed `tools/sprites/render_chatgpt_originals.py` source and the editable per-frame SVG files. The 18 local atlases, including two context IDLE anchors, are the canonical **creation candidates**. External GPU outputs may be compared as references, but they must not displace locally authored source or become the only reproducible candidate. Any future role/action added to the strict backlog must have a local SVG/PNG candidate and mobile animation preview before it can be considered for review. This requirement does not bypass visual, semantic, Android or release checks.

## How to reproduce

From repository root with Python 3.12:

```bash
python -m pip install Pillow==11.3.0 CairoSVG==2.7.1
python tools/sprites/render_chatgpt_originals.py --output-dir art/incoming/chatgpt-original --save-svg
python tools/sprites/render_original_character_previews.py --output-dir art/incoming/chatgpt-original
```

The CI checks that every currently unresolved character manifest ID has an
on-repository candidate and that the atlas geometry, alpha and frame counts
are valid. This is **not** an automatic-artistic-quality approval.

## Known quality gaps

The bespoke vector style resolves many prior stochastic-identity and
morphing-object failures. However it is **not yet premium AAA game art**:

- WORK and REPAIR remain visually simple, with hand-held props requiring
  improved contact/readability and richer material effects.
- WALK and CARRY are readable gait loops, but need motion polish and an actual
  Android animation/runtime playback test.
- Character appearance should be compared with the existing game's 219
  approved assets for art-direction coherence.
- Frame opacity, full-body framing and repeated colors do not prove game feel.

No entry may become strict DONE until approved semantic review, matching
role-family identity, exact artifact provenance, correct runtime conversion,
and Android validation have passed. No historical `strict_status` was changed
when these candidates were committed.
