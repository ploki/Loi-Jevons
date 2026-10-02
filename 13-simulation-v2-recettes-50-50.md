# Simulation v2 : recettes de la taxe 50/50 et trajectoire de montée en charge

- **Statut** : brouillon
- **Créé le** : 2026-10-02
- **Dernière mise à jour** : 2026-10-02

## En bref

> Unité retenue : l'**octet-équivalent** (octet × coefficient par type de contenu, fichier 04). Quand ce fichier parle de « token », il faut lire « unité taxable ».

Avec la règle 50/50 (taxe = 100 % du prix hors taxe), la taxe rapporte environ le **chiffre d'affaires de l'IA vendue aux professionnels en France**, soit **environ 1,3 Md€ en 2026** dans le scénario central (fourchette de 0,5 à 3 Md€). Il faut **environ 3 ans** de croissance du marché pour atteindre les 10 Md€ nécessaires, soit vers 2029, et **environ 5 ans** pour 50 Md€, soit vers 2031. La montée en charge est donc indispensable, et elle est plausible.

## Méthode

Recettes = **dépenses mondiales en modèles d'IA** × **part professionnelle** × **part de la France** × taux de change (0,9 € pour 1 $).

La taxe vaut 100 % du prix hors taxe, donc les recettes sont égales au chiffre d'affaires taxable.

## Les hypothèses

**1. Dépenses mondiales en modèles d'IA (API et abonnements), 2026**

- **[S]** Gartner (septembre 2026) : 28,3 Md$ pour les « modèles d'IA générative » et 29,2 Md$ pour les « agents et assistants ». Total : environ **57 Md$**. Gartner prévoit +117 % pour les modèles en 2026.
- **[S]** Revenu annualisé d'OpenAI : environ 70 Md$ au 3ᵉ trimestre 2026 (40 Md$ en août). Celui d'Anthropic : environ 65 Md$ fin juillet 2026.
- **[C]** Ce sont des rythmes de fin de période. Le chiffre d'affaires réel sur l'année est plus faible, et il faut y ajouter Google, Mistral et les autres. J'en déduis une fourchette de **57 / 90 / 120 Md$** (bas, central, haut).

**2. Part professionnelle**

- **[S]** Environ 70 à 75 % du revenu d'Anthropic vient de son API, et plus de 40 % de celui d'OpenAI vient des entreprises. OpenAI vend par ailleurs beaucoup d'abonnements aux particuliers.
- **[C]** Je retiens **60 / 65 / 70 %**. Les particuliers sont exonérés (fichier 04).

**3. Part de la France** : **1,5 / 2,5 / 4 %**, comme dans la simulation v1 (fichier 03).

**4. Croissance annuelle de la valeur du marché** : **×1,5 / ×2 / ×3**.

- **[S]** Gartner prévoit environ ×2,2 en 2026, et les revenus annualisés des fournisseurs sont multipliés par 2 à 3.

## Résultats

| Scénario | Recettes 2026 | Avec une baisse de la demande* | Années avant 10 Md€ | Années avant 50 Md€ |
|---|---|---|---|---|
| Bas | 0,46 Md€ | 0,33 Md€ | ~7,6 (≈ 2034) | ~11,6 |
| **Central** | **1,32 Md€** | **0,93 Md€** | **~2,9 (≈ 2029)** | **~5,2 (≈ 2031)** |
| Haut | 3,0 Md€ | 2,1 Md€ | ~1,1 (≈ 2027) | ~2,6 |

\* Le doublement du prix fait baisser la demande. Avec une élasticité de −0,5, le volume diminue d'environ 30 %. **[C]**

**Trajectoire du scénario central (Md€)** : 2026 : 1,3 · 2027 : 2,6 · 2028 : 5,3 · **2029 : 10,5** · 2030 : 21 · 2031 : 42.

## Lecture

- **[C]** Les 10 Md€ correspondent au besoin au-delà de ce que l'Unédic finance déjà (fichier 11). Les 50 Md€ correspondent au coût total estimé du chômage universel (fichier 05).
- **[C]** Le double dividende en découle directement : chaque tranche d'environ 11 Md€ supplémentaires permet de baisser la cotisation chômage d'environ 1 point (fichier 11).
- **[G] Utilisation des recettes (décision du fichier 11)** :
  1. **2026-2028** : le fonds de réserve et la formation rémunérée.
  2. **Ensuite** : un partage **moitié-moitié** entre l'extension des droits et la baisse des cotisations.
- **[C]** Avec ce partage, les 10 Md€ ne sont plus le bon objectif. Pour un chômage universel complet (environ 50 Md€, dont environ 40 Md€ déjà financés par les cotisations) avec, en plus, une baisse des cotisations, le besoin réel de recettes est plus élevé. Il faudra recalculer la trajectoire avec le partage moitié-moitié (à faire en simulation v3).

## Limites

- **Une croissance exponentielle ne dure pas.** Le scénario haut devient absurde au-delà de 2028. Même le scénario central suppose que le marché de l'IA professionnelle en France atteigne environ 42 Md€ en 2031, soit environ 1,4 % du PIB. C'est plausible si l'IA remplace réellement du travail, mais c'est **l'hypothèse clé** de toute la trajectoire.
- **L'inférence faite sur ses propres serveurs** n'est pas comptée ici. Elle **est pourtant soumise à la taxe [G]**, avec le SDK installé partout et un abattement par entreprise (fichier 08), et valorisée à l'indice du prix moyen. **Les recettes ci-dessus sont donc un minimum.**
- **Le revenu annualisé n'est pas le chiffre d'affaires de l'année**, et les chiffres d'OpenAI et d'Anthropic viennent de la presse spécialisée, pas de comptes publiés.
- **La part de la France n'est publiée nulle part** : c'est toujours la principale incertitude.

## Sources

- Gartner (16/09/2026) : https://www.gartner.com/en/newsroom/press-releases/2026-09-16-gartner-forecasts-worldwide-ai-spending-to-grow-49-point-5-percent-in-2026
- OpenAI, revenu annualisé au 3ᵉ trimestre 2026 : https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html
- Anthropic et OpenAI, répartition des revenus : https://www.saastr.com/anthropic-just-passed-openai-in-revenue-while-spending-4x-less-to-train-their-models/ et https://valueaddvc.com/blog/anthropic-revenue-hits-47b-run-rate-how-it-passed-openai-in-just-five-months
- Marché de l'IA en France (IDC, 18,4 Md€ tous segments confondus, pour ordre de grandeur) : https://www.jedha.co/formation-ia/les-chiffres-sur-le-marche-de-l-ia-en-2025

## Liens

- [03-cadrage-simulation-tokens-france-vs-masse-salariale.md](03-cadrage-simulation-tokens-france-vs-masse-salariale.md)
- [10-hypothese-taux-variable-indexe.md](10-hypothese-taux-variable-indexe.md)
- [11-cadrage-impact-economique.md](11-cadrage-impact-economique.md)
