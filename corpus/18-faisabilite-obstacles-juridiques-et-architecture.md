# Faisabilité juridique : obstacles, solutions et architecture révisée

- **Statut** : en discussion (état à la fin de M14, la passe de corrections, le 2026-10-04)
- **Créé le** : 2026-10-02
- **Dernière mise à jour** : 2026-10-04 (élagage, décisions 115 et 116 ; auparavant M14 : décisions 98 à 109, passe de corrections après la relecture de cohérence, note 20)

> Note de la session metamaieutique « Rendre la Loi Jevons réalisable » (voir `mandat.md`). Les décisions par procuration sont marquées **[P]** et numérotées comme au journal ; les propositions non validées restent **[C]**. Les textes vérifiés sur le web sont marqués **[S]** ; le reste est **[À vérifier]**. **Depuis le 2026-10-04** (décision 76), les ajouts portent les marqueurs nominatifs : **[opus-5.5]** (proposition de l'agent), **[opus-5.5 as ggim]** (décision par procuration, l'ancien [P]), **[Unverified]** (l'ancien [À vérifier]) ; voir le fichier 00, « Identités et marqueurs ».

## En vigueur

> **Pour reprendre** : l'architecture tient en une page ci-dessous. Les décisions de la session sont au journal (n° 37 à 109 ; les suivantes, hors session, depuis le n° 110). La trajectoire chiffrée est dans la **note 19** (simulation v4). Les questions qui restent sont dans la rubrique « Questions ouvertes » et dans le fichier 17. Les sections A, B et D gardent le raisonnement. **Élagage du 2026-10-04 (décision 115)** [opus-5.5 → ggim] : le récapitulatif des décisions par itération, le plan de travail (ancienne section C), le suivi des 20 questions, toutes fermées (ancienne section E), et le guide de reprise de la session (ancienne section F) sont recopiés tels quels dans `../archive/18-faisabilite-sections-C-E-F-et-decisions-par-iteration.md`. L'architecture en une page et la liste des points d'expertise en sont tirées ici.

**L'architecture en une page** (état à la fin de M14) :

| Élément | Règle retenue | Décisions |
|---|---|---|
| Nature | Une imposition de toutes natures, du type accise sur un service, à un seul stade, sans déduction ; placée dans le CIBS [À vérifier] | 37 |
| Champ | L'utilisation professionnelle en France de l'inférence des modèles d'IA à usage général et des systèmes générant des contenus de synthèse (D13.1) ; les particuliers, l'entraînement et l'IA non générative sont hors du champ ; le secteur public est inclus | 45, 46, 64 |
| Unité | L'octet-équivalent (1 caractère = 1) ; des coefficients par type de contenu et par flux (générées 1 ; lues 0,25 ; cache 0,025), fixés par la loi | 9, 30, 65 |
| Abattement | 1 000 € de taxe par groupe et par an, non indexé, révisable en LFSS, restitué automatiquement | 67, **88** |
| Tarif | m × P_k par classe (trois tranches de prix catalogue, lissées aux bornes) ; P_k calculé par l'INSEE chaque trimestre ; m voté en LFSS entre 1 et 4, avec une justification renforcée au-delà de 2 ; en repli, un tarif en euros par unité | 39, 40, 41, 48, 50, 51, 68 |
| Redevable | Le fournisseur enregistré collecte ; à défaut, le client autoliquide ; l'usage propre est déclaré ; un revendeur agréé achète en suspension ; règle de transparence ; règle contre les comptes grand public | 37, 38, 53, 66, 68 |
| Territorialité | L'utilisation effective en France ; l'export est hors du champ, mais déclaré ; une table de conversion, des forfaits, une option pour le réel | 52, 61 |
| IA sur terminal | 0,25 × le tarif pendant les trois premières années d'application, prolongation votée en LFSS jusqu'à cinq ans au plus, extinction anticipée par un critère de maturité ; **notification en amont, et entrée en vigueur de toute la taxe subordonnée à la décision de la Commission ou à l'autorisation réputée acquise** (D11 bis) | 44, 60, 62, **103** |
| Comptage | Une obligation de résultat pour le redevable (une comptabilité-matière) ; le SDK libre et certifié vaut présomption de bonne foi | 43, 67 |
| Affectation | Une branche de sécurité sociale propre ; une recette exclusive (art. LO 111-3-14) ; un fonds de réserve de six mois ; une fraction pour l'Unédic ; une loi organique et une loi ordinaire | 42, 49, 54 |
| Emploi des recettes | Les droits ouverts, puis le fonds, puis **les droits d'abord** jusqu'au socle cible ; ensuite le partage moitié-moitié entre les extensions de droits et la baisse des cotisations ; **l'évolution du socle comme le revenu médian est un droit de rang 1 (106)** ; en retournement, le fonds, m, la suspension de la baisse des cotisations, puis la contribution d'équilibre ; **une baisse des cotisations n'est engagée que si elle est soutenable avec m ≤ 2** ; m ramené à 2 au plus après la cible, compte tenu d'un tiers de l'excédent du fonds ; le retournement défini sur la dépense taxable | 54, **75**, 79, 86, **89**, **94**, **95**, **106** |
| Chômage universel | Le socle (prestation de chômage au sens du règlement 883/2004), individuel, du niveau du RSA vers le seuil de pauvreté (environ 1 200 €) ; le RSA et l'ASS repris avec la non-régression ; une condition de séjour plus ouverte que celle du RSA ; la part « socle » de l'ARE reversée à la branche ; la sortie progressive de 12 mois, jamais moins favorable que le droit actuel, avec une dégressivité linéaire sur les derniers mois des douze (98) ; le RSA des actifs à faible revenu en complément différentiel (99) ; une garantie familiale revalorisée comme le RSA (108) ; l'Unédic recentrée sur le complément | 55 à 59, 72, 74, 91, **96, 98, 99, 108** |
| Calendrier | Le vote et la notification en 2027 ; l'entrée en vigueur le 1ᵉʳ janvier suivant la décision de la Commission (en principe 2028) ; la phase 0 de trois ans ; l'ouverture du socle au plus tôt en 2031 ; le montant du socle, voté en LFSS, est la variable d'ajustement | 62, 73 |
| Champ du socle, choix ouverts | **Les étudiants en formation initiale** et **la réduction pour les revenus du patrimoine** : dans le corpus, réservés à Guillaume ; dans les livrables, options ouvertes au débat parlementaire ; chiffrés en variantes | 70, 71, **102** |

**Encore à l'état de proposition** [opus-5.5] : le socle (**D13.2** : montant, individualisation, aides au logement) et la formation (**D13.5**). Le dispositif v0.1 les rédige (art. 4, VI et VII), sous la mention [opus-5.5] ; **aucune décision du journal ne les arrête** (correction M14, rapport de relecture A10). Il en va de même des bornes de 0,2 et 2 fois l'indice des trois classes (L.-12) et du seuil de dix fois le volume médian (L.-3, I, 4°).

**Ce que dit la simulation v4** (note 19 ; état à la fin de M14, règles des décisions 75 à 109) [opus-5.5] : la première recette est d'environ 2,6 Md€ (2028) ; le socle s'ouvre à tous en 2031, à 839 € de 2026 ; dans le scénario central, **la cible est atteinte en 2033 si la LFSS autorise m jusqu'à 3** (m à 2,5 en 2033 et 2034, ramené à 2 en 2035), **ou en 2037 avec m ≤ 2** ; au plancher, le socle plafonne à 939 € de 2026 en 2040 ; **la baisse des cotisations commence en 2036 et atteint 0,16 point en 2040** ; **dans le scénario bas, la taxe seule ne finance pas le but** : le socle s'ouvre au niveau du RSA en 2035 (m ≤ 3 ou 4) ou 2037 (m ≤ 2), puis le recours est la contribution d'équilibre (1,7 Md€ en 2040 avec m ≤ 3, aucune avec m ≤ 4) ; la taxe Zucman est citée hors dispositif, sans rendement chiffré (32, 77) ; la variante « étudiants » n'est pas finançable par la taxe dans le scénario central. *Ces chiffres remplacent ceux de M13 (cible 2036 avec m ≤ 2, 0,21 point) : le besoin a été raccordé à la sortie progressive et la garantie familiale est chiffrée (décisions 108 et 109).*

**État des obstacles** (inchangé en M7 ; la décision 75 et le scénario bas posent des questions budgétaires, pas juridiques, voir D13.8) : l'article 401 n'est pas bloquant (O1, D1). Les blocages de l'article 34 (O3), du compteur (O9) et de l'affectation (O4) sont **levés** (décisions 40, 43 et 49). Aucun obstacle bloquant connu ne reste sans solution. Restent un risque moyen sur l'égalité (O2), les aides d'État (O6) et la territorialité (O5), et l'inscription du socle à l'annexe X du règlement 883/2004, qui est une **étape ultérieure**.

| Obstacle | Bloquant en l'état ? | Piste recommandée [C] | Risque résiduel |
|---|---|---|---|
| O1. Art. 401 de la directive TVA | Non, sous conditions | Taxe spéciale, à un stade unique, sans déduction ; la revente est en suspension | Faible |
| O2. Égalité, capacité contributive, confiscation | Risque sérieux sur deux points | Un tarif par classe de modèles ; des critères de champ objectifs ; un plafond justifié | Moyen |
| O3. Article 34 (taux par arrêté selon les « besoins ») | **Levé** (décision 40) | La formule d'indexation dans la loi ; le multiple m voté chaque année par le Parlement, entre 1 et 4 | Faible |
| O4. Affectation (LOLF, LFSS, Unédic) | **Levé** (décision 49) | Une **branche de sécurité sociale** financée par la taxe, affectée en LFSS (D4, D6) ; une fraction à l'Unédic | Faible |
| O5. Territorialité, fournisseurs étrangers, cascade | Difficulté pratique | Le fournisseur enregistré collecte ; sinon le client autoliquide ; la revente est en suspension ; directive DAC | Moyen |
| O6. Aides d'État (IA locale, abattement) | Risque sérieux | Un champ défini objectivement ; une notification préventive, **l'entrée en vigueur de la taxe étant subordonnée à la décision de la Commission** (D11 bis) ; l'abattement est une mesure générale | Moyen ; retard de la recette si la procédure formelle est ouverte |
| O7. OMC, AGCS, conventions fiscales | Non | Une taxe neutre quant à l'origine | Faible en droit ; risque de représailles politique |
| O8. Départements (RSA), article 72-2 | Non, mais à organiser | Recentralisation du RSA avec reprise des ressources, sur le modèle de la LFI pour 2022 (D6) | Faible |
| O9. Compteur obligatoire (directive 2015/1535, AI Act, RGPD) | **Levé** (décision 43) | Obligation pesant sur le **redevable** (tenir une comptabilité-matière), le SDK n'étant qu'une **voie simplifiée** ; notification | Faible à moyen |
| O10. Chômage universel et droit de l'UE (résidence, coordination) | Non | En l'état, une prestation de chômage, avec un droit au séjour exigé (C-308/14) ; l'annexe X est une étape ultérieure (D6) | Faible à moyen (les frontaliers) |

---

## A. Architecture révisée proposée en M1 [C] (historique : l'état à jour est dans « En vigueur »)

> Les décisions 37, 38, 39, 40, 43, 44, 45 et 46 [P] ont validé l'essentiel de A1 à A4.

### A1. Nature juridique et code d'accueil
- Une **imposition de toutes natures** (pas une cotisation : elle n'ouvre pas de droits à celui qui la paie ; pas une redevance : elle n'est pas la contrepartie d'un service rendu).
- Elle est du type **accise sur un service** : un montant par unité de volume, perçu **une seule fois**, au stade de l'**utilisation professionnelle finale**.
- Code d'accueil : le **code des impositions sur les biens et services (CIBS)**, qui regroupe depuis 2022 les accises et des taxes sur des services, plutôt que le CGI. [S] (ordonnance n° 2021-1843 du 22 décembre 2021) [À vérifier : l'opportunité du CIBS plutôt que le CGI]

### A2. Redevable (inspiré de l'accise sur l'électricité, où le fournisseur collecte auprès du consommateur final)
- **Le fournisseur de services d'IA** qui s'est **enregistré** en France, qu'il soit établi en France ou non, collecte la taxe auprès de ses clients professionnels et la reverse.
- **À défaut** (un fournisseur étranger non enregistré), le **client professionnel autoliquide**.
- **L'inférence exécutée par l'entreprise elle-même**, sur ses serveurs ou dans des capacités louées, est déclarée par l'entreprise, comme une **production pour usage propre**.
- **L'achat pour revente** (un intégrateur qui revend de l'IA à un client professionnel) se fait **en suspension** de taxe, sur attestation, comme pour un entrepositaire. Il n'y a donc **pas de cascade** (Q35), et **pas de mécanisme de déduction**, ce qui est essentiel pour l'article 401.

### A3. Assiette et tarif
- **L'assiette reste le volume** en octet-équivalent (décision 9), avec des **coefficients par type de contenu inscrits dans la loi**.
- **Le tarif unitaire est fixé par classe de modèles** (par exemple trois ou quatre classes, définies par un critère objectif tel que la taille ou le prix catalogue) : tarif de la classe k = m × P_k, où P_k est le prix moyen de la classe. Cela règle **Q26** (un modèle sobre n'est plus taxé à cinquante fois son prix) et rend le **50/50 vrai pour chaque classe**.
- **P_k est indexé chaque trimestre** par arrêté, selon une **formule fixée par la loi**, qui ne laisse aucune marge d'appréciation à l'administration (simple constat de l'indice).
- **Le multiple m est voté chaque année par le Parlement** (décision 40 [P]), entre **1** (le plancher : la moitié de la valeur) et **4** (le plafond), au vu d'un rapport sur le besoin de financement. Il serait voté en **loi de financement de la sécurité sociale** si la voie D4 est retenue, sinon en loi de finances. Le « moteur » B/A devient ainsi une **décision du Parlement** et non un arrêté (règle O3).
- [C] Variante à discuter : une assiette **ad valorem** (100 % à 400 % du prix hors taxe), plus simple à contrôler. Elle reste compatible avec l'article 401 (voir O1), mais elle s'éloigne de la décision 9 sur le volume. **Je ne la recommande pas** comme régime principal, mais comme **régime de secours** pour les offres au forfait (Q23).

### A4. Champ
- **Le champ est l'usage professionnel.** Les particuliers ne sont pas « exonérés » : ils sont **hors du champ**, parce que le fait générateur est l'utilisation par une personne qui agit dans le cadre d'une activité économique ou d'une mission de service public. Le critère est objectif (O2).
- **L'entraînement et l'affinage** : à trancher (Q40). Ma recommandation provisoire est de les mettre **hors champ**, au motif que l'objet de la taxe est l'**usage productif** qui substitue au travail, et parce que les taxer pénaliserait la recherche et les modèles français.
- **Le secteur public, les associations et la recherche** : à trancher (Q22). Je recommande provisoirement de les inclure, avec l'abattement, pour la cohérence du critère.

### A5. Affectation (première version, remplacée par la comparaison D4)
- **Une loi de finances** affecte le produit de la taxe (article 2 de la LOLF, voir O4) à :
  - un **établissement public** à créer, par exemple une « Caisse nationale du chômage universel », qui gère le **socle** et le **fonds de réserve** ;
  - et, pour une fraction, à l'**Unédic**, en compensation de la **baisse des contributions patronales** (le double dividende).
- Variante : un **compte d'affectation spéciale** (article 21 de la LOLF), qui garde la recette dans le budget de l'État.
- Le **complément** proportionnel reste une prestation d'**assurance**, gérée par l'Unédic.

### A6. Calendrier
- La loi est votée en N. La taxe entre en vigueur au 1ᵉʳ janvier N+1 au plus tôt, après la **notification** à la Commission (règles techniques et, si besoin, aides d'État : un délai d'au moins trois mois). [À vérifier]

---

## B. Les obstacles, un par un

### O1. Article 401 de la directive 2006/112/CE (Q69)

- **Le texte** [S] : « les dispositions de la présente directive ne font pas obstacle au maintien ou à l'introduction par un État membre […] d'accises, de droits d'enregistrement, et, plus généralement, de tous impôts, droits et taxes **n'ayant pas le caractère de taxes sur le chiffre d'affaires**, à condition que la perception de ces impôts, droits et taxes ne donne pas lieu dans les échanges entre États membres à des formalités liées au passage d'une frontière ».
- **Le critère de la Cour de justice** [S] : ont le caractère de taxes sur le chiffre d'affaires les impôts qui présentent les **quatre caractéristiques essentielles de la TVA** :
  1. l'**application générale** aux transactions ayant pour objet des biens ou des services ;
  2. un montant **proportionnel au prix** perçu par l'assujetti ;
  3. une perception **à chaque stade** du processus de production et de distribution ;
  4. la **déduction** de la taxe payée aux stades antérieurs, de sorte que la charge finale repose sur le consommateur.

  Sources : CJCE, Rousseau Wilmot, C-295/84, pt 16 ; Dansk Denkavit, C-200/90, pt 11 ; Pelzl, C-338/97, pt 20. Un impôt qui ne présente pas ces caractéristiques n'est pas interdit (Solisnor, C-130/96 ; GIL Insurance, C-308/01, pt 34). **Une taxe qui ne frappe qu'une ou plusieurs catégories de biens ou de services n'est pas incompatible** (GIL Insurance). La Cour retient une conception **juridique** et non économique (Banca Popolare di Cremona, C-475/03, à propos de l'IRAP). Tout cela est repris dans le rapport du Conseil des prélèvements obligatoires sur le cadre juridique de la TVA (2015, p. 33-34).
- **Jurisprudence récente** [S] : la Cour, en grande chambre, a jugé compatibles avec l'article 401 des **taxes spéciales hongroises assises sur le chiffre d'affaires** des opérateurs de télécommunications et du commerce de détail (CJUE, 3 mars 2020, **Vodafone Magyarország, C-75/18**, et Tesco-Global, C-323/18).
- **Analyse de la taxe Jevons** :
  - critère 1 : **absent**, puisque seuls les services d'IA sont visés ;
  - critère 2 : **absent ou affaibli**, puisque le montant dépend du volume et d'un prix **moyen** de marché, et non du prix perçu dans chaque transaction ;
  - critère 3 : **absent** dans l'architecture A2 (un seul stade, la revente en suspension) ;
  - critère 4 : **absent**, il n'y a pas de déduction.
- **Ce qui créait le risque dans la v0.1** : l'« autoliquidation comme la TVA », le calendrier de la TVA et l'idée d'éviter la cascade par une **déduction**. Le calendrier et l'autoliquidation ne sont pas en eux-mêmes des caractéristiques essentielles ; **la déduction en serait une**.
- **Pistes** : (a) **un seul stade et la suspension pour la revente, sans déduction** (recommandé) ; (b) si l'on voulait une déduction, la restreindre à la revente du même service, ce qui reste moins sûr.
- **Risque résiduel** : **faible**. La condition sur les formalités aux frontières est remplie (pas de contrôle au passage de la frontière ; des déclarations périodiques).
- **Effet secondaire** : la taxe entre dans la base de la TVA (les taxes font partie de la base d'imposition, art. 78 de la directive) [À vérifier]. Pour un client assujetti, la TVA est déductible, donc neutre.

### O2. Égalité devant les charges publiques, capacité contributive, confiscation (Q67, Q68, Q26)

- **Le précédent le plus proche** [S] : **Cons. const., n° 2025-1157 QPC du 12 septembre 2025**, sur la **taxe sur les services numériques** (art. 299 et s. du CGI). Le Conseil la juge **conforme**. Il retient qu'« il était loisible au législateur de soumettre à la taxe des services numériques dont la création de valeur repose de façon déterminante sur l'activité des utilisateurs » (§ 27), que l'assiette, les sommes encaissées, ne fait pas peser une capacité contributive inexistante (§ 48), et que la taxe n'est pas confiscatoire (§ 59).
  - **C'est un appui direct à l'argument du savoir collectif** : une valeur créée de façon déterminante à partir d'une ressource commune justifie un prélèvement spécifique sur cette valeur.
- **Le contre-exemple** [S] : **Cons. const., n° 2009-599 DC du 29 décembre 2009** (contribution carbone). Le Conseil censure le régime entier, parce que l'**importance des exemptions** était **contraire à l'objectif** poursuivi et créait une rupture d'égalité (93 % des émissions industrielles hors carburant étaient exonérées).
  - **Leçon** : chaque exclusion (les particuliers, l'IA locale, l'entraînement, le secteur public) doit être **cohérente avec l'objet de la loi** et ne doit pas vider l'assiette.
- **La confiscation** [S] : depuis la décision n° 2012-662 DC, un **taux marginal d'environ deux tiers** sur les revenus est regardé comme un seuil de risque (avis du Conseil d'État du 21 mars 2013). [À vérifier] Ce critère porte sur l'imposition des **revenus** d'un contribuable. Pour une **taxe sur la consommation d'un intrant**, répercutée dans les prix, le contrôle se fait plutôt sous l'angle de l'**égalité** et de la **liberté d'entreprendre**. Les accises sur le tabac représentent une part du prix comparable au plafond de la taxe Jevons. [À vérifier]
- **Les points faibles de la v0.1** :
  1. **Un tarif unique par octet** face à des prix qui varient d'un facteur 100 (Q26) : la charge serait sans rapport avec la valeur, ce qui est fragile au regard de l'objet même (« la moitié de la valeur »). **Piste** : un tarif **par classe de modèles** (A3).
  2. **Le plafond 4P** (80 % du coût total) : à **justifier** dans l'exposé et l'étude d'impact (le carburant, le tabac, le besoin de financement) ; m est voté par le Parlement. **Piste de repli** : un plafond à 3P.
  3. **L'exclusion des particuliers** : le critère « activité économique ou mission de service public » est objectif et en rapport avec l'objet (l'usage productif qui substitue au travail). Risque faible.
  4. **Le taux réduit de l'IA locale** : il doit reposer sur un critère objectif (l'exécution sur un **équipement terminal**, et non sur un serveur) et sur un objet affiché (ne pas freiner une technologie émergente, pour une durée limitée). Risque moyen (voir aussi O6).
- **Risque résiduel** : **moyen**. Il se réduit avec le tarif par classe et une étude d'impact solide.

### O3. Article 34 de la Constitution et incompétence négative (Q27)

- **Le texte** [S] : « La loi fixe les règles concernant l'assiette, le taux et les modalités de recouvrement des impositions de toutes natures. »
- **Le problème** : la v0.1 laisse un **arrêté trimestriel** relever le montant « lorsque les besoins l'exigent ». Le critère est indéterminé, ce qui est une **incompétence négative**, et il pourrait être censuré en contrôle *a priori* (en QPC, le grief n'est recevable que si un droit ou une liberté est affecté, comme le rappelle la décision 2025-1157 QPC [S]).
- **Pistes** :
  - (a) **recommandée** : la loi fixe la **formule** de l'indice P_k ; l'arrêté se borne à **constater** l'indice ; le **multiple m** est fixé **chaque année en loi de finances**, entre 1 et 4. La marge politique revient au Parlement, et la règle 50/50 reste un plancher légal.
  - (b) : la loi fixe m selon une **formule automatique** B/A, avec une définition légale de B (le coût constaté du chômage universel en N-1, moins les autres ressources) et des bornes. C'est plus fragile, car B dépend de choix de dépense.
- **Précédents d'indexation par arrêté selon une formule légale** [À vérifier] : la valeur forfaitaire de la taxe d'aménagement, revalorisée chaque année selon l'indice du coût de la construction ; la révision du Livret A (qui n'est pas un impôt).
- **Les coefficients par type de contenu** relèvent de l'**assiette** : ils doivent être **dans la loi**, ou dans une fourchette légale.
- **Risque résiduel** : **faible** avec la piste (a).

### O4. Affectation de la recette (Q60, Q61)

- **Les textes** [S] : depuis la loi organique n° 2021-1836 du 28 décembre 2021, l'article 2 de la LOLF prévoit que « les impositions de toutes natures ne peuvent être affectées à un tiers autre que ceux mentionnés au premier alinéa du présent II [notamment les collectivités et les organismes de sécurité sociale, À vérifier], et leur affectation ne peut être maintenue que si ce tiers est doté de la personnalité morale et si ces impositions sont en lien avec les missions de service public qui lui sont confiées », et que « l'affectation du produit d'une imposition de toute nature à un tiers **ne peut résulter que d'une disposition d'une loi de finances** ». L'article 21 de la LOLF permet un **compte d'affectation spéciale** pour des recettes « en relation directe » avec les dépenses. [S]
- **Le problème** : la v0.1 affecte la taxe à un « fonds de réserve » sans personnalité morale, par une loi ordinaire. Ce n'est pas possible.
- **Le cas de l'assurance chômage** : elle n'est **pas** un régime obligatoire de base de sécurité sociale, et elle est donc **hors du champ des LFSS** [À vérifier : l'effet de la LO n° 2022-354 sur l'information du Parlement]. L'Unédic reçoit déjà une **fraction de CSG** depuis 2019, en remplacement de la contribution salariale supprimée [À vérifier : la base légale exacte]. Le précédent d'une imposition affectée à l'assurance chômage existe donc.
- **Pistes** :
  - (a) **recommandée** : le **projet de loi Jevons est une loi ordinaire** pour la taxe et pour le chômage universel, et l'**affectation est inscrite dans la loi de finances** de l'année (un article de la LFI ou d'une LFR). Le bénéficiaire est un **établissement public administratif** à créer (une caisse nationale du chômage universel), avec une fraction à l'**Unédic** pour compenser la baisse des contributions patronales.
  - (b) : un **compte d'affectation spéciale** « Chômage universel » dans le budget de l'État, plus simple, mais qui protège moins la recette.
  - (c) : porter tout le texte en **loi de finances** (la taxe, l'affectation, le chômage universel). C'est possible pour la fiscalité, mais les dispositions sur le chômage universel seraient des **cavaliers budgétaires**. **À écarter.**
- **Point de vigilance** : le **plafonnement des taxes affectées** (art. 46 de la LFI pour 2012), dont l'excédent revient au budget général. Il faut prévoir l'exclusion de la taxe Jevons de ce plafond, ou un plafond élevé. [À vérifier]
- **Risque résiduel** : **faible**.

### O5. Territorialité, fournisseurs étrangers, cascade (Q31 à Q35)

- **Le critère** : l'**établissement du client professionnel** en France (comme pour les prestations de services entre entreprises en TVA). L'export, pour un client établi à l'étranger, est **hors du champ** (plutôt qu'au « taux zéro »), ce qui supprime la question du remboursement.
- **Les fournisseurs étrangers (Q32)** : la France ne peut pas exiger d'eux un **représentant fiscal** de façon disproportionnée lorsque l'assistance administrative existe [À vérifier : CJUE, Commission c/ Espagne, C-678/11]. Or la **directive 2011/16/UE** (DAC) s'applique à « tous les types de taxes », sauf la TVA, les droits de douane, les accises harmonisées et les cotisations sociales [S] : elle couvrirait donc la taxe Jevons, de même que la directive 2010/24/UE sur le recouvrement [À vérifier].
  - **Pistes** : (a) un **enregistrement simplifié, volontaire**, pour les fournisseurs, qui collectent alors la taxe (et leurs clients en sont déchargés) ; (b) à défaut, l'**autoliquidation** par le client, avec une **règle de conversion légale** des unités facturées (tokens, requêtes, forfait) en octet-équivalent, ou, en dernier recours, une base forfaitaire assise sur le montant facturé.
  - **Une obligation d'information** sur les factures (le volume en octet-équivalent) pour tout fournisseur qui s'adresse à des clients établis en France, sans formalité aux frontières.
- **La cascade (Q35)** : la **suspension** pour l'achat en vue de la revente (A2).
- **Les exportateurs qui utilisent de l'IA comme intrant (Q33)** : la taxe pèse sur leurs coûts. **Un remboursement à l'export n'est pas recommandé** : il serait une aide à l'exportation au regard du droit des aides d'État. La réponse passe par le **double dividende** (la baisse des contributions patronales) et par la sincérité de l'exposé, qui doit retirer « les exportateurs ne sont pas pénalisés ».
- **Les prestations produites à l'étranger avec de l'IA (Q34)** : on ne peut pas taxer le contenu en IA d'une prestation importée sans créer une taxe sur l'importation de services fondée sur leur mode de production. **Risque assumé**, à documenter dans l'étude d'impact.
- **Risque résiduel** : **moyen**, surtout pratique (le recouvrement auprès des acteurs non coopératifs).

### O6. Aides d'État (Q70)

- **Le cadre** [S] : la Cour admet une large **autonomie fiscale** des États pour définir le **système de référence** d'une taxe, à condition qu'il ne soit pas manifestement discriminatoire (CJUE, gr. ch., 16 mars 2021, **Commission c/ Hongrie, C-596/19 P**, et Commission c/ Pologne, C-562/19 P : une taxe progressive sur le chiffre d'affaires n'est pas sélective). Un **critère de distinction cohérent avec l'objectif** de la taxe n'est pas sélectif (CJUE, 26 avril 2018, **ANGED, C-233/16** : une taxe sur les grands établissements commerciaux) ; des exonérations sans lien avec cet objectif peuvent l'être. [S, le détail À vérifier]
- **Les mesures en cause** :
  - l'**abattement par entreprise**, ouvert à tous, est une **mesure générale** ; risque faible. Il faut une règle anti-fractionnement au niveau du groupe (Q42) ;
  - le **taux réduit de l'IA locale et embarquée** : risque **moyen**. Il favorise les entreprises qui exécutent sur des terminaux.
- **Pistes** :
  - (a) **définir le système de référence** de façon à ce que le critère soit objectif : l'inférence sur **équipement terminal** (portable, appareil embarqué) est soumise à un tarif propre, justifié par l'objet (ne pas freiner une technologie émergente, plus sobre) et **limité dans le temps** ;
  - (b) **notifier** préventivement le régime à la Commission (art. 108, § 3, TFUE) et le défendre au titre de l'article 107, § 3, c) ;
  - (c) le cas échéant, plafonner l'avantage au **règlement de minimis** (n° 2023/2831, 300 000 € sur trois ans) [À vérifier].
- **Risque résiduel** : **moyen**, réduit à **faible** si la notification aboutit.

### O7. OMC, AGCS, conventions fiscales (Q36)

- **L'AGCS** : le **traitement national** (art. XVII) interdit de traiter moins favorablement les services étrangers dans les secteurs où l'UE a pris des engagements (les services informatiques en font partie [À vérifier]). La taxe Jevons est **neutre quant à l'origine** : même tarif pour un fournisseur français ou étranger, et pour l'IA en nuage ou sur ses propres serveurs. L'exception de l'article XIV d) ne couvre que les **impôts directs**, elle ne servirait pas [À vérifier].
- **Le seul point sensible** : le **tarif réduit de l'IA sur terminal** pourrait être présenté comme une discrimination *de facto* contre la fourniture transfrontière (mode 1). Le critère ne dépend pas de l'origine (un modèle américain exécuté sur un portable en bénéficie). Risque faible.
- **Les conventions fiscales** : elles couvrent les impôts sur le revenu et la fortune. Seule la **clause de non-discrimination** (art. 24 du modèle OCDE) vaut pour les impôts de toute nature [À vérifier] : la neutralité quant à l'origine y répond.
- **Le risque politique** : la taxe française sur les services numériques a fait l'objet d'une enquête américaine (« section 301 ») et de menaces de représailles [À vérifier]. **Ce n'est pas un obstacle juridique**, mais il faut le documenter dans l'étude d'impact.

### O8. Les départements et l'article 72-2 (Q57)

- La substitution du socle au **RSA**, financé par les départements, est une **recentralisation** de compétence. Elle appelle une **compensation** au sens de l'article 72-2 de la Constitution, sous la forme d'une **reprise** par l'État des ressources transférées aux départements pour le RSA. [À vérifier : les expérimentations de recentralisation du RSA engagées depuis 2022]
- **Piste** : un titre dédié du dispositif, et la reprise des ressources en loi de finances. Risque faible.

### O9. Le compteur : directive 2015/1535, AI Act, RGPD (Q37, Q38, Q70)

- **Le problème** : une **obligation d'intégrer un compteur certifié** dans les logiciels d'exécution des modèles est une **règle technique** (ou une règle relative aux services de la société de l'information) qu'il faut **notifier** à la Commission, avec un délai de statu quo d'au moins trois mois (directive (UE) 2015/1535) [À vérifier]. Imposée aux **éditeurs** de logiciels libres étrangers, elle pourrait aussi être une **restriction** à la libre prestation de services et entrer en conflit avec le règlement (UE) 2024/1689 sur l'IA, qui harmonise les exigences applicables aux systèmes d'IA [À vérifier].
- **Piste recommandée** : déplacer l'obligation sur le **redevable** : tenir une **comptabilité-matière** des volumes, avec une obligation de résultat (des données exactes et contrôlables). Le **SDK libre et certifié** n'est qu'une **voie simplifiée**, qui vaut **présomption de bonne foi** (comme les logiciels de caisse certifiés). Le texte est **notifié** de toute façon.
- **Le RGPD et le secret des affaires** : le compteur ne transmet **que des volumes agrégés**, jamais le contenu (minimisation). Une analyse d'impact (AIPD) est à prévoir dans l'étude d'impact.
- **Risque résiduel** : **faible à moyen**.

### O10. Le chômage universel et le droit de l'Union (Q51)

- **Le socle**, non contributif et sans limite de durée, relève de l'**assistance sociale**. Il peut être soumis à une **condition de résidence**, conformément à la directive 2004/38/CE (art. 24) et à la jurisprudence de la Cour (Dano, C-333/13) [À vérifier]. Il peut aussi être qualifié de **prestation spéciale en espèces à caractère non contributif**, non exportable (règlement (CE) n° 883/2004, art. 70) [À vérifier].
- **Le complément** reste une prestation d'**assurance chômage**, coordonnée selon les règles habituelles.
- **L'absence d'obligation de recherche d'emploi** est un **choix du législateur**, sans obstacle juridique connu ; elle inverse en revanche la logique de la loi « plein emploi » de 2023 pour le RSA, qu'il faudra modifier. [À vérifier]

---

## D. Réponses aux contestations et vérifications (M2 à M6)

### D1. Le tarif m × P_k est-il « proportionnel au prix » au sens de l'article 401 ? (contestation du point 3)

**Réponse : non. Et même s'il l'était, la taxe resterait compatible.** La démonstration tient en trois temps.

1. **Le 2ᵉ critère porte sur le prix de chaque transaction.** La Cour le formule ainsi : « la fixation de son montant **proportionnellement au prix perçu par l'assujetti en contrepartie des biens et des services qu'il fournit** » (Banca Popolare di Cremona, C-475/03 ; Dansk Denkavit, C-200/90, pt 11 ; Pelzl, C-338/97, pt 20) [S, via le rapport du CPO de 2015 et le rapport particulier de la Cour des comptes de 2023].
   - Avec m × P_k, **deux transactions de même volume dans la même classe paient la même taxe**, quel que soit leur prix. Un fournisseur qui facture deux fois le prix moyen ne paie pas deux fois plus de taxe. Le montant ne dépend **pas** du prix perçu par l'assujetti.
   - P_k est une **donnée statistique** (une moyenne de marché, constatée sur une période **antérieure**, publiée par un organisme indépendant). C'est un **paramètre du tarif**, pas l'assiette. La taxe est donc un **droit spécifique**, c'est-à-dire un montant par unité de volume, comme une accise. Or l'article 401 nomme expressément les **accises** parmi les impositions permises.
   - Dans Banca Popolare di Cremona, la Cour a écarté la qualification de taxe sur le chiffre d'affaires parce que l'assiette de l'IRAP n'était **pas strictement proportionnelle** au prix des fournitures [S]. **L'exigence est donc stricte**, et une indexation sur une moyenne ne la satisfait pas.
2. **Même un impôt proportionnel au prix est permis s'il manque les autres caractéristiques.** Un impôt qui ne présente pas les caractéristiques essentielles de la TVA n'est pas interdit (Solisnor, C-130/96 ; GIL Insurance, C-308/01, pt 34). Une taxe qui ne frappe qu'une catégorie de services n'est pas incompatible (GIL Insurance) [S]. Les exemples sont nombreux :
   - la Cour a validé des **taxes sectorielles assises sur le chiffre d'affaires** (Vodafone, C-75/18 ; Tesco-Global, C-323/18, 2020) et une **taxe sur les ventes** (KÖGÁZ, C-283/06, 2007) [S] ;
   - la France applique **plus d'une trentaine de taxes spéciales sur le chiffre d'affaires** à côté de la TVA, qui sont toutes proportionnelles au prix (le BOFiP les recense dans la série BOI-TCA) [S, rapport particulier de la Cour des comptes, 2023] ; la taxe sur les services numériques (3 % des sommes encaissées) en fait partie.

   Or la taxe Jevons n'a **ni l'application générale, ni la perception à chaque stade, ni la déduction** (décision 37).
3. **La limite à ne pas franchir** : l'arrêt Dansk Denkavit, où la Cour a censuré une contribution danoise **générale**, assise sur une base proche de la valeur ajoutée [S]. La taxe Jevons s'en éloigne sur tous les points.

**Pourquoi je ne recommande pas l'alternative** (un tarif en euros par unité, fixé par la loi et revalorisé chaque année) [C] :
- elle est juridiquement **encore plus sûre** au regard de l'article 401 (c'est une accise pure) ;
- mais **les prix de l'IA baissent très vite** (d'un facteur de l'ordre de 10 par an selon le corpus, fichier 10 [À vérifier]). Un tarif fixé pour un an dépasserait le prix réel en quelques mois, puis **franchirait le plafond de 4P**. Cela violerait à la fois l'intention (le 50/50 deviendrait un 90/10) et l'égalité devant les charges publiques (D3) ;
- c'est **l'indexation trimestrielle** qui garantit à la fois le plancher et le plafond.
- **Elle reste un repli**, au cas où l'expertise jugerait l'indexation risquée : un tarif voté chaque année, avec une **clause de réduction automatique** si l'indice franchit 4P.

**Les trois classes** [C] :
- le critère de classement est le **prix catalogue public par unité** du modèle, dans **trois tranches** dont les bornes sont **fixées par la loi**, exprimées en fractions de l'indice global (par exemple : moins de 0,2 fois l'indice, entre 0,2 et 2 fois, plus de 2 fois). Une **fonction en escalier** n'est pas une proportionnalité au prix, et le classement est vérifiable ;
- les offres **au forfait** ou intégrées sans prix unitaire sont rangées par défaut dans la classe médiane, avec une option pour le classement réel ;
- **un critère écarté** : la taille du modèle (le nombre de paramètres), qui n'est pas vérifiable pour les modèles fermés.
- **Contre la manipulation (Q24)** : P_k est calculé par l'**INSEE** [À confirmer] à partir des prix catalogue et d'un échantillon de transactions, et **non** à partir des seules déclarations des redevables.

**Proposition** : lever la condition de la décision 39. → **Levée en M3 (décision 48 [P]).**

### D2. Le plancher m ≥ 1 respecte-t-il « au moins la moitié de la valeur au bien commun » ? (vérification du point 4)

- **Le calcul.** Pour un volume V de la classe k, le client paie V × p (le prix) plus V × m × P_k (la taxe). La part du bien commun dans le coût total hors TVA vaut **m P_k / (p + m P_k)**.
- **En moyenne dans la classe**, p = P_k, et cette part vaut **m / (1 + m)** :

| m | Part du bien commun dans le coût total hors TVA |
|---|---|
| 1 | **1/2** |
| 2 | 2/3 |
| 3 | 3/4 |
| 4 | 4/5 |

- **Conclusion** : **oui**, m ≥ 1 garantit au moins la moitié **de la valeur marchande**, en moyenne et dans chaque classe. L'intention est respectée.
- **Trois nuances, à dire dans l'exposé** :
  1. **Transaction par transaction**, la part est inférieure à 1/2 pour un service plus cher que la moyenne de sa classe, et supérieure pour un service moins cher. C'est le prix de la neutralité au regard de l'article 401 (D1).
  2. **Le décalage temporel joue dans le sens de l'intention** : P_k est constaté sur le trimestre précédent, et les prix baissent. La part réelle est donc en général un peu **supérieure** à 1/2.
  3. **Deux exceptions assumées** font descendre la part sous 1/2 : l'**abattement** et le **taux réduit** de l'IA sur équipement terminal. Elles sont **temporaires ou limitées**, et elles découlent elles-mêmes de l'intention (« ménager ce qui démarre »).
- **Précision de vocabulaire** : la « valeur » s'entend de la **valeur marchande** (le prix payé). Le surplus du client, c'est-à-dire la valeur d'usage au-delà du prix, n'est pas mesurable et n'est pas visé.

### D3. Le plafond 4P est-il confiscatoire ? Le seuil des deux tiers est-il pertinent ? (vérification du point 5)

- **Ce qu'est le contrôle de confiscation.** Selon le Conseil constitutionnel, l'exigence d'égalité ne serait pas respectée si l'impôt revêtait un caractère confiscatoire ou faisait peser sur une catégorie de contribuables une charge excessive au regard de leurs facultés contributives (décision 2005-530 DC, reprise depuis) [S, commentaire de la décision 2018-755 QPC]. La doctrine décrit l'impôt confiscatoire comme celui qui, excédant les revenus du contribuable, l'obligerait à céder une partie de son patrimoine [S, *Nouveaux Cahiers du Conseil constitutionnel*]. **Le Conseil n'a jamais censuré d'impôt sur la consommation pour ce motif** [À vérifier].
- **Le seuil des deux tiers** (décision 2012-662 DC, et l'avis du Conseil d'État du 21 mars 2013) [S] est un **taux marginal maximal** calculé en **additionnant tous les prélèvements sur un même revenu d'un même contribuable**. **Il n'est pas pertinent juridiquement** pour la taxe Jevons, pour trois raisons :
  1. elle ne frappe **aucun revenu** : elle frappe une **dépense** d'exploitation, volontaire et proportionnée à l'usage ;
  2. son redevable légal (le fournisseur qui collecte) ne la supporte pas sur son revenu, et le client professionnel la **déduit de son résultat imposable** comme une charge [À vérifier] ;
  3. elle est **répercutée** dans les prix, comme toute accise.
- **Il reste utile comme repère politique** : à **m = 2**, la taxe représente exactement **les deux tiers** du coût total hors TVA. On peut afficher dans l'exposé qu'**au-delà de m = 2**, le relèvement exige une justification renforcée dans le rapport annexé au projet de loi qui fixe m [C].
- **Le contrôle pertinent est celui de l'égalité et de la liberté d'entreprendre** :
  - **l'appui principal** est la décision **2025-1157 QPC** (§ 48 et § 59 : la taxe sur les services numériques, assise sur des sommes encaissées, ne crée ni capacité contributive fictive ni effet confiscatoire) [S] ;
  - **le parallèle avec les accises** : les taxes sur le tabac représentent environ 80 % du prix de vente, et celles sur le carburant environ 60 % [À vérifier]. Aucune n'a été jugée confiscatoire [À vérifier]. Le plafond 4P (80 % du coût hors TVA) est **du même ordre que le tabac** ;
  - **les impositions comportementales**, honnêtement : je n'ai pas trouvé de décision du Conseil qui pose une doctrine propre aux impositions « comportementales » en matière de confiscation [À vérifier par un juriste]. Surtout, la taxe Jevons **n'est pas principalement comportementale** : son objet est le **rendement** et la **redistribution de la valeur**, l'incitation à la sobriété n'étant qu'un objet secondaire. **Il ne faut donc pas fonder la défense du plafond sur la logique du tabac** (dissuader), mais sur celle de la décision 2025-1157 QPC : une valeur qui repose de façon déterminante sur une ressource commune.
- **Les garde-fous qui rendent 4P défendable** [C] : m est voté chaque année par le Parlement, sur rapport ; le plafond est une borne et non un objectif ; l'abattement protège les petits usages ; l'étude d'impact doit montrer que la taxe **n'empêche pas l'exercice** d'une activité (l'élasticité, les alternatives).
- **Risque résiduel** : **faible** pour le principe, **moyen** si m approche 4 sans justification.

### D4. Affectation : quelle voie protège le mieux le chômage universel ? (point 6)

**Les textes** [S] :
- LOLF, art. 2 (rédaction de la LO n° 2021-1836) : une imposition ne peut être affectée à un tiers que par une **loi de finances** ; le tiers doit avoir la personnalité morale et des missions de service public en lien avec la taxe ; les organismes de sécurité sociale font partie des affectataires admis [À vérifier : la rédaction exacte du premier alinéa du II].
- LOLF, art. 21 : un **compte d'affectation spéciale** retrace des opérations financées par des recettes « par nature, en relation directe avec les dépenses concernées ».
- Code de la sécurité sociale, **art. LO 111-3-14** (LO n° 2022-354) : l'affectation, totale ou partielle, d'une **recette exclusive** des régimes obligatoires de base, ou des organismes qui concourent à leur financement ou à la mise en réserve de recettes à leur profit, **à toute autre personne morale ne peut résulter que d'une loi de financement**. C'est un **cliquet organique** : une loi de finances ne peut pas reprendre la recette.
- Le **plafonnement des taxes affectées** (art. 46 de la LFI pour 2012) vise les taxes affectées aux **opérateurs et organismes** énumérés, dont l'excédent revient au budget général [À vérifier : l'exclusion de fait des recettes de la sécurité sociale].

**La comparaison** [C] :

| Critère | (a) Établissement public, par loi de finances | (b) Compte d'affectation spéciale | (c1) Branche de sécurité sociale, par LFSS | (c2) Fraction vers l'Unédic, sur le modèle de la CSG |
|---|---|---|---|---|
| Base | LOLF, art. 2 | LOLF, art. 21 | LOLFSS ; code de la sécurité sociale | LFSS [À vérifier] |
| La recette quitte-t-elle le budget de l'État ? | Oui | **Non** : elle reste dans le budget de l'État, mais hors du budget général | Oui | Oui |
| Protection contre une reprise | **Faible** : toute loi de finances peut la réaffecter ou la plafonner | **Faible** : le compte et son solde dépendent de chaque loi de finances | **Forte** : seule une LFSS peut la réaffecter (art. LO 111-3-14) | Moyenne : la fraction est révisée chaque année |
| Plafonnement des taxes affectées | Exposé : il faut une exclusion explicite, qu'une loi de finances ultérieure peut supprimer | Sans objet | **Hors du dispositif** [À vérifier] | Hors du dispositif |
| Pilotage par le Parlement | Le vote de m en loi de finances | Le vote des crédits | **Le vote de m et de l'objectif de dépenses de la branche en LFSS** | Indirect |
| Cohérence avec l'objet | Bonne | Moyenne | **Très bonne** : la protection sociale, sous le contrôle de la LFSS | Bonne pour le complément et le double dividende |
| Précédents | Nombreux opérateurs | Le CAS Pensions | La **branche autonomie** (2020), financée par une fraction de CSG ; les **fonds** du champ de la LFSS (FRR, ancien FSV) [À vérifier] | La CSG versée à l'Unédic depuis 2019 [À vérifier] |
| Lourdeur | Faible | Faible | **Élevée** : une loi organique peut être nécessaire pour créer la branche [À vérifier] | Faible |

**Recommandation** [C] : une **architecture mixte**, centrée sur la voie (c1).
1. **Le socle** du chômage universel est une **prestation d'un régime obligatoire de base de sécurité sociale**. Il peut s'agir d'une nouvelle branche « chômage universel », gérée par une caisse nationale, ou d'une prestation rattachée à une branche existante. Pour éviter la dilution, je recommande une **branche propre**. Le **versement peut être confié aux CAF**, qui versent déjà le RSA.
2. **La taxe Jevons est une recette exclusive** de cette branche, affectée par la loi Jevons puis confirmée en **LFSS** chaque année. Elle bénéficie du **cliquet de l'article LO 111-3-14**.
3. **Le fonds de réserve** est un organisme de **mise en réserve de recettes** au profit de la branche, sur le modèle du **FRR**. Il est protégé par le même cliquet.
4. **Le double dividende** : une **fraction** de la taxe est versée à l'**Unédic** en compensation de la baisse des contributions patronales, sur le modèle de la CSG (c2), en LFSS.
5. **Le complément** proportionnel reste une prestation d'**assurance**, gérée par l'Unédic.
6. **m est voté en LFSS**, ce qui précise la décision 40 (« voté par le Parlement »).
7. **Une loi organique**, si elle est nécessaire pour créer la branche dans le cadre des LFSS, fait partie des outils du mandat (point 4).

**Pourquoi c'est le plus robuste dans la durée** : c'est la seule voie où une **règle organique** interdit à une loi de finances de reprendre la recette. Elle échappe au plafonnement des taxes affectées, et elle inscrit le chômage universel dans la **sécurité sociale**, ce qui l'expose moins aux arbitrages budgétaires annuels de l'État.

**Ses limites** : elle est plus lourde à créer, et elle ne protège pas contre une LFSS ultérieure. Aucune voie ne protège contre une majorité future ; seule une révision constitutionnelle le ferait, ce qui est une étape ultérieure au sens du mandat.

**Le repli** : la voie (a), avec une exclusion explicite du plafonnement.

**Le CAS (b) est déconseillé** : la recette resterait dans le budget de l'État, ce qui va contre l'exigence posée par la décision 42.

→ **Arrêtée en M3 (décision 49 [P])**, après la vérification de D6.

### D5. Le secteur public : l'effet budgétaire circulaire (point 10)

- **L'État** paie la taxe sur son propre usage de l'IA professionnelle. Avec la voie D4, cette taxe est un **transfert de l'État vers la sécurité sociale**. Il est **neutre pour le solde des administrations publiques** prises ensemble (au sens de Maastricht), et **positif pour le chômage universel**. Il a un coût de gestion, et il rend visible le coût réel de l'IA dans l'administration.
- **Les collectivités, les hôpitaux et les universités** supportent une **charge réelle**. L'article 72-2 n'impose pas de compensation, puisque la taxe n'est ni un transfert ni une création de compétences [À vérifier]. L'État peut toutefois choisir de la compenser par les dotations, ce qui serait circulaire.
- **Les associations** supportent une charge réelle, atténuée par l'abattement.
- **L'ordre de grandeur** : si le secteur public pèse environ 10 % de la dépense professionnelle d'IA [À vérifier], la taxe qu'il paie représente environ 10 % de la recette, dont une partie seulement est un vrai coût net pour les administrations publiques.
- **Ce qu'on y gagne** : la cohérence du critère, en écho à la décision 2009-599 DC, et une incitation à la sobriété dans l'administration.
- **Le risque** : un frein à l'adoption de l'IA publique. Il est atténué par l'abattement et par le taux réduit sur équipement terminal.

---

### D6. La branche de sécurité sociale face au règlement 883/2004, au RSA et à l'ASS (M3, point 2)

**1. La classification du socle ne dépend pas de la voie d'affectation.**
- La Cour de justice qualifie une prestation d'après ses **caractéristiques** (ses conditions d'octroi, son objet, son financement), et non d'après son rattachement en droit national [À vérifier : Hoeckx, C-249/83 ; Molenaar, C-160/96]. Le RSA, versé par les CAF, est par exemple regardé comme de l'assistance sociale [À vérifier].
- **La question se pose donc à l'identique avec l'établissement public de repli.** Elle ne fait pas tomber la voie « sécurité sociale », qui est arrêtée (décision 49 [P]).

**2. Les trois qualifications possibles du socle** [C] :

| Qualification | Conditions | Conséquences | Accessible en droit actuel ? |
|---|---|---|---|
| **Assistance sociale** (exclue du règlement, art. 3, § 5) | Un octroi largement discrétionnaire, sous condition de besoin apprécié au cas par cas | Le règlement ne s'applique pas ; seule la directive 2004/38 joue (Dano, C-333/13) | **Non** : le socle est un **droit subjectif**, ouvert sur simple inscription |
| **Prestation spéciale en espèces à caractère non contributif** (art. 70, annexe X) | Un caractère mixte (sécurité sociale et assistance), un financement exclusif par l'impôt, un revenu minimal de subsistance lié à l'environnement social, **et une inscription à l'annexe X** | Elle est servie **uniquement dans l'État de résidence**, **sans exportation** [S, Cleiss]. Précédents : l'ASPA française [S, CE, 16 avril 2019, n° 423586] et le minimum allemand pour les demandeurs d'emploi (Alimanovic, C-67/14) | **Non** : l'inscription à l'annexe X exige de **modifier le règlement** (procédure législative de l'Union). C'est une **étape ultérieure** |
| **Prestation de chômage** (art. 3, § 1, h) | Un droit lié à l'absence d'emploi, accordé selon des critères légaux | Le régime de droit commun du chapitre 6 (voir ci-dessous) | **Oui** : c'est la **qualification par défaut** |

**3. Les conséquences de la qualification « prestation de chômage »** [C, À vérifier par un spécialiste de la coordination] :
- **La condition de résidence.** Pour une personne sans activité, la législation applicable est celle de l'**État de résidence** (art. 11, § 3, e). La France peut subordonner le socle à un **droit au séjour**, au sens de la directive 2004/38. Cette discrimination indirecte est justifiée par la protection des finances de l'État d'accueil : la Cour l'a admis pour des prestations de **sécurité sociale** (Commission c/ Royaume-Uni, **C-308/14**, 14 juin 2016) [S]. Le coût reste donc comparable à celui du RSA actuel, qui exige déjà un droit au séjour pour les ressortissants de l'Union [À vérifier].
- **L'exportation.** Elle est limitée à **3 mois**, prolongeables jusqu'à 6, pour un chômeur **inscrit** qui part chercher un emploi dans un autre État membre (art. 64). Le socle n'impose pas de recherche ; mais celui qui veut l'exporter doit s'inscrire dans l'État d'arrivée. Le coût est faible.
- **La totalisation des périodes** est **sans objet pour le socle**, qui n'exige aucune période d'assurance. Pour le **complément**, rien ne change : l'ARE y est déjà soumise.
- **Les frontaliers.** Un frontalier résidant en France et totalement privé d'emploi est indemnisé par l'**État de résidence** (art. 65). La France leur verse déjà l'ARE, avec un remboursement partiel par l'État d'emploi [À vérifier : le montant et la révision du règlement en cours depuis 2016]. Le socle s'ajouterait pour ceux qui n'ont pas droit à l'ARE. **C'est le principal surcoût**, à chiffrer dans l'étude d'impact.
- **Un levier de conception**, à trancher en M6 avec la question 50 : une **condition de ressources** rapprocherait le socle du caractère mixte de l'article 70. Elle préparerait son inscription à l'annexe X, mais elle **changerait l'intention** (le socle pour toute personne sans emploi). **Je ne la recommande pas** à ce stade.
- **L'égalité de traitement** (art. 4) : un ressortissant de l'Union qui réside légalement en France a les mêmes droits qu'un Français. C'est conforme à l'intention.

**4. Le transfert du RSA vers la branche.**
- **Le précédent** [S] : l'art. 43 de la **loi de finances pour 2022** autorise, pour cinq ans, la **recentralisation** de l'instruction, de l'attribution et du financement du RSA dans les départements volontaires (la Seine-Saint-Denis et les Pyrénées-Orientales depuis 2022, par le décret n° 2022-322 du 4 mars 2022). La gestion est confiée aux **CAF** et aux caisses de MSA. L'État **reprend** les compensations versées au titre de la décentralisation du RSA (des fractions de TICPE), puis, si elles ne suffisent pas, une partie des droits de mutation. La décision n° 2021-833 DC n'a pas censuré ce dispositif [À vérifier].
- **La piste** [C] : une **recentralisation générale** du RSA, au profit de la branche, avec la **reprise des ressources** de chaque département, calculée sur la dépense d'une période de référence. La reprise de ressources fiscales relève d'un **article de loi de finances**.
- **L'article 72-2** : il impose de compenser un **transfert** de compétences vers une collectivité. Pour une **reprise** par l'État, la question est l'inverse : il faut reprendre les ressources sans aller au-delà de ce qui avait été transféré. Le modèle de 2022 y répond [À vérifier : la jurisprudence sur les reprises de compétences].
- **Ce que gardent les départements** : l'**accompagnement social et l'insertion**, qui sont volontaires pour le bénéficiaire, puisque le socle n'impose aucune obligation. Il faut modifier la loi « plein emploi » de 2023, qui conditionne le RSA à des heures d'activité [À vérifier].

**5. Le transfert de l'ASS.** L'ASS est financée par le **budget de l'État** [À vérifier]. Sa dépense est transférée à la branche par une **contribution de l'État**, fixée en LFSS sur le coût de la dernière année, puis indexée.

**6. Le véhicule de création de la branche.**
- **Le précédent** [S] : la **5ᵉ branche** (l'autonomie) a été créée par la **loi organique n° 2020-991** et la **loi n° 2020-992** du 7 août 2020, puis organisée par la **LFSS pour 2021** (art. 32, une habilitation) et par l'**ordonnance n° 2021-1554** du 1ᵉʳ décembre 2021. La CNSA est devenue la caisse nationale de la branche.
- **La piste** [C] : un **projet de loi organique**, qui adapte la LOLFSS si la liste des branches doit y figurer [À vérifier : l'apport exact de la LO n° 2020-991], et un **projet de loi ordinaire**, la loi Jevons, qui crée la branche « chômage universel », sa caisse nationale (un établissement public) et la taxe. Une **LFSS** affecte ensuite les recettes et fixe m, et un **article de loi de finances** organise la reprise des ressources du RSA.
- **Le calendrier** : la loi organique et la loi ordinaire sont examinées ensemble, comme en 2020. La branche entre en vigueur au 1ᵉʳ janvier suivant la première LFSS qui l'intègre.

**7. Un flux à préciser en M6.** Quand le socle est versé à tous les chômeurs, l'ARE devient un **complément** au-dessus du socle. L'Unédic **économise** la part « socle » de l'ARE actuelle. Cette économie doit être **reversée à la branche**, ou s'imputer sur la fraction versée à l'Unédic. Sinon, le besoin net de 16 à 20 Md€ (note 05) serait faux.

### D7. L'usage professionnel par un compte grand public : une règle qui ferme la faille (contestation de M3)

**La faille** : la règle de M2 (« sans identifiant, le client est traité comme un particulier ») permettait à une entreprise d'échapper à la taxe en utilisant des comptes grand public.

**La règle proposée** [C] :
1. **Le fournisseur doit demander**, à la souscription et à chaque renouvellement, si l'usage est professionnel et, si c'est le cas, l'identifiant (le SIREN, ou le numéro de TVA intracommunautaire vérifié par VIES). La réponse est une **déclaration** du client, que le fournisseur conserve. Un fournisseur de bonne foi n'est pas responsable d'une fausse déclaration.
2. **L'usage professionnel est présumé**, sauf preuve contraire du client, dans quatre cas :
   - (a) un accès par **API** ;
   - (b) un **paiement par une entreprise** (un moyen de paiement ou une facture au nom d'une entreprise) ;
   - (c) une offre destinée aux **équipes ou aux entreprises** ;
   - (d) un **volume** au-delà d'un seuil élevé, fixé par la loi (par exemple dix fois l'usage médian d'un abonnement grand public).

   Dans ces cas, le fournisseur applique la taxe, ou demande l'identifiant.
3. **Le redevable de dernier ressort est l'entreprise.** Une entreprise qui fait un usage professionnel par un compte grand public (le sien, ou celui de ses salariés, remboursé en note de frais) **autoliquide** la taxe. Faute de relevé de volume, elle la calcule sur un **volume forfaitaire par compte**, fixé par la loi et rattaché à la classe médiane.
4. **Les sanctions** : l'entreprise qui n'a pas autoliquidé paie la taxe éludée, avec les intérêts de retard et une **majoration**, plus forte en cas de manquement délibéré (sur le modèle de l'art. 1729 du CGI, À vérifier). Une **fausse déclaration** d'usage personnel est passible d'une amende fixe. **Le salarié n'est jamais redevable.**
5. **La protection des particuliers** : un particulier qui dépasse le seuil de volume peut renverser la présomption par une simple déclaration d'usage personnel. Il ne paie rien. Les fausses déclarations relèvent du contrôle a posteriori.
6. **La diligence de l'employeur** : une entreprise qui met des comptes professionnels à la disposition de ses salariés et qui interdit l'usage de comptes personnels pour le travail n'est pas sanctionnée pour un usage isolé qu'elle ignorait. Elle doit la taxe seulement sur l'usage qu'elle connaît ou qu'elle rembourse.

**La compatibilité avec le RGPD** [C, À vérifier par un DPO] :
- **La base légale** est une **obligation légale** (art. 6, § 1, c) du RGPD.
- **La minimisation** (art. 5, § 1, c) :
  - le fournisseur ne collecte qu'une **déclaration** (professionnel ou personnel) et, pour un professionnel, un **identifiant d'entreprise**. Le SIREN d'une personne morale n'est pas une donnée personnelle ; celui d'un entrepreneur individuel l'est, mais il est strictement nécessaire ;
  - le **seuil de volume** est calculé à partir des données de **facturation** que le fournisseur traite déjà. Aucune donnée nouvelle n'est collectée, et **le contenu des requêtes n'est jamais traité** à des fins fiscales ;
  - **aucune liste de particuliers n'est transmise** à l'administration. Seules les déclarations agrégées par client professionnel le sont. L'accès aux déclarations conservées se fait **au cas par cas**, lors d'un contrôle, par le droit de communication [À vérifier : art. L. 81 du LPF].
- **Une variante plus intrusive**, que je ne recommande pas à ce stade : une transmission automatique des comptes grand public au-delà d'un seuil très élevé, sur le modèle des déclarations des plateformes (DAC7) [À vérifier].
- **Les garanties** : une analyse d'impact (AIPD), et la **consultation de la CNIL** sur le projet de loi (art. 36, § 4, du RGPD).

### D8. Le fonds de réserve et l'ordre d'emploi des recettes (Q61, Q62, Q64, Q65)

- **Le fonds de réserve** [C] : un organisme de **mise en réserve** au profit de la branche, sur le modèle du FRR, protégé par l'art. LO 111-3-14.
  - **Sa cible** : ~~six mois de prestations du socle~~ → **six mois du besoin net financé par la taxe, formation comprise** (décision 81). Une fois la cible atteinte, l'excédent est employé selon l'ordre ci-dessous ; un tiers de l'excédent compte pour ramener m à 2 (décision 94).
  - **Sa gestion** : un conseil de surveillance (l'État, des parlementaires, les partenaires sociaux) et des **règles de placement prudentes** fixées par décret.
  - **Son usage** : il est mobilisable par la LFSS en cas de retournement.
- **L'ordre d'emploi des recettes** [C], qui interprète la décision 30 [G] comme le fait le script `sim_v3.py` :
  1. le **financement des droits déjà ouverts** ;
  2. la **reconstitution du fonds de réserve**, jusqu'à sa cible ;
  3. ~~le **surplus**, partagé **moitié-moitié** entre l'extension des droits et la baisse des contributions patronales~~ → **↺ décision 75 [opus-5.5 as ggim]** : le **surplus va aux droits** (la hausse du socle) **jusqu'au socle cible** ;
  4. **une fois le socle cible atteint**, le surplus est **partagé moitié-moitié** entre les droits et la baisse des contributions patronales. ~~La part « droits » finance alors l'indexation du socle et les extensions votées en LFSS~~ → **décision 106 (M14)** : l'évolution du socle comme le revenu médian est un **droit prioritaire**, financé au rang 1 (comme dans le script) ; la moitié « droits » ne finance plus que les extensions votées en LFSS ; à défaut, elle revient à la baisse des cotisations, qui n'est engagée que si elle est soutenable avec m ≤ 2 (décision 89).
- **Pourquoi la décision 75** : le partage dès l'ouverture doublait l'effort, et la cible n'était atteinte qu'avec m = 4 (note 19, sans indexation). **M9** : la moitié « droits » est précisée (décision 80), m est ramené à 2 au plus après la cible (79), et la cible du fonds est de six mois du besoin net (81). Le chômage universel est le vrai but ; le double dividende est différé, pas abandonné. **Le dispositif doit écrire la règle ainsi**, reprise du partage comprise.
- **En cas de retournement (Q62)** :
  1. le fonds de réserve est mobilisé ;
  2. la LFSS **relève m**, dans la limite de 4 ;
  3. la **baisse des cotisations** est suspendue avant toute réduction des droits ;
  4. en dernier ressort, une **contribution d'équilibre de l'État**, votée en LFSS, intervient, comme pour les autres branches.
- **Cela règle la tension de Q65** : relever m pour financer les droits ne déclenche plus mécaniquement une baisse des cotisations, puisque le partage ne porte que sur le surplus. *(M7 [opus-5.5] : c'était vrai pour les droits déjà ouverts, mais pas pour la montée vers la cible, où la moitié de chaque euro relevé partait encore aux cotisations. La décision 75 règle Q65 pour de bon.)*
- **Quand la contribution patronale atteint zéro (Q64)** : le surplus va au fonds de réserve, puis la LFSS **abaisse m**, sans descendre sous le plancher m = 1.


---

### D9. La garantie de non-régression pour les bénéficiaires du RSA et de l'ASS (M4, décision 55)

**Le risque est réel.** Le socle est **individuel** (environ 1 200 € par mois par adulte sans emploi, note 05 [À vérifier]), alors que le RSA est **familialisé**. Une comparaison indicative, avec un montant forfaitaire du RSA d'environ 650 € pour une personne seule [À vérifier pour 2026] et les coefficients du barème [À vérifier] :

| Foyer sans autre ressource | RSA (environ, avant le forfait logement) | Socle (adultes sans emploi) | Écart |
|---|---|---|---|
| Une personne seule | 650 € | 1 200 € | **+** |
| Un couple sans enfant | 975 € | 2 400 € | **+** |
| Un couple avec 2 enfants | 1 365 € | 2 400 € | **+** |
| Un parent isolé avec 1 enfant (RSA majoré) | 1 110 € | 1 200 € | + (faible) |
| **Un parent isolé avec 2 enfants (RSA majoré)** | **1 390 €** | 1 200 € | **−** |
| **Un parent isolé avec 3 enfants (RSA majoré)** | **1 670 €** | 1 200 € | **−** |
| Un couple avec 6 enfants | environ 2 700 € | 2 400 € | **−** |

**Les autres risques de régression** : les **droits connexes** du RSA (la complémentaire santé solidaire gratuite, les tarifs sociaux, certaines aides locales) [À vérifier] ; la **validation de trimestres de retraite** que procure l'ASS, et que le socle doit reprendre ; le cumul avec la **prime d'activité**, qui doit rester au moins aussi favorable.

**Le mécanisme proposé** [C] :
1. **Une garantie familiale permanente.** Le foyer reçoit le plus élevé de deux montants : la somme des socles de ses membres, ou le **montant du RSA**, majoration comprise, calculé selon le barème en vigueur à la date de la bascule, puis ~~revalorisé comme le socle~~ → **revalorisé comme le RSA** (décision 108, M14 : la non-régression se mesure par rapport au droit actuel ; indexée sur le socle, la garantie coûterait environ 4,3 Md€ à la cible). L'écart est versé par la CAF sous la forme d'un **complément familial de garantie**. Il est **permanent** et vaut pour les nouveaux demandeurs, faute de quoi un parent isolé futur serait moins bien traité qu'aujourd'hui.
2. **Le maintien des droits connexes.** Tout droit aujourd'hui attaché à la qualité d'allocataire du RSA est attaché à celle de bénéficiaire du socle (ou de la garantie familiale). Un article de coordination modifie les codes concernés [À vérifier : l'inventaire de ces droits].
3. **Les trimestres de retraite.** Les périodes de socle sont des **périodes assimilées**, au moins dans les conditions applicables aujourd'hui à l'ASS.
4. **La prime d'activité est maintenue.** La sortie progressive du socle (environ 50 centimes perdus par euro gagné, note 05) s'articule avec elle selon une règle qui garantit qu'**aucun travailleur modeste ne perd** par rapport au droit actuel. Le **calcul différentiel** est fait par la CAF.
5. **Une clause de sauvegarde individuelle**, à la bascule. Chaque bénéficiaire du RSA ou de l'ASS reçoit au moins, pendant cinq ans, le montant qu'il percevait la veille, revalorisé. Elle couvre les cas que la règle générale n'aurait pas prévus.
6. **Une démonstration chiffrée** par cas types (un parent isolé, une famille nombreuse, un couple avec un actif modeste, un bénéficiaire de l'ASS en fin de carrière), à faire en **M6** et à intégrer au chiffrage. Le coût de la garantie familiale porte surtout sur les parents isolés avec deux enfants ou plus [À vérifier : leur nombre parmi les allocataires du RSA majoré].

### D10. La condition de séjour du socle, comparée à celle du RSA (M4, décision 56)

**Le RSA aujourd'hui** [S] :
- un ressortissant d'un **pays tiers** doit être titulaire **depuis au moins cinq ans** d'un titre de séjour autorisant à travailler (art. L. 262-4 du CASF) ;
- cette condition **ne s'applique pas** aux réfugiés, aux bénéficiaires de la protection subsidiaire, aux apatrides, aux titulaires de la carte de résident ou d'un titre équivalent, ni aux **bénéficiaires du RSA majoré**, pour qui la régularité du séjour suffit ;
- la condition a été jugée conforme aux droits fondamentaux (CE, 10 juillet 2015, n° 375887) [S] ;
- un **ressortissant de l'Union** doit disposer d'un droit au séjour (art. L. 262-6 du CASF) [À vérifier].

**La contrainte nouvelle du droit de l'Union.** Si le socle est une **prestation de chômage**, il relève des « branches de sécurité sociale » du règlement 883/2004. La **directive 2011/98/UE** (le permis unique), art. 12, § 1, e, impose alors l'égalité de traitement aux travailleurs de pays tiers. Selon l'art. 12, § 2, b, un État peut limiter ces droits, mais il « **ne doit pas restreindre** ces droits pour les travailleurs issus de pays tiers qui occupent un emploi ou qui ont occupé un emploi pendant une période minimale de six mois et qui sont inscrits comme chômeurs » [S]. La directive 2003/109/CE sur les résidents de longue durée va dans le même sens [À vérifier].

**La condition proposée** [C] : **la réunion des conditions actuelles et des exigences du droit de l'Union.** Le socle est ouvert, sous réserve de la résidence stable en France :
1. aux Français ;
2. aux ressortissants de l'Union, de l'EEE et de la Suisse qui disposent d'un **droit au séjour** (C-308/14), comme pour le RSA ;
3. aux ressortissants de pays tiers qui remplissent **l'une** des conditions suivantes :
   - (a) **la condition actuelle du RSA**, avec toutes ses exceptions (cinq ans de titre ; ou réfugié, protégé subsidiaire, apatride, carte de résident ; ou la situation de parent isolé) ;
   - (b) **ou** un titre autorisant à travailler, et au moins **six mois d'emploi**, avec une inscription : c'est l'exigence de la directive 2011/98.

**La réponse à la question posée** :
- La condition de séjour du socle est **moins restrictive** que celle du RSA. Elle reprend toutes les voies d'accès actuelles et en ajoute une (la voie b).
- **Personne d'aujourd'hui éligible n'est exclu**, ni au titre du RSA ni au titre de l'ASS : l'ASS n'exige pas de durée de titre de séjour [À vérifier], et ses bénéficiaires ont travaillé cinq ans dans les dix dernières années, ce qui leur ouvre la voie (b).
- **Le surcoût** vient des ressortissants de pays tiers arrivés depuis moins de cinq ans, qui ont travaillé au moins six mois et sont sans emploi. Il est à chiffrer en **M6** [À vérifier].
- **Le risque constitutionnel** : garder la condition de cinq ans pour les autres ressortissants de pays tiers, dans une prestation qualifiée de sécurité sociale, est moins sûr que pour le RSA. Le Conseil constitutionnel protège les droits sociaux des étrangers en séjour stable et régulier [À vérifier : décision n° 93-325 DC]. **Le repli** consiste à supprimer la condition de cinq ans pour tous les titulaires d'un titre autorisant à travailler. C'est plus simple et plus sûr, mais plus coûteux.

### D11. Territorialité, IA locale, aides d'État, AGCS et compteur (M4)

**Q31, le critère de rattachement** [C] : la taxe est due au titre de l'**utilisation effective en France** par une entité ou un établissement stable établi en France.
- Quand un service est acheté par une entité étrangère d'un groupe puis mis à la disposition d'une entité française (le contrat irlandais de la question), **l'entité française autoliquide** sur les volumes qu'elle utilise. Les refacturations internes au groupe servent de base. C'est une règle d'« utilisation effective », sur le modèle de celle que permet la directive TVA [À vérifier : art. 59 *bis*].
- L'abattement s'applique au niveau du **groupe** (M5).

**Q32, la conversion des unités** [C] : la loi fixe une **table de conversion** des unités facturées en octet-équivalent :
- par **token**, selon le type de contenu (par exemple, pour un texte, environ 4 octets par token [À vérifier]) ;
- par **image**, par **seconde de son ou de vidéo** ;
- pour un **forfait sans relevé**, un volume forfaitaire par compte et par mois, rattaché à la classe médiane (comme en D7).

Le fournisseur enregistré déclare le volume réel. Le client qui autoliquide peut retenir le volume réel, s'il est justifié, ou la table.

**Q33, les exportateurs qui utilisent de l'IA** : **pas de remboursement à l'export**. Ce serait une aide à l'exportation, contraire aux articles 107 et 108 du TFUE pour les échanges dans l'Union [À vérifier], et contraire à l'esprit de l'OMC. La réponse est le **double dividende** (la baisse des contributions patronales profite aussi aux exportateurs) et l'**abattement**. L'exposé doit **retirer** la phrase « les exportateurs ne sont pas pénalisés » et dire honnêtement ce qui pèse sur eux.

**Q34, les prestations produites à l'étranger avec de l'IA** : **un risque assumé**. Taxer le contenu en IA d'un service importé, d'après la façon dont il a été produit, serait une taxe sur l'importation de services difficile à justifier au regard de l'AGCS, et impossible à contrôler. L'étude d'impact mesure le risque de délocalisation des tâches, qui est atténué par le double dividende.

**Q36, l'AGCS et les conventions fiscales** : voir O7. Rien de nouveau : la taxe ne dépend pas de l'origine, et le taux réduit dépend du lieu d'exécution technique (un terminal), pas de l'origine du modèle. Le risque de représailles est politique, et il est documenté dans l'étude d'impact.

**Q37 et Q38, le SDK** [C] :
- il est développé en **logiciel libre** (sous la licence EUPL, À vérifier) par un projet piloté par la **DGFiP** et ouvert aux contributions ;
- le **référentiel de certification** est établi par un organisme de normalisation, sur le modèle de la norme NF525, et la certification est délivrée par un organisme accrédité ;
- l'utiliser est **volontaire** (décision 43) ;
- il transmet, avec la déclaration périodique, des **volumes agrégés** par classe, par type de contenu et par période, **signés et horodatés**. **Aucun contenu**, aucune donnée sur l'utilisateur individuel.

**Q45, la frontière entre terminal, serveur et nuage** [C] : un **équipement terminal** est un matériel placé sous la maîtrise physique de son utilisateur final et qui n'est pas exploité pour fournir un service d'inférence à des tiers par le réseau : un ordinateur, un téléphone, un appareil embarqué dans un produit ou une machine. **Un serveur en colocation, sur site ou dans le nuage, n'est pas un terminal** : il est au taux plein, « dans les mêmes conditions ».

**Q46, l'IA embarquée dans un produit professionnel** : le **redevable** est l'**utilisateur professionnel** qui exploite le produit, et non son fabricant. Pour les **flux continus** de capteurs (le traitement audio, un véhicule, une machine), la loi fixe un **volume forfaitaire annuel par catégorie d'appareil**, au lieu de mesurer des flux continus [C]. Le taux réduit s'applique pendant la période de lancement.

**Q47, « mêmes conditions » et taux réduit** : l'incohérence de l'exposé est levée. L'IA sur **serveur** de l'entreprise est taxée dans les mêmes conditions que l'IA en nuage. Seule l'IA sur **terminal** bénéficie du taux réduit. L'incitation à rapatrier les traitements est limitée aux terminaux, là où l'IA démarre, ce qui est le but recherché.

**Q48, la période de lancement et la maturité** [C, à valider] :
- **le taux réduit** : un tarif de **0,25 × m × P_k** pendant **trois ans** (les trois premières années civiles d'application) ;
- **une clause de rendez-vous** à trois ans, sur rapport ;
- **l'extinction** à la fin de la troisième année, ~~au plus tard au bout de cinq ans~~ → **sauf prolongation votée en LFSS, jusqu'à cinq ans au plus** (décision 103, M14, ↺ partiel de la décision 60) ;
- **le critère objectif de maturité** : la part de l'inférence sur terminal dans le volume total déclaré dépasse **20 %**, ou la part des entreprises qui l'utilisent dépasse **50 %** (une enquête de l'INSEE ou d'Eurostat). Les seuils sont à discuter.

C'est un écart assumé et temporaire au 50/50, découlant de « ménager ce qui démarre » (D2).

**Q70, la notification et les aides d'État** :
- l'obligation de comptage, qui pèse sur le redevable, n'est **pas une règle technique** ; le SDK est volontaire ;
- en revanche, le **taux réduit lié à un mode d'exécution technique** pourrait être une **règle technique de fait** liée à une mesure fiscale, au sens de la directive (UE) 2015/1535 [À vérifier]. **Je recommande de notifier** le projet par prudence, ce qui impose un statu quo d'au moins trois mois ;
- le taux réduit est **notifié** aussi au titre des aides d'État (décision 44), en le défendant par la logique du système (un critère objectif, temporaire, lié à l'objet) et, à titre subsidiaire, par l'art. 107, § 3, c, du TFUE ;
- le **règlement sur l'IA** : la taxe et le comptage ne fixent aucune exigence de mise sur le marché des systèmes d'IA. Le risque de conflit est faible [À vérifier].

**Q72, les PME sur les marchés tiers** : leurs coûts augmentent face à des concurrents qui ne sont pas taxés. Ce n'est pas un obstacle juridique, mais un **effet économique** à chiffrer dans l'étude d'impact, avec le double dividende et l'abattement en contrepartie (traité partiellement dans l'étude d'impact v0.1, § 5.2.3).


### D11 bis. Le tarif réduit sur terminal : une entrée en vigueur sans frein pour l'IA locale (M14, décision 103)

[opus-5.5, à valider ; la décision 103 [opus-5.5 as ggim] fixe la durée et la contrainte d'intention, le mécanisme ci-dessous est une proposition de l'agent]

**Le problème** (rapport de relecture, A1). Le dispositif v0.1 suspendait le seul article du tarif réduit (L.-15) « jusqu'à la décision de la Commission le déclarant compatible » (art. 16, II). Deux défauts : en attendant, l'IA sur terminal aurait payé le **plein tarif**, c'est-à-dire que la procédure aurait freiné ce que l'intention veut ménager ; et si la Commission conclut, comme le soutient l'étude d'impact, à l'**absence d'aide**, aucune décision « de compatibilité » n'interviendrait jamais, et L.-15 n'entrerait jamais en vigueur.

**Les voies écartées.**
- Mettre le tarif réduit en œuvre avant la décision : une aide d'État non notifiée ou mise en œuvre avant la décision viole la clause de suspension de l'art. 108, § 3, TFUE [S], et une aide illégale est **récupérable auprès de ses bénéficiaires** (règlement (UE) 2015/1589, art. 16) [Unverified : numéro exact], donc auprès de l'IA locale que l'on veut aider.
- Suspendre seulement L.-15 : c'est la rédaction de la v0.1, qui impose le plein tarif en attendant.
- Un régime *de minimis* ou une exemption par catégorie : plafonds par entreprise sur trois ans et champ ne couvrant pas une mesure fiscale générale ; aucune des deux voies n'est adaptée [Unverified].

**La solution retenue** (dispositif, art. 15 et 16).
1. **Notifier en amont**, dès la rédaction du projet (prénotification) et au stade du projet de loi : directive (UE) 2015/1535 (statu quo de trois mois) et art. 108, § 3, TFUE, pour L.-15 et pour l'abattement.
2. **Subordonner l'entrée en vigueur de tout le titre Ier**, et non du seul L.-15, à l'un de deux actes : (a) une décision de la Commission constatant l'absence d'aide, ou la compatibilité (règlement (UE) 2015/1589, art. 4, § 2 et 3) ; (b) l'**autorisation réputée acquise** faute de décision dans le délai d'examen préliminaire de deux mois, après un avis préalable du Gouvernement à la Commission, qui peut alors décider dans les quinze jours ouvrables (même règlement, art. 4, § 5 et 6) [S : texte vérifié sur legislation.gov.uk].
3. Ainsi, **le tarif réduit s'applique dès le premier jour d'application de la taxe** : l'IA sur terminal ne paie jamais le plein tarif du fait de la procédure. Le délai de trois ans court à compter de l'application effective, et non de la publication.
4. Si la Commission déclare L.-15 **incompatible**, le Gouvernement dépose dans les trois mois un projet de loi qui en tire les conséquences (art. 16, III) ; le tarif réduit n'a alors pas été appliqué, donc rien n'est à récupérer.

**Risque résiduel.**
- **Un retard de toute la recette** si la Commission ouvre la procédure formelle d'examen (art. 4, § 4) : elle dispose alors d'un délai indicatif de dix-huit mois [Unverified : art. 9, § 6]. Le calendrier de l'étude d'impact (entrée en vigueur au 1ᵉʳ janvier 2028) n'est tenu que si la Commission s'est prononcée en 2027. Une prénotification précoce et une notification qui coïncide avec le vote réduisent ce risque ; elles ne le suppriment pas.
- **Le coût du retard** est une recette différée, pas perdue : la phase 0 (trois ans) est décalée d'autant, et le socle s'ouvre plus tard (les droits ne précèdent jamais les recettes).
- **La qualification d'aide** reste incertaine (la thèse « logique du système » est défendue, non garantie) ; le juriste doit relire.
- **L'alternative** si ce retard est jugé inacceptable : entrer en vigueur sans tarif réduit sur terminal et remplacer l'aide par une mesure générale (un abattement de volume par appareil) ; elle serait une autre architecture, **non retenue** car elle ferait payer le plein tarif à l'IA locale qui démarre.

**Chiffrage.** Prolonger le tarif réduit de trois à cinq ans ne change ni la cible (2033) ni la baisse des cotisations (0,16 point en 2040) ; le socle d'ouverture est de 804 € au lieu de 839 € (`sim_v4.py`, `TERM_RED_END=2032`).


---

### D12. Assiette technique et contrôle (M5)

#### D12.1 Le champ : quels systèmes d'IA ? (Q20, Q80)

- **Le problème.** La définition du **système d'IA** du règlement (UE) 2024/1689 (art. 3, point 1) est très large. Elle couvrirait l'apprentissage automatique classique : le scoring, l'OCR, l'anti-spam, la réduction de bruit.
- **La proposition** [C] : le champ est l'**inférence d'un modèle d'IA à usage général**, au sens de l'art. 3, point 63, du règlement sur l'IA : « un modèle d'IA, y compris lorsqu'il est entraîné à l'aide d'une grande quantité de données au moyen de l'auto-supervision à grande échelle, qui fait preuve d'une généralité significative et est capable d'exécuter de manière compétente un large éventail de tâches distinctes » [S]. Le champ couvre aussi les modèles **dérivés** d'un tel modèle (affinés, distillés).
- **Pourquoi** :
  - ce critère est **objectif**, et il repose sur une définition du droit de l'Union déjà appliquée ;
  - il coïncide avec la **justification du savoir collectif** : ce sont les modèles entraînés sur une grande quantité de données ;
  - il exclut l'IA spécialisée, ce qui répond à la critique « qu'est-ce qu'un robot ? » (fichier 11).
- **Q80, les fonctions marginales intégrées à un logiciel** :
  - une autocomplétion, un résumé ou un assistant fondés sur un modèle à usage général sont **dans le champ**. L'**éditeur du logiciel** est le fournisseur qui collecte la taxe ; il achète l'inférence en suspension. Le volume est réel, ou forfaitaire par poste, avec l'option pour le réel (décision 61) ;
  - une **réduction de bruit** ou une **correction orthographique** fondées sur un modèle spécialisé sont **hors du champ**.
- **Le risque** : un éditeur qui requalifie un modèle général en modèle « spécialisé ». La parade : une **présomption** fondée sur la liste des modèles à usage général notifiés au Bureau de l'IA [À vérifier], et la clause anti-abus.

#### D12.2 L'unité de mesure et le format de référence (Q14, Q17)

L'**octet-équivalent** (décisions 9 et 30) est conservé. Le format de référence est précisé ainsi [C] :

| Type de contenu | Mesure de référence | Pourquoi |
|---|---|---|
| **Texte**, y compris le code et les données tabulaires sérialisées | **1 caractère Unicode = 1 octet-équivalent**, quel que soit l'encodage | La langue française n'est pas pénalisée : en UTF-8, un caractère accentué compte deux octets (Q14) |
| **Image** | Un nombre d'octets-équivalents par **mégapixel** de sortie, dans une résolution de référence | C'est indépendant de la compression (JPEG ou PNG) |
| **Son** | Par **seconde** | C'est indépendant de l'échantillonnage |
| **Vidéo** | Par **seconde**, selon une **classe de résolution** | C'est indépendant du codec |
| **Autres sorties** (vecteurs d'embeddings, structures moléculaires, modèles 3D, signaux) | Les **entrées** sont comptées ; les sorties non textuelles sont comptées sous leur forme textuelle sérialisée de référence, ou au forfait | Elles sont rattachées à une règle unique (Q17) |

- **Les coefficients** par type de contenu et par flux sont **fixés par la loi** (ils relèvent de l'assiette, au titre de l'article 34). Ils sont **révisés en LFSS**, sur l'avis d'une **commission indépendante** (l'INSEE, l'Arcom ou l'ARCEP, et des personnalités qualifiées [C]), qui les calibre sur les prix relatifs de chaque type (fichier 04).

#### D12.3 Lecture, cache, raisonnement, outils, agents (Q15, Q16, Q78)

- **Q15, la lecture et le cache** [C] : chaque lecture est **comptée** (c'est un calcul réel, et c'est facturé), avec un **coefficient par flux** calé sur les prix relatifs observés :
  - les données **générées** : un coefficient de **1** ;
  - les données **lues** : un coefficient de **0,25** environ [À vérifier : le rapport usuel entre le prix d'entrée et le prix de sortie] ;
  - les données lues **depuis le cache** : un coefficient de **0,025** environ.

  Le même contexte relu dix fois paie donc dix fois, mais au **tarif du cache**. C'est cohérent avec la valeur et avec la sobriété (décision 24, 2ᵉ enseignement).
- **Q16, le raisonnement interne** : il est compté comme des données **générées**. Les fournisseurs le facturent déjà comme une sortie, et le SDK le compte en local. **Les appels d'outils** : ce que le modèle lit et produit est compté selon les flux ci-dessus. Les outils eux-mêmes (une recherche, un calcul) ne sont pas de l'IA à usage général : ils sont hors du champ.
- **Q78, les agents en chaîne** :
  - chaque inférence d'un modèle à usage général est une **utilisation** : un agent qui appelle dix modèles consomme dix inférences. Ce n'est **pas une cascade**, mais une consommation réelle, comme dix machines qui consomment de l'électricité ;
  - quand un **intermédiaire** orchestre les agents pour un client, il achète en suspension (décision 37) et **collecte la taxe sur les volumes d'inférence consommés pour ce client** (une règle de transparence), et non sur sa propre facture. Sans cette règle, un résumé d'une page tiré de cent pages lues échapperait presque entièrement à la taxe ;
  - **les données synthétiques** destinées à entraîner un autre modèle : leur **génération** est une inférence, donc **taxée**. L'**entraînement** qui les utilise est hors du champ (décision 45).

#### D12.4 Les cas limites (Q19, Q79)

- **Q19, la compression des sorties** : la mesure porte sur la sortie **dans le format de référence**. Une sortie encodée ou compressée pour réduire le volume taxable (en base64, en abrégé codé, puis décodée hors du système) est **réintégrée** par une **clause anti-abus** spécifique, en plus de l'abus de droit (art. L. 64 du LPF) [À vérifier]. **Une sortie simplement plus concise n'est pas un abus** : c'est la sobriété recherchée.
- **Q79, les erreurs, les réessais et les tests** :
  - le volume taxable est le volume **facturé** par le fournisseur ou, en usage propre, le volume **effectivement traité**. Une requête en erreur non facturée n'est pas comptée ;
  - un **réessai** facturé est compté ;
  - les **tests et évaluations** sont un usage professionnel et sont **taxés**. L'abattement couvre les petits volumes.

#### D12.5 Contrôle, sanctions et moyens (Q39, Q41, Q42, Q43)

- **Q39, les indicateurs indirects.** La consommation électrique et les heures de GPU servent au **ciblage des contrôles**, jamais d'assiette. Pour distinguer l'inférence de l'entraînement, une entreprise qui entraîne des modèles tient un **registre d'entraînement** (le matériel, la durée, l'objet). Il est déclaré, mais non taxé. Une capacité de calcul importante, sans inférence déclarée ni entraînement enregistré, déclenche une demande d'information.
- **Q41, les sanctions et la procédure** [C, sur le modèle des taxes sur le chiffre d'affaires, À vérifier] :
  - **le défaut ou le retard de déclaration** : l'intérêt de retard (art. 1727 du CGI), et une majoration de 10 %, portée à 40 % après une mise en demeure et à 80 % en cas d'activité occulte (art. 1728) ;
  - **l'insuffisance** : 40 % en cas de manquement délibéré, 80 % en cas de manœuvres frauduleuses (art. 1729) ;
  - **le défaut de comptabilité-matière** : une **amende spécifique**, proportionnée au volume, avec un minimum forfaitaire ;
  - **le délai de reprise** : **trois ans**, comme pour les taxes sur le chiffre d'affaires, et dix ans en cas d'activité occulte ;
  - **la charge de la preuve** : le redevable doit justifier ses volumes par sa comptabilité-matière ou par le SDK, qui vaut présomption de bonne foi. À défaut, l'administration procède à une **évaluation d'office** à partir d'indices (les factures, les heures de GPU, la table de conversion).
- **Les moyens de l'administration.** L'architecture **concentre** le recouvrement. Les **fournisseurs enregistrés**, de quelques dizaines à quelques centaines, collectent la majeure partie de la recette. Les autoliquidants et les déclarants pour usage propre sont des milliers, pas des centaines de milliers. Les contrôles s'appuient sur le **rapprochement automatique** avec la facturation électronique. Le nombre d'emplois nécessaires est à chiffrer dans l'étude d'impact (M10).
- **Q42, le fractionnement** :
  - **l'abattement** s'apprécie au niveau du **groupe**, défini comme dans la taxe sur les services numériques, dont les seuils s'apprécient au niveau du groupe [À vérifier : art. 299 du CGI] ;
  - **le passage par des comptes de particuliers** est traité par la décision 53 ;
  - **le basculement vers un usage local non déclaré** : le terminal est compté et taxé à 0,25 (décision 60), et le serveur au taux plein. Une omission est une fraude, repérée par les factures de matériel (la facturation électronique) et la consommation électrique.
- **Q43, le coût de conformité d'une TPE** [C] :
  - une TPE qui n'utilise que des services de **fournisseurs enregistrés** n'a **aucune déclaration à faire**. Elle donne son SIREN, et le fournisseur collecte ;
  - **l'abattement** lui est restitué par un **remboursement automatique** : les fournisseurs déclarent les volumes par SIREN, et l'administration calcule et rembourse chaque année, sur un relevé prérempli ;
  - seule une TPE qui recourt à un fournisseur **non enregistré** fait une **déclaration annuelle simplifiée**, avec la table de conversion.

#### D12.6 La fraude à l'attestation de suspension (décision 37)

[C] :
- **Le statut de revendeur agréé.** Seul un redevable **inscrit sur un registre public** de revendeurs peut acheter en suspension. Le fournisseur vérifie le numéro en ligne, comme dans VIES.
- **La bonne foi du fournisseur.** S'il a vérifié un numéro valide, il n'est pas responsable.
- **La comptabilité-matière du revendeur** retrace les **entrées** (les volumes acquis en suspension) et les **sorties** (les volumes consommés pour ses clients, selon la règle de transparence de D12.3). **Un écart non justifié est taxé.**
- **Les sanctions** : une fausse attestation entraîne la taxe, les intérêts et une **majoration de 80 %** (pour manœuvres). Le revendeur radié perd le bénéfice de la suspension.
- **La solidarité** du client qui s'est fait passer pour un revendeur.

#### D12.7 Le contournement aux bornes des tranches (décision 48)

- **Le risque.** Un fournisseur fixe son prix catalogue juste sous une borne, pour que son modèle tombe dans la classe inférieure, dont le P_k est plus bas.
- **Les parades** [C] :
  1. **Le classement est fondé sur le plus élevé de deux prix** : le prix catalogue, et le **prix moyen réellement facturé** pour le modèle sur l'année précédente (constaté par l'INSEE à partir des déclarations).
  2. **Le classement porte sur la famille de modèles** : on ne peut pas scinder un modèle en variantes artificielles.
  3. **Un lissage aux bornes.** Dans une zone de **± 10 %** autour de chaque borne, le tarif est **interpolé linéairement** entre les deux classes. Le gain d'un prix « juste sous la borne » devient nul.

     Cette interpolation reste fondée sur un **prix catalogue de référence**, et non sur le prix de chaque transaction. Elle ne change pas l'analyse de l'article 401 (D1).
  4. **La clause anti-abus générale.**


---

### D13. Le champ révisé, puis le chômage universel (M6)

#### D13.1 La formulation légistique du champ (décision 64)

> **Validée en M7 (décision 69)**, avec l'ajout au 2° : « y compris la traduction et la transcription ».

**Les textes** [S, le texte exact est à vérifier au JOUE] :
- le règlement (UE) 2024/1689, **art. 3, point 63** : le modèle d'IA à usage général (cité en D12.1) ;
- son **art. 50, § 2**, qui vise les « fournisseurs de systèmes d'IA, y compris de systèmes d'IA à usage général, qui génèrent des contenus de synthèse de type audio, image, vidéo ou texte ». Le même paragraphe prévoit une **exception** pour les systèmes qui « remplissent une fonction d'assistance pour la mise en forme standard » ou qui « ne modifient pas de manière substantielle les données d'entrée […] ou leur sémantique ».

**La proposition de rédaction** [C] :

> **Article L. [À vérifier]-1.** – I. – Est soumise à la taxe sur l'intelligence artificielle l'utilisation en France, dans le cadre d'une activité économique ou d'une mission de service public, de l'inférence réalisée par :
>
> 1° Un modèle d'intelligence artificielle à usage général, au sens du 63) de l'article 3 du règlement (UE) 2024/1689 du Parlement européen et du Conseil du 13 juin 2024, y compris un modèle qui en est dérivé par affinage, distillation ou tout autre procédé ;
>
> 2° Un système d'intelligence artificielle, au sens du 1) du même article 3, qui génère des contenus de synthèse de type audio, image, vidéo ou texte, y compris du code informatique, au sens du paragraphe 2 de l'article 50 du même règlement.
>
> II. – Ne sont pas soumises à la taxe les utilisations d'un système mentionné au 2° du I lorsque ce système remplit une fonction d'assistance pour la mise en forme standard ou ne modifie pas de manière substantielle les données d'entrée ou leur sémantique.
>
> III. – L'entraînement et l'affinage des modèles ne constituent pas une utilisation au sens du I.

**Ce que cette rédaction couvre** :
- **l'illustrateur** : un générateur d'images, même spécialisé, entre au 2° ;
- la voix, la musique, la vidéo et le code générés ;
- tous les grands modèles de langage, au 1°.

**Ce qu'elle exclut** : le scoring, la recommandation, l'anti-spam (ils ne génèrent pas de contenu), et l'OCR, le débruitage et la correction orthographique (ils relèvent de l'exception du II).

**Un point à arbitrer : la traduction et la transcription automatiques** par un système spécialisé. Elles conservent la **sémantique** de l'entrée et pourraient donc relever de l'exception du II. Pourtant, elles remplacent un travail humain qualifié, celui des traducteurs et des sténotypistes.
- **Je recommande de les inclure expressément** par un ajout au 2° : « y compris la traduction et la transcription », par cohérence avec le principe du travail remplacé.
- Quand elles reposent sur un modèle à usage général, elles sont de toute façon couvertes par le 1°.

**Le lien avec la justification.** Le savoir collectif est l'argument central de l'exposé (décision 45). Le critère du 2° ne mentionne pas l'échelle des données d'entraînement, parce qu'un tel critère serait invérifiable. Il retient la **fonction générative**, qui est objective et vérifiable. Les générateurs sont, de fait, entraînés sur de grands corpus.

#### D13.2 Le socle : montant, foyer, cumuls (Q49)

> **M14** : ces points sont rédigés dans le dispositif (art. 4, V et VI) comme **propositions [opus-5.5], non validées** ; aucune décision du journal ne les arrête. L'indexation du socle sur le revenu médian, une fois la cible atteinte, est un droit prioritaire (décision 106).

- **Le montant** [C] : la cible est le **seuil de pauvreté à 60 % du revenu médian**, pour une personne seule, soit environ 1 200 € par mois (note 05) [À vérifier]. Le niveau est fixé chaque année en LFSS, sur une trajectoire (D13.6).
- **Le socle est individuel** : il est versé à chaque adulte sans emploi, conformément à l'intention (« dès 18 ans »). La **garantie familiale** (décision 58) protège les foyers que l'individualisation désavantagerait.
- **Les APL** : pour ne pas faire perdre les allocataires actuels du RSA, le socle n'est pris en compte dans les ressources qu'au-delà du montant du RSA du foyer [C ; À vérifier : la neutralisation actuelle des ressources des allocataires du RSA].
- **Les prestations familiales** ne sont **pas** déduites du socle.

#### D13.3 Qui est « sans emploi » ? (Q50)

> **M7** : la sortie progressive de 12 mois est validée (décision 72). **Les étudiants (décision 70) et les rentiers (décision 71) restent des questions OUVERTES, réservées à Guillaume** : la base de chiffrage exclut les étudiants et n'applique pas de réduction pour le patrimoine ; les deux variantes sont chiffrées dans la note 19 ; les livrables les présentent comme des choix ouverts.

[C, à valider] :

| Situation | Traitement proposé | Pourquoi |
|---|---|---|
| Une personne sans activité professionnelle, inscrite | **Éligible**, même si elle était inactive auparavant (une personne au foyer, par exemple) | C'est la logique de l'absence d'obligation de recherche. Le surcoût est voulu (note 05) |
| Un **étudiant en formation initiale** | **Non éligible** ; les bourses restent | L'inclure coûterait environ 40 Md€ (2,9 millions d'étudiants [À vérifier]) et changerait la nature du dispositif. **Point d'intention à confirmer** |
| Une personne en **formation rémunérée**, après sa formation initiale | **Éligible** (D13.5) | — |
| Une personne qui **reprend un emploi** | La **sortie progressive** pendant **12 mois**, puis la **prime d'activité**, qui est maintenue | Une sortie progressive ouverte à tous les bas salaires coûterait des dizaines de milliards. La limiter dans le temps est une différence de traitement justifiée par l'objet (inciter à la reprise) [À vérifier] |
| Un temps partiel ou un indépendant à faible revenu | La prime d'activité, comme aujourd'hui ; la sortie progressive après une période de socle | — |
| **Un « rentier »** (revenus du patrimoine élevés) | Le socle est **réduit** des revenus du patrimoine au-delà d'un seuil élevé (par exemple le socle lui-même) | Ce n'est pas une condition de ressources sur le travail. Cela évite le paradoxe d'un socle versé à de hauts revenus du capital. **Point d'intention à confirmer** |
| Un retraité | Non éligible ; la pension, puis l'ASPA | Le socle s'arrête à l'âge du taux plein |

#### D13.4 Le complément et l'Unédic (Q53, décision 57)

> **Assumé en M7 (décision 74)**, avec une mention explicite, dans l'exposé, du rôle maintenu des partenaires sociaux et de la concertation.

- **L'ARE devient le socle plus un complément.** Le complément vaut l'**écart positif** entre l'ARE calculée selon les règles actuelles et le socle, pendant la durée d'indemnisation actuelle [C].
- **L'Unédic garde** la gestion paritaire du complément, de ses paramètres (la convention d'assurance chômage) et de ses contributions, réduites par le double dividende.
- **La part « socle » de l'ARE** (décision 57) est versée par l'Unédic à la branche, sous la forme d'une **contribution de l'assurance chômage**, sur le modèle de la contribution de l'Unédic à France Travail [À vérifier]. **Ordre de grandeur** : la plupart des indemnisés perçoivent une ARE proche du socle, si bien que cette contribution représenterait **une grande partie des prestations actuelles de l'Unédic** (environ 37 Md€ par an, note 05 [À vérifier]). C'est déjà l'hypothèse du chiffrage de la note 05, qui retranche l'assurance chômage actuelle du coût brut. **Conséquence** : le rôle de l'Unédic se recentre sur le complément. Ce point est politiquement sensible pour les partenaires sociaux et doit être dit dans l'exposé.

#### D13.5 La formation rémunérée (Q55)

> **M14** : rédigée dans le dispositif (art. 4, VII) comme **proposition [opus-5.5], non validée** ; le principe d'une formation financée en phase 0 est décidé (décision 30 [G], 73).

[C] :
- La « rémunération » est le **socle**, maintenu pendant la formation, et le complément pour qui y a droit.
- **Les formations ouvrant droit** : les certifications enregistrées au RNCP et au répertoire spécifique, dispensées par des organismes certifiés Qualiopi [À vérifier].
- **Le financement des coûts pédagogiques** : un **abondement automatique du CPF** par la branche, et les financements existants (les régions, France Travail).
- **Le contrôle de la qualité** reste celui du droit commun.
- Pendant le rodage, les recettes financent la formation (décision 30 [G]). Le chiffrage est à faire en M7.

#### D13.6 La date d'ouverture des droits : les droits ne précèdent jamais les recettes (Q58)

> **Validée en M7 (décision 73).** La simulation v4 applique une règle d'ouverture **annuelle**, plus stricte que la règle ci-dessous (l'équilibre sur trois ans, fonds compris) ; l'écart ne compte que dans le scénario bas (note 19, § 2.5). **Décision 78** : c'est la règle sur trois ans qui est retenue pour le dispositif.

[C] :
- **Phase 0 (les trois premières années)** : la taxe est perçue, le fonds de réserve se constitue et la formation rémunérée est financée. La branche est créée. Le RSA et l'ASS sont **repris à l'identique** par la branche, avec la garantie de non-régression ; c'est à peu près neutre.
- **Phase 1** : l'**ouverture du socle aux 18-24 ans** sans droits (environ 0,5 million de personnes, note 05 [À vérifier]), et aux inactifs qui s'inscrivent.
- **Phase 2** : la **hausse progressive du montant**, du niveau du RSA vers la cible du seuil de pauvreté. Le niveau est voté chaque année en LFSS en fonction des recettes et du fonds. C'est **la variable d'ajustement de la montée en charge**, et non l'ouverture des droits.
- **La règle** : la LFSS fixe chaque année le niveau du socle, de sorte que la branche soit équilibrée sur trois ans, compte tenu du fonds de réserve.

#### D13.7 Le chiffrage à intégrer en M7

> **Intégré en M7** : la note 19 retient 7 Md€ à l'ouverture au niveau du RSA, 20 Md€ au socle cible et 1 Md€ de formation. Le tableau ci-dessous reste la source des ordres de grandeur.

Tous les montants sont [C, À vérifier].

| Poste | Ordre de grandeur | Source |
|---|---|---|
| Besoin net du chômage universel complet | 16 à 20 Md€ par an | Note 05 |
| Garantie familiale (D9) | environ 0,5 à 1 Md€ par an (les parents isolés avec deux enfants ou plus au RSA majoré, avec un écart moyen de quelques centaines d'euros par mois). **M14 : chiffrée dans le script (décision 108, revalorisée comme le RSA)** : 0,55 Md€ de 2026 au socle cible, 0,16 au socle de 925 €, rien de plus au niveau du RSA [Unverified : 410 000 foyers] ; revalorisée comme le socle, elle coûterait 4,3 Md€ à la cible | D9 |
| Voie (b) de la condition de séjour (D10) | environ 0,5 à 1,5 Md€ par an | D10 |
| Frontaliers privés d'emploi résidant en France (D6) | à chiffrer | D6 |
| Sortie progressive limitée à 12 mois | inclus dans les 3 à 5 Md€ de la note 05 | D13.3 |
| Formation rémunérée (les coûts pédagogiques) | à chiffrer | D13.5 |
| Réduction pour les revenus du patrimoine | une économie modeste | D13.3 |
| **Besoin net révisé** | **environ 18 à 23 Md€ par an** | à confirmer en M7 |


#### D13.8 La règle d'emploi et le scénario bas (M7)

[opus-5.5, sauf mention contraire]

- **La règle d'emploi des recettes** : les droits d'abord jusqu'au socle cible, puis le partage moitié-moitié (**décision 75 [opus-5.5 as ggim]**, D8). **Sa forme juridique** : la loi ordinaire qui crée la branche l'inscrit au code de la sécurité sociale comme une **règle de pilotage**, que la LFSS applique chaque année en fixant la fraction versée à l'Unédic (décision 49). Une LFSS ultérieure peut y déroger, puisqu'une loi ordinaire ne lie pas le législateur ; pour la rendre plus solide, la loi organique peut exiger que le rapport annexé au PLFSS justifie tout écart [Unverified : à confirmer avec la LO n° 2020-991]. **Ce n'est pas un obstacle juridique.**
- **Le scénario bas** : la taxe seule ne finance pas le but d'ici 2040 (note 19, § 2.5). **Pas de revirement** (orchestrateur, M7). Les livrables le disent honnêtement ; le recours est la **contribution d'équilibre** de l'État, votée en LFSS comme pour les autres branches (D8, point 4 du retournement) ; la **taxe Zucman** est citée comme une ressource complémentaire, **hors dispositif** (décision 32). La formulation proposée pour l'exposé et l'étude d'impact est dans la note 19, § 3, point 6.
- **Un effet à éviter** : avec une règle d'ouverture annuelle, le scénario bas perçoit la taxe pendant des années (le fonds atteint 15 à 43 Md€ en 2040) sans ouvrir le socle. La règle de D13.6 (l'équilibre sur trois ans, fonds compris), retenue par la **décision 78**, l'évite : avec l'indexation, le socle s'ouvre au niveau du RSA en 2035 (m ≤ 3 ou 4) ou en 2037 (m ≤ 2) (chiffres de M14).
- **m au-delà de 2 une fois la cible atteinte** : **décision 79** : m est ramené à 2 au plus, par défaut ; la LFSS peut aller au-delà par un vote motivé (justification renforcée, décision 51), notamment en cas de retournement.

---

## Historique du raisonnement

1. **2026-10-02, M1** : lecture du mandat, de l'intention, du corpus et du fichier 17. Vérification sur le web de l'article 401 et de ses critères (rapport du CPO de 2015, arrêts Vodafone et Tesco de 2020), des décisions 2025-1157 QPC, 2009-599 DC et 2012-662 DC, de l'article 2 de la LOLF modifié en 2021, de l'article 2 de la directive DAC, des arrêts Commission c/ Hongrie (2021) et ANGED (2018). **[C]**
2. Constat principal : **l'article 401, que le fichier 17 plaçait en tête des risques, n'est pas bloquant** si l'on évite la déduction en chaîne. Les vrais blocages sont **l'article 34** (le taux fixé par arrêté selon les « besoins »), **l'affectation** à un fonds sans base organique et **le compteur imposé aux éditeurs**. **[C]**
3. Tension identifiée avec une décision [G] : la décision 25 (« le montant par unité est égal au prix moyen ») et la décision 9 (le volume) produisent ensemble un **tarif unique** qui viole l'esprit du 50/50 pour les modèles peu chers. Le **tarif par classe** garde les deux décisions et rend le 50/50 vrai. **[C]**
4. **2026-10-02, M2** : l'orchestrateur valide par procuration les points 1, 2, 4 et 6 à 11 ; il accepte le point 3 sous condition (la démonstration au regard du 2ᵉ critère de l'article 401) et demande deux vérifications (m ≥ 1, la confiscation). Décisions 37 à 47 **[P]**. Recherches complémentaires : le rapport particulier de la Cour des comptes sur la TVA (2023) ; l'article LO 111-3-14 du code de la sécurité sociale ; la doctrine sur la confiscation (commentaire de la décision 2018-755 QPC, *Nouveaux Cahiers*). **Constat nouveau** : le cliquet de l'article LO 111-3-14 fait de la **voie « sécurité sociale »** la plus robuste pour protéger la recette (D4). **[C]**
5. **2026-10-02, M3** : décisions 48 à 52 **[P]**. L'orchestrateur demandait de vérifier le règlement 883/2004 avant d'arrêter la voie « sécurité sociale ». **Constat** : la classification d'une prestation au regard du règlement est fonctionnelle et indépendante de la voie d'affectation. Le socle serait en l'état une prestation de chômage, pour laquelle un droit au séjour peut être exigé (C-308/14), et l'annexe X est une étape ultérieure. La voie est donc arrêtée. L'orchestrateur a aussi contesté la règle d'identification de M2 : la nouvelle règle est en D7. **[C]**
6. **2026-10-02, M4** : décisions 53 à 57 **[P]**. Deux exigences nouvelles de l'orchestrateur : la non-régression (D9) et ne rien exclure de ce qui est éligible aujourd'hui (D10). **Constat** : la directive 2011/98 interdit de restreindre le socle aux ressortissants de pays tiers qui ont travaillé six mois et sont inscrits. La condition de séjour du socle est donc nécessairement **plus ouverte** que celle du RSA. **[C]**
7. **2026-10-02, M5** : décisions 58 à 63 **[P]**. Rédaction de D12 (l'assiette technique et le contrôle). **Choix structurant** : le champ est limité aux **modèles d'IA à usage général**, au sens de l'art. 3, point 63, du règlement sur l'IA. Cela relie le champ à la justification du savoir collectif, et règle les questions 20 et 80. **[C]**
8. **2026-10-02, M6** : décisions 64 à 68 **[P]**. L'orchestrateur a contesté le champ (un générateur spécialisé d'images échapperait à la taxe, alors que l'illustrateur est l'exemple fondateur) : le champ est élargi aux systèmes de l'art. 50, § 2 (D13.1). Rédaction de D13 (le chômage universel) et de la section F (le guide de reprise). **[C]**
9. **2026-10-04, fin de M7** : un agent neuf (opus-5.5) reprend après l'interruption de l'agent de relève, qui avait inscrit les décisions 69 à 74 et écrit la note 19. Vérification de la note 19 contre la sortie du script (trois écarts mineurs, corrigés) ; **décision 75** [opus-5.5 as ggim], les droits d'abord, ↺ de la décision 30 [G] ; décision 76 [ggim], les conventions de la branche ; rédaction de D13.8 (la règle d'emploi, le scénario bas) ; revue des 80 questions du fichier 17 et de la section E. **Constat** : aucun obstacle juridique bloquant nouveau ; le scénario bas est une limite budgétaire, assumée. **[opus-5.5]**
10. **2026-10-04, M11** : un agent neuf (opus-5.5) reprend d'après la section F. Décisions 88 à 93 ; modélisation de la décision 89 et contrôle de non-régression ; rédaction de l'étude d'impact v0.1 et de son script ; Q8, Q71, Q73 et Q74 répondues. **Constat** : aucun obstacle juridique nouveau ; la sortie progressive au plafond de 50 % est moins favorable que la prime d'activité tant que le socle est proche du RSA. **[opus-5.5]**
11. **2026-10-04, M12** : décisions 94 à 97 ; la sortie progressive de M11, contestée (une régression au niveau du RSA), est corrigée dans la loi (plancher au droit actuel, dégressivité linéaire) ; modélisation et non-régression ; l'étude d'impact est mise à jour. **Constat** : la modalité de la dégressivité pèse plus sur la trajectoire que le plancher lui-même ; la relecture de cohérence reste à faire par un agent neuf. **[opus-5.5]**
12. **2026-10-04, M13-M14** : la relecture de cohérence (agent neuf, lecture seule) relève 17 contradictions de fond, 9 erreurs de tenue et 7 points de décision (note 20). L'orchestrateur arbitre les points C par procuration (C1 à C7) ; un agent de relève applique les corrections. **Constats** [opus-5.5] : le modèle comptait la sortie progressive sur deux bases (A4) et omettait la garantie familiale (A5) : raccord du modèle, trajectoire révisée (cible 2033 avec m ≤ 3, 2037 avec m ≤ 2, 0,16 point en 2040) ; le tarif réduit sur terminal ne pouvait pas être suspendu sans faire payer le plein tarif à l'IA locale : l'entrée en vigueur de toute la taxe est subordonnée à la décision de la Commission (D11 bis).

## Questions ouvertes

- **Après M15 (10-04)** [ggim] : étudier l'effet de la mesure par la consommation (TVA, achats) **par tranche d'âge**, avec le cas des jeunes adultes en formation initiale chez leurs parents (décision 110). Aucune décision d'inclure les étudiants ; la question 50 reste réservée à lui. À traiter dans l'étude d'impact, avec les effets sur les foyers des parents et le multiplicateur.
- **Après M14** [opus-5.5] : (1) le mécanisme de D11 bis (entrée en vigueur subordonnée à la décision de la Commission) : le valider, ou accepter un tarif réduit sans notification préalable au risque d'une récupération ; (2) la dégressivité dans les douze mois et la trajectoire m ≤ 3, **hésitations** à porter au rapport de retour (104, 107) ; (3) les paramètres [Unverified] de la sortie progressive et de la garantie familiale (100, 108), à faire confirmer par l'économiste ; (4) les propositions du dispositif non arrêtées (D13.2, D13.5, bornes des classes, seuil de volume).
- **Après M9** [opus-5.5] : le taux d'indexation (2 %) [Unverified], à confirmer par l'économiste (85). **Réservées à Guillaume** : les étudiants (70) et le patrimoine (71).
- **Les points à faire relire par un expert** (tirés de l'ancienne section F) :
  - la confiscation et les impositions comportementales (D3) ;
  - la coordination européenne et les frontaliers (D6) ;
  - le RGPD (D7) ;
  - les reprises de ressources des départements (D6) ;
  - l'apport exact de la LO n° 2020-991 ;
  - les montants du RSA et du seuil de pauvreté ;
  - le texte exact des articles 3 et 50 du règlement sur l'IA au JOUE ;
  - la force juridique de la règle d'emploi des recettes (loi ordinaire, LFSS, loi organique), D13.8 [opus-5.5] ;
  - le mécanisme d'entrée en vigueur subordonnée à la décision de la Commission, l'autorisation réputée acquise et le risque de procédure formelle (D11 bis) [opus-5.5] ;
  - les paramètres [Unverified] de la sortie progressive (600 000 reprises d'emploi par an, droit actuel simplifié, six mois de dégressivité, décision 100) et les effectifs de la garantie familiale (410 000 foyers, décision 108) ;
  - les montants des amendes (décision 90) et leur proportionnalité, ainsi que le périmètre des personnes qui y sont exposées (décision 105).

## Sources

- Directive 2006/112/CE, art. 401 : https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=celex%3A32006L0112
- Conseil des prélèvements obligatoires, « Le cadre juridique de la TVA », 2015, p. 33-34 : https://www.ccomptes.fr/sites/default/files/EzPublish/20151216-rapport-Pourreau-cadre-juridique-TVA.pdf
- CJUE, 3 mars 2020, Vodafone Magyarország, C-75/18 (communiqué) : https://curia.europa.eu/jcms/upload/docs/application/pdf/2020-03/cp200020en.pdf
- Cons. const., n° 2025-1157 QPC du 12 septembre 2025 (taxe sur les services numériques) : https://www.conseil-constitutionnel.fr/decision/2025/20251157QPC.htm
- Cons. const., n° 2009-599 DC du 29 décembre 2009 (contribution carbone) : https://www.concurrences.com/fr/review/issues/no-2-2010/chroniques/secteur-public/annulation-de-la-contribution-climat-energie-le-conseil-constitutionnel-pose
- Cons. const., n° 2012-662 DC (le seuil des deux tiers) : https://cms.law/fr/fra/a-la-une/l-impot-confiscatoire-au-sens-de-la-decision-du-conseil-constitutionnel-n-2012-662-dc-du-29-decembre-2012
- LO n° 2021-1836, art. 3 (modifiant l'art. 2 de la LOLF) : https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000044589833
- Directive 2011/16/UE, art. 2 : https://www.legislation.gov.uk/eudr/2011/16/article/2/data.htm?view=plain
- CJUE, 16 mars 2021, Commission c/ Hongrie, C-596/19 P : https://kpmg.com/xx/en/our-insights/eu-tax/etf-445-cjeu-decisions-on-state-aid.html
- CJUE, 26 avril 2018, ANGED, C-233/16 : https://www.concurrences.com/en/bulletin/news-issues/april-2018/the-eu-court-of-justice-clarifies-application-of-selectivity-criterion-to-state
- Cour des comptes, rapport particulier sur la TVA, février 2023, p. 1-2 (les caractéristiques de la TVA, la souplesse de la Cour, plus de trente taxes spéciales sur le chiffre d'affaires) : https://www.ccomptes.fr/system/files/2023-02/20230209-TVA-rapport-particulier-1_0.pdf
- Code de la sécurité sociale, art. LO 111-3-14 et LO 111-3-16 : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045354454
- Commentaire de la décision 2018-755 QPC (la confiscation, la décision 2005-530 DC) : https://qpc360.conseil-constitutionnel.fr/commentaire-decision-2018-755-qpc
- *Nouveaux Cahiers du Conseil constitutionnel*, « Le Conseil constitutionnel mobilise-t-il d'autres principes constitutionnels que l'égalité en matière fiscale ? » : https://www.conseil-constitutionnel.fr/nouveaux-cahiers-du-conseil-constitutionnel/le-conseil-constitutionnel-mobilise-t-il-d-autres-principes-constitutionnels-que-l-egalite-en
- CJUE, 14 juin 2016, Commission c/ Royaume-Uni, C-308/14 : https://curia.europa.eu/jcms/upload/docs/application/pdf/2015-10/cp150114en.pdf et https://asil.org/print/blogs/court-justice-european-union-holds-uk-can-require-child-benefit-and-tax-credit-recipients-have
- Cleiss, les prestations spéciales à caractère non contributif (art. 70 et annexe X du règlement 883/2004) : https://www.cleiss.fr/reglements/883_prestations_acnc.html
- CE, 16 avril 2019, n° 423586 (l'ASPA à l'annexe X) : https://www.conseil-etat.fr/fr/arianeweb/CE/analyse/2019-04-16/423586
- Alimanovic, C-67/14, et Dano, C-333/13 : https://www.cleiss.fr/docs/jurisprudence/c67-14.html
- La recentralisation du RSA (art. 43 de la LFI pour 2022, décret n° 2022-322) : https://blog.landot-avocats.net/2022/04/11/recentralisation-du-rsa-mode-demploi/ et https://www.banquedesterritoires.fr/un-decret-organise-lexperimentation-de-la-recentralisation-du-rsa
- La 5ᵉ branche (LO n° 2020-991, loi n° 2020-992, ordonnance n° 2021-1554) : https://blog.landot-avocats.net/2022/05/13/entree-en-vigueur-de-la-5e-branche-autonomie-de-la-secu/ et https://www.banquedesterritoires.fr/le-cinquieme-risque-officiellement-cree-la-dette-sociale-cantonnee
- Directive 2011/98/UE, art. 12 : https://www.legislation.gov.uk/eudr/2011/98/article/12
- Le RSA et la condition de cinq ans (art. L. 262-4 du CASF ; RSA majoré ; CE, 10 juillet 2015, n° 375887) : https://questions.assemblee-nationale.fr/dyn/14/questions/QANR5L14QE59693.pdf et https://blog.landot-avocats.net/2017/12/04/rsa-la-condition-de-5-ans-de-residence-en-france-imposee-aux-etrangers-non-communautaire-nest-pas-contraire-a-la-cedh-selon-le-ta-de-paris/
- Règlement (UE) 2024/1689, art. 3, points 1 et 63 : https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/fra et https://www.regulation-ai.eu/fr/articles/article-3/
- CIBS, ordonnance n° 2021-1843 : https://www.douane.gouv.fr/fiche/code-des-impositions-sur-les-biens-et-services-contributions-indirectes

## Liens

- [mandat.md](mandat.md)
- [17-objection-questions-lecteur-critique.md](17-objection-questions-lecteur-critique.md)
- [04-hypothese-modalites-assiette-et-collecte.md](04-hypothese-modalites-assiette-et-collecte.md)
- [10-hypothese-taux-variable-indexe.md](10-hypothese-taux-variable-indexe.md)
- [08-hypothese-sdk-comptage-infalsifiable.md](08-hypothese-sdk-comptage-infalsifiable.md)
- [05-hypothese-revenu-universel-musk.md](05-hypothese-revenu-universel-musk.md)
- [11-cadrage-impact-economique.md](11-cadrage-impact-economique.md)
