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


## v7 — transfert d'appui et raccord WORK optimisé

Le module `tools/sprites/weight_transfer.py` calcule la charge relative de chaque
pied avec une enveloppe `sin²` qui s'annule continûment au lever/poser. Pour
WALK et CARRY, le bassin et les deux poignets suivent un léger déplacement
avant/arrière de respectivement 4,0 et 2,2 px (référentiel 512×512) ;
**les coordonnées des pieds et leurs événements restent identiques**.
Le solveur IK recalcule automatiquement les genoux et compense le transfert
de poids, sans déplacement des cibles d'appui au sol. Les poses sont
déterministes et ne nécessitent ni Kaggle ni interface utilisateur.

Le clip WORK utilise une rotation cyclique de son origine temporelle :
`phase_origin_frame=round(frames*5/24)` (soit 5 pour 24 images et 2 pour 8).
Ce changement reindexe simplement les frames, sans interpolation, et
rapproche la transition de fin de boucle de la variation médiane.
Lors du contrôle local sur le prototype texturé à 24 images, le ratio de
raccord WORK est passé d'environ 1,81 à 1,02. Cela ne garantit pas une
animation naturelle, seulement un meilleur point de raccord.

`test_weight_transfer.py` vérifie la continuité cyclique, la portée des
jambes et des bras, la conservation des pieds plantés et le mouvement
borné du bassin. Les tests des six animations couvrent aussi les
métadonnées de provenance et la nouvelle origine WORK. Le packeur
`package_tech_actions_runtime.py` rejette les candidats sans ces
informations ou sans `weight_transfer_pass`. Les sorties gardent
`NEEDS_REVIEW`, `visual_review_pass=false` et
`semantic_review_pass=false`. La validation visuelle en lecture réelle
reste indispensable, particulièrement pour l'armature 2D et les textiles.


## v8 — interaction physique des outils, effets liés aux mains

`action_contact.py` centralise les coordonnées des deux points de contact
sur la console WORK, le point fixe de soudure REPAIR, la longueur admissible du
chalumeau et les courbes d'intensité lumineuse. Les trajectoires des mains sont
périodiques, calculées depuis **un seul rig** et bornées à l'intérieur de l'écran
pour les 24 frames : elles ne sont plus de simples gestes aléatoires devant
un accessoire statique.

- **WORK** : les deux poignets touchent effectivement les limites de l'écran ;
  deux indicateurs lumineux suivent chaque gant dans un calque de premier plan
  sans passer derrière les bras. La console conserve son identité et son
  affichage technique.
- **REPAIR** : le manche du chalumeau relie le poignet au même point de
  soudure sur la pièce ; les étincelles sont produites en premier plan et leur
  déclenchement suit exactement `repair_spark_intensity(t)` ainsi que les
  événements `weld-sparks` exportés.
- **QA** : les violations de contact, la plage de longueur du chalumeau et
  `interaction_contact_pass` figurent dans `qa-manifest.json`.
  L'export `package_tech_actions_runtime.py` refuse les candidats présentant
  des mains hors écran, une connexion d'outil invraisemblable ou des métadonnées
  de contact absentes.
- **Tests** : `test_action_contact.py` vérifie les trajectoires échantillonnées
  et leur périodicité ; les suites `test_rigged_tech_actions_v3.py` et
  `test_package_tech_actions_runtime.py` assurent le raccord au rendu et
  le verrou d'export.

Le prototype local de revue a généré **48 sprites** (WORK et REPAIR),
deux atlas transparents et deux GIF, avec contrôles géométriques conformes.
Cela ne constitue ni un test de gameplay dans le moteur ni une approbation
visuelle ; les 19 éléments du backlog restent soumis à leur validation
sémantique individuelle. Pas de mise à jour automatique du compteur strict.


## v8.1 — événements synchronisés et régressions bloquantes

Pour l'action WORK, les impulsions lumineuses de contact se produisent à
quatre maxima temporels par boucle. Le générateur utilise désormais
`work_event_indices(frames, phase_origin_frame)` plutôt que des événements
tous les quarts de boucle (qui tombaient sur les minima de lumière).
Le calcul tient compte de l'origine du cycle WORK et fonctionne pour
chaque nombre pair de frames autorisé (8 à 64), y compris 12 frames.
En 24 frames, origine=5, les événements WORK sont sur les frames
**4, 10, 16, 22**. Les étincelles REPAIR ont leur propre règle de phase
et restent alignées sur le rendu.

Le packeur refuse maintenant les timelines WORK/REPAIR désynchronisées
des effets visibles, même si le reste des tests géométriques passe.
Les tests ne doivent jamais exiger des événements de pas pour
IDLE, WORK, REPAIR ou CELEB : seuls WALK et CARRY émettent des
pas. Cette erreur de test a été corrigée.

Contrôles : `test_action_contact.py`,
`test_rigged_tech_actions_v3.py`,
`test_package_tech_actions_runtime.py`. Le workflow
`.github/workflows/modular-tech-actions.yml` exécute les tests
avant la production des 144 frames puis le packeur QA.
Ces contrôles sont **techniques** et ne valident aucune qualité artistique.
Tous les candidats restent `NEEDS_REVIEW` jusqu'à revue visuelle réelle.


## Audit temporel v1 — contrôles des vraies images à 96 px

Le pipeline contient désormais `tools/sprites/temporal_sprite_audit.py` et
`test_temporal_sprite_audit.py`. Après la génération des six actions,
l'audit lit **chaque PNG RGBA réellement exporté**, puis effectue :

- détection des images vides, tronquées et massivement dupliquées ;
- comparaison des silhouettes alpha entre chaque frame consécutive, y compris 24→1 ;
- contrôle de la discontinuité de boucle, d'un saut de pose isolé et d'une brusque variation de surface opaque ;
- vérification de l'identité du skin commun et du verrou de revue visuelle/sémantique.

Les limites de rejet sont volontairement objectives et tolérantes :
ratio de raccord >2,5, saut isolé >4,5× la variation médiane ou
variation de surface opaque >20 % d'une frame à la suivante.
Une animation très peu changeante (variation médiane <0,002)
ou contenant trop d'images identiques (<80 % de frames uniques)
est également refusée. Le seuil n'évalue **pas** le talent artistique,
la cohérence des accessoires ni les contacts physiques.

Exécution automatique :
```bash
python -m unittest discover -s tools/sprites -p 'test_temporal_sprite_audit.py' -v
python tools/sprites/temporal_sprite_audit.py \
  --source build/tech-actions-v3 --output build/tech-temporal-review
```

Le workflow GitHub Actions publie `temporal-qa.json`,
`frame-transition-metrics.csv` et `motion-timeline.png` avec les
candidats de revue. Cinq tests synthétiques vérifient aussi que des
frames absentes/vides, coupées, dupliquées, une rupture de cycle et
un faux statut visuellement approuvé sont rejetés. Tous les résultats
restent `NEEDS_REVIEW` et ne modifient jamais la file stricte de 235 assets.


## Audit temporel v2 — anti-scintillement et preuves liées aux pixels

L'audit `temporal_sprite_audit.py` contrôle désormais la stabilité des couleurs
en plus des silhouettes : pour chaque paire de frames adjacentes (y compris
la transition dernière→première), il calcule une différence RGB médiane
sur les pixels fortement opaques communs, après réduction à 96×96.
Cette méthode reste insensible à l'essentiel des particules et halos transparents,
tout en détectant une modification brutale du costume ou de la peau qui
ne déplacerait aucun contour. Seuil conservateur : maximum de 42 unités
RGB ou six fois la variation médiane plus 15. Ce seuil n'est **pas** une
note de qualité artistique.

L'outil peut aussi vérifier le SHA-256 du **fichier WebP réel** passé par
`--skin tools/sprites/skin-tech-v1.webp`, au lieu de simplement comparer
les déclarations des manifests. Chaque séquence est identifiée par
`ordered_frame_digest_sha256`, calculé sur les pixels RGBA des frames
dans l'ordre exact de lecture.

Le packeur accepte `--temporal-report build/tech-temporal-review/temporal-qa.json`.
Ce mode est **obligatoire dans GitHub Actions** : le packeur recalcule
les signatures des sprites sources et rejette toute preuve temporelle
ancienne, falsifiée ou associée à un autre jeu de frames. Le manifeste
du pack final indique `temporal_evidence_verified=true` uniquement
après cette vérification. L'appel sans rapport reste permis pour
l'inspection locale, mais porte explicitement
`temporal_evidence_verified=false`.

Les tests de régression incluent une frame recolorée sans changement
d'alpha et un atlas de skin modifié. Ces contrôles ne certifient ni la
continuité du mouvement en situation réelle ni la validation humaine.
`strict_status` reste `NEEDS_REVIEW`, avec
`visual_review_pass=false` et `semantic_review_pass=false`.
