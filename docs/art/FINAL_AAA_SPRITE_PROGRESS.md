# FINAL AAA SPRITE PROGRESS — Zero → Empire

Live companion ledger for `FINAL_AAA_SPRITE_MANIFEST.md`. The manifest remains the canonical 235-item scope. This file is updated during generation so candidate art cannot be confused with DONE runtime assets.

## Official progress
- DONE: **4 / 235**
- ART VALIDATED: **8 / 235**
- RUNTIME INTEGRATED: **8 / 235**
- Generated candidates accepted as DONE: **4**
- Rule: only runtime-integrated, individually clean/transparent, manifest-matching assets with green Android CI increment DONE.

## Accepted assets
| Asset | Master | Isolation | Runtime | State |
|---|---|---|---|---|
| `BLD-00-T0 — Street Stand T0` | 2048×2048 RGBA | PASS — 69.7% transparent; 100.0% dominant | `zte_business_00_t0_final.webp`, referenced | DONE; Android CI green |
| `BLD-00-T1 — Street Stand T1` | 2048×2048 RGBA | PASS | `zte_business_00_t1_final.webp`, referenced | DONE; Android CI green |
| `BLD-00-T2 — Street Stand T2` | 2048×2048 RGBA | PASS | `zte_business_00_t2_final.webp`, referenced | DONE; Android CI green |
| `BLD-00-T3 — Street Stand T3` | 2048×2048 RGBA | PASS | `zte_business_00_t3_final.webp`, referenced | DONE; Android CI green |
| `BLD-00-T4 — Street Stand T4` | 2048×2048 RGBA | PASS | `zte_business_00_t4_final.webp`, referenced | RUNTIME; CI pending |
| `BLD-00-T5 — Street Stand T5` | 2048×2048 RGBA | PASS | `zte_business_00_t5_final.webp`, referenced | RUNTIME; CI pending |
| `BLD-00-T6 — Street Stand T6` | 2048×2048 RGBA | PASS | `zte_business_00_t6_final.webp`, referenced | RUNTIME; CI pending |
| `BLD-01-T0 — Corner Shop T0` | 2048×2048 RGBA | PASS | `zte_business_01_t0_final.webp`, referenced | RUNTIME; CI pending |

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
`BLD-01-T1 — Corner Shop T1`: generate the reinforced shop with dedicated finishing machinery, improved organization and stronger silhouette.
