# PROJET DE LOI

## relatif au financement du chômage universel par une taxe sur l'intelligence artificielle

### dite « Loi Jevons » — ÉTUDE D'IMPACT

*Document de travail : version 0.1, 4 octobre 2026, révisée le même jour après la relecture de cohérence (chiffrage de la sortie progressive raccordé au besoin, garantie familiale chiffrée, tarif réduit sur terminal, entrée en vigueur).*

*Point de départ destiné à être expertisé par un économiste et par un juriste. Elle accompagne l'exposé des motifs v0.2 et le dispositif v0.1. Elle suit le plan prévu par l'article 8 de la loi organique n° 2009-403 du 15 avril 2009.*

*Tous les chiffres viennent de `outils/etude_impact_v01.py`, qui appelle le modèle `outils/sim_v4.py` (note 19 du corpus). Ce sont des **ordres de grandeur**. Les montants sont en milliards d'euros courants (Md€), sauf le socle, exprimé en euros de 2026 (pouvoir d'achat constant au regard du seuil de pauvreté). Les hypothèses non sourcées sont marquées [Unverified] ; les sources vérifiées, [S]. Les propositions de l'agent rédacteur qui n'ont pas été validées sont marquées [opus-5.5].*

---

## 1. Diagnostic

### 1.1 Une indemnisation du chômage fragmentée

La privation d'emploi est aujourd'hui couverte par trois dispositifs aux logiques distinctes : l'allocation d'aide au retour à l'emploi, financée par les contributions assises sur les salaires et gérée par les partenaires sociaux ; l'allocation de solidarité spécifique, financée par l'État ; le revenu de solidarité active, familialisé, financé par les départements et soumis à des obligations d'accompagnement. Une part importante des personnes sans emploi n'a droit à aucune de ces prestations, en particulier les jeunes de moins de vingt-cinq ans sans droits ouverts. Le niveau du revenu de solidarité active (environ 650 € par mois pour une personne seule [Unverified]) se situe nettement sous le seuil de pauvreté (environ 1 200 € [Unverified]).

### 1.2 La diffusion de l'intelligence artificielle

En 2024, 10 % des entreprises de dix salariés ou plus implantées en France utilisaient au moins une technologie d'intelligence artificielle, soit quatre points de plus qu'en 2023 ; la proportion atteint 33 % des entreprises de 250 salariés ou plus et 42 % dans l'information et la communication. La France reste en deçà de la moyenne de l'Union (13 %) [S : Insee Première n° 2061, juillet 2025]. Le marché professionnel de l'inférence en France est estimé, dans le scénario central, à 1,3 Md€ hors taxe en 2026, et à environ 28 Md€ en 2040 [Unverified : note 13 du corpus].

### 1.3 Ce que l'on sait de l'effet sur l'emploi (question 8)

Aucune série statistique française ne permet aujourd'hui d'établir que l'intelligence artificielle remplace du travail de façon nette et mesurable, par métier, en chômage ou en heures travaillées [Unverified : à confirmer par la DARES et l'Insee]. **Le projet n'en dépend pas.** La taxe est justifiée par le fait que la valeur de l'intelligence artificielle procède du savoir collectif, une ressource commune (décision n° 2025-1157 QPC [S]) ; le chômage universel répond à un besoin existant, et non à une vague de destructions annoncée. Si les besoins sont moindres que prévu, le socle atteint sa cible plus tôt et le Parlement abaisse le multiple.

Le Gouvernement propose de suivre l'effet sur l'emploi par trois sources : l'enquête annuelle de l'Insee sur les technologies de l'information dans les entreprises ; les déclarations de la taxe, qui donnent les volumes par classe et par type de contenu (article 19 du dispositif) ; une enquête de la DARES sur l'exposition des métiers. L'évaluation biennale (article 18) les mobilise.

### 1.4 La nécessité de légiférer

L'assiette, le taux et les modalités de recouvrement d'une imposition de toutes natures relèvent de la loi (article 34 de la Constitution). La création d'une branche de la sécurité sociale et l'affectation d'une recette exclusive supposent une loi organique, qui ouvre le champ des lois de financement de la sécurité sociale à la nouvelle branche, et une loi ordinaire. Le multiple de la taxe et le montant du socle sont fixés chaque année en loi de financement de la sécurité sociale.

## 2. Objectifs

1. **Instituer un chômage universel** : un socle individuel versé à toute personne de dix-huit ans ou plus, sans emploi et inscrite, sans obligation de recherche d'emploi, du niveau du revenu de solidarité active vers le seuil de pauvreté.
2. **Le financer par la valeur de l'intelligence artificielle** : une taxe sur l'utilisation professionnelle de l'inférence, dont le tarif est au moins égal au prix moyen du marché (au moins la moitié de la valeur payée revient au bien commun).
3. **Épargner les particuliers et ménager ce qui démarre** : l'usage personnel hors du champ ; un abattement de 1 000 € de taxe par groupe ; un tarif réduit et temporaire pour l'inférence sur équipement terminal.
4. **Protéger la recette** : une branche de sécurité sociale, une recette exclusive, un fonds de réserve, la règle « les droits d'abord ».
5. **À terme, alléger le coût du travail** : une baisse des contributions patronales d'assurance chômage, seconde et différée.

## 3. Options écartées

| Option | Motif de l'écart | Corpus |
|---|---|---|
| Une taxe sur les « robots » ou sur la masse salariale substituée | Le remplacement du travail n'est pas mesurable entreprise par entreprise ; une assiette d'usage l'est | Note 04 |
| Une taxe sur le chiffre d'affaires des fournisseurs de modèles | Elle manque les fournisseurs non établis, ne distingue pas l'usage professionnel et taxe le prix plutôt que l'usage | Note 18, O5 |
| Une taxe avec déduction en chaîne | Elle présenterait les quatre caractéristiques de la TVA et tomberait sous l'article 401 de la directive 2006/112/CE ; la taxe retenue est perçue à un seul stade, la revente se faisant en suspension | O1, D1 ; décision 37 |
| Un tarif unique par unité | Il taxerait plusieurs dizaines de fois leur prix les petits modèles : rupture d'égalité ; le tarif est fixé par classe de modèles | D1 ; décisions 39 et 48 |
| Un taux relevé par arrêté « selon les besoins » | Incompétence négative (article 34) ; le multiple est voté chaque année en LFSS, entre 1 et 4 | O3 ; décisions 40 et 50 |
| Un compteur logiciel imposé aux éditeurs | Règle technique à notifier, lourde et contournable ; l'obligation pèse sur le redevable, le logiciel certifié restant facultatif | O9 ; décision 43 |
| Une affectation au budget général ou à un fonds sans base organique | La recette ne serait pas protégée ; la voie « sécurité sociale » donne une recette exclusive (art. LO 111-3-14 du code de la sécurité sociale) | D4 ; décisions 42 et 49 |
| La taxation de l'entraînement des modèles | Incohérente avec une assiette d'usage ; c'est une piste ultérieure | Décision 45 |
| Le partage à parts égales du surplus dès l'ouverture du socle | Il double l'effort nécessaire pour atteindre la cible ; les droits d'abord, le partage ensuite | Décision 75 |
| Un « cliquet » maintenant le multiple pour préserver la baisse des cotisations | Il tiendrait le multiple au-dessus de 2 pour le seul double dividende ; la baisse des cotisations n'est engagée que si elle est soutenable avec un multiple de 2 au plus | Décision 89 |
| Un droit de douane sur les services d'intelligence artificielle | Contraire au droit de l'Union (la politique commerciale commune) et aux engagements de l'OMC | O7 |

## 4. Le dispositif retenu

| Élément | Règle | Article |
|---|---|---|
| Nature | Une imposition de toutes natures du type accise, à un seul stade, sans déduction, au code des impositions sur les biens et services | 1ᵉʳ |
| Champ | L'utilisation professionnelle en France de l'inférence des modèles à usage général et des systèmes générant des contenus de synthèse ; l'usage personnel, l'entraînement et l'intelligence artificielle non générative hors du champ ; le secteur public inclus | L. [À vérifier]-1 à -3 |
| Tarif | m × P_k par octet-équivalent, P_k étant le prix moyen de la classe k constaté chaque trimestre ; m voté en LFSS entre 1 et 4, avec une justification particulière au-delà de 2 | L. [À vérifier]-12 à -14 |
| Redevable | Le fournisseur enregistré collecte ; à défaut, le client autoliquide ; l'usage propre est déclaré | L. [À vérifier]-5 à -8 |
| Abattement | 1 000 € de taxe par groupe et par an, restitué automatiquement (décision 88) | L. [À vérifier]-16 |
| Terminal | 0,25 × le tarif pendant les trois premières années d'application ; prolongation possible en LFSS jusqu'à cinq ans ; extinction anticipée par un critère de maturité ; la taxe entière n'entre en vigueur qu'après la décision de la Commission ou son accord réputé acquis | L. [À vérifier]-15 ; 15, 16, 17 |
| Branche | Une branche du chômage universel, une caisse nationale, le versement par les CAF | 3 |
| Socle | Individuel, sans obligation de recherche ; du niveau du RSA vers le seuil de pauvreté, fixé en LFSS ; formation maintenue | 4 |
| Séjour | Les conditions du RSA, plus l'accès après six mois d'emploi (directive 2011/98/UE) | 5 |
| Sortie progressive | Douze mois, réduction d'une fraction des revenus d'activité fixée par décret, au plus 50 % ; dégressivité linéaire sur les derniers des douze mois ; jamais moins que le droit actuel | 6 |
| Reprises | Le RSA et l'ASS repris par la branche ; le RSA des personnes en activité servi en complément différentiel ; une garantie familiale revalorisée comme le RSA | 8, 9 |
| Phases | Trois ans de lancement ; ouverture puis hausse du socle selon l'équilibre sur trois ans | 10 |
| Emploi des recettes | Les droits, y compris la revalorisation du socle ; le fonds de réserve ; la hausse du socle jusqu'à la cible ; puis le partage entre les extensions de droits et la baisse des cotisations, qui n'est engagée que si elle est soutenable avec m ≤ 2 ; m ramené à 2 au plus après la cible, compte tenu d'un tiers de l'excédent du fonds ; le retournement défini sur la dépense taxable | 11 à 14 |

## 5. Impacts

### 5.1 Impacts budgétaires

#### 5.1.1 La trajectoire de référence du Gouvernement

Le dispositif n'inscrit aucune trajectoire du multiple : le Parlement le vote chaque année. **Le Gouvernement retient comme trajectoire de référence un multiple de 3 au plus pendant la montée en charge, avec la justification particulière qu'exige l'article 19, puis un retour à 2 une fois la cible atteinte** (décision 84). Dans le scénario central, le multiple ne dépasse pas 2,5 :

| Année | m | Recette | Socle (€ de 2026) | Socle (€ courants) | Besoin net | Baisse des cotisations : Md€ (points) | Fonds de réserve | Cible du fonds |
|---|---|---|---|---|---|---|---|---|
| 2028 | 1,0 | 2,6 | — | — | — | 0 | 1,5 | — |
| 2029 | 1,0 | 4,3 | — | — | — | 0 | 4,8 | — |
| 2030 | 1,0 | 6,4 | — | — | — | 0 | 10,1 | — |
| 2031 | 1,5 | 12,3 | 839 (ouverture) | 926 | 11,2 | 0 | 10,1 | 6,1 |
| 2032 | 2,0 | 18,2 | 1 038 | 1 169 | 17,1 | 0 | 10,1 | 9,1 |
| 2033 | 2,5 | 24,4 | **1 200** (cible) | 1 378 | 22,2 | 0 | 11,0 | 11,7 |
| 2034 | 2,5 | 26,8 | 1 200 | 1 406 | 22,7 | 0 | 14,0 | 11,9 |
| 2035 | 2,0 | 24,3 | 1 200 | 1 434 | 23,1 | 0 | 14,0 | 12,2 |
| 2036 | 2,0 | 25,3 | 1 200 | 1 463 | 23,6 | 0,5 (0,04) | 14,0 | 12,4 |
| 2037 | 2,0 | 26,3 | 1 200 | 1 492 | 24,1 | 1,0 (0,07) | 14,0 | 12,7 |
| 2038 | 2,0 | 27,4 | 1 200 | 1 522 | 24,6 | 1,6 (0,11) | 14,0 | 12,9 |
| 2039 | 2,0 | 28,5 | 1 200 | 1 552 | 25,0 | 2,2 (0,15) | 14,0 | 13,2 |
| 2040 | 2,0 | 29,7 | 1 200 | 1 583 | 25,6 | 2,3 (0,16) | 14,5 | 13,4 |

*Le besoin net est la dépense supplémentaire de la branche par rapport au droit existant (le RSA, l'ASS et la part « socle » de l'assurance chômage étant repris), hors formation (1 Md€ de 2026 par an) ; il comprend la sortie progressive (§ 5.3.4) et la garantie familiale (§ 5.3.2).*

**Lecture.** La première recette est de 2,6 Md€ (2028). Le socle s'ouvre à tous en 2031, à 839 € de 2026, et atteint le seuil de pauvreté en **2033**. Le multiple reste à 2,5 en 2033 et 2034, puis revient à 2 en **2035**, en tenant compte d'un tiers de l'excédent du fonds de réserve sur sa cible ; sans cette règle, il ne reviendrait à 2 qu'en 2036. **La baisse des cotisations commence en 2036**, après le retour du multiple à 2, et atteint **0,16 point en 2040** ; elle ne recule jamais, car elle n'est engagée que si elle est soutenable avec un multiple de 2 au plus.

**Ce qui fait la trajectoire** (scénario central, m ≤ 3 ; chaque ligne ajoute une règle à la précédente) :

| Règles | Cible | Années à m > 2 | Retour de m à 2 | Baisse des cotisations 2040 | Fonds 2040 |
|---|---|---|---|---|---|
| Règles d'une version antérieure (sortie progressive sans plancher) | 2033 | 4 | 2037 | 0,10 point | 20,0 |
| + excédent du fonds compté pour ramener m à 2 | 2033 | 3 | 2036 | 0,10 point | 15,9 |
| + retournement défini sur la dépense taxable | 2033 | 3 | 2036 | 0,10 point | 15,9 |
| + sortie au plus favorable, sans dégressivité | 2033 | 3 | 2036 | 0,10 point | 15,9 |
| + dégressivité sur les six derniers des douze mois | 2033 | 2 | 2035 | 0,21 point | 15,8 |
| + besoin raccordé au chiffrage explicite de la sortie progressive | 2033 | 2 | 2035 | 0,21 point | 15,8 |
| **+ garantie familiale revalorisée comme le RSA (retenue)** | **2033** | **2** | **2035** | **0,16 point** | **14,5** |
| *Variantes de la trajectoire retenue :* | | | | | |
| sans l'excédent du fonds | 2033 | 3 | 2036 | 0,16 point | 18,4 |
| douze mois pleins, puis six mois dégressifs | 2034 | 4 | 2037 | 0 | 17,8 |
| garantie familiale revalorisée comme le socle | 2035 | 8 | après 2040 | 0 | 21,4 |
| tarif réduit sur terminal prolongé à cinq ans | 2033 | 2 | 2035 | 0,16 point | 14,5 |

Trois enseignements. **La modalité de la dégressivité** pèse lourd : placée dans les douze mois, elle réduit le coût de la sortie progressive à la cible (2,14 Md€ au lieu de 3,32, § 5.3.4) ; placée après, elle l'augmente (3,80 Md€) et retarde la cible d'un an, de trois ans avec m ≤ 2 (2040 au lieu de 2037). **La garantie familiale** ramène la baisse des cotisations de 0,21 à 0,16 point en 2040 et retarde d'un an la cible avec m ≤ 2 ; revalorisée comme le socle, elle maintiendrait le multiple au-dessus de 2 jusqu'en 2040. **Le raccord du besoin** relève le socle d'ouverture (839 € au lieu de 790 €) sans changer la suite. Une prolongation du tarif réduit sur terminal jusqu'à cinq ans ne change ni la cible ni la baisse des cotisations ; elle abaisse le socle d'ouverture (804 €).

#### 5.1.2 Si le Parlement s'en tient à un multiple de 2

| Plafond de m | Socle cible | m maximal | Années à m > 2 | Baisse des cotisations 2040 | Fonds 2040 | Socle 2040 |
|---|---|---|---|---|---|---|
| 1 (plancher) | non | 1 | 0 | 0 | 10,1 | 939 € |
| 2 | **2037** | 2 | 0 | 0,16 point | 13,7 | 1 200 € |
| 3 (référence) | **2033** | 2,5 | 2 | 0,16 point | 14,5 | 1 200 € |

Le choix du Parlement porte sur **quatre années** d'avance du chômage universel (2033 au lieu de 2037), au prix de deux années à un multiple de 2,5, au-delà du repère des deux tiers du coût. Au plancher, le socle plafonne à 939 € de 2026 en 2040 : le plancher est un principe (la moitié de la valeur au bien commun), pas un financement suffisant.

#### 5.1.3 Le scénario bas et la contribution d'équilibre

**Dans le scénario bas, l'objectif de la loi n'est pas atteint par la seule taxe sur l'intelligence artificielle d'ici 2040.**

| Plafond de m | Ouverture du socle | Socle 2040 | Recette 2040 | Fonds 2040 | Contribution d'équilibre | Écart à la cible en 2040 |
|---|---|---|---|---|---|---|
| 2 | 2037 | 650 € | 5,7 | 0 | 0,1 (2040) | 21,2 |
| 3 (référence) | 2035 | 650 € | 7,5 | 0 | 0,8 (2039) ; 1,7 (2040) | 19,4 |
| 4 | 2035 | 650 € | 9,0 | 5,3 | aucune d'ici 2040 | 17,8 |

Le socle s'ouvre plus tard, au niveau du RSA, et ne monte pas : la loi ne promet pas de droits que ses recettes ne financent pas. Une fois le fonds épuisé, maintenir le socle demande une **contribution d'équilibre** de l'État, votée en LFSS comme pour les autres branches : 1,7 Md€ en 2040 dans la trajectoire de référence. Au niveau du RSA, la sortie progressive ne coûte rien par rapport au droit actuel (§ 5.3.4). Atteindre la cible demanderait environ **18 à 21 Md€ par an** de ressources hors taxe. D'autres ressources pourraient s'y ajouter, dont une imposition des très grandes fortunes débattue par ailleurs ; le projet n'en dépend pas, et la présente étude ne lui attribue aucun rendement.

#### 5.1.4 Deux options ouvertes au débat parlementaire

Le dispositif retient, pour le chiffrage, l'exclusion des étudiants en formation initiale et l'absence de réduction pour les revenus du patrimoine. **Ces deux points sont des options ouvertes, soumises au débat parlementaire** : ils touchent à l'universalité du dispositif, et le présent projet n'en fait pas une condition de son équilibre.

| Variante (scénario central) | Surcoût au niveau du RSA | Surcoût au socle cible | m ≤ 2 | m ≤ 3 | m ≤ 4 |
|---|---|---|---|---|---|
| Base | — | — | cible en 2037 | cible en 2033 | cible en 2033 |
| **Étudiants inclus** (2,9 millions, bourses reprises) | + 20,3 Md€ | + 39,5 Md€ | ouverture 2033 ; 650 € en 2040 | ouverture 2033 ; 688 € en 2040 | ouverture 2033 ; 789 € en 2040 |
| **Réduction pour le patrimoine** (2 % des bénéficiaires, socle réduit de moitié) | − 0,3 Md€ | − 0,6 Md€ | cible en 2036 | cible en 2033 | cible en 2033 |

*Surcoûts en Md€ de 2026.* L'inclusion des étudiants **n'est pas finançable par la taxe** dans le scénario central : le socle n'atteint pas la cible d'ici 2040, quel que soit le multiple. Elle l'est dans le scénario haut (cible en 2033, multiple maximal de 2,5). La réduction pour le patrimoine a un enjeu de principe, l'introduction d'une condition de ressources dans un dispositif universel, et un enjeu budgétaire faible.

#### 5.1.5 Sensibilités

| Hypothèse (scénario central) | m ≤ 2 : cible | m ≤ 2 : socle 2040 | m ≤ 3 : cible | m ≤ 3 : socle 2040 | Baisse des cotisations 2040 (m ≤ 3) | Recette 2035 (m ≤ 3) |
|---|---|---|---|---|---|---|
| Indexation à 1 % | 2034 | 1 200 € | 2033 | 1 200 € | 0,48 point | 24,3 |
| **Indexation à 2 % (centrale)** | **2037** | 1 200 € | **2033** | 1 200 € | **0,16 point** | 24,3 |
| Indexation à 3 % | non | 1 156 € | 2034 | 1 200 € | 0 | 28,2 |
| Élasticité 0,3 | 2033 | 1 200 € | 2033 | 1 200 € | 0,67 point | 30,4 |
| **Élasticité 0,5 (centrale)** | **2037** | 1 200 € | **2033** | 1 200 € | **0,16 point** | 24,3 |
| Élasticité 1,0 | non | 898 € | non | 961 € | 0 | 15,6 |

L'**indexation** des montants sur le revenu médian (+ 2 % par an en nominal [Unverified], décision 85) est décisive : à 3 %, la cible n'est jamais atteinte avec un multiple de 2. L'**élasticité** de la demande au prix est l'hypothèse la plus incertaine : à 1,0, la cible n'est atteinte d'ici 2040 dans aucun cas. Ces deux paramètres sont soumis à l'économiste.

#### 5.1.6 L'effet circulaire pour les administrations publiques

Les administrations publiques, dans le champ de la taxe (décision 46), en acquittent environ 10 % [Unverified] : 0,3 Md€ en 2028, 1,2 Md€ en 2031, 2,4 Md€ en 2035, 3,0 Md€ en 2040. Pour l'État, c'est un transfert vers la sécurité sociale, neutre pour le solde des administrations publiques au sens de Maastricht. Pour les collectivités, les hôpitaux et les universités, c'est une charge réelle que l'article 72-2 de la Constitution n'oblige pas à compenser [Unverified] ; la compenser par les dotations serait circulaire. L'apport net de la taxe aux administrations publiques, hors leur propre part, est donc d'environ 90 % de la recette (26,7 Md€ en 2040).

#### 5.1.7 Les frontaliers

Un frontalier résidant en France et totalement privé d'emploi relève de l'État de résidence (article 65 du règlement (CE) n° 883/2004). Le surcoût du socle porte sur ceux qui n'ont pas droit à l'allocation d'assurance. **Il est borné** entre 0,04 et 0,27 Md€ de 2026 par an (5 600 à 18 800 personnes ; valeur centrale 0,13 Md€), sous les hypothèses suivantes [Unverified] : 470 000 résidents en France travaillant dans un pays voisin, un taux de chômage de 4 à 8 %, une part sans droit à l'assurance de 30 à 50 %, un socle au niveau du RSA ou de la cible. Le chiffrage retient 0,3 Md€, au-dessus de la borne haute. La révision du règlement n° 883/2004 en cours de négociation pourrait déplacer la charge vers l'État d'emploi [Unverified].

### 5.2 Impacts économiques

#### 5.2.1 L'incidence de la taxe (question 71)

La taxe est collectée par le fournisseur et facturée au client ; elle est, comme toute accise, répercutée. Le prix des services d'intelligence artificielle étant fixé sur un marché mondial, la France ne peut en infléchir le niveau : **la charge pèse d'abord sur les utilisateurs professionnels en France**, puis, selon les marchés, sur leurs clients, leurs salariés ou leurs actionnaires. Les fournisseurs en supportent la part qui tient à la baisse de la demande (§ 5.2.2).

**Ce n'est pas une contradiction avec l'objet du projet.** La valeur que le projet entend faire revenir au bien commun n'est pas la marge des fournisseurs : c'est la valeur de l'usage, qui se réalise chez l'utilisateur, dans ses gains de productivité. La taxe la saisit là où elle naît, quel que soit le pays d'établissement du fournisseur. Les fournisseurs établis et non établis sont traités de la même façon.

#### 5.2.2 L'élasticité et la croissance (question 74)

Le tarif s'ajoute au prix : un multiple de 1 double le prix acquitté, un multiple de 4 le quintuple. Effet sur la dépense hors taxe, selon l'élasticité de la demande au prix :

| Élasticité | m = 1 (prix × 2) | m = 2 (× 3) | m = 3 (× 4) | m = 4 (× 5) |
|---|---|---|---|---|
| 0,3 | − 19 % | − 28 % | − 34 % | − 38 % |
| **0,5 (centrale)** | **− 29 %** | **− 42 %** | **− 50 %** | **− 55 %** |
| 1,0 | − 50 % | − 67 % | − 75 % | − 80 % |

Aucune estimation publiée de l'élasticité de la demande professionnelle d'intelligence artificielle n'a été trouvée [Unverified]. La baisse des prix unitaires, de l'ordre de plusieurs dizaines de pour cent par an [Unverified], est d'un ordre de grandeur comparable à l'effet de la taxe : si les prix baissent de 30 % par an, le prix acquitté taxe comprise à m = 2 en 2033 reste inférieur à la moitié du prix hors taxe de 2028 [opus-5.5 : calcul hors script, 3 × 0,7⁵ ≈ 0,5]. L'effet sur la productivité et la croissance potentielle **n'est pas modélisé** ; il le sera avec les outils de la direction générale du Trésor. La présente étude ne prétend pas qu'il est nul.

#### 5.2.3 Les PME, les jeunes entreprises et les centres de données (question 73)

- **Les très petites entreprises** : un groupe dont la dépense annuelle hors taxe est inférieure à 1 000 € (m = 1), 500 € (m = 2) ou 333 € (m = 3) n'acquitte rien ; au-delà, l'abattement réduit la charge de 1 000 €. Une entreprise cliente d'un fournisseur enregistré n'a aucune déclaration à faire (§ 5.4).
- **Les jeunes entreprises françaises d'intelligence artificielle** : leurs clients français acquittent la taxe dans les mêmes conditions que les clients de leurs concurrents étrangers ; leurs ventes à l'étranger sont hors du champ. La taxe ne les désavantage pas face à la concurrence. Elle réduit, en revanche, la taille de leur premier marché, comme celui de tous les fournisseurs (§ 5.2.2). Le tarif réduit sur équipement terminal favorise l'intelligence artificielle locale et embarquée.
- **Les centres de données** : la taxe porte sur l'utilisation en France, quel que soit le lieu d'exécution de l'inférence. Un centre de données situé en France qui sert des clients étrangers n'est pas concerné ; un centre situé à l'étranger qui sert des clients français l'est. **La taxe est neutre quant à la localisation des centres de calcul.**
- **Les exportateurs qui utilisent l'intelligence artificielle** supportent la taxe sans remboursement à l'export, qui serait une aide à l'exportation ; l'abattement et, à terme, la baisse des cotisations en atténuent la portée (décision 63).
- **Les prestations produites à l'étranger avec de l'intelligence artificielle** et importées ne sont pas taxées (question 34) : c'est un risque de délocalisation de certaines tâches, assumé, que l'évaluation suivra.

#### 5.2.4 Le coût du travail

La baisse des contributions patronales d'assurance chômage est **modeste et tardive** : 0,16 point en 2040 dans la trajectoire de référence, 0,48 point si l'indexation est de 1 %, de 2,20 à 3,61 points dans le scénario haut. Le projet n'en fait pas une promesse. Ses effets sur l'emploi ne sont pas modélisés.

### 5.3 Impacts sociaux

#### 5.3.1 Les bénéficiaires

Le socle s'ouvre en 2031 aux personnes sans emploi qui n'ont aujourd'hui aucun droit, en premier lieu les jeunes de dix-huit à vingt-quatre ans (3,9 Md€ du besoin net à l'ouverture), aux membres de couples qui n'ont pas de droit propre (1,2 Md€), aux ressortissants de pays tiers qui ont travaillé au moins six mois (0,5 Md€) et aux frontaliers (0,3 Md€), soit 6,0 Md€ de 2026 au niveau du RSA [Unverified]. La sortie progressive et la garantie familiale ne coûtent rien de plus, à ce niveau, que le droit actuel (§ 5.3.2 et 5.3.4). Le socle atteint le seuil de pauvreté en 2033 dans la trajectoire de référence.

#### 5.3.2 La garantie de non-régression

Le socle étant individuel et le RSA familialisé, certains foyers seraient perdants sans garantie : les parents isolés avec deux enfants ou plus relevant du RSA majoré, les familles nombreuses (note 18, D9). L'article 9 leur garantit au moins le montant du RSA, majoration comprise, **revalorisé comme le RSA**, sous la forme d'un complément familial ; il maintient les droits connexes, assimile les périodes de socle pour la retraite et prévoit une clause de sauvegarde individuelle de cinq ans.

**Le coût.** Par rapport au droit actuel, la garantie ne verse rien de plus : le foyer garde le RSA qu'il perçoit aujourd'hui. Mais par rapport à un socle purement individuel, sur lequel est calé le besoin au socle cible, elle a un coût, qui décroît à mesure que le socle monte [Unverified : 410 000 foyers, du parent isolé avec un enfant à la famille nombreuse, hypothèses de l'agent rédacteur] :

| Socle (€ de 2026) | Complément versé, garantie revalorisée comme le RSA (retenue) | Complément versé, garantie revalorisée comme le socle | Ajout au besoin net (retenue) |
|---|---|---|---|
| 650 € | 2,34 Md€ | 2,34 Md€ | 0 (déjà servi au titre du RSA repris) |
| 925 € | 1,33 Md€ | 3,33 Md€ | 0,16 Md€ |
| 1 200 € | 0,55 Md€ | 4,31 Md€ | 0,55 Md€ |

Revalorisée comme le socle, la garantie coûterait environ 4,3 Md€ par an à la cible et maintiendrait le multiple au-dessus de 2 jusqu'en 2040 (§ 5.1.1) ; c'est pourquoi elle suit la revalorisation du RSA, qui suffit à garantir qu'aucun foyer ne perde par rapport au droit actuel. Les droits connexes restent à inventorier [Unverified].

#### 5.3.3 La condition de séjour

La condition de séjour du socle reprend toutes les voies d'accès actuelles au RSA, avec leurs exceptions, et en ajoute une : six mois d'emploi en France, qu'impose l'article 12 de la directive 2011/98/UE dès lors que le socle est une prestation de chômage [S]. **Personne d'aujourd'hui éligible n'est exclu.** Le surcoût est de 0,5 Md€ (§ 5.3.1). La suppression de la condition de cinq ans pour les autres ressortissants de pays tiers, plus sûre au regard de la Constitution mais plus coûteuse, est un **choix politique ouvert** (décision 59) ; elle n'est pas chiffrée dans la présente version.

#### 5.3.4 La sortie progressive et ses taux marginaux (question 56)

**La règle** (article 6) : pendant douze mois après une reprise d'activité, le socle est réduit d'une fraction des revenus d'activité, fixée par décret et au plus égale à 50 % ; sur les derniers mois, fixés par décret, le montant restant **décroît linéairement** jusqu'à s'annuler ; **pendant toute la période, le bénéficiaire perçoit le plus favorable** de ce montant et de ce que lui procureraient le RSA et la prime d'activité selon le droit actuel. Reprendre un travail rapporte donc toujours au moins autant qu'aujourd'hui.

Revenu mensuel (salaire plus versement), personne seule, taux de 50 %, six mois de dégressivité [Unverified : SMIC net de 1 430 € ; droit actuel simplifié : max(0 ; 640 € − 0,39 × salaire), sans bonification individuelle] :

| Socle | Salaire net | Droit actuel | Version précédente : mois 1 à 12 / 13ᵉ mois | Corrigé : mois 1 à 6 / 7ᵉ mois / 12ᵉ mois / 13ᵉ mois | Plus forte baisse d'un mois sur l'autre |
|---|---|---|---|---|---|
| 650 € (ouverture) | 358 € (quart de SMIC) | 858 € | 829 / 858 € | 858 / 858 / 858 / 858 € | 0 |
| 650 € | 715 € (mi-temps) | 1 076 € | **1 008** / 1 076 € | 1 076 / 1 076 / 1 076 / 1 076 € | 0 |
| 650 € | 1 430 € (SMIC) | 1 512 € | 1 430 / 1 512 € | 1 512 / 1 512 / 1 512 / 1 512 € | 0 |
| 1 200 € (cible) | 358 € | 858 € | 1 379 / **858** € | 1 379 / 1 233 / 858 / 858 € | 146 € |
| 1 200 € | 715 € | 1 076 € | 1 558 / **1 076** € | 1 558 / 1 437 / 1 076 / 1 076 € | 120 € |
| 1 200 € | 1 430 € | 1 512 € | 1 915 / **1 512** € | 1 915 / 1 846 / 1 512 / 1 512 € | 69 € |

**Taux marginaux effectifs après correction** :
- **au niveau d'ouverture** (650 €), le droit actuel est plus favorable dès 91 € de salaire : le taux marginal est celui d'aujourd'hui, **39 %**. La régression de la version précédente (1 008 € au lieu de 1 076 € pour un mi-temps au SMIC) disparaît ;
- **à la cible** (1 200 €), le taux marginal est de **50 %** pendant les six premiers mois, jusqu'à 2 400 € de salaire ; il descend ensuite de 43 % à 7 % pendant la dégressivité. Le revenu reste toujours supérieur au droit actuel ;
- **la marche du 13ᵉ mois** (de 403 à 521 € au socle cible dans la version précédente ; aucune au niveau du RSA) est remplacée par des baisses mensuelles de 69 à 146 €.

**Le coût** (Md€ de 2026 par an, par rapport au droit actuel ; 600 000 reprises d'emploi par an, salaires répartis du quart de SMIC au SMIC [Unverified]) :

| Socle | Version précédente (sans plancher) | Au plus favorable, sans dégressivité | **Au plus favorable, dégressivité sur les six derniers mois (retenue)** | Au plus favorable, douze mois pleins puis six mois dégressifs |
|---|---|---|---|---|
| 650 € | − 0,52 | 0 | **0** | 0 |
| 925 € | 1,34 | 1,34 | **0,78** | 1,45 |
| 1 200 € | 3,32 | 3,32 | **2,14** | 3,80 |

Le plancher coûte **0,52 Md€ au niveau du RSA** : c'est exactement ce que la version précédente « économisait » par la régression. À la cible, il ne coûte rien, la sortie progressive y étant toujours plus favorable que le droit actuel. La dégressivité dans les douze mois réduit le coût de 1,18 Md€ à la cible ; une dégressivité ajoutée après les douze mois l'augmente de 0,48 Md€. **Le modèle de la branche retire des points de calage du besoin net la sortie progressive qu'ils supposaient, puis ajoute son coût ainsi chiffré** (`sim_v4.py`, `sp_cost`) : c'est ce qui explique les changements de trajectoire du § 5.1.1. La dégressivité dans les douze mois est retenue ; ses paramètres (600 000 reprises par an, le droit actuel simplifié, six mois) sont soumis à l'économiste.

### 5.4 Impacts administratifs et coût de conformité (questions 43 et 75)

**L'abattement** (décision 88) coûte environ 0,5 Md€ par an [Unverified : 500 000 groupes utilisateurs], soit 16 % de la recette brute en 2028, 4 % en 2031, 2 % en 2035 et en 2040. Il n'est pas indexé : son poids relatif décroît.

**Le coût de conformité**, sous les hypothèses de l'agent rédacteur [Unverified] :

| Catégorie | Nombre | Mise en place | Coût annuel |
|---|---|---|---|
| Fournisseurs enregistrés (collecte, déclaration par numéro SIREN) | 200 | 30 M€ | 12 M€ |
| Autoliquidants (fournisseur non enregistré) | 5 000 | 10 M€ | 8 M€ |
| Déclarants pour usage propre (serveurs propres) | 2 000 | 40 M€ | 16 M€ |
| Revendeurs agréés (attestations, registre) | 1 000 | 5 M€ | 3 M€ |
| TPE et PME clientes d'un fournisseur enregistré (numéro SIREN, relevé prérempli) | 500 000 | 0 | 10 M€ |
| **Total des entreprises** | | **0,09 Md€** | **0,05 Md€** |
| Administration (600 équivalents temps plein ; logiciel libre et systèmes) | | 30 M€ | 48 M€ |

Les coûts annuels représentent 3,8 % de la recette en 2028 et 0,4 % en 2035. L'essentiel de la charge pèse sur quelques centaines de fournisseurs ; **une entreprise qui n'achète qu'à des fournisseurs enregistrés n'a rien à déclarer**. Pour la branche, le versement du socle est délégué aux caisses d'allocations familiales, qui servent déjà le RSA ; la reprise du RSA et de l'ASS modifie l'organisation des départements et de France Travail (§ 7).

**Les sanctions** (article L. [À vérifier]-21) reprennent le droit commun des taxes sur le chiffre d'affaires ; les amendes propres à la taxe sont un point de départ, à expertiser sous l'angle de la proportionnalité (décision 90). Elles ne frappent que les professionnels, entrepreneurs individuels compris, ou l'employeur pour le compte duquel une fausse déclaration a été faite ; jamais un salarié, un agent ni un particulier.

## 6. Articulation avec le droit de l'Union européenne

| Norme | Analyse | Risque résiduel |
|---|---|---|
| Directive 2006/112/CE, art. 401 | La taxe n'a pas les caractéristiques de la TVA : un seul stade, pas de déduction, un tarif par unité de volume et non proportionnel au prix de la transaction (CJUE, Vodafone Magyarország, C-75/18) [S] | Faible |
| Aides d'État (art. 107 et 108 TFUE) | Le champ est défini objectivement ; l'abattement est une mesure générale ; le tarif réduit sur terminal est notifié, défendu par la logique du système et, à titre subsidiaire, par l'art. 107, § 3, c (Commission c/ Hongrie, C-596/19 P ; ANGED, C-233/16) [S]. La taxe entière n'entre en vigueur qu'après la décision de la Commission ou l'autorisation réputée acquise (règlement (UE) 2015/1589, art. 4, § 6 [S]) : aucune aide n'est mise en œuvre avant, et le tarif réduit s'applique dès le premier jour | Moyen ; retard de la recette si la procédure formelle est ouverte |
| Directive (UE) 2015/1535 | Aucune règle technique n'est imposée ; le tarif réduit lié au mode d'exécution est notifié par prudence, avec un statu quo de trois mois | Faible |
| Règlement (UE) 2024/1689 sur l'IA | Le champ renvoie à ses définitions (art. 3, points 1 et 63 ; art. 50, § 2) ; la taxe n'ajoute aucune exigence de mise sur le marché | Faible |
| Règlement (CE) n° 883/2004 | Le socle est une prestation de chômage ; un droit au séjour peut être exigé (C-308/14) [S] ; l'inscription à l'annexe X est une étape ultérieure | Faible à moyen (frontaliers) |
| Directive 2011/98/UE, art. 12 | Accès au socle après six mois d'emploi (article 5, b) | Faible |
| RGPD | Aucune liste de particuliers n'est transmise ; le logiciel certifié transmet des volumes agrégés ; avis de la CNIL sur les décrets | Faible |
| Directive 2011/16/UE (DAC) | Coopération administrative pour les fournisseurs établis dans l'Union | Faible |
| OMC et AGCS | La taxe ne dépend pas de l'origine ; le tarif réduit dépend du lieu technique d'exécution | Faible en droit ; risque de représailles politique |

Aucune disposition du projet ne suppose une modification du droit de l'Union. L'inscription du socle à l'annexe X du règlement n° 883/2004 est une étape ultérieure.

## 7. Consultations à mener

| Instance | Objet | Fondement |
|---|---|---|
| **Partenaires sociaux** (organisations syndicales et patronales représentatives) | Concertation préalable : le recentrage de l'assurance chômage sur le complément, la contribution de l'organisme gestionnaire à la branche, la baisse des contributions patronales | Art. L. 1 du code du travail [Unverified] ; décision 74 |
| **Départements** et Conseil national d'évaluation des normes | La reprise du RSA, la reprise des ressources correspondantes, l'accompagnement devenu facultatif | Art. L. 1212-2 du code général des collectivités territoriales [Unverified] ; art. 72-2 de la Constitution |
| Caisses nationales de sécurité sociale (CNAF, CCMSA) et organisme gestionnaire de l'assurance chômage | Le versement délégué du socle, la reprise des droits | Art. L. 200-3 du code de la sécurité sociale [Unverified] |
| **CNIL** | Les données de déclaration par numéro d'identification, la règle des comptes grand public, le logiciel certifié | Loi n° 78-17 du 6 janvier 1978 [Unverified : article applicable] ; article 20 du dispositif |
| **Commission européenne** | Prénotification dès la rédaction du projet ; notification au titre de la directive 2015/1535 (statu quo de trois mois) et de l'art. 108, § 3, TFUE (examen préliminaire de deux mois) ; l'entrée en vigueur en dépend | Articles 15 et 16 du dispositif |
| Conseil d'État | Avis sur le projet de loi et le projet de loi organique | Art. 39 de la Constitution |
| Haut Conseil du financement de la protection sociale | Avis sur la création de la branche [opus-5.5, facultatif] | — |

Les collectivités d'outre-mer et le département de Mayotte, où le RSA obéit à des règles propres, appellent une consultation et des adaptations spécifiques [Unverified].

## 8. Modalités d'application et d'évaluation

**Textes d'application** : des décrets en Conseil d'État, après avis de la CNIL pour les données personnelles (article 20) ; un décret fixant le taux de la sortie progressive (article 6) ; un décret sur la contribution de l'organisme gestionnaire de l'assurance chômage (article 7) ; l'arrêté trimestriel constatant les prix P_k ; le référentiel de certification du logiciel.

**Calendrier** : la prénotification et la notification en 2027, en même temps que le vote ; l'entrée en vigueur au 1ᵉʳ janvier 2028 si la Commission s'est prononcée avant (sinon, le 1ᵉʳ janvier suivant sa décision) ; trois ans de lancement (fonds de réserve, formation, reprise à l'identique du RSA et de l'ASS) ; l'ouverture du socle au plus tôt en 2031 ; le rapport sur le terminal au plus tard le 30 juin 2030 ; l'extinction du tarif réduit fin 2030, sauf prolongation votée en LFSS jusqu'à fin 2032 au plus.

**Évaluation** : le rapport annuel annexé au PLFSS (rendement par classe et par type de contenu, trajectoire du socle, fonds de réserve, application de l'ordre d'emploi, justification du multiple au-delà de 2, scénario bas) ; l'évaluation biennale des effets sur l'emploi, l'activité, la formation et la pauvreté (article 18). Indicateurs proposés : le taux de pauvreté des personnes sans emploi ; le taux de recours au socle ; les taux de reprise d'emploi pendant et après la sortie progressive ; la part des entreprises utilisant l'intelligence artificielle (Insee) ; les volumes déclarés ; le prix moyen par classe.

---

## Annexe : les questions de la confrontation fermées par la présente étude

| Question (fichier 17) | Réponse | Section |
|---|---|---|
| 8. Des données montrent-elles que l'IA remplace déjà du travail ? | Pas de série française probante ; le projet n'en dépend pas ; un dispositif d'observation est prévu | 1.3 |
| 71. Qui supporte la taxe ? | Les utilisateurs professionnels en France, puis leurs clients ; la valeur saisie est celle de l'usage, pas la marge des fournisseurs | 5.2.1 |
| 73. Effets sur les PME, les jeunes entreprises, les centres de données | Abattement ; aucune déclaration via un fournisseur enregistré ; neutralité concurrentielle et de localisation | 5.2.3 |
| 74. Élasticité et croissance | Effets de − 29 % à − 55 % sur la dépense (élasticité 0,5) ; sensibilité de 0,3 à 1,0 ; effet sur la croissance non modélisé, renvoyé à l'économiste | 5.2.2, 5.1.5 |
| 43 et 75. Coût de conformité | 0,05 Md€ par an pour les entreprises, 48 M€ pour l'administration | 5.4 |
| 56. Taux marginaux de la sortie progressive | Jamais moins que le droit actuel (39 % au niveau du RSA) ; 50 % à la cible, puis une dégressivité sans marche ; coût chiffré | 5.3.4 |
| 34. Prestations importées | Risque assumé, suivi par l'évaluation | 5.2.3 |

*Sources principales : note 18 du corpus (O1 à O10, D1 à D13), note 19 (simulation v4), journal des décisions (n° 37 à 109) ; Insee Première n° 2061 (juillet 2025) : https://www.insee.fr/fr/statistiques/8604126.*
