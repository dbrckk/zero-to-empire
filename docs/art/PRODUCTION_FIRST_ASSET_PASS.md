# Production-first asset completion pass

Scope: **235** canonical production items in `art/production/master-asset-queue.json`,
plus already-existing `ONB-00` tracked separately in the 236-item manifest.

## Definition of completion

- **Produced / candidate:** a real generated PNG atlas or runtime asset, with a traceable
  producer run and the existing technical image/sheet QA passed. This is the
  throughput target. It does not imply the character's motion is artistically
  convincing.
- **Strict DONE:** reviewed semantic identity/action, exact Android runtime
  mapping and integration, and applicable green Android CI. This count must
  *never* be incremented just because a candidate was produced.
- **Deferred art warnings:** palette/headgear drift, subtle motion, baked shadow,
  or similar *visual* concerns documented for later polish. Invalid dimensions,
  missing/cropped actors, multiple people, structurally broken atlases and unknown
  blocking risks remain blocking.

## Production policy

The explicitly selected `production-first` Kaggle controlled-character wave
uses lower, still nonzero motion thresholds. The candidate report carries
`acceptance_mode`, `deferred_art_warnings`, `visual_risk`,
`automatic_semantic_approval=false` and producer evidence. The strict policy
is unchanged for other waves.

The current 16 unresolved strict items are character sheets. Four existing
candidates are already awaiting review; regenerate only the 12 rejected sheets
on the new generation epoch. `art/production/autofactory-state.json` and
`art/production/autofactory-summary.md` are the live state, not this historical
snapshot.

`Asset Autofactory 235` is re-enabled on relevant changes to `main`, every
six hours, and via manual dispatch. It coordinates one Kaggle wave at a time,
with four candidate attempts per character generation epoch and a bounded
infrastructure failure budget. A Kaggle quota/authentication failure must be
reported; it must not be counted as a successful asset.

## Acceptance checklist

1. Confirm every canonical target has a validated generated candidate, with a
   real artifact or runtime file and evidence. Target **235/235 produced**, plus
   the existing `ONB-00`.
2. Keep every deferred quality issue in the strict-review backlog; do not delete
   or retroactively rename rejected evidence.
3. Run Android build and visual review before strict runtime promotion.
4. After the production pass, revisit weak gait, work, carry, repair and
   celebration animations in a separate AAA polish phase.

Local smoke checks:

```bash
python -m unittest discover -s tools/sprites/tests -p test_asset_production_policy.py
python -m py_compile tools/sprites/character_acceptance_policy.py \
  tools/sprites/kaggle_character_sheet_factory_v1.py \
  tools/sprites/asset_wave_orchestrator.py tools/sprites/asset_queue_utils.py
```
