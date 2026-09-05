# FINAL AAA SPRITE PROGRESS — Zero → Empire

Live companion ledger for `FINAL_AAA_SPRITE_MANIFEST.md`. The manifest remains the canonical 235-item scope. Candidate art is never confused with DONE runtime assets.

## Official progress
- DONE: **52 / 235**
- ART VALIDATED: **67 / 235**
- RUNTIME INTEGRATED: **67 / 235**
- Generated candidates accepted as DONE: **52**
- Rule: only runtime-integrated, individually clean/transparent, manifest-matching assets with green Android CI increment DONE.

## DONE baseline
- `BLD-00-T0` through `BLD-02-T3`: **18 buildings**, individually validated, referenced, visible and Android CI green.

## Reviewed FLUX run 20 — DONE
Run-20 promotion retained only the **28 semantically approved** isolated masters. Promotion revalidated all 28, generated Android WebP runtime assets, committed master/runtime copies, and integrated them into the active city stage. Android CI completed green.

### Vehicles — 10 DONE
`VEH-00`, `VEH-01`, `VEH-02`, `VEH-03`, `VEH-04`, `VEH-05`, `VEH-06`, `VEH-07`, `VEH-08`, `VEH-10`.

### Props — 18 DONE
`PRP-02-B`, `PRP-04-A`, `PRP-05-B`, `PRP-06-A`, `PRP-06-B`, `PRP-07-A`, `PRP-07-B`, `PRP-08-A`, `PRP-08-B`, `PRP-09-A`, `PRP-09-B`, `PRP-10-A`, `PRP-10-B`, `PRP-11-A`, `PRP-11-B`, `PRP-12-A`, `PRP-12-B`, `PRP-13-A`.

## Reviewed FLUX run 22 — DONE
Run-22 semantic review accepted **6** replacements/new assets: `PRP-13-B` and `VEH-11` through `VEH-15`. The promotion workflow revalidated the exact approved files, generated optimized runtime WebP assets and committed them. `WorldTrafficArt.kt` references all six in the active `AscendantCityStage`; Android CI run `33989987865` for commit `b464ac22f904e5faebd8773601a317ab9890dd1a` completed successfully.

### Vehicles — 5 DONE
`VEH-11`, `VEH-12`, `VEH-13`, `VEH-14`, `VEH-15`.

### Props — 1 DONE
`PRP-13-B`.

## Existing ART/RUNTIME assets not yet promoted to DONE
The following previously validated assets remain outside the DONE count until their own strict reconciliation is complete:
- `BLD-02-T4`, `BLD-02-T5`, `BLD-02-T6`, `BLD-03-T0`, `BLD-03-T1`.
- `FX-08` through `FX-17`.

## Rejected candidates
Technically valid but semantically wrong candidates remain excluded. This includes generic/non-progressive building renders, Power Core renders that omit their tier-defining mechanisms, `VEH-16` renders that still read as wheeled cars, `VEH-17` single-drone renders instead of a swarm, and the rejected `VEH-09` concept. `PRP-13-B` was rejected in run 20 but replaced by a valid run-22 generation and is now DONE.

## Next production targets
1. Regenerate the remaining vehicle set with stricter semantics: `VEH-09`, `VEH-16`, `VEH-17`.
2. Regenerate missing props regardless of stale unapproved candidate files: `PRP-00-A/B`, `PRP-01-A/B`, `PRP-02-A`, `PRP-03-A/B`, `PRP-04-B`, `PRP-05-A`.
3. Regenerate Power Core tiers with explicit tier-defining geometry before any promotion.
4. Rework building generation around coherent family/tier evolution; do not accept generic unrelated buildings.
5. Continue machines, characters, terrain and FX only through the same generate → technical QA → semantic QA → runtime → green-CI gate.
