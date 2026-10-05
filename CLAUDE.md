# CLAUDE.md

Ce dossier est un **projet maieutique** (skills `maieutics` et `metamaieutics`). Il porte sur la **Loi Jevons** : le **financement d'un chômage universel par une taxe sur l'intelligence artificielle**.

À lire en premier : `corpus/intention-de-l-auteur.md`, `corpus/00-methode-conventions-et-index.md`, `corpus/journal-des-decisions.md`, `corpus/glossaire.md`.

- **L'intendance de ce dépôt est en français**, à l'inverse de ce que demandent les skills `maieutics` et `metamaieutics` : noms des fichiers et des dossiers, titres de sections (« En vigueur », « Historique du raisonnement », « Questions ouvertes », « Liens »), en-têtes des notes. Les skills doivent s'y conformer. Les dossiers sont `corpus/` (les notes et les journaux), `livrable/`, `outils/` et `archive/`.
- Le dossier est versionné avec git (branche `main`), en **mode (c)** : un commit par itération et une entrée dans `corpus/prompt-log.md`.
- Le journal des décisions est tenu au fil de l'eau. Quand Guillaume change d'avis, chercher dans le corpus ce que ce changement rend faux, le corriger, puis inscrire le revirement au journal.

## Instructions à tester avant de les intégrer au skill

> Propositions de **[sonnet-5.5]** (1 à 10, tirées de la session metamaieutique des 2 à 4 octobre 2026) et de **[opus-5.5]** (11). **Elles ne sont pas validées** : applique-les dans ce projet ; Guillaume décide lesquelles passent dans le skill. La parenthèse dit d'où vient chaque instruction ; le détail est au journal et dans l'historique git.

1. **Avant de valider un mandat, demande à Guillaume « qu'est-ce qui te bloque aujourd'hui ? »**, et vérifie que le but du mandat y répond. *(Origine : le mandat validé, trop étroit, a été réécrit à l'itération 5.)*
2. **Ne migre pas le skill pendant une session en cours.** Finis la session avec les conventions de départ, fusionne, puis migre sur `main` dans une itération à part. Dis-le à Guillaume avant de lancer. *(Origine : la migration vers `maieutics`, bloquée puis repoussée, décision 76.)*
3. **Décide le coût avant la boucle.** Propose un budget : nombre de tours, modèle de l'orchestrateur, modèle des agents. Dis où un modèle plus petit suffit (lecture à l'aveugle, rapport de retour) et où il faut le plus fort (arbitrages, rédaction juridique). *(Origine : chaque tour d'agent a coûté 200 000 à 350 000 tokens, et Guillaume a atteint sa limite.)*
4. **Fais une relecture de cohérence toutes les cinq ou six itérations**, pas une seule fois, et contrôles-y les marqueurs de provenance. *(Origine : des décisions prises par procuration étaient marquées comme validées par Guillaume.)*
5. **Consigne dans un fichier `chantiers.md` les idées de Guillaume à faire plus tard qui ne sont pas des décisions**, et non au journal des décisions. *(Origine : ses chantiers ont fini au journal, n° 110, 111 et 113.)*
6. **Dès la 3ᵉ itération d'une session longue, tiens un guide de reprise en tête de la note de travail** (ordre de lecture, architecture en une page, reste à faire), et mets-le à jour à chaque tour. *(Origine : trois relèves d'agent, toutes réussies grâce à la section F de la note 18.)*
7. **Pendant une session sur une branche, numérote ses décisions avec un préfixe (`M37`)**, et n'ajoute aucune décision au journal de `main`. *(Origine : `main` et la branche ont chacun reçu un n° 37 ; deux conflits, un renommage en 36 bis.)*
8. **Au lancement d'une session metamaieutics, écris en tête de ce CLAUDE.md, sur `main`, « session metamaieutics en cours sur la branche X, dossier Y »**, et retire la ligne à la fusion. *(Origine : rien n'y signalait la branche ni le worktree pendant la session.)*
9. **À chaque retour d'agent et à chaque reprise, donne une ligne d'état** : branche, dossier, itération n sur le maximum du mandat, ce qui tourne. *(Origine : Guillaume a demandé deux fois « où en est-on ? ».)*
10. **Laisse à Guillaume les questions qui touchent son intention, et accepte « je ne sais pas » comme réponse** : note la question comme ouverte, n'en conclus rien, et continue sans bloquer. *(Origine : les étudiants et le patrimoine laissés ouverts ; « je ne sais pas » pour les 97 questions du lecteur aveugle.)*
11. **Ne commite que si toutes les modifications ont réussi.** Enchaîne la modification et le commit par `&&`, ou fais s'arrêter le script au premier échec. Avant d'insérer, vérifie que le point d'ancrage existe. Relis dans le journal tout numéro de décision ou de note que tu cites, au lieu de le citer de mémoire. Après une modification groupée, compte ce qui a changé avant de commiter. *(Origine : un commit incomplet le 2026-10-05, journal 123.)*
