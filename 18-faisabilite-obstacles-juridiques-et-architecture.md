# Faisabilité juridique : obstacles, solutions et architecture révisée

- **Statut** : en discussion (M2 de la session metamaieutique)
- **Créé le** : 2026-10-02
- **Dernière mise à jour** : 2026-10-02 (M2)

> Note de la session metamaieutique « Rendre la Loi Jevons réalisable » (voir `mandat.md`). Les décisions par procuration sont marquées **[P]** et numérotées comme au journal ; les propositions non validées restent **[C]**. Les textes vérifiés sur le web sont marqués **[S]** ; le reste est **[À vérifier]**.

## En vigueur

**Décisions prises en M2** (journal, n° 37 à 47) :
- **37 [P]** : pas de déduction en chaîne ; la revente est en suspension, sur attestation.
- **38 [P]** : le fournisseur enregistré collecte la taxe ; à défaut, le client autoliquide ; l'usage propre est déclaré. Le client professionnel est identifié par son SIREN ou son numéro de TVA intracommunautaire.
- **39 [P, sous condition]** : un tarif par classe de modèles, m × P_k, avec trois classes. La condition (l'article 401) est traitée en **D1** : à confirmer.
- **40 [P] ↺** : m est voté chaque année par le Parlement, entre 1 et 4 ; l'arrêté ne fait que constater l'indice.
- **41 [P]** : le plafond 4P est une borne légale ; l'analyse du caractère non confiscatoire est en **D3**.
- **42 [P]** : la recette ne passe jamais par le budget général. La voie d'affectation est comparée en **D4**, où je recommande la **voie « sécurité sociale »** [C].
- **43 [P] ↺** : l'obligation de comptage pèse sur le redevable ; le SDK est une voie simplifiée.
- **44 [P]** : le taux réduit vise l'exécution sur un équipement terminal ; il est temporaire et notifié.
- **45 [P]** : l'entraînement est hors du champ ; c'est une piste ultérieure.
- **46 [P]** : le secteur public, les associations et la recherche sont dans le champ, avec l'abattement (effet circulaire en **D5**).
- **47 [P]** : le plan est validé ; les 20 questions sont suivies une par une en **section E** ; le plan est resserré (**section C**).

**État des obstacles** : l'article 401 n'est pas bloquant (O1, D1). Les blocages de l'article 34 (O3) et du compteur (O9) sont levés par les décisions 40 et 43. Le blocage de l'affectation (O4) le sera par le choix de la voie en M3.

| Obstacle | Bloquant en l'état ? | Piste recommandée [C] | Risque résiduel |
|---|---|---|---|
| O1. Art. 401 de la directive TVA | Non, sous conditions | Taxe spéciale, à un stade unique, sans déduction ; la revente est en suspension | Faible |
| O2. Égalité, capacité contributive, confiscation | Risque sérieux sur deux points | Un tarif par classe de modèles ; des critères de champ objectifs ; un plafond justifié | Moyen |
| O3. Article 34 (taux par arrêté selon les « besoins ») | **Levé** (décision 40) | La formule d'indexation dans la loi ; le multiple m voté chaque année par le Parlement, entre 1 et 4 | Faible |
| O4. Affectation (LOLF, LFSS, Unédic) | **Oui**, en cours (décision 42) | Recommandé : une **branche de sécurité sociale** financée par la taxe, affectée en LFSS (D4) ; une fraction à l'Unédic | Faible |
| O5. Territorialité, fournisseurs étrangers, cascade | Difficulté pratique | Le fournisseur enregistré collecte ; sinon le client autoliquide ; la revente est en suspension ; directive DAC | Moyen |
| O6. Aides d'État (IA locale, abattement) | Risque sérieux | Un champ défini objectivement ; une notification préventive ; l'abattement est une mesure générale | Moyen |
| O7. OMC, AGCS, conventions fiscales | Non | Une taxe neutre quant à l'origine | Faible en droit ; risque de représailles politique |
| O8. Départements (RSA), article 72-2 | Non, mais à organiser | Recentralisation du RSA avec compensation | Faible |
| O9. Compteur obligatoire (directive 2015/1535, AI Act, RGPD) | **Levé** (décision 43) | Obligation pesant sur le **redevable** (tenir une comptabilité-matière), le SDK n'étant qu'une **voie simplifiée** ; notification | Faible à moyen |
| O10. Chômage universel et droit de l'UE (résidence, coordination) | Non | Le socle est une prestation de solidarité non contributive, sous condition de résidence | Faible |

---

## A. Architecture révisée proposée [C]

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

## C. Plan de travail (validé, décision 47 [P], resserré en M2)

Le plan initial comptait 20 itérations. Il est resserré à **14**, en regroupant les itérations voisines. Les itérations 15 à 30 restent en réserve.

| Itération | Objet | Questions du fichier 17 | Production |
|---|---|---|---|
| M1 ✔ | État des lieux juridique | 69, 67, 68, 60, 70, 36 | Note 18 (ébauche) |
| M2 ✔ | Arbitrages structurants ; l'article 401 et le 2ᵉ critère ; m ≥ 1 ; la confiscation ; la comparaison des voies d'affectation | 69, 26, 27, 35, 22, 40 | Journal 37-47 ; notes 04, 08, 10, 18 |
| M3 | **Affectation et Constitution** : le choix de la voie (D4), le fonds de réserve, l'Unédic, les départements, les coefficients dans la loi, la justification du plafond, le lissage | 60, 61, 62, 64, 65, 67, 68, 28, 29, 57 | Notes 05, 11, 18 |
| M4 | **Territorialité, IA locale, aides d'État, AGCS, compteur** : les fournisseurs étrangers, la conversion des unités, la DAC, la notification | 31 à 34, 36, 37, 38, 45 à 48, 70, 72 | Notes 04, 08, 18 |
| M5 | **Assiette technique et contrôle** : le contexte et le cache, le raisonnement, les cas limites, la définition du système d'IA, les sanctions, le fractionnement, la fraude à l'attestation | 14 à 21, 15, 39, 41 à 44, 78 à 80 | Notes 04, 08, 18 |
| M6 | **Chômage universel** : le foyer, l'éligibilité, la résidence, l'Unédic, la formation, la date d'ouverture des droits | 49 à 51, 53, 55, 58 | Notes 05, 18 |
| M7 | **Simulation v4** (tarif par classe, vote de m, lissage, entrée en vigueur réaliste, formation chiffrée) et **revue des 80 questions** | 13, 59, 62, 63, 74 ; toutes | `outils/sim_v4.py`, notes 17, 18, 19 |
| M8 | **Exposé des motifs v0.2** | 1, 75, contradictions | Livrable |
| M9 | **Dispositif v0.1** (titres I à IV, et l'article de loi de financement ou de finances) | — | Livrable |
| M10 | **Étude d'impact v0.1** | 8, 71, 73, 75 | Livrable |
| M11 | Relecture de cohérence entre le corpus et les livrables | — | Corrections |
| M12 | **Confrontation à l'aveugle** centrée sur la légalité : les questions, puis le classement R/P/N | — | Note 20, note 17 |
| M13 | Corrections après la confrontation | — | Livrables |
| M14 | **Rapport de retour** | — | `rapport-de-retour.md` |

---

## D. Réponses de M2 aux contestations et vérifications

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

**Proposition** : lever la condition de la décision 39.

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

À arrêter en M3.

### D5. Le secteur public : l'effet budgétaire circulaire (point 10)

- **L'État** paie la taxe sur son propre usage de l'IA professionnelle. Avec la voie D4, cette taxe est un **transfert de l'État vers la sécurité sociale**. Il est **neutre pour le solde des administrations publiques** prises ensemble (au sens de Maastricht), et **positif pour le chômage universel**. Il a un coût de gestion, et il rend visible le coût réel de l'IA dans l'administration.
- **Les collectivités, les hôpitaux et les universités** supportent une **charge réelle**. L'article 72-2 n'impose pas de compensation, puisque la taxe n'est ni un transfert ni une création de compétences [À vérifier]. L'État peut toutefois choisir de la compenser par les dotations, ce qui serait circulaire.
- **Les associations** supportent une charge réelle, atténuée par l'abattement.
- **L'ordre de grandeur** : si le secteur public pèse environ 10 % de la dépense professionnelle d'IA [À vérifier], la taxe qu'il paie représente environ 10 % de la recette, dont une partie seulement est un vrai coût net pour les administrations publiques.
- **Ce qu'on y gagne** : la cohérence du critère, en écho à la décision 2009-599 DC, et une incitation à la sobriété dans l'administration.
- **Le risque** : un frein à l'adoption de l'IA publique. Il est atténué par l'abattement et par le taux réduit sur équipement terminal.

---

## E. Suivi des 20 questions non traitées du fichier 17 (dont les 10 prioritaires, marquées ★)

| Q | Objet | Statut | Réponse ou décision | Itération |
|---|---|---|---|---|
| 69 ★ | L'article 401 de la directive TVA | **répondue**, à confirmer | O1 et D1 ; décisions 37 et 39 | M2 |
| 67 ★ | L'égalité, la confiscation | en cours | O2 et D3 ; décision 41 ; à compléter avec la justification du plafond | M3 |
| 68 ★ | La justification des différences de traitement | en cours | O2 ; décisions 44 et 46 ; les critères à rédiger | M3 |
| 60 ★ | La nature juridique et l'affectation | en cours | A1, O4, D4 ; décision 42 | M3 |
| 40 ★ | L'entraînement | **décidée** | Hors du champ ; piste ultérieure (décision 45) | M2 |
| 15 ★ | Le contexte relu et le cache | ouverte | — | M5 |
| 35 ★ | La cascade | **décidée** | La suspension, sans déduction (décision 37) | M2 |
| 32 ★ | Les octets des fournisseurs étrangers | en cours | O5 : l'enregistrement, la conversion légale, l'information sur facture | M4 |
| 26 ★ | Le tarif unique face à des prix très différents | **décidée** (sous condition) | Le tarif par classe (décision 39, D1) | M2 |
| 22 ★ | Le secteur public, les associations, la recherche | **décidée** | Dans le champ, avec l'abattement (décision 46, D5) | M2 |
| 1 | La productivité depuis Keynes | ouverte | — | M8 |
| 34 | Les prestations produites à l'étranger avec de l'IA | en cours | O5 : un risque assumé, à documenter | M4 |
| 55 | La formation rémunérée | ouverte | — | M6 |
| 63 | Si l'IA ne détruit pas d'emplois en net | ouverte | — | M7 |
| 70 | Le compteur, les aides d'État | en cours | O6, O9 ; décisions 43 et 44 | M4 |
| 71 | L'incidence de la taxe | ouverte | — | M10 |
| 73 | Les PME, les jeunes entreprises, les centres de données | ouverte | — | M10 |
| 75 | L'acceptabilité pour les entreprises | ouverte | — | M8, M10 |
| 78 | Les agents en chaîne, les données synthétiques | ouverte | Probablement réglé par la suspension (décision 37), à confirmer | M5 |
| 79 | Les erreurs, les réessais, les tests | ouverte | — | M5 |

**Décompte** : 4 décidées et 1 répondue (à confirmer), 6 en cours, 9 ouvertes.

---

## Historique du raisonnement

1. **2026-10-02, M1** : lecture du mandat, de l'intention, du corpus et du fichier 17. Vérification sur le web de l'article 401 et de ses critères (rapport du CPO de 2015, arrêts Vodafone et Tesco de 2020), des décisions 2025-1157 QPC, 2009-599 DC et 2012-662 DC, de l'article 2 de la LOLF modifié en 2021, de l'article 2 de la directive DAC, des arrêts Commission c/ Hongrie (2021) et ANGED (2018). **[C]**
2. Constat principal : **l'article 401, que le fichier 17 plaçait en tête des risques, n'est pas bloquant** si l'on évite la déduction en chaîne. Les vrais blocages sont **l'article 34** (le taux fixé par arrêté selon les « besoins »), **l'affectation** à un fonds sans base organique et **le compteur imposé aux éditeurs**. **[C]**
3. Tension identifiée avec une décision [G] : la décision 25 (« le montant par unité est égal au prix moyen ») et la décision 9 (le volume) produisent ensemble un **tarif unique** qui viole l'esprit du 50/50 pour les modèles peu chers. Le **tarif par classe** garde les deux décisions et rend le 50/50 vrai. **[C]**
4. **2026-10-02, M2** : l'orchestrateur valide par procuration les points 1, 2, 4 et 6 à 11 ; il accepte le point 3 sous condition (la démonstration au regard du 2ᵉ critère de l'article 401) et demande deux vérifications (m ≥ 1, la confiscation). Décisions 37 à 47 **[P]**. Recherches complémentaires : le rapport particulier de la Cour des comptes sur la TVA (2023) ; l'article LO 111-3-14 du code de la sécurité sociale ; la doctrine sur la confiscation (commentaire de la décision 2018-755 QPC, *Nouveaux Cahiers*). **Constat nouveau** : le cliquet de l'article LO 111-3-14 fait de la **voie « sécurité sociale »** la plus robuste pour protéger la recette (D4). **[C]**

## Questions ouvertes

- La levée de la condition de la décision 39 (D1).
- Le choix de la voie d'affectation (D4), à arrêter en M3.
- Le vote de m en LFSS plutôt qu'en loi de finances, si la voie (c1) est retenue.
- L'export « hors du champ » plutôt que « déclaré au taux nul » (O5), une précision juridique de la décision 30.

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
- CIBS, ordonnance n° 2021-1843 : https://www.douane.gouv.fr/fiche/code-des-impositions-sur-les-biens-et-services-contributions-indirectes

## Liens

- [mandat.md](mandat.md)
- [17-objection-questions-lecteur-critique.md](17-objection-questions-lecteur-critique.md)
- [04-hypothese-modalites-assiette-et-collecte.md](04-hypothese-modalites-assiette-et-collecte.md)
- [10-hypothese-taux-variable-indexe.md](10-hypothese-taux-variable-indexe.md)
- [08-hypothese-sdk-comptage-infalsifiable.md](08-hypothese-sdk-comptage-infalsifiable.md)
- [05-hypothese-revenu-universel-musk.md](05-hypothese-revenu-universel-musk.md)
- [11-cadrage-impact-economique.md](11-cadrage-impact-economique.md)
