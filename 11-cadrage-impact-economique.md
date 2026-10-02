# Cadrage : impact économique (volet de l'étude d'impact)

- **Statut** : brouillon
- **Créé le** : 2026-10-02
- **Dernière mise à jour** : 2026-10-02 (session metamaieutique, M3)


## En vigueur

- **Le double dividende est un argument central** : la taxe finance le chômage universel et permet de baisser les cotisations chômage sur les salaires.
- **Utilisation des recettes** : de 2026 à 2028, le fonds de réserve et la formation rémunérée ; ensuite, un **partage moitié-moitié** entre l'extension des droits et la baisse des cotisations.
- **Ordre de grandeur** : 1 point de cotisation ≈ 11 à 12 Md€ [Déduit, à vérifier].
- **L'objection de Summers** et les réponses : on taxe l'IA, on assume. L'adoption est mûre dans le cloud ; l'IA locale démarre.
- **Questions ouvertes** (fichier 17) : qui paie réellement la taxe, la compétitivité, l'effet sur les PME et sur l'industrie française.
- **Affectation (M3, décision 49 [P])** : le double dividende passe par une **fraction de la taxe versée à l'Unédic en LFSS**, en compensation de la baisse des contributions patronales, sur le modèle de la CSG versée à l'Unédic.
- **Ordre d'emploi des recettes [C, à valider]** : une interprétation de la décision 30 [G], conforme au script `sim_v3.py`. Les recettes financent d'abord les **droits déjà ouverts** ; le **surplus** est ensuite partagé moitié-moitié entre l'extension des droits et la baisse des cotisations. En cas de retournement, les droits passent avant la baisse des cotisations (Q62, Q65). Quand la contribution patronale atteint zéro (Q64), le surplus va au fonds de réserve, et m peut être abaissé.

---

## Historique du raisonnement

> Les sections suivantes retracent le raisonnement. En cas de divergence, la section « En vigueur » prévaut.

### Session metamaieutique, M3 (2026-10-02)

- **[P] Décision 49** : une fraction de la taxe va à l'Unédic pour la baisse des cotisations. **[C]** L'ordre d'emploi des recettes est proposé (note 18, D8).

### En bref

Ce volet de l'étude d'impact analyse les effets économiques de la taxe et du chômage universel. Pour l'instant, ce n'est qu'une liste de questions : rien n'est encore documenté.

### Ce qui a été posé

- **[G]** Il faut traiter un volet sur l'impact économique.

### Le double dividende : un argument central

- **[G]** Le double dividende est **important**. C'est un argument central de l'exposé des motifs.
- **[C] Le principe** :
  - **1ᵉʳ dividende** : la taxe finance le chômage universel.
  - **2ᵉ dividende** : elle permet de baisser les cotisations chômage sur les salaires. Le travail humain devient moins cher, et le financement passe **du travail à la machine**.
- **[S] Les chiffres** :
  - La contribution patronale d'assurance chômage est de **4,00 %** du salaire brut depuis le 1ᵉʳ mai 2025. Avec le bonus-malus, elle varie de 2,95 % à 5,00 %.
  - Les salariés ne cotisent plus depuis 2018 : leur part a été remplacée par la CSG. **[À vérifier]**
- **[C] Ordre de grandeur** :
  - La contribution de l'Unédic à France Travail (5,2 Md€ en 2026) représente 11 % des contributions de l'année N-2. Les contributions s'élèvent donc à environ **47 Md€**.
  - **1 point de cotisation représente donc environ 11 à 12 Md€.**
  - Conséquence : **environ 11 Md€ de taxe sur l'IA permettent de baisser la cotisation chômage d'environ 1 point**. **[Déduit, à vérifier]**
- **[G] Décision (point 6 de la relecture du corpus) : comment utiliser les recettes.**
  1. **Pendant le rodage (2026-2028)** : les recettes vont au **fonds de réserve** et à la **formation rémunérée**.
  2. **Ensuite** : chaque euro au-delà de ce qui est nécessaire au fonds de réserve est **partagé moitié-moitié**. Une moitié étend les droits au chômage universel, l'autre baisse les cotisations chômage sur les salaires.
  3. **L'objectif de long terme est assumé** : la taxe remplace une grande partie des cotisations chômage. Il faut environ 50 Md€ pour le chômage universel complet, plus environ 11 Md€ par point de cotisation supprimé.
  - **L'intérêt** : un gain visible tout de suite pour les deux publics, les chômeurs et les employeurs.
  - Cette décision remplace l'ancienne proposition d'arbitrage, qui hésitait entre plusieurs ordres de priorité.
- **[C] Une critique à anticiper** : la notion vient de la fiscalité environnementale (Pearce, 1991). La version forte du double dividende a été contestée (Goulder, 1995), car la nouvelle taxe crée elle-même des distorsions qui peuvent annuler le gain. Pour y répondre, on peut montrer qu'une taxe par unité, sur une assiette qui croît, distord peu. **[À vérifier]**

### L'objection de Summers

- **[S]** Contexte : Bill Gates propose en février 2017 de taxer le robot qui remplace un salarié au même niveau que le salaire remplacé. Larry Summers lui répond dans le *Washington Post* le 5 mars 2017 : l'idée est « profondément malavisée ».
- **[S]** Ses arguments :
  1. Les robots **créent de la richesse**, et il est illogique de taxer ce qui rend plus productif. Ce serait du « **protectionnisme contre le progrès** ».
  2. On a tort de **désigner les robots** comme les destructeurs d'emplois : bien d'autres innovations permettent de produire plus avec moins de travail.
- **[C]** Argument souvent associé, à vérifier dans le texte : il est impossible de définir ce qu'est un « robot ». Un distributeur de billets ? Un traitement de texte ? Une caisse automatique ? Pour aider ceux qui perdent leur emploi, il vaudrait mieux une redistribution générale.
- **[G] Position assumée** :
  - **Le stade de l'adoption est dépassé pour l'IA dans le cloud.** Elle est déjà massivement utilisée, donc la taxe ne freine pas une technologie naissante.
  - **Précision (point 7 de la relecture du corpus)** : l'IA **locale et embarquée** en est encore à ses débuts. C'est pourquoi elle bénéficie d'un **taux réduit pendant une période de lancement** (fichier 08). Les deux positions sont cohérentes : on taxe pleinement ce qui est mûr, on ménage ce qui démarre.
  - On l'assume : **on taxe l'intelligence artificielle**.
- **[C]** Cela répond à l'argument « ne pas taxer une industrie naissante », qui avait du sens en 2017 et n'en a plus en 2026. Le parallèle avec l'automobile tient : les taxes sur le carburant ont surtout augmenté une fois la voiture devenue un bien de masse. **[À vérifier]**
- **[C] Nuance** : l'adoption est massive chez les grandes entreprises, mais peut-être moins avancée dans les PME françaises (chiffres d'Eurostat à vérifier). C'est un argument pour protéger les PME, pas contre la taxe. **Décision (fichier 08)** : pas de franchise, mais un **abattement** par entreprise et un taux réduit pour l'IA locale.
- **[C] Nos réponses** :
  - **La définition.** On ne taxe pas un « robot » mais un **flux mesurable**, des octets ou des tokens traités par un modèle. Reste à définir juridiquement ce qu'est un « modèle d'IA » : le problème n'est pas entièrement résolu, et il faut le dire.
  - **Le protectionnisme.** On ne protège pas un métier, on finance des personnes (voir les fausses bonnes idées du fichier 02). Summers lui-même préconise la redistribution : la taxe en est l'outil de financement.
  - **La productivité.** Le carburant est indispensable à la productivité, et il est pourtant taxé à plus de 100 % de son prix hors taxe (fichier 12). Le double dividende baisse en outre l'impôt sur le travail.
  - **La littérature économique postérieure** va dans notre sens **[À vérifier]** :
    - Acemoglu, Manera et Restrepo (2020) montrent que le système fiscal américain taxe davantage le travail que le capital, ce qui pousse à une automatisation excessive. Corriger cette asymétrie, c'est exactement le double dividende.
    - Guerreiro, Rebelo et Teles (« Should Robots Be Taxed? ») concluent qu'une taxe sur les robots peut être optimale pendant une période de transition.
- **[S] Sources** :
  - Marketplace / larrysummers.com : https://larrysummers.com/2017/04/19/former-treasury-secretary-lawrence-summers-says-taxing-robots-makes-no-sense/
  - Route Fifty : https://www.route-fifty.com/finance/2017/03/bill-gates-idea-robot-tax-called-extremely-misguided/135933
  - Bruegel : https://www.bruegel.org/blog-post/taxing-robots

### Questions à traiter **[C]**

1. **Incidence : qui paie réellement ?** Les fournisseurs d'IA, les entreprises clientes, ou leurs propres clients, par la hausse des prix ? Cela dépend de l'élasticité de la demande.
2. **Adoption de l'IA et productivité.** La taxe freine-t-elle la diffusion de l'IA en France ? C'est l'objection de Summers à la « taxe robots » : taxer l'innovation revient à taxer la productivité.
3. **Coût relatif du travail.** La taxe rend l'IA un peu plus chère par rapport au travail humain. Elle ralentit donc un peu la substitution. Est-ce un effet voulu, ou un effet à neutraliser ?
4. **Baisse du coût du travail, un double dividende possible.** Si la taxe finance une partie de l'assurance chômage, on peut **baisser les cotisations chômage sur les salaires**. Le financement passe du travail à la machine, et l'emploi humain devient moins cher.
5. **Compétitivité et délocalisation.**
   - Le risque : une inférence faite à l'étranger pour éviter la taxe. L'autoliquidation à l'import y répond (fichier 04).
   - L'exonération à l'export donne un avantage aux acteurs français.
6. **L'industrie française de l'IA** (Mistral, centres de données installés en France) : l'effet est-il net positif ou négatif ?
7. **Grandes entreprises et PME.** Le coût de mise en conformité (comptage, SDK) pèse plus lourd sur les petites. Réponse retenue : un abattement, sans franchise (fichier 08).
8. **Effet macroéconomique du chômage universel.**
   - Il soutient la consommation et joue le rôle de **stabilisateur automatique** en cas de crise.
   - Il fluidifie les reconversions.
9. **Finances publiques.**
   - Les recettes et les dépenses, année après année, pendant la montée en charge (fichiers 03 et 10).
   - Ce que l'on économise ailleurs : le RSA, les dépenses de santé (voir Mincome, fichier 09).
10. **Cadre européen.** La compatibilité avec le marché unique, l'AI Act, les règles d'aides d'État, et le précédent de la taxe GAFA. **[À vérifier]**

### Sources

- Unédic, paramètres utiles (juillet 2026) : https://s3.eusc-de-east-1.amazonaws.eu/unedic-eks-prod-cms/2026/07/15/unedic_parametres_utiles_juillet2026-vf_uid_6a5757953d941.pdf
- Éditions Tissot, la baisse de la contribution et le bonus-malus : https://www.editions-tissot.fr/actualite/droit-du-travail/assurance-chomage-la-baisse-de-la-contribution-et-son-impact-sur-le-bonus-malus

### Liens

- [03-cadrage-simulation-tokens-france-vs-masse-salariale.md](03-cadrage-simulation-tokens-france-vs-masse-salariale.md)
- [04-hypothese-modalites-assiette-et-collecte.md](04-hypothese-modalites-assiette-et-collecte.md)
- [10-hypothese-taux-variable-indexe.md](10-hypothese-taux-variable-indexe.md)
