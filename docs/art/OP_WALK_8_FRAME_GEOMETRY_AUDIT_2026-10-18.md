# OP WALK — eight-frame source geometry audit (2026-10-18)

Source: `art/incoming/chatgpt-original/src_svg/OP/WALK/{00..07}.svg` on main.
Review only; no semantic approval or runtime promotion.

| Frame | Left stance | Left ankle (x,y) | Right stance | Right ankle (x,y) |
|---:|:---:|---|:---:|---|
| 0 | yes | (115.45,226.00) | no | (131.25,224.54) |
| 1 | yes | (107.26,226.00) | no | (141.46,208.33) |
| 2 | yes | (99.07,226.00) | no | (157.92,207.85) |
| 3 | yes | (90.88,226.00) | no | (168.61,224.01) |
| 4 | no | (84.25,224.54) | yes | (162.45,226.00) |
| 5 | no | (94.46,208.33) | yes | (154.26,226.00) |
| 6 | no | (110.92,207.85) | yes | (146.07,226.00) |
| 7 | no | (121.61,224.01) | yes | (137.88,226.00) |

## Findings
- Each planted half-cycle moves the source ankle **−8.19 px per frame**, at exactly y=226.
- Swing ankles lift to approximately y=208 before returning toward the ground.
- Stance switches from left to right at frame 4; the opposite switch occurs across the loop seam.
- This supports source-space regularity **only**. Foot slide cannot be determined without knowing the actor's world-space translation, frame timing, and scale in the shipping city.
- The source's palette and costume must remain intact. No demonstrated defect warrants replacing the eight existing SVGs.

## Next actionable verification
Capture the actual shipping-city stage at 8 successive animation indices while recording actor translation and scaling. For planted frames calculate `world_ankle_x = actor_world_x + rendered_scale * source_ankle_x` (account for sprite origin/transform). A nearly constant value is expected while planted. Inspect contact shadows and animation seam at day/night 39–42dp. If drift is observed, adjust only the affected motion parameters, regenerate OP WALK, and run existing Android CI + emulator gates. Do not add unit tests or change the strict queue.
