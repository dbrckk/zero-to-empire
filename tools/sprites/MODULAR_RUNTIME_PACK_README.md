# TECH runtime review atlas packaging

All six TECH clips are synthesized **without Kaggle, image regeneration per frame or manual Pose Studio operations**. The existing single-skin IK renderer builds the character and the new packaging stage generates compact game-scale atlases, metadata and a browser playback diagnostic.

## Reproducible one-command stages

```bash
python -m pip install pillow numpy
python tools/sprites/rigged_tech_actions_v3.py \
  --skin tools/sprites/skin-tech-v1.webp \
  --output build/tech-actions-v3 --frames 24 --fps 12 --all
python tools/sprites/package_tech_actions_runtime.py \
  --source build/tech-actions-v3 \
  --output build/tech-actions-runtime-review
python -m unittest discover -s tools/sprites -p test_package_tech_actions_runtime.py -v
```

The GitHub workflow `.github/workflows/modular-tech-actions.yml` runs these stages unattended and publishes the result as a **review-only** Actions artifact.

## Output

- `atlases/{walk,carry,idle,work,repair,celeb}-{128,256}.png`: 24-frame RGBA atlases in 6 columns × 4 rows.
- `runtime-manifest.json`: timing, row-major UV ordering, per-frame visual bounds, fixed pivots, identity hashes and strict review flags.
- `events/{action}.json`: original footstep, screen update, repair and celebration events.
- `atlases/{action}-shadow-{128,256}.png`: optional per-frame contact shadow, computed from the same foot trajectories; shipped as a **separate VFX layer** and disabled by default in the runtime manifest.
- `review-player.html`: six animations side by side, independent of external UI libraries, with speed adjustment and responsive layout.
- `game-scale-overview.jpg`: a quick 6-action comparison.
- `REVIEW_REQUIRED.txt`: explicit release gate.

Pivots derive from (252,449) in the 512×512 source canvas. The variants contain pixel pivots scaled to their canvas size. **Visual alpha bounds are not collision or damage hitboxes**; gameplay hitboxes must be designed and approved separately.

## Strict release safeguard

The package refuses missing assets, conflicting skin hashes, missing review markers, unapproved QA, unexpectedly sized frames, missing frame indices, clipped silhouettes or a malformed source index. Four regression tests cover success, the shadow layer and intentional attempts to bypass the review gate. The review player can composite optional shadows behind the character; neither the candidate sprites nor the source identity atlas are modified.

The pipeline NEVER edits `art/production/master-asset-queue.json`, NEVER marks assets `strict DONE` and NEVER copies candidates over release resources. Original visual quality limits (stiff articulated seams, boot motion, hand-object overlap and small-screen readability) remain open for genuine independent visual/semantic review.


## Contrat de données et revue à l'échelle réelle (octobre 2026)

Le générateur `rigged_tech_actions_v3.py` émet `production-index.json` au format
`zte-modular-actions-v3`, avec `source_skin_sha256` commun aux six clips.
Chaque action fournit `footstep-events.json` (et l'alias de compatibilité
`animation-events.json`) ; le module `package_tech_actions_runtime.py`
vérifie explicitement ce contrat avant l'export. Aucun raccourci de validation
visuelle n'est autorisé.

Le packer effectue un contrôle à **96×96 pixels** pour chaque image : silhouette
non vide (au moins 500 pixels alpha ≥128), largeur ≥20 pixels, hauteur ≥56
pixels, marge extérieure ≥3 pixels. Les mesures individuelles figurent dans
`runtime-manifest.json` sous `game_scale_96px_metrics`. Elles repèrent les
sprites coupés ou illisibles, mais ne certifient **ni le réalisme ni la qualité AAA**.

La planche `review-all-actions-96.png` montre huit poses de chacune des six
animations sans agrandissement. Le lecteur `review-player.html` affiche
96 pixels réels par défaut, permet pause, vitesse, zoom, et conserve les
**ombres désactivées par défaut**. Les ombres sont des calques facultatifs,
pas des pixels du personnage.

Les gestes WORK, REPAIR et CELEB ont été élargis pour être davantage visibles
à petite échelle ; le chalumeau REPAIR suit désormais la main. Une amplitude
d'au moins 18 pixels du poignet droit à l'échelle source 512px est requise pour
ces trois actions. Le modèle reste un assemblage texturé 2D rigide, à inspecter
dans une véritable séquence de jeu avant tout passage en production.

Le workflow `.github/workflows/modular-tech-actions.yml` doit être contrôlé
après chaque changement. Un passage de tests local ne signifie pas que la
dernière exécution GitHub Actions est confirmée.
