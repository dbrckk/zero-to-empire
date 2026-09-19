# Automated Asset Factory

Goal: drive the canonical 236-sprite scope toward **235 strict DONE** with minimal manual intervention without converting technical validity into fake semantic approval.

## Safety invariants

1. `FINAL_AAA_SPRITE_PROGRESS.md` is the trusted strict count while historical manifest DONE flags are under reconciliation.
2. Generation never means DONE.
3. BLD/CHR/MCH/FX require semantic approval before runtime promotion.
4. Runtime promotion requires technical QA, exact runtime mapping, visible gameplay integration and green Android CI.
5. The factory stops at 235/236 by design, leaving one manual safety slot.
6. Per-asset retry budgets prevent infinite paid/free compute loops.
7. Existing controlled building/character queues take precedence over opening new work.

## Automation loop

Hourly or manual dispatch:

`plan -> select lane/family -> mark IN_PROGRESS -> dispatch specialized generator -> QA/review evidence -> reconcile -> next wave`

The orchestrator intentionally refuses to trust the manifest's historical DONE labels as strict evidence. The queue begins in `RECONCILE` and is normalized as strict per-asset evidence is made machine-readable.

## Lanes

- `building-family`: Kaggle sequential family generation, seven tiers together.
- `character-atlas`: role/action atlas generation.
- `terrain`: dedicated terrain pipeline.
- `fx`: FX-specific production.
- `static`: CORE/VEH/PRP; review-safe static provider required before automatic dispatch.
- `machine`: animation-aware generator required before automatic dispatch.

## Completion rule

The workflow may automate generation, retries, QA, evidence and scheduling. It must not automatically invent semantic approval. Strict DONE remains gated by reviewed evidence + runtime integration + green Android CI.
