---
name: chrome-discipline
description: >
  Protocole d'utilisation de Chrome par Claude : profil dédié, fermeture d'onglets, hiérarchie d'outils. Déclencher ce skill dès que Claude s'apprête à utiliser Chrome (MCP Claude in Chrome, navigate, tabs, computer use), ou quand la tâche implique de naviguer sur le web, se connecter à un service, ou interagir avec une page. Aussi déclencher quand Claude hésite entre computer use et les MCP disponibles. Ne PAS déclencher pour de la conversation pure ou des recherches via WebSearch/WebFetch qui ne passent pas par Chrome.
---

# Discipline Chrome — règles non négociables

Ce skill existe parce que sans lui, Claude utilise le profil personnel de Gildas, laisse des onglets ouverts partout, et recourt au computer use alors que des canaux plus propres sont disponibles. Chaque règle ci-dessous corrige un problème constaté en session réelle.

## 1. Profil Chrome dédié

Claude ne navigue JAMAIS dans le profil personnel de Gildas. Avant toute session Chrome, vérifier que le navigateur tourne sur le bon profil.

Le profil dédié s'appelle "Claude". Les credentials de ce profil seront ajoutés au fur et à mesure par Gildas — Claude ne crée jamais de compte de sa propre initiative.

Pourquoi c'est important : si Claude navigue dans le profil de Gildas, il a accès à toutes ses sessions authentifiées (Google, GitHub, services bancaires, etc.). Un clic maladroit ou une navigation vers un service qui déclenche un OAuth flow peut modifier l'état d'un compte personnel. Le profil séparé élimine ce risque à la racine.

Pour lancer Chrome sur le profil Claude via osascript :

```
open -na "Google Chrome" --args --profile-directory="Claude"
```

Si le profil n'existe pas encore, Chrome le créera automatiquement au premier lancement. Gildas y ajoutera les comptes nécessaires manuellement.

Avant d'utiliser les outils MCP Chrome (navigate, tabs_create_mcp, etc.), toujours vérifier le profil actif. En cas de doute, demander à Gildas plutôt que de naviguer à l'aveugle.

## 2. Fermeture systématique des onglets

Chaque onglet ouvert par Claude DOIT être fermé par Claude dès que l'information en a été extraite. Pas d'exception, pas de "je le garde au cas où".

Le pattern correct pour toute navigation est :

1. `tabs_create_mcp` ou `navigate` → ouvrir/aller sur la page
2. Extraire l'information nécessaire (`get_page_text`, `read_page`, screenshot, etc.)
3. `tabs_close_mcp` → fermer l'onglet

L'étape 3 doit arriver systématiquement, y compris si l'extraction échoue ou si la tâche est interrompue. C'est l'équivalent d'un `finally` block : le close n'est pas conditionnel au succès.

Pourquoi c'est important : Gildas travaille sur un M1 8 Go. Chaque onglet Chrome consomme entre 80 et 300 Mo de RAM. Cinq onglets orphelins, c'est potentiellement 1 Go de RAM perdue sur une machine qui n'en a que 8, dont une partie est déjà prise par le GPU unifié. L'impact sur les performances est direct et mesurable.

## 3. Hiérarchie d'outils — computer use en dernier recours

Claude dispose de quatre canaux d'action, classés par ordre de préférence :

1. **Bash sandboxé** — pour tout ce qui est scriptable sans interaction GUI (curl, scripts, manipulation de fichiers dans le sandbox)
2. **osascript (MCP Mac)** — pour les actions sur le Mac qui nécessitent le système mais pas un navigateur (lancer une app, manipuler des fenêtres, lire des fichiers locaux)
3. **MCP Chrome (Claude in Chrome)** — pour la navigation web, l'extraction de contenu de pages, les interactions avec des interfaces web
4. **Computer use (screenshots + contrôle souris/clavier)** — UNIQUEMENT quand aucun des trois canaux précédents ne peut atteindre l'objectif

Le computer use a un coût spécifique que les autres canaux n'ont pas : il prend le contrôle visuel de l'écran, ce qui minimise la fenêtre Claude comme effet de bord. Gildas perd alors la visibilité sur ce que Claude fait, et le retour à la conversation nécessite une manipulation manuelle. Ce coût est acceptable uniquement quand l'objectif ne peut pas être atteint autrement — typiquement une application native sans API scriptable, ou une interaction complexe qui ne passe pas par les MCP disponibles.

Avant de basculer en computer use, Claude doit se poser la question : "Est-ce que Bash, osascript ou le MCP Chrome peuvent faire ça ?" Si la réponse est oui, même partiellement, utiliser ces canaux d'abord.

## 4. Ne jamais minimiser la fenêtre Claude

Corollaire direct de la règle 3 : Claude ne doit jamais minimiser, masquer ou déplacer la fenêtre de l'application Claude (Cowork/Claude Desktop). Cette fenêtre est l'interface principale de Gildas avec Claude. La minimiser pour "faire de la place" à une action computer use est contre-productif — Gildas perd le fil de ce qui se passe.

Si une action nécessite de l'espace écran (rare), demander à Gildas plutôt que de réarranger les fenêtres de sa propre initiative.

## Checklist pré-session Chrome

Avant toute utilisation de Chrome dans une session :

- [ ] Le profil Chrome actif est "Claude" (pas le profil personnel de Gildas)
- [ ] Aucun onglet orphelin d'une session précédente ne traîne
- [ ] Le canal d'action choisi est le plus léger possible (Bash > osascript > MCP Chrome > computer use)
