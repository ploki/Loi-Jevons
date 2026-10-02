# Simulation v3 : trajectoire avec la règle de taux et le partage moitié-moitié

- **Statut** : brouillon
- **Créé le** : 2026-10-02
- **Dernière mise à jour** : 2026-10-02

## En bref

Dans le scénario central, **le plancher 50/50 seul ne suffit pas** : en 2035, il rapporte environ 16 Md€, le chômage universel n'est pas encore complet et la cotisation n'a baissé que de 0,7 point. **Avec le moteur et le plafond de 4 fois le prix**, le chômage universel est complet **vers 2031**, et la cotisation baisse d'environ **2,8 points en 2035**. Tout dépend de la croissance du marché : le scénario haut atteint tous les objectifs dès 2032 en restant près du plancher, le scénario bas ne les atteint jamais.

> Unité : l'octet-équivalent (fichier 04). Le script de calcul est dans `outils/sim_v3.py`.

## Hypothèses **[C]**

- **Point de départ** : le chiffre d'affaires de l'IA vendue aux professionnels en France, hors taxe, en 2026 (simulation v2, fichier 13). Bas : 0,46 Md€ ; central : 1,32 Md€ ; haut : 3,0 Md€.
- **Croissance du marché, qui ralentit chaque année** (une croissance exponentielle ne dure pas) :
  - central : ×2,0 en 2027, puis ×1,8 ; 1,6 ; 1,45 ; 1,3 ; 1,2 ; 1,15 ; 1,1 ; 1,05 ;
  - bas : de ×1,5 à ×1,1 ;
  - haut : de ×2,5 à ×1,05.
- **Règle de taux** (fichier 10) : un multiple m du prix moyen, compris entre 1 (le plancher 50/50) et 4 (le plafond).
- **Réaction de la demande** : une élasticité de −0,5. Recettes = m × marché × (1+m)^−0,5. À m = 1, la demande baisse d'environ 30 %. À m = 4, elle baisse d'environ 55 %.
- **Utilisation des recettes** (fichier 11) :
  - **2026-2028** : tout va au fonds de réserve et à la formation rémunérée.
  - **À partir de 2029** : on finance d'abord le maintien des mesures déjà décidées, puis le **surplus** se partage **moitié-moitié** :
    - **A, l'extension des droits** : objectif de 10 Md€ par an, puisque le chômage universel complet coûte environ 50 Md€ et que l'Unédic en finance déjà environ 40 ;
    - **B, la baisse des cotisations** : objectif de 44 Md€ par an, soit 4 points de cotisation à environ 11 Md€ chacun.
  - Quand A atteint son objectif, le surplus va entièrement à B.
- **Le moteur** (variante 2) : à partir de 2029, m est fixé pour atteindre les deux objectifs **en 2032**, dans la limite du plafond de 4.

## Résultats : scénario central

| Année | Marché HT (Md€) | Plancher seul : recettes | Plancher seul : A / B | Avec moteur : m | Avec moteur : recettes | Avec moteur : A / B (points de cotisation) |
|---|---|---|---|---|---|---|
| 2026 | 1,3 | 0,9 | réserve | 1,0 | 0,9 | réserve |
| 2027 | 2,6 | 1,9 | réserve | 1,0 | 1,9 | réserve |
| 2028 | 4,8 | 3,4 | réserve (fonds ≈ 6,2) | 1,0 | 3,4 | réserve (fonds ≈ 6,2) |
| 2029 | 7,6 | 5,4 | 2,7 / 2,7 | 3,95 | 13,5 | 6,8 / 6,8 (0,6 pt) |
| 2030 | 11,0 | 7,8 | 3,9 / 3,9 | 4,0 | 19,7 | 9,9 / 9,9 (0,9 pt) |
| 2031 | 14,3 | 10,1 | 5,1 / 5,1 | 4,0 | 25,6 | **10 / 15,6** (1,4 pt) |
| 2032 | 17,2 | 12,2 | 6,1 / 6,1 | 4,0 | 30,8 | 10 / 20,8 (1,9 pt) |
| 2035 | 22,8 | 16,2 | 8,1 / 8,1 (0,7 pt) | 4,0 | 40,9 | 10 / 30,9 (**2,8 pts**) |

## Résultats : comparaison des scénarios en 2035

| Scénario | Plancher seul : recettes | Chômage universel complet ? | Avec moteur : recettes | Chômage universel complet ? | Baisse de cotisation |
|---|---|---|---|---|---|
| Bas | 3,3 Md€ | non (1,6 sur 10) | 8,3 Md€ (m = 4) | non (4,2 sur 10) | 0,4 pt |
| **Central** | **16,2 Md€** | non (8,1 sur 10) | **40,9 Md€** (m = 4) | **oui, vers 2031** | **2,8 pts** |
| Haut | 52,3 Md€ | oui, vers 2030 | 54 Md€ (m ≈ 1,0-1,4) | oui, vers 2030 | **4 pts dès 2032** |

## Lecture **[C]**

1. **Le plancher 50/50 est un principe moral, pas un financement suffisant.** Sauf dans le scénario haut, c'est le **moteur**, avec son plafond de 4 fois le prix, qui rend le chômage universel atteignable dans les années 2030. Le choix d'un plafond élevé est donc décisif.
2. **Le scénario haut montre la logique de Jevons à l'œuvre** : quand le marché croît fortement, tous les objectifs sont atteints avec un taux proche du plancher. **Plus l'IA réussit, plus la taxe est légère.** C'est un argument fort pour l'exposé des motifs.
3. **La baisse de cotisation est l'objectif le plus coûteux.** Remplacer les 4 points coûte environ 44 Md€, soit plus de quatre fois l'extension des droits. Il est réaliste de viser **1 à 3 points vers 2035** dans le scénario central.
4. **Le fonds de réserve accumulé pendant le rodage** (environ 6 Md€ dans le scénario central) représente environ six mois de recettes de 2030. C'est un amortisseur sérieux en cas de récession.

## Mise à jour après les paramètres du chômage universel

- Le besoin pour l'extension des droits passe d'environ 10 Md€ à **environ 16 à 20 Md€** (fichier 05).
- **Nouvelle simulation du scénario central, avec le moteur et un objectif de 16 Md€** :
  - le chômage universel complet est atteint **vers 2033**, au lieu de 2031 ;
  - la baisse de cotisation atteint environ **2,3 points en 2035**, au lieu de 2,8.

## Limites

- **Le lissage n'est pas modélisé.** Dans la variante avec moteur, m saute de 1 à près de 4 en 2029, ce qui est contraire au lissage de ±20 % prévu (fichier 10). Une montée progressive, par exemple 1 → 1,5 → 2 → 3 → 4, **retarderait** les résultats d'environ 2 ans.
- **À m = 4, la demande baisse d'environ 55 %** si l'élasticité vaut −0,5. Si la demande réagit plus fortement, les recettes au plafond sont plus faibles. Le chiffre de l'élasticité est **inconnu** : c'est la deuxième hypothèse clé, après la croissance du marché.
- **L'IA qui tourne sur les serveurs des entreprises n'est pas incluse**, alors qu'elle est taxée (fichier 08) : les recettes sont un **minimum**. Ni l'abattement ni le taux réduit sur l'IA locale ne sont non plus modélisés, et ils jouent en sens inverse.
- **Le coût de la formation rémunérée** pendant le rodage n'est pas chiffré. Il réduit d'autant le fonds de réserve.
- **Les objectifs** ont été mis à jour : environ 16 à 20 Md€ pour les droits (voir la section précédente).
- **L'entrée en vigueur en 2026 est théorique.** Une loi votée au mieux en 2027 décalerait tout d'environ un an.

## Liens

- [13-simulation-v2-recettes-50-50.md](13-simulation-v2-recettes-50-50.md)
- [10-hypothese-taux-variable-indexe.md](10-hypothese-taux-variable-indexe.md)
- [11-cadrage-impact-economique.md](11-cadrage-impact-economique.md)
- [05-hypothese-revenu-universel-musk.md](05-hypothese-revenu-universel-musk.md)
