# Revue mobile des 16 personnages — Zero to Empire

Le périmètre de production est de **235 assets** (hors ONB-00). Le paquet
provisoire contient 16 animations de personnages non encore validées ;
**219 assets restent strictement DONE** et ne sont pas affectés.

## Interface disponible sur Android

La dernière page autonome est publiée avec le paquet d'assets :

- **[Revue mobile hors ligne (HTML)](https://github.com/dbrckk/zero-to-empire/releases/download/zte-character-candidates/zte-character-bank-mobile-review.html)**
- [Paquet de 16 atlases PNG (ZIP)](https://github.com/dbrckk/zero-to-empire/releases/download/zte-character-candidates/zte-character-bank-current.zip)
- [Index de provenance et contrôles SHA-256 (JSON)](https://github.com/dbrckk/zero-to-empire/releases/download/zte-character-candidates/zte-character-bank-current.json)

Sur Android, enregistrer le fichier HTML puis l'ouvrir avec le navigateur via
le gestionnaire de fichiers. Tout est embarqué : aucune connexion, API externe,
inscription, PC ni installation Roblox/Android Studio ne sont nécessaires.

## Fonctions

- Sélectionner le rôle (OP, LOG, ENG) puis l'animation.
- Comparer la planche **retenue dans le paquet** à la planche
  **originale éditable** pour le même rôle et la même action.
- Lire les frames de façon synchronisée, mettre en pause, avancer/reculer
  frame par frame et régler la cadence.
- Tester la lisibilité à **42 pixels** de jour et de nuit ; le rendu est une
  simulation HTML, **pas** une preuve de rendu natif Android.
- Voir les avertissements artistiques déjà produits par les contrôles automatiques.
- Ajouter une appréciation locale et exporter un JSON de notes.
  **Ce JSON ne modifie jamais GitHub, le manifeste ou les assets Android.**

## Chaîne de confiance

L'interface est générée par
`tools/sprites/build_character_bank_mobile_review.py` à partir du dernier ZIP
créé par `build_character_candidate_bank.py`. La construction vérifie :

1. Index review-only, unicité des identifiants et noms des fichiers.
2. Intégrité SHA-256 de chaque PNG retenu.
3. Géométrie RGBA 1024 × 1024.
4. Présence de l'original local vérifié techniquement et de ses poses SVG.
5. Conservation du mode **sans promotion automatique**, sans marqueur strict DONE.

La page se reconstruit à chaque mise à jour du paquet ; les créations Kaggle
valides remplacent éventuellement un repli local si leur collecte est
confirmée dans la file canonique. Les risques d'esthétique/animation,
d'intégration Android et de cohérence de direction artistique sont toujours
des tâches distinctes avant une promotion définitive.
