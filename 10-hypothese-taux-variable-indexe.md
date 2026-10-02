# Hypothèse : un taux variable, indexé sur des indicateurs

- **Statut** : en discussion
- **Créé le** : 2026-10-02
- **Dernière mise à jour** : 2026-10-02

## En bref

> Unité retenue : l'**octet-équivalent** (octet × coefficient par type de contenu, fichier 04). Quand ce fichier parle de « token », il faut lire « unité taxable ».

**Règle du taux retenue** : un montant par unité, **au minimum égal au prix moyen** (le plancher 50/50), relevé si le besoin de financement l'exige (besoin ÷ assiette), et **plafonné à 4 fois le prix moyen**. Le montant est révisé tous les trois mois par arrêté, d'après l'indice des prix, avec un lissage. Le surplus éventuel alimente le fonds de réserve et la baisse des cotisations.

## Règle du taux retenue (point 1 de la relecture du corpus)

- **[G] Validé** : une combinaison de trois règles qui se contredisaient jusque-là.
  - **Plancher = le prix moyen** : la taxe vaut au moins 100 % du prix hors taxe, soit le **50/50**. Le bien commun touche toujours au moins la moitié de la valeur.
  - **Le moteur = le besoin de financement** du chômage universel, divisé par l'assiette. Si ce besoin dépasse le plancher, le montant monte. C'est là que jouent les trois enseignements de la section « Le prix du token tend vers zéro » : la part de la taxe dans le prix peut dépasser la moitié sans que l'utilisateur le ressente.
  - **[G] Plafond = 4 fois le prix moyen**, soit au plus 80 % du prix payé taxes comprises.
  - **Le surplus** (quand le plancher rapporte plus que le besoin) alimente le **fonds de réserve** et la **baisse des cotisations sur les salaires** (le double dividende, fichier 11).
  - **Ce qui ne change pas** : la révision trimestrielle par arrêté d'après l'indice des prix, le lissage et la déclaration calquée sur la TVA.
- **Formule** : montant par unité au trimestre T = min( 4 × P, max( P, B ÷ A ) ), lissé.
  - P = le prix moyen du trimestre précédent ;
  - B = le besoin de financement ;
  - A = l'assiette.
- **Formule pour l'exposé des motifs** : *« la moitié de la valeur au minimum, et davantage si la solidarité l'exige »*.
- Les sections ci-dessous, « Principe directeur : 50/50 », « Indicateurs possibles » et « Proposition de synthèse », gardent la trace du raisonnement. **Cette section-ci prévaut.**

## Ce qui a été posé

- **[G]** L'idée : un taux qui fluctue selon des indicateurs extérieurs, par exemple les besoins de financement du programme de chômage universel.

## Principe directeur : 50/50

- **[G]** Une taxe de **100 %**, autrement dit **50 % pour l'exploitant et 50 % pour le bien commun**, dont l'exploitant profite lui-même.
- **[C]** Une taxe de 100 % du prix hors taxe représente la **moitié du prix payé**. La formule « moitié-moitié » est simple et lisible pour l'exposé des motifs.
- **[G]** « Les modèles ont été entraînés sur le savoir collectif » est un argument **très important**. Il doit figurer en bonne place dans l'exposé des motifs.
- **[C]** Ce que l'exploitant tire du bien commun :
  - une main-d'œuvre formée, des infrastructures, la stabilité sociale ;
  - et surtout **des modèles entraînés sur le savoir collectif** : le web public, Wikipédia, les livres, la recherche publique. L'IA est en grande partie bâtie sur ce bien commun, et il est juste qu'une part de sa valeur y retourne.
- **[C]** Comment concilier ce principe avec la taxe par unité :
  - Le principe 50/50 sert à **calibrer le taux de départ** : un montant par unité égal au prix moyen hors taxe au moment où la loi entre en vigueur.
  - Ensuite, le taux suit la formule (besoin ÷ assiette) et ses garde-fous. Comme le prix baisse, la part de la taxe dans le prix **dépassera ensuite 50 %**. Il faut décider si l'on accepte ce dépassement, ou si l'on plafonne la taxe à 100 % du prix hors taxe. Plafonner revient à réintroduire une taxe sur le prix, et donc à perdre l'avantage de la taxe par unité.

- **[G] Décision** : un **montant par token égal au prix moyen**, **révisé régulièrement**. Le principe 50/50 est donc maintenu dans la durée.
- **[C]** Conséquence à assumer : si le montant suit le prix moyen, les recettes valent environ **volume × prix moyen**, c'est-à-dire la **valeur du marché de l'IA en France**, et non plus le seul volume. Les recettes augmentent si la valeur du marché augmente : la baisse du prix doit être plus que compensée par la hausse du volume (effet Jevons). **[À vérifier]**

## Période de révision et de déclaration

- **Le problème** : le prix du token chute très vite. Avec une révision annuelle, le montant de la taxe pourrait valoir plusieurs fois le prix en fin d'année.
- **Le précédent du Livret A** : la loi fixe une formule, le taux est recalculé **chaque semestre** (1ᵉʳ février et 1ᵉʳ août) et publié par arrêté. C'est le modèle le plus proche : la formule est dans la loi, le chiffre dans l'arrêté. Cela respecte l'article 34. **[À vérifier]**
- **Un indice du prix du token calculé à partir des déclarations elles-mêmes** : chaque déclaration indique le volume et le montant facturé, d'où un prix moyen pondéré par les volumes, calculé automatiquement. C'est un intérêt de plus du SDK (fichier 08). Il faut désigner qui publie cet indice : l'INSEE, la DGFiP ou un régulateur.
- **Options de période de révision du montant** :

| Période | Avantage | Inconvénient |
|---|---|---|
| Annuelle (loi de finances) | Simple, prévisible | Trop lente face à la baisse des prix |
| Semestrielle (modèle Livret A) | Précédent solide | Encore un peu lente si le prix est divisé par 10 en un an |
| **Trimestrielle** | Suit le marché de près | Plus de charge pour le fisc ; peu pour les entreprises si tout est automatisé |
| Mensuelle | Colle au prix | Trop de variations, et la conformité se complique |

- **[G] Validé** : une révision **trimestrielle** par arrêté, d'après l'indice du trimestre précédent, avec le lissage et les garde-fous (plancher, plafond, fonds de réserve). On pourra passer au semestriel quand la baisse des prix ralentira.
- **[G] Validé** : une période de déclaration **calquée sur la TVA** (mensuelle pour les grandes entreprises, trimestrielle pour les petites, annuelle pour les très petites). On reprend ainsi un circuit que les entreprises connaissent déjà. **[À vérifier]**

## Contrainte juridique **[À vérifier]**

- **[C]** L'article 34 de la Constitution réserve à la loi la fixation de « l'assiette, le taux et les modalités de recouvrement » des impôts. Le taux ne peut donc pas être laissé libre à l'administration.
- **[C]** Ce qui est admis : la loi fixe une **formule**, ou une **fourchette** avec un plancher et un plafond, et un décret ou la loi de finances de chaque année fixe le taux à l'intérieur de ce cadre.

## Choix préalable : taxe par unité ou taxe sur le prix

- **[C] Taxe sur le prix** (un pourcentage, comme la TVA) : si le prix du token s'effondre, les recettes s'effondrent avec lui. C'est le contraire de l'effet recherché.
- **[C] Taxe par unité** (un montant par octet ou par token, comme une accise) : les recettes suivent le **volume**, donc l'effet Jevons. **C'est le bon choix** pour ce projet.

## Le prix du token tend vers zéro

- **[G]** Le prix du token va tendre vers 0, et ce qu'on fait déjà avec le débit actuel est remarquable. Une conversation comme celle-ci coûtera peut-être 0,2 $ un jour.
- **[G]** Une taxe qui **double le prix du token** forcera quand même à optimiser.
- **[C → validé par G]** Trois enseignements, jugés « très intéressants » par Guillaume :
  1. **Avec une taxe par unité, la part de la taxe dans le prix augmente toute seule à mesure que le prix baisse.** Elle finit par dépasser le prix lui-même, comme pour le carburant (fichier 12). L'utilisateur ne le ressent pas, puisque le prix total continue de baisser : un prix doublé aujourd'hui, c'est le prix d'il y a quelques mois.
  2. **Forcer à optimiser est un bénéfice en soi** : des prompts plus courts, la mise en cache, de petits modèles quand ils suffisent. On consomme moins d'énergie pour le même service. C'est le mécanisme d'une taxe carbone.
  3. **La taxe accompagne l'effet Jevons, elle ne le casse pas.** L'optimisation qu'elle provoque rend chaque usage moins cher, ce qui fait augmenter le volume total, donc les recettes.
- Exemple concret : cette conversation à environ 0,2 $, face à des heures de travail de juriste et d'économiste (fichier 07).

## Indicateurs possibles

| Indicateur | Logique | Limite |
|---|---|---|
| **Besoin de financement du chômage universel** (piste de Guillaume) | Taux = besoin ÷ assiette de l'année précédente. Le système s'équilibre de lui-même. Point remarquable : **le taux baisse quand le volume d'IA augmente** | En récession, le besoin augmente et donc le taux aussi, au moment où les entreprises souffrent |
| Taux de chômage | Le taux suit directement le problème | Le chômage a beaucoup d'autres causes que l'IA |
| **Part des salaires dans la valeur ajoutée** | Si la machine remplace le travail, la part des salaires baisse et le taux monte. C'est **la mesure la plus directe de la substitution** | L'indicateur est lent, publié avec retard, et ses variations ont plusieurs causes |
| Prix moyen du token ou de l'octet | Garde une taxe proportionnée au prix | Annule l'avantage de la taxe par unité |

## Proposition de synthèse

- **[C]** Le taux de l'année N vaut le besoin de financement de l'année N divisé par l'assiette déclarée en N-1.
  - Il est encadré par un **plancher et un plafond** inscrits dans la loi.
  - Il est **lissé**, par exemple avec une variation limitée à ±20 % par an, pour que les entreprises puissent prévoir.
  - En cas de récession, un **fonds de réserve** alimenté les bonnes années absorbe les pics.
- **[C]** Variante : une modulation selon la part des salaires dans la valeur ajoutée. Elle relierait le taux à la substitution du travail, et pas seulement aux besoins de la caisse.

## Précédents **[À vérifier]**

- Les **taux de cotisation chômage**, fixés par la convention Unédic puis agréés par l'État.
- Le **bonus-malus sur les contributions chômage** (depuis 2022), modulé selon le taux de séparation de chaque entreprise.
- Les **impôts locaux**, dont les collectivités votent le taux dans les limites fixées par la loi.

## Liens

- [04-hypothese-modalites-assiette-et-collecte.md](04-hypothese-modalites-assiette-et-collecte.md)
- [05-hypothese-revenu-universel-musk.md](05-hypothese-revenu-universel-musk.md)
