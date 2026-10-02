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

---

# Session metamaieutique « Rendre la Loi Jevons réalisable » (branche `metamaieutique/loi-jevons-faisabilite-2026-10-02`)

> À partir d'ici, les messages consignés sont ceux de l'orchestrateur (Claude), qui parle **par procuration** au nom de Guillaume, d'après `mandat.md` et `intention-de-l-auteur.md`. Les décisions qui en découlent sont marquées **[P]**.

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
