# Simulation : tokens consommés en France en 2026 face à la masse salariale perdue

- **Statut** : brouillon
- **Créé le** : 2026-10-01
- **Dernière mise à jour** : 2026-10-02


## En vigueur

- **Rôle** : une illustration pour l'étude d'impact. Pour les **recettes, les fichiers 13 et 19 font foi**.
- **Ordres de grandeur toujours utiles** [À vérifier] :
  - environ 1 × 10¹⁷ tokens par an dans le monde en 2026 ;
  - environ 2,5 × 10¹⁵ pour la France (fourchette de 1,5 à 4 %), dont environ 90 % de données lues ;
  - Atos et Capgemini : environ 2 495 postes, soit environ 87 M€ par an.
- Le taux de « 0,035 € par million de tokens » est **obsolète**, puisque la règle de taux a changé (fichier 10).

---

## Historique du raisonnement

> Les sections suivantes retracent le raisonnement. En cas de divergence, la section « En vigueur » prévaut.

### En bref

Destination : l'étude d'impact du projet de loi. C'était au départ une annexe de l'article, demandée par Guillaume [G]. Elle est complétée par la simulation v2 (fichier 13). Environ 2,5 millions de milliards de tokens consommés en France en 2026, face à environ 87 M€ de masse salariale perdue chez Atos et Capgemini. Une taxe d'environ **0,035 € par million de tokens** suffirait à compenser une année de cette masse salariale. C'est de l'ordre de quelques % du prix d'un token.

### 1. Volume mondial

- **[S]** Environ 360 000 milliards de tokens par jour dans le monde en juillet 2026, d'après une triangulation de tokensperday.com. Le plancher, calculé uniquement sur les chiffres publiés par les fournisseurs, est d'environ 300 000 milliards par jour.
- **[S]** Google traite 3,2 millions de milliards de tokens par mois (Google I/O, mai 2026), soit 7 fois plus en un an.
- **[S]** L'API d'OpenAI traite plus de 15 milliards de tokens par minute (mars 2026), contre 6 milliards en octobre 2025.
- **[C]** Comme le volume croît fortement en cours d'année, je retiens une moyenne d'environ 275 000 milliards par jour sur 2026, soit **environ 1 × 10¹⁷ tokens par an** dans le monde.

### 2. La part de la France

Aucune source ne publie de volume de tokens par pays. On utilise donc des indicateurs indirects :

- **[S]** La France compte environ 18 millions d'utilisateurs de ChatGPT, sur plus de 900 millions d'utilisateurs hebdomadaires dans le monde, soit environ 2 %.
- **[S]** Sur OpenRouter, l'Europe représente 21 % des tokens et l'Allemagne 7,5 %. La France n'apparaît pas dans le top 10.
- **[S]** La France est classée 4ᵉ ou 5ᵉ mondiale pour l'adoption de l'IA générative, avec environ 48 % des 15-64 ans utilisateurs.
- **[C]** J'en déduis une fourchette de 1,5 % à 4 %, avec une valeur centrale de **2,5 %**.

| Hypothèse | Part de la France | Tokens par an en France |
|---|---|---|
| Basse | 1,5 % | 1,5 × 10¹⁵ |
| **Centrale** | **2,5 %** | **2,5 × 10¹⁵** |
| Haute | 4 % | 4,0 × 10¹⁵ |

**Tokens lus et générés.** [S] Sur OpenRouter, une requête moyenne compte environ 6 000 tokens en entrée pour 400 tokens en sortie. [C] On peut donc compter environ **90 % de tokens lus et 10 % de tokens générés**.

### 3. Masse salariale perdue

| Entreprise | Postes supprimés | Source |
|---|---|---|
| Capgemini France | Jusqu'à 2 400, par départs volontaires (rupture conventionnelle collective validée en 2026, 7 % de 35 000 salariés). Motif invoqué : l'IA | [S] |
| Atos France | 95 au final (135 annoncés), en définitive uniquement sur volontariat | [S] |
| **Total** | **≈ 2 495** | |

- Au salaire moyen de 35 000 € retenu par [G], cela donne **≈ 87 M€ par an**.
- **[C]** Avec les charges patronales (environ × 1,45), on arrive à environ 127 M€. Il faut aussi noter que 35 000 € est probablement bas pour des ingénieurs ESN. **[À vérifier]**

### 4. Le taux de taxe nécessaire

Ce que doit rapporter la taxe : 87 M€, soit une année de masse salariale.

| Hypothèse | Taxe sur tous les tokens | Taxe sur les tokens générés seulement |
|---|---|---|
| Basse (1,5 %) | 0,058 € par million de tokens | 0,58 € par million |
| **Centrale (2,5 %)** | **0,035 € par million de tokens** | **0,35 € par million** |
| Haute (4 %) | 0,022 € par million de tokens | 0,22 € par million |

**[C]** Pour comparer, les prix publics vont d'environ 0,1 $ à plus de 15 $ par million de tokens selon le modèle. Le taux nécessaire représente donc **quelques % du prix**, ou moins.

### Limites

- Le lien de causalité avec l'IA n'est pas établi. C'est le motif invoqué par Capgemini. Chez Atos, il s'agit d'une restructuration des fonctions support.
- Ces suppressions passent par des départs volontaires, sans licenciements secs.
- Deux entreprises ne représentent pas toute l'économie. C'est un échantillon d'illustration, pas une mesure des dégâts.
- Le volume de tokens par pays n'est publié nulle part : c'est la principale incertitude.
- L'effet Jevons joue sur l'assiette : si le volume est multiplié par environ 7 par an, un taux fixe rapporte de plus en plus. **[C]**

### Sources

- tokensperday.com : https://tokensperday.com/
- Google I/O 2026 : https://www.shacknews.com/article/149205/google-3-2-quadrillion-monthly-ai-tokens
- OpenAI, 15 milliards de tokens par minute : https://aidailypost.com/news/openai-api-token-usage-rises-from-6-bn-15-bn-per-minute-straining
- OpenRouter, State of AI : https://openrouter.ai/state-of-ai
- Adoption en France : https://siecledigital.fr/2026/05/11/la-france-devient-le-5e-pays-le-plus-avance-au-monde-dans-ladoption-de-lia-generative/
- Capgemini : https://www.lemondeinformatique.fr/actualites/lire-capgemini-pret-a-supprimer-jusqu-a-2-400-postes-99093.html et https://france3-regions.franceinfo.fr/occitanie/haute-garonne/toulouse/suppression-de-2400-postes-chez-capgemini-les-departs-volontaires-vont-pouvoir-commencer-la-cgt-s-inquiete-pour-ceux-qui-vont-rester-3369787.html
- Atos : https://www.usinenouvelle.com/article/informatique-atos-continue-de-diminuer-ses-effectifs-en-france-et-va-supprimer-135-postes.N2237427 et https://www.cgtatos.org/atos-france-un-plan-social-modifie-par-coup-de-theatre/

### Liens

- [01-cadrage-intention-initiale.md](01-cadrage-intention-initiale.md)
