# ENG + OP — third Kaggle character batch semantic review

- Producer run: [38186016651](https://github.com/dbrckk/zero-to-empire/actions/runs/38186016651)
- Collector run: [38201816567](https://github.com/dbrckk/zero-to-empire/actions/runs/38201816567)
- Artifact: `kaggle-async-character-batch` in collector run
- Dispatch token: `38185997333`
- Date: 2026-10-12 UTC
- **Strict DONE added: 0.** This is an evidence-only review; no sprites have passed complete manual, runtime and Android checks.

## Assessment by manifest ID

| Manifest ID | Generator outcome | Full-frame semantic review |
|---|---|---|
| CHR-ENG-IDLE | CANDIDATE; technical PASS | **HOLD**: the six-frame full-body IDLE is substantially more visually coherent than previous attempts, with consistent overall outfit and headgear, but cannot be approved until all six ENG actions have matching identity, premium motion, and Android/runtime proof. |
| CHR-ENG-WALK | REJECT | The adjacent silhouette abruptly changes (IoU 0.27). |
| CHR-ENG-WORK | CANDIDATE; technical PASS | **REJECT**: head/face identity changes, pseudo-text "ENG" appears on a blue floating panel, hand/tool interaction is inconsistent, device morphology varies. |
| CHR-ENG-CARRY | REJECT | Identity/silhouette discontinuity (IoU 0.15). |
| CHR-ENG-REPAIR | CANDIDATE; technical PASS | **REJECT**: head/face changes and tools/panels morph between frames; no coherent repair contact point or stable object. |
| CHR-ENG-CELEB | REJECT | Fails meaningful celebration gesture count, 2 of 7 transitions. |
| CHR-OP-IDLE | CANDIDATE, context-only | **REJECT as replacement anchor**: hard-hat/operator identity mostly stable, but baked gray ground shadows are visible in transparent game frames; not a certified same-family IDLE replacement. |
| CHR-OP-WALK | REJECT | Lower-body motion 0.167, below required 0.22. |
| CHR-OP-CARRY | CANDIDATE; technical PASS | **REJECT**: cargo panel/handle geometry mutates, hands/grip alignment changes, face and glasses visibly drift, baked ground shadow remains. Measured alpha-stride changes alone do not imply an animated walk. |
| CHR-OP-REPAIR | REJECT | Frame 5 could not pass after border and detached-artifact retries. |

## Root causes and corrections

The generator creates a text-to-image character anchor but uses stochastic diffusion for every subsequent action pose. Subject geometry can remain technically continuous while the person/props silently change. The older WORK/REPAIR scaffolds drew large standalone consoles to the right of the figure, strongly encouraging floating/morphing devices and fake labels.

Changes introduced following this review:

1. Candidate-only risk metrics independently compare top-of-body **head/helmet color** and middle-of-body **tool/crate color** across frames. Severe discontinuities block the candidate, but passing the image-only metrics never grants semantic approval.
2. WORK and REPAIR seed **small wrist-connected handheld tools**, not detached large consoles.
3. CARRY denoising is reduced to preserve a stable face and crate; leg articulation is kept, and minimum gait motion still applies.
4. An IDLE awaiting review always reserves a GPU slot when generating a coherent family. A failed context-only refresh does not destroy the previous candidate's source evidence.
5. Strict approval is withheld until complete role identity, specific action semantics, motion, provenance, Android integration and runtime checks pass.

The source-specific rejections have been appended to `art/production/generation-rejection-ledger.json`. After this review, the canonical target remains **235**, with **219** strict DONE and **16** not DONE. The next wave is [38201875119](https://github.com/dbrckk/zero-to-empire/actions/runs/38201875119), covering LOG plus selected ENG targets; do not confuse its outputs with this run.

Only the canonical master queue is authoritative for later counts.
