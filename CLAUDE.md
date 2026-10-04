# CLAUDE.md

Ce dossier est un **projet maieutique** (skills `maieutics` et `metamaieutics`). Il porte sur la **Loi Jevons** : le **financement d'un chômage universel par une taxe sur l'intelligence artificielle**.

À lire en premier : `corpus/intention-de-l-auteur.md`, `corpus/00-methode-conventions-et-index.md`, `corpus/journal-des-decisions.md`, `corpus/glossaire.md`.

- **L'intendance de ce dépôt est en français**, à l'inverse de ce que demandent les skills `maieutics` et `metamaieutics` : noms des fichiers et des dossiers, titres de sections (« En vigueur », « Historique du raisonnement », « Questions ouvertes », « Liens »), en-têtes des notes. Les skills doivent s'y conformer. Les dossiers sont `corpus/` (les notes et les journaux), `livrable/`, `outils/` et `archive/`.
- Le dossier est versionné avec git (branche `main`), en **mode (c)** : un commit par itération et une entrée dans `corpus/prompt-log.md`.
- Le journal des décisions est tenu au fil de l'eau. Quand Guillaume change d'avis, chercher dans le corpus ce que ce changement rend faux, le corriger, puis inscrire le revirement au journal.

## Extension du skill, à tester avant de l'intégrer au skill

> Observations de **[sonnet-5.5]** sur la façon dont Guillaume utilise le skill et ce CLAUDE.md, tirées de la session metamaieutique des 2 à 4 octobre 2026. **Ce sont des propositions, pas des règles validées** : on les applique ici pour voir si elles aident, puis Guillaume décide lesquelles passent dans le skill. Chaque point dit ce qui a été observé, puis la règle à essayer.

1. **Le but réel se découvre en route, mandat compris.** Le mandat validé a été réécrit à l'itération 5 (il était trop étroit). *À essayer* : avant de valider un mandat, demander « qu'est-ce qui te bloque aujourd'hui ? » et vérifier que le but y répond.
2. **Pas de migration du skill pendant une session en cours.** Le skill est passé à `maieutics` (structure anglaise, marqueurs nominatifs) alors qu'une branche tournait ; la migration a été bloquée puis repoussée (décision 76). *À essayer* : finir la session avec les conventions de départ, fusionner, puis migrer sur `main` dans une itération à part. Le dire à Guillaume avant de lancer.
3. **Le coût se décide avant la boucle.** Chaque tour d'agent a coûté 200 000 à 350 000 tokens (il relit le corpus) et Guillaume a atteint sa limite. *À essayer* : proposer un budget (nombre de tours, modèle de l'orchestrateur, modèle des agents) et dire où un modèle plus petit suffit (lecture à l'aveugle, rapport de retour) et où il faut le plus fort (arbitrages, rédaction juridique).
4. **Les décisions par procuration se confondent avec celles de Guillaume.** La relecture de cohérence a trouvé des décisions prises par procuration marquées comme validées par lui. *À essayer* : relecture de cohérence toutes les 5 ou 6 itérations, pas une seule fois, avec contrôle des marqueurs de provenance.
5. **Les idées de Guillaume qui ne sont pas des décisions n'ont pas de place.** Pendant la pause, ses chantiers (effet de consommation par tranche d'âge, application Rust, données) ont fini dans le journal des décisions (n° 110, 111, 113). *À essayer* : un fichier `chantiers.md` pour ce qui est à faire plus tard, sans décision.
6. **La reprise après saturation marche avec un guide en tête de la note de travail.** Trois relèves d'agent, toutes réussies grâce à la section F de la note 18 (ordre de lecture, architecture en une page, reste à faire). *À essayer* : l'exiger dès la 3ᵉ itération de toute session longue, et la mettre à jour à chaque tour.
7. **La numérotation du journal se heurte à la fusion.** `main` et la branche ont chacun reçu un n° 37 ; deux conflits, un renommage (36 bis). *À essayer* : numéroter les décisions d'une branche avec un préfixe (`M37`) et n'ajouter aucune décision sur `main` pendant la session.
8. **Ce CLAUDE.md ne dit pas l'état courant.** Rien n'y signalait la branche ni le worktree pendant la session. *À essayer* : l'orchestrateur ajoute en tête, sur `main`, « session metamaieutics en cours sur la branche X, dossier Y », et le retire à la fusion.
9. **Se repérer après une longue marche autonome.** Guillaume a demandé deux fois où il en était (« où en est-on ? »). *À essayer* : à chaque retour d'agent et à chaque reprise, une ligne d'état : branche, dossier, itération n sur 30, ce qui tourne.
10. **Les questions qui touchent l'intention restent à Guillaume, et « je ne sais pas » est une réponse.** Les étudiants et le patrimoine ont été laissés ouverts sans bloquer la suite ; pour les 97 questions du lecteur aveugle, il a répondu qu'il ne savait pas. *À essayer* : garder ce régime, ne jamais conclure d'un « je ne sais pas », noter la question comme ouverte.
