# Référentiel de principes — Gildas Frémont

Version: 0.1 — 25 mars 2026
Calibré sur : 10 sessions Cowork (mars 2026)

---

## Couche 1 — Principes de sortie

Ce que le travail fini doit être.

### 1.1 Soustraction

Le processus de conception consiste à retirer jusqu'à ce que tout ce qui reste soit structurel. S'applique indifféremment à un layout, une copy, une architecture logicielle, un périmètre de feature. L'unité de mesure n'est pas ce qu'on a ajouté mais ce qu'on a réussi à ne pas mettre.

Signaux positifs : palette réduite, suppression de sections entières, police unique, une seule colonne.
Signaux négatifs : ajout d'éléments décoratifs, sections qui reformulent les précédentes, options multiples non tranchées.

### 1.2 Démonstration, pas affirmation

La compétence se transmet par la preuve embarquée dans le travail lui-même, jamais par la revendication. Toute formulation qui dit "nous sommes bons" ou "c'est simple" est un signal d'insécurité. Montrer le travail en détail, y compris ses limites, est plus convaincant que le qualifier.

Signaux positifs : walkthrough détaillé, onglet "vérifications manuelles", transparence sur ce qui n'a pas marché.
Signaux négatifs : sections "à propos de nous", adjectifs auto-qualificatifs, dissimulation des limites.

### 1.3 Précision opératoire

Chaque élément — mot, composant, champ de données, feature — doit porter une information qui contraint une décision ou une action. Les qualificatifs de confort ("pertinent", "innovant", "optimisé"), les anglicismes de paresse syntaxique, les best practices génériques sont des symptômes du même problème : on a mis quelque chose qui ne fait rien.

Signaux positifs : chaque mot porte du sens opératoire, pas de synonyme décoratif, terminologie française précise.
Signaux négatifs : adjectifs de confort, calques de l'anglais dans la syntaxe, formulations génériques.

### 1.4 Le prompt est l'interface

Dans un système à base d'agents, le vrai livrable est la configuration qui encode le savoir métier de l'utilisateur, pas le moteur d'exécution. Le moteur est générique et réutilisable ; la valeur est dans la séparation explicite entre ce qui est stable (la procédure) et ce qui est personnel (les critères, les seuils, le vocabulaire).

Signaux positifs : prompt écrit en langage métier, séparation config/moteur, paramètres nommés.
Signaux négatifs : logique métier en dur dans le code, prompt technique incompréhensible par l'utilisateur final.

### 1.5 Autonomie progressive

Le livrable final n'est pas un résultat mais un transfert de capacité. Le chemin va de "je fais pour toi" à "tu fais seul avec l'outil que je t'ai laissé". Commencer par le cas le plus simple qui démontre le mécanisme, accepter les contraintes du moment, élargir ensuite.

Signaux positifs : prompt réutilisable livré, plugin packageable, démo avant automatisation.
Signaux négatifs : dépendance créée, complexité prématurée, sur-ingénierie.

### 1.6 Feedback sans intermédiaire

L'information doit atteindre l'entité qui en a besoin par le chemin le plus court. Tout circuit qui ajoute une étape entre l'émetteur et le récepteur du feedback est suspect. Les limites d'un système doivent être explicites dans sa sortie, pas cachées dans un résultat agrégé.

Signaux positifs : canal direct, limites explicites, erreurs surfacées.
Signaux négatifs : circuit indirect, résultat agrégé sans détail, limites cachées.

---

## Couche 2 — Patterns de fabrication

Comment le travail est construit dans l'outil.

### 2.1 Construire des outils, pas des livrables

Le travail porte sur la couche qui produit le résultat, pas sur le résultat lui-même. Le livrable visible (un PDF, un Excel, un briefing) est le test du vrai livrable (un module Python, un prompt, un plugin).

Signaux positifs : le résultat est un sous-produit d'un outil réutilisable.
Signaux négatifs : livrable unique sans couche de réutilisation.

### 2.2 Exploration parallèle puis merge

Plusieurs versions coexistent, chacune explorant une direction différente. La convergence se fait par merge sélectif, pas par progression linéaire. Chaque branche apporte des capacités distinctes.

Signaux positifs : versions concurrentes, merge explicite, comparaison des apports.
Signaux négatifs : une seule version itérée linéairement sans exploration.

### 2.3 Savoir théorique encodé en code exécutable

La connaissance de domaine (typographie, grilles, analyse financière) est transformée en méthodes, en scripts, en configurations qui la rendent calculable. Le savoir ne reste pas dans la tête, il devient du code.

Signaux positifs : théorie → méthodes Python, règles de domaine → paramètres de config.
Signaux négatifs : savoir implicite non formalisé, décisions ad hoc sans règle sous-jacente.

### 2.4 Fichier unique autonome

L'unité de travail est le fichier qui contient tout ce qu'il faut pour fonctionner. Résistance à la décomposition en petits fichiers.

Signaux positifs : un HTML, un module, un prompt. Tout dans un seul fichier.
Signaux négatifs : fragmentation en micro-fichiers sans justification.

### 2.5 Méta-outils

Construire l'outil et la machine qui permet d'en construire d'autres. Le skill qui crée des skills. Le prompt qui configure l'agent. L'onboarding qui génère la configuration personnelle.

Signaux positifs : le livrable permet de produire d'autres livrables similaires.
Signaux négatifs : livrable terminal sans capacité de reproduction.

---

## Couche 3 — Patterns de pilotage

Comment le processus est dirigé en conversation.

### 3.1 Itération par rejet

Le feedback est soustractif : dire ce qui ne va pas, pas ce qu'on veut. La direction est donnée par élimination, pas par spécification. Confiance dans le prochain cycle pour converger.

### 3.2 Reprise en main

Quand l'itération patine, proposer soi-même la formulation ou la solution au lieu de re-briefer. Utiliser l'agent comme surface de rebond, pas comme exécutant.

### 3.3 Couper les détours

Recadrer immédiatement quand l'exploration s'éloigne du chemin le plus court. Changer d'approche plutôt que de déboguer un chemin compliqué.

### 3.4 Demander le méta

Comprendre la logique sous-jacente, les hypothèses de fonctionnement, les modes d'échec, avant d'investir dans l'itération suivante. "Quelles sont les conditions pour que ça marche ?"

### 3.5 Penser distribution

Dès qu'un cas particulier fonctionne, penser à le généraliser. "Comment je file ça à un ami ?"

### 3.6 Synthèse à voix haute

Reformuler ce qu'on a compris dans ses propres termes pour vérifier la représentation mentale avant de proposer quoi que ce soit.

---

## Journal de calibration

| Date | Session | Principe | Observation | Verdict |
|------|---------|----------|-------------|---------|
| — | — | — | (aucune entrée encore) | — |
