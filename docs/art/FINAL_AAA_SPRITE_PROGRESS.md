# FINAL AAA SPRITE PROGRESS — Zero → Empire

Live companion ledger for `FINAL_AAA_SPRITE_MANIFEST.md`. The manifest remains the canonical 235-item scope. Candidate art is never confused with DONE runtime assets.

## Official progress
- DONE: **106 / 235**
- ART VALIDATED: **121 / 235**
- RUNTIME INTEGRATED: **121 / 235**
- Generated candidates accepted as DONE: **106**
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
2. Continue coherent family/tier building production; promote only families that preserve architectural identity and visibly satisfy the required T0 → T6 scale/complexity progression.
3. Regenerate the two rejected machines (`MCH-05-1`, `MCH-07-0`) and four rejected terrain connectors (`TER-05`, `TER-07`, `TER-09`, `TER-10`).
4. Continue characters and FX only through the same generate → technical QA → semantic QA → runtime → green-CI gate.

## Reviewed FLUX run 51 — 23 machines DONE
Run-51 produced 29 technically valid candidates. Semantic QA accepted 23 machine masters and rejected `MCH-03-0` (baked lettering), `MCH-05-1` (wrong battery-carousel read), `MCH-11-1` (detached underside sphere), `MCH-12-0` (missing required containment-ring identity), both terrain candidates (camera/connector mismatch; TER-01 also has a baked road marking), while `MCH-07-0` was not emitted as a technically valid candidate. The 23 accepted machines are integrated into the era-specific active city runtime layer. Android CI run `34047735544` on descendant commit `7ec8e75e57ba34c45a32f474d86ffb93b3230e30` completed successfully with those unchanged runtime assets present, so all 23 are strict DONE.

## Reviewed FLUX run 52 — 13 assets DONE
Semantic QA accepted `MCH-03-0`, `MCH-11-1`, `MCH-12-0` plus terrain `TER-00`, `TER-01`, `TER-02`, `TER-03`, `TER-04`, `TER-06`, `TER-08`, `TER-11`, `TER-12`, `TER-13`. Rejected: `MCH-05-1` (wrong carousel read with detached dark base), `MCH-07-0` (crane-like loose suspended composition instead of a compact gantry), `TER-05` (baked arrows), `TER-07` (open frame rather than a complete square tile), `TER-09` (missing twin cyan maglev guide identity), `TER-10` (bridge-like structure rather than square service-deck tile), and `VEH-16` (still reads as a conventional car with wheel-like side volumes). The 13 accepted assets are integrated and visible in the active city stage. Android CI run `34047735544` on descendant commit `7ec8e75e57ba34c45a32f474d86ffb93b3230e30` completed successfully with those unchanged runtime assets present, so all 13 are strict DONE.

## Reviewed FLUX run 56 — strict semantic rejection
The anchored-family generator produced 26 technically valid building candidates for `BLD-03-T2` through `BLD-06-T6`. Full-resolution semantic review rejects all four families from promotion. `BLD-04` has residual dark background rectangles. `BLD-03` preserves a recognizable low square assembly-hub identity but T2 through T6 remain near-duplicate low blocks and never reach the required district-scale/megastructure verticality. `BLD-05` preserves a strong furnace-tower identity but all seven tiers are effectively the same tower with small pipe/roof variations rather than a controlled starter → ultimate progression. `BLD-06` similarly remains a near-static white processing plant across T0 through T6 with insufficient footprint, machinery and verticality growth. None of run-56 is promoted.

## Reviewed FLUX run 57 — strict semantic rejection
Run-57 produced 21 technically valid 2048×2048 transparent candidates for `BLD-04`, `BLD-07` and `BLD-09`, all with safe outer margins and no edge-alpha contamination. Full-resolution semantic review rejects all three families from promotion. `BLD-04` is visually clean but the seven tiers remain near-duplicate warehouse variants and do not deliver the required starter → industrial → district-scale → megastructure progression. `BLD-07-T0` already reads as a large multi-storey crane-equipped industrial complex, violating the required low-verticality starter tier; subsequent tiers mostly reshuffle roof cranes rather than adding a controlled production hierarchy. `BLD-09` preserves a recognizable energy-building theme but tier mass/verticality is non-monotonic, repeatedly collapsing from taller tower forms back to low blocks before rising again at T6. None of run-57 is promoted. Sequential image-conditioned tier evolution is therefore preferred for the next building attempt.

## FLUX run 59 — generator QA rejection
The first sequential img2img attempt (`building-family-flux-v5-sequential-img2img`) completed rendering work but emitted zero fresh candidates. Automatic family QA correctly rejected families with insufficient tier growth; one intermediate `BLD-07` render was also rejected for a non-uniform/non-black border. This failure is treated as useful QA evidence rather than art progress: no candidate is promoted and the strict DONE counter remains unchanged. The next iteration must increase controlled additive growth while preserving family anchors and isolation.

## Reviewed FLUX run 63 — strict semantic rejection
Run-63 emitted 21 technically passing candidates for `BLD-11`, `BLD-12` and `BLD-13`, but full-resolution review rejects the complete batch. `BLD-11-T2` through `T5` retain a large circular/rectangular backdrop field instead of a clean isolated sprite; `BLD-11-T4` also contains large baked lettering and unrelated flag/worker props. `BLD-12` does not preserve a monotonic apex progression, and `BLD-12-T6` contains baked `TIER 6` text plus a large ground/background remnant. `BLD-13` remains structurally near-static across tiers, includes detached decorative particles at `T4`, and `BLD-13-T6` contains multiple baked pseudo-word labels and small vehicle/worker-like props. None of run-63 is promoted. Automatic QA must reject backdrop-like high-coverage masks, baked-text contamination and non-monotonic family evolution before promotion.
