# Rapport de retour : session metamaieutique « Rendre la Loi Jevons réalisable »

- **Statut** : session arrêtée par Guillaume le 2026-10-04, à l'itération 19 sur 30 au maximum
- **Branche** : `metamaieutique/loi-jevons-faisabilite-2026-10-02` (plus de vingt commits au-dessus de `main`)
- **Branche de départ** : `main`
- **Rédigé par** : opus-5.5 / sonnet-5.5 (orchestrateur), à partir des rapports des agents, du journal et du prompt-log

> Ce rapport est un point de départ. **Rien n'a été relu par un juriste, un économiste ou un spécialiste de la protection sociale.** Les analyses juridiques viennent de recherches web faites par des agents. Tout ce qui est marqué « par procuration » est une décision que l'orchestrateur a prise au nom de Guillaume, d'après le mandat. Guillaume peut la défaire.

## 1. Les écarts par rapport aux décisions de Guillaume

Chaque écart sert l'intention ou la rend possible (mandat, § 3). Le journal donne le « pourquoi » de chacun.

| Décision [G] d'origine | Ce qui change | Pourquoi | Journal |
|---|---|---|---|
| **25, 30** : un prix moyen unique, un plancher au prix moyen | Un prix moyen **par classe de modèles** (trois classes, indice calculé par l'INSEE), tarif m × P_k | Garder le « au moins la moitié » vrai pour chaque classe, et rester une accise au regard de l'article 401 de la directive TVA | 39 |
| **26, 30** : un taux qui monte « selon les besoins » par arrêté trimestriel | Le multiple m est **voté chaque année en loi de financement de la sécurité sociale**, entre 1 et 4 ; l'arrêté ne fait que constater l'indice | Article 34 de la Constitution (incompétence négative) | 40 |
| **13, 28** : un SDK de comptage, et « un portable d'entreprise installe le SDK » | L'obligation de comptage pèse sur le **redevable** ; le SDK certifié devient une **voie simplifiée** | Un compteur imposé aux éditeurs exigerait une notification et heurterait le droit de l'Union | 43 |
| **30** : les recettes partagées moitié-moitié après le rodage | **Les droits d'abord** : pendant la montée en charge, tout le surplus va au socle jusqu'à la cible ; le partage moitié-moitié reprend ensuite | « Le vrai but, c'est le chômage universel » ; la baisse des cotisations est un bénéfice second | 75 |
| **30** : l'export « à taux nul » | **Hors du champ, mais déclaré** | Précision de forme, même effet | 52 |
| **31** : « une sortie progressive » | Douze mois, **dégressivité linéaire**, le bénéficiaire reçoit **le plus favorable** entre elle et le droit actuel (RSA et prime d'activité) | Reprendre un travail ne doit jamais rapporter moins qu'aujourd'hui | 72, 96, 98 |
| **31** : « ouvert dès 18 ans » | Le chiffrage de base **exclut les étudiants en formation initiale** (hypothèse de chiffrage seulement) | Ils coûteraient environ 39,5 Md€ de plus par an. **Question ouverte, réservée à Guillaume** | 70 |

Les décisions **9** (le volume de données), **30** (le plafond à 4 fois le prix moyen, l'abattement, les coefficients) et **31** (la fusion avec le RSA et l'ASS) sont maintenues, avec des précisions.

## 2. L'architecture retenue (une page)

- **La taxe** : une imposition de toutes natures, du type accise sur un service, perçue **une seule fois**, sans déduction en chaîne ; la revente se fait en suspension, sur attestation.
- **Le champ** : l'utilisation professionnelle en France des modèles d'IA à usage général et des systèmes qui génèrent des contenus de synthèse, traduction et transcription comprises. Les particuliers, l'entraînement et l'IA non générative sont hors du champ. Le secteur public est dans le champ.
- **L'assiette** : l'octet-équivalent (un caractère vaut un octet-équivalent), avec des coefficients par type de contenu et par flux (généré 1, lu 0,25, en cache 0,025), fixés par la loi.
- **Le tarif** : m × prix moyen de la classe. Le multiple m est voté en LFSS entre 1 et 4, avec une justification renforcée au-delà de 2. Abattement de 1 000 € de taxe par groupe et par an.
- **Le redevable** : le fournisseur enregistré collecte ; à défaut, le client autoliquide. Une règle ferme la faille des comptes grand public sans taxer les particuliers.
- **L'IA locale** : un quart du tarif pendant trois ans, prolongeable jusqu'à cinq ans par la LFSS. Toute la taxe n'entre en vigueur qu'après la décision de la Commission, afin que l'IA locale ne paie jamais le plein tarif.
- **L'affectation** : une **branche de sécurité sociale propre**, créée par une loi organique ; la taxe en est une recette exclusive (art. LO 111-3-14) ; un fonds de réserve de six mois du besoin net ; une fraction pour l'Unédic.
- **Le chômage universel** : un socle individuel visant le seuil de pauvreté, ouvert par phases, **sans que les droits précèdent les recettes** ; le RSA et l'ASS repris avec une garantie de non-régression ; une condition de séjour plus ouverte que celle du RSA.

Les chiffres de référence (cible en 2033 avec m ≤ 3, retour de m à 2 en 2035, baisse des cotisations de 0,16 point en 2040) sont dans la note 19 et l'étude d'impact. Ils sont calculés par `outils/sim_v4.py`. Plusieurs hypothèses sont marquées [Unverified], dont l'indexation à 2 % et les effectifs.

## 3. Les obstacles juridiques

**Levés dans le droit actuel** : l'article 401 de la directive TVA, l'article 34 de la Constitution, l'affectation de la recette (LOLF, LO 111-3-14), l'égalité et le caractère confiscatoire (appui sur la décision 2025-1157 QPC), le compteur imposé, le règlement 883/2004 (le socle est une prestation de chômage), l'OMC et l'AGCS. Le détail est dans la note 18.

**Étape ultérieure** : l'inscription du socle à l'annexe X du règlement 883/2004 exigerait de modifier le règlement.

**Risques moyens qui restent** : l'égalité devant l'impôt, la territorialité, les aides d'État, et la place exacte de la branche dans les dispositions organiques de la LFSS.

## 4. Les décisions prises par procuration

Ce sont les décisions **37 à 109** du journal, marquées `[P]` puis `[opus-5.5 as ggim]`, chacune avec son pourquoi. Les plus structurantes sont dans le tableau du § 1 et dans l'architecture du § 2.

## 5. Les hésitations : où je ne suis pas sûr d'avoir bien représenté Guillaume

**À lire en premier.**

1. **La dégressivité dans les douze mois** (décisions 98 et 104). Elle explique une grande part du gain de trajectoire, et elle touche la décision 31 [G].
2. **m jusqu'à 3** pendant la montée en charge (décisions 84 et 107). Cela dépasse le repère des deux tiers du coût pendant deux ans. Ce repère est lui-même une décision par procuration (51).
3. **L'entrée en vigueur subordonnée à la Commission** (décision 103, note 18 D11 bis). Si la Commission ouvre la procédure formelle, toute la recette est retardée, y compris le calendrier de 2028. J'ai préféré protéger l'IA locale, d'après « ménager ce qui démarre », mais c'est un vrai coût.
4. **La baisse des cotisations devient modeste et tardive** (environ 0,16 point en 2040). La décision 30 [G] faisait du double dividende un argument central. L'exposé le dit honnêtement, mais Guillaume voudra peut-être le défendre autrement.
5. **L'abattement de 1 000 €** et les montants de sanction sont des valeurs que j'ai proposées. Je n'ai pas de source.
6. **Le changement de modèle en cours de session.** À la demande de Guillaume, qui consommait beaucoup de tokens, l'orchestrateur est passé à un modèle plus petit et les derniers agents (lecture à l'aveugle) aussi. Les analyses de fond datent d'avant ce changement.

## 6. Les questions laissées ouvertes, et la raison de l'arrêt

**Réservées à Guillaume** (elles touchent son intention) : les étudiants en formation initiale (décision 70) et la réduction du socle pour les gros revenus du patrimoine (décision 71), question 50 du fichier 17. Les livrables les présentent comme des options ouvertes au débat.

**Chantiers notés par Guillaume** :
- étudier l'effet de la mesure par la consommation (TVA, achats de biens et services), **tranche d'âge par tranche d'âge**, dont les jeunes en formation initiale chez leurs parents (décision 110) ;
- **une application en Rust**, « à un moment », pour simuler la mesure sur tous les indicateurs, avec changement des paramètres et des conditions en temps réel. Des données seront nécessaires (décisions 111 et 113).

**Non traité** :
- les **97 questions et 20 contradictions** du lecteur aveugle (note 21) ne sont pas classées ;
- trois contradictions entre les livrables restent à trancher : le montant d'ouverture du socle (650 ou 839 €), le multiple fixé à 1 pendant trois ans, et la baisse des cotisations « jamais en recul » face à sa suspension en cas de déficit ;
- la question 6 (le montant des docks en euros actuels, sans source) et les questions 54, 66 et 72 du fichier 17, partiellement traitées.

**Raison de l'arrêt** : Guillaume a demandé l'arrêt à l'itération 19 sur 30, après la confrontation à l'aveugle, pour faire le point avec moi. Aucun obstacle juridique bloquant connu ne reste sans solution.

## 7. Ce qu'il faut relire en premier

1. `intention-de-l-auteur.md`, pour juger si les écarts du § 1 la respectent.
2. Les hésitations du § 5, puis les décisions 98 à 109 du journal.
3. La note 18, section « En vigueur » et section F (guide de reprise).
4. Les trois livrables dans `livrable/` : l'exposé des motifs v0.2, le dispositif v0.1, l'étude d'impact v0.1. L'exposé v0.1 est conservé tel quel.

## 8. Ce qu'il faut faire relire par un expert

- Un juriste en droit public et en droit de l'Union : la confiscation et les impositions comportementales (note 18, D3), la coordination européenne et les frontaliers (D6), le RGPD (D7), la procédure de notification (D11 bis), le texte exact des articles 3 et 50 du règlement sur l'IA, les 87 marques « à vérifier » du dispositif.
- Un économiste : l'indexation à 2 %, l'élasticité, les effectifs de la garantie familiale et de la sortie progressive.
- Un spécialiste de la protection sociale et des finances locales : la reprise du RSA et de l'ASS, la compensation aux départements.

## 9. Comment décider

C'est Guillaume qui décide. **Rien n'a été fusionné.**

- **Voir les différences** : `git diff main..metamaieutique/loi-jevons-faisabilite-2026-10-02`
- **Tout garder** : depuis le dossier principal (`/home/ggim/Documents/Jevons`), `git merge metamaieutique/loi-jevons-faisabilite-2026-10-02`. **Il y aura deux conflits**, dans `journal-des-decisions.md` et `prompt-log.md`, parce que `main` a reçu deux commits (itérations 6 et 7) qui ajoutent des lignes aux mêmes endroits. Il faut garder les deux côtés.
- **Garder une partie** : récupérer seulement certains fichiers, par exemple `git checkout metamaieutique/loi-jevons-faisabilite-2026-10-02 -- livrable/ outils/`.
- **Jeter la branche** : `git branch -D metamaieutique/loi-jevons-faisabilite-2026-10-02`
- **Supprimer le dossier de travail** (après avoir décidé) : `git worktree remove /home/ggim/Documents/Jevons-meta`
