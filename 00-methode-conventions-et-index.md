# Méthode, conventions et index

> **Projet maieutique** (voir le skill `maieutique`). À lire en premier, avec `intention-de-l-auteur.md`, `journal-des-decisions.md` et `glossaire.md`.

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
| `faisabilite` | L'examen des obstacles juridiques, fiscaux, techniques ou budgétaires, et des solutions (session metamaieutique) |

On ajoutera un type si le besoin apparaît, et on le reportera dans ce tableau.

## Structure de chaque fichier

1. **En-tête** : statut (`brouillon` / `en discussion` / `stabilisé`), date de création, date de dernière mise à jour.
2. **En vigueur** : ce qui vaut aujourd'hui. C'est la section qui prévaut.
3. **Historique du raisonnement** : le cheminement, dont l'ancien « En bref », avec la provenance marquée :
   - **[G]** : dit ou décidé par Guillaume
   - **[C]** : proposé par Claude, pas encore validé
   - **[S]** : appuyé sur une source citée
   - **[C → validé]** : proposé par Claude, validé par Guillaume
   - **[À vérifier]** : un fait ou un chiffre pas encore sourcé
   - **[P]** : une décision prise par procuration (session `metamaieutique`)
4. **Questions ouvertes**
5. **Liens** vers les autres fichiers de notes.

## Identités et marqueurs

> Depuis le 2026-10-04 (décision 76 [ggim]). Les écrits antérieurs gardent leurs anciens marqueurs, qui ne sont pas réécrits : ils sont datés, pas faux.

**Les identités** :
- **`ggim`** : Guillaume Gimenez, l'auteur du projet ;
- **`opus-5.5`** : le modèle `claude-opus-5-5` (Anthropic), qui a tenu la session metamaieutique.

**Les marqueurs des nouveaux écrits** :

| Marqueur | Sens |
|---|---|
| **[ggim]** | Dit ou décidé par Guillaume |
| **[opus-5.5]** | Proposé par l'agent, pas encore validé |
| **[opus-5.5 → ggim]** | Proposé par l'agent, validé par Guillaume |
| **[opus-5.5 as ggim]** | Décidé par procuration au nom de Guillaume (session metamaieutique) |
| **[S]** | Appuyé sur une source citée |
| **[Unverified]** | Un fait ou un chiffre pas encore sourcé |

**La correspondance avec les anciens marqueurs** :

| Ancien | Nouveau |
|---|---|
| [G] | [ggim] |
| [P] | [opus-5.5 as ggim] |
| [C] | un modèle Claude ; pour tout ce qui relève de la session metamaieutique, opus-5.5 |
| [C → validé] | [opus-5.5 → ggim] (pour la session metamaieutique) |
| [À vérifier] | [Unverified] |

## Fichiers hors numérotation

- `intention-de-l-auteur.md` : l'intention, les convictions et les états d'âme de Guillaume, liés au projet. C'est la boussole, et elle est **à lire en premier**.
- `prompt-log.md` : le journal des prompts du mode (c).
- `CLAUDE.md` : déclare le dossier comme projet maieutique.
- `glossaire.md` : les termes du projet et leur sens exact.
- `journal-des-decisions.md` : le journal des décisions structurantes et des changements d'avis, **à tenir à jour à chaque décision**.
- `transcript-session-2026-10-01.md` : le transcript, arrêté le 2026-10-02 (fin des sauvegardes). Il est conservé comme archive.
- Le dossier est versionné avec **git** depuis le 2026-10-02.
- `livrable/` : les livrables. Le projet de loi existe en **v0.1** (exposé des motifs, objet du fichier 17) et en **v0.2** (exposé des motifs aligné sur l'architecture révisée, M9, décision 83). Le **dispositif v0.1** (`loi-jevons-dispositif-v0.1.md`, M10, décision 87) contient le projet de loi ordinaire, le projet de loi organique et une annexe LFSS / loi de finances.
- `outils/` : les scripts de simulation. `sim_v4.py` est la référence depuis M7.

## Index

| Fichier | Type | Statut | En bref |
|---|---|---|---|
| `00-methode-conventions-et-index.md` | — | stabilisé | Ce fichier |
| `01-cadrage-intention-initiale.md` | cadrage | en discussion | But : chômage universel ; livrables : projet de loi Loi Jevons + campagne ; « drastique mais juste » ; Gouvernement porteur |
| `02-cas-inventaire-candidats.md` | cas | brouillon | 12 cas candidats en 3 familles (amorti / refusé / fausse bonne idée), non sourcés |
| `03-cadrage-simulation-tokens-france-vs-masse-salariale.md` | cadrage | brouillon | ~2,5×10¹⁵ tokens FR 2026 vs ~87 M€ (Atos+Capgemini) → ~0,035 €/Mtok |
| `04-hypothese-modalites-assiette-et-collecte.md` | hypothese | en discussion | Accise sur un service, un seul stade, sans déduction ; fournisseur enregistré collecteur, sinon autoliquidation ; revente en suspension ; particuliers hors du champ ; entraînement hors du champ ; secteur public inclus (M2 [P]) |
| `05-hypothese-revenu-universel-musk.md` | hypothese | brouillon | Chômage universel (pas un revenu pour tous) ; paramètres [G] ; besoin net de 16 à 20 Md€ ; M3 : socle versé par une branche de sécurité sociale, complément Unédic, RSA recentralisé, prestation de chômage au sens du règlement 883/2004 |
| `06-decision-titre.md` | decision | stabilisé | « Loi Jevons : financement du chômage universel par la taxe sur l’intelligence artificielle » |
| `07-decision-fin-disclaimer-et-chute.md` | decision | stabilisé | Pour la campagne : disclaimer (tokens au lieu d'un juriste), chute « OH LES GARS! », conversation à 0,2 $ |
| `08-hypothese-sdk-comptage-infalsifiable.md` | hypothese | brouillon | ↺ Obligation de comptage sur le redevable, SDK certifié = voie simplifiée (M2 [P]) ; taux réduit pour l'exécution sur équipement terminal, temporaire, notifié ; recoupements |
| `09-objection-paresse.md` | objection | brouillon | Faits contre l'objection de la paresse (Finlande, Alaska, Mincome…) |
| `10-hypothese-taux-variable-indexe.md` | hypothese | en discussion | Tarif m × P_k par classe (3 classes) ; P_k constaté chaque trimestre ; ↺ m voté chaque année par le Parlement entre 1 et 4 ; plafond 4P (M2 [P]) |
| `11-cadrage-impact-economique.md` | cadrage | brouillon | 10 questions d’impact éco ; double dividende par une fraction versée à l'Unédic en LFSS (M3) ; ↺ **les droits d'abord**, puis le partage une fois le socle cible atteint (75) : double dividende différé, modeste et tardif (80) |
| `12-concept-analogie-carburant.md` | concept | en discussion | IA aussi stratégique que le carburant → accise par unité, taxes ~100 % du prix HT ; limites : externalités, Gilets jaunes, frontière |
| `13-simulation-v2-recettes-50-50.md` | cadrage | brouillon | Taxe 50/50 ≈ CA IA pro France : ~1,3 Md€ 2026 (0,5–3) ; 10 Md€ vers 2029, 50 Md€ vers 2031 (central) ; trajectoire de référence : note 19 |
| `14-simulation-v3-trajectoire-partage.md` | cadrage | brouillon | ↺ Remplacée par la v4 (note 19). Central : plancher seul insuffisant (16 Md€ en 2035) ; avec moteur jusqu’à 4P, chômage universel complet ≈ 2033 (objectif 16 Md€) ; script `outils/sim_v3.py` |
| `15-concept-complementarite-taxe-zucman.md` | concept | stabilisé | Jevons (flux IA) + Zucman (stock) ; Zucman citée dans l’exposé des motifs, hors dispositif |
| `16-cas-selection-et-faits-verifies.md` | cas | stabilisé | 4 cas sourcés (tisserands, quartz, dockers 1960, TRR Suède) + Keynes ; récit refus → sans mécanisme → ça marche ; Loi Jevons = généralisation |
| `17-objection-questions-lecteur-critique.md` | objection | en discussion (liste de suivi) | 80 questions d’un agent lecteur critique sur l'exposé v0.1 ; en M9 : 44 décidées, 30 répondues, 6 ouvertes, toutes rattachées (M10, M11 ou réservée à Guillaume) ; les 10 prioritaires sont fermées |
| `18-faisabilite-obstacles-juridiques-et-architecture.md` | faisabilite | en discussion | Session metamaieutique : 10 obstacles (O1-O10), aucun bloquant restant ; art. 401 (D1) ; m ≥ 1 = 50/50 (D2) ; 4P non confiscatoire (D3) ; affectation arrêtée : branche de sécurité sociale, cliquet LO 111-3-14 (D4, D6) ; règlement 883/2004, RSA, ASS (D6) ; comptes grand public (D7) ; fonds de réserve (D8) ; non-régression RSA/ASS (D9) ; condition de séjour (D10) ; territorialité, IA locale, notification (D11) ; assiette technique et contrôle (D12) ; champ révisé et chômage universel (D13) ; **guide de reprise (F)** ; suivi des 20 questions (E) ; plan renuméroté (M9 à M15) ; règle d'emploi et scénario bas (D13.8) ; état à la fin de M7 |
| `19-simulation-v4-architecture-revisee.md` | cadrage | en discussion | Simulation v4 (`outils/sim_v4.py`) : 2,6 Md€ en 2028 ; socle ouvert en 2031 ; droits d'abord (75), ouverture sur trois ans (78), m ≤ 2 après la cible (79), indexation (80) : cible en 2034 avec m = 3, vers 2038 avec m ≤ 2 (central) ; baisse des cotisations de 0,1-0,2 pt en 2040 ; scénario bas non financé par la taxe seule (contribution d'équilibre) ; variantes étudiants et patrimoine |
