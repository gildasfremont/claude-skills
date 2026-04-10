---
name: playwright
description: >
  Contrôle de navigateur via Playwright MCP (Microsoft). Instance isolée, 26+ outils, cross-browser. Déclencher dès que la tâche implique : naviguer sur un site, scraper, remplir un formulaire, tester une UI, vérifier un déploiement, automatiser une action web, capturer un screenshot de page, interagir avec une webapp. Triggers : browser, navigateur, scrape, formulaire, test UI, screenshot page, vérifier le site, ouvrir une page, playwright, automation web, remplir, cliquer, naviguer. Ne PAS déclencher pour du browsing simple via Claude in Chrome (lecture rapide d'une page déjà ouverte).
---

# Playwright MCP (Microsoft) — @playwright/mcp

Serveur MCP officiel Microsoft. Lance sa propre instance Chromium isolée.
## Quand l'utiliser

- Automatisation multi-étapes (formulaires, workflows, parcours utilisateur)
- Scraping de pages publiques sans authentification
- Vérification de déploiements (Vercel, sites publics)
- Tests cross-browser (Chromium, Firefox, WebKit via --browser)
- Quand l'isolation est nécessaire (pas de sessions authentifiées exposées)

## Quand utiliser Claude in Chrome à la place

- Lecture rapide d'une page déjà ouverte
- Actions dans des apps où Gildas est authentifié (Gmail, Notion, dashboards)
- Vérifications visuelles rapides

## Outils disponibles

- `browser_navigate` → URL cible
- `browser_snapshot` → arbre d'accessibilité avec refs (e1, e5, etc.)
- `browser_click` → cliquer via ref
- `browser_type` → taper du texte
- `browser_fill_form` → remplir un formulaire
- `browser_select_option` → sélectionner dans un dropdown
- `browser_press_key` → appuyer sur une touche
- `browser_take_screenshot` → capture visuelle
- `browser_wait_for` → attendre un élément ou une condition
- `browser_evaluate` → exécuter du JS dans la page
- `browser_run_code` → exécuter un snippet Playwright complet

## Pattern d'usage standard

1. `browser_navigate` → aller sur la page
2. `browser_snapshot` → lire l'arbre, repérer les refs
3. `browser_click` / `browser_type` → interagir via refs
4. `browser_snapshot` ou `browser_take_screenshot` → vérifier le résultat

## Coût token

Chaque snapshot retourne l'arbre d'accessibilité complet. Sur des pages complexes, ça peut faire 50k+ tokens. Préférer `depth` limité pour les pages lourdes.

## Note

playwright-repl (@playwright-repl/mcp) a été testé et désinstallé : crash systématique après 30s d'idle, bug côté package. Si une future version corrige le problème, reconsidérer.