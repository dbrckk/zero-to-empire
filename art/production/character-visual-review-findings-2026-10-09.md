# Zero to Empire — audit visuel des 19 sprites CHR canoniques

**Décision : aucun nouveau strict DONE.** Contrôle humain/visuel assisté sur la
planche des 19 PNG originaux et inspection directe de plusieurs sprites 1024×1024.
Les tests de format/alpha ne démontrent ni une identité cohérente ni une animation.

## Défauts constatés et correction demandée

| Asset | Problème visuel observé | Correctif nécessaire |
|---|---|---|
| CHR-TECH-WALK | Visages et nuances de tenue cyan variables, perspectives changeantes | Identité ancrée, 8 poses d'une seule personne et pieds fixes |
| CHR-OP-WALK | Casque présent mais visage, vêtements et caméra changent entre les cellules | Un seul ouvrier; alternance des appuis sans changement d'identité |
| CHR-LOG-WALK | Apparences multiples; image à plusieurs personnes | Un logisticien unique, palette orange cohérente |
| CHR-ENG-WALK | Costume et silhouette varient, certaines vues se retournent | Caméra 3/4 fixe et ingénieur stable |
| CHR-OP-CARRY | Caisse non maintenue par les deux mains sur tout le cycle | Une caisse unique, poignées contrôlées image par image |
| CHR-LOG-CARRY | Première rangée : bustes, deuxième rangée : jambes, pas d'images de portage complètes | Recréer 8 images autonomes entières avec caisse identique |
| CHR-ENG-CARRY | Casques/visages séparés des parties inférieures, aucune caisse stable | Recréer 8 images entières et imposer deux prises de main |
| CHR-TECH-CARRY | Corps fragmenté en vêtements/jambes, non exploitable comme animation | Générer une pose entière par frame depuis une identité verrouillée |
| CHR-OP-WORK | Tenue/outil variables; cellule avec plusieurs personnes | Un seul personnage, même outil et contact main/outil explicite |
| CHR-LOG-WORK | Perspectives et morphologies variables; outils incohérents | Même ouvrier et outil lié à la main |
| CHR-ENG-WORK | Visages et vêtements différents, la plupart des poses ne travaillent pas | Une identité d'ingénieur et interaction visible avec un dispositif |
| CHR-TECH-WORK | Torses en première rangée, jambes séparées, portraits sans action | Abandonner l'atlas issu d'un collage; corps complet par cellule |
| CHR-OP-REPAIR | Présence de deux personnes dans des cellules; outil absent/incohérent | Un seul réparateur, point de contact fixé et gestes visibles |
| CHR-LOG-REPAIR | Plusieurs personnes et costumes différents selon les images | Un logisticien unique, outil de réparation identifiable |
| CHR-ENG-REPAIR | Identité et équipement variables, réparation peu lisible | Outil + contact récurrents et identité constante |
| CHR-ENG-IDLE | Grandes portions de visage/torse découpées dans plusieurs cellules | 6 poses corps entier, respiration sans déplacement des pieds |
| CHR-OP-CELEB | Sujets/tenues variables; vraie célébration absente | Une identité, mouvement de bras ascendant explicite |
| CHR-LOG-CELEB | Portrait agrandi puis découpé en cellules | Corps entier unique, célébration de 8 poses |
| CHR-ENG-CELEB | Visages et fragments répartis entre cases; pas de célébration | Corps entier, même ingénieur et animation claire |

## Causes racines et remédiations déjà engagées

1. L'ancien générateur demandait une **planche 4×4 entière en une requête** ;
   l'image obtenue ne contenait pas forcément 16 poses indépendantes.
   Découper cet ensemble produisait des bustes et jambes séparés.
2. Pour IDLE/WORK/CARRY/CELEB, la génération a été remplacée par
   **une requête d'image par pose complète** ; WALK/REPAIR disposaient déjà
   d'un chemin image-par-image.
3. Un filtre supplémentaire signale des silhouettes de portrait,
   des changements brutaux de palette et les incohérences d'échelle.
   Il **ne certifie jamais une réussite sémantique**.
4. Première régénération contrôlée : `CHR-LOG-CARRY`. Les anciennes images
   ne doivent pas être supprimées ni remplacer un asset déjà validé.

## Condition pour passer strict DONE

Une validation exige la revue de chaque frame **à l'échelle du jeu et en
animation**, des mains/accessoires, de l'identité/caméra, des bords
transparents et des transitions de cycle, ainsi que la provenance de
l'image régénérée. La réussite des tests géométriques seuls n'autorise
aucune promotion. **Compteur de départ : 216/235.**
