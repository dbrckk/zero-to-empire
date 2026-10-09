# Revue visuelle — candidat TECH articulé — 2026-10-09

## Périmètre et provenance

- Source graphique unique : `tools/sprites/skin-tech-v1.webp` (12 parties de corps à textures constantes).
- Moteur : `tools/sprites/rigged_tech_actions_v3.py`, animation articulée à 24 images par action.
- Conversion au contrat Android : `tools/sprites/export_tech_canonical_review.py`, 8 images WALK, 10 WORK et 8 CARRY sur 4×4 / 1024×1024 / RGBA. Aucune source canonique ni ressource Android de production n'est modifiée par cet export.
- Sources des trois candidats, planches d'inspection, aperçus GIF, empreintes SHA-256 et rapport : `art/production/character-rig-review-candidates/`.
- GitHub Actions : `TECH canonical review staging` run `37983201807` et run `37983528623` (après correction de la caisse) : **SUCCESS** pour génération, QA technique/temporal, export canonique et staging.
- Production officielle : **216 / 235 strict DONE** ; ces trois sorties sont des candidats distincts et ne valent **aucune** nouvelle validation.

## Revue visuelle de vraies images exportées

| Candidat | Points positifs observés | Réserve bloquant encore un strict DONE |
|---|---|---|
| `CHR-TECH-WALK` | Une seule identité réelle d'une frame à l'autre, visage et équipement stables, animation de jambes effective, transparence propre et silhouette entière | Vue essentiellement de profil plutôt que la 2.5D trois-quarts souhaitée ; la séparation des deux jambes est parfois difficile à lire en aperçu 96 px. La pertinence esthétique dans la caméra Android et les contacts de pieds en mouvement restent à constater dans le jeu. |
| `CHR-TECH-WORK` | Identité stable, panneau de contrôle et éclairages cyan cohérents, variations de mains/écran ; anomalies automatiques majeures non détectées | L'interaction des deux mains avec le panneau est trop discrète à petite échelle. Il faut comparer la visibilité de l'action et du dispositif à l'échelle de gameplay réelle, pas valider seulement la présence d'un effet lumineux. |
| `CHR-TECH-CARRY` | Identité et silhouette stables. Le dispositif bleu qui ressemblait à un écran a été remplacé par une caisse industrielle ambrée unique, avec poignées attachées aux deux positions de main sur tout le cycle et vérification de couleurs/points de contact | Le contact visuel des mains/poignées demeure difficile à distinguer en 96 px ; un examen de l'animation et des occultations à l'échelle Android est nécessaire. Le filtre automatique signale encore une structure des membres inférieurs difficile à certifier. |

Ces observations sont des constats artistiques sur les planches exportées, **pas** une approbation de sortie en production.

## Preuves et critères de transition vers strict DONE

1. Chaque frame doit montrer exactement un seul technicien, un corps complet, une seule identité, la bonne action et une caméra cohérente. Vérifier l'animation en lecture normale, pas uniquement le contact sheet.
2. WALK : alternance crédible des appuis et absence de glissement du pied planté ; WORK : mains en contact lisible avec un équipement réellement opéré ; CARRY : deux mains supportent une même caisse sans aucun flottement.
3. Confirmer sur Android que le code de la ville affiche effectivement les ressources exactes, à la taille de jeu prévue, avec réglage de mouvement réduit si applicable. Un APK construit ne certifie pas cette visibilité.
4. Conserver empreintes des PNG approuvés, QA complète, preuves de revue et commit Android strictement associé. Seule une CI Android verte sur ce commit permet de promouvoir le statut canonique et la ligne du manifeste.
5. Garder ces trois candidats dans `art/production/character-rig-review-candidates/` tant que ces critères ne sont pas démontrés. Ne pas modifier `art/incoming/final-sprites` ou `master-asset-queue.json` sur la seule base d'un test géométrique.

Le workflow `TECH candidate Android preview (no promotion)` produit un APK de **test** à partir des candidats sans les committer en ressources de production. Sa validation et la revue en jeu restent des étapes distinctes.
