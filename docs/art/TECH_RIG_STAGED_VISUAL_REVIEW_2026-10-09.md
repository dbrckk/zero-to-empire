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

## APK Android de prévisualisation (CI vérifiée)

- GitHub Actions : `TECH candidate Android preview (no promotion)` run `37983740983`, conclusion **SUCCESS**.
- L'export exact de chacun des trois candidats vers WebP Android a satisfait `process_final_sprites.py`, `validate_runtime_asset.py` et `audit_character_runtime.py` dans un espace de travail éphémère.
- `gradle assembleDebug`, `testDebugUnitTest` et `lintDebug` : **SUCCESS**. Le fichier APK de test contient ces WebP temporaires ; aucune modification des masters et statuts canoniques n'a été committée.
- SHA-256 APK debug : `c8c878e662b9950256f1a29a414120f3c50224c9bb7314f25b67e6ea11667eca` (vérifiée par rapport au rapport de provenance CI).
- **Reste à vérifier :** lancement effectif sur Android, affichage des sprites dans la partie et qualité des interactions / animations dans le jeu. Une compilation verte n'accorde pas une revue artistique ni un strict DONE.

## Preuve d'exécution Android et blocage d'identité — 2026-10-10

- Exécution TECH debug APK [38087592549](https://github.com/dbrckk/zero-to-empire/actions/runs/38087592549) : **SUCCESS** après activation KVM sur GitHub Actions. Le journal confirme CHARACTER_PREVIEW_EMULATOR_PASS=1 et les vrais contrôles « Animation QA », « Pause », « Lecture », « +1 » et « TECHNICIAN ». Les APK et preuves sont dans l'artefact tech-three-art-review-debug-apk-not-approved.
- Capture Android exacte : tmp/zte-character-preview/tech-candidate-grid.png dans cet artefact. Pixels produits par l'émulateur, pas des rendus exportés par le script artistique.
- **Défaut transversal observé** : TECH-IDLE canonique présente un technicien debout en uniforme gris à accents cyan et casquette, de face/3⁄4 ; les trois candidats TECH-WALK, WORK, CARRY présentent un autre personnage, en armure noire et silhouette de profil. Les transitions IDLE → WALK/WORK/CARRY violent l'identité, la tenue et l'orientation cohérentes exigées pour une finition premium.
- La CI Android prouve seulement l'affichage correct des fichiers candidats à 96 dp, pas la cohérence des six actions ni une approbation de production.
- Le candidat TECH-WALK articulé issu du rig est distinct du candidat Kaggle REJECTED_SEMANTIC enregistré dans la file principale : ne pas confondre leurs provenances.
- Une section STAGE-SCALE CHARACTER LAYER utilise maintenant le vrai composable ReviewedCharacterLayer à la taille de scène (35–46 dp), et le workflow capture tech-game-scale-layer.png après un vrai rendu Android. Cette preuve supplémentaire reste soumise à une nouvelle exécution CI.
- **Décision** : aucun nouveau strict DONE. Unifier l'apparence et la perspective entre les six actions, examiner la séparation des pieds, les interactions mains/objets et le mouvement à l'échelle du jeu avant d'envisager toute promotion.
