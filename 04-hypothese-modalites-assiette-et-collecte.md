# Hypothèse : modalités (assiette et collecte de la taxe)

- **Statut** : en discussion
- **Créé le** : 2026-10-01
- **Dernière mise à jour** : 2026-10-02 (session metamaieutique, M2)


## En vigueur

> Mis à jour en M2 de la session metamaieutique (décisions [P] 37, 38, 45 et 46). La faisabilité juridique est dans la note 18.

- **Nature** : une imposition de toutes natures du type **accise sur un service**, perçue **une seule fois**, au stade de l'**utilisation professionnelle finale** ; **aucune déduction en chaîne** (décision 37 [P]).
- **Champ** : l'**usage professionnel**, c'est-à-dire l'utilisation par une personne qui agit dans le cadre d'une activité économique ou d'une mission de service public. Les **particuliers sont hors du champ**. Le **secteur public, les associations et la recherche sont dans le champ**, avec l'abattement (décision 46 [P]).
- **Hors du champ** : l'**entraînement et l'affinage** des modèles (décision 45 [P]). C'est une piste ultérieure.
- **Unité** : l'**octet-équivalent** (décision 9 [G]), l'octet mesuré dans un format de référence et multiplié par un **coefficient par type de contenu**. Les coefficients sont **fixés par la loi** (ils relèvent de l'assiette, article 34).
- **Tarif** : par **classe de modèles** (note 10).
- **Redevable** (décision 38 [P]) :
  - le **fournisseur enregistré** en France, établi ou non, collecte la taxe auprès de ses clients professionnels ;
  - **à défaut**, le client professionnel **autoliquide** ;
  - l'**inférence pour usage propre** (sur ses serveurs ou des capacités louées) est déclarée par l'entreprise.
- **Identification du client professionnel** : le **SIREN** ou le **numéro de TVA intracommunautaire** (vérifié par VIES), ou un identifiant fiscal équivalent pour un client étranger. Un client sans identifiant est traité comme un particulier. Un accès par API, ou un volume au-delà d'un seuil, fait présumer l'usage professionnel.
- **Revente** : l'achat en vue de la revente se fait **en suspension**, sur attestation (décision 37 [P]). Il n'y a donc pas de cascade.
- **Territorialité** : le critère est l'**établissement du client** professionnel. L'export vers un client établi à l'étranger est **déclaré** et non taxé (décision 30 [G]) ; la note 18 propose de le qualifier juridiquement de « hors du champ » [C].
- **Le tarif douanier** n'est qu'une boutade, réservée à la campagne.
- **Questions ouvertes** (fichier 17) : le format de référence et l'encodage du texte (Q14), le contexte relu et le cache (Q15), le raisonnement interne et les appels d'outils (Q16), les fournisseurs étrangers (Q32), à traiter en M5 et M7.

---

## Historique du raisonnement

> Les sections suivantes retracent le raisonnement. En cas de divergence, la section « En vigueur » prévaut.

### Session metamaieutique, M2 (2026-10-02) : décisions par procuration

- **[P] Décision 37** : pas de déduction en chaîne, la revente se fait en suspension. Raison : la déduction est la 4ᵉ caractéristique essentielle de la TVA (article 401 de la directive, note 18).
- **[P] Décision 38** : le fournisseur enregistré collecte ; à défaut, le client autoliquide. Ce modèle s'inspire de l'accise sur l'électricité, où le fournisseur collecte auprès du consommateur final. Il réduit le nombre de redevables et sécurise le recouvrement.
- **[P] Décision 45** : l'entraînement est hors du champ, par cohérence avec une assiette d'usage.
- **[P] Décision 46** : le secteur public, les associations et la recherche sont dans le champ. Exclure de grands utilisateurs affaiblirait la cohérence du critère, au vu de la décision 2009-599 DC sur la contribution carbone (note 18).

### En bref

Unité : l'octet, avec un coefficient par type de contenu. On taxe quatre flux de tokens : la génération, la lecture, l'import et l'export. L'entreprise comptabilise les tokens consommés sur place et les déclare au fisc. Seul l'usage professionnel est taxé : **les particuliers sont exonérés** (hors taxe). La taxe peut servir de levier pour l'industrie française de l'IA. Le schéma ressemble beaucoup à la TVA et aux accises.

### Ce qui a été posé

- **[G]** L'assiette : les tokens **générés, lus, importés et exportés**.
- **[G]** Une entreprise qui fait tourner une IA chez elle enregistre en comptabilité les tokens lus et générés sur place, puis les reporte dans sa déclaration fiscale.
- **[G]** Les appels d'API sont **hors taxe pour les particuliers** : la taxe ne vise que l'usage professionnel. (Correction de Guillaume : Claude avait d'abord compris l'inverse.)
- **[G]** La taxe peut devenir un levier tarifaire pour l'industrie française de l'IA.

### Analogies et points à creuser

- **[C] Le modèle de la TVA**
  - Contrairement à la TVA, la taxe ne pèse pas sur le consommateur final particulier. Elle vise l'usage productif, c'est-à-dire là où la substitution du travail a lieu.
  - Cela répond à l'objection selon laquelle le token mesure mal le travail remplacé : le lycéen qui révise ne paie rien.
  - L'import de services se règle déjà par **autoliquidation** : c'est le client professionnel qui déclare la taxe.
  - Les exportations sont exonérées.
  - Avantage : l'infrastructure fiscale existe déjà et les entreprises connaissent le mécanisme.
- **[C] Le modèle des accises**
  - Une IA qui tourne sur place ressemble à une production soumise à accise, comme l'alcool ou l'énergie : on déclare un volume produit.
  - Il faut un **comptage certifiable**, sur le modèle d'un compteur ou d'un entrepositaire agréé.
- **[C] Une unité commune**
  - Un « token » n'a pas la même taille d'un modèle à l'autre, parce que chaque modèle découpe le texte à sa façon (tokenizer).
  - Il faut donc une unité normalisée, par exemple un nombre de caractères ou d'octets traités, ou un tokenizer de référence défini par le fisc.
- **[C] Lecture et génération**
  - Environ 90 % des tokens sont lus et 10 % générés (voir le fichier 03).
  - Deux taux distincts permettent de régler le poids de chacun.
- **[C] Le levier pour l'industrie française : point juridique sensible**
  - En principe de destination (taxer ce qui est consommé en France, quelle que soit l'origine, comme la TVA), la taxe est neutre et défendable. L'avantage français vient alors de l'**exonération à l'export**.
  - Taxer davantage les tokens étrangers que les tokens français serait contraire au droit de l'UE (marché unique, compétence douanière exclusive de l'UE) et aux règles de l'OMC. **[À vérifier]**
  - La taxe GAFA de 2019 en est le précédent, avec la menace de représailles américaines. **[À vérifier]**

### Unité de mesure : la quantité de données

- **[G] Décision (point 2 de la relecture du corpus)** : l'unité est l'**octet**, mesuré dans un format de référence, avec un **coefficient par type de contenu** (texte, image, audio, vidéo, code…).
- **[C] Interprétation retenue** : chaque coefficient convertit les octets d'un type de contenu en une unité commune, l'« octet-équivalent ». Il est calibré sur le prix moyen de ce type de contenu, de sorte que le plancher 50/50 et le plafond de 4 fois le prix moyen s'appliquent de façon cohérente à chaque type. Les coefficients sont révisés avec l'indice trimestriel (fichier 10).
  - Au sein d'un même type de contenu, plus on génère, plus on paie, ce qui reste proportionnel au travail remplacé.
  - Si l'on voulait une pondération « équivalent-travail », par exemple surtaxer les images, ce coefficient serait le levier. Ce n'est pas retenu à ce stade.
- Les sections ci-dessous gardent la trace du raisonnement.

- **[G]** Piste : mesurer la quantité de données traitées plutôt que le nombre de tokens.
- **[C]** Avantages : on ne dépend plus du découpage propre à chaque modèle, on peut compter côté réseau, et c'est auditable.
- **[G]** Argument de justice sociale : le volume de données est **à peu près proportionnel au travail humain remplacé**. Exemple : une image générée au bureau à partir d'un prompt de 200 octets représente environ 4 heures de travail pour un illustrateur.
- **[C]** Ce qui ressemblait à une limite devient donc un argument : le poids élevé des images et des vidéos reflète le travail substitué, et le token l'aurait sous-estimé.
- **[C]** Là où la proportionnalité casse, et comment la corriger :
  - **la compression et le format** : un même visuel pèse jusqu'à 10 fois plus en PNG qu'en JPEG, et une vidéo pèse beaucoup plus en 4K qu'en 720p pour le même travail. Il faut mesurer dans un **format de référence** (un codec et une résolution normalisés) ;
  - **le texte** : 1 Ko de code peut représenter des heures de travail, 1 Ko d'e-mail quelques minutes. L'écart est acceptable pour une taxe simple ;
  - **l'entrée et la sortie** : le prompt de 200 octets ne représente presque rien, c'est la sortie qui porte le travail remplacé. Cela plaide pour un **taux plus élevé sur les données générées**. En revanche, lire un document de 300 pages, c'est aussi des heures de lecture humaine, donc l'entrée reste taxée.
- **[C]** Limite qui demeure :
  - le raisonnement interne des modèles, qui génère des tokens jamais transmis, échappe à la mesure.

### Frontière entre usage pro et perso

- **[G]** C'est le miroir de la fraude classique à la TVA : ici, ce sont des professionnels qui achèteraient au tarif des particuliers. L'accès serait plus facile, mais pourrait être soumis à contrôle.
- **[C]** Un outil simple : au-delà d'un seuil de volume, un compte de particulier serait présumé professionnel. L'accès par API serait présumé professionnel.

### Les quatre flux et le lieu d'imposition (point 5 de la relecture du corpus)

- **[G] Décision** : l'**export est déclaré, avec un taux nul**. Les quatre flux (génération, lecture, import, export) sont tous comptés par le SDK.
- **[G] Définition de l'export** : l'inférence a lieu **sur des GPU en France**, pour un **client établi à l'étranger**.
- **[C]** Le critère déterminant est le **lieu d'établissement du client professionnel**, comme en TVA pour les services entre entreprises. L'endroit où se trouve le GPU ne suffit pas.

| Où sont les GPU | Où est le client | Qualification | Taux |
|---|---|---|---|
| France | France | Consommation en France | Taux plein (règle du fichier 10) |
| Étranger | France | **Import**, autoliquidé par le client | Taux plein |
| France | Étranger | **Export** | **0 %**, déclaré |
| Étranger | Étranger | Hors du champ de la taxe | — |

- **[C] Garde-fous contre les montages** :
  - la preuve que le client est établi à l'étranger se fait par son numéro de TVA ou un équivalent, comme en TVA ;
  - une **clause anti-abus** : si un intermédiaire étranger revend en réalité à un utilisateur professionnel établi en France, l'opération est requalifiée en import taxable. **[À vérifier : la règle de « l'utilisation effective » existe en TVA]**


- **[G]** On garde l'aspect tarif douanier, mais **comme une boutade**, réservée à la campagne de promotion, pas comme une proposition sérieuse. La proposition sérieuse reste la taxation au lieu de consommation, avec exonération à l'export.

### Questions ouvertes

- ~~Quel est le taux sur l'export ?~~ Réglé : export déclaré, taux nul.
- ~~Comment traiter les particuliers qui font tourner des modèles en local ?~~ Réglé : ils sont exonérés (fichier 08).

### Liens

- [03-cadrage-simulation-tokens-france-vs-masse-salariale.md](03-cadrage-simulation-tokens-france-vs-masse-salariale.md)
