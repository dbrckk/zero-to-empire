# Semantic review — controlled regeneration pass 1

Date: 2026-09-19
Reviewer: ChatGPT visual inspection of GitHub Actions evidence artifacts
Status: **REJECTED — regeneration required**

## BLD-04 Tech Company T0–T6

Verdict: **REJECT ALL 7**

Reason:
- family identity is not preserved across tiers;
- scale/footprint/verticality are non-monotonic;
- T0/T1 read as towers, T2/T3 shrink to unrelated blocks, T4/T5 flatten into platform-like forms, T6 changes massing again;
- the set therefore fails the required same-family T0→T6 evolution even though each image passed technical alpha/padding QA.

Action:
- regenerate using the canonical **Tech Company** identity from runtime art;
- use one shared family seed across all tiers;
- enforce explicit tier language for footprint, verticality and subsystem escalation;
- keep outputs candidate-only pending another full-family visual review.

## CHR-OP controlled wave

### CHR-OP-IDLE
Verdict: **REJECT**

Identity changes across frames: face, clothing, body proportions and facing direction are not stable enough for one character animation.

### CHR-OP-WALK
Verdict: **REJECT**

Identity and accessories drift across frames. Props appear/disappear, so the sequence does not read as one continuous walking worker.

### CHR-OP-WORK
Verdict: **REJECT**

Identity drift is severe and one frame contains two people. This is an immediate semantic rejection.

### CHR-OP-CARRY
Verdict: **REJECT**

The worker and carried object change across frames; the sequence is not a coherent carry cycle.

Action for all four:
- stop generating frames as independent image calls;
- generate each action as one 4×4 atlas in a single model call;
- slice cells after generation and retain existing pivot/coverage/IoU QA;
- keep results candidate-only until visual identity continuity is reviewed.

## Strict-count effect

No asset from this pass is promoted to runtime or strict DONE.
Trusted progress remains **125 / 236**, with characters still **0 / 24 strict**.
