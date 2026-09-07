# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read this file before any new work on this repository and update it at every assistant intervention that changes goals, state, decisions, blockers, or next actions.

## Global continuity rule
- This repository must always keep a recent, concrete record of the latest changes and the next objectives.
- The assistant must update this file whenever it works on the repository and before ending an intervention that materially changes project state.
- Do not rely on chat history as the only source of continuity.
- Apply the same `PROJECT_CONTINUITY.md` convention to every actively worked repository going forward.
- Never mark an objective complete from intent alone: record the commit/run/CI evidence that proves completion.

## Primary objective
Bring **Zero → Empire** to full production completion, with the current immediate art objective being **100% of the canonical final sprite manifest**.

Canonical art sources:
- `docs/art/FINAL_AAA_SPRITE_MANIFEST.md`
- `docs/art/FINAL_AAA_SPRITE_PROGRESS.md`

Locked scope: **235 final deliverables**.

## Non-negotiable sprite completion gate
An asset is not strict `DONE` until it is individually authored/generated, semantically correct, technically clean, transparent where required, committed to the final runtime path, actually referenced/visible in runtime, and validated by green Android CI. Candidate sheets, concept collages, technically valid but semantically wrong generations, or merely integrated files do not increment strict DONE.

## Current handoff — 2026-09-07
### Current execution state
- Strict committed progress ledger: **112 / 235 DONE** until a later strict reconciliation proves a higher number.
- `BLD-03-T2` through `BLD-03-T6` were integrated by run 75 (`e14b6897...`) but still require canonical reconciliation/green-CI proof before silently increasing strict DONE.
- Run 77 (`34102566634`) completed technically and produced 21 building candidates.
- Full-resolution semantic review of run 77 rejected **21 / 21**. Review record: `docs/art/reviews/RUN_77_SEMANTIC_REVIEW.md` (`44d83fbf...`).
- Run-77 rejection reasons: BLD-04 contains people/vehicles/text/ground slab and weak family progression; BLD-06 contains ground/background residue, alpha damage and weak tier growth; BLD-07 T0 is already a late-game multi-storey crane-equipped complex and the family lacks valid starter→ultimate progression.
- No run-77 candidate is promoted. Strict DONE remains unchanged.

### Generator evolution after run 77
- Added `tools/sprites/kaggle_building_family_factory_v11.py` (`2f34a6f1...`).
- Routed `kaggle/github_mass_factory.py` through v11 (`f2ac1945...`).
- v11 adds: stricter T0 ceiling, much stronger no-people/no-vehicles/no-slab prompt contract, lower img2img drift, monotonic per-tier display scaling, anti-ground-slab heuristic, internal-alpha-hole guard, stronger adjacent-tier identity IOU, center-drift limit, and minimum family-growth checks.
- Failed run-77 families 04/06/07 are deprioritized while v11 is proven on other remaining families.

### User-approved wave trigger mechanism
- `.github/workflows/kaggle-mass-sprite-factory.yml` now accepts a push only on `ops/sprite-wave-trigger.txt` in addition to manual `workflow_dispatch` (`a5a651f8...`).
- This preserves the rule that mass GPU generation happens only after explicit user `Go` / `Continue`, while allowing the assistant to launch the approved wave directly.
- `ops/sprite-wave-trigger.txt` was created for **wave 78** (`4750b26a...`).
- GitHub Actions **Kaggle Mass Sprite Factory run 78** id `34116344191` is queued from that trigger and uses the v11 semantic-guard route.

## Immediate next actions — ordered
1. Wait for run 78 to complete; retrieve its QA artifact immediately when available.
2. Inspect every emitted candidate at full resolution, not just the contact sheet.
3. Reject any semantic mismatch, people/vehicles/text/UI, ground slab/background remnant, alpha damage, wrong family identity, starter-tier over-complexity, or non-monotonic family progression.
4. Promote only accepted candidates to final runtime/master paths and wire them into active runtime references.
5. Reconcile `FINAL_AAA_SPRITE_MANIFEST.md` and `FINAL_AAA_SPRITE_PROGRESS.md` with actual promoted state.
6. Verify Android CI and increment strict DONE only on green evidence.
7. On the next explicit user `Go` / `Continue`, update this continuity file and pulse `ops/sprite-wave-trigger.txt` for the next wave if generation is still required.
8. Repeat generate → technical QA → semantic QA → promotion → runtime integration → green CI until **235 / 235 strict DONE**.

## Known unresolved art targets
- Remaining building families/tiers after `BLD-03`, with coherent family identity and unmistakable monotonic T0→T6 growth.
- `TER-07` Expansion energy conduit remains unresolved in the canonical manifest unless superseded by a later accepted promotion.
- Any other TODO/ART/RUNTIME item in the canonical manifest must be resolved through the same strict gate.

## Operating principle
Quality beats nominal throughput. A failed/rejected generation wave is valid QA evidence but is **not progress toward DONE**. Never replace a correct strict counter with an optimistic candidate count.
