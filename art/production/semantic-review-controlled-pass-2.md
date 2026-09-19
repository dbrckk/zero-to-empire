# Semantic review — controlled regeneration pass 2

Date: 2026-09-19
Status: **PARTIAL TECHNICAL SUCCESS / SEMANTIC REJECTION**

## BLD-04 — Tech Company

Verdict: **REJECT T0–T6 as a family**

Pass 2 improved the overall dark-tech visual language, but the required monotonic family evolution is still not satisfied.

Observed problems:
- T0/T1 read as tower-like headquarters;
- T2 collapses into a much smaller squat block;
- T3/T4/T5 change massing rather than clearly evolving the same base structure;
- T6 becomes a narrow spire and does not read as the maximal evolution of T5;
- one shared seed was insufficient to guarantee architectural continuity.

Action:
- generate all seven tiers in **one model call** as a 4×2 family-evolution board;
- crop T0→T6 from that one board;
- technically validate all seven together;
- reject the entire board if any tier fails technical QA;
- keep candidate-only until another semantic review.

## CHR-OP-IDLE

Verdict: **BLOCKED / REJECT**

Single-sheet generation did not consistently produce one full-body character in every required cell.

## CHR-OP-WALK

Verdict: **REJECT**

Although technical QA reported min IoU 0.60, visual inspection still shows major identity drift:
- changing helmet/head shape;
- changing face;
- changing body proportions;
- inconsistent costume details;
- sequence does not represent one stable worker walking.

This demonstrates that geometric IoU is not a sufficient identity-consistency test.

## Character production decision

Automatic character generation is **PAUSED**.

No further Operator/Technician/Logistics/Engineer generation should run until an identity-locked method is available, such as:
- image-conditioned generation using one approved base character,
- pose/control guidance,
- or another deterministic rig/animation workflow.

Free text-to-image generation is not allowed to advance character assets beyond experimental evidence.

## Strict-count effect

No pass-2 asset is promoted to runtime or strict DONE.
Trusted progress remains **125 / 236** and characters remain **0 / 24 strict**.
