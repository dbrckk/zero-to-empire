# Autonomous TECH animation library — six review candidates

The same 12-piece character texture atlas and two-bone IK rig produce all six clips with no Kaggle, prompt-by-frame regeneration, or manual Pose Studio interaction.

| Asset | Motion | Special element |
| --- | --- | --- |
| CHR-TECH-WALK | Alternating grounded walk | Footstep events |
| CHR-TECH-CARRY | Carrying a box while walking | Two fixed cargo grips |
| CHR-TECH-IDLE | Breathing at rest | Cyclic status light |
| CHR-TECH-WORK | Working with a display | Moving hands and UI |
| CHR-TECH-REPAIR | Welding equipment | Tool and timed sparks |
| CHR-TECH-CELEB | Raised-arm celebration | Particle accents |

## One-command production

```bash
python -m pip install pillow numpy
python -m unittest discover -s tools/sprites -p 'test_rigged_tech_actions_v3.py' -v
python tools/sprites/rigged_tech_actions_v3.py --skin tools/sprites/skin-tech-v1.webp --output build/tech-actions-v3 --frames 24 --fps 12 --all
```

This produces 144 RGBA frames, six atlases, six looping GIFs, six normal and six 96px game-scale contact sheets, six event timelines, six QA manifests, six ZIP packages and a production-index.json. GitHub Actions workflow `.github/workflows/modular-tech-actions.yml` runs the same process automatically.

The shared `rigged_tech_walk_v2.py` supports optional pose_override, prop_underlay, and prop_overlay callbacks. Without them, the original WALK rendering remains unchanged.

## Safety / acceptance

Machine tests check cyclic continuity, foot-ground placement, footstep events, cargo grip, arm reach, alpha boundaries, movement distinctness and determinism. These are *technical checks*, not artistic approval.

Known limitations: stiff 2D fabric and metal pieces, mechanical knees and ankles, equipment and hand overlap at small scale, and near-static facial expression. The clips need actual playback at the target game camera size and an independent semantic/visual review.

All six candidates explicitly retain `strict_status: NEEDS_REVIEW`, `visual_review_pass: false` and `semantic_review_pass: false`. The scripts NEVER modify the canonical production queue, bypass the manual review gate or claim to have completed the 235-asset backlog.

## Next steps

1. Refine silhouette and shoe roll at 96px, and separate optional VFX layers.
2. Create a unified on-device visual review sheet for six loops.
3. Review each generated action in game context before integrating into runtime assets.


## Spine flex v4 — mouvement secondaire déterministe

Le rendu des six animations prend maintenant en charge `torso_lean_rad`, une
flexion du buste autour du pivot du bassin. La tête reste redressée, tandis que
les épaules, les bras, le sac et les protections du torse suivent un même pivot.
Les pieds ne sont pas déplacés par cette transformation. Les courbes sont
périodiques et adaptées à l'action : marche plus dynamique, transport plus
stable, repos discret, gestes de travail/réparation modérés et célébration plus
ample. REPAIR utilise une amplitude réduite pour protéger la transition 24→1.

Compatibilité : si `torso_lean_rad` est absent ou égal à zéro, le renderer
génère les mêmes pixels que sa version antérieure (test de non-régression).
Les valeurs non finies ou dépassant 0,085 radian sont rejetées. Les tests
vérifient la périodicité, la portée réelle des épaules après rotation, les
contacts au sol, l'identité et le verrou de revue.

Une planche `review-all-actions-96.png` à l'échelle du jeu est également
générée et le module d'export vérifie chaque silhouette. Ces diagnostics ne
constituent pas une validation visuelle professionnelle : anatomie, poids,
matériaux et raccords doivent encore être inspectés, surtout en lecture dans le
jeu. Aucun asset unreviewed ne doit devenir strict DONE.


## Joint fabric v5 — souplesse des raccords sans redessin de l'identité

Le module \`rigged_tech_walk_v2.py\` dispose désormais d'une option
\`joint_fabric=True\`, activée pour les six animations candidates via
\`rigged_tech_actions_v3.py\`. Les protections existantes restent, mais
des raccords en tissu foncé, avec plis orientés selon les vecteurs de
cinématique inverse, sont placés **derrière** les genoux/coudes ; un
manchon court relie la jambe à la botte. Ces raccords suivent les
articulations à chaque pose, sans IA et sans régénérer les textures.

Le rendu historique de WALK utilise \`joint_fabric=False\` par défaut ;
il conserve ses pixels, ses pivots et ses sorties. Les tests vérifient
que la version modifiée est reproductible, distincte de l'ancienne,
non coupée dans son canevas et toujours soumise à une revue stricte.

**Limites :** il s'agit de panneaux 2D flexibles superposés, pas d'un
simulateur physique de tissu ni d'une déformation 3D. Les détails
peuvent rester peu visibles à 96 pixels. Le jeu ne doit pas utiliser
ces clips comme assets validés sans vérification visuelle et sémantique.
Les anciens assets strict DONE ne sont ni réécrits ni réévalués.
