# FINAL AAA SPRITE PROGRESS — Zero → Empire

Live companion ledger for `FINAL_AAA_SPRITE_MANIFEST.md`. The manifest remains the canonical 235-item scope. Candidate art is never confused with DONE runtime assets.

## Official progress
- DONE: **70 / 235**
- ART VALIDATED: **121 / 235**
- RUNTIME INTEGRATED: **121 / 235**
- Generated candidates accepted as DONE: **70**
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

## Reviewed FLUX run 25 — 16 DONE
Run-25 semantic review accepted 16 assets. Eight missing props plus `VEH-17` are referenced in the active city stage and Android CI run `33997464241` completed successfully, so those nine are strict DONE. `CORE-T0` through `CORE-T6` are tier-aware runtime sprites in `AscendantCorePlaza`; Android CI run `34007328616` for commit `0aad3c58190c9650f278cbc7c67782baff1d3581` completed successfully, so all seven are strict DONE.

### New strict DONE
`PRP-00-A`, `PRP-00-B`, `PRP-01-A`, `PRP-01-B`, `PRP-02-A`, `PRP-03-A`, `PRP-03-B`, `PRP-04-B`, `VEH-17`.

### Power Core — 7 DONE
`CORE-T0`, `CORE-T1`, `CORE-T2`, `CORE-T3`, `CORE-T4`, `CORE-T5`, `CORE-T6`.

## Reviewed FLUX run 29 — 1 DONE
The reviewed `PRP-05-A` replacement is referenced by `WorldTrafficArt.kt` in the active city stage. Android CI run `34010813072` for commit `e9b301f2a79d3451dbacb8c7a3e754889ea899ad` completed successfully, so `PRP-05-A` is strict DONE. The rejected `VEH-09` runtime was removed and remains TODO.

## Reviewed FLUX run 37 — 1 DONE
`VEH-09` passed technical QA and semantic review as a wheel-less enclosed maglev freight capsule, was integrated into `WorldTrafficArt.kt`, and the Android runtime build completed successfully. It is strict DONE. `VEH-16` from the same run was rejected because it remained a conventional wheeled automobile.

## Existing ART/RUNTIME assets not yet promoted to DONE
The following previously validated assets remain outside the DONE count until their own strict reconciliation is complete:
- `BLD-02-T4`, `BLD-02-T5`, `BLD-02-T6`, `BLD-03-T0`, `BLD-03-T1`.
- `FX-08` through `FX-17`.

## Rejected candidates
Technically valid but semantically wrong candidates remain excluded. This includes generic/non-progressive building renders, Power Core renders that omit their tier-defining mechanisms, `VEH-16` renders that still read as wheeled cars, `VEH-17` single-drone renders instead of a swarm, and earlier rejected `VEH-09` concepts superseded by the valid run-37 replacement. `PRP-13-B` was rejected in run 20 but replaced by a valid run-22 generation and is now DONE.

## Next production targets
1. Regenerate the remaining vehicle target with stricter semantics: `VEH-16`.
2. Rework building generation around coherent family/tier evolution; do not accept generic unrelated buildings.
3. Continue machines, characters, terrain and FX only through the same generate → technical QA → semantic QA → runtime → green-CI gate.

## Reviewed FLUX run 51 — 23 machines awaiting green CI
Run-51 produced 29 technically valid candidates. Semantic QA accepted 23 machine masters and rejected `MCH-03-0` (baked lettering), `MCH-05-1` (wrong battery-carousel read), `MCH-11-1` (detached underside sphere), `MCH-12-0` (missing required containment-ring identity), both terrain candidates (camera/connector mismatch; TER-01 also has a baked road marking), while `MCH-07-0` was not emitted as a technically valid candidate. The 23 accepted machines are integrated into the era-specific active city runtime layer and remain RUNTIME until Android CI is green.

## Reviewed FLUX run 52 — 13 assets awaiting green CI
Semantic QA accepted `MCH-03-0`, `MCH-11-1`, `MCH-12-0` plus terrain `TER-00`, `TER-01`, `TER-02`, `TER-03`, `TER-04`, `TER-06`, `TER-08`, `TER-11`, `TER-12`, `TER-13`. Rejected: `MCH-05-1` (wrong carousel read with detached dark base), `MCH-07-0` (crane-like loose suspended composition instead of a compact gantry), `TER-05` (baked arrows), `TER-07` (open frame rather than a complete square tile), `TER-09` (missing twin cyan maglev guide identity), `TER-10` (bridge-like structure rather than square service-deck tile), and `VEH-16` (still reads as a conventional car with wheel-like side volumes). Accepted assets are integrated and remain RUNTIME until Android CI is green.
