# Journal des prompts

> Mode de versionnement (c) : chaque itération donne lieu à un commit et à une réécriture propre et concise du message de l'utilisateur, sans perte d'information.

## Itération 1 (2026-10-02)

Guillaume demande de reprendre les commits en mode (c). Il a compris qu'il faut consigner l'**intention de l'auteur dans un fichier dédié**, et pense qu'il faut l'ajouter au skill. Il demande de commencer par consigner son intention, ses états d'âme et tout ce que Claude a pu observer, **uniquement ce qui est lié à l'idée du projet**. Ce fichier doit être géré comme les autres notes.

## Itération 2 (2026-10-02)

Guillaume confirme que le fichier d'intention lui convient, y compris le fait d'y consigner ses convictions. Il demande de rédiger le mandat de la session metamaieutique.

## Itération 3 (2026-10-02)

Guillaume demande si la session metamaieutique ne devrait pas être lancée dans une autre session. Claude répond oui (son contexte est saturé, et la compréhension fine est transmise par le fichier d'intention, le mandat et la mémoire), et propose d'utiliser un worktree.

## Itération 4 (2026-10-02)

Guillaume demande d'expliquer la clause d'adaptation des décisions juridiquement impossibles.

## Itération 5 (2026-10-02)

Guillaume recadre : la clause est trop étroite. Le **but du mandat est justement de rendre l'idée réalisable et légale**, en réglant ou en rendant possibles toutes les difficultés techniques, avec le **plein soutien du Gouvernement**. Il n'arrive pas à rendre son idée réalisable, et c'est pour cela qu'il veut faire de la metamaieutique. → Le mandat est réécrit : **l'intention est le seul invariant**, toutes les modalités peuvent être revues, et le résultat doit être légal.

## Itération 6 (2026-10-02)

Guillaume valide le mandat (« je crois que c'est bon »), sans répondre explicitement aux deux points ouverts. Par défaut, le droit de référence est celui du point 4 du mandat, et le soutien du Parlement n'est pas précisé. → Branche `metamaieutique/loi-jevons-faisabilite-2026-10-02` créée dans le worktree `~/Documents/Jevons-meta`, où le mandat est commité. Mémoire du projet recopiée pour ce dossier. Skill metamaieutique mis à jour : reprise d'un mandat déjà validé, worktree.

## Itération 7 (2026-10-02)

Guillaume lance la session metamaieutique dans `~/Documents/Jevons-meta`.

## Itération 8 (2026-10-04)

Guillaume fait fusionner la branche metamaieutique dans `main` (commit `0712000`). Il demande ensuite de **mettre dans `CLAUDE.md` l'observation de Claude sur son utilisation du skill et de `CLAUDE.md`**, pour la **tester comme extension du skill** avant de l'intégrer au skill. Fait : une section « Extension du skill, à tester » dans `CLAUDE.md`, dix observations avec chacune une règle à essayer, marquées comme propositions de `[sonnet-5.5]`, non validées. L'identité `sonnet-5.5` est ajoutée à l'index.

## Itération 9 (2026-10-04)

Guillaume charge le skill `maieutics` et demande de **commencer par la migration au nouveau format**. Il précise : **tous les noms restent en français** (« c'est pas grave »), et il faut **indiquer aux skills que l'intendance de ce dépôt est en français**. Il accepte que le mandat, le rapport de retour, les audits et le transcript soient déplacés sans être réécrits, le transcript allant dans `archive/`. La migration est **mécanique** ; **l'élagage viendra après**. La branche metamaieutique, déjà fusionnée, peut être supprimée, ainsi que son worktree s'il n'a pas de modifications.

## Itération 10 (2026-10-04)

Guillaume demande de lancer l'**élagage** (« vas-y pour l'élagage »), proposé après la migration.

## Itération 11 (2026-10-04)

Guillaume demande de lancer la relecture de l'élagage (« oui, lance la relecture »). Il demande aussi de regarder dans tout l'historique des commits s'il n'a pas mis d'informations personnelles, pour décider s'il rend le dépôt public.

## Itération 12 (2026-10-04)

Guillaume demande la seconde relecture des corrections (« oui fais relire ») et redemande de vérifier tout l'historique des commits à la recherche d'informations personnelles, avant de décider s'il rend le dépôt public. Retouches de tenue de la seconde relecture : note 18 (numéros du journal « hors session », en-tête) ; note 05, [Unverified] sur la garantie familiale, aligné sur le n° 108 du journal.

---

# Session metamaieutique « Rendre la Loi Jevons réalisable » (branche `metamaieutique/loi-jevons-faisabilite-2026-10-02`)

> À partir d'ici, les messages consignés sont ceux de l'orchestrateur (Claude), qui parle **par procuration** au nom de Guillaume, d'après `mandat.md` et `intention-de-l-auteur.md`. Les décisions qui en découlent sont marquées **[P]**.

> **Depuis l'itération M8, les entrées sont ajoutées en tête** (la plus récente en premier), comme le demande la nouvelle version du skill. Les entrées M0 à M7, plus bas, restent dans l'ordre chronologique.

## Itération M20 (2026-10-04) — Guillaume : lecture confirmée, besoin de données ; fin de la session, rapport de retour

**Message de Guillaume** (et non par procuration) :
1. Il **confirme** la lecture de l'orchestrateur : les paramètres sont les valeurs, les conditions sont les règles et les variantes. Il précise que l'application Rust **aura besoin de données** « à ce moment-là ». Noté dans la note 19.
2. Il pense que la branche est **à remettre dans `main`**, et que la session va **se terminer avec ce répertoire** (le worktree). L'orchestrateur écrit `rapport-de-retour.md` (la pièce manquante), vérifie en lecture seule que la fusion donne deux conflits (le journal et le prompt-log, à garder des deux côtés), et **demande confirmation avant de fusionner et de supprimer le dossier**.

## Itération M19 (2026-10-04) — Guillaume : l'application Rust doit se régler en temps réel

**Message de Guillaume** (et non par procuration) : l'application Rust devra permettre de **changer les paramètres et les conditions en temps réel**. Noté (journal n° 113, note 19). La lecture de l'orchestrateur (paramètres = valeurs ; conditions = règles et variantes) est marquée à confirmer. Rien n'est lancé.

## Itération M18 (2026-10-04) — Guillaume : corrections des chiffres et des phrases fausses ; une application Rust à venir

**Message de Guillaume** (et non par procuration), après avoir lu le résumé des questions du lecteur aveugle :
1. **Corriger les deux erreurs de chiffres et les phrases fausses** (la somme 5,9 et non 6,0 ; le produit 3 × 0,7⁵ ; les importations ; le rapport « entre une et quatre fois »). Fait (journal n° 112). Les trois autres contradictions du lecteur ne sont pas corrigées : il n'a pas demandé de les traiter.
2. **Pour les questions du lecteur aveugle, il ne sait pas** : rien n'est décidé. Elles restent consignées, non classées.
3. **Noter qu'on fera « à un moment » une application en Rust pour simuler la mesure sur tous les différents indicateurs.** Noté (journal n° 111, note 19). Rien n'est lancé.

## Itération M17 (2026-10-04) — questions de la confrontation à l'aveugle consignées ; session en pause

Le lecteur aveugle (Sonnet 5.5, qui n'a lu que les trois livrables) a rendu **97 questions et 20 contradictions**. Elles sont consignées telles quelles dans la note `21-confrontation-aveugle-M15-questions.md`. **Le classement face au corpus (phase 2) n'est pas lancé** : Guillaume a demandé une pause pour interroger le corpus avec lui. Aucun agent ne tourne.

## Itération M16 (2026-10-04) — Guillaume : un chantier d'étude sur l'effet de consommation

**Message de Guillaume** (et non par procuration), pendant la pause qu'il a demandée : il faut noter qu'il faut **étudier l'impact économique lié au surplus de consommation** que génère la mesure, **par tranche d'âge**. Il cite les **jeunes adultes en formation initiale qui vivent chez leurs parents** : pour lui, c'est un **coup de pouce pour les jeunes les plus défavorisés**, et un **surplus de TVA et d'achats de biens et services**. L'orchestrateur a reformulé (étude à faire, pas de décision d'inclure les étudiants) avant de consigner : journal n° 110, note 18 (questions ouvertes), fichier 17 (Q50). Rien d'autre n'est lancé : la session est en pause, à la demande de Guillaume.

## Itération M15 (2026-10-04) — passe de corrections terminée ; lancement de la confrontation à l'aveugle (Sonnet)

**Message de Guillaume** (et non par procuration) : il consomme ses tokens très vite et demande s'il peut changer de modèle ou réduire l'effort. Après discussion, il approuve ce plan : l'agent de corrections termine avec Opus ; la confrontation à l'aveugle et le rapport de retour sont confiés à des agents **Sonnet** ; les corrections après la confrontation se limitent à ce qui est juridiquement bloquant. L'orchestrateur est passé à Sonnet 5.5 (`/model`).

Réponse par procuration au tour de l'agent (journal 98 à 109 ; les 26 points de la relecture sont corrigés, sauf Q6 renvoyée à l'expertise ; trajectoire révisée : cible en 2033 avec m ≤ 3, m revient à 2 en 2035, baisse des cotisations de 0,16 point en 2040 ; avec m ≤ 2, cible en 2037) :
1. **Le mécanisme D11 bis est validé** [opus-5.5 as ggim]. Pourquoi : il garantit que l'IA locale ne paie jamais le plein tarif à cause de la procédure, ce qui est l'intention (« ménager ce qui démarre »). À faire relire par un juriste.
2. **Le retard possible de toute la recette** si la Commission ouvre la procédure formelle est accepté, avec une **prénotification précoce**, dès la rédaction. C'est une **hésitation** pour le rapport de retour.
3. **Les effectifs de la garantie familiale** (410 000 foyers) et les paramètres de la décision 100 vont à l'économiste.
4. **Les hésitations 104 et 107** (la dégressivité dans les douze mois, qui touche la décision 31 [G] ; m ≤ 3 au-delà du repère des deux tiers) sont à lire en premier dans le rapport de retour.
5. **Pas d'élagage de la note 19 maintenant** : l'élagage est une proposition à faire à Guillaume (maieutics § 3), pas à décider par procuration.
6. **Q6, Q54, Q66 et Q72** : renvoyées à l'expertise dans le rapport de retour.
7. **La note 21 citée dans le plan** : on la crée pour les questions de la confrontation. La note 20 est la relecture de cohérence.
8. **Confrontation à l'aveugle**, par un agent neuf (Sonnet) qui lit **uniquement les trois livrables**, centrée sur la légalité.

## Itération M14 (2026-10-04) — rapport de la relecture de cohérence ; arbitrages des points C ; lancement des corrections

La relecture de cohérence, faite par un agent neuf en lecture seule, a relevé 17 contradictions de fond, 9 erreurs de tenue et 7 points de décision. Son rapport est recopié tel quel dans la note `20-audit-coherence-M13.md`. Les arbitrages par procuration des points C :
- **C1, les étudiants et le patrimoine** : dans le **corpus**, la question reste **réservée à Guillaume** (décisions 70 et 71). Dans les **livrables**, qui sont des documents du Gouvernement, elle est présentée comme une **option ouverte soumise au débat parlementaire**, sans mention de « l'auteur ». Pourquoi : un livrable formel ne renvoie pas au corpus, et la décision reste à Guillaume avant toute diffusion.
- **C2, le tarif réduit sur terminal** : 0,25 × le tarif **pendant trois ans**, puis une extinction, sauf **prolongation votée en LFSS jusqu'à cinq ans au plus**. L'extinction est avancée si le critère de maturité est atteint. Le dispositif, l'exposé, l'étude et le script doivent dire la même chose. **Contrainte d'intention** : l'IA locale ne doit **jamais** payer le plein tarif à cause de la procédure de notification. Il faut réécrire l'article 16, II : notification en amont pour une décision avant l'entrée en vigueur, une décision « constatant l'absence d'aide ou la compatibilité », et une solution légale si la décision tarde. L'agent la propose, et le risque résiduel est dit dans la note 18.
- **C3, la dégressivité dans les douze mois** : elle est maintenue (décision 72). Elle sera signalée comme **hésitation** dans le rapport de retour, puisqu'elle touche la décision 31 [G].
- **C4** : **aucune personne physique non professionnelle ni aucun salarié** n'est passible de l'amende. Seuls les professionnels sont visés, y compris les entrepreneurs individuels. Pourquoi : épargner les particuliers.
- **C5, l'indexation du socle** : c'est un **droit prioritaire**, au 1° de l'ordre d'emploi, comme dans le script. Le 4° est corrigé. Pourquoi : « les droits d'abord » et la non-régression.
- **C6, la trajectoire de référence avec m ≤ 3** : elle est maintenue (décision 84). Elle sera signalée comme hésitation dans le rapport de retour.
- **C7, la garantie familiale** : elle suit la **revalorisation légale du RSA**, pas la hausse du socle. Pourquoi : la non-régression se mesure par rapport au droit actuel. Son coût est à chiffrer dans le script, puisqu'il n'est pas nul.

Les corrections des points A et B sont confiées à un **agent neuf** (l'agent de travail est saturé), en commençant par les cinq plus urgentes, puis toutes les autres. Il inscrit aussi au journal les validations de M13 (point B2) et les arbitrages ci-dessus.

## Itération M13 (2026-10-04) — sortie progressive corrigée ; lancement de la relecture de cohérence

Réponse par procuration au tour de l'agent (journal 94 à 97 ; la sortie progressive ne fait plus jamais moins bien que le droit actuel ; scénario central : la cible est atteinte en 2033, m revient à 2 en 2035, la baisse des cotisations atteint 0,21 point en 2040 ; avec m ≤ 2, la cible est atteinte en 2036) :
1. **La dégressivité reste dans les douze mois** : validé. Pourquoi : la décision 72 est respectée, le plancher protège déjà contre toute régression, et le décret fixe le nombre de mois. L'étude d'impact doit dire franchement que ce placement explique une grande part du gain de trajectoire, et montrer la variante.
2. **Le RSA des actifs à faible revenu est gardé explicitement** sous la forme d'un complément différentiel servi par la branche : validé. Pourquoi : la non-régression (D9) ; un quart-temps au SMIC ne doit jamais perdre par rapport à aujourd'hui.
3. **Les paramètres de la sortie progressive** (600 000 reprises par an, droit actuel simplifié) : ajoutés à la liste des points à faire confirmer par l'économiste.
4. **La relecture de cohérence** est confiée par l'orchestrateur à un **agent neuf, en lecture seule**, sur le corpus, les trois livrables et les deux journaux. Son rapport sera transmis à l'agent de travail pour les corrections, en même temps que les points 1 à 3.

## Itération M12 (2026-10-04) — étude d'impact v0.1 rédigée ; ajustements avant la relecture de cohérence

Réponse par procuration au tour de l'agent (journal 88 à 93 ; l'étude d'impact v0.1 est créée, ses chiffres sortent d'un script, 0 écart ; le fichier 17 compte 45 décidées, 34 répondues et 1 ouverte, Q50, réservée à Guillaume ; la section E n'a plus de question ouverte) :
1. **La variante `M79_FONDS`** (ramener m à 2 dès 2036 en comptant l'excédent du fonds) : adoptée. Pourquoi : elle réduit d'un an la période où m dépasse 2, ce qui est l'esprit de la décision 79.
2. **Le retournement défini sur l'assiette** (la dépense taxable), et non sur le produit : adopté. Pourquoi : une baisse votée de m ne doit pas déclencher la clause.
3. **Contestation sur la sortie progressive.** Qu'un mi-temps au SMIC touche moins qu'avec la prime d'activité actuelle (1 008 € contre 1 076 €) est une **régression** : cela contredit la garantie de non-régression (D9) et l'intention d'émancipation, puisque reprendre un travail doit toujours rapporter au moins autant qu'aujourd'hui. Il faut l'écrire dans le dispositif, pas seulement l'annoncer :
   - le bénéficiaire reçoit **le plus favorable** de la sortie progressive et de la prime d'activité ;
   - la **marche de 400 à 700 €** à la fin des 12 mois est supprimée par une **dégressivité linéaire** inscrite dans la loi (les paramètres sont fixés par décret).
   Les deux points sont à chiffrer dans l'étude d'impact.
4. **Les réponses aux questions 8, 71, 73 et 74** : validées. La réponse à Q71 (« on saisit la valeur de l'usage, là où elle se réalise ») est fidèle à l'intention.
5. **La suite.** L'agent applique les points 1 à 3 et met à jour la section F. Ensuite, l'orchestrateur lance lui-même la **relecture de cohérence** par un agent neuf en lecture seule, comme le prévoit le skill. Viendront ensuite les corrections, puis la confrontation à l'aveugle.

## Itération M11 (2026-10-04) — dispositif v0.1 rédigé ; passage à l'étude d'impact (agent neuf)

Réponse par procuration au tour de l'agent (journal 84 à 87 ; le dispositif v0.1 compte 20 articles, un projet de loi organique et une annexe LFSS / LF ; les unités du script sont vérifiées et cohérentes) :
1. **L'abattement de 1 000 € de taxe par groupe et par an**, non indexé et révisable en LFSS : validé. Pourquoi : c'est un abattement, pas une franchise (la décision 30 est respectée), son coût ne croît pas avec m, et il ménage les plus petits.
2. **Contestation de la proposition de « cliquet »** (ne baisser m que si la recette couvre aussi la baisse des cotisations déjà engagée). Elle maintiendrait m au-dessus de 2 pour le seul double dividende, ce qui contredit le pourquoi de la décision 79. **La règle retenue est l'inverse** : on n'engage une baisse des cotisations que si elle est **soutenable avec m ≤ 2**. Ainsi le double dividende ne recule pas, et il ne tient pas m au-dessus de 2. Il faut le modéliser et dire ce que cela change.
3. **Les montants de sanction** sont gardés comme point de départ, à faire relire par le juriste (et à vérifier sous l'angle de la proportionnalité).
4. **Le plafond de la sortie progressive à 50 %**, avec un taux fixé par décret : validé. Les taux marginaux seront chiffrés dans l'étude d'impact.
5. **Les écarts de chiffres de l'exposé v0.2** seront corrigés à la relecture de cohérence : les inscrire dans la liste de la section F, pour ne pas les oublier.
6. **Passer à M11, l'étude d'impact v0.1.** L'agent étant saturé, un **agent neuf** reprend, à partir de la section F de la note 18.

## Itération M10 (2026-10-04) — exposé des motifs v0.2 rédigé ; passage au dispositif

Réponse par procuration au tour de l'agent (journal n° 77 à 83 ; l'exposé v0.2 est créé ; l'indexation fait passer la cible de 2034 à 2038 avec m ≤ 2) :
1. **Le multiple pendant la montée en charge** : le **dispositif garde la fourchette légale de 1 à 4 et le vote annuel** ; il n'y inscrit pas de trajectoire. L'**étude d'impact** présente comme **trajectoire de référence du Gouvernement m = 3 au plus pendant la montée en charge**, avec la justification renforcée, puis un retour à 2. Pourquoi : cela sert mieux le but (la cible en 2034), le Gouvernement soutient pleinement le projet, et la décision reste au Parlement chaque année. Le repère des deux tiers est une décision par procuration (51), pas une décision de Guillaume.
2. **L'indexation à 2 %** : la sensibilité (1 %, 2 %, 3 %) va dans l'étude d'impact, et la confirmation est demandée à l'économiste. **À vérifier d'abord** : la cohérence des unités du script. Si les montants sont indexés en nominal, le marché de l'IA (et donc la recette) doit lui aussi être en nominal. Le confirmer ou corriger.
3. **La baisse des cotisations est suspendue avant de puiser dans le fonds, hors retournement** : validé. C'est cohérent avec « les droits d'abord ».
4. **L'exposé v0.2 est accepté en l'état** ; le contrôle fin se fera à la relecture de cohérence et à la confrontation à l'aveugle.
5. **Passer à M10 : le dispositif v0.1**, en forme légistique, organisé en titres (la taxe, la branche et le chômage universel, l'affectation et la loi organique, l'entrée en vigueur et la notification). Les numéros d'articles inconnus sont marqués [À vérifier]. Le montant de l'abattement (Q44) doit être tranché.

## Itération M9 (2026-10-04) — fin de M7 : v4 vérifiée, « les droits d'abord » ; passage à l'exposé

Réponse par procuration au tour de l'agent (décisions 75 et 76, revue des 80 questions : 42 décidées, 26 répondues, 12 ouvertes) :
1. **La formulation du scénario bas est validée** [opus-5.5 as ggim]. Une précision : l'exposé ne doit chiffrer **aucun** rendement de la taxe Zucman.
2. **La règle d'ouverture du socle sur trois ans (D13.6) est validée** pour le dispositif. Pourquoi : on ne perçoit pas une taxe pendant des années sans ouvrir de droits.
3. **m ramené à 2 au plus une fois la cible atteinte** : validé, mais comme une **règle par défaut**. La LFSS peut aller au-delà sur un vote motivé (la justification renforcée de la décision 51), notamment en cas de retournement. Pourquoi : « drastique mais juste ». Le double dividende ne justifie pas à lui seul de dépasser les deux tiers, mais on ne lie pas les mains du législateur.
4. **La moitié « droits » après la cible** : validée (l'indexation sur le seuil de pauvreté et les extensions votées, à défaut la baisse des cotisations). **Exigence** : modéliser l'indexation dans `sim_v4.py`, pour ne pas surestimer le double dividende. L'exposé doit dire honnêtement que la baisse des cotisations sera **modeste et tardive** (environ 0,3 point en 2035) : c'est un bénéfice second, pas une promesse.
5. **Le fonds de réserve à six mois du besoin net** : validé.
6. **Les réponses à Q63 et Q75** : validées pour l'argumentaire. Q63 est fidèle à l'intention (« c'est pas tant pour absorber la vague »).
7. **La décision 76** est gardée : c'est bien une décision de Guillaume.
8. **Passer à M9 : l'exposé des motifs v0.2** (un nouveau fichier, la v0.1 étant conservée). Contraintes :
   - un ton formel ;
   - toutes les corrections de la section F, et les contradictions du fichier 17 levées ;
   - le savoir collectif au centre ;
   - les étudiants et le patrimoine présentés comme des choix ouverts ;
   - pas de mise en avant de l'auteur.

## Itération M8 (2026-10-04) — Guillaume : reprise, sans migration de structure

**Message de Guillaume (et non par procuration).** Il a mis à jour les skills (`maieutics` et `metamaieutics`) et demande de reprendre la boucle. La migration du corpus vers la nouvelle structure en anglais (`corpus/`, `partus/`, `instrumenta/`) a été refusée par le contrôle des permissions. Il choisit l'option 2 : **ne pas migrer la structure** sur cette branche (ce sera fait plus tard, sur `main`), et appliquer seulement les nouvelles conventions à partir de maintenant :
- les marqueurs nominatifs : `[ggim]` pour lui, `[opus-5.5]` pour l'agent, `[opus-5.5 as ggim]` pour les décisions par procuration ;
- le prompt-log avec la plus récente entrée en tête ;
- le « pourquoi » de chaque décision dans le journal.

Les anciens marqueurs [G], [C] et [P] restent en l'état. L'orchestrateur lance un agent neuf pour finir M7.

## Itération M0 (2026-10-02) — lancement

L'orchestrateur lance un agent maieutique neuf. Consignes : lire le skill maieutique, le mandat, le fichier d'intention, l'index, le journal, le glossaire et le fichier 17 ; ne jamais commiter, changer de branche, publier ou envoyer quoi que ce soit ; marquer [P] les décisions par procuration. Premier tour demandé : un état des lieux des obstacles juridiques bloquants (en premier lieu l'article 401 de la directive TVA), avec une proposition de plan de travail et des premières pistes d'architecture.

## Itération M1 (2026-10-02) — réponse aux 11 arbitrages de l'état des lieux

Réponse par procuration à l'ébauche de la note 18 :
1. **La cascade** : accepté [P]. On renonce à toute déduction en chaîne, et l'achat pour revente se fait en suspension sur attestation. Le risque de fraude sur l'attestation doit être traité en M8.
2. **Le redevable** : accepté [P]. Il faut préciser comment le fournisseur distingue un client professionnel d'un particulier (SIREN, numéro de TVA).
3. **Le tarif par classe** : accepté sous condition. **Contestation** : un tarif m × P_k, indexé sur un prix de marché, risque de rendre la taxe « proportionnelle au prix », le 2e critère de l'article 401. L'agent doit vérifier que l'indexation sur un prix moyen constaté n'équivaut pas à une proportionnalité au prix de la transaction, et le démontrer avec la jurisprudence. Les classes doivent rester peu nombreuses et objectives.
4. **Le vote annuel de m entre 1 et 4** : accepté [P] ↺, révision partielle de la décision 26. Vérifier que m ≥ 1 garantit bien l'esprit de « au moins la moitié de la valeur au bien commun ».
5. **Le plafond à 4P** : on le garde comme borne légale [P], mais il faut une analyse explicite du caractère non confiscatoire (jurisprudence du Conseil constitutionnel sur les impositions comportementales et les accises, et le seuil des deux tiers est-il applicable ?).
6. **L'affectation** : la piste (a) est acceptée [P], mais **la recette ne doit pas se perdre dans le budget général** : l'intention, c'est le chômage universel. Traiter le risque du plafonnement des taxes affectées (en prévoir l'exclusion), et comparer avec un CAS et avec une voie « sécurité sociale » (LFSS ou fraction de CSG). Garder la solution la plus robuste.
7. **Le compteur** : accepté [P]. L'obligation porte sur le redevable, et le SDK certifié devient une voie simplifiée. C'est une inflexion des décisions 13 et 28, à marquer ↺.
8. **L'IA locale** : accepté [P]. Un taux réduit défini par l'exécution sur un équipement terminal, temporaire (cohérent avec « ménager ce qui démarre »), et notifié à titre préventif.
9. **L'entraînement hors du champ** : accepté [P], par cohérence avec l'assiette d'usage. Mais l'argument du savoir collectif doit rester central dans l'exposé, et la taxation de l'entraînement peut être mentionnée comme une piste ultérieure.
10. **Le secteur public, les associations et la recherche** : inclus avec l'abattement [P]. Préciser l'effet budgétaire circulaire pour l'État.
11. **Le plan** : validé, avec deux exigences : les 20 questions non traitées et les 10 prioritaires doivent être explicitement fermées dans la note 18, et il faut regrouper si possible pour finir en moins de 20 itérations.

Demande pour M2 : inscrire ces arbitrages au journal (n° 37 et suivants, [P], ↺ si besoin), mettre à jour les notes 04, 08 et 10, et répondre à la contestation 3 et aux vérifications 4 et 5.

## Itération M2 (2026-10-02) — tarif, affectation, plafond

Réponse par procuration au tour M2 (journal n° 37 à 47) :
1. **La condition de la décision 39 est levée** [P] : le tarif m × P_k, trois classes par tranches de prix catalogue, un indice calculé par l'INSEE, et en repli le tarif en € par unité avec sa clause de réduction automatique. Traiter en M8 le contournement aux bornes des tranches (prix catalogue fixé juste sous une borne).
2. **La branche de sécurité sociale est acceptée en principe** [P], avec le cliquet de l'article LO 111-3-14 et une fraction pour l'Unédic. Le double dividende (la baisse des cotisations) vient bien de la décision 30 [G] : c'est cohérent. **Mais il faut vérifier un point** : une prestation de sécurité sociale entre dans le champ du règlement (CE) 883/2004 (exportabilité, totalisation, égalité de traitement des ressortissants de l'Union). Le socle est-il une « prestation de chômage » ou une « prestation spéciale en espèces à caractère non contributif » (annexe X) ? Quelles conséquences sur la condition de résidence et le coût ? Et le transfert du RSA et de l'ASS vers cette branche (article 72-2, compensation aux départements) ? Si ce point fait tomber la voie sécurité sociale, on retombe sur l'établissement public.
3. **m est voté en LFSS** [P], par cohérence avec le point 2.
4. **Une justification renforcée au-delà de m = 2** [P]. Rappeler dans l'exposé que l'ordre de grandeur reste celui du carburant (l'intention de l'auteur).
5. **L'export est « hors du champ, mais déclaré »** [P] : une précision de forme de la décision 30, sans changement d'effet.
6. **La réserve sur la confiscation est notée pour le juriste.** On passe à M3.

**Contestation** (point 2 de M2) : « sans identifiant, le client est traité comme un particulier » ouvre une échappatoire massive, puisque les entreprises n'auraient qu'à utiliser des comptes grand public. Il faut une règle qui ferme la faille. Par exemple : le fournisseur doit demander l'identifiant ; l'usage professionnel est présumé au-delà d'un volume ou en cas d'accès par API ; l'entreprise qui fait un usage professionnel par un compte grand public autoliquide et s'expose à une sanction. Et cela sans taxer les particuliers.

Demande pour M3 : traiter le point 2 (règlement 883/2004, RSA et ASS, loi organique de création de la branche) et la contestation, puis arrêter l'affectation. Continuer la fermeture des questions du fichier 17.

## Itération M3 (2026-10-02) — règlement 883/2004, RSA et ASS, comptes grand public, fonds de réserve

Réponse par procuration au tour M3 (journal n° 48 à 52) :
1. **La règle D7 sur les comptes grand public est validée** [P].
2. **D8 est validé** [P] : un fonds de six mois, l'ordre d'emploi (les droits, le fonds, puis le surplus partagé moitié-moitié) et, en cas de retournement, la priorité aux droits sur la baisse des cotisations. C'est fidèle à l'intention : le chômage universel prime.
3. **Le RSA et l'ASS sont validés** [P], avec l'accompagnement volontaire, cohérent avec la décision 31 [G]. **Exigence nouvelle** : une **garantie de non-régression**. Aucun bénéficiaire actuel du RSA (y compris le RSA majoré des parents isolés, la composition familiale et le cumul avec la prime d'activité) ni de l'ASS ne doit y perdre. Le montrer, avec un mécanisme (différentiel ou maintien des droits acquis), et en tenir compte dans le chiffrage.
4. **La qualification de prestation de chômage, avec un droit au séjour**, et l'annexe X en étape ultérieure : validées [P]. Préciser si la condition de séjour est plus ou moins restrictive que celle du RSA actuel (cinq ans de titre de séjour pour les ressortissants d'un pays tiers). On ne doit pas exclure des personnes aujourd'hui éligibles.
5. **Le reversement de la part « socle » de l'ARE** à la branche est accepté comme principe [P].
6. **Passer à M4.** Rappel : il reste 8 questions ouvertes, et le plan prévoit 14 itérations.

## Itération M4 (2026-10-02) — non-régression, séjour, territorialité, IA locale

Réponse par procuration au tour M4 (journal n° 53 à 57) :
1. **Le mécanisme de non-régression D9 est validé** [P] : la garantie familiale permanente, les droits connexes, les trimestres de retraite, la prime d'activité maintenue et la sauvegarde de cinq ans.
2. **La condition de séjour D10 est validée** [P] : la réunion des conditions du RSA et de la voie de la directive 2011/98. La suppression de la condition de cinq ans reste le repli, à présenter au rapport comme un choix politique ouvert.
3. **La période de lancement Q48 est validée** [P] : 0,25 × le tarif pendant trois ans, une extinction à cinq ans au plus tard, un critère de maturité à 20 % du volume ou 50 % des entreprises. C'est cohérent avec « ménager ce qui démarre ».
4. **Le volume forfaitaire et la table de conversion sont validés** [P], avec une condition : le redevable doit pouvoir opter pour la **déclaration au réel** (avec le SDK certifié) quand le forfait le pénalise. Le volume compté reste la mesure juste.
5. **La notification par prudence est validée** [P], avec le statu quo de trois mois intégré au calendrier.
6. **Q33** : d'accord pour retirer « les exportateurs ne sont pas pénalisés ». La franchise vaut mieux qu'une promesse fausse.
7. **Passer à M5** (l'assiette technique et le contrôle).

## Itération M5 (2026-10-02) — le champ, la mesure, le contrôle

Réponse par procuration au tour M5 (journal n° 58 à 63) :
1. **Le champ limité aux modèles d'IA à usage général** (D12.1) : accepté en principe, mais **contesté sur un point**. L'exemple fondateur de l'intention est l'**illustrateur** : une image générée à partir d'un prompt de 200 octets. Un générateur d'images, de voix, de musique ou de code spécialisé n'est pas toujours un modèle « à usage général » au sens de l'article 3, point 63, du règlement sur l'IA, et il pourrait échapper au champ. Or il remplace du travail humain et il est bâti sur le savoir collectif. Il faut un critère qui inclut **toute IA générative entraînée sur des données à grande échelle**, par exemple les modèles à usage général **plus** les systèmes qui génèrent des contenus de synthèse (article 50 du même règlement), tout en excluant l'IA spécialisée non générative (le scoring, l'OCR, le débruitage). À vérifier dans le texte.
2. **La mesure et les coefficients** : acceptés [P], avec des valeurs indicatives à caler en M7. **Une réserve à documenter** : taxer les données lues, même à 0,25, frappe l'analyse documentaire. C'est cohérent (l'analyse documentaire est aussi du travail humain remplacé), mais il faut le justifier par le principe du travail remplacé, pas seulement par la grille de prix.
3. **La transparence pour les intermédiaires et la taxation des données synthétiques** : acceptées [P].
4. **Le contrôle** (D12.5) : accepté [P].
5. **Le registre des revendeurs agréés et les quatre parades aux bornes** : acceptés [P].
6. **Passer à M6** (le chômage universel), en y ajoutant le point 1.

## Itération M6 (2026-10-02) — le chômage universel ; relève de l'agent

Réponse par procuration au tour M6 (journal n° 64 à 68) :
1. **Le champ D13.1 est validé** [P], avec la traduction et la transcription incluses expressément. Les traducteurs et les sous-titreurs sont l'exemple même du travail remplacé.
2. **Les étudiants en formation initiale : la question est LAISSÉE OUVERTE.** Elle touche l'intention (le revenu digne de « celles et ceux qui n'ont pas d'emploi ») et une décision [G] (la 31, « ouvert dès 18 ans »). Elle est structurante (environ 40 Md€). On contourne : le chiffrage de base les exclut (les bourses sont maintenues), à titre d'**hypothèse de chiffrage**, et une variante chiffrée les inclut. Les livrables présentent la question comme un choix ouvert, que Guillaume tranchera.
3. **La réduction du socle pour les revenus élevés du patrimoine : la question est LAISSÉE OUVERTE.** Elle introduit une forme de condition de ressources dans un dispositif voulu universel, ce qui touche l'intention. Chiffrage de base : sans réduction, avec une variante. À signaler.
4. **La sortie progressive de 12 mois, puis la prime d'activité** : validée [P].
5. **Les phases d'ouverture, avec le montant du socle voté en LFSS** : validées [P]. Les droits ne précèdent jamais les recettes.
6. **Le recentrage de l'Unédic** : assumé [P], avec une mention explicite du rôle maintenu des partenaires sociaux et de la concertation prévue au mandat.
7. **Relève** : sur la recommandation de l'agent, dont le contexte est saturé, un **agent neuf** reprend à partir de M7, avec la section F de la note 18.

## Itération M7 (partielle, 2026-10-02/03) — interrompue par Guillaume

L'agent de relève avait intégré les réponses de M6 (journal n° 69 à 74), écrit `outils/sim_v4.py` et la note 19 (simulation v4). Guillaume l'a arrêté pendant la mise à jour de la note 18. Le travail est commité en l'état. Il reste à vérifier et à finir.
