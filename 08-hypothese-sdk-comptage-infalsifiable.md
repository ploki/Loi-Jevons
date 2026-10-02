# Hypothèse : un SDK open source pour faire remonter les compteurs au Trésor public

- **Statut** : brouillon
- **Créé le** : 2026-10-02
- **Dernière mise à jour** : 2026-10-02 (session metamaieutique, M4)


## En vigueur

> Mis à jour en M2 de la session metamaieutique (décisions [P] 43 et 44). La faisabilité juridique est dans la note 18 (O6 et O9).

- **↺ L'obligation de comptage pèse sur le redevable** (décision 43 [P]). Il doit tenir une **comptabilité-matière** des volumes, exacte et contrôlable. **Aucune obligation n'est imposée aux éditeurs** de logiciels.
- **Le SDK libre et certifié devient une voie simplifiée** : l'utiliser vaut **présomption de bonne foi**, comme les logiciels de caisse certifiés. L'entreprise peut aussi justifier ses volumes autrement (les relevés des fournisseurs, ses propres journaux).
- **Raisons** : imposer un compteur aux éditeurs serait une règle technique à notifier (directive (UE) 2015/1535), une restriction possible à la libre prestation de services, et une source de conflit avec le règlement européen sur l'IA [À vérifier]. Le texte sera **notifié** de toute façon.
- **Données transmises** : uniquement des **volumes agrégés**, jamais le contenu des requêtes (RGPD, secret des affaires).
- **Abattement** : un par entreprise, appliqué au niveau du **groupe** (anti-fractionnement, à préciser en M8). Pas de forfait ni de franchise (décision 30 [G]).
- **IA locale et embarquée** (décision 44 [P]) : un **taux réduit** pour l'inférence **exécutée sur un équipement terminal** (poste de travail, appareil embarqué), et non sur un serveur. Il est **temporaire**, avec une clause de rendez-vous, et **notifié préventivement** à la Commission (aides d'État).
- **IA embarquée des particuliers** : hors du champ.
- **Contrôle** : une falsification est **détectable, pas impossible**. On recoupe avec la facturation électronique, les heures de GPU louées et l'électricité consommée.
- **Questions ouvertes** (fichier 17) : les sanctions, les moyens de l'administration, le fractionnement, le coût de conformité (M8) ; la durée de la période de lancement et le niveau du taux réduit (M6).
- **M4 [C]** (note 18, D11) : l'**équipement terminal** est défini (sous la maîtrise physique de l'utilisateur, non exploité pour servir des tiers) ; un serveur en colocation n'en est pas un. Le taux réduit est proposé à 0,25 × le tarif plein pendant trois ans, avec une extinction au plus tard à cinq ans et un critère objectif de maturité. L'IA embarquée est taxée sur un volume forfaitaire par catégorie d'appareil. Le SDK libre est piloté par la DGFiP, avec un référentiel de type NF525. Le projet est notifié par prudence (directive 2015/1535 et aides d'État).

---

## Historique du raisonnement

> Les sections suivantes retracent le raisonnement. En cas de divergence, la section « En vigueur » prévaut.

### Session metamaieutique, M4 (2026-10-02)

- **[C]** Les questions 37, 38 et 45 à 48 sont traitées en note 18, D11.

### Session metamaieutique, M2 (2026-10-02) : décisions par procuration

- **[P] ↺ Décision 43** : l'obligation porte sur le redevable, et le SDK devient une voie simplifiée. Elle revient sur les décisions **13** (le SDK comme dispositif de collecte pour le Trésor) et **28** (« un portable d'entreprise installe le SDK »). **L'intention est préservée** : on compte partout où l'IA sert un usage professionnel, mais par une obligation de résultat sur l'entreprise, et non par un logiciel imposé.
- **[P] Décision 44** : le taux réduit est défini par l'exécution sur un équipement terminal. Le « voire nul » de la décision 30 n'est pas retenu à ce stade : le niveau sera fixé en M6.

### En bref

> Unité retenue : l'**octet-équivalent** (octet × coefficient par type de contenu, fichier 04). Quand ce fichier parle de « token », il faut lire « unité taxable ».

Un algorithme, diffusé sous forme de SDK open source, permet au Trésor public de collecter les compteurs (tokens ou données) de façon infalsifiable. Il offre une voie simple aux acteurs de bonne foi et s'accompagne de moyens de contrôle.

### Ce qui a été posé

- **[G]** Développer un algorithme et un SDK open source qui permettent au Trésor public de collecter les compteurs de façon infalsifiable.
- **[G]** Il s'adresse aux acteurs de bonne foi et s'accompagne de moyens de contrôle.

### Qui doit installer le SDK

- **[G] Décision (point 4 de la relecture du corpus)** :
  - **Pas de régime forfaitaire, pas de franchise.** Le SDK est installé **partout** où l'IA sert un usage professionnel, y compris sur les portables. La seule exonération est celle des **particuliers**.
  - **Un abattement par entreprise** : un petit volume annuel n'est pas taxé. L'entreprise déclare tout son volume, mais ne paie que sur ce qui dépasse l'abattement. L'État garde ainsi une vue complète des usages, et les très petits usages ne coûtent rien. Le montant de l'abattement reste à fixer.
  - Les PME sont aussi protégées par le **taux réduit sur l'IA locale et embarquée** pendant la période de lancement, et par la **simplicité** : un SDK intégré directement dans les logiciels qui font tourner les modèles, et une déclaration annuelle pour les très petites entreprises, comme pour la TVA.
- Le tableau des régimes ci-dessous (réel, forfaitaire, franchise) est **remplacé** par cette décision. Il est conservé comme trace du raisonnement.

- **[G]** L'IA qui tourne sur les serveurs d'une entreprise **est soumise à la taxe**. Il faut définir **à partir de quand une entreprise est obligée d'installer le SDK des impôts**.
- **[C] Le principe** : toute entité qui fait tourner, pour un **usage professionnel**, un modèle d'IA sur du matériel qu'elle contrôle (possédé, ou loué dans le cloud) est un **exploitant de système d'inférence**, et donc redevable de la taxe. La définition du « modèle » ou du « système d'IA » pourrait reprendre celle de l'AI Act (article 3). **[À vérifier]**
- **[C] Deux régimes, sur le modèle de la TVA ou de l'impôt sur le revenu (micro et réel)** :

| Régime | Qui | Calcul de la taxe |
|---|---|---|
| **Réel**, SDK obligatoire | Au-delà d'un seuil de capacité installée ou de volume | Volume compté par le SDK × montant par unité (indice trimestriel, fichier 10) |
| **Forfaitaire**, sans SDK | En dessous du seuil | Un **forfait selon la capacité installée** (par exemple par GPU de classe centre de données, ou par kW de puissance de calcul) |
| **Franchise** | Très petites capacités : poste de développeur, essais | Exonération |

- **[G] Décision** : **un ordinateur portable d'entreprise qui fait tourner un modèle installe le SDK.** Il n'y a donc **pas de franchise pour les postes de travail professionnels**. Le régime forfaitaire et la franchise du tableau ci-dessus sont à revoir (voir les questions ouvertes).
- **[C] Ce que cela implique** :
  - **Le SDK doit être léger** et **déployable automatiquement sur tout le parc**, avec les outils de gestion de flotte (MDM) déjà utilisés par les DSI.
  - **Le meilleur levier : intégrer le SDK aux logiciels qui font tourner les modèles** (Ollama, llama.cpp, vLLM, ONNX Runtime) et aux fonctions d'IA des systèmes d'exploitation (NPU de Windows et de macOS). Une obligation de certification pèserait sur les **éditeurs**, comme pour les logiciels de caisse NF525, plutôt que sur chaque entreprise.
  - **Le cas du logiciel libre** : n'importe qui peut modifier un logiciel open source pour en retirer le compteur. La logique reste celle de la bonne foi, avec des contrôles : utiliser une version sans compteur sur un poste professionnel serait une infraction.
  - **Les fonctions d'IA locales des logiciels de bureautique** (un assistant qui tourne sur le NPU du portable) entrent dans le champ de la taxe.
- ~~Question ouverte : le régime forfaitaire a-t-il encore une raison d'être ?~~ Réglé : il est supprimé (voir la décision ci-dessus).
- ~~**[C] L'incitation au régime réel**~~ (sans objet depuis la suppression du forfait) : une entreprise peut **choisir de passer au régime réel**, en installant le SDK, si son usage réel est inférieur au forfait. Celle qui utilise peu ses GPU a donc intérêt à compter honnêtement.
- **[C] Ce qui déclenche l'obligation**, et ce que le fisc peut vérifier :
  - **le matériel** : les achats d'accélérateurs d'IA apparaissent sur les factures électroniques, que le fisc voit déjà à partir de 2026 ;
  - **la location de GPU dans le cloud** : le fournisseur déclare les heures de GPU louées par client, ce qui permet de recouper les déclarations sans que le fournisseur ne collecte la taxe ;
  - **la consommation électrique** des salles de serveurs.
- **[C] Le prix de référence** : l'inférence sur ses propres serveurs n'a pas de prix de marché. On applique l'**indice du prix moyen** issu des déclarations.
### L'IA embarquée

- **[G] Décision** : l'IA embarquée est **exonérée pour les particuliers**.
- **[G] Pour les appareils professionnels, l'impact reste à étudier.**
  - Une taxe ou un forfait sur ces appareils risque de **freiner l'adoption de l'IA embarquée**, qui en est encore à ses débuts. C'est l'inverse de l'IA dans le cloud, déjà massivement adoptée (fichier 11).
  - Plus largement, une taxe sur les appareils professionnels risque de **freiner l'adoption d'une IA plus locale, mieux adaptée au besoin**.
- **[C] Une tension à résoudre** avec la décision sur les portables : un portable qui fait tourner un modèle, c'est aussi de l'IA locale.
- **[G] Validé : compter partout, ne taxer que ce qui est mûr.**
  - Le **SDK est installé partout**, y compris sur les portables et les appareils professionnels : on **mesure**.
  - Le **taux est réduit, voire nul, pour l'inférence locale et embarquée** pendant une période de lancement, par exemple 3 à 5 ans, avec une **clause de rendez-vous**.
  - Le taux plein s'applique quand les volumes mesurés montrent que l'usage est arrivé à maturité.
  - **Avantage** : l'État dispose dès le départ des données d'usage, sans freiner l'IA locale. On peut aussi y voir une préférence assumée pour une IA **frugale, proche du besoin et souveraine**, par rapport à la grande inférence dans le cloud.

### Pistes techniques

- **[C] Où placer le compteur** : dans le serveur d'inférence ou dans la passerelle d'API. Il compte les données lues et générées, dans un format de référence (voir le fichier 04).
- **[C] Comment rendre la falsification visible** :
  - un journal où l'on ne peut qu'ajouter des entrées, chacune liée à la précédente par une empreinte cryptographique (chaîne de hachage, arbre de Merkle) ;
  - des relevés signés et horodatés ;
  - si possible, une signature produite par le matériel lui-même (puce TPM, enclave sécurisée), qui atteste que le compteur n'a pas été modifié.
- **[C] Comment déclarer** : un relevé périodique signé, transmis à la DGFiP en même temps que la déclaration fiscale.
- **[C] Limite honnête** : sur une machine contrôlée par le contribuable, aucun logiciel n'est strictement infalsifiable. On obtient une falsification **détectable**, pas impossible. D'où la logique de la bonne foi accompagnée de contrôles.

### Moyens de contrôle

- **[C] Le recoupement** :
  - les volumes déclarés par les fournisseurs d'API, comparés à ceux déclarés par leurs clients, comme le rapprochement des factures en TVA ;
  - la consommation électrique des GPU comparée aux volumes déclarés : une machine qui consomme beaucoup mais déclare peu attire l'attention.
- **[C] Les audits** : des contrôles aléatoires, et la publication du code pour que tout le monde puisse vérifier le compteur.

### Précédents français à citer **[À vérifier]**

- **Les logiciels de caisse certifiés** (loi anti-fraude à la TVA, 2018, norme NF525). Ils doivent garantir quatre propriétés : inaltérabilité, sécurisation, conservation et archivage des données.
- **La facturation électronique obligatoire**, déployée à partir de septembre 2026, avec des plateformes agréées qui transmettent les données au fisc.
- **D'autres compteurs certifiés** : le chronotachygraphe des poids lourds, le compteur électrique Linky.

### Liens

- [04-hypothese-modalites-assiette-et-collecte.md](04-hypothese-modalites-assiette-et-collecte.md)
