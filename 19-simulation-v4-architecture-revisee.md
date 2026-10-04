# Simulation v4 : la trajectoire de l'architecture révisée

- **Statut** : en discussion (M7 de la session metamaieutique)
- **Créé le** : 2026-10-02
- **Dernière mise à jour** : 2026-10-02 (M7)

> Script : `outils/sim_v4.py` (la v3 est conservée dans `outils/sim_v3.py` et la note 14). Tous les paramètres sont **[C]** ; les montants non sourcés sont **[À vérifier]**. Les décisions citées sont celles du journal.

## En vigueur

**La réponse franche.** L'architecture révisée **ne finance pas le but au plancher**. Elle le finance **à deux conditions** dans le scénario central, et **pas du tout** dans le scénario bas.

1. **Au plancher (m = 1), le chômage universel est ouvert à tous en 2031, mais à un niveau réduit** : le socle atteint environ **790 € par mois en 2035** et **860 € en 2040**, contre une cible de 1 200 €. Seul le scénario haut atteint la cible au plancher (2032).
2. **Dans le scénario central, la cible de 1 200 € est atteinte à l'une de deux conditions** :
   - **(a) m monte jusqu'à 4** (80 % du coût hors TVA, avec la justification renforcée de la décision 51), et l'ordre d'emploi D8 est appliqué tel quel : la cible est atteinte en **2036** ;
   - **(b) les recettes vont d'abord aux droits** pendant la montée en charge, puis seulement à la baisse des cotisations. La cible est alors atteinte en **2034 avec m ≤ 2**, c'est-à-dire **sans dépasser le seuil des deux tiers**. C'est une proposition **[C]**, qui touche la décision 30 [G] et la décision 54 [P] (voir la question 1 de la fin de tour).
3. **Dans le scénario bas, la taxe ne finance même pas l'ouverture du socle au niveau du RSA** (environ 8 Md€ par an), même avec m = 4 : elle rapporte 7,7 Md€ en 2040. Le but dépend donc du **pari de Jevons**, la croissance de l'usage. L'exposé doit le dire, et prévoir le recours à la **contribution d'équilibre** de la LFSS (D8) ou à une autre ressource (une fraction de CSG, la taxe Zucman, hors dispositif).
4. **La variante « étudiants inclus »** (question laissée ouverte, décision 70) ajoute environ **40 Md€ par an** au socle cible. Dans le scénario central, **elle n'est pas finançable par la taxe** : avec m = 4, le socle n'ouvre qu'en 2034 et plafonne à environ 790 € en 2040. Seul le scénario haut la finance (cible en 2034, m = 3).
5. **La variante « réduction pour le patrimoine »** (question laissée ouverte, décision 71) économise environ **0,6 Md€ par an** au socle cible et avance la cible d'un an (2035 au lieu de 2036, avec m ≤ 4). **Son enjeu est de principe, pas budgétaire.**
6. **La première année** (2028, au plancher) rapporte environ **2,6 Md€**, et non « un milliard » comme le dit l'exposé v0.1 (Q13 et Q59, à corriger en M8).
7. **Les quatre sensibilités qui comptent** : la croissance du marché, l'**élasticité** (à 1,0, la cible n'est jamais atteinte ; à 0,3, elle l'est en 2034), l'**inscription des inactifs** (500 000 personnes de plus repoussent la cible à 2040), et la **règle d'emploi des recettes** (point 2).

---

## 1. Les hypothèses

### 1.1 Le calendrier

| Élément | Hypothèse | Source |
|---|---|---|
| Entrée en vigueur | Le **1ᵉʳ janvier 2028** : un vote en 2027, plus le statu quo de trois mois de la notification | Décision 62 |
| Phase 0 | 2028 à 2030 : la taxe est perçue, le fonds se constitue, la formation est financée ; le RSA et l'ASS sont repris à l'identique (neutre) ; **m = 1** | D13.6, décision 73 |
| Phase 1 | Au plus tôt en **2031**, et seulement si la recette de l'année couvre l'ouverture du socle au niveau du RSA (« les droits ne précèdent jamais les recettes ») | D13.6, décision 73 |
| Phase 2 | Le socle monte du niveau du RSA (650 € [À vérifier]) vers la cible (1 200 € [À vérifier]), en fonction des recettes | D13.6, décision 73 |
| Vote de m | En LFSS, à partir de la LFSS pour 2031 ; **lissé à ± 0,5 par an** ; relevé tant que le socle cible n'est pas atteint ; abaissé seulement si la recette attendue couvre encore les engagements | Décisions 40, 50, 51 ; fichier 10 |

### 1.2 L'assiette et la recette

- **Le marché** : celui de la v3 (bas 0,46 ; central 1,32 ; haut 3,0 Md€ en 2026, avec la même croissance), prolongé à + 4 % par an de 2036 à 2040 [C].
- **La recette** : m × dépense × (1 + m)^−ε, avec ε = 0,5, comme en v3.
- **Les ajustements** [C, À vérifier] :

| Paramètre | Valeur | Effet | Fondement |
|---|---|---|---|
| Champ D13.1 | × 0,95 | − 5 % | L'IA non générative est exclue (décision 64) |
| Serveurs propres | × 1,10 | + 10 % | Taxés, mais absents de la v2 et de la v3 (note 13) |
| Recouvrement | × 0,90 | − 10 % | La fraude, les erreurs et les litiges |
| Abattement | 0,5 Md€ de dépense exonérée | − 10 % en 2028, − 2 % en 2035 | Environ 500 000 groupes × 1 000 € ; **le montant reste à fixer** (Q44) |
| IA sur terminal | 5 % du volume en 2028, + 2 points par an, jusqu'à 20 % | Au tarif 0,25 jusqu'en 2030, puis au plein tarif | Décision 60 |
| Coefficients par flux et classes | Neutres | — | P_k est un prix moyen par octet-équivalent pondéré : en moyenne de classe, la taxe vaut m × la dépense (D2) |
| Décalage de P_k | Neutralisé (× 1,00) | Sensibilité à × 1,09 | Un trimestre de décalage avec des prix en baisse de 30 % par an joue **en faveur** de la recette (D2) |

- **Le secteur public** (environ 10 % de la recette [À vérifier], D5) n'est pas retranché : sa part est un transfert entre administrations.

### 1.3 Les dépenses

| Poste | Valeur | Source |
|---|---|---|
| Besoin net à l'ouverture, au niveau du RSA | **7 Md€** : les 18-24 ans (3,9), l'individualisation des couples (1,2), la voie (b) du séjour (0,5), les frontaliers (0,3), la sortie progressive de 12 mois (1,0) [C] | D13.3, D13.7, décision 72 |
| Besoin net au socle cible | **20 Md€** (hors formation) | D13.7 (18 à 23 Md€) |
| Entre les deux | Interpolation linéaire selon le montant du socle | — |
| Formation (coûts pédagogiques, abondement du CPF) | **1 Md€** par an dès 2028 [C, À vérifier] | D13.5 |
| Baisse des cotisations | Jusqu'à 44 Md€ (4 points à 11 Md€) | Fichier 11, v3 |
| Fonds de réserve | Six mois du **besoin net financé par la taxe** (environ 10,5 Md€ au socle cible) [C] | Décision 54 ; voir la question 3 |
| Ordre d'emploi | Les droits ouverts, puis le fonds, puis le surplus partagé moitié-moitié (D8) ; en déficit, le fonds, puis la suspension de la baisse des cotisations | Décision 54 |

**Les variantes** [C, À vérifier] :
- **étudiants inclus** : 2,9 millions d'étudiants au socle, moins les bourses reprises (2,3 Md€), soit **+ 39,5 Md€** au socle cible et + 20 Md€ au niveau du RSA ;
- **patrimoine** : 2 % des bénéficiaires voient leur socle réduit de moitié, soit **− 0,6 Md€** au socle cible ;
- **inscription des inactifs** : 500 000 personnes de plus, soit **+ 7,2 Md€** au socle cible.

## 2. Les résultats

### 2.1 Synthèse (ordre d'emploi D8, tel que décidé)

| Scénario | Plafond de m | Ouverture du socle | Socle cible atteint | Socle en 2035 (€/mois) | Socle en 2040 | Baisse de cotisation en 2040 |
|---|---|---|---|---|---|---|
| Bas | 1, 2 ou 4 | **jamais** | non | — | — | 0 |
| Central | 1 | 2031 | non | 793 | 862 | 0,5 pt |
| Central | 2 | 2031 | non | 987 | 1 100 | 1,0 pt |
| **Central** | **4** | 2031 | **2036** | 1 197 | 1 200 | 2,2 pts |
| Haut | 1 | 2031 | **2032** | 1 200 | 1 200 | 3,5 pts |
| Haut | 2 ou 4 | 2031 | 2031 (m = 1,5) | 1 200 | 1 200 | 4 pts |

### 2.2 La variante d'emploi « les droits d'abord » [C]

| Scénario | Plafond de m | Socle cible atteint | m maximal | Baisse de cotisation en 2040 |
|---|---|---|---|---|
| Central | 1 | non (1 074 € en 2040) | 1 | 0 |
| **Central** | **2** | **2034** | **2** | 0,75 pt |
| Central | 4 | 2033 | 2,5 | 1,2 pt |
| Haut | 1 | 2031 | 1 | 3,5 pts |

**Lecture** : le partage moitié-moitié du surplus pendant la montée en charge **double l'effort** demandé pour atteindre la cible. Pour chaque euro qui fait monter le socle, un euro va à la baisse des cotisations. C'est la tension de la question 65, que la décision 54 n'avait résolue que pour le cas du retournement.

### 2.3 Le scénario central, année par année

| Année | Marché HT | m (D8, plafond 4) | Recette | Socle (€/mois) | Cotisation | m (droits d'abord, plafond 2) | Recette | Socle | Cotisation |
|---|---|---|---|---|---|---|---|---|---|
| 2028 | 4,8 | 1,0 | 2,6 | — | — | 1,0 | 2,6 | — | — |
| 2030 | 11,0 | 1,0 | 6,4 | — (fonds : 10,4) | — | 1,0 | 6,4 | — (fonds : 10,4) | — |
| 2031 | 14,3 | 1,5 | 12,1 | 737 | 0,2 pt | 1,5 | 12,1 | 824 | 0 |
| 2032 | 17,2 | 2,0 | 17,8 | 857 | 0,4 pt | 2,0 | 17,8 | 1 064 | 0 |
| 2033 | 19,8 | 2,5 | 23,7 | 983 | 0,7 pt | 2,0 | 20,6 | 1 182 | 0 |
| 2034 | 21,8 | 3,0 | 29,3 | 1 101 | 1,0 pt | 2,0 | 22,7 | **1 200** | 0,2 pt |
| 2035 | 22,8 | 3,5 | 33,9 | 1 197 | 1,2 pt | 2,0 | 23,9 | 1 200 | 0,3 pt |
| 2036 | 23,8 | 4,0 | 38,2 | **1 200** | 1,6 pt | 2,0 | 24,9 | 1 200 | 0,4 pt |
| 2040 | 27,8 | 4,0 | 45,0 | 1 200 | 2,2 pts | 2,0 | 29,3 | 1 200 | 0,75 pt |

### 2.4 Les variantes et les sensibilités (scénario central, ordre D8)

| Variante | m ≤ 2 : socle cible ? | m ≤ 2 : socle en 2040 | m ≤ 4 : socle cible ? | m ≤ 4 : socle en 2040 |
|---|---|---|---|---|
| Base | non | 1 100 | 2036 | 1 200 |
| **Étudiants inclus** | non (ouverture vers 2040) | 658 | **non** (ouverture en 2034) | **792** |
| **Réduction pour le patrimoine** | non | 1 116 | **2035** | 1 200 |
| 500 000 inactifs de plus | non | 943 | 2040 | 1 200 |
| Fonds de six mois **bruts** (29 Md€) | non | 1 088 | 2036 | 1 200 |
| Élasticité 0,3 | 2039 | 1 200 | 2034 | 1 200 |
| Élasticité 1,0 | non | 830 | **non** | 885 |
| Décalage de P_k (× 1,09) | non | 1 156 | 2035 | 1 200 |
| Sans serveurs propres ni écart de recouvrement | non | 1 105 | 2035 | 1 200 |

**Les étudiants dans le scénario haut** (m ≤ 4, ordre D8) : la cible est atteinte en 2034 avec m = 3, et la baisse des cotisations est complète en 2036. C'est le seul cas où la variante est finançable par la taxe seule.

### 2.5 Comparaison avec la v3 (scénario central)

| | v3 (note 14) | v4 | Pourquoi |
|---|---|---|---|
| Entrée en vigueur | 2026 | 2028 | Le vote, puis le statu quo de trois mois (décision 62) |
| Première recette au plancher | 0,9 Md€ (2026) ; 3,4 Md€ (2028) | 2,6 Md€ (2028) | L'abattement, le terminal à 0,25, le champ et le recouvrement (− 24 % en 2028) |
| Montée de m | De 1 à 4 d'un coup en 2029 | ± 0,5 par an, à partir de 2031 | Le lissage et la phase 0 (décisions 40 et 73) |
| Besoin pour les droits | 16 Md€ | 20 Md€ + 1 Md€ de formation | D13.7 |
| Chômage universel complet | **vers 2033** | **2036** (D8, m ≤ 4) ou **2034** (droits d'abord, m ≤ 2) | Les quatre raisons ci-dessus |
| Baisse de cotisation en 2035 | 2,3 pts | 1,2 pt (D8, m ≤ 4) | Le retard des droits, puis le partage |
| Fonds de réserve | 6,2 Md€ | 10,4 Md€ en 2030 | Trois ans de phase 0 au lieu de deux |

## 3. Ce que la v4 change pour les livrables [C]

1. **L'exposé v0.2** ne peut pas dire que le chômage universel est « finançable au début des années 2030 ». Il peut dire : **ouvert à tous en 2031 ; au niveau cible entre 2034 et 2036 dans le scénario central**, selon la règle d'emploi et le niveau de m que le Parlement votera ; **pas avant 2040 si la croissance de l'usage est faible**.
2. **Le niveau du socle est bien la variable d'ajustement** (décision 73) : le dispositif ne fait jamais défaut, il monte moins vite.
3. **Le plancher reste un principe moral** (la moitié de la valeur au bien commun), pas un financement suffisant : c'est ce que disait déjà la v3, et la v4 le confirme.
4. **L'étude d'impact v0.1** reprendra les tableaux 2.1 à 2.4, avec la variante « étudiants » et la variante « patrimoine » présentées comme des **choix ouverts**, que Guillaume tranchera (décisions 70 et 71).

## 4. Limites

- Le modèle des dépenses est **linéaire** entre deux points de calibrage, eux-mêmes [À vérifier]. La population du socle (4 millions de personnes, note 05) est **probablement sous-estimée** : les couples allocataires du RSA comptent deux adultes, et les personnes au foyer qui s'inscrivent ne sont comptées qu'en variante.
- **L'excédent du fonds** au-delà de sa cible n'est pas employé (il l'est seulement par la baisse de m) : c'est prudent, et cela sous-estime légèrement la vitesse de montée.
- **La baisse de m** est faite pas à pas : dans le scénario haut, le fonds dépasse sa cible, et la LFSS pourrait abaisser m plus vite.
- **La formation** est chiffrée forfaitairement (1 Md€).
- **Les effets de second tour** (la baisse des cotisations sur l'emploi, l'IA sur la masse salariale) ne sont pas modélisés (fichier 11, M10).

## Historique du raisonnement

1. **2026-10-02, M7** : création de la note et du script `sim_v4.py`, d'après les paramètres de la section F de la note 18. **[C]**
2. Constat principal : l'ordre d'emploi D8, appliqué pendant la montée en charge, envoie la moitié de chaque euro de surplus vers la baisse des cotisations, ce qui oblige à porter m à 4 dans le scénario central. D'où la variante « les droits d'abord ». **[C]**

## Questions ouvertes

- La règle d'emploi pendant la montée en charge : D8 tel quel, ou les droits d'abord (question 1 du tour M7).
- La cible du fonds : six mois du besoin net, ou six mois des prestations brutes (question 3 du tour M7).
- Le montant de l'abattement (Q44), à fixer dans le dispositif (M9).
- Les étudiants et le patrimoine : des choix ouverts, réservés à Guillaume (décisions 70 et 71).

## Liens

- [14-simulation-v3-trajectoire-partage.md](14-simulation-v3-trajectoire-partage.md)
- [18-faisabilite-obstacles-juridiques-et-architecture.md](18-faisabilite-obstacles-juridiques-et-architecture.md) (sections D8, D13, F)
- [05-hypothese-revenu-universel-musk.md](05-hypothese-revenu-universel-musk.md)
- [11-cadrage-impact-economique.md](11-cadrage-impact-economique.md)
- `outils/sim_v4.py`
