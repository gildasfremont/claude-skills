# Relecture avant livraison

Une passe à la fois, dans cet ordre. Ne pas mélanger le fond et la forme : réécrire un beau paragraphe qui ne montre aucune décision ne sert à rien.

## 0. Linter

`python3 scripts/lint.py texte.md`, ou le texte sur stdin. Lire le rapport en entier. Chaque ligne signalée est traitée : corrigée, ou gardée avec une raison. Les seuils sont dans `tics-ia.md`. Relancer après correction jusqu'à ce que les lignes "À CORRIGER" disparaissent ou soient toutes justifiées.

## 1. Fond

Pour chaque section, écrire mentalement une ligne : quelle décision, quel fait ? Si la ligne est "contexte" ou "transition", la section ne tient pas seule. Supprimer toute phrase dont le retrait ne fait perdre aucun fait au lecteur. Vérifier que le chapeau ou la première phrase tient seul. Dans une étude de cas, vérifier que la section Options contient une alternative écartée avec sa raison.

## 2. Faits

Chaque chiffre, date, nom, effectif, résultat : établi, à confirmer ou trou ? Marquer entre crochets ce qui n'est pas établi. Comparer avec la fiche du dépôt ~/dev/job-hunting quand elle existe. Vérifier la liste des faits interdits (tronc, section Faits). Vérifier le statut de livraison de chaque cas : livré, conçu et remis, ou proposé.

## 3. Registre

- Chaque "on" : test de substitution (`publication.md`).
- Chaque "nous" : qui ? nommé dans la section ?
- Chaque évaluation (adjectif d'appréciation, verbe de bilan) : convertie en scène ou supprimée.
- Ouverture et fermeture de chaque paragraphe : commentaire, annonce, maxime ? Supprimer.
- Dernière phrase du texte : nom concret, chiffre ou date ?
- Aucune qualité auto-attribuée.

## 4. Phrase

- Longueur : phrases de moins de sept mots à rattacher, phrases de plus de trente-cinq mots à couper à la deuxième subordonnée.
- Nominalisations (mise en place de, réalisation de, mise en œuvre de) : verbe.
- Passifs sans agent : acteur.
- Adverbes de renforcement : retirer.
- Connecteurs : test de suppression.
- Première phrase de chaque paragraphe : porte-t-elle le fait principal ?

## 5. Tics

Relire les items de `tics-ia.md` sur les passages signalés par le linter, puis à l'œil ce que le linter ne voit pas : symétrie des paragraphes, sections qui se ferment toutes de la même façon, métaphores, incises en chaîne.

## 6. Langue

Tables de `anglicismes.md`. Typographie française : espaces insécables, guillemets, nombres, majuscules.

## 7. Voix haute

Relire chaque phrase comme si elle était dite à la personne visée. Toute phrase qu'on ne dirait pas ainsi est réécrite. Lire une section entière d'un trait : pas de staccato, pas de phrase où l'on manque de souffle.

## 8. Livraison

Le texte, puis à part la liste des crochets restants avec ce qu'il faudrait pour les lever. Pas de récit des passes, pas de "j'ai veillé à", pas de résumé des choix de style. Si le texte modifie un document existant, dire seulement ce qui a changé, par remplacement ciblé.
