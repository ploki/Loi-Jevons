# Simulation v4 : la trajectoire de l'architecture révisée

- **Statut** : en discussion (M7 de la session metamaieutique, terminée le 2026-10-04)
- **Créé le** : 2026-10-02
- **Dernière mise à jour** : 2026-10-04 (fin de M7 : vérification des chiffres, décision 75, scénario bas)

> Script : `outils/sim_v4.py` (la v3 est conservée dans `outils/sim_v3.py` et la note 14). Tous les paramètres sont **[C]** ; les montants non sourcés sont **[À vérifier]**. Les décisions citées sont celles du journal. Depuis le 2026-10-04, les ajouts portent les marqueurs nominatifs (voir `00-methode-conventions-et-index.md`, « Identités et marqueurs ») : **[opus-5.5]** pour une proposition de l'agent, **[opus-5.5 as ggim]** pour une décision par procuration.

## En vigueur

**La règle d'emploi des recettes est désormais « les droits d'abord »** (décision 75 [opus-5.5 as ggim], ↺ de la décision 30 [G] pendant la montée en charge) : tant que le socle cible n'est pas atteint, le surplus va aux droits ; le partage moitié-moitié reprend ensuite. Les résultats ci-dessous sont calculés avec cette règle ; ceux de l'ancienne règle D8 (décision 54) sont gardés pour comparaison.

**La réponse franche** [opus-5.5]. L'architecture révisée **ne finance pas le but au plancher**, sauf dans le scénario haut. Elle le finance **avec m ≤ 2** dans le scénario central. Elle **ne le finance pas** dans le scénario bas.

1. **Au plancher (m = 1), le chômage universel est ouvert à tous en 2031, à un niveau réduit** : le socle atteint environ **935 € par mois en 2035** et **1 074 € en 2040**, contre une cible de 1 200 €. Seul le scénario haut atteint la cible au plancher (2031).
2. **Dans le scénario central, la cible de 1 200 € est atteinte en 2034 avec m ≤ 2**, c'est-à-dire **sans dépasser le repère des deux tiers** (décision 51). Si le Parlement laisse m monter jusqu'à 2,5, elle l'est en 2033. Avec l'ancienne règle D8, il fallait porter m à 4 pour l'atteindre en 2036.
3. **Le double dividende est retardé, pas abandonné** : la baisse des cotisations commence l'année où la cible est atteinte. Elle vaut **0,26 point en 2035 et 0,75 point en 2040** (m ≤ 2), contre 1,2 et 2,2 points avec D8 et m = 4.
4. **Dans le scénario bas, la taxe ne finance pas le but.** Elle rapporte 3,3 à 7,7 Md€ en 2040 selon m, alors que l'ouverture du socle au niveau du RSA coûte environ 8 Md€ par an (formation comprise). Avec la règle d'ouverture du script (la recette de l'année doit couvrir l'ouverture), **le socle ne s'ouvre jamais d'ici 2040**, et le fonds de réserve accumule 15 à 43 Md€ sans emploi. Avec la règle de D13.6 (l'équilibre sur trois ans, fonds compris), il s'ouvre au niveau du RSA en **2035 (m ≤ 4) ou 2037 (m ≤ 2)**, et le fonds est épuisé vers 2040. **Pas de revirement** : on le dit dans l'exposé et dans l'étude d'impact, avec le recours à la **contribution d'équilibre** (D8) ; la taxe Zucman est citée comme une ressource complémentaire, **hors dispositif** (décision 32). Formulation proposée en section 3.
5. **La variante « étudiants inclus »** (question laissée ouverte, décision 70) ajoute environ **40 Md€ par an** au socle cible. Dans le scénario central, **elle n'est pas finançable par la taxe** : avec m ≤ 4, le socle n'ouvre qu'en 2034 et atteint 935 € en 2040. Dans le scénario haut, elle l'est (cible en 2032, m = 2).
6. **La variante « réduction pour le patrimoine »** (question laissée ouverte, décision 71) économise environ **0,6 Md€ par an** au socle cible et avance la cible d'un an (2033 au lieu de 2034, avec m ≤ 2). **Son enjeu est de principe, pas budgétaire.**
7. **La première année** (2028, au plancher) rapporte environ **2,6 Md€**, et non « un milliard » comme le dit l'exposé v0.1 (Q13 et Q59, à corriger dans l'exposé v0.2, M9).
8. **Les sensibilités qui comptent** : la croissance du marché ; l'**élasticité** (à 1,0, la cible n'est jamais atteinte, et le socle plafonne à environ 1 010 à 1 120 € en 2040 ; à 0,3, elle l'est en 2032) ; l'**inscription des inactifs** (500 000 personnes de plus repoussent la cible à 2040 avec m ≤ 2, à 2035 avec m ≤ 4).

---

## 1. Les hypothèses

### 1.1 Le calendrier

| Élément | Hypothèse | Source |
|---|---|---|
| Entrée en vigueur | Le **1ᵉʳ janvier 2028** : un vote en 2027, plus le statu quo de trois mois de la notification | Décision 62 |
| Phase 0 | 2028 à 2030 : la taxe est perçue, le fonds se constitue, la formation est financée ; le RSA et l'ASS sont repris à l'identique (neutre) ; **m = 1** | D13.6, décision 73 |
| Phase 1 | Au plus tôt en **2031**, et seulement si la recette de l'année couvre l'ouverture du socle au niveau du RSA (« les droits ne précèdent jamais les recettes »). **Variante** [opus-5.5] : la recette plus un tiers du fonds (l'équilibre sur trois ans de D13.6) | D13.6, décision 73 |
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
| Abattement | 0,5 Md€ de dépense exonérée | **− 15 % de la recette en 2028, − 3 % en 2035** (scénario central, m = 1) ; soit 10 % puis 2 % du marché | Environ 500 000 groupes × 1 000 € ; **le montant reste à fixer** (Q44) |
| IA sur terminal | 5 % du volume en 2028, + 2 points par an, jusqu'à 20 % | Au tarif 0,25 jusqu'en 2030, puis au plein tarif | Décision 60 |
| Coefficients par flux et classes | Neutres | — | P_k est un prix moyen par octet-équivalent pondéré : en moyenne de classe, la taxe vaut m × la dépense (D2) |
| Décalage de P_k | Neutralisé (× 1,00) | Sensibilité à × 1,09 | Un trimestre de décalage avec des prix en baisse de 30 % par an joue **en faveur** de la recette (D2) |

- **Le secteur public** (environ 10 % de la recette [À vérifier], D5) n'est pas retranché : sa part est un transfert entre administrations.

### 1.3 Les dépenses

| Poste | Valeur | Source |
|---|---|---|
| Besoin net à l'ouverture, au niveau du RSA | **7 Md€** : les 18-24 ans (3,9), l'individualisation des couples (1,2), la voie (b) du séjour (0,5), les frontaliers (0,3), la sortie progressive de 12 mois (1,0) [C]. *La somme fait 6,9 ; le script l'arrondit à 7.* | D13.3, D13.7, décision 72 |
| Besoin net au socle cible | **20 Md€** (hors formation) | D13.7 (18 à 23 Md€) |
| Entre les deux | Interpolation linéaire selon le montant du socle | — |
| Formation (coûts pédagogiques, abondement du CPF) | **1 Md€** par an dès 2028 [C, À vérifier] | D13.5 |
| Baisse des cotisations | Jusqu'à 44 Md€ (4 points à 11 Md€) | Fichier 11, v3 |
| Fonds de réserve | Six mois du **besoin net financé par la taxe**, formation comprise (environ 10,5 Md€ au socle cible) [C] | Décision 54 ; voir les questions ouvertes |
| Règle d'emploi retenue | Les droits ouverts ; puis le fonds ; puis **le surplus aux droits jusqu'au socle cible** ; ensuite le partage moitié-moitié, dont la part « droits », sans objet une fois la cible atteinte, revient à la baisse des cotisations. En déficit : le fonds, puis la suspension de la baisse des cotisations, puis la contribution d'équilibre | **Décision 75** (et 54 pour le retournement) |
| Ancienne règle D8 (pour comparaison) | Les droits ouverts, puis le fonds, puis le surplus partagé moitié-moitié dès l'ouverture | Décision 54 |

**Les variantes** [C, À vérifier] :
- **étudiants inclus** : 2,9 millions d'étudiants au socle, moins les bourses reprises (2,3 Md€), soit **+ 39,5 Md€** au socle cible et + 20 Md€ au niveau du RSA ;
- **patrimoine** : 2 % des bénéficiaires voient leur socle réduit de moitié, soit **− 0,6 Md€** au socle cible ;
- **inscription des inactifs** : 500 000 personnes de plus, soit **+ 7,2 Md€** au socle cible.

## 2. Les résultats

### 2.1 Synthèse, règle retenue (« les droits d'abord », décision 75)

| Scénario | Plafond de m | Ouverture du socle | Socle cible atteint | m maximal | Socle en 2035 (€/mois) | Socle en 2040 | Baisse de cotisation en 2035 | en 2040 |
|---|---|---|---|---|---|---|---|---|
| Bas | 1, 2 ou 4 | **jamais** (règle annuelle) ; 2037 ou 2035 (règle sur trois ans, m ≤ 2 ou 4) | non | — | — | — ou 650 | 0 | 0 |
| Central | 1 | 2031 | non | 1 | 935 | 1 074 | 0 | 0 |
| **Central** | **2** | 2031 | **2034** | **2** | 1 200 | 1 200 | 0,26 pt | **0,75 pt** |
| Central | 4 | 2031 | 2033 | 2,5 | 1 200 | 1 200 | 0,60 pt | 1,16 pt |
| Haut | 1 | 2031 | **2031** | 1 | 1 200 | 1 200 | 2,5 pts | 3,5 pts |
| Haut | 2 ou 4 | 2031 | 2031 | 1,5 | 1 200 | 1 200 | 4 pts | 4 pts |

### 2.2 Pour comparaison : l'ancienne règle D8 (décision 54)

| Scénario | Plafond de m | Ouverture du socle | Socle cible atteint | Socle en 2035 (€/mois) | Socle en 2040 | Baisse de cotisation en 2040 |
|---|---|---|---|---|---|---|
| Bas | 1, 2 ou 4 | **jamais** | non | — | — | 0 |
| Central | 1 | 2031 | non | 793 | 862 | 0,5 pt |
| Central | 2 | 2031 | non | 987 | 1 100 | 1,0 pt |
| Central | 4 | 2031 | 2036 | 1 197 | 1 200 | 2,2 pts |
| Haut | 1 | 2031 | 2032 | 1 200 | 1 200 | 3,5 pts |
| Haut | 2 ou 4 | 2031 | 2031 (m = 1,5) | 1 200 | 1 200 | 4 pts |

**Lecture** [C] : le partage moitié-moitié du surplus pendant la montée en charge **double l'effort** demandé pour atteindre la cible. Pour chaque euro qui fait monter le socle, un euro va à la baisse des cotisations. C'est la tension de la question 65, que la décision 54 n'avait résolue que pour le cas du retournement, et que la **décision 75** résout pour la montée en charge.

### 2.3 Le scénario central, année par année

| Année | Marché HT | m (retenue, plafond 2) | Recette | Socle (€/mois) | Cotisation | m (D8, plafond 4) | Recette | Socle | Cotisation |
|---|---|---|---|---|---|---|---|---|---|
| 2028 | 4,8 | 1,0 | 2,6 | — | — | 1,0 | 2,6 | — | — |
| 2030 | 11,0 | 1,0 | 6,4 | — (fonds : 10,4) | — | 1,0 | 6,4 | — (fonds : 10,4) | — |
| 2031 | 14,3 | 1,5 | 12,1 | 824 | 0 | 1,5 | 12,1 | 737 | 0,2 pt |
| 2032 | 17,2 | 2,0 | 17,8 | 1 064 | 0 | 2,0 | 17,8 | 857 | 0,4 pt |
| 2033 | 19,8 | 2,0 | 20,6 | 1 182 | 0 | 2,5 | 23,7 | 983 | 0,7 pt |
| 2034 | 21,8 | 2,0 | 22,7 | **1 200** | 0,2 pt | 3,0 | 29,3 | 1 101 | 1,0 pt |
| 2035 | 22,8 | 2,0 | 23,9 | 1 200 | 0,3 pt | 3,5 | 33,9 | 1 197 | 1,2 pt |
| 2036 | 23,8 | 2,0 | 24,9 | 1 200 | 0,35 pt | 4,0 | 38,2 | **1 200** | 1,6 pt |
| 2040 | 27,8 | 2,0 | 29,3 | 1 200 | 0,75 pt | 4,0 | 45,0 | 1 200 | 2,2 pts |

**Avec la règle retenue et m ≤ 4**, m monte à 2,5 en 2033, la cible est atteinte la même année, puis **m reste à 2,5** : le script ne l'abaisse que lorsque la baisse des cotisations est complète. Au-delà de m = 2, c'est donc le double dividende seul qui maintient la taxe au-dessus du repère des deux tiers (voir les questions ouvertes).

### 2.4 Les variantes et les sensibilités (scénario central, règle retenue)

| Variante | m ≤ 2 : socle cible ? | m ≤ 2 : socle en 2040 | m ≤ 4 : socle cible ? | m ≤ 4 : socle en 2040 | Rappel D8, m ≤ 4 |
|---|---|---|---|---|---|
| Base | **2034** | 1 200 | 2033 | 1 200 | 2036 |
| **Étudiants inclus** | non (ouverture en 2040) | 666 | **non** (ouverture en 2034) | **935** | non (792) |
| **Réduction pour le patrimoine** | 2033 | 1 200 | 2033 | 1 200 | 2035 |
| 500 000 inactifs de plus | 2040 | 1 200 | 2035 | 1 200 | 2040 |
| Fonds de six mois **bruts** (29 Md€) | 2035 | 1 200 | 2034 | 1 200 | 2036 |
| Ouverture sur trois ans (D13.6) | 2034 | 1 200 | 2033 | 1 200 | 2036 |
| Élasticité 0,3 | 2032 | 1 200 | 2032 | 1 200 | 2034 |
| Élasticité 1,0 | non | 1 011 | **non** | 1 120 | non (885) |
| Décalage de P_k (× 1,09) | 2033 | 1 200 | 2033 | 1 200 | 2035 |
| Sans serveurs propres ni écart de recouvrement | 2034 | 1 200 | 2033 | 1 200 | 2035 |

**Les étudiants dans le scénario haut** (m ≤ 4, règle retenue) : la cible est atteinte en 2032 avec m = 2, et la baisse des cotisations atteint 3,3 points en 2040. Avec D8, il fallait m = 3 (cible en 2034). C'est le seul cas où la variante est finançable par la taxe seule.

### 2.5 Le scénario bas, en détail (règle retenue)

| Règle d'ouverture | Plafond de m | Ouverture | Recette 2035 | Recette 2040 | Fonds en 2040 | Socle en 2040 |
|---|---|---|---|---|---|---|
| Annuelle (script) | 1 | jamais | 2,7 | 3,3 | 15,0 | — |
| Annuelle | 2 | jamais | 4,2 | 5,3 | 29,0 | — |
| Annuelle | 4 | jamais | 5,7 | 7,7 | 43,0 | — |
| Sur trois ans (D13.6) | 1 | jamais | 2,7 | 3,3 | 15,0 | — |
| Sur trois ans | 2 | 2037 | 4,2 | 5,3 | 1,0 | 650 |
| Sur trois ans | 4 | 2035 | 5,7 | 7,7 | 1,0 | 650 |

**Lecture** [opus-5.5] : une fois le fonds épuisé (vers 2040), maintenir le socle au niveau du RSA demande une **contribution d'équilibre** d'environ **0,3 Md€ par an (m = 4) à 2,7 Md€ par an (m = 2)**. Atteindre la cible demanderait environ **13 à 16 Md€ par an** de ressources hors taxe. Avec la règle annuelle, la taxe est perçue sans que le socle s'ouvre, et le fonds grossit sans emploi : c'est un argument pour retenir, dans le dispositif, la règle d'équilibre sur trois ans de D13.6 (voir les questions ouvertes).

### 2.6 Comparaison avec la v3 (scénario central)

| | v3 (note 14) | v4 | Pourquoi |
|---|---|---|---|
| Entrée en vigueur | 2026 | 2028 | Le vote, puis le statu quo de trois mois (décision 62) |
| Première recette au plancher | 0,9 Md€ (2026) ; 3,4 Md€ (2028) | 2,6 Md€ (2028) | L'abattement, le terminal à 0,25, le champ et le recouvrement (− 24 % en 2028) |
| Montée de m | De 1 à 4 d'un coup en 2029 | ± 0,5 par an, à partir de 2031 | Le lissage et la phase 0 (décisions 40 et 73) |
| Besoin pour les droits | 16 Md€ | 20 Md€ + 1 Md€ de formation | D13.7 |
| Chômage universel complet | **vers 2033** | **2034 avec m ≤ 2** (règle retenue) ; 2036 avec D8 et m ≤ 4 | Les raisons ci-dessus, et la décision 75 |
| Baisse de cotisation en 2035 | 2,3 pts | 0,26 pt (règle retenue, m ≤ 2) ; 1,2 pt (D8, m ≤ 4) | Le retard des droits, puis la priorité aux droits |
| Fonds de réserve | 6,2 Md€ | 10,4 Md€ en 2030 | Trois ans de phase 0 au lieu de deux |

## 3. Ce que la v4 change pour les livrables

1. **L'exposé v0.2** [C, mis à jour par opus-5.5] ne peut pas dire que le chômage universel est « finançable au début des années 2030 ». Il peut dire : **ouvert à tous en 2031 ; au niveau cible vers 2034 dans le scénario central**, sans que la taxe dépasse les deux tiers du coût ; **pas d'ici 2040 si la croissance de l'usage est faible**, sans une autre ressource.
2. **Le niveau du socle est bien la variable d'ajustement** (décision 73) : le dispositif ne fait jamais défaut, il monte moins vite.
3. **Le plancher reste un principe moral** (la moitié de la valeur au bien commun), pas un financement suffisant : c'est ce que disait déjà la v3, et la v4 le confirme.
4. **La règle d'emploi** (décision 75) s'écrit dans le dispositif : les droits d'abord jusqu'au socle cible, puis le partage moitié-moitié. L'exposé présente le double dividende comme **différé**, et non abandonné.
5. **L'étude d'impact v0.1** reprendra les tableaux 2.1 à 2.5, avec la variante « étudiants » et la variante « patrimoine » présentées comme des **choix ouverts**, que Guillaume tranchera (décisions 70 et 71).
6. **Le scénario bas : la formulation proposée** [opus-5.5], à valider.
   - **Pour l'exposé des motifs** : « Le rendement de la taxe dépend de la croissance de l'usage professionnel de l'intelligence artificielle. Si cette croissance est forte, comme elle l'est aujourd'hui, la taxe suffit à porter le socle au seuil de pauvreté dans les premières années de la décennie 2030. Si elle est faible, elle ne suffit pas à elle seule : le socle s'ouvre plus tard et monte moins vite, car la loi ne promet pas de droits que ses recettes ne financent pas. La branche dispose alors, comme les autres branches de la sécurité sociale, de la contribution d'équilibre que vote la loi de financement de la sécurité sociale. D'autres ressources pourront s'y ajouter, au premier rang desquelles une imposition des très grandes fortunes, dont le principe est débattu par ailleurs : le présent projet n'en dépend pas. »
   - **Pour l'étude d'impact** : le tableau 2.5, avec l'écart chiffré (de 0,3 à 2,7 Md€ par an pour maintenir le socle au niveau du RSA après l'épuisement du fonds, de 13 à 16 Md€ par an pour atteindre la cible), et une phrase franche : « Dans le scénario bas, l'objectif de la loi n'est pas atteint par la seule taxe sur l'intelligence artificielle d'ici 2040. »
   - **Le nom de la taxe Zucman** peut figurer dans l'exposé (décision 32), comme un projet distinct et complémentaire (Jevons taxe le flux de valeur de l'IA, Zucman le stock des grandes fortunes, note 15), à condition de ne lui attribuer aucun rendement chiffré dans le texte (Q76).

## 4. Limites

- Le modèle des dépenses est **linéaire** entre deux points de calibrage, eux-mêmes [À vérifier]. La population du socle (4 millions de personnes, note 05) est **probablement sous-estimée** : les couples allocataires du RSA comptent deux adultes, et les personnes au foyer qui s'inscrivent ne sont comptées qu'en variante.
- **L'excédent du fonds** au-delà de sa cible n'est pas employé (il l'est seulement par la baisse de m) : c'est prudent, et cela sous-estime légèrement la vitesse de montée.
- **La baisse de m** est faite pas à pas : dans le scénario haut, le fonds dépasse sa cible, et la LFSS pourrait abaisser m plus vite.
- **La formation** est chiffrée forfaitairement (1 Md€).
- **Les effets de second tour** (la baisse des cotisations sur l'emploi, l'IA sur la masse salariale) ne sont pas modélisés (fichier 11, étude d'impact).
- [opus-5.5] **La cible de 1 200 € est constante en euros courants.** Or le seuil de pauvreté suit le revenu médian. Son indexation absorberait une partie de la moitié « droits » du partage après la cible ; le script l'envoie entièrement à la baisse des cotisations, ce qui **surestime** le double dividende après 2034.
- [opus-5.5] **La règle d'ouverture du script est annuelle**, plus stricte que celle de D13.6 (l'équilibre sur trois ans, fonds compris). Elle ne change rien dans les scénarios central et haut, mais beaucoup dans le scénario bas (section 2.5).

## Historique du raisonnement

1. **2026-10-02, M7** : création de la note et du script `sim_v4.py`, d'après les paramètres de la section F de la note 18. **[C]**
2. Constat principal : l'ordre d'emploi D8, appliqué pendant la montée en charge, envoie la moitié de chaque euro de surplus vers la baisse des cotisations, ce qui oblige à porter m à 4 dans le scénario central. D'où la variante « les droits d'abord ». **[C]**
3. **2026-10-04, fin de M7** : un agent neuf relance le script et contrôle chaque chiffre de la note. **Écarts trouvés et corrigés** [opus-5.5] : l'effet de l'abattement était donné en part du marché (− 10 % puis − 2 %), et non en part de la recette (− 15 % puis − 3 %) ; la somme des composantes du besoin à l'ouverture fait 6,9 et non 7 (arrondi du script) ; « pas avant 2040 » dans le scénario bas devient « pas d'ici 2040 ». Tous les autres chiffres concordent avec la sortie du script.
4. **2026-10-04** : la proposition (b), « les droits d'abord », est **acceptée par procuration** : **décision 75** [opus-5.5 as ggim], ↺ de la décision 30 [G] pendant la montée en charge. Le script prend cette règle par défaut ; l'ancienne règle reste calculable (`alloc='D8'`) et ses résultats sont inchangés. Les variantes sont recalculées avec la règle retenue. **[opus-5.5]**
5. **2026-10-04** : l'orchestrateur demande de dire honnêtement que la taxe seule ne finance pas le but dans le scénario bas, sans revirement. **Constat nouveau** [opus-5.5] : avec la règle annuelle, le fonds y accumule 15 à 43 Md€ sans que le socle s'ouvre. Ajout de la variante d'ouverture sur trois ans (D13.6), du tableau 2.5 et d'une formulation pour l'exposé et l'étude d'impact.

## Questions ouvertes

- ~~La règle d'emploi pendant la montée en charge : D8 tel quel, ou les droits d'abord~~ : **les droits d'abord** (décision 75).
- La cible du fonds : six mois du besoin net, ou six mois des prestations brutes. [opus-5.5] Je recommande le **besoin net** : le fonds protège ce que la taxe finance, et le reste du socle est financé par des recettes de la branche qui ne dépendent pas de la taxe. La variante brute retarde la cible d'un an.
- [opus-5.5] **La règle d'ouverture** : annuelle (le script) ou sur trois ans, fonds compris (D13.6). Je recommande d'écrire **la règle de D13.6** dans le dispositif : elle reste prudente, et elle évite de percevoir la taxe pendant des années sans ouvrir de droits.
- [opus-5.5] **m au-delà de 2 après la cible** : faut-il ramener m à 2 au plus une fois le socle cible atteint, de sorte que le double dividende ne justifie jamais à lui seul de dépasser le repère des deux tiers ? Je le recommande, par cohérence avec la décision 75 (le double dividende est un bénéfice second).
- [opus-5.5] **L'objet de la moitié « droits » après la cible** : l'indexation du socle sur le seuil de pauvreté et les extensions que la LFSS voterait ; à défaut, la baisse des cotisations.
- Le montant de l'abattement (Q44), à fixer dans le dispositif (M10).
- Les étudiants et le patrimoine : des choix ouverts, réservés à Guillaume (décisions 70 et 71).

## Liens

- [14-simulation-v3-trajectoire-partage.md](14-simulation-v3-trajectoire-partage.md)
- [18-faisabilite-obstacles-juridiques-et-architecture.md](18-faisabilite-obstacles-juridiques-et-architecture.md) (sections D8, D13, F)
- [05-hypothese-revenu-universel-musk.md](05-hypothese-revenu-universel-musk.md)
- [11-cadrage-impact-economique.md](11-cadrage-impact-economique.md)
- [15-concept-complementarite-taxe-zucman.md](15-concept-complementarite-taxe-zucman.md)
- `outils/sim_v4.py`
