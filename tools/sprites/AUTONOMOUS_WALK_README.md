# Pose Studio — production autonome des animations

Ce module **ne demande aucune interaction utilisateur**. Il ne dépend ni de Kaggle, ni d'une IA de génération de poses. Il exploite un **seul renderer vectoriel et un squelette fixe** pour dessiner automatiquement chaque pose. La séquence reste un **candidat technique**, jamais un asset strict DONE.

## Fichiers

- `tools/sprites/pose_studio.html` : renderer/éditeur de secours, appelé automatiquement en mode navigateur invisible.
- `tools/sprites/autonomous_walk.py` : calculateur de marche, rendu PNG, atlas, GIF et QA.
- `tools/sprites/test_autonomous_walk.py` : tests géométriques, rendu navigateur et verrou strict.
- `.github/workflows/pose-studio-autonomous.yml` : génération et dépôt d'archive en artifact GitHub Actions, sans Kaggle.

## Exécution sans interface

```bash
python -m pip install pillow numpy playwright
python -m playwright install chromium
python -m unittest discover -s tools/sprites -p test_autonomous_walk.py
python tools/sprites/autonomous_walk.py \
  --studio tools/sprites/pose_studio.html \
  --output build/auto-pose-tech-walk --frames 24 --fps 12
```

Sur un système disposant déjà de Chromium, aucun téléchargement de navigateur n'est requis. Le script détecte `chromium` ou `google-chrome`, sinon utilise le navigateur installé par Playwright.

## Mouvement contrôlé

La phase de **contact** dure 62 % du cycle par défaut. Le pied au sol reste fixe dans les coordonnées monde pendant que le bassin avance régulièrement. La phase de retour est une courbe d'Hermite avec dégagement vertical sinusoïdal. Les deux pieds sont déphasés de 50 % et les bras bougent à contre-phase. Les coudes et genoux sont calculés par IK dans le renderer.

Le système est réglable par les paramètres `--stride`, `--clearance`, `--stance`, `--frames` et `--fps`. La ligne de sol, les longueurs de jambes et les limites de réglage sont vérifiées ; les configurations impossibles sont rejetées. Le générateur produit le même résultat pour une même configuration et une même version de renderer.

## Sorties

- `frames/` : PNG RGBA 512×512 (24 par défaut).
- `atlas.png` : spritesheet en 4 colonnes.
- `preview.gif` et `contact-sheet.jpg` : observation sans outils externes.
- `frame-poses.json` : **toutes les poses exactes utilisées** par le générateur.
- `project.json` : huit poses-clés compatibles avec Pose Studio pour diagnostic. Les interpolations de l'éditeur ne sont **pas garanties pixel-identiques** aux 24 poses générées automatiquement.
- `qa-manifest.json` : longueur des jambes, glissement, pénétration du sol, continuité, contours transparents, source SHA-256, statut.
- `REVIEW_REQUIRED.txt` : verrou de validation explicite.

## Critères et limites

Un candidat passe les contrôles techniques si les jambes restent dans leur portée IK, qu'aucun pied ne traverse le sol, que les pieds plantés ne glissent pas, que les sprites sont contenus dans leur canevas et que les changements de silhouette ont un raccord suffisamment cohérent.

**Ces vérifications ne prouvent pas la qualité artistique.** Le skin actuel est vectoriel et ne remplace pas le technicien photoréaliste demandé. Une revue du cycle animé, des contacts, des silhouettes et du skin final est indispensable avant l'intégration de production. Aucun script de ce module ne modifie les files de validation ou ne peut placer un asset dans le statut strict `DONE`.

### Évolutions suivantes

1. Remplacer le skin vectoriel par un modèle 3D unique riggé ou des calques artistiques segmentés à pivots, réutilisant les poses calculées.
2. Ajouter les animations WORK, CARRY, REPAIR, IDLE, CELEB avec contraintes propres.
3. Tester le rendu avec la caméra et l'échelle réelles du jeu, puis mener la revue visuelle.

## Matériaux et articulation du pied (mise à jour)

Le renderer `pose_studio.html` ajoute désormais un habillage procédural cohérent avec le squelette : textures de tissu, détails de harnais, genouillères, sacs et noyaux lumineux. Ces effets restent liés aux pivots d'une **identité unique**. Ils sont stylistiques, et ne constituent pas des textures PBR photoréalistes.

Le calculateur `autonomous_walk.py` génère les valeurs `rollL` / `rollR` (bascule talon/pointe) et exporte `frame-events.json` qui associe chaque frame à ses contacts au sol et à ses deux angles de pied. Les événements `footstep_event` indiquent les moments de pose du pied droit et gauche pour les sons et VFX.

Les tests vérifient les raccords de ces angles et la présence des métadonnées. La revue sémantique reste nécessaire : aucun résultat technique, même avec les métriques validées, ne peut promouvoir un asset au statut `strict DONE`.
