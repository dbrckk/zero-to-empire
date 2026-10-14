# Tester les personnages originaux sur Android — APK de revue isolé

Ce parcours sert exclusivement à **voir et tester les 18 atlas de personnages créés dans ce dépôt**. Il ne remplace aucun asset de production et ne change pas le compteur strict `DONE`.

## Télécharger et lancer sur Android (sans ordinateur)

1. Ouvrir [GitHub Actions — Local Original Characters Android Review APK](../../.github/workflows/local-original-character-android-preview.yml) ou `https://github.com/dbrckk/zero-to-empire/actions/workflows/local-original-character-android-preview.yml`.
2. Sélectionner la **dernière exécution réussie** dont le manifeste `provenance.json` contient `"application_id": "com.zerotoempire.game.originalreview"`.
3. Sous **Artifacts**, télécharger `zero-to-empire-local-original-review-debug-apk-not-approved` (une connexion GitHub peut être nécessaire).
4. Décompresser le ZIP avec l'application de fichiers Android, puis lancer `app/build/outputs/apk/debug/app-debug.apk`.
5. Autoriser ponctuellement l'installation depuis le navigateur ou gestionnaire de fichiers utilisé, uniquement si l'APK provient bien de cette exécution GitHub. Cette version est une compilation **debug de revue**, pas une version Play Store.
6. Ouvrir l'icône **Animation QA**. La galerie permet de sélectionner OPERATOR, TECHNICIAN, LOGISTICS, ENGINEER et chaque action : IDLE, WALK, WORK, CARRY, REPAIR, CELEBRATE. Comparer les animations de jour et de nuit, les silhouettes à taille réelle et l'enchaînement frame par frame.

L'application de revue porte le package **`com.zerotoempire.game.originalreview`**, distinct de l'application habituelle `com.zerotoempire.game`. Ne pas installer de vieux APK de revue utilisant encore le package de production, car ils peuvent entrer en conflit avec une installation existante.

## Ce qui est construit et ce qui ne l'est pas

La CI copie temporairement **18 PNG sources**, issus de `art/incoming/chatgpt-original/candidates/`, puis les transforme en WebP lossless pour le même moteur d'animation Android. Les 150 SVG éditables et les GIF restent dans le dépôt. Le manifeste `provenance.json` conserve les SHA-256 exacts de chaque candidat, de chaque conversion et de l'APK.

La galerie reflète les positions et tailles réelles du rendu de personnages du jeu, mais elle ne prouve pas à elle seule leur qualité esthétique. Il reste nécessaire de vérifier les gestes, les contacts main/outil, les transitions de boucle, la lisibilité à 35–46 dp, le contraste et la cohérence entre métiers.

**Interdit dans cette étape :** modifier `art/production/master-asset-queue.json`, remplacer les ressources finales validées dans un commit, ou déclarer `strict_status=DONE` sur la base d'une simple compilation, d'un GIF ou d'une métrique technique.

## Reproduire

Depuis le dépôt, la génération locale reste déterministe :

```bash
python -m pip install Pillow==11.3.0 CairoSVG==2.7.1
python tools/sprites/render_chatgpt_originals.py --output-dir art/incoming/chatgpt-original --save-svg
python tools/sprites/render_original_character_previews.py --output-dir art/incoming/chatgpt-original
```

La construction de la variante Android de revue se fait dans une **copie éphémère** par la CI avec `gradle assembleDebug -PLOCAL_ORIGINAL_CHARACTER_REVIEW=true`. Sans cette propriété, les builds Android normaux conservent leur identifiant et ne prennent pas les candidats en lieu et place des textures approuvées.
