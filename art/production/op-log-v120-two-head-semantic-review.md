# OP/LOG character wave — verified semantic review

- **Source GPU submission:** [38281199147](https://github.com/dbrckk/zero-to-empire/actions/runs/38281199147)
- **Canonical dispatch token:** `38263107266`
- **Collected evidence:** [38281126201](https://github.com/dbrckk/zero-to-empire/actions/runs/38281126201), artifact `kaggle-async-character-batch`
- **Generated files:** 4 of 12 requested candidate atlas files; 8 were rejected by the producer.
- **Technical QA:** all 4 delivered atlases passed resolution, transparency, margins and basic checks.
- **Manual semantic approval:** **0**. Technical pass is not a semantic/runtime/AAA guarantee.
- **Canonical strict total:** 219/235. The next OP/LOG dispatch `38281171130` remains separate.

## Evidence from full 256 × 256 frames

| Manifest ID | Producer outcome | Visual findings / decision |
|---|---|---|
| CHR-OP-IDLE | CANDIDATE, context-only | One identifiable man with the same orange helmet/glasses, but brown/gray cast-floor streaks remain around his boots. Not an approved replacement of the already-strict-DONE legacy IDLE. |
| CHR-OP-WALK | REJECT | `walk-too-static lower-motion=0.170` |
| CHR-OP-WORK | CANDIDATE | **REJECTED_SEMANTIC**. Ten mostly standing poses, with tool/screens changing or disappearing. Frame 7 also changes the sleeve/uniform. There is no fixed workstation or coherent hand-to-tool contact. |
| CHR-OP-CARRY | REJECT | `carry-too-static mean-change=0.109<0.120` |
| CHR-OP-REPAIR | CANDIDATE | **REJECTED_SEMANTIC**. Tools morph or disappear. Frame 7 contains a large unrelated circular prop across the torso, not a stable repair action. |
| CHR-OP-CELEB | REJECT | `celeb-upper-silhouette-jump=0.669>0.450` |
| CHR-LOG-IDLE | CANDIDATE, context-only | **REJECTED as identity reference**. All six frames contain **TWO women in white helmets standing side-by-side**, with their shoulder/torso silhouettes touching. Earlier connected-component and aspect-ratio QA incorrectly passed this. Never promote this image or use it as a single-person anchor. |
| CHR-LOG-WALK | REJECT | `walk-too-static lower-motion=0.156` |
| CHR-LOG-WORK | REJECT | Face, headgear and equipment color/shape discontinuities |
| CHR-LOG-CARRY | REJECT | `carry-too-static mean-change=0.084<0.120` |
| CHR-LOG-REPAIR | REJECT | Face, headgear and equipment color/shape discontinuities |
| CHR-LOG-CELEB | REJECT | `identity/silhouette jump=0.28` |

## Root cause, correction and propagation

The previous isolation test looked for multiple **separate full-body connected components**. Two people touching at their shoulders can form one connected alpha mass, and a sufficiently narrow pair remains under the width-to-height limit. The producer therefore classified a two-woman IDLE as technically valid.

Commit `206d2c18` introduces `idle_distinct_head_clusters` in `tools/sprites/character_semantic_gate.py`. It examines the upper 2%-14% of visible IDLE height and rejects **two sufficiently wide, separated opaque head/helmet clusters observed in two or more frames**, even when the bodies touch. Commit `205b52fd` additionally checks canonical role anchors with the same detector *before* costly GPU frame production; bad seeds are retried using independent seeds, and the approved-source fallback is checked too. The criterion deliberately applies to IDLE only, since raised arms or held props can create false head-like clusters in action frames.

Synthetic regressions cover adjacent/connected two-worker torsos and valid single-person IDLEs. The updated CI run [38281738278](https://github.com/dbrckk/zero-to-empire/actions/runs/38281738278) **succeeded**. All recorded defects are also stored as source-specific `prompt_hint` rows in `art/production/generation-rejection-ledger.json`.

The improvement was committed **after** the current GPU kernel `38281199147` was submitted. It will not retroactively change its producer output. Continue collecting that wave and manually reject any two-person, morphing-prop, frozen-action or inconsistent-identity candidate. **No review, technical gate, or this report can grant strict DONE automatically.**
