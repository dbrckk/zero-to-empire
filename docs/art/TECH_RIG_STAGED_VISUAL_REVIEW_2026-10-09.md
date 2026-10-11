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

## Extension cohérente à six animations — 2026-10-10

- L'exécution [38088886010](https://github.com/dbrckk/zero-to-empire/actions/runs/38088886010) a réussi le rendu du rig de 24 images par action, les contrôles temporels et les exports canoniques de **six** actions : TECH-IDLE (6 frames), TECH-WALK (8), TECH-WORK (10), TECH-CARRY (8), TECH-REPAIR (10), TECH-CELEB (8).
- Les six planches et leurs planches de contact sont stockées dans art/production/character-rig-review-candidates/ avec le même SHA-256 de texture source, un rapport de provenance par frame et un indicateur semantic_approved=false. Chacune est review-only : aucun master, statut strict ou manifeste de production n'a été promu.
- L'identité du rig est maintenant commune entre ces **six alternatives de revue**, ce qui permet d'évaluer la cohérence d'apparence lors des transitions. Les trois actions TECH-IDLE/REPAIR/CELEB déjà strict DONE dans la file officielle **ne sont pas remplacées** ; l'essai compare des alternatives d'identité unifiée, pas une rétrogradation.
- Les réserves identifiées sur les vrais pixels ne disparaissent pas : perspective principalement latérale, chevauchement des pieds de WALK/CARRY, contact écran de WORK et geste de REPAIR à rendre lisibles à la taille réelle. Le premier vrai test Android du groupe de six est lancé par le workflow dédié et doit terminer avant toute nouvelle conclusion artistique.
- La synchronisation du compte strict reste : **216/235 DONE** et **19 actions en revue**. Ne jamais compter six candidats exportés comme six validations.

## Contrôle de cadrage de la taille réelle — 2026-10-10

- L'exécution Android à six candidats [38088989331](https://github.com/dbrckk/zero-to-empire/actions/runs/38088989331) a réussi compilation, audit, galerie et création de l'APK de revue. Les six ressources candidates s'ouvrent réellement dans la galerie Android.
- **Limitation découverte dans les preuves** : la première capture tech-game-scale-layer.png affichait la partie supérieure vide du conteneur 620 dp. Le libellé visible et un fichier PNG non vide étaient insuffisants pour prouver l'apparition des personnages placés à mi-hauteur/en bas de la scène. Ce succès d'automatisation ne doit pas être interprété comme une revue du rendu à taille réelle.
- Correction dans le script d'émulateur : un défilement supplémentaire vers le bas, puis refus d'une capture dont le bas de la zone de jeu ne présente pas suffisamment de pixels colorés compatibles avec des acteurs. Le fond de la scène seul ne peut pas satisfaire ce test. Nouvelle CI nécessaire pour confirmer le cadrage.
- La relance [38089476096](https://github.com/dbrckk/zero-to-empire/actions/runs/38089476096) a finalement **réussi** avec CHARACTER_PREVIEW_GAME_SCALE_COLORED_PIXELS=1012 et CHARACTER_PREVIEW_GAME_SCALE_SCREENSHOT_PASS=1. La capture réelle tech-game-scale-layer.png montre bien les huit personnages, dont deux TECH à 35–46 dp : fin du faux positif de scène vide.
- L'inspection visuelle de cette capture met en évidence une **faible séparation tonale des deux TECH en armure noire sur le décor nocturne**. Ces figures restent minuscules ; ni le seuil de pixels, ni le PASS émulateur ne prouvent une lisibilité premium.
- Un traitement de lumière de contour cyan **réversible, limité aux TECH dans ReviewedCharacterLayer** a été proposé sur le rendu de jeu, sans changer les masters ni le découpage des atlas. La nouvelle CI Android et la comparaison de captures sont nécessaires pour juger son bénéfice et son coût.
- **Statut inchangé** : six variantes TECH en revue, aucun nouveau strict DONE. Vérifier ensuite la lisibilité sur fond nocturne, les poses, la continuité de costume/caméra et les contacts mains/objets à l'échelle véritable.

## Inspection des captures Android réelles — 2026-10-11

Sources : artefact `tech-six-art-review-debug-apk-not-approved` de [la CI 38089476096](https://github.com/dbrckk/zero-to-empire/actions/runs/38089476096), fichiers `tmp/zte-character-preview/tech-candidate-grid.png` et `tmp/zte-character-preview/tech-game-scale-layer.png`. Il s'agit de **captures d'écran réelles de l'émulateur Android** ; elles ont été ouvertes et examinées visuellement, pas simplement déclarées présentes par le script.

| Contrôle | Observation vérifiable | Conséquence |
|---|---|---|
| Galerie, six actions TECH | Les six vignettes IDLE, WALK, WORK, CARRY, REPAIR, CELEBRATE présentent désormais la même silhouette masculine de profil, coiffure noire, équipement sombre et sac dorsal. Les anciens personnages gris/cyan de face ne sont pas mélangés à ces six *alternatives de revue*. | **Amélioration d'identité inter-actions**, pas une approbation des masters officiels. |
| WALK à 96 dp | L'animation est dessinée de profil ; les chaussures se superposent et la séparation de la jambe arrière est faible sur certaines poses. | **Blocage de lisibilité** pour un jeu en vue 2.5D ; examiner l'intégralité des frames et améliorer le contraste des appuis. |
| WORK et REPAIR à 96 dp | Les deux actions présentent chacune un panneau cyan devant le corps ; la différence gestuelle entre « travailler » et « réparer » est faible sur la vignette figée. | Rendre le contact de main, l'outil et la conséquence de l'action nettement distincts sur tout le cycle. |
| CARRY à 96 dp | Une caisse ambrée remplace l'ancien panneau bleu ; sa lecture est plus claire, mais elle paraît petite par rapport au buste et son support par les deux mains reste difficile à juger. | Revoir la silhouette de charge et le contact main/poignée, sans prétendre que le test de coordonnées prouve l'illusion de poids. |
| CELEBRATE à 96 dp | Les bras sont levés avec particules cyan, mais l'impact du geste est limité par la perspective latérale. | Accentuer l'arc de mouvement et la silhouette de célébration sans changer d'identité. |
| Rendu dans la ville | La capture de scène montre **huit personnages**, dont deux TECH effectivement visibles à taille réelle. Les TECH sont très petits et sombres sur un fond bleu nuit. Le liseré cyan est subtil ; l'identification du métier par la silhouette seule demeure difficile. | L'existence de pixels visibles **n'est pas une preuve de qualité AAA**. Réviser lisibilité, éclairage local, hiérarchie visuelle et animation en contexte. |

**Priorités de correction avant promotion :** (1) marche avec appuis distincts et direction cohérente avec la caméra ; (2) gestes WORK/REPAIR non interchangeables et accessoires en contact ; (3) charge CARRY visiblement portée ; (4) différenciation et contraste à 35–46 dp sur la scène ; (5) inspection temporelle Android en lecture, pause et pas-à-pas. Les tests d'export et le smoke Android sont verts, mais la revue sémantique reste **NON VALIDÉE**.

**Compte officiel : 216/235 strict DONE ; 19 NEEDS_REVIEW.** Aucune promotion sur la base de ces captures.

## TECH-REPAIR : arc industriel chaud, preuve comparée — 2026-10-11

- Changement source limité au rig : PR [#144](https://github.com/dbrckk/zero-to-empire/pull/144), fusionnée (commit `843ea863`). L'action REPAIR possède désormais un noyau de contact ambré, une bande de sécurité industrielle et onze petites étincelles déterministes calculées à partir de la **même pointe physique** que le chalumeau. L'action WORK conserve le panneau de télémétrie cyan. Aucun autre costume, pivot, atlas master de production ou statut strict n'est modifié par ce changement.
- Rendu de la branche en revue : workflow [38122095069](https://github.com/dbrckk/zero-to-empire/actions/runs/38122095069) **SUCCESS** (moteur, 144 images, audits temporels, paquets et contrôles techniques). La planche REPAIR a été inspectée visuellement à 96 px. Les étincelles se voient surtout durant les frames de soudure ; elles restent petites à l'échelle de la ville.
- Le réexport canonique de revue à six actions [38122285871](https://github.com/dbrckk/zero-to-empire/actions/runs/38122285871) est **SUCCESS**. Dans `art/production/character-rig-review-candidates/review-report.json`, la nouvelle planche REPAIR a le SHA-256 `a2c080be81431a` (préfixe), `semantic_approved=false`, et les mêmes contraintes 1024×1024 / 4×4. Les cinq autres actions ont conservé leurs empreintes.
- Comparaison locale de la frame source REPAIR-04, mise à l'échelle d'affichage 192×192 : le nombre de pixels définis comme « ambrés » par une heuristique simple passe de **79 à 183**. Il s'agit d'une mesure de changement de palette, **pas** d'un score de qualité graphique ou d'une approbation automatique.
- L'APK de revue de ces nouveaux pixels est en cours de validation via [38122340570](https://github.com/dbrckk/zero-to-empire/actions/runs/38122340570). Même une CI verte ne prouve ni le contact crédible à 35–46 dp, ni une qualité AAA : inspection temporelle des gestes et de la perspective toujours requise.
- **Décision :** six candidats TECH encore en revue, zéro nouvelle promotion. Nombre strict canonique inchangé : **216/235**.
