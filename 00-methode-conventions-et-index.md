# Méthode, conventions et index

> Fichier de référence : à relire en premier à chaque reprise de contexte.

## Méthode

- Le travail avance par rounds. Chaque round crée ou met à jour des fichiers de notes.
- Les fichiers numérotés forment un corpus. Quand il est jugé suffisant, on en tire les livrables, dans `livrable/` : le projet de loi, puis la campagne de promotion.
- C'est Guillaume qui décide du fond, de l'angle et de la forme. Claude consigne, structure et documente.

## Nommage des fichiers

`NN-<type>-<sujet>.md`

- `NN` : l'ordre de création uniquement. Il n'a aucune valeur de plan ou de hiérarchie.
- `<type>` : la nature de l'élément de recherche.

| Type | Contenu |
|---|---|
| `cadrage` | Intention, question de recherche, périmètre, public visé |
| `concept` | Notion ou mécanisme (définition, limites) |
| `cas` | Cas historique ou contemporain étudié |
| `source` | Fiche de lecture d'une source précise |
| `hypothese` | Une idée à tester, formulée de façon à pouvoir être contredite |
| `objection` | Un contre-argument et sa discussion |
| `decision` | Un choix acté (angle, titre, exclusions…) |

On ajoutera un type si le besoin apparaît, et on le reportera dans ce tableau.

## Structure de chaque fichier

1. **En-tête** : statut (`brouillon` / `en discussion` / `stabilisé`), date de création, date de dernière mise à jour.
2. **En bref** : trois lignes au maximum, pour qu'on puisse reprendre le contexte sans lire le reste.
3. **Contenu**, avec la provenance marquée :
   - **[G]** : dit ou décidé par Guillaume
   - **[C]** : proposé par Claude, pas encore validé
   - **[S]** : appuyé sur une source citée
   - **[À vérifier]** : un fait ou un chiffre pas encore sourcé
4. **Questions ouvertes**
5. **Liens** vers les autres fichiers de notes.

## Fichiers hors numérotation

- `journal-des-decisions.md` : le journal des décisions structurantes et des changements d'avis, **à tenir à jour à chaque décision**.
- `transcript-session-2026-10-01.md` : le transcript, arrêté le 2026-10-02 (fin des sauvegardes).
- `livrable/` : les livrables.
- `outils/` : les scripts de simulation.

## Index

| Fichier | Type | Statut | En bref |
|---|---|---|---|
| `00-methode-conventions-et-index.md` | — | stabilisé | Ce fichier |
| `01-cadrage-intention-initiale.md` | cadrage | en discussion | But : chômage universel ; livrables : projet de loi Loi Jevons + campagne ; « drastique mais juste » ; Gouvernement porteur |
| `02-cas-inventaire-candidats.md` | cas | brouillon | 12 cas candidats en 3 familles (amorti / refusé / fausse bonne idée), non sourcés |
| `03-cadrage-simulation-tokens-france-vs-masse-salariale.md` | cadrage | brouillon | ~2,5×10¹⁵ tokens FR 2026 vs ~87 M€ (Atos+Capgemini) → ~0,035 €/Mtok |
| `04-hypothese-modalites-assiette-et-collecte.md` | hypothese | en discussion | Taxe génération/lecture/import/export ; compta + déclaration ; particuliers exonérés, usage pro taxé ; ≈ TVA + accises |
| `05-hypothese-revenu-universel-musk.md` | hypothese | brouillon | « Musk a raison » ; chômage universel (pas revenu pour tous) ~50 Md€ ; paramètres à trancher |
| `06-decision-titre.md` | decision | stabilisé | « Loi Jevons : financement du chômage universel par la taxe sur l’intelligence artificielle » |
| `07-decision-fin-disclaimer-et-chute.md` | decision | stabilisé | Pour la campagne : disclaimer (tokens au lieu d'un juriste), chute « OH LES GARS! », conversation à 0,2 $ |
| `08-hypothese-sdk-comptage-infalsifiable.md` | hypothese | brouillon | SDK partout (portables inclus), IA locale/embarquée à taux réduit au lancement ; journal chaîné, recoupements ; NF525 |
| `09-objection-paresse.md` | objection | brouillon | Faits contre l'objection de la paresse (Finlande, Alaska, Mincome…) |
| `10-hypothese-taux-variable-indexe.md` | hypothese | en discussion | 50/50, bien commun, révision trimestrielle, déclaration type TVA ; règle de taux à unifier |
| `11-cadrage-impact-economique.md` | cadrage | brouillon | 10 questions d’impact éco : incidence, adoption, coût du travail (double dividende), compétitivité, PME, macro, UE |
| `12-concept-analogie-carburant.md` | concept | en discussion | IA aussi stratégique que le carburant → accise par unité, taxes ~100 % du prix HT ; limites : externalités, Gilets jaunes, frontière |
| `13-simulation-v2-recettes-50-50.md` | cadrage | brouillon | Taxe 50/50 ≈ CA IA pro France : ~1,3 Md€ 2026 (0,5–3) ; 10 Md€ vers 2029, 50 Md€ vers 2031 (central) |
| `14-simulation-v3-trajectoire-partage.md` | cadrage | brouillon | Central : plancher seul insuffisant (16 Md€ en 2035) ; avec moteur jusqu’à 4P, chômage universel complet ≈ 2031, −2,8 pts de cotisation en 2035 ; script `outils/sim_v3.py` |
| `15-concept-complementarite-taxe-zucman.md` | concept | stabilisé | Jevons (flux IA) + Zucman (stock) ; Zucman citée dans l’exposé des motifs, hors dispositif |
| `16-cas-selection-et-faits-verifies.md` | cas | stabilisé | 4 cas sourcés (tisserands, quartz, dockers 1960, TRR Suède) + Keynes ; récit refus → sans mécanisme → ça marche ; Loi Jevons = généralisation |
| `17-objection-questions-lecteur-critique.md` | objection | en discussion | 80 questions d’un agent lecteur critique ; corpus : 10 R / 50 P / 20 N ; top 10 à régler (dir. TVA art. 401…) ; contradictions exposé ↔ notes |
