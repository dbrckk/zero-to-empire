# FINAL AAA SPRITE PROGRESS — Zero → Empire

Live companion ledger for `FINAL_AAA_SPRITE_MANIFEST.md`. The manifest remains the canonical 235-item scope. This file is updated during generation so candidate art cannot be confused with DONE runtime assets.

## Official progress
- DONE: **18 / 235**
- ART VALIDATED: **22 / 235**
- RUNTIME INTEGRATED: **22 / 235**
- Generated candidates accepted as DONE: **18**
- Rule: only runtime-integrated, individually clean/transparent, manifest-matching assets with green Android CI increment DONE.

## Accepted assets
| Asset | Master | Isolation | Runtime | State |
|---|---|---|---|---|
| `BLD-00-T0 — Street Stand T0` | 2048×2048 RGBA | PASS — 69.7% transparent; 100.0% dominant | `zte_business_00_t0_final.webp`, referenced | DONE; Android CI green |
| `BLD-00-T1 — Street Stand T1` | 2048×2048 RGBA | PASS | `zte_business_00_t1_final.webp`, referenced | DONE; Android CI green |
| `BLD-00-T2 — Street Stand T2` | 2048×2048 RGBA | PASS | `zte_business_00_t2_final.webp`, referenced | DONE; Android CI green |
| `BLD-00-T3 — Street Stand T3` | 2048×2048 RGBA | PASS | `zte_business_00_t3_final.webp`, referenced | DONE; Android CI green |
| `BLD-00-T4 — Street Stand T4` | 2048×2048 RGBA | PASS | `zte_business_00_t4_final.webp`, referenced | DONE; Android CI green |
| `BLD-00-T5 — Street Stand T5` | 2048×2048 RGBA | PASS | `zte_business_00_t5_final.webp`, referenced | DONE; Android CI green |
| `BLD-00-T6 — Street Stand T6` | 2048×2048 RGBA | PASS | `zte_business_00_t6_final.webp`, referenced | DONE; Android CI green |
| `BLD-01-T0 — Corner Shop T0` | 2048×2048 RGBA | PASS | `zte_business_01_t0_final.webp`, referenced | DONE; Android CI green |
| `BLD-01-T1 — Corner Shop T1` | 2048×2048 RGBA | PASS | `zte_business_01_t1_final.webp`, referenced | DONE; Android CI green |
| `BLD-01-T2 — Corner Shop T2` | 2048×2048 RGBA | PASS | `zte_business_01_t2_final.webp`, referenced | DONE; Android CI green |
| `BLD-01-T3 — Corner Shop T3` | 2048×2048 RGBA | PASS | `zte_business_01_t3_final.webp`, referenced | DONE; Android CI green |
| `BLD-01-T4 — Corner Shop T4` | 2048×2048 RGBA | PASS | `zte_business_01_t4_final.webp`, referenced | DONE; Android CI green |
| `BLD-01-T5 — Corner Shop T5` | 2048×2048 RGBA | PASS | `zte_business_01_t5_final.webp`, referenced | DONE; Android CI green |
| `BLD-01-T6 — Corner Shop T6` | 2048×2048 RGBA | PASS | `zte_business_01_t6_final.webp`, referenced | DONE; Android CI green |
| `BLD-02-T0 — Furnace Stall T0` | 2048×2048 RGBA | PASS | `zte_business_02_t0_final.webp`, referenced | DONE; Android CI green |
| `BLD-02-T1 — Furnace Stall T1` | 2048×2048 RGBA | PASS | `zte_business_02_t1_final.webp`, referenced | DONE; Android CI green |
| `BLD-02-T2 — Furnace Stall T2` | 2048×2048 RGBA | PASS | `zte_business_02_t2_final.webp`, referenced | DONE; Android CI green |
| `BLD-02-T3 — Furnace Stall T3` | 2048×2048 RGBA | PASS | `zte_business_02_t3_final.webp`, referenced | DONE; Android CI green |
| `BLD-02-T4 — Furnace Stall T4` | 2048×2048 RGBA | PASS | `zte_business_02_t4_final.webp`, referenced | RUNTIME; CI pending |
| `BLD-02-T5 — Furnace Stall T5` | 2048×2048 RGBA | PASS | `zte_business_02_t5_final.webp`, referenced | RUNTIME; CI pending |
| `BLD-02-T6 — Furnace Stall T6` | 2048×2048 RGBA | PASS | `zte_business_02_t6_final.webp`, referenced | RUNTIME; CI pending |
| `BLD-03-T0 — Assembly Hub T0` | 2048×2048 RGBA | PASS | `zte_business_03_t0_final.webp`, referenced | RUNTIME; CI pending |

## Current generated candidates
| Candidate | Intended manifest item | State | Reason not DONE |
|---|---|---|---|
| Street Stand render | BLD-00-T0 | REJECTED | Background/vignette and baked sign/icon details; not clean transparent final runtime asset. |
| Corner Shop render | BLD-01-T0 | REJECTED | Background plus baked readable SHOP/OPEN/24-7/promo text. |
| Furnace render | BLD-02-T0 | REJECTED | Background/vignette and baked signage; not transparent final runtime asset. |
| Clinic render | Unmapped | REJECTED | Does not map to a locked manifest building and contains baked text/signage. |
| Tavern render | Unmapped | REJECTED | Does not map to locked Foundry target; background and baked TAVERN signage. |
| Castle render | Unmapped | REJECTED | Does not map to locked current target; background. |
| Police HQ render | Unmapped | REJECTED | Baked readable text/logos and background. |
| Farm render | Unmapped | REJECTED | Baked FARM signage and background. |
| Fire Station render | Unmapped | REJECTED | Baked readable text/logos and background. |

## Next production target
`BLD-03-T1 — Assembly Hub T1`: generate the reinforced assembly workshop with dedicated powered tooling and stronger organization.
