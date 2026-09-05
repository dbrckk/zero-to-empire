# FINAL AAA SPRITE PROGRESS — Zero → Empire

Live companion ledger for `FINAL_AAA_SPRITE_MANIFEST.md`. The manifest remains the canonical 235-item scope. Candidate art is never confused with DONE runtime assets.

## Official progress
- DONE: **46 / 235**
- ART VALIDATED: **61 / 235**
- RUNTIME INTEGRATED: **61 / 235**
- Generated candidates accepted as DONE: **46**
- Rule: only runtime-integrated, individually clean/transparent, manifest-matching assets with green Android CI increment DONE.

## DONE baseline
- `BLD-00-T0` through `BLD-02-T3`: **18 buildings**, individually validated, referenced, visible and Android CI green.

## Reviewed FLUX batch — DONE
Run-20 promotion retained only the **28 semantically approved** isolated masters. Promotion revalidated all 28, generated Android WebP runtime assets, and committed both master and runtime copies. They are referenced by `WorldTrafficArt.kt`, rendered as physical city-stage scenery by `AscendantCityStage`, and Android CI run `33981695482` completed green (full tests, release lint, APK and bundle builds).

### Vehicles — 10 DONE
`VEH-00`, `VEH-01`, `VEH-02`, `VEH-03`, `VEH-04`, `VEH-05`, `VEH-06`, `VEH-07`, `VEH-08`, `VEH-10`.

Runtime files:
`zte_vehicle_00_final.webp`, `zte_vehicle_01_final.webp`, `zte_vehicle_02_final.webp`, `zte_vehicle_03_final.webp`, `zte_vehicle_04_final.webp`, `zte_vehicle_05_final.webp`, `zte_vehicle_06_final.webp`, `zte_vehicle_07_final.webp`, `zte_vehicle_08_final.webp`, `zte_vehicle_10_final.webp`.

### Props — 18 DONE
`PRP-02-B`, `PRP-04-A`, `PRP-05-B`, `PRP-06-A`, `PRP-06-B`, `PRP-07-A`, `PRP-07-B`, `PRP-08-A`, `PRP-08-B`, `PRP-09-A`, `PRP-09-B`, `PRP-10-A`, `PRP-10-B`, `PRP-11-A`, `PRP-11-B`, `PRP-12-A`, `PRP-12-B`, `PRP-13-A`.

Runtime files use the corresponding `zte_prop_*_final.webp` names and are placed off the cargo avenue with depth-scaled world pivots.

## Existing ART/RUNTIME assets not yet promoted to DONE
The following previously validated assets remain outside the DONE count until their own strict reconciliation is complete:
- `BLD-02-T4`, `BLD-02-T5`, `BLD-02-T6`, `BLD-03-T0`, `BLD-03-T1`.
- `FX-08` through `FX-17`.

## Rejected candidates
Rejected concept sheets, baked-background/signage renders, non-alpha renders, semantically wrong terrain, and the two rejected FLUX run-20 candidates remain excluded from all completion counts.

## Next production targets
1. Generate the missing vehicle set: `VEH-09`, `VEH-11` through `VEH-17`.
2. Generate missing props: `PRP-00-A/B`, `PRP-01-A/B`, `PRP-02-A`, `PRP-03-A/B`, `PRP-04-B`, `PRP-05-A`, `PRP-13-B`.
3. Continue machines, characters, Power Core and remaining buildings only through the same generate → technical QA → semantic QA → runtime → green-CI gate.
