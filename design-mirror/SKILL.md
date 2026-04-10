---
name: design-mirror
description: >
  Évalue le comportement de Gildas dans ses sessions de travail par rapport à son référentiel de principes de conception.
  Utiliser ce skill quand Gildas demande une revue de ses sessions récentes, un miroir de ses pratiques,
  une évaluation de sa cohérence, ou quand il veut calibrer / mettre à jour ses principes.
  Déclencher aussi quand il dit "miroir", "évalue ma session", "est-ce que j'ai respecté mes principes",
  "review de mon travail", "calibre mes principes", "qu'est-ce que j'ai fait de bien ou de mal",
  ou toute variante. Déclencher systématiquement en fin de session de travail substantielle
  si Gildas a indiqué vouloir un suivi régulier.
---

# Design Mirror

Évalue le comportement de conception de Gildas en le confrontant à son référentiel de principes.

## Quand ce skill se déclenche

Deux modes d'invocation :

1. **Revue ponctuelle** — Gildas demande une évaluation d'une ou plusieurs sessions récentes.
2. **Calibration** — Gildas veut mettre à jour le référentiel lui-même (ajouter, reformuler, déclasser un principe).

## Référentiel

Le référentiel est dans `references/referentiel.md`. Il contient trois couches :

- **Couche 1 — Principes de sortie** : ce que le travail fini doit être.
- **Couche 2 — Patterns de fabrication** : comment le travail est construit dans l'outil.
- **Couche 3 — Patterns de pilotage** : comment le processus est dirigé en conversation.

Chaque principe a des signaux positifs et négatifs. Le référentiel est versionné et évolue via la boucle de calibration.

Lire `references/referentiel.md` avant toute évaluation.

## Mode Revue

### Étape 1 — Collecter les sessions

Utiliser `mcp__session_info__list_sessions` pour lister les sessions disponibles. Filtrer celles qui contiennent du travail de conception (exclure les sessions de test, les conversations triviales, les sessions qui n'ont qu'un ou deux échanges).

Si Gildas ne précise pas de périmètre, prendre les sessions depuis la dernière revue (date dans le journal de calibration) ou les 7 derniers jours si aucune revue n'a eu lieu.

### Étape 2 — Lire et analyser

Pour chaque session retenue, lire le transcript via `mcp__session_info__read_transcript`.

Analyser le transcript en cherchant les moments de décision — pas les échanges mécaniques (appels d'outils, confirmations), mais les points où un choix de conception est fait ou un comportement de pilotage est observable.

Pour chaque moment de décision identifié, noter :
- Ce qui s'est passé (le fait observable)
- Quel(s) principe(s) du référentiel sont en jeu
- Si le comportement est cohérent ou en tension avec le principe

### Étape 3 — Produire le diagnostic

Présenter le diagnostic en prose continue, session par session. Pas de tableau, pas de score numérique. Pour chaque session, décrire :

1. Ce que Gildas a construit ou fait dans cette session (en une phrase).
2. Les principes qui étaient en jeu et comment ils se sont manifestés — en citant les moments concrets du transcript.
3. Les tensions éventuelles : moments où le comportement observé diverge d'un principe, ou moments où deux principes entrent en conflit.

Ne pas juger. Décrire le mécanisme. Laisser Gildas décider si la tension est un problème ou un choix délibéré.

### Étape 4 — Recueillir le verdict

Pour chaque tension ou observation notable, demander à Gildas :
- **Juste** — l'observation est correcte et le principe s'applique bien ici.
- **Faux** — l'observation est incorrecte (mauvaise lecture du transcript ou du principe).
- **Délibéré** — le comportement diverge du principe, mais c'est un choix conscient dans ce contexte.
- **À reformuler** — le principe est mal formulé, il ne capture pas ce que Gildas fait réellement.

## Mode Calibration

Quand Gildas veut mettre à jour le référentiel :

### Renforcement

Un principe confirmé à travers plusieurs sessions et plusieurs contextes différents se renforce. Pas de changement à faire, juste noter dans le journal.

### Déclassement

Un principe que Gildas contredit régulièrement sans que ça le dérange n'est probablement pas un vrai principe. Deux options : reformuler pour capturer ce qu'il fait réellement, ou le retirer du référentiel. Proposer les deux options, laisser Gildas trancher.

### Nouveau principe candidat

Si l'analyse des sessions révèle un comportement récurrent qui n'est capturé par aucun principe existant, le proposer comme candidat. Un candidat devient principe après confirmation dans au moins trois sessions distinctes.

### Mise à jour du fichier

Après calibration, mettre à jour `references/referentiel.md` :
- Incrémenter la version.
- Modifier les principes concernés.
- Ajouter les entrées dans le journal de calibration (date, session, principe, observation, verdict).

## Ce que ce skill ne fait pas

- Il ne donne pas de score. Il n'y a pas de note de 0 à 10.
- Il ne dit pas "bien" ou "mal". Il décrit des cohérences et des tensions.
- Il ne prescrit pas. Si Gildas dévie d'un principe, c'est peut-être le principe qui est mauvais.
- Il ne s'invoque pas automatiquement sans que Gildas le demande ou l'ait programmé.
