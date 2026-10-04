# Relecture de cohérence M13 (agent neuf, lecture seule)

- **Statut** : rapport brut, recopié tel quel par l'orchestrateur ; les corrections sont suivies au journal (n° 98 et suivants)
- **Date** : 2026-10-04 ; état relu : commit 068cfa5

---

# Relecture de cohérence (lecture seule) — branche `metamaieutique/loi-jevons-faisabilite-2026-10-02`, état du commit 068cfa5 (M13)

**Méthode.** J'ai lu le mandat, l'intention, le journal (n° 1 à 97), le prompt-log, l'index, le glossaire, les notes 04, 05, 08, 10 à 19 (« En vigueur », avec les sections C à F de la note 18 et toute la note 19) et les trois livrables. J'ai exécuté `outils/sim_v4.py` et `outils/etude_impact_v01.py`, avec une sortie redirigée vers le scratchpad, ainsi que deux tests de variantes faits sans modifier les scripts.

**Ce qui concorde avec les scripts.** Tous les tableaux de l'étude d'impact (§ 5.1.1 à 5.1.7, 5.2.2, 5.2.4, 5.3.4, 5.4), la mise à jour M12 de la note 19 (l. 13-19), l'« état à la fin de M12 » de la note 18 (F, l. 805-810) et les décomptes du fichier 17 (49 décidées, 30 répondues, 1 ouverte) et de la section E (14, 6, 0). Seules exceptions, signalées plus bas : A6 et A12.

Notation : **[F]** signale un écart déjà connu, listé dans la section F de la note 18, que je confirme et chiffre. **[nouveau]** signale un écart absent de la section F.

---

## A. Contradictions de fond (de la plus grave à la moins grave)

**A1. [nouveau] Le tarif réduit de l'IA sur terminal : sa durée et son entrée en vigueur divergent d'un texte à l'autre, et l'IA locale peut se retrouver freinée.**
- La décision 60 prévoit 0,25 × le tarif « pendant trois ans ». On retrouve cette durée dans l'exposé (l. 67), dans l'étude (§ 4, l. 68) et dans le script (`TERM_RED_END=2030`).
- Le dispositif ne fixe **aucune durée de trois ans** (L.[…]-15, l. 177-185). Le tarif réduit y court jusqu'au critère de maturité, ou au plus tard jusqu'à la fin de la 5ᵉ année. L'étude (§ 8, l. 303) situe cette extinction en 2033.
- **Effet chiffré** : si le tarif réduit dure jusqu'à son terme légal, la recette baisse de 0,9 Md€ en 2031 et de 1,6 Md€ en 2032. Avec une extinction fin 2033, la cible n'est atteinte qu'en **2034** (m monte à 3,0) au lieu de 2033, et en **2037** au lieu de 2036 avec m ≤ 2.
- **Risque pour l'intention** : l'art. 16, II (l. 402) suspend L.-15 jusqu'à une « décision la déclarant compatible ». En attendant, l'IA sur terminal paierait le **plein tarif**, ce qui revient à freiner l'IA locale. Et si la Commission conclut à l'absence d'aide d'État (c'est la thèse de l'étude, § 6, l. 274), aucune décision de compatibilité n'interviendra, et L.-15 n'entrera jamais en vigueur.

**A2. [nouveau] Des décisions par procuration sont présentées comme validées ou voulues par l'auteur.**
- Dans le dispositif, le marqueur **[opus-5.5 → ggim]** (« validé par Guillaume », fichier 00, l. 218) est apposé sur des décisions prises par procuration :
  - l. 196 (décision 88) ;
  - l. 224 et 228 (décision 90) ;
  - l. 296 (décision 91).
- Toujours dans le dispositif, la note de la l. 438 parle de « règles de pilotage **voulues par l'auteur** » en citant les décisions 51, 75, 79 et 86. Or ces quatre décisions ont été prises par procuration, et la décision 84 précise même que « le repère des deux tiers est une décision par procuration (51), pas une décision de Guillaume ».
- Dans le journal, la décision 96 (l. 103) porte la mention « Contestation [ggim, par procuration] » : un marqueur [ggim] y est employé pour un acte fait par procuration.

**A3. [F, confirmé et chiffré] Les chiffres de l'exposé v0.2 contredisent ceux de l'étude d'impact.**
- § V, l. 95 :
  - « vers 2038 » (m ≤ 2) doit devenir **2036** ;
  - « dès 2034 » (m ≤ 3) doit devenir **2033** ; le multiple culmine à **2,5** en 2033 et 2034, puis revient à 2 en **2035**.
- § V, l. 97 : « 0,1 à 0,2 point en 2040 » doit devenir **0,21 point**, avec m ≤ 2 comme avec m ≤ 3. Il faut aussi dire que la baisse ne commence qu'au retour de m à 2 (en 2035 dans la trajectoire de référence, en 2036 avec m ≤ 2) et rappeler la condition de soutenabilité (décision 89).
- l. 81 et 111 : il manque « jamais moins qu'aujourd'hui » (décision 96).
- l. 121 (présentation du titre III) : il manque les décisions 89, 94 et 95.

**A4. [nouveau] Le coût de la sortie progressive au niveau du RSA est compté sur deux bases incompatibles.**
- `N_RSA` (sim_v4.py, l. 79-80) inclut **1,0 Md€** pour la sortie progressive (l'« hypothèse d'origine »). Or le modèle explicite du même script chiffre cette hypothèse à **− 0,52 Md€** (`sp_cost(650,'M11')`).
- `need(650)` vaut donc 7,52 Md€. La sortie progressive y pèse **1,52 Md€**, alors que l'étude, § 5.3.4 (l. 243), annonce un coût de **0** pour la modalité retenue au niveau du RSA.
- Le § 5.3.1 (l. 209, 1,0 Md€), le § 5.3.4 et le besoin net du tableau 5.1.1 (11,2 Md€ en 2031) ne se raccordent donc pas.
- Le § 5.3.1 était déjà signalé dans la section F, mais pas l'incohérence du modèle lui-même.

**A5. [nouveau] Le coût de la garantie familiale : l'étude, la note 18 et le dispositif ne disent pas la même chose.**
- L'étude, § 5.3.2 (l. 213), le déclare **nul** [opus-5.5].
- La note 18, D13.7 (l. 727), l'estime à **0,5 à 1 Md€ par an**. Il ne figure dans aucune composante de `N_RSA`.
- Le dispositif, art. 9, I (l. 318), garantit un RSA familial « **revalorisé comme le socle** », de façon permanente et y compris pour les nouveaux demandeurs (D9). Si le socle monte de 650 à 1 200 € de 2026, la garantie le suit, et son coût ne peut pas être nul.

**A6. [nouveau] La décision 94 n'a plus aucun effet dans la configuration retenue.**
- La note du dispositif (art. 13, IV, l. 380) affirme qu'elle « raccourcit d'un an » la période où m dépasse 2. L'étude (l. 103) attribue à cette décision le retour de m à 2 en 2035.
- Or la variante « sans l'excédent du fonds » de `sim_v4.py` donne une trajectoire **identique** : m = 2,5 en 2033-2034, m = 2 dès 2035, fonds de 15,8 Md€ en 2040, 0,21 point.
- La décision n'avait d'effet que sur les règles de M11. La dégressivité de la décision 96 l'a rendue sans objet.
- Le tableau de décomposition (étude, l. 107-114), qui est séquentiel, entretient cette lecture.

**A7. [nouveau] L'indexation du socle a deux rangs différents dans l'ordre d'emploi.**
- L'art. 13, I, 1° (l. 354) range « la revalorisation du socle » parmi les droits, au premier rang. Le 4° (l. 360) finance « l'indexation du socle » par la moitié du surplus seulement.
- L'art. 4, V (l. 264) rend automatique le suivi du revenu médian une fois la cible atteinte.
- L'exposé (l. 97) suit le 4°. Le script finance l'indexation en priorité, dans le besoin indexé, conformément au 1°.

**A8. [nouveau] Le mot « assiette » change de sens d'un article à l'autre.**
- L.-9 (l. 99) définit l'assiette comme un **volume** en octets-équivalents, qui ne dépend pas du multiple.
- L'art. 13, III (l. 374) parle d'une « assiette […] évaluée au multiple de l'année précédente », et la note de la l. 376 précise qu'il s'agit de la **dépense taxable**.
- Avec la définition par le volume, le retournement ne se déclencherait presque jamais, puisque le volume croît quand les prix baissent. C'est la définition par la dépense que le script applique.

**A9. [nouveau] La table de conversion est fixée par arrêté, alors que la décision 61 la voulait légale.**
- L.-11, I et II (l. 137-139) renvoient à un arrêté, de même que le forfait par compte de L.-6, III (l. 86).
- Or la décision 61 parle d'une « **table légale** de conversion », la note 18, D11 (l. 496), dit que « la loi fixe une table de conversion », et la note de L.-9 (l. 121) rattache elle-même les équivalences à l'article 34.
- Cela crée un risque d'incompétence négative sur l'assiette.

**A10. [nouveau] Des propositions d'agent figurent dans le dispositif sans marquage, et sans décision au journal.**
- Art. 4, VI : la règle sur les APL (D13.2, [C]).
- Art. 4, VII : la formation (D13.5, [C]). La note 18 (l. 41) annonçait qu'ils « seront arrêtés dans le dispositif », mais aucune décision ne les arrête.
- L.-12 : les bornes à 0,2 et 2 fois l'indice, qui ne sont qu'un « par exemple » en D1 (l. 264).
- L.-3, I, 4° : le seuil de dix fois le volume médian.
- L'en-tête du dispositif (l. 7) promet pourtant de marquer [opus-5.5] toute proposition non validée.

**A11. [nouveau] Les dates d'entrée en vigueur du titre II forment une boucle.**
- L'art. 15, II (l. 394) fait entrer en vigueur les articles 4 à 10 « selon le calendrier prévu à l'article 10 ». Or l'art. 10 n'ordonnance que le socle, et il est lui-même soumis à ce calendrier.
- L'art. 8 (la reprise du RSA et de l'ASS, à servir dès la phase 0, art. 8, IV) renvoie à « la date d'entrée en vigueur du présent titre », qui n'est définie nulle part.
- L'art. 7 n'a pas de date.
- S'y ajoute un risque de chevauchement : l'art. 6, III (RSA et prime d'activité) et l'art. 9, I (le complément familial) peuvent jouer en même temps. C'est déjà signalé dans la section F.

**A12. [nouveau] L'étude d'impact, § 5.3.4 (l. 237), surévalue la marche du 13ᵉ mois.**
- Elle écrit « 400 à 700 € ». Le script donne **403 à 521 €**, au socle de 1 200 € (1 379→858, 1 558→1 076, 1 736→1 294, 1 915→1 512), et aucune marche au socle de 650 €.
- Le chiffre vient du prompt-log, M12, l. 48.

**A13. [nouveau] L'exposé v0.2 ne mentionne pas la condition de cinq ans de séjour comme choix ouvert.**
- La décision 59 demande de la présenter comme un « choix politique ouvert ». La section F (l. 858) la range parmi les corrections « appliquées en M9 ».
- L'exposé (l. 83-85) n'en parle pas. Il ne présente que deux choix ouverts. L'étude, elle, le fait (§ 5.3.3).

**A14. [nouveau] Les textes ne s'accordent pas sur qui tranche la question des étudiants et du patrimoine.**
- L'exposé (l. 85) et le dispositif (l. 270) la renvoient au « débat parlementaire ».
- L'étude, § 5.1.4 (l. 140-142), parle de choix « **réservés à l'auteur du projet** […] pas tranchés par le Gouvernement ». Dans un document du Gouvernement, l'auteur du projet, c'est le Gouvernement : la phrase se contredit.
- Les décisions 70 et 71 les réservent à Guillaume. (Voir aussi C1.)

**A15. [nouveau] L'amende pour fausse déclaration d'usage personnel peut atteindre une personne physique.**
- L.-21, IV (l. 228) sanctionne la « fausse déclaration d'usage personnel » prévue à L.-3, II. Cette déclaration est faite par « l'utilisateur », qui peut être un salarié ou un particulier.
- L.-6, III (l. 86) rend redevable « la personne qui utilise […] au moyen d'un compte souscrit au nom d'une personne physique », ce qui, à la lettre, vise le salarié.
- Cela entre en tension avec L.-3, IV (« le salarié n'est jamais redevable »), avec la décision 53 (« l'entreprise autoliquide […] sous peine de majoration ») et avec l'intention d'épargner les particuliers.

**A16. [nouveau] Plusieurs points du dispositif sont ambigus ou mal rédigés.**
- **Le multiple pendant la phase 0** (L.-14, III, l. 170) : la formule « au plus tard jusqu'au 31 décembre de la troisième année suivant l'entrée en vigueur » ne dit pas clairement si m est bloqué à 1 pendant la phase 0. Elle se combine mal avec l'annexe C1, où la LFSS pour 2028 fixe déjà m.
- **Le décompte des années** n'est pas le même partout : l'art. 10 compte 2028 comme la 1ʳᵉ année, alors que l'étude (§ 8) lit L.-15, III comme une extinction en 2033 (« cinquième année suivant »).
- **Le statu quo** : l'art. 15, I renvoie à un « délai de statu quo mentionné à l'article 16 », que l'art. 16 ne mentionne pas.
- **La reconnaissance de caractères (OCR)** : l'exposé (l. 49) l'exclut comme système qui « ne génère pas de contenu ». La note 18, D13.1 (l. 660), l'exclut au titre de l'exception du II. Mais le II de L.-1 (l. 33) écarte cette exception pour la « transcription », ce qui pourrait réintégrer l'OCR.
- **Les sanctions** : l'exposé (l. 63) dit qu'elles « sont celles des taxes sur le chiffre d'affaires », alors que L.-21, II à IV crée des amendes propres.
- **La présentation des titres** : l'exposé attribue au titre III « la règle d'équilibre sur trois ans » (l. 121) et au titre IV « la phase de lancement » (l. 123), qui se trouvent toutes deux à l'art. 10, dans le titre II.

**A17. Des notes « En vigueur » et le glossaire n'ont pas suivi les décisions récentes [nouveau, sauf mention].** La section F (l. 784) affirme pourtant que les notes 04, 05, 08, 10 et 11 sont à jour.
- **Note 11** :
  - l. 10 : « il commence quand le socle cible est atteint (2034 à 2038) ». Selon la décision 89, il commence au retour de m à 2 : en 2035 (trajectoire de référence) ou en 2036 (m ≤ 2).
  - l. 17 : « 0,1 point (m ≤ 2), 0,2 point (m ≤ 3) » doit devenir 0,21 dans les deux cas.
  - La décision 89 n'y figure pas.
- **Note 14**, l. 14 : « 2034 avec m = 3 […] 2038 avec m ≤ 2 » doit devenir 2033 et 2036.
- **Note 10** :
  - les décisions 79, 84 et 89 n'y figurent pas, alors que le journal (décision 79) cite la note 10 parmi les fichiers concernés ;
  - l. 21 : « la simulation v4 (M10) le modélisera » est périmé.
- **Note 08**, l. 16 : l'abattement « par entreprise […] à préciser en M8 » est antérieur à la décision 88.
- **Note 05**, l. 25 : un « socle réduit pour les revenus élevés du patrimoine » y figure parmi les paramètres, contre la décision 71, qui le garde en variante.
- **Glossaire**, l. 28 : l'abattement y est « un volume annuel non taxé par entreprise », alors que la décision 88 fixe 1 000 € **de taxe** par **groupe**. Le glossaire ne définit pas non plus le « retournement » de la décision 95.
- **Note 19** [F pour les sections 2.0 à 2.6 et la « réponse franche »] :
  - « réponse franche », l. 43-49 :
    - point 3 : 2038/2034 doit devenir 2036/2033 ;
    - point 4 : 890 € doit devenir 910 € ;
    - point 5 : « 0,1/0,2 » doit devenir 0,21 ;
    - point 6 : les ouvertures 2036/2037/2039 doivent devenir 2036/2036/2038. Surtout, il n'y a **aucune** contribution d'équilibre avec m ≤ 4 (et non 2,8 Md€) ; elle est de 1,3 Md€ (2039) et 3,7 Md€ (2040) avec m ≤ 3. Le besoin hors taxe est d'environ 17 à 20,5 Md€ ;
    - point 7 : 748 € doit devenir 767 € ;
    - point 9 : avec une indexation à 1 %, la cible est atteinte en 2034 (et non 2036) ; avec une élasticité de 0,3, en 2032 ; avec les inactifs, en 2035 (m ≤ 4) et 2038 (m ≤ 3).
  - [nouveau] § 1.1, l. 61 : la règle d'ouverture sur trois ans y est présentée comme une « variante ».
  - [nouveau] § 1.2, l. 76 : l'abattement y figure en « dépense exonérée […] à fixer », avant la décision 88.
  - [nouveau] § 4, l. 237 : « l'excédent du fonds n'est pas employé » contredit la décision 94.
  - [nouveau] Question ouverte, l. 265 : le multiple pendant la montée en charge n'a pas été clos après la décision 84.
- **Note 18** :
  - [F] l. 43 : les chiffres de M9. Il faut lire 2033/2036, 910 €, 0,21 point, une ouverture dans le scénario bas entre 2036 et 2038, et aucune contribution d'équilibre avec m ≤ 4 ;
  - [nouveau] l. 41 : D13.2 et D13.5 « seront arrêtés en M10 » ;
  - [nouveau] D8, l. 423 : la cible du fonds est donnée en « six mois de prestations du socle », contre la décision 81 ;
  - [nouveau] D13.8, l. 742 : « 2039 (m ≤ 2) » doit devenir 2038 ;
  - [nouveau] Questions ouvertes, l. 896 : le multiple « (cible vers 2038 / 2034) » n'a pas été clos après la décision 84.

## B. Erreurs de tenue

- **B1. [nouveau] La numérotation des itérations ne concorde pas.**
  - La section C de la note 18 (l. 219-236) n'est pas renumérotée : M8 y désigne l'exposé et M14 le rapport, et le plan y est « resserré à 14 ».
  - La section E (l. 749), la section F (l. 828-836 : M9 à M15) et l'index (« renuméroté M9 à M15 ») suivent une autre numérotation.
  - « M12 » désigne tantôt la relecture de cohérence (décision 92, F l. 833), tantôt le cycle des décisions 94 à 97 (en-tête de l'étude, l. 7 ; F l. 805).
  - « M13 » désigne tantôt la confrontation (F), tantôt le lancement de la relecture (prompt-log, commit).
- **B2. [nouveau] Le journal n'a pas reçu les validations faites par procuration en M13.** Il s'arrête au n° 97. Les validations du prompt-log, M13 (l. 36-38), n'y figurent pas :
  - la dégressivité dans les douze mois ;
  - le RSA des actifs à faible revenu, servi par la branche sous la forme d'un complément différentiel ;
  - les paramètres à soumettre à l'économiste.

  En conséquence, l'étude (l. 116) et le dispositif (l. 296) parlent encore d'une « proposition non arrêtée ».
- **B3. [nouveau] La rubrique « Points en suspens » du journal est périmée (l. 108-111).**
  - Les formules de la v0.1 qu'elle signale ont disparu de la v0.2.
  - La « condition de la décision 39 à confirmer » a été levée par la décision 48.
- **B4. [nouveau] L'index (fichier 00) est incomplet ou périmé.**
  - `mandat.md` manque dans les « Fichiers hors numérotation » (l. 233-243), et `sim_v3.py` n'est pas cité.
  - Ligne 05 : « 16 à 20 Md€ » est un chiffre ancien.
  - Ligne 12 : « taxes ~100 % du prix HT », alors que la note 12 donne environ 1,4 fois.
  - Ligne 17 : « en M9 : 44/30/6 », alors que le décompte actuel est 49/30/1.
- **B5. [nouveau] Dans le fichier 17, des renvois vers « M11 » n'ont pas été tenus.**
  - Q54 (les effets sur l'offre de travail), Q66 (l'effet net sur l'arbitrage entre travail et IA) et Q72 (le chiffrage pour les PME sur les marchés tiers) : l'étude ne les traite pas. La section F ne cite que Q6, dont la reprise est confirmée.
  - Q19, Q49, Q55 et Q79 renvoient à des points « arrêtés / rédigés en M10 », mais aucune décision ne les arrête.
- **B6. [F, corrigé]** La section F (l. 845) parle de « 60 renvois [À vérifier] » dans le dispositif. On en compte **77**, répartis sur 61 lignes.
- **B7. [F]** L'exposé v0.2 (l. 129-137) contient encore les rubriques « DISPOSITIF » et « ÉTUDE D'IMPACT » marquées « À rédiger ». Le fichier 17, Q6 (le montant des docks en euros actuels), n'a pas été traité.
- **B8. [nouveau]** Le mot « cliquet » désigne deux choses : la protection de l'art. LO 111-3-14 (glossaire) et la règle refusée par la décision 89.
- **B9. [nouveau]** L'étude d'impact, document formel, contient des renvois internes au corpus : « Intention de l'auteur » (l. 57) et « réservés à l'auteur du projet » (l. 140).

## C. Points qui demandent une décision de l'auteur (non tranchés ici)

- **C1.** Qui tranche la question des étudiants et du patrimoine ? Les décisions 70 et 71 la réservent à Guillaume. L'exposé et le dispositif la renvoient au Parlement. L'étude parle de « l'auteur du projet ». Quelle présentation garder dans les livrables ?
- **C2.** Le tarif réduit de l'IA sur terminal : une durée ferme de trois ans (décision 60, script) ou une extinction par maturité dans la limite de cinq ans (dispositif) ? Faut-il en suspendre l'application jusqu'à une décision de la Commission (art. 16, II), au risque de freiner l'IA locale ?
- **C3.** La modalité de la dégressivité (dans les douze mois), validée par procuration en M13. À elle seule, elle fait passer la cible avec m ≤ 2 de 2038 à 2036. Elle réduit aussi les versements de 1,18 Md€ à la cible par rapport à un plancher sans dégressivité. Cette modalité touche la décision 31 [G] (« une sortie progressive »).
- **C4.** Une personne physique (un salarié, un particulier) peut-elle être frappée de l'amende de 150 € par compte et par mois ?
- **C5.** L'indexation du socle sur le revenu médian, une fois la cible atteinte : est-ce un droit prioritaire (art. 4, V ; art. 13, I, 1°) ou un emploi de la moitié du surplus (art. 13, I, 4°) ?
- **C6.** La trajectoire de référence avec m ≤ 3 (décision 84, par procuration) dépasse le repère des deux tiers pendant deux ans. Ce repère a lui-même été posé par procuration (décision 51). Guillaume veut-il confirmer ce choix au regard de « drastique mais juste » ?
- **C7.** La garantie familiale « revalorisée comme le socle » (art. 9, I) : doit-elle suivre la hausse du socle vers la cible, ce qui est coûteux, ou seulement la revalorisation du RSA ?

---

## Décompte

- **A (contradictions de fond)** : 17 points, dont 15 nouveaux, 1 connu (A3) et 1 regroupement mixte (A17).
- **B (tenue)** : 9 points, dont 7 nouveaux et 2 déjà connus (B6, B7).
- **C (décisions de l'auteur)** : 7 points.
- **Section F** : ses écarts sont tous confirmés. Le décompte des marqueurs [À vérifier] y est corrigé (77 au lieu de 60).

## Les cinq corrections les plus urgentes

1. **Aligner les chiffres de l'exposé v0.2 sur l'étude d'impact (A3).** Il faut lire 2036 et 2033 (m à 2,5 pendant deux ans), 0,21 point, une baisse qui commence au retour de m à 2, et le principe « jamais moins qu'aujourd'hui ». Il faut aussi y introduire les décisions 59 (A13) et 89, 94 et 95.
2. **Remplacer les marqueurs qui prêtent des décisions par procuration à l'auteur (A2).** Dans le dispositif, [opus-5.5 → ggim] devient [opus-5.5 as ggim] (l. 196, 224, 228 et 296) ; la note de la l. 438 doit être corrigée (« voulues par l'auteur ») ; au journal, la décision 96 ne doit plus porter [ggim]. Il faut aussi marquer [opus-5.5] les propositions non validées qui figurent dans le dispositif (A10).
3. **Mettre en cohérence le tarif réduit sur terminal (A1).** La durée doit être la même dans la loi, l'exposé, l'étude et le script. La rédaction de l'art. 16, II doit être revue pour ne pas freiner l'IA locale. La trajectoire doit être recalculée si la durée change.
4. **Remettre d'aplomb le chiffrage de la sortie progressive et de la garantie familiale (A4, A5, A12).** La base `N_RSA` doit être raccordée à `sp_cost`, le coût de la garantie familiale doit être chiffré ou justifié, et la marche du 13ᵉ mois corrigée à 403-521 €. Il faut aussi retirer l'effet attribué à la décision 94 (A6).
5. **Corriger les défauts de rédaction du dispositif (A7 à A9, A11).** Cela concerne le rang de l'indexation dans l'art. 13, le sens d'« assiette » dans l'art. 13, III, la table de conversion fixée par la loi, et l'entrée en vigueur des articles 7 à 10. Enfin, inscrire au journal les validations de M13 (B2) et renuméroter le plan (B1).
