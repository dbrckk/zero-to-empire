# LOG / ENG — quatrième vague Kaggle, revue visuelle et causes de rejet

**Vague GPU :** [38201875119](https://github.com/dbrckk/zero-to-empire/actions/runs/38201875119)  
**Collecteur et artefact :** [38220177038](https://github.com/dbrckk/zero-to-empire/actions/runs/38220177038) → `kaggle-async-character-batch`  
**Jeton :** `38201851009`  
**Revue :** 12 octobre 2026 (UTC)

L'analyse a comparé les frames 256 × 256 réelles, les agrandissements des
visages/casques et le rapport du producteur. **Aucune promotion stricte.**

| Asset | Résultat technique | Décision sémantique |
|---|---|---|
| `CHR-LOG-IDLE` | CANDIDATE, 6 frames, QA PASS | Image de référence de contexte seulement. Casque, visage et uniforme plus stables, mais aucun gain `strict_status` et pas de famille LOG utilisable. |
| `CHR-LOG-WALK` | REJECT | Déplacement des jambes trop faible : `lower-motion=0.109`. |
| `CHR-LOG-WORK` | CANDIDATE, 10 frames, QA PASS | **REJECT** : outil flottant/écran bleu qui change de taille, cadre et visage modifiés, frame 5 avec personnage nettement raccourci (`175/218` px de haut). |
| `CHR-LOG-CARRY` | REJECT | Animation trop immobile : `mean-change=0.065<0.120`. |
| `CHR-LOG-REPAIR` | CANDIDATE, 10 frames, QA PASS | **REJECT** : casque, visage, uniforme, écran et fils changent d'une frame à l'autre, absence d'interaction de réparation stable. |
| `CHR-LOG-CELEB` | CANDIDATE, 8 frames, QA PASS | **REJECT** : sept positions essentiellement neutres, ajout brusque de rayons dorés sur la dernière image ; ce n'est pas une célébration animée. |
| `CHR-ENG-IDLE` | REJECT | **Blocage technique excessif identifié** : `idle-too-static mean-change=0.010<0.025`. La respiration subtile n'exige pas une grande différence de silhouette. |
| `CHR-ENG-WALK` | REJECT | Non produit car l'IDLE ENG de la même vague a été rejeté. |
| `CHR-ENG-CARRY` | REJECT | Non produit car l'IDLE ENG de la même vague a été rejeté. |
| `CHR-ENG-CELEB` | REJECT | Non produit car l'IDLE ENG de la même vague a été rejeté. |

## Corrections livrées après examen

- `tools/sprites/character_semantic_gate.py` : `idle_visual_activity` détecte
  les variations réelles de respiration ou de clignement sans imposer des
  déplacements excessifs, et `FRAME_SCALE_COLLAPSE_RISK` bloque une unique
  frame de travail anormalement raccourcie.
- `tools/sprites/kaggle_character_sheet_factory_v1.py` : action `IDLE`
  désormais acceptée en cas de respiration subtile ou de changement de pixels
  pertinent ; refus maintenu des copies identiques figées. Les contrôles
  rigoureux de marche, portage et célébration restent distincts.
- `tools/sprites/test_character_semantic_gate.py` et
  `tools/assets/test_workflow_policy.py` : régressions explicites pour
  clignement discret, sprites parfaitement figés et frame tronquée.
- Collecteur Kaggle : plafond de détection d'absence de réponse adapté à
  **600 minutes pour les grands lots** et **420 minutes pour les autres**,
  afin de ne pas supprimer des résultats calculés par un GPU encore actif.

**Portée** : ces changements influencent les *futures* soumissions. La
vague suivante `38220241414`, soumise avant eux, ne peut pas les adopter
rétroactivement.

La revue technique et visuelle ne modifie pas automatiquement le registre
canonique. À cette étape, `strict_status == DONE` : **219/235**, avec
**16 assets à finaliser**.
