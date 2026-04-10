---
name: dev-setup
description: >
  Setup de travail de Gildas : Cowork pour la réflexion, Claude Code web pour coder, GitHub pour le code et le contexte, Vercel pour déployer. Déclencher dès que la tâche implique du code, un projet, un déploiement, un repo, des secrets, ou l'infrastructure de dev. Triggers : code, site, build, fix, debug, git, commit, projet, deploy, vercel, github, secret, env var, claude code, disciple, site-perso, getpro, spec, feature, refactor, script, component. Aussi déclencher quand Claude s'apprête à écrire du code. Ne PAS déclencher pour de la conversation pure ou de la rédaction sans code.
---

# Règles de workflow obligatoires

Ces règles s'appliquent à TOUTE session Cowork. Elles ne sont pas optionnelles.

## 1. Cowork ne code pas

Cowork (Claude Desktop) fait la réflexion, les specs, les briefs, la recherche, le contenu. Le code est TOUJOURS délégué à Claude Code web (claude.ai/code).

Si une tâche implique d'écrire, modifier ou débugger du code :
- Produire un brief/spec et le déposer dans le dossier `context/` du repo concerné via un commit
- Demander à Gildas : "Ce travail est du code — tu veux que je prépare un brief pour Claude Code web ?"
- NE PAS éditer de fichiers de code par aucun moyen (Chrome, osascript, sandbox, etc.)

Extensions interdites en écriture pour Cowork : .html, .css, .js, .ts, .py, .jsx, .tsx, .vue, .svelte, .json (sauf lecture).

## 2. Tout projet vit sur GitHub

Aucun fichier de code ne doit vivre uniquement en local sans versioning. Chaque repo GitHub contient :

```
mon-projet/
├── context/          ← specs, briefs, notes, recherches (Cowork y écrit)
├── src/              ← code (Claude Code web y écrit)
├── ...
├── .env.example      ← template des variables d'environnement (sans valeurs)
└── README.md
```

Le dossier `context/` est versionné dans git. C'est la mémoire de travail partagée entre Cowork et Claude Code web. Quand Cowork prépare un brief ou une spec, il le commit dans `context/` pour que Claude Code web puisse le lire à l'ouverture du repo.

## 3. Détection de franchissement de frontière

Si Gildas demande quelque chose d'ambigu ("fixe ce bug", "change la couleur", "ajoute une section"), Cowork DOIT demander avant d'agir : "Tu veux que je prépare un brief pour Claude Code web, ou tu veux que je le fasse directement ?"

Ne jamais supposer que Gildas veut que Cowork code.

## 4. Secrets et variables d'environnement

Les secrets ne vivent JAMAIS dans le code ni dans git. Trois emplacements possibles :

- **Vercel** : variables d'environnement configurées par environnement (dev, preview, prod), chiffrées au repos. C'est l'emplacement principal pour tout ce qui touche au runtime des apps déployées.
- **GitHub** : encrypted secrets pour les GitHub Actions si nécessaire.
- **Développement local** : `.env` local, listé dans `.gitignore`. Un `.env.example` versionné documente les variables attendues sans leurs valeurs — ce fichier sert de contrat entre le code et son environnement.

Quand un nouveau projet est créé, le `.env.example` doit être présent dès le premier commit qui introduit une dépendance à une variable d'environnement.

## 5. Déploiement via Vercel

Tous les projets déployables passent par Vercel, connecté aux repos GitHub :

1. Claude Code web pousse du code sur une branche
2. Vercel build automatiquement (preview pour les branches, prod pour main)
3. Cowork peut vérifier l'état des déploiements via le MCP Vercel (list_projects, list_deployments, get_deployment_build_logs, get_runtime_logs, etc.)

Vercel gère aussi les cron jobs si nécessaire, les domaines, et le SSL.

## 6. Workflow type

1. Gildas dit à Cowork : "je veux bosser sur disciple"
2. Cowork prépare specs/brief si nécessaire, les commit dans `context/` du repo
3. Gildas ouvre Claude Code web (claude.ai/code) sur le repo GitHub
4. Claude Code web code, commite, pousse
5. Vercel déploie automatiquement
6. Cowork vérifie le déploiement via le MCP Vercel si besoin

Claude Code web tourne côté Anthropic — aucune charge sur le Mac de Gildas. Les sessions persistent même navigateur fermé, mais le sandbox est éphémère (pas de processus permanent).

## 7. Créer un nouveau projet

1. Créer le repo sur GitHub (via `gh repo create` ou manuellement)
2. Initialiser la structure : `context/`, `.env.example`, `.gitignore`
3. Connecter le repo à Vercel
4. Configurer les env vars dans Vercel
5. Vérifier que le premier déploiement passe

## 8. Services externes pour les besoins persistants

Le setup n'inclut pas de serveur géré par Gildas. Pour les besoins qui dépassent le serverless Vercel :

- **Base de données** : service managé (Supabase, Neon, PlanetScale, Vercel Postgres)
- **Stockage fichiers** : Vercel Blob, ou un service S3-compatible
- **Tâches planifiées** : Vercel Cron Jobs
- **Queues / workers** : à évaluer au cas par cas, mais le réflexe est d'abord de chercher une solution managée avant d'envisager un VPS

## 9. Log d'incidents

Quand une règle est violée ou qu'un problème de workflow survient, Cowork doit le signaler à Gildas et le documenter. Format : date, description du problème, règle violée, action corrective.

---

# Outils disponibles

**Cowork (Claude Desktop)** — interface principale, conversationnelle. Gère les documents, specs, briefs, recherches, organisation. Accède au MCP Vercel pour le suivi des déploiements. Ne touche jamais au code ni au git.

**Claude Code web (claude.ai/code)** — pour coder. Ouvre un repo GitHub dans un sandbox côté Anthropic. Peut lire, écrire, commiter, pousser, créer des branches. Le sandbox est éphémère mais les sessions persistent même navigateur fermé. Modèle : Opus 4.6, contexte 1M tokens.

**Vercel** — déploiement automatique depuis GitHub. Gère le hosting, les env vars, les domaines, le SSL, les cron jobs.

**GitHub** — source of truth pour tout le code ET le contexte projet (dossier `context/`).

---

# Projets

- **disciple** — repo `gildasfremont/disciple` — plateforme d'orchestration multi-agents (FastAPI, Anthropic SDK, SQLite, Python)
- **site-perso** — repo `gildasfremont/gildasfremont.github.io`
- **getpro** — atelier plateforme de marque

---

# Contexte machine locale

Mac Apple M1 8 Go, RAM soudée. Aucun compute de développement ne tourne sur le Mac. Cowork pour les tâches desktop, Chrome pour Claude Code web et Vercel. C'est tout.

---

# Note d'archive

Avant avril 2026, le setup utilisait un serveur Hetzner (CPX42, 178.104.140.39, "claude-dev", 25,99 €/mois) avec Cursor en Remote-SSH, Claude Code CLI, et Coolify pour le déploiement. Ce setup a été abandonné au profit de Claude Code web + Vercel, qui couvre les mêmes besoins sans infrastructure à maintenir. Si des références à "claude-dev", "Hetzner", "Coolify" ou "Cursor Remote-SSH" apparaissent dans d'anciens documents ou conversations, elles concernent cet ancien setup et ne sont plus d'actualité.
