# Pose Studio — édition de sprites à squelette 2D

Éditeur HTML autonome : `tools/sprites/pose_studio.html`. Téléchargez le fichier et ouvrez-le dans Chrome, Firefox ou Edge, y compris sur Android. Aucune connexion à Kaggle ou backend n'est nécessaire.

## Utilisation
1. Choisir Marche, Course ou Repos.
2. Régler amplitude, levée des pieds, bras et oscillation.
3. Déplacer les poignées des pieds, mains ou hanches. Les genoux et les coudes sont recalculés par cinématique inverse (IK).
4. Éditer chacune des huit poses via les poignées ou les coordonnées X/Y; utiliser Annuler/Rétablir.
5. Vérifier la boucle, les contacts au sol et la cohérence à l'échelle du jeu.
6. Exporter un ZIP (PNG RGBA par frame, atlas PNG, project.json), ou enregistrer/importer le projet JSON.

## Limites
Le modèle livré est un **personnage vectoriel de démonstration**, pas le personnage photoréaliste final. Une image PNG importée sert seulement de guide visuel et n'est pas utilisée comme texture à l'export. Pour obtenir l'apparence définitive, remplacer le skin du rig par des calques de corps détourés ou utiliser un modèle 3D unique riggé, rendu à caméra constante. Le système de contrôle des poses peut servir à définir les phases d'animation; il ne produit pas automatiquement des déformations photoréalistes.

## Qualité et sécurité de production
- Le projet conserve `strict_status: NEEDS_REVIEW` et `review_required: true`.
- La cinématique inverse garantit des pivots cohérents mais pas une animation physiquement parfaite.
- L'indicateur 8→1 mesure les distances entre points d'articulation, pas une certification visuelle.
- Les images restent non validées tant que la boucle, les appuis et l'identité n'ont pas été examinés visuellement.

## Test
Un test navigateur Playwright vérifie les commandes, l'annulation/rétablissement, l'import/export JSON, le ZIP et l'affichage mobile. Le script de test local est conservé dans le paquet de travail livré séparément.
