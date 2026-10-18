# Manual visual semantic review — Android evidence, 18 October 2026

Source: [Android emulator run 39147290254](https://github.com/dbrckk/zero-to-empire/actions/runs/39147290254) (24 screenshots `atlas-*.png`, 8 stepped OP WALK frames, separate debug package). The screenshot gallery was **actually retrieved and inspected**, not inferred from CI exit status.

## 24 screenshot inspection

The 4×6 role/action screenshot grid was inspected at cropped, enlarged scale for both **39dp daytime** and **42dp nighttime**. The operator, logistics and engineer identities are visually coherent across actions; full bodies remain inside the preview region. The fourth technician role is a context/reference role and is not part of the 16 strict pending targets.

| Pending action | Operator | Logistics | Engineer | What the screenshot proves |
| --- | --- | --- | --- | --- |
| IDLE | already strict DONE | already strict DONE | visible; pending | full-body role anchor |
| WALK | visible, 8-frame sequence separately inspected | visible | visible | walk silhouette; operator has 8 distinct sampled poses |
| WORK | tool visible | hand tool visible | handheld diagnostic device visible | static pose, not tool contact across frames |
| CARRY | crate visible | parcel visible | front-held device visible | equipment readable in static screenshot |
| REPAIR | small tool visible | small tool visible | large socket/equipment visible | equipment readability; animated contact not yet reviewed |
| CELEB | both arms raised | both arms raised | both arms raised | celebration gesture recognizable in sampled pose |

**Operator WALK additional review:** eight emulator screenshots were inspected in sequence: helmet, face, jacket and full-body framing remain consistent; leg positions alternate and no obvious detached limbs are present. The emulator CI independently verified all eight distinct frame indices and motion in the city-stage actor bounds.

## Approval decisions

- **Static visual framing and role identity: PASS** for the 24 sampled screens.
- **Static action readability: PASS** for WALK, CARRY and CELEB sampled poses; WORK and REPAIR require more detailed motion/prop-contact examination.
- **Full animated loop semantics: NOT YET VERIFIED** for 15 pending actions; OP WALK has an eight-pose review, but strict approval additionally requires canonical artifact provenance and runtime conversion verification.
- **Strict promotions: ZERO**. Existing 219/235 count unchanged.

## Required next step

Capture or regenerate **all frames for each of the 16 pending atlases**, with canonical source hashes and Android-tested runtime hashes, review full loops for foot sliding, tool contact, identity drift and loop seams, and record per-asset decisions. Do not infer semantic approval from zero machine-detected risks.
