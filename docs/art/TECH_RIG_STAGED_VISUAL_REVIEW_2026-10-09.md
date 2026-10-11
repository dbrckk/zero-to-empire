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

## CARRY — nouvelle charge industrielle lisible — 2026-10-11

- Source : commit [7c62428](https://github.com/dbrckk/zero-to-empire/commit/7c62428c9609f0453e9cbf0d2686f21898be6dba), générateur `rigged_tech_actions_v3.py` et contrôle `test_rigged_tech_actions_v3.py`. La caisse occupe maintenant une plus grande surface de silhouette : bandeaux, nervures ambrées, serrure centrale et couvercle en légère perspective.
- Cinématique préservée : poignées relatives fixes `(root_x+29,root_y-55)` et `(root_x+103,root_y-55)` ; le renderer conserve le rig, l'identité du personnage, les 24 phases et les deux appuis. La modification est un prop de revue, pas une retouche de master.
- [Pipeline de staging 38124224085](https://github.com/dbrckk/zero-to-empire/actions/runs/38124224085) : **SUCCESS** ; le nouvel export est stocké dans `art/production/character-rig-review-candidates/zte_chr_tech_carry_final.png`. Son SHA-256 dans `review-report.json` commence par `3a6059d78d71b5`, différent de l'ancien `3d1b10d44b46`. Les autres actions ne changent pas sur ce point.
- **Examen des huit vraies vignettes CARRY à 96px :** caisse nettement plus volumineuse et orange distincte de l'écran cyan de WORK ; la tenue et la silhouette restent stables entre images. La lisibilité des deux points de prise, le poids de l'objet et la jambe arrière restent insuffisamment démontrés à 39–42dp pour accorder strict DONE.
- L'exporteur a conservé `LOWER_LIMB_STRUCTURE_UNVERIFIED` pour CARRY et WALK. Le test Android de ce **nouveau** SHA doit encore être vérifié avant une éventuelle décision.
- **Statut officiel inchangé : 216/235 strict DONE** ; six TECH alternatives restent hors production.

## QA Android : captures de personnages coupées et touches hors écran — 2026-10-11

- **Revue des pixels Android** : les six fichiers `tech-stage-<ACTION>.png` issus du run [38124838699](https://github.com/dbrckk/zero-to-empire/actions/runs/38124838699) avaient reçu le verdict automatique « six actions différentes », mais les vignettes TECH « NIGHT · 42 dp » et « DAY · 39 dp » étaient **coupées au niveau des jambes** par le bas de la zone visible de la `LazyColumn`. Le pixel audit ancien comptait aussi une partie de la barre de navigation Android comme pixels « visibles », ce qui gonflait artificiellement sa preuve. Les tests de différences par paire d'actions ne signifient pas que les personnages sont entiers.
- **Correction de l'interface QA** : commit [f5b3257](https://github.com/dbrckk/zero-to-empire/commit/f5b32577871035eb958e34ae263c95ee9c8a0eaf), qui place les deux aperçus compacts **avant** les six boutons de sélection pour préserver la visibilité du personnage entier.
- **Contrôle strict** : commit [8380bce](https://github.com/dbrckk/zero-to-empire/commit/8380bce8a04adf33df08c028f5e33dea846172c0), qui vérifie en vrais pixels d'émulateur que **les deux fonds de la vignette** existent encore bien en dessous de la position attendue des chaussures. Sur les anciennes captures, le contrôle du fond DAY échoue conformément à l'anomalie observée, au lieu de valider seulement la tête et le buste.
- **Défaillance intermédiaire diagnostiquée** : [run 38128625718](https://github.com/dbrckk/zero-to-empire/actions/runs/38128625718), compilation et validations de sources vertes mais smoke Android rouge : le libellé « Daylight stage » occupait `[95,100][329,105]`, soit **5 px de hauteur**, car il était presque intégralement hors écran. Le script utilisait une simple recherche de texte et tapait hors de la surface tactile utilisable ; aucun problème de graphique ni de code de jeu n'était démontré par cet échec.
- **Nouvelle protection d'interaction** : commit [9c06bc3](https://github.com/dbrckk/zero-to-empire/commit/9c06bc3b8b1b6c0d01a06bffdef13d5f4edae496). Le bouton « Daylight stage » doit être suffisamment haut et complètement présent à l'écran ; sinon le smoke défile puis vérifie à nouveau. Nouvelle CI Android [38129090657](https://github.com/dbrckk/zero-to-empire/actions/runs/38129090657) à conclure avant d'affirmer que le flux complet est corrigé.
- **Interprétation** : la géométrie des contrôles de QA fait partie des exigences de validation des graphismes. Même une capture de personnages complets sur Android ne garantit pas leur animation AAA, leur perspective, la séparation des pieds ni la qualité des contacts ; aucun `strict_status` ne change sans revue sémantique. **216/235 DONE**.

## Galerie Android : six actions TECH en corps entier — 2026-10-11

- **Exécution finale :** [TECH preview 38129090657](https://github.com/dbrckk/zero-to-empire/actions/runs/38129090657) **SUCCESS** ; [Android CI 38129090659](https://github.com/dbrckk/zero-to-empire/actions/runs/38129090659) **SUCCESS** ; Repository Standards [38129091329](https://github.com/dbrckk/zero-to-empire/actions/runs/38129091329) **SUCCESS**.
- **Correction de la navigation :** le bouton Daylight stage est vérifié entièrement visible avant clic. La relance montre `CHARACTER_PREVIEW_DAYLIGHT_BUTTON_FULLY_VISIBLE=1`, puis la bascule et le retour nuit fonctionnent (`CHARACTER_PREVIEW_DAY_NIGHT_CONTRAST_PASS=1`).
- **Preuve exigée du corps entier :** `CHARACTER_PREVIEW_FULL_BODY_PANELS=<ACTION>:NIGHT+DAY` pour chacune des six actions IDLE, WALK, WORK, CARRY, REPAIR et CELEBRATE. Le script sonde les véritables fonds de scène bien en dessous de la position des chaussures, et ne peut plus confondre la barre de navigation Android avec le pied du personnage.
- **Inspection visuelle des six PNG réels :** contrairement à l'ancienne galerie tronquée, la nouvelle rangée TECH à 42 dp montre maintenant tête, corps, **deux jambes/chaussures et ombre de contact** dans le panneau de nuit pour les six actions. Les panneaux sont cadrés au même endroit et sont issus de l'émulateur Android, non d'un rendu généré directement sur PC. Les effets et les accessoires restent distincts ; l'évaluation qualitative de la démarche n'est pas déduite du succès automatique.
- **Différenciation en situation de jeu :** le script imprime `CHARACTER_PREVIEW_ALL_SIX_DISTINCT_GAME_SCALE_PASS=1` après comparaisons de pixels entre les quinze paires d'actions. L'écart minimum observé est `IDLE/WORK:413` pixels au seuil de l'audit ; ce nombre prouve uniquement une différence de rendu, **pas** une reconnaissance immédiate par un joueur.
- **Prochain défaut artistique prioritaire :** renforcer la séparation jambe arrière/jambe avant sur WALK et CARRY, puis les gestes mains/équipement pour WORK et REPAIR à 39–42 dp, avec vérification de l'animation complète (pas seulement une frame). Le rig reste une série de **candidats non approuvés**, sans écrasement des assets strict DONE existants.
- **Compte vérifié : 216/235 strict DONE**. Aucune approbation n'a été accordée sur ces seules preuves techniques.

## WALK / CARRY : décalage de profondeur des chaussures — 2026-10-11

- Rig de revue : commit [947817c](https://github.com/dbrckk/zero-to-empire/commit/947817c763980261d7b2744f1a8fe78d6af76b9d) ; le pied arrière des actions WALK et CARRY est décalé de **22 px dans la source 512 px**, sans modifier la hauteur de semelle ni les phases d'appui. La cible du genou suit la nouvelle coordonnée (IK), plutôt que déplacer l'image de la chaussure de façon déconnectée. Les quatre autres actions et les masters officiels sont inchangés.
- Les premiers contrôles ont détecté des assertions historiques contradictoires avec ce nouveau décalage et une comparaison flottante trop stricte ; ces contrôles ont été corrigés en conservant les vérifications de contact au sol et d'allonge du genou.
- Les pipelines [Six modular TECH animations 38131878117](https://github.com/dbrckk/zero-to-empire/actions/runs/38131878117) et [staging canonique 38131900689](https://github.com/dbrckk/zero-to-empire/actions/runs/38131900689) sont **SUCCESS**. La planche WALK commence maintenant par SHA-256 `81e8ad1879e3`, CARRY par `0841d2befbf1` ; le rapport `review-report.json` garde les drapeaux de revue.
- Comparaison de vrais atlases de revue avant/après, à sources communes : environ **13 355 pixels modifiés pour WALK** et **13 299 pour CARRY** (seuil de différence RGBA supérieur à 5, environ 1,27 % de chacun des atlas 1024×1024). La modification est localisée aux deux actions de marche, sans altération de la couleur du costume.
- **Observation des jambes agrandies et à 96 px :** la trajectoire arrière devient un peu plus latérale dans plusieurs images, mais l'occlusion à l'instant où les pieds se croisent subsiste ; la série de huit frames conserve **six frames signalées ambiguës** par le détecteur inférieur (`LOWER_LIMB_STRUCTURE_UNVERIFIED`). Les chiffres ne permettent donc pas de dire que la marche est strictement approuvée ou irréprochable.
- L'APK de revue qui incorpore ces nouveaux SHA est suivi par la [CI Android 38131947157](https://github.com/dbrckk/zero-to-empire/actions/runs/38131947157). Ne pas confondre ses résultats avec la revue humaine de la fluidité et de la perspective.
- **Reste à résoudre :** lisibilité de la jambe arrière à 39–42 dp pendant le croisement, perspective de profil versus le décor de ville, et vrais contacts poids/sol. Aucun statut `strict_status` n'est modifié : **216/235 DONE**.

## Planches sources reproductibles et contraste 42 px — 2026-10-11

- **Nouveau générateur sans promotion** : `tools/sprites/build_tech_review_board.py`, exécuté automatiquement par `.github/workflows/tech-canonical-review-stage.yml` après l'export des six planches TECH. Il ne lit que `art/production/character-rig-review-candidates/review-report.json` et les six atlas PNG, et refuse un rapport comportant une approbation sémantique automatique.
- **Preuve CI** : [TECH canonical review staging 38133713680](https://github.com/dbrckk/zero-to-empire/actions/runs/38133713680), **SUCCESS** avec `TECH_REVIEW_TRUE_SOURCE_PREVIEW_PASS=6 STRICT_PROMOTION=0` et `CANONICAL_REVIEW_STAGE_PASS=6 STRICT_DONE_UNCHANGED=1`.
- L'artefact `tech-six-canonical-review-not-approved` contient désormais `build/tech-review-visual-evidence/tech-review-true-source-board.png` et `build/tech-review-visual-evidence/tech-review-true-source-motion.gif`. Il montre les six identités, quatre échantillons de frames par action, ainsi que les mêmes PNG sur fonds clair/sombre.
- **Distinction essentielle des sources** : ces deux fichiers sont des prévisualisations recréées à partir des **vrais PNG du dépôt**, **pas** des captures d'écran Android. Les maquettes graphiques générées par IA dans le chat sont des exemples de direction artistique et **ne servent jamais de preuves CI ni d'assets validés**.
- La dimension **42 px** du script désigne une taille en pixels physiques pour le diagnostic conservateur ; elle n'est **pas équivalente à 42 dp** sur un Android dont la densité d'écran est supérieure à 1. Pour juger les 39–42 dp effectivement affichés par Compose, utiliser séparément les preuves de l'émulateur Android.
- Sur WALK et CARRY, l'audit `LOWER_LIMB_STRUCTURE_UNVERIFIED` reste à **six images sur huit**. Le détecteur observe une silhouette inférieure potentiellement fusionnée, mais ne sait pas distinguer à lui seul le pied levé durant une phase de balancement d'une véritable fusion de pieds : il s'agit d'un **risque à examiner visuellement**, jamais d'un échec de contact avéré ni d'une approbation automatique.
- **Décision** : ne pas modifier les masters, les atlas WebP de production ni le statut officiel sur la base de ces prévisualisations ; conserver **216/235 strict DONE** jusqu'à revue sémantique confirmée et CI Android correspondante.
