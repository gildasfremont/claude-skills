# Tics des textes générés (français)

Le signal n'est pas la présence d'un procédé mais sa répétition et son automatisme. Compter, puis remplacer l'effet par une information. `scripts/lint.py` fait les comptes ; ce fichier dit quoi faire de chaque signalement.

Seuils pour 1 000 mots (au-delà, corriger jusqu'à passer dessous) : tirets 0 ; antithèses 1 ; triades 2 ; phrases de moins de six mots 2 ; connecteurs automatiques 3 ; adverbes de renforcement 0 ; mots d'emphase 1 ; adjectifs d'appréciation (difficile, complexe, fluide, robuste, ambitieux) 3, chacun à convertir en scène ou en mesure ; "on" de substitution 0 ; clivées "ce qui..., c'est" 1 ; questions rhétoriques 0 ; mots de brochure 2.

## 1. Tiret en incise

Repérer : cadratin, demi-cadratin, ou trait d'union entouré d'espaces. Réécrire : virgule pour une incise courte, parenthèses pour une précision qu'on pourrait sauter, deux-points pour une explication, deux phrases pour le reste. Après suppression des tirets, vérifier qu'il ne reste pas une cascade de deux-points ou d'incises entre virgules dans la même phrase (item 19).

## 2. Triade

Repérer : trois adjectifs, trois exemples, trois membres coordonnés par "et", surtout en fin de phrase. Réécrire : garder l'élément qui porte le fait ; si la liste réelle a quatre ou cinq éléments, les donner tous. La réalité ne vient pas par trois.
Avant : Une solution robuste, lisible et évolutive.
Après : Un modèle que l'administrateur d'une ETI configure sans ticket au support.

## 3. Antithèse

Repérer : "ce n'est pas X, c'est Y" et ses variantes : "non pas X mais Y", "il ne s'agit pas de X mais de Y", "pas seulement X, aussi Y", "au-delà de X", "plus qu'un X", "ne se limite pas à". Réécrire : écrire Y avec son fait. Ne garder X que si quelqu'un de nommé l'a cru ("le PM maison voulait simplifier l'écran ; le problème tenait au modèle").
Avant : Ce n'était pas un simple outil de conformité, c'était un changement de culture.
Après : L'outil de conformité a changé la façon dont les équipes juridiques traitaient les déclarations au quotidien.

## 4. Phrase nominale d'effet

Repérer : fragment de moins de six mots, sans verbe conjugué, posé seul entre deux points. Réécrire : le rattacher à la phrase précédente par deux-points ou une virgule, ou lui donner sujet et verbe.
Avant : Un vrai tournant.
Après : À partir de là, le solveur a recalculé les cibles à chaque changement de prévision.

## 5. Chute, maxime, retour au titre

Repérer : dernière phrase d'un paragraphe ou d'un texte dont le sujet est un nom abstrait, ou qui reformule une idée déjà dite, ou qui reprend le titre. Réécrire : terminer sur le dernier fait.

## 6. Commentaire et annonce

Repérer : "ce qui est intéressant", "il est important de", "notons que", "on voit que", "cela montre", "ce projet illustre", "autrement dit", "en d'autres termes", "dans cet article", "ce que j'ai appris", "la leçon", "ce qui compte". Supprimer la phrase. Si elle portait un fait, garder le fait sans le commentaire.

## 7. Emphase

Repérer : crucial, clé, majeur, massif, essentiel, incontournable, véritable, réel (adjectif), profond, fort (pour une idée), puissant, indispensable, déterminant, stratégique. Réécrire : supprimer, ou remplacer par la mesure.
Avant : Un projet crucial aux enjeux massifs.
Après : Sans ce système, la facturation restait manuelle pour 400 sites.

## 8. Adverbes de renforcement

Liste dans le tronc. Supprimer. Vérifier que la phrase tient ; si elle ne tient plus, c'est l'assertion qui était faible, pas l'adverbe qui manque.

## 9. Connecteurs automatiques

Repérer : en effet, par ailleurs, ainsi, de plus, en outre, dès lors, c'est pourquoi, dans ce contexte, dans le cadre de, il convient de, force est de constater, d'une part / d'autre part. Test de suppression (`publication.md`).

## 10. Vocabulaire de brochure

Repérer : accompagner, démarche, approche, enjeu, levier, écosystème, valeur ajoutée, impact sans mesure, vision, transformation, dynamique, synergie, agile, excellence, passion, solution pour désigner un produit. Réécrire avec le nom concret : le catalogue, l'import, la facture, le rôle Manager, le pont-bascule.

## 11. Question rhétorique et faux suspense

Repérer : "Que faire ?", "Et si...", "La suite allait le montrer", "Pourquoi ?" seul, "Résultat ?". Réécrire : donner la réponse dans la phrase.

## 12. Métaphore décorative

Repérer : chantier, voyage, aventure, boussole, pont, fil rouge, pierre angulaire, bataille, tempête, cap, jungle. Réécrire avec le mot propre. Termes de métier admis : brique logicielle, socle RH, feuille de route.

## 13. Anaphore et parallélisme

Repérer : trois phrases qui commencent par le même mot ; "Pas de X. Pas de Y. Pas de Z." ; deux phrases construites en miroir. Réécrire en une phrase avec les faits.

## 14. Clivée

Repérer : "ce qui compte, c'est", "ce que je sais, c'est", "ce qui a changé, c'est", "le problème, c'est". Une par texte au plus. Réécrire à l'ordre direct : "Ce que je sais, c'est ce qui a changé dans le modèle" devient "Deux choses ont changé dans le modèle".

## 15. Symétrie de gabarit

Repérer : paragraphes de même longueur, sections de même structure, chaque section qui se ferme par une phrase de bilan. Le linter ne le voit pas ; regarder les longueurs de paragraphes et les dernières phrases de section. Couper ce qui remplit.

## 16. Récapitulation

Repérer : "pour résumer", "en somme", "au final", "finalement" en tête d'un dernier paragraphe, "in fine". Supprimer le paragraphe ; remonter le fait s'il y en avait un.

## 17. Paire d'adjectifs qui se couvrent

Repérer : "simple mais puissant", "sobre et précis", "ambitieux mais réaliste", "rapide et fiable". Réécrire avec un seul adjectif, ou le fait qui le prouve.

## 18. Ancrage temporel creux

Repérer : "aujourd'hui" sans date derrière, "désormais", "à l'heure où", "à l'ère de", "dans un monde où", "plus que jamais", "de nos jours". Supprimer ou dater. "Aujourd'hui" est admis quand il oppose un état présent à un état passé daté.

## 19. Incises en chaîne

Repérer : deux deux-points dans une phrase, ou trois incises entre virgules, ou parenthèses dans une incise. C'est la trace d'une réécriture LLM après interdiction du tiret. Une incise par phrase ; couper.

## 20. Verbe de bilan avec le projet pour sujet

Repérer : "ce projet montre / illustre / démontre / révèle / prouve", "cette mission témoigne de". Supprimer la phrase entière.

## 21. Qualité auto-attribuée

Repérer : "avec rigueur", "j'ai fait preuve de", "mon sens de", "ma capacité à", "passionné", "curieux", "orienté résultats". Supprimer et laisser le fait qui aurait dû la prouver.

## Après le linter

Un texte propre selon le linter peut encore sonner artificiel par sa symétrie (item 15), ses métaphores (item 12) et ses fins de section (item 5). Relire ces trois points à l'œil sur tout le texte, pas seulement sur les passages signalés.
