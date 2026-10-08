# TECH sprites — soft-mesh v6 (candidats de revue)

## Objectif

Améliorer la continuité des textures de vêtements et d'armure autour du squelette
IK sans redessiner l'identité du personnage à chaque frame. Le module
`soft_skin_deform.py` déforme **les pixels du même atlas WebP** le long de
bandes légèrement courbées entre deux articulations. Les rotations et les
appuis du squelette restent déterministes.

## Méthode

- `signed_joint_bend(hip, knee, foot)` calcule la courbure latérale à partir
  des directions des deux segments, bornée à 5 pixels (3,4 pour les bras).
- `soft_limb(..., bend_px=...)` réalise un échantillonnage bilinéaire inverse
  d'une texture RGBA autour de l'os, avec prémultiplication alpha pour éviter
  les bords noirs. La courbure est nulle aux deux extrémités osseuses.
- `rigged_tech_walk_v2.draw_frame(..., soft_deform=False)` conserve
  **exactement l'ancien rendu** par défaut.
- `rigged_tech_actions_v3.draw_frame` active explicitement
  `joint_fabric=True` et `soft_deform=True` pour les six nouveaux
  candidats, sans toucher aux assets existants.

L'identité, le costume, les accessoires, les points IK et les semelles
reposent toujours sur une seule source atlas commune ; aucun appel à Kaggle.

## Génération automatique

```bash
python -m pip install pillow numpy
python -m unittest discover -s tools/sprites -p test_soft_skin_deform.py -v
python -m unittest discover -s tools/sprites -p test_rigged_tech_walk_v2.py -v
python -m unittest discover -s tools/sprites -p test_rigged_tech_actions_v3.py -v
python tools/sprites/rigged_tech_actions_v3.py --all \
  --skin tools/sprites/skin-tech-v1.webp \
  --output build/tech-actions-v3 --frames 24 --fps 12
python tools/sprites/package_tech_actions_runtime.py \
  --source build/tech-actions-v3 \
  --output build/tech-actions-runtime-review
python -m unittest discover -s tools/sprites \
  -p test_package_tech_actions_runtime.py -v
```

Le workflow `.github/workflows/modular-tech-actions.yml` exécute les mêmes
vérifications et publie les six animations comme **artifacts de revue**.

## Qualité et limites

Le rapport du prototype local couvre 144 images (6 × 24) avec aucun
débordement, une erreur d'alignement des semelles ≤ 0,5 pixel et des
raccords de silhouettes à l'intérieur des seuils configurés. Il s'agit
d'un test géométrique, **pas d'une certification artistique**.
La déformation reste légère : elle ne simule pas la physique du tissu,
les faces cachées, les vrais volumes ni les plis photoréalistes.

`qa-manifest.json` déclare `renderer_features.soft_deform: true`,
`strict_status: NEEDS_REVIEW`, `visual_review_pass: false` et
`semantic_review_pass: false`. Le packer refuse d'établir un pack
runtime candidat si la provenance soft-deform manque.

**Aucun générateur de ce dossier ne peut modifier la queue canonique
ni déclarer une frame non examinée strict DONE.** La revue du mouvement,
des jointures et de la lisibilité dans la véritable caméra du jeu reste
obligatoire avant la publication.

## Points à travailler ensuite

1. Raccord de WORK proche du plafond technique : examiner la boucle à 96px.
2. Améliorer la cinématique poids/bassin et les alternances d'appui réelles.
3. Concevoir un vrai modèle 3D riggé si une qualité photoréaliste AAA est
   indispensable à toutes les animations.
