# Chantiers

- **Statut** : en discussion
- **Créé le** : 2026-10-05
- **Dernière mise à jour** : 2026-10-05 (création, décision 125)

> Les idées de Guillaume à faire plus tard, qui ne sont pas des décisions (instruction n° 5 du `CLAUDE.md`, à tester). Un chantier dit ce qu'il faut faire et pourquoi ; il ne tranche rien. Quand un chantier débouche sur une décision, elle va au journal, et le chantier renvoie vers elle.

## En vigueur

### 1. L'effet de la mesure par la consommation, par tranche d'âge

- **[ggim]** Étudier ce que la mesure rapporte en retour à l'économie, et pas seulement ce qu'elle coûte : la consommation supplémentaire (TVA, achats de biens et services), **tranche d'âge par tranche d'âge**, avec un cas à part pour les **jeunes adultes en formation initiale qui vivent chez leurs parents**, vus comme un coup de pouce aux jeunes les plus défavorisés.
- **Ce n'est pas une décision d'inclure les étudiants** : « il faut étudier » [ggim]. La question reste ouverte et réservée à Guillaume (décision 70 ; fichier 17, Q50).
- **Points à instruire** [opus-5.5] : le multiplicateur de dépense et les recettes de TVA par tranche d'âge ; l'effet sur les foyers des parents (APL, prestations familiales, quotient familial) ; l'effet net sur le besoin de financement. Le cas des étudiants pèse le plus lourd : + 39,5 Md€ par an dans la variante de la décision 70.
- **Où cela aboutirait** : l'étude d'impact.
- **Origine** : 2026-10-04, journal 110.

### 2. Une application de simulation en Rust

- **[ggim]** Réaliser « à un moment » une application en Rust pour **simuler la mesure sur tous les indicateurs (KPI)**, plus complète que les deux scripts Python actuels.
- **[ggim]** Elle doit permettre de **changer les paramètres et les conditions en temps réel**. Lecture confirmée par Guillaume le 2026-10-04 : les paramètres sont les valeurs (m, taux d'indexation, élasticité, abattement, socle cible…) ; les conditions sont les règles et les variantes (étudiants inclus ou non, réduction pour le patrimoine, durée du tarif sur terminal, règle d'emploi des recettes).
- **[ggim]** Elle aura **besoin de données**, qui restent à identifier.
- **Rien n'est lancé** : ni calendrier, ni périmètre des indicateurs. Les scripts `outils/sim_v4.py` et `outils/etude_impact_v01.py` restent la référence chiffrée en attendant.
- **Origine** : 2026-10-04, journal 111 et 113.

---

## Historique du raisonnement

1. **2026-10-05** : création du fichier à la demande de Guillaume, pour tester l'instruction n° 5 du `CLAUDE.md`. Les deux chantiers y sont rangés depuis le journal (n° 110, 111, 113), qui n'est pas modifié, et depuis les questions ouvertes des notes 18 et 19, qui renvoient désormais ici. **[ggim]**

## Liens

- [journal-des-decisions.md](journal-des-decisions.md)
- [18-faisabilite-obstacles-juridiques-et-architecture.md](18-faisabilite-obstacles-juridiques-et-architecture.md)
- [19-simulation-v4-architecture-revisee.md](19-simulation-v4-architecture-revisee.md)
