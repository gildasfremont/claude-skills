---
name: menage
description: "Nettoyage périodique du Mac de Gildas : audit disque, classification des projets (actif/dormant/mort), archivage sur GitHub ou Google Drive, suppression locale. Déclencher ce skill dès que Gildas mentionne 'ménage', 'nettoyage', 'ranger', 'libérer de la place', 'disk space', 'archiver', 'cleanup', 'faire de la place', 'qu'est-ce qui prend de la place', 'projets dormants', ou quand l'espace disque libre passe sous 30 Go. Aussi déclencher quand Gildas demande d'organiser ~/Projects, ~/Desktop, ou ~/Downloads. Ne PAS confondre avec boost-session (qui optimise la RAM, pas le disque)."
---

# Ménage — Nettoyage et archivage du Mac

Ce skill encode le workflow de nettoyage établi pour la machine de Gildas (MacBook Air M1, 228 Go). L'objectif est de maintenir ~80 Go libres en archivant ce qui dort et en supprimant ce qui est redondant, sans jamais perdre de données.

## Règles absolues

1. **Ne jamais toucher à la config Claude Desktop.** Pas de suppression dans `~/Library/Application Support/Claude/` sauf le Cache et le Code Cache quand l'app est fermée. Le dossier `vm_bundles` (≈20 Go) est intouchable — il se retéléchargerait de toute façon.

2. **Code → GitHub, pas Drive.** Tout projet avec du code source va sur un repo GitHub privé via `gh`. On ne met jamais un dossier `.git` dans Drive (ça syncherait des milliers de petits fichiers inutilement). Avant de push sur GitHub, scanner les secrets (`.env`, `.key`, `credentials`, `master.key`, tokens en clair dans des JSON).

3. **Non-code → "Archive pour Drive".** Les fichiers non-code (vidéos, PDFs, exports, dossiers de mission) vont dans `~/Desktop/Archive pour Drive/` qui est synchronisé via Google Drive for Desktop. Une fois synchés, on les déplace dans Drive vers un dossier "Archive Desktop" non synchronisé, puis on supprime le local.

4. **Nettoyer avant d'archiver.** Avant tout déplacement vers Drive : supprimer `node_modules`, `.next`, `venv`, `.pythonlibs`, `.cache`, `dist`, `build`. Supprimer les `.git` (le code est déjà sur GitHub). Supprimer les `.env` et fichiers sensibles.

5. **Build artifacts = toujours supprimables.** `node_modules`, `.next`, `venv`, `.pythonlibs`, `.cache`, `dist`, `build` ne contiennent aucun code source. Un `npm install` ou `pip install` les recrée. Les supprimer même sur les projets actifs si l'espace manque.

## Workflow de nettoyage

### Phase 1 — Audit

Commencer par un état des lieux complet. Ne pas demander d'autorisation, creuser à fond.

1. Espace disque global : `df -h /` pour total/libre.
2. Consommateurs principaux dans Home : `du -sh ~/Library ~/Downloads ~/Projects ~/Desktop ~/Documents 2>/dev/null | sort -rh`.
3. Pour chaque projet dans `~/Projects` : taille totale, taille des build artifacts, présence d'un `.git`, présence d'un remote GitHub (`git remote -v`), date du dernier commit (`git log -1 --format=%cr`), présence de fichiers sensibles (`find . -name ".env" -o -name "*.key" -o -name "credentials*" -o -name "master.key"`).
4. Pour `~/Desktop` : lister les sous-dossiers et leur taille, identifier ce qui est du travail en cours vs de l'archive.
5. Pour `~/Downloads` : lister les fichiers > 50 Mo, identifier les doublons et les installeurs (.dmg, .pkg).

Produire un document de diagnostic complet dans `/Users/gildasfremont/Desktop/Archive pour Drive/diagnostic-menage-YYYY-MM-DD.md` avec tableaux et plan d'action chiffré.

### Phase 2 — Classification des projets

Classer chaque projet dans une des catégories suivantes :

- **Actif** : dernier commit < 2 semaines, ou remote GitHub avec activité récente, ou explicitement mentionné par Gildas comme en cours. Action : garder tel quel, éventuellement nettoyer les build artifacts si l'espace est critique.
- **Dormant** : dernier commit > 2 mois, remote GitHub existant. Action : supprimer les build artifacts. Si le remote est à jour, le local peut être supprimé (un `git clone` le ramène).
- **Dormant sans remote** : dernier commit > 2 mois, pas de remote GitHub. Action : créer un repo GitHub privé, push, puis supprimer le local.
- **Non-code** : pas de `.git`, contient des fichiers média, PDFs, exports. Action : nettoyer les fichiers sensibles, déplacer vers "Archive pour Drive".
- **Mort** : build artifacts orphelins, dossiers vides, caches. Action : supprimer directement.

Présenter la classification à Gildas sous forme de tableau avec la taille, le verdict, et l'action proposée. Attendre sa validation avant d'exécuter.

### Phase 3 — Exécution

Exécuter par ordre d'impact décroissant (plus gros gains d'abord).

**Pour les projets code → GitHub :**
1. Vérifier qu'il n'y a pas de changements non commités (`git status`).
2. Scanner les secrets : `grep -r "ANTHROPIC_API_KEY\|sk-ant-\|ghp_\|gho_\|password\|secret" --include="*.json" --include="*.env" --include="*.yml" --include="*.yaml" .` et vérifier le `.gitignore`.
3. Si des secrets sont trouvés, les ajouter au `.gitignore` et ne pas les commiter.
4. Créer le repo : `gh repo create <nom> --private --source=. --push`.
5. Vérifier que le push a fonctionné : `gh repo view <nom>`.
6. Supprimer le dossier local : `rm -rf ~/Projects/<nom>`.

**Pour les fichiers non-code → Drive :**
1. Supprimer les build artifacts et caches.
2. Supprimer les `.git` (la règle dit : si c'est sur GitHub, pas besoin dans Drive).
3. Supprimer les `.env` et fichiers sensibles.
4. Déplacer vers `~/Desktop/Archive pour Drive/` : `mv ~/Projects/<dossier> ~/Desktop/Archive\ pour\ Drive/`.
5. Le dossier sera synchronisé automatiquement par Google Drive for Desktop.

**Pour les build artifacts sur projets actifs :**
1. `rm -rf node_modules .next dist build venv .pythonlibs .cache` dans chaque projet concerné.
2. Ne pas toucher au code source, aux configs, ni aux lockfiles (package-lock.json, yarn.lock).

### Phase 4 — Gestion Drive

Une fois les fichiers dans "Archive pour Drive" et synchronisés :

1. Vérifier avec le MCP Google Drive que les fichiers sont bien arrivés dans "Mon MacBook Air > Desktop > Archive pour Drive".
2. Déplacer les fichiers dans Drive vers un dossier "Archive Desktop" (non synchronisé) pour libérer l'espace local.
3. Confirmer que le déplacement Drive est fait, puis supprimer le contenu local de `~/Desktop/Archive pour Drive/` (en gardant le dossier vide).

Cette phase peut nécessiter d'attendre que la synchronisation Drive soit terminée. Vérifier avec `brctl status` ou en vérifiant la présence des fichiers dans Drive via le MCP.

### Phase 5 — Vérification finale

1. `df -h /` pour confirmer l'espace récupéré.
2. Comparer avec l'état initial du diagnostic.
3. Mettre à jour le document de diagnostic avec les résultats.
4. Lister les projets actifs restants et leur taille pour référence.

## Zones connues

| Zone | Comportement typique |
|---|---|
| ~/Downloads | S'accumule vite. Zips Google Drive, DMGs, screenshots. Souvent 10+ Go récupérables. |
| ~/Projects | 20-30 projets, beaucoup dormants. Les node_modules seuls font 3-5 Go. |
| ~/Desktop | Dossiers de missions (Lucca, GetPro), Archives. "Archive pour Drive" est le staging. |
| ~/Library/Application Support/Claude | 20 Go de VM (intouchable) + ~1 Go de cache (supprimable app fermée). |
| ~/Documents | Généralement négligeable (<50 Mo). |

## Fréquence recommandée

Un ménage complet tous les mois, ou dès que l'espace libre passe sous 30 Go. Un nettoyage léger (Downloads + build artifacts) peut être fait à chaque session de travail via le skill boost-session.
