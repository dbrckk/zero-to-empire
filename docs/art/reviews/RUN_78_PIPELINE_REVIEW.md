# Run 78 — Pipeline Review

Date: 2026-09-07
GitHub Actions run: `34116344191`
Result: **generator failure / zero promotable candidates**
Strict DONE delta: **+0**

## What actually happened
The GitHub wrapper completed correctly, but the Kaggle kernel returned `ERROR` after roughly 18 minutes. The kernel itself did not crash from infrastructure or authentication: it exhausted the selected building families without emitting a fresh technically validated family, then intentionally exited because `KAGGLE_FRESH_CANDIDATES=0`.

Backlog at launch: `BLD=70`, `STATIC=0`, `CHAR_FX=24`, `SKIPPED_RUNTIME=14`.

## Family outcomes
- `BLD-05-T0`: rejected for non-uniform/chromatic border (`sd=30.3`, `chroma=45`).
- `BLD-08-T0`: rejected for non-uniform/chromatic border (`sd=34.1`, `chroma=37`).
- `BLD-09-T0`: rejected for excessive ground-slab geometry (`ground-slab-score=0.55`).
- `BLD-10-T0`: rejected for border contamination (`sd=8.3`, `chroma=24`).
- `BLD-12-T0`: rejected for chromatic border (`chroma=38`).
- `BLD-13-T0` through `T6`: all seven rendered successfully with coverage increasing from **15.2% → 32.7%**, but the entire family was rejected by the previous family QA because centroid drift measured `7.9` against a fixed limit of `7`.

## Diagnosis
1. The previous factory spent one seed on each T0 and abandoned a whole seven-tier family after a single anchor failure. This is poor GPU yield.
2. Centroid drift was a bad proxy after canonical bottom-center normalization; asymmetric machinery growth naturally moves the alpha centroid even when the pivot and framing are correct.
3. The runtime entrypoint referenced a separate v11 factory while the canonical versioned generator remained v10, creating reproducibility drift.
4. The GitHub workflow used brittle source-string substitution for sprite count.
5. Pillow 12 dependency conflicts polluted the Kaggle environment despite not being the direct cause of this run's rejection.

## Corrections made after run 78
- Canonical generator upgraded directly to `building-family-flux-v12-retry-normalized`.
- T0 receives up to **4 seed retries**; later tiers receive adaptive retries.
- Family QA now evaluates normalized geometry, adjacent identity IoU, coverage progression, final-vs-initial growth, and horizontal bbox drift rather than raw alpha centroid drift.
- T0 uses a deliberately smaller canonical frame envelope so starter buildings cannot accidentally read as late-game landmarks.
- Prompts now explicitly demand a flat neutral studio cutout and prohibit floor cards, terrain slabs, horizons, workers, vehicles, pseudo-text, and disconnected props.
- Added automated ground-slab and internal-hole rejection.
- Batch size reduced to **28 manifest tiers** for building waves so adaptive retries can spend compute on recovery instead of breadth.
- `kaggle/github_mass_factory.py` now invokes the canonical factory directly; no temporary v11 mutation layer.
- Workflow count injection is now regex-validated and deterministic.
- Kaggle/runner Pillow is pinned below 12 to avoid the observed Gradio compatibility conflict.

## Next gate
Run 79 must demonstrate at least one complete seven-tier family passing technical family QA before any semantic promotion. Every resulting family still requires full-resolution human/vision semantic review before runtime promotion and strict DONE credit.
