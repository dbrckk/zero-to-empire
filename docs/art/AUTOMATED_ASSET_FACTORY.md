# Automated Asset Factory — 235 production target

## Goal

Drive the 235 gameplay-production assets (all canonical sprite deliverables except `ONB-00`) through generation and technical QA with minimal manual intervention.

The factory intentionally keeps **production completion** separate from **strict DONE**.

- Canonical manifest scope: 236
- Autofactory production target: 235
- Excluded from this loop: `ONB-00`
- Trusted strict baseline at creation: 126 / 235
- Remaining strict-review set: 109
  - 75 buildings
  - 24 character sheets
  - 10 historical FX

## Safety contract

The autofactory may automatically:

1. queue generation;
2. run Kaggle/technical producers;
3. retry failed technical generations;
4. move to the next family/role;
5. gather FX runtime evidence;
6. persist run IDs, attempts and review backlog.

It may **not** automatically:

- declare semantic/visual approval;
- promote an unreviewed candidate to strict DONE;
- overwrite the strict ledger merely because a runtime file exists;
- bypass the historical review gate.

## Autonomous order

### Buildings

Whole-family candidate generation is prioritized:

`BLD-04 → BLD-07 → BLD-11 → BLD-12 → BLD-13 → BLD-02 → BLD-03 → BLD-05 → BLD-06 → BLD-08 → BLD-09 → BLD-10`.

Whole-family generation is intentional even when only part of an early family remains unresolved, because tier coherence must be judged against the complete T0→T6 lineage.

### Characters

Roles are produced in this order:

`CHR-OP → CHR-TECH → CHR-LOG → CHR-ENG`.

The Kaggle lane produces at most two sheets per run. The workflow keeps dispatching until the active controlled role queue is exhausted.

### FX

The ten historical FX (`FX-00..08`, `FX-17`) use exact-runtime evidence reconciliation first. A failed semantic review can later requeue individual FX for regeneration.

## Retry behavior

Each unresolved asset has an automatic attempt counter.

At 8 automatic attempts, it becomes `BLOCKED_AUTOMATION_LIMIT` and the factory moves on instead of creating an infinite loop.

## Completion states

`art/production/master-asset-queue.json` is the machine-readable authority for the factory.

Important states:

- `DONE`: already part of the trusted strict baseline.
- `PENDING*`: ready for automated work.
- `DISPATCHED`: producer dispatch recorded.
- `AWAITING_REVIEW`: candidate/evidence exists and needs semantic review.
- `BLOCKED_AUTOMATION_LIMIT`: automation exhausted; manual intervention required.

When all 235 assets are either strict DONE or have reached a review-ready production state, the workflow emits:

`PRODUCTION_235_COMPLETE_REVIEW_BACKLOG`

That does **not** mean 235/235 strict DONE. Strict DONE continues to require the full promotion policy from `AAA_HISTORICAL_PROMOTION_REVIEW.md`.

## Trigger model

`.github/workflows/asset-autofactory.yml` runs:

- after Kaggle Mass Sprite Factory completes;
- after FX Historical Review Evidence completes;
- every 30 minutes as a recovery heartbeat;
- manually via workflow dispatch.

This makes the chain self-resuming after failures, quota delays and GitHub runner interruptions.
