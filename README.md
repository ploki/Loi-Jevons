# Loi Jevons

*Projet de loi relatif au financement du chômage universel par une taxe sur l'intelligence artificielle.*

**La Loi Jevons propose un chômage universel, « le chômage comme il devrait être », financé par une taxe sur l'usage professionnel de l'intelligence artificielle.** Le but, c'est le chômage universel : un revenu digne pour celles et ceux qui n'ont pas d'emploi, sans limite de durée et sans obligation de recherche. La taxe en est le moyen, et l'IA l'occasion historique.

Ce dépôt contient le corpus de réflexion et trois livrables : l'exposé des motifs, le dispositif et l'étude d'impact. **C'est un point de départ, pas un texte fini.** Il a été écrit par un auteur seul, avec une IA, en consommant des tokens ; s'il avait été sérieux, il aurait embauché un juriste. Rien n'a encore été relu par un juriste, un économiste ou un spécialiste de la protection sociale : c'est la prochaine étape.

Le nom est un hommage à William Stanley Jevons. Il ne désigne pas le paradoxe qui porte son nom, même si ce paradoxe travaille pour la loi : plus l'IA devient efficace, plus on l'utilise, et plus l'assiette de la taxe grandit.

---

## Comment ce projet est construit

Le projet est tenu avec le skill [**Maieutics**](https://github.com/ploki/Maieutics), pour Claude. La loi naît d'un **dialogue entre l'auteur et une IA**, selon une méthode maïeutique : l'auteur ne sait pas d'avance tout ce qu'il cherche, et le dialogue sert à le lui faire trouver et formuler. L'IA pose des questions, propose, objecte ; l'auteur tranche.

**Vous pouvez y jouer vous aussi.** Clonez le dépôt (`git clone https://github.com/ploki/Loi-Jevons.git`), installez le skill [Maieutics](https://github.com/ploki/Maieutics), puis ouvrez [Claude Code](https://claude.com/claude-code) dans le dossier et lancez `/maieutics`. Le modèle lit le corpus et fait le point sur le projet ; à vous ensuite de lui poser des questions (pourquoi taxer les octets plutôt que les tokens, comment la taxe échappe à la directive TVA, ce que coûte le chômage universel, que se passe-t-il si l'IA croît peu…) ou de contester ses réponses.

- **Les notes.** Tout ce qui prend de la substance est consigné dans une note (un cadrage, un concept, un cas historique, une hypothèse, une objection, une décision). Chacune s'ouvre sur ce qui vaut aujourd'hui (« En vigueur »), puis l'histoire du raisonnement et les questions ouvertes.
- **Les journaux.** Chaque décision est notée avec sa raison, et chaque changement d'avis y reste visible (`corpus/journal-des-decisions.md`). Chaque message de l'auteur est réécrit et gardé (`corpus/prompt-log.md`). On peut toujours savoir pourquoi le texte est tel qu'il est.
- **Les calculs.** Quand des chiffres apparaissent (recettes, coût du chômage universel, trajectoire de montée en charge), on écrit un script plutôt que de raisonner de tête. Les chiffres de l'étude d'impact viennent de `outils/sim_v4.py`.
- **La session par procuration.** Pour rendre l'idée juridiquement réalisable, une session [`metamaieutics`](https://github.com/ploki/Maieutics) a été menée de façon autonome : l'IA a joué le rôle de l'auteur, d'après un mandat qu'il avait validé, puis lui a remis un rapport (`corpus/rapport-de-retour.md`). Les décisions prises ainsi sont marquées comme telles, et l'auteur peut les défaire.
- **Les relectures.** Des agents neufs, qui n'ont rien écrit, relisent le travail : à l'aveugle, pour voir ce qu'un lecteur comprend des livrables sans le corpus, ou en audit, pour traquer les contradictions.
- **L'élagage.** Les versions dépassées (la simulation v3, l'exposé des motifs v0.1) partent dans `archive/`, gardées pour mémoire du raisonnement.

Chaque affirmation dit de qui elle vient : **[ggim]** l'auteur (ploki sur GitHub), **[opus-5.5]** une proposition de l'IA, **[opus-5.5 → ggim]** une proposition validée par l'auteur, **[opus-5.5 as ggim]** une décision prise par procuration. Les notes plus anciennes utilisent **[G]**, **[C]** et **[P]**. Un chiffre non sourcé est marqué **[Unverified]** ou **[À vérifier]**.

| | |
|---|---|
| `corpus/` | les notes, le glossaire, l'intention de l'auteur, les journaux, le mandat et le rapport de la session par procuration |
| `livrable/` | les livrables |
| `outils/` | les scripts de simulation |
| `archive/` | les versions dépassées |

Pour entrer : `corpus/intention-de-l-auteur.md`, puis `corpus/00-methode-conventions-et-index.md`.

---

## L'idée

- **L'IA est bâtie sur le savoir collectif.** Les modèles ont été entraînés sur ce que l'humanité a écrit, dessiné, enseigné. Il est juste qu'au moins la moitié de la valeur de leur usage revienne au bien commun.
- **L'intelligence est aussi stratégique que le carburant**, si ce n'est plus. Elle mérite d'être taxée dans les mêmes ordres de grandeur.
- **Le volume de données est une mesure juste.** Il est à peu près proportionnel au travail humain remplacé : une image générée à partir d'un prompt de 200 octets, c'est quatre heures de travail pour un illustrateur.
- **Apprendre du passé.** Les tisserands à main, laissés sans rien, et l'horlogerie suisse face au quartz, sans mécanisme collectif, montrent ce que coûte l'absence d'intervention. Les dockers de la côte ouest américaine (1960) et les conseils suédois de sécurité de l'emploi montrent qu'on peut faire financer la transition par ceux qui profitent de l'automatisation. La Loi Jevons généralise ce qui n'a existé que secteur par secteur, et tente de tenir la promesse de Keynes.
- **Des mesures drastiques, mais justes.** On taxe l'IA dans le cloud, dont l'adoption est faite ; on ménage l'IA locale, qui démarre ; on épargne les particuliers.

## La taxe

- **Une accise sur un service**, perçue une seule fois, au stade de l'utilisation professionnelle finale, sans déduction en chaîne. C'est ce qui la tient à l'écart de l'article 401 de la directive TVA.
- **Le champ** : l'utilisation professionnelle en France des modèles d'IA à usage général et des systèmes qui génèrent des contenus de synthèse, traduction et transcription comprises. Les particuliers, l'entraînement des modèles et l'IA non générative sont hors du champ. Le secteur public est dans le champ.
- **L'assiette** : l'octet-équivalent. Un caractère vaut un octet-équivalent ; les images, le son et la vidéo ont leurs unités. Des coefficients par flux : une donnée générée compte 1, une donnée lue 0,25, une donnée en cache 0,025.
- **Le tarif** : m fois le prix moyen de la classe de modèles. Le multiple m est voté chaque année en loi de financement de la sécurité sociale, entre 1 et 4. À m = 1, la moitié du prix payé revient au bien commun.
- **Le redevable** : le fournisseur enregistré collecte ; à défaut, le client autoliquide. Un abattement de 1 000 € de taxe par groupe et par an épargne les petits usages.
- **L'IA locale** : un quart du tarif pendant trois ans, pour l'inférence sur un poste de travail ou un appareil embarqué.

## Le chômage universel

- **Un socle individuel**, versé par une branche de sécurité sociale propre dont la taxe est une recette exclusive. Il s'ouvre au niveau du RSA et monte vers le seuil de pauvreté (environ 1 200 € par mois), à mesure que les recettes le permettent : les droits ne précèdent jamais les recettes.
- **Sans limite de durée, sans obligation de recherche d'emploi** : une inscription suffit, et la formation rémunérée est un droit.
- **Il reprend le RSA et l'ASS**, sans que personne n'y perde. L'Unédic garde un complément lié à l'ancien salaire.
- **Une sortie progressive** de douze mois quand on reprend un emploi, jamais moins favorable que le droit actuel.

## Ce que disent les chiffres

D'après `outils/sim_v4.py`, scénario central, hypothèses en grande partie [Unverified] :

- environ **2,6 Md€** la première année d'application (2028) ;
- le socle ouvert à tous en **2031**, au niveau du RSA ;
- le seuil de pauvreté atteint en **2033** si le Parlement porte temporairement m à 3, en **2037** s'il s'en tient à 2 ;
- une baisse des cotisations chômage modeste et tardive (environ 0,16 point en 2040) : un bénéfice second, pas une promesse ;
- **si l'usage de l'IA croît peu, la taxe seule ne suffit pas** : l'État doit compléter. La taxe Zucman, sur le stock des grandes fortunes, est citée comme complément naturel de la taxe Jevons, qui porte sur le flux de valeur de l'IA.

## Où en est le projet

- **Les livrables** : l'exposé des motifs (v0.2), le dispositif (v0.1 : projet de loi ordinaire, projet de loi organique, article de loi de financement) et l'étude d'impact (v0.1). Ils contiennent encore des contradictions connues entre eux, à trancher.
- **Les obstacles juridiques** examinés (directive TVA, article 34 de la Constitution, affectation de la recette, égalité devant l'impôt, aides d'État, règlement européen de coordination des systèmes de sécurité sociale, OMC) ont chacun une solution proposée. Aucune n'a été validée par un juriste.
- **Les questions ouvertes** : faut-il ouvrir le socle aux étudiants en formation initiale ? le réduire pour les gros revenus du patrimoine ? Elles restent à l'auteur.
- **À venir** : une application de simulation, où l'on pourra changer les paramètres et les règles en temps réel.

Juristes, économistes, spécialistes de la protection sociale : le texte attend vos objections.
