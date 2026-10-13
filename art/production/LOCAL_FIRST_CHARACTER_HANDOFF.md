# Local-first character production (13 October 2026)

The user requested that all **new** art be created directly in the ChatGPT working environment, **without Kaggle**.

## Production decision

- Stop automatically scheduling `Asset Autofactory 235` and `Kaggle Async Character Collector`. The manual dispatch entrypoints remain for historical compatibility but are not part of the new production workflow.
- New art is generated locally as deterministic RGBA character sprites and assembled as **1024×1024, 4×4 grids of 256×256 cells**, matching `CanonicalCharacterRaster.kt`.
- Role silhouettes and costumes are fixed across actions: OP orange helmet/dark suit, LOG ivory helmet/amber jacket, ENG ivory helmet/graphite-cyan outfit.
- The first locally created candidate pack contains **16 atlases / 138 authored frames** covering every unresolved canonical character ID. Its exact source and PNGs are attached to the ChatGPT conversation as `zero_to_empire_local_characters_v1.zip`, with a `zero_to_empire_local_preview.png` contact sheet. These files are **not yet checked into GitHub or wired into Android resources**.
- These are **stylized 2D prototypes**, not approved AAA production assets. Technical drawing quality, animation smoothness, silhouette clarity, runtime compatibility and artistic review still need improvement.
- The master ledger's strict DONE count must **not** change on the basis of creating these candidate PNGs. Each asset requires review and Android integration first.

## Next steps

1. Iterate the local sprite renderer's anatomy, pose dynamics, shading and prop interaction; regenerate the atlases locally.
2. Import only reviewed candidate PNGs into `app/src/main/res/drawable-nodpi` and the canonical incoming-art directory.
3. Run full character motion and Android release validation before marking any of the 16 unresolved entries strict DONE.
4. Remove remaining Kaggle-only assumptions from the queue/orchestrator as the local pipeline is proven.

Do not automatically resume Kaggle or count candidate PNG files as strict DONE.
