# Hypothèse : un SDK open source pour faire remonter les compteurs au Trésor public

- **Statut** : brouillon
- **Créé le** : 2026-10-02
- **Dernière mise à jour** : 2026-10-02

## En bref

> Unité retenue : l'**octet-équivalent** (octet × coefficient par type de contenu, fichier 04). Quand ce fichier parle de « token », il faut lire « unité taxable ».

Un algorithme, diffusé sous forme de SDK open source, permet au Trésor public de collecter les compteurs (tokens ou données) de façon infalsifiable. Il offre une voie simple aux acteurs de bonne foi et s'accompagne de moyens de contrôle.

## Ce qui a été posé

- **[G]** Développer un algorithme et un SDK open source qui permettent au Trésor public de collecter les compteurs de façon infalsifiable.
- **[G]** Il s'adresse aux acteurs de bonne foi et s'accompagne de moyens de contrôle.

## Qui doit installer le SDK

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
## L'IA embarquée

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

## Pistes techniques

- **[C] Où placer le compteur** : dans le serveur d'inférence ou dans la passerelle d'API. Il compte les données lues et générées, dans un format de référence (voir le fichier 04).
- **[C] Comment rendre la falsification visible** :
  - un journal où l'on ne peut qu'ajouter des entrées, chacune liée à la précédente par une empreinte cryptographique (chaîne de hachage, arbre de Merkle) ;
  - des relevés signés et horodatés ;
  - si possible, une signature produite par le matériel lui-même (puce TPM, enclave sécurisée), qui atteste que le compteur n'a pas été modifié.
- **[C] Comment déclarer** : un relevé périodique signé, transmis à la DGFiP en même temps que la déclaration fiscale.
- **[C] Limite honnête** : sur une machine contrôlée par le contribuable, aucun logiciel n'est strictement infalsifiable. On obtient une falsification **détectable**, pas impossible. D'où la logique de la bonne foi accompagnée de contrôles.

## Moyens de contrôle

- **[C] Le recoupement** :
  - les volumes déclarés par les fournisseurs d'API, comparés à ceux déclarés par leurs clients, comme le rapprochement des factures en TVA ;
  - la consommation électrique des GPU comparée aux volumes déclarés : une machine qui consomme beaucoup mais déclare peu attire l'attention.
- **[C] Les audits** : des contrôles aléatoires, et la publication du code pour que tout le monde puisse vérifier le compteur.

## Précédents français à citer **[À vérifier]**

- **Les logiciels de caisse certifiés** (loi anti-fraude à la TVA, 2018, norme NF525). Ils doivent garantir quatre propriétés : inaltérabilité, sécurisation, conservation et archivage des données.
- **La facturation électronique obligatoire**, déployée à partir de septembre 2026, avec des plateformes agréées qui transmettent les données au fisc.
- **D'autres compteurs certifiés** : le chronotachygraphe des poids lourds, le compteur électrique Linky.

## Liens

- [04-hypothese-modalites-assiette-et-collecte.md](04-hypothese-modalites-assiette-et-collecte.md)
