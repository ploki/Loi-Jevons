# Faisabilité juridique : obstacles, solutions et architecture révisée

- **Statut** : brouillon (ébauche du tour M1 de la session metamaieutique)
- **Créé le** : 2026-10-02
- **Dernière mise à jour** : 2026-10-02

> Note de la session metamaieutique « Rendre la Loi Jevons réalisable » (voir `mandat.md`). Tout ce qui suit est **[C]** tant que l'orchestrateur ne l'a pas validé. Les décisions par procuration seront marquées **[P]**. Les textes vérifiés sur le web sont marqués **[S]** ; le reste est **[À vérifier]**.

## En vigueur

**Aucune décision n'est encore prise.** Cette ébauche :

1. recense **dix obstacles juridiques** de l'architecture v0.1 (O1 à O10), dont trois sont bloquants en l'état (**O3**, l'article 34 ; **O4**, l'affectation ; **O9**, l'obligation de compteur) ;
2. conclut que **l'article 401 de la directive TVA (O1) n'est pas bloquant**, à condition de **ne pas** introduire de mécanisme de déduction en chaîne et de garder une taxe **spéciale** (le seul secteur de l'IA) et **à un seul stade** ;
3. propose une **architecture révisée** (section A), qui garde l'intention (taxer l'IA, au moins la moitié de la valeur, épargner les particuliers, ménager ce qui démarre) ;
4. propose un **plan de travail** (section C).

| Obstacle | Bloquant en l'état ? | Piste recommandée [C] | Risque résiduel |
|---|---|---|---|
| O1. Art. 401 de la directive TVA | Non, sous conditions | Taxe spéciale, à un stade unique, sans déduction ; la revente est en suspension | Faible |
| O2. Égalité, capacité contributive, confiscation | Risque sérieux sur deux points | Un tarif par classe de modèles ; des critères de champ objectifs ; un plafond justifié | Moyen |
| O3. Article 34 (taux par arrêté selon les « besoins ») | **Oui** | La formule d'indexation dans la loi ; le multiple m voté chaque année en loi de finances, entre 1 et 4 | Faible |
| O4. Affectation (LOLF, LFSS, Unédic) | **Oui** (le « fonds » n'a pas de base) | Affectation par **loi de finances** à un établissement public, ou un CAS ; une fraction à l'Unédic | Faible |
| O5. Territorialité, fournisseurs étrangers, cascade | Difficulté pratique | Le fournisseur enregistré collecte ; sinon le client autoliquide ; la revente est en suspension ; directive DAC | Moyen |
| O6. Aides d'État (IA locale, abattement) | Risque sérieux | Un champ défini objectivement ; une notification préventive ; l'abattement est une mesure générale | Moyen |
| O7. OMC, AGCS, conventions fiscales | Non | Une taxe neutre quant à l'origine | Faible en droit ; risque de représailles politique |
| O8. Départements (RSA), article 72-2 | Non, mais à organiser | Recentralisation du RSA avec compensation | Faible |
| O9. Compteur obligatoire (directive 2015/1535, AI Act, RGPD) | **Oui** dans la rédaction actuelle | Obligation pesant sur le **redevable** (tenir une comptabilité-matière), le SDK n'étant qu'une **voie simplifiée** ; notification | Faible à moyen |
| O10. Chômage universel et droit de l'UE (résidence, coordination) | Non | Le socle est une prestation de solidarité non contributive, sous condition de résidence | Faible |

---

## A. Architecture révisée proposée [C]

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
- **Le multiple m est voté chaque année en loi de finances**, entre **1** (le plancher : la moitié de la valeur) et **4** (le plafond), au vu d'un rapport sur le besoin de financement. Le « moteur » B/A devient ainsi une **décision du Parlement** et non un arrêté (règle O3).
- [C] Variante à discuter : une assiette **ad valorem** (100 % à 400 % du prix hors taxe), plus simple à contrôler. Elle reste compatible avec l'article 401 (voir O1), mais elle s'éloigne de la décision 9 sur le volume. **Je ne la recommande pas** comme régime principal, mais comme **régime de secours** pour les offres au forfait (Q23).

### A4. Champ
- **Le champ est l'usage professionnel.** Les particuliers ne sont pas « exonérés » : ils sont **hors du champ**, parce que le fait générateur est l'utilisation par une personne qui agit dans le cadre d'une activité économique ou d'une mission de service public. Le critère est objectif (O2).
- **L'entraînement et l'affinage** : à trancher (Q40). Ma recommandation provisoire est de les mettre **hors champ**, au motif que l'objet de la taxe est l'**usage productif** qui substitue au travail, et parce que les taxer pénaliserait la recherche et les modèles français.
- **Le secteur public, les associations et la recherche** : à trancher (Q22). Je recommande provisoirement de les inclure, avec l'abattement, pour la cohérence du critère.

### A5. Affectation
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

## C. Plan de travail proposé [C]

Une vingtaine d'itérations (la limite du mandat est de 30). Chaque itération se termine par la mise à jour de cette note, du journal et de la liste de suivi (fichier 17).

| Itération | Objet | Questions du fichier 17 | Production |
|---|---|---|---|
| M1 | État des lieux juridique, ébauche de cette note | 69, 67, 68, 60, 70, 36 | Note 18 (ébauche) |
| M2 | **Arbitrages structurants** : nature juridique, redevable, tarif par classe, vote de m en loi de finances, affectation | 69, 27, 60, 26, 35 | Journal [P] ; notes 04 et 10 |
| M3 | Article 34 et égalité : la formule légale, les coefficients dans la loi, la justification du plafond | 67, 68, 27, 28, 29, 25, 30 | Notes 10 et 18 |
| M4 | Affectation : l'établissement public, l'Unédic, le fonds de réserve, la loi de finances, le plafonnement des taxes affectées | 60, 61, 62, 64, 65 | Notes 11 et 18 |
| M5 | Territorialité : les fournisseurs étrangers, la conversion des unités, la suspension, la DAC, l'export | 31 à 35, 72 | Notes 04 et 18 |
| M6 | IA locale et aides d'État ; AGCS ; le compteur (2015/1535, AI Act, RGPD) | 37, 38, 45 à 48, 70, 36 | Notes 08 et 18 |
| M7 | Assiette technique : le contexte et le cache, le raisonnement, l'entraînement, les cas limites, le secteur public, la définition du système d'IA | 14 à 22, 40, 78 à 80 | Notes 04 et 18 |
| M8 | Contrôle : les sanctions, les moyens, le fractionnement, le coût de conformité | 39, 41 à 44 | Notes 08 et 18 |
| M9 | Chômage universel : le foyer, l'éligibilité, la résidence, l'Unédic, la formation, les départements, la date d'ouverture des droits | 49 à 51, 53, 55, 57, 58 | Notes 05 et 18 |
| M10 | Simulation v4 : le tarif par classe, le vote de m, le lissage, l'entrée en vigueur en 2028, la formation chiffrée | 13, 59, 62, 63, 74 | `outils/sim_v4.py`, note 19 |
| M11 | Revue des 80 questions et des contradictions du fichier 17 ; note 18 « stabilisée » | toutes | Notes 17 et 18 |
| M12 | **Exposé des motifs v0.2** | contradictions | Livrable |
| M13 | **Dispositif v0.1**, titres I (la taxe) et II (le chômage universel) | — | Livrable |
| M14 | **Dispositif v0.1**, titres III (l'affectation) et IV (l'entrée en vigueur), et l'article de loi de finances | — | Livrable |
| M15 | **Étude d'impact v0.1** | 8, 71 à 75 | Livrable |
| M16 | Relecture de cohérence entre le corpus et les livrables | — | Corrections |
| M17 | **Confrontation à l'aveugle**, centrée sur la légalité : les questions | — | Note 20 |
| M18 | Classement R/P/N, liste de suivi | — | Notes 17 et 20 |
| M19 | Corrections après la confrontation | — | Livrables |
| M20 | **Rapport de retour** | — | `rapport-de-retour.md` |

Les itérations 21 à 30 restent en réserve pour les arbitrages imprévus.

---

## Historique du raisonnement

1. **2026-10-02, M1** : lecture du mandat, de l'intention, du corpus et du fichier 17. Vérification sur le web de l'article 401 et de ses critères (rapport du CPO de 2015, arrêts Vodafone et Tesco de 2020), des décisions 2025-1157 QPC, 2009-599 DC et 2012-662 DC, de l'article 2 de la LOLF modifié en 2021, de l'article 2 de la directive DAC, des arrêts Commission c/ Hongrie (2021) et ANGED (2018). **[C]**
2. Constat principal : **l'article 401, que le fichier 17 plaçait en tête des risques, n'est pas bloquant** si l'on évite la déduction en chaîne. Les vrais blocages sont **l'article 34** (le taux fixé par arrêté selon les « besoins »), **l'affectation** à un fonds sans base organique et **le compteur imposé aux éditeurs**. **[C]**
3. Tension identifiée avec une décision [G] : la décision 25 (« le montant par unité est égal au prix moyen ») et la décision 9 (le volume) produisent ensemble un **tarif unique** qui viole l'esprit du 50/50 pour les modèles peu chers. Le **tarif par classe** garde les deux décisions et rend le 50/50 vrai. **[C]**

## Questions ouvertes

- Voir la rubrique « Questions et propositions » du tour M1 : les arbitrages de M2.

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
- CIBS, ordonnance n° 2021-1843 : https://www.douane.gouv.fr/fiche/code-des-impositions-sur-les-biens-et-services-contributions-indirectes

## Liens

- [mandat.md](mandat.md)
- [17-objection-questions-lecteur-critique.md](17-objection-questions-lecteur-critique.md)
- [04-hypothese-modalites-assiette-et-collecte.md](04-hypothese-modalites-assiette-et-collecte.md)
- [10-hypothese-taux-variable-indexe.md](10-hypothese-taux-variable-indexe.md)
- [08-hypothese-sdk-comptage-infalsifiable.md](08-hypothese-sdk-comptage-infalsifiable.md)
- [05-hypothese-revenu-universel-musk.md](05-hypothese-revenu-universel-musk.md)
- [11-cadrage-impact-economique.md](11-cadrage-impact-economique.md)
