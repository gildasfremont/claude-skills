# Règles pratiques de typographie

Règles ancrées dans des principes premiers (optique, physiologie de la lecture, construction des caractères) ou validées par le Lindy effect (si ça marche depuis 50+ ans, c'est que c'est solide). Pas de mystique, pas de "règles de design" inventées par des blogs.

---

## Serif vs Sans-serif — la vraie différence

La distinction fondamentale est optique, pas esthétique.

**Les empattements (serifs) créent une ligne de base visuelle continue.** L'œil suit cette ligne horizontale implicite, ce qui facilite la lecture de longues lignes de texte. C'est pour ça que les livres imprimés utilisent du serif depuis 500 ans — le Lindy effect est écrasant.

**Les sans-serif ont des formes plus simples avec moins de détails fins.** Elles résistent mieux à la dégradation (petites tailles, écrans basse résolution, impression médiocre). C'est pour ça que le web a convergé vers le sans-serif pour le corps — les écrans avaient longtemps une résolution insuffisante pour rendre les empattements correctement.

**Aujourd'hui (écrans haute résolution), la distinction s'estompe.** Une bonne serif fonctionne parfaitement en corps sur un écran Retina. Le choix entre serif et sans-serif est donc redevenu principalement un choix de registre expressif, pas une contrainte technique.

Principe premier : le serif aide la lecture horizontale longue (print, articles), le sans-serif est plus robuste aux conditions dégradées (petites tailles, écrans, signalétique). Sur un bon écran en 2024+, les deux marchent en corps.

---

## Le "a" et le "g" — pourquoi c'est important

Les lettres "a" et "g" existent chacune en deux formes :
- **Simple étage (single-storey)** : le "a" rond comme un "o" avec une queue, le "g" comme un cercle avec un crochet
- **Double étage (double-storey)** : le "a" avec un arc au-dessus d'un ventre, le "g" avec deux boucles

**En romain (regular/bold)**, les deux formes sont acceptables. Le simple étage est plus géométrique (Futura, Circular), le double étage plus traditionnel et lisible en petit (parce que la forme est plus distinctive, donc plus facile à reconnaître rapidement).

**En italique, le "a" simple étage est la norme typographique.** Une bonne italique est calligraphique — elle imite le mouvement de la main. Le "a" double étage en italique est un signal fort que la police est construite mécaniquement (juste penchée) plutôt que dessinée comme une vraie italique. Ce n'est pas "interdit" mais c'est un marqueur de qualité : les polices sérieuses ont un "a" simple étage en italique. Si tu vois un "a" double étage en italique, la police est soit cheap, soit elle fait un choix délibéré (auquel cas elle assume et c'est OK).

Pourquoi ça compte : c'est un test rapide de la qualité d'une police. Regarde l'italique — si le "a" est juste le romain penché, la police n'a probablement pas été dessinée avec soin.

---

## Contraste des fûts (stroke contrast)

Le contraste entre les traits épais et fins d'une lettre est le principal levier expressif d'une police.

**Faible contraste** (traits d'épaisseur uniforme) → signal de modernité, simplicité, robustesse. Les sans-serif ont généralement un faible contraste. Fonctionne bien à toutes les tailles.

**Fort contraste** (traits épais + empattements fins) → signal de luxe, drama, formalisme. Les Didones (Bodoni, Didot) maximisent ce contraste. **Problème : en petit corps, les traits fins disparaissent.** C'est un principe optique, pas une question de goût. Bodoni en 12px sur écran, les empattements sont en dessous du pixel. Résultat : illisible.

Règle : le contraste élevé fonctionne en grand (titrage, affiches). En corps, il faut un contraste modéré (transitionnelles comme Baskerville) ou faible (sans-serif, slab serif).

---

## X-height (hauteur d'œil)

La x-height est la hauteur des lettres minuscules sans ascendantes ni descendantes (le "x", le "o", le "e"). C'est LE facteur de lisibilité en petit corps.

**Grand x-height** = plus lisible en petit, aspect plus large et ouvert. Inter, Roboto, Söhne ont un grand x-height. C'est pour ça qu'elles fonctionnent bien en UI.

**Petit x-height** = aspect plus élégant, plus "classique", plus d'espace entre les lignes. Garamond, Bembo ont un petit x-height. Fonctionnent en print à bonne taille mais souffrent en petit sur écran.

Quand on apparie deux polices : vérifier que leurs x-heights sont compatibles. Deux polices avec des x-heights très différents vont sembler incohérentes côte à côte, même à la même taille nominale.

---

## Contreformes (counters) et ouvertures (apertures)

Les contreformes sont les espaces intérieurs des lettres (le trou du "o", du "e", du "a"). Les ouvertures (apertures) sont les espaces où la lettre n'est pas fermée (l'ouverture du "c", du "e", du "s").

**Contreformes larges + ouvertures grandes** = meilleure lisibilité. L'œil distingue les lettres par leurs espaces intérieurs autant que par leurs traits. Plus les espaces sont ouverts, plus vite le cerveau identifie la lettre.

C'est pour ça que les polices optimisées pour la lisibilité (Frutiger, Source Sans, Inter) ont des ouvertures très généreuses. C'est aussi pour ça que Helvetica, malgré sa réputation, est médiocre en corps texte long : ses ouvertures sont fermées (le "c" et le "e" se ressemblent trop).

Test rapide de lisibilité en corps : regarde le "e" minuscule. Si l'ouverture est large et franche, la police est probablement bonne en corps. Si elle est étroite et presque fermée, la police est mieux en titrage.

---

## Optical size — Text vs Display

Beaucoup de familles de qualité existent en deux versions : Text (optimisée pour le corps) et Display (optimisée pour le titrage). Ce ne sont PAS les mêmes dessins à des tailles différentes.

Différences concrètes :
- **Text** : x-height plus grand, contreformes plus ouvertes, contraste réduit, espacement plus large, traits fins plus épais (pour qu'ils ne disparaissent pas en petit)
- **Display** : contraste augmenté, détails plus fins, espacement plus serré (en grand les lettres doivent être rapprochées), formes plus expressives

**Utiliser une Display en corps** = les traits fins vont disparaître, l'espacement sera trop serré, la lecture sera fatigante. C'est une erreur technique, pas une question d'opinion.

**Utiliser une Text en titrage** = pas catastrophique mais la police va sembler terne, avec trop d'espacement. Elle ne "remplit" pas l'espace comme elle le devrait.

Familles avec distinction Text/Display : Tiempos, Domaine, GT Sectra, Miller, Freight, Playfair.

---

## Graisses et hiérarchie

La hiérarchie typographique (ce qui est important → ce qui est secondaire) se construit avec 3 leviers : taille, graisse, et contraste de style (serif vs sans).

**Règle des 2 niveaux minimum de différence.** Pour que deux niveaux hiérarchiques soient clairement distincts, il faut au moins 2 degrés de graisse d'écart (ex: Regular pour le corps, Bold pour les titres — pas Regular vs Medium, qui sont trop proches). Ou combiner un changement de graisse avec un changement de taille.

**Gras ≠ important.** Le gras attire l'œil, donc il hiérarchise. Mais dans un texte courant, trop de gras annule l'effet (si tout est important, rien ne l'est). Réserver le gras pour la structure (titres, sous-titres) et l'emphase ponctuelle.

**L'italique est pour l'emphase dans le texte courant.** Pas pour les titres (sauf choix stylistique assumé). L'italique en titrage signale souvent une intention calligraphique ou une élégance recherchée — mais c'est un registre spécifique.

---

## Espacement et rythme

L'espacement entre les lettres (tracking/letter-spacing) et entre les lignes (leading/line-height) affecte la lisibilité autant que le choix de police.

**Corps de texte** : line-height entre 1.4 et 1.6 (pour le web). Longueur de ligne idéale : 45-75 caractères. Au-delà de 80 caractères, l'œil perd la ligne au retour. En dessous de 35, le rythme de lecture est saccadé.

**Titrage en grande taille** : resserrer le tracking. Les lettres en gros ont trop d'espace entre elles par défaut (le spacing est conçu pour le corps). En display, on réduit le tracking pour que les lettres forment un bloc visuellement cohérent. C'est un ajustement optique standard, pas une astuce.

**Capitales** : augmenter légèrement le tracking. Les capitales sont dessinées pour coexister avec des minuscules. En texte tout-en-capitales, elles sont trop serrées. Un tracking augmenté de 2-5% améliore la lisibilité et le registre visuel.

---

## Les vrais critères de qualité d'une police

Quand tu évalues une police, voici ce qui sépare une police sérieuse d'une police amateur :

1. **Vraie italique** (pas juste le romain penché — oblique ≠ italic). Le "a", le "e", le "f" changent de forme en italic.
2. **Kerning soigné** — les paires de lettres problématiques (AV, To, LT, VA) sont correctement ajustées.
3. **Hinting** (pour le web) — la police rend bien à toutes les tailles sur tous les OS.
4. **Jeu de caractères complet** — au minimum les accents français (é, è, ê, ë, à, ç, œ, etc.), idéalement Latin Extended.
5. **Plusieurs graisses** — minimum Regular, Italic, Bold. Idéalement Light à Black avec italiques.
6. **Métriques cohérents** — les chiffres alignent, le spacing est régulier, les graisses progressent de manière harmonieuse.
7. **Chiffres tabulaires et proportionnels** — les deux options existent pour les tableaux (tabulaires) et le texte courant (proportionnels).

---

## Licence — ce qu'il faut savoir

- **Google Fonts / Open Font License** : gratuit pour tout usage, commercial inclus.
- **Fonderie indépendante** : licence par usage (desktop, web, app). Desktop ~50-200€ par graisse, souvent des packs famille ~100-500€. Web souvent en plus.
- **Adobe Fonts** : inclus dans l'abonnement Creative Cloud. Pas utilisable sans abo.
- **Variable fonts** : un seul fichier, souvent une seule licence pour toutes les graisses. Économique.
- **Attention** : "free for personal use" ≠ gratuit pour un site commercial. Vérifier la licence.
