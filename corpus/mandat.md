# Mandat : session metamaieutique « Rendre la Loi Jevons réalisable »

- **Statut** : **validé par Guillaume le 2026-10-02** (« je crois que c'est bon »). Le droit de référence est celui du point 4, tel que rédigé. Le soutien du Parlement n'est pas précisé.
- **Rédigé le** : 2026-10-02, par Claude (l'orchestrateur, qui agit par procuration)
- **Branche** : `metamaieutique/loi-jevons-faisabilite-2026-10-02`, dans un worktree séparé, créée à partir de `main`

## 1. Le but de la session

Guillaume n'arrive pas à rendre son idée réalisable. **La session a pour but de la rendre légale et réalisable** : régler, ou rendre possibles, toutes les difficultés juridiques, fiscales, techniques et budgétaires, pour aboutir à un projet de loi qui tienne debout.

**Hypothèse de départ : le Gouvernement soutient pleinement le projet.** Toute la volonté politique et tous les outils légaux dont dispose le Gouvernement sont disponibles. **En revanche, le résultat doit être légal.**

## 2. Ce qui ne change pas : l'intention

La référence est **`intention-de-l-auteur.md`**. **C'est le seul invariant.** Les points suivants ne peuvent pas être abandonnés :

- **le but** : un **chômage universel**, « le chômage comme il devrait être », financé par la valeur de l'IA, dans une logique d'**émancipation** ;
- **la justification** : l'IA est bâtie sur le **savoir collectif**, et une part substantielle de sa valeur (**au moins la moitié** dans l'esprit) revient au bien commun ;
- **le principe** : des mesures **drastiques mais justes**. **On taxe l'IA**, on **épargne les particuliers**, on **ménage ce qui démarre** (l'IA locale et embarquée) ;
- **ce qu'il refuse** : se mettre en avant, les attaques personnelles, et le protectionnisme douanier comme proposition sérieuse ;
- **la posture** : un **point de départ** formel et étayé.

## 3. Ce qui peut changer : tout le reste

Toutes les **modalités** peuvent être revues, **y compris les décisions [G] déjà prises** (le journal, n° 1 à 36), **à une condition : la nouvelle solution sert mieux l'intention ou la rend possible.** Cela concerne notamment :

- **l'assiette** : l'octet-équivalent, les coefficients, le token, ou une autre base ;
- **le redevable** : l'utilisateur, le fournisseur, l'exploitant de capacités de calcul ;
- **la règle de taux** : le plancher, le moteur et le plafond, l'indexation, un barème ;
- **la nature juridique** du prélèvement : un impôt, une taxe affectée, une cotisation, une redevance ;
- **le texte qui le porte** : une loi ordinaire, une loi de finances, une loi de financement de la sécurité sociale, une loi organique ;
- **la territorialité, le comptage, le contrôle et l'abattement** ;
- **les paramètres du chômage universel**, à condition de rester fidèle au but ;
- **le calendrier et la montée en charge**.

Chaque changement est **marqué [P]**, **inscrit au journal** (marqué ↺ si c'est un revirement) et **justifié**, en expliquant pourquoi l'ancienne modalité bloquait et pourquoi la nouvelle respecte l'intention.

## 4. Le cadre juridique (à confirmer, voir la question 1 ci-dessous)

- **Le droit en vigueur** : la Constitution et le bloc de constitutionnalité, le droit de l'Union européenne (dont la directive TVA et les règles sur les aides d'État), les conventions fiscales, les règles de l'OMC et de l'AGCS.
- **Les outils du Gouvernement, tous mobilisables** : le projet de loi, la loi de finances, la loi de financement de la sécurité sociale, la loi organique, les ordonnances, les décrets et les arrêtés, la notification à la Commission européenne, l'expérimentation, la concertation avec les partenaires sociaux et les départements.
- **Si une voie n'est légale qu'au prix d'une évolution du droit de l'Union ou de la Constitution**, le rapport la présente comme une **étape ultérieure**. Le cœur du dispositif doit être **légal dans le droit actuel**.

## 5. Les objectifs

1. **Une note de faisabilité** (une nouvelle note du corpus). Pour chaque obstacle (les 80 questions du fichier 17, en commençant par les 20 non traitées et les 10 prioritaires), elle indique : l'obstacle, la solution juridique ou technique retenue, sa base légale [À vérifier si besoin] et le risque résiduel.
2. **Une architecture révisée** de la taxe et de son affectation, compatible avec le droit de l'Union, notamment l'article 401 de la directive TVA, avec la Constitution (l'égalité devant les charges publiques, l'absence de caractère confiscatoire, l'article 34) et avec les règles budgétaires (la LOLF et la LFSS).
3. **L'exposé des motifs en version 0.2**, aligné sur l'architecture révisée. Les contradictions relevées dans le fichier 17 y sont levées.
4. **Le dispositif en version 0.1** : les articles de loi en forme légistique, organisés en titres. Quand on ne connaît pas encore les numéros d'articles, on les marque [À vérifier].
5. **L'étude d'impact en version 0.1**, avec la trajectoire recalculée si l'architecture change (le script `outils/`).
6. **Une confrontation à l'aveugle de l'ensemble**, centrée sur la légalité, puis la mise à jour de la liste de suivi.

## 6. Les critères qui permettent de dire que c'est atteint

- **Aucun obstacle juridique bloquant connu ne reste sans solution**, ou bien il est explicitement présenté comme une étape ultérieure.
- Les 10 questions prioritaires et les 20 questions non traitées ont le statut « répondue » ou « décidée ».
- Les trois livrables et la note de faisabilité existent. La confrontation à l'aveugle a été faite.
- Tout ce qui s'écarte d'une décision [G] est marqué [P], justifié et inscrit au journal.

## 7. Le cadre de travail

- **Nombre maximal d'itérations** : **30**.
- **Hors mandat** : est hors mandat tout ce qui toucherait à l'**intention**. Je n'y touche pas, je le signale. Le reste fait partie du mandat.
- **Hors périmètre** :
  - la campagne de promotion ;
  - le titre ;
  - toute modification de `intention-de-l-auteur.md`.
- **Le ton** : formel pour les livrables ; concis partout.

## 8. Les interdits absolus

- **Rien n'est publié.**
- **Rien n'est envoyé vers un service extérieur.** La **recherche web en lecture seule est permise**, et même attendue pour vérifier les textes juridiques.
- **On ne touche pas à `main`.**
- **On ne supprime rien de l'historique git.**
- **On ne met jamais en cause une personne nommément.**

## 9. Le retour

`rapport-de-retour.md` est rédigé sur la branche. Il contient :
- **en premier, les écarts par rapport aux décisions [G]**, chacun avec sa justification ;
- l'architecture retenue ;
- les obstacles levés et ceux qui restent ;
- les décisions [P] ;
- les hésitations ;
- ce qu'il faut relire en premier ;
- les commandes git pour comparer, fusionner, garder une partie ou jeter la branche.

C'est Guillaume qui décide de la suite.
