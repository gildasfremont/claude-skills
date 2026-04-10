---
name: boost-session
description: >
  Optimise la machine de Gildas (M1 8 Go) avant une session de travail lourde avec Claude.
  Ferme les apps gourmandes en RAM (WhatsApp, Preview, etc.), réduit les onglets Chrome,
  vérifie la pression mémoire et le swap, et rapporte l'état avant/après.
  Déclencher ce skill dès que Gildas dit "boost", "nettoie", "prépare la machine",
  "libère de la RAM", "on va bosser", "session lourde", "avant de commencer",
  "fais de la place", "optimise", "clean up", ou quand une tâche lourde est sur le point
  de démarrer (génération de documents, exécution de code complexe, travail multi-agents).
  Aussi pertinent quand Claude détecte que la mémoire est sous pression pendant une session.
  Ne PAS déclencher pour de la conversation légère ou des tâches purement textuelles.
---

# Boost Session

Ce skill prépare le Mac M1 8 Go de Gildas pour une session de travail intensive avec Claude.
La contrainte de fond : 8 Go de RAM soudée, pas d'upgrade possible. Chaque Mo compte.

## Pourquoi c'est nécessaire

La VM Cowork (~1,6 Go) + Claude desktop (~1,2 Go) + les serveurs MCP node (~800 Mo) consomment
environ 3,6 Go incompressibles. macOS en prend ~2 Go. Il reste donc ~2,4 Go pour tout le reste.
Dès qu'on dépasse, le système swap et compresse en boucle, ce qui ralentit tout — y compris
les réponses de Claude dans l'interface.

## Séquence d'exécution

### 1. Diagnostic initial

Lancer via `mcp__Control_your_Mac__osascript` :

```applescript
do shell script "memory_pressure 2>/dev/null | head -5"
```

```applescript
do shell script "top -l 1 -o MEM -n 15 -stats pid,command,mem,cpu 2>/dev/null | tail -20"
```

```applescript
do shell script "sysctl vm.swapusage"
```

Capturer les valeurs de :
- Pression mémoire (normal / warn / critical)
- Swap utilisé
- Top 10 processus par RAM

Rapporter ces chiffres à l'utilisateur de manière concise.

### 2. Fermeture des apps non essentielles

Les apps suivantes sont considérées non essentielles pendant une session de travail.
Les fermer via osascript **seulement si elles sont en cours d'exécution** :

```applescript
tell application "System Events"
  set runningApps to name of every process whose background only is false
end tell
```

**Apps à fermer automatiquement (sans demander) :**
- WhatsApp
- Preview / Aperçu
- Messages
- FaceTime
- Musique / Music
- Podcasts
- News / Actualités
- Bourse
- Plans / Maps
- Photos (sauf si l'utilisateur travaille dessus)

Pour chaque app détectée :
```applescript
tell application "NomApp" to quit
```

**Apps à signaler mais ne PAS fermer sans confirmation :**
- Figma (travail en cours possible)
- Slack (communication active possible)
- Mail (peut être nécessaire)
- Tout app non listée ci-dessus

### 3. Réduction Chrome

Chrome est le principal levier de libération mémoire après les apps.
Vérifier le nombre de processus renderer Chrome :

```applescript
do shell script "pgrep -f 'Chrome Helper (Renderer)' | wc -l"
```

Si plus de 8 renderers :
- Informer l'utilisateur du nombre d'onglets/processus Chrome
- Suggérer de fermer les onglets non nécessaires
- Ne PAS fermer Chrome ou ses onglets sans confirmation explicite

Si Chrome n'est pas nécessaire pour la session :
- Proposer de le quitter entièrement (gain ~2-3 Go)

### 4. Nettoyage système léger

Purger les caches mémoire inactifs :

```applescript
do shell script "purge 2>/dev/null || true"
```

Note : `purge` nécessite parfois des droits admin. Si ça échoue, ce n'est pas grave,
le système fait ça naturellement sous pression.

### 5. Diagnostic final

Relancer les mêmes commandes qu'à l'étape 1 et comparer :
- RAM libérée (delta avant/après)
- Pression mémoire (changement de niveau)
- Swap (réduction éventuelle)

### 6. Rapport

Présenter un résumé concis en prose :
- Ce qui a été fermé et combien de Mo libérés
- État actuel de la mémoire
- Si la machine est prête pour du travail lourd ou si des actions supplémentaires sont recommandées
- Si Chrome tourne encore, rappeler combien il consomme

## Comportement adaptatif

Si le diagnostic initial montre une pression mémoire "normal" et moins de 1 Go de swap utilisé,
le skill peut se contenter de rapporter que la machine est en bon état sans rien fermer.
L'objectif n'est pas de tout quitter systématiquement, mais de libérer de la marge quand c'est nécessaire.

## Choses à ne jamais faire

- Ne jamais quitter Finder, WindowServer, Spotlight ou tout processus système
- Ne jamais quitter Claude (évidemment)
- Ne jamais kill -9 un processus (toujours utiliser `tell application X to quit`)
- Ne jamais fermer Chrome ou Slack sans confirmation explicite
- Ne jamais toucher aux processus node liés à Claude/MCP
