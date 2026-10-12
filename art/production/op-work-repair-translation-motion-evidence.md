# WORK / REPAIR movement-translation false positives — GPU evidence

**Reviewed on 2026-10-12 UTC.** Evidence source: `Kaggle Async Character Collector`
run [38281126201](https://github.com/dbrckk/zero-to-empire/actions/runs/38281126201),
archive `kaggle-async-character-batch`. Exact retrospective reviewer run:
[38285461131](https://github.com/dbrckk/zero-to-empire/actions/runs/38285461131),
archive `character-single-subject-evidence-38281126201`.

Both files initially passed size/alpha technical checks. A human visual review
rejected the animations: the same standing worker shifts position while hands,
tools and forearms fail to perform a coherent action. Raw foreground alpha
motion greatly overstates true pose articulation.

| Candidate | Mean raw alpha change | Mean pose change after head registration | Pose motion retained | Head horizontal excursion | Decision |
|---|---:|---:|---:|---:|---|
| `CHR-OP-WORK` | 0.3318 | 0.1087 | 0.3278 | 26 px | REJECT, translation-dominated |
| `CHR-OP-REPAIR` | 0.3813 | 0.1246 | 0.3269 | 23 px | REJECT, translation-dominated |

## Corrected gate

`tools/sprites/character_semantic_gate.py` registers the upper opaque head
centroid of each 256px frame before measuring residual pose motion. For WORK
and REPAIR only, image risk `ACTION_TRANSLATION_DOMINATES_POSE_RISK` blocks
when raw alpha motion is at least 0.15, head excursion at least 12px, and
registered pose motion retains less than 43% of raw motion. This catches a
moving *camera/actor position* masquerading as a moving *arm/tool*.

`tools/sprites/verify_character_action_candidates.py` independently
reruns the action risk screening on downloaded producer PNGs, even if the GPU
kernel ran an older generator version. It updates the derived GitHub technical
QA report **before** the canonical collector reconciles candidate statuses.
It does not edit source PNGs, mark assets approved, or increase strict DONE.
Deterministic synthetic regressions and a real GPU evidence workflow both
verify this behavior.

## What this does not solve

Passing registered-motion QA does not establish coherent hands, tools,
object physics, costume continuity or premium animation. New generator
candidates still require full-frame visual inspection, identity continuity,
Android runtime conversion, audit and build/lint checks. High stochastic
pose-to-pose redrawing remains the underlying creative quality limitation.

The verified count at this review was **219/235 strict DONE**. This QA
improvement intentionally does **not** promote any animation.
