# Fondamentaux techniques de la typographie

Référence de niveau expert. Chaque définition vise la précision mécanique, pas la vulgarisation. Organisé du plus concret (anatomie d'une lettre) au plus abstrait (systèmes de classification).

---

## 1. Anatomie du caractère

### Lignes de référence verticales

Le système de positionnement vertical d'un caractère repose sur cinq lignes :

- **Ligne de base (baseline)** : ligne invisible sur laquelle reposent les lettres. Point d'ancrage de l'alignement horizontal. Les descendantes passent en dessous.
- **Hauteur d'x (x-height / hauteur d'oeil)** : distance entre la ligne de base et le sommet des minuscules sans ascendante (x, o, e, a). Détermine la taille apparente d'une police. Facteur principal de lisibilité en petit corps.
- **Ligne des capitales (cap height)** : sommet des capitales à bord plat (H, I, E). Souvent légèrement inférieure à la ligne des ascendantes.
- **Ligne des ascendantes (ascender line)** : sommet atteint par les fûts ascendants (b, d, f, h, k, l). Peut dépasser la cap height.
- **Ligne des descendantes (descender line)** : point le plus bas atteint par les descendantes (g, j, p, q, y).

### Dépassement optique (overshoot)

Les formes rondes (O, C, S, o, e) et pointues (A, V, W) dépassent la ligne de base vers le bas et la cap height / x-height vers le haut d'environ 1 à 3 %. Sans ce dépassement, elles paraissent plus petites que les lettres à bord plat. C'est une correction optique, pas une erreur de dessin : l'égalité mathématique ne produit pas l'égalité visuelle.

### Éléments structurels principaux

- **Fût (stem)** : trait vertical principal d'une lettre. Trait le plus épais dans une police à contraste.
- **Trait (stroke)** : toute ligne composant un caractère, droite ou courbe.
- **Panse (bowl)** : trait courbe enfermant une contreforme. Présent dans b, d, o, p, g, q.
- **Contreforme (counter)** : espace intérieur d'une lettre, fermé (o, d, p) ou ouvert (n, c, u). La taille des contreformes est un facteur majeur de lisibilité.
- **Ouverture (aperture)** : espace où la lettre n'est pas fermée — l'ouverture du c, du e, du s. Des ouvertures larges favorisent la distinction rapide des lettres.
- **Traverse (crossbar)** : trait horizontal reliant deux fûts (H, A) ou traversant un fût (e, f, t).
- **Épaule (shoulder)** : courbe reliant un fût à un autre trait (arc du n, du h, du m).
- **Dos / épine (spine)** : courbe centrale du S.
- **Queue (tail)** : trait descendant du Q, du R, du y.
- **Oreille (ear)** : petit trait en saillie au sommet du g binoculaire.
- **Bras (arm)** : trait horizontal ou montant libre à une extrémité (barres du T, diagonales du Y).
- **Jambe (leg)** : trait descendant libre à une extrémité (diagonale basse du K, du R).

### Jonctions et angles

- **Apex** : jonction où deux traits se rencontrent en haut (sommet du A, du M).
- **Vertex** : jonction où deux traits se rencontrent en bas (creux du V, du W).
- **Crotch** : angle intérieur à la jonction de deux traits, typiquement aux vertex.

### Formes terminales (terminals)

Terminaisons des traits dans les polices sans empattement ou aux extrémités courbes des polices avec empattement :

- **Boule (ball terminal)** : terminaison circulaire ou sphérique. Caractéristique des Didones (Bodoni, Didot).
- **Bec (beak terminal)** : terminaison pointue en forme de bec d'oiseau. Fréquente sur les traits horizontaux (E, L) et les courbes (a, c, f, r).
- **Goutte (teardrop / lachrymal terminal)** : forme de goutte d'eau, large à une extrémité, effilée à l'autre. Fréquente dans les serif humanistes.
- **Terminaison effilée (finial)** : extrémité courbe amincie. Bas du C, ouverture du e.

### Types d'empattements (serifs)

- **Empattement raccordé (bracketed)** : transition courbe entre l'empattement et le fût. Fluidité visuelle. Caractéristique des Garaldes et Transitionnelles.
- **Empattement non raccordé (unbracketed)** : jonction directe, perpendiculaire. Aspect rationnel, moderne. Caractéristique des Didones.
- **Empattement rectangulaire (slab)** : épais, bloc, poids proche du fût. Aspect mécanique. Caractéristique des Mécanes (Rockwell, Clarendon).
- **Empattement cunéiforme (wedge)** : triangulaire, évoquant la gravure. Caractéristique des Glyphiques (Trajan).
- **Empattement filiforme (hairline)** : extrêmement fin par rapport au fût. Contraste maximal. Caractéristique des Didones (Bodoni, Didot).

### Éléments complémentaires

- **Lien (link)** : trait reliant la panse et la boucle du g binoculaire (double étage).
- **Boucle (loop)** : contreforme inférieure du g binoculaire, sous la ligne de base.
- **Lobe** : panse à extrémité plate (D, P). Parfois synonyme de boucle pour le g.
- **Oeil (eye)** : contreforme fermée du e minuscule (partie supérieure spécifiquement).

---

## 2. Systèmes de mesure typographiques

### Systèmes de points

Trois systèmes de points coexistent historiquement :

**Point Didot** (standard continental européen) : défini par François-Ambroise Didot comme 1/72 du pouce de Paris. 1 point Didot = 0,376 mm. 12 points Didot = 1 cicéro = 4,512 mm.

**Point anglo-américain** (standard anglo-saxon) : établi par l'United States Type Founders' Association en 1886. 1 point = environ 1/72,27 pouce. 12 points = 1 pica = 4,217 mm.

**Point PostScript** (standard numérique universel) : standardisé par Adobe. 1 point = exactement 1/72 de pouce = 0,3528 mm. 12 points = 1 pica = exactement 1/6 de pouce = 4,233 mm. C'est le standard dans tous les logiciels de conception actuels.

### Unités relatives

**Em** : unité proportionnelle à la taille du corps. Dans un corps de 12 points, 1 em = 12 points. L'em est un carré dont le côté est la taille nominale du caractère. Historiquement, la largeur du M majuscule ; en pratique, c'est le cadre de référence du dessin de caractères.

**En** : moitié d'un em. Utilisé pour le tiret demi-cadratin et certains espacements.

**Cadratin (em quad)** : en composition au plomb, pièce de métal carrée (épaisseur = corps) servant d'espace large. Équivalent physique de l'em.

### Système d'unités Monotype

Le système Monotype divisait l'em en 18 unités. Chaque caractère se voyait attribuer une chasse (set width) de 5 à 18 unités, 18 unités = 1 em. Ce système permettait un espacement proportionnel précis en composition chaude.

### UPM (Units Per Em) — mesure numérique

L'UPM est la résolution de la grille de dessin d'une police numérique. Tous les contours de glyphes, les chasses, les approches et les valeurs de crénage sont exprimés dans ces unités.

**PostScript / OpenType CFF** : 1000 UPM (standard).
**TrueType / OpenType TTF** : 2048 UPM (standard ; puissance de 2, favorable au calcul entier).
**Maximum autorisé** : 16 384 pour TrueType/OpenType.

La mise à l'échelle fonctionne ainsi : pour un corps de 12 pt dans une police à 1000 UPM, 1 unité = 0,012 pt. Toutes les coordonnées du fichier sont des entiers dans cet espace.

### Table de conversion

| Unité | PostScript | Métrique | Didot |
|---|---|---|---|
| 1 point | 1 pt | 0,3528 mm | 0,935 pt Didot |
| 1 pica (12 pt) | 12 pt | 4,233 mm | 11,22 pt Didot |
| 1 pouce | 72 pt | 25,4 mm | 67,93 pt Didot |
| 1 cicéro | 12,84 pt | 4,512 mm | 12 pt Didot |

---

## 3. Mécanique de l'espacement

### Approches (sidebearings)

Chaque glyphe possède une approche gauche et une approche droite : l'espace invisible intégré de chaque côté du dessin. La chasse (advance width) d'un caractère se calcule :

**Chasse = approche gauche + largeur du glyphe + approche droite**

En composition numérique, les approches peuvent être négatives (le glyphe dépasse de son espace — impossible en plomb sans kerns physiques). La qualité des approches détermine la « couleur typographique » du texte (la densité visuelle uniforme d'un bloc de texte vu de loin).

### Crénage (kerning) vs. approche de groupe (tracking)

**Crénage** : ajustement de l'espacement entre deux caractères spécifiques. Opère au niveau de la paire. Corrige les problèmes optiques créés par la géométrie de certaines combinaisons (AV, To, LT, VA, fy). Stocké dans le fichier de police.

**Tracking** : ajustement uniforme de l'espacement sur une plage de caractères (mot, ligne, paragraphe). Paramètre de mise en page, pas de la police elle-même.

Le crénage corrige des problèmes locaux ; le tracking ajuste la densité globale.

### Crénage par paires vs. par classes

**Par paires** : chaque combinaison de deux caractères reçoit une valeur individuelle. Un fichier peut contenir des milliers de paires. Précis mais volumineux.

**Par classes** : les caractères partageant le même profil de crénage d'un côté sont groupés (ex. C, G, O partagent le même contour droit). Le crénage est défini entre classes, pas entre glyphes individuels. Réduit la taille du fichier, garantit la cohérence. Méthode standard dans les polices professionnelles.

### Encodage dans le fichier de police

**Table kern** (format historique) : stocke les paires de crénage en format simple. Compatible mais limité.

**Table GPOS** (Glyph Positioning, format moderne) : table OpenType Layout qui gère tout le positionnement des glyphes, y compris le crénage contextuel (ajustements qui varient selon le contexte textuel). Nécessite un moteur de mise en forme (shaping engine) comme HarfBuzz. Supporte le crénage par classes et le crénage contextuel.

### Crénage métrique vs. crénage optique

**Métrique** : utilise les données de crénage intégrées au fichier de police — les choix délibérés du dessinateur.

**Optique** : algorithme qui analyse la géométrie réelle des glyphes et ajuste l'espacement indépendamment de la table de crénage. Utile quand la police a un crénage déficient ou quand on mélange des polices différentes.

### Couleur typographique

La « couleur » d'un bloc de texte désigne sa densité tonale globale — la valeur de gris perçue quand on regarde le texte de loin ou en plissant les yeux. Une couleur uniforme signifie un espacement bien calibré. Des zones sombres ou claires signalent des problèmes d'approche, de crénage, d'interligne ou de chasse.

---

## 4. Composition des lignes

### Interligne (leading)

Le terme vient de la composition au plomb : les compositeurs inséraient des lames de plomb (leads) entre les lignes de caractères pour ajouter de l'espace vertical. En numérique, l'interligne mesure la distance de ligne de base à ligne de base.

Règle empirique : interligne environ 120 à 150 % du corps (1,4 à 1,6x la taille nominale en web). L'interligne doit augmenter avec la longueur de ligne pour que l'oeil retrouve le début de la ligne suivante après la saccade de retour.

### Longueur de ligne (mesure)

Bringhurst (The Elements of Typographic Style) établit l'optimum à 66 caractères par ligne (espaces compris), avec une plage acceptable de 45 à 75 caractères pour une colonne simple en police de labeur avec empattements.

**Base physiologique** : au-delà de 75-80 caractères, l'oeil perd le début de la ligne suivante pendant la saccade de retour, ce qui provoque fatigue et perte de compréhension. En dessous de 35 caractères, les retours à la ligne trop fréquents cassent le rythme de lecture.

Pour les mises en page multi-colonnes, viser 40-50 caractères par colonne.

### Espacement des mots

L'espacement des mots doit être cohérent au sein d'une ligne et raisonnablement stable d'une ligne à l'autre pour maintenir une couleur typographique uniforme. En texte justifié, la variation de l'espace mot devient le problème central.

### Algorithmes de justification

**Algorithme glouton (greedy)** : remplit chaque ligne au maximum de gauche à droite. Décisions locales, irréversibles. Produit des variations d'espacement sous-optimales.

**Algorithme Knuth-Plass** (TeX) : programmation dynamique qui optimise l'espacement sur un paragraphe entier simultanément. Modélise le texte comme trois types d'objets :
- **Boîtes (boxes)** : contenu non redimensionnable (mots, lettres)
- **Colle (glue)** : espacement flexible (espaces mots, espaces lettres), avec largeur idéale, extensibilité et compressibilité
- **Pénalités (penalties)** : coût esthétique des points de coupure (coupure de mot = pénalité positive)

L'algorithme minimise une fonction de « laideur » (badness) cumulée sur toutes les lignes du paragraphe. Résultat : justification visuellement supérieure parce qu'elle équilibre les contraintes globalement, pas ligne par ligne.

### Césure (hyphenation)

La césure réduit les problèmes d'espacement en permettant de couper les mots en fin de ligne. Contrainte : éviter plus de deux ou trois lignes consécutives se terminant par un trait d'union. La qualité de la césure est souvent intégrée à l'algorithme de justification.

### Défauts de composition

**Lézardes (rivers)** : alignement vertical ou quasi-vertical d'espaces mots sur plusieurs lignes consécutives, créant une « fissure » blanche dans le texte. Plus visibles en texte justifié à espacement large.

**Veuve (widow)** : dernière ligne d'un paragraphe isolée en haut d'une page ou d'une colonne.

**Orphelin (orphan)** : première ligne d'un paragraphe isolée en bas d'une page ou d'une colonne.

**Drapeau (rag)** : en composition en drapeau (fer à gauche, drapeau à droite), le bord irrégulier doit varier sans créer de formes visuellement marquées. Un bon drapeau a des variations modérées et irrégulières.

---

## 5. Ajustements optiques dans le dessin de caractères

### Centre optique vs. centre géométrique

Le centre géométrique d'un rectangle est à 50 % de la hauteur. Le centre optique se situe environ à 46 % depuis le haut. Les éléments placés au centre géométrique paraissent trop bas. En dessin de caractères, la traverse du H est légèrement au-dessus du milieu géométrique pour paraître centrée.

### Illusion d'épaisseur des traits horizontaux

Un trait horizontal est perçu comme environ 5 % plus épais qu'un trait vertical de même largeur (illusion vérifiée expérimentalement sur 27 sujets sur 28). Conséquence : dans toute police bien dessinée, les traits horizontaux sont légèrement plus fins que les verticaux. Si le fût vertical mesure 100 unités, le trait horizontal mesure typiquement 90-95 unités pour paraître de poids égal.

### Compensation du contraste

Dans le dessin des courbes et des diagonales, l'épaisseur du trait varie optiquement. Le « o » minuscule a des segments verticaux plus épais que ses segments horizontaux, mais cette différence est invisible à l'oeil quand la lettre est correctement dessinée. Si on la tourne de 90 degrés, la différence devient évidente.

### Pièges à encre (ink traps)

Encoches concaves creusées aux jonctions intérieures des traits (apex du A, jonction de diagonales). Fonction : à petites tailles en impression offset, l'encre diffuse et remplit les jonctions. Les pièges à encre retirent de la matière pour que, une fois l'encre étalée, la forme résultante soit correcte. Pertinents en petit corps print ; largement obsolètes à l'écran où l'anti-aliasing gère le problème. Certaines polices contemporaines (ABC Whyte Inktrap) les utilisent comme élément stylistique à grande taille.

---

## 6. Classification Vox-ATypI

Conçue par Maximilien Vox en 1954, adoptée par l'Association Typographique Internationale (ATypI) en 1962. Classe les caractères selon des critères structurels formels : axe du contraste, forme des empattements, contraste des traits, proportions, et filiation historique.

### Classiques (serifs à axe progressivement vertical)

**Humanes (Humanist / Venetian)** — XVe siècle (Jenson, Centaur, Goudy Old Style)
Axe oblique marqué (~45 degrés, angle de la plume). Contraste faible. Empattements raccordés, cunéiformes. Traverse du e oblique. Influence calligraphique directe des manuscrits humanistes. Formes organiques.
Critère distinctif : axe diagonal + faible contraste + traverse du e oblique.

**Garaldes (Aldine)** — XVIe-XVIIe siècle (Garamond, Caslon, Granjon)
Axe diagonal mais plus redressé que les Humanes. Contraste modéré à fort. Empattements raccordés mais plus fins que les Humanes. Proportions romaines raffinées.
Critère distinctif : pont entre Humanes et Réales — plus de contraste que les Humanes, empattements encore raccordés (contrairement aux Didones).

**Réales / Transitionnelles** — XVIIe-XVIIIe siècle (Baskerville, Times New Roman, Georgia)
Axe quasi vertical. Contraste marqué. Empattements raccordés mais aminciés. Esprit rationaliste des Lumières. Forte hauteur d'x.
Critère distinctif : axe presque vertical + contraste fort + empattements encore raccordés.

**Didones (Modern)** — Fin XVIIIe-début XIXe (Bodoni, Didot)
Axe parfaitement vertical. Contraste extrême (fûts épais, empattements filiformes). Empattements non raccordés, perpendiculaires. Terminaisons en boule fréquentes. Rationalisme géométrique poussé au maximum.
Critère distinctif : contraste maximal + empattements filiformes non raccordés + axe vertical pur.

**Mécanes (Slab Serif / Mechanistic)** — XIXe siècle (Rockwell, Clarendon, Courier)
Contraste très faible (empattements quasi aussi épais que les fûts). Empattements rectangulaires. Deux sous-types : Clarendons (raccordés, transition courbe) et Égyptiennes (non raccordés, jonction directe). Aspect mécanique, industriel.
Critère distinctif : empattements épais rectangulaires + faible contraste.

### Linéales (sans empattement) — 4 sous-catégories

**Grotesques** — XIXe siècle (Franklin Gothic, Akzidenz Grotesk)
Contraste léger entre pleins et déliés. G à éperon. Jambe du R courbée. Formes encore individualisées. Héritage industriel.

**Néo-grotesques** — XXe siècle (Helvetica, Univers, Arial)
Contraste minimal. Design régulier, modulaire. G sans éperon. Apparence neutre, rationnelle. Standard du modernisme suisse.

**Géométriques** — XXe siècle (Futura, Avenir, Montserrat)
Construites sur des formes géométriques pures (cercle, rectangle, ligne). Épaisseur de trait uniforme. O circulaire. Pureté mathématique.

**Humanistes** (Humanist sans) — XXe siècle (Gill Sans, Frutiger, Myriad, Calibri)
Axe diagonal hérité des capitales romaines et de la minuscule carolingienne. Variation de trait calligraphique. Proportions classiques. Qualité organique. Lisibilité supérieure en corps grâce aux formes différenciées.

### Catégories complémentaires

**Incises / Glyphiques** (Trajan, Albertus) — Évoquent la gravure dans la pierre ou le métal. Empattements triangulaires, petits, effilés. Aspect ciselé.

**Scriptes** (Snell Roundhand, Brush Script) — Imitent l'écriture cursive à la plume. Inclinaison droite marquée. Connexions entre lettres. Angle de plume visible.

**Manuaires / Graphiques** (Cooper Black, polices display décoratives) — Aspect dessiné à la main. Qualité décorative ou illustrative. Rupture avec les conventions structurelles.

**Fractures / Blackletter** (Fraktur, Textura) — Modèle des écritures médiévales à plume large. Formes angulaires, compressées. Forte densité verticale.

**Non-latines** : toutes les écritures non latines (grec, cyrillique, arabe, hébreu, CJK, devanagari, etc.). Classées par système d'écriture plutôt que par style.

### Limites de la classification

La Vox-ATypI date de 1954 et peine à couvrir la production contemporaine. Les polices variables, les hybrides serif/sans, les néo-grotesques expressives (ABC Diatype), les serif contemporaines à contrastes aiguisés (GT Sectra) ne rentrent pas proprement dans les catégories. La classification reste utile comme vocabulaire structurel et comme repère historique, mais elle n'est pas prescriptive pour le dessin contemporain.

---

## 7. Technologie des polices numériques

### Formats de fichiers

**PostScript Type 1** (Adobe, 1984) : courbes de Bézier cubiques (4 points de contrôle : point de départ, deux poignées hors courbe, point d'arrivée). Premier format vectoriel pour la typographie. Dominant en PAO professionnelle jusqu'aux années 2000.

**TrueType** (Apple 1991, Microsoft 1992) : courbes de Bézier quadratiques (3 points de contrôle : point de départ, un point hors courbe, point d'arrivée). Calcul plus léger pour le rastériseur (arithmétique de second degré). Stratégie d'Apple contre le monopole Adobe.

**OpenType** (Adobe + Microsoft, 1996) : conteneur unifié acceptant les deux types de contours. Un fichier .otf contient des contours CFF (cubiques PostScript). Un fichier .ttf contient des contours TrueType (quadratiques). Les deux sont des polices OpenType ; l'extension indique le format des contours.

**Variable Fonts** (OpenType 1.8, 2016) : un seul fichier interpole sur un ou plusieurs axes de variation. Cinq axes enregistrés : weight (wght), width (wdth), slant (slnt), optical size (opsz), italic (ital). Axes personnalisés illimités (GRAD, XTRA, etc.).

**WOFF / WOFF2** (web) : WOFF 1.0 compresse avec zlib (~40 % de réduction). WOFF2 utilise Brotli après transformation des tables (~30 % d'amélioration supplémentaire). WOFF2 couvre >97 % des navigateurs.

### Bézier cubiques vs. quadratiques

La conversion quadratique vers cubique est sans perte. La conversion cubique vers quadratique est une approximation qui augmente le nombre de points de 20-35 % sans différence visible au rendu. Les cubiques offrent plus de contrôle au dessinateur (deux poignées indépendantes vs. une seule). Sur les machines modernes, la différence de performance de rendu est négligeable.

### Intérieur d'un fichier de police

**Contours de glyphes** : séquences de points sur courbe (on-curve) et hors courbe (off-curve) formant des contours fermés. Stockés dans la table glyf (TrueType) ou CFF (PostScript).

**Table cmap** : associe les codes Unicode aux indices de glyphes. Le moteur de texte lit un code Unicode, obtient l'indice de glyphe, accède au contour.

**Tables de métriques** : hhea (en-tête horizontal), hmtx (chasses et approches gauches), OS/2 (ascendante, descendante, interligne, hauteur d'x — métriques globales).

**Tables de mise en forme avancée** :
- **GSUB** (substitution de glyphes) : ligatures, alternates stylistiques, petites capitales, substitutions contextuelles.
- **GPOS** (positionnement de glyphes) : crénage, attachement cursif, positionnement des signes diacritiques.
- **GDEF** (définition des glyphes) : classifie chaque glyphe (base, composant de ligature, marque combinatoire).

**Pipeline de traitement** : cmap (code vers glyphe) puis GSUB (substitutions) puis GPOS + baseline (positionnement) puis rendu.

### Features OpenType — tags principaux

| Tag | Fonction |
|---|---|
| liga | Ligatures standard (fi, fl, ffi) |
| dlig | Ligatures discrétionnaires |
| smcp | Petites capitales (vraies, dessinées) |
| c2sc | Capitales vers petites capitales |
| pnum | Chiffres proportionnels |
| tnum | Chiffres tabulaires |
| lnum | Chiffres alignés (lining) |
| onum | Chiffres elzéviriens (oldstyle) |
| salt | Alternates stylistiques |
| ss01-ss20 | Jeux stylistiques 1 à 20 |
| calt | Alternates contextuels |
| swsh | Fioritures (swashes) |
| frac | Fractions |
| ordn | Ordinaux |

### Ligatures — pourquoi elles existent

En composition au plomb, certaines combinaisons de lettres entraient en collision physique (le crochet du f avec le point du i, le sommet du l). Les fondeurs créaient des sorts de ligature — pièces de métal uniques combinant les caractères problématiques. En numérique, les ligatures persistent pour des raisons esthétiques et de lisibilité, encodées comme règles de substitution GSUB.

### Petites capitales : dessinées vs. mises à l'échelle

**Vraies petites capitales** : glyphes dessinés à la hauteur d'x avec des traits plus épais que des capitales réduites, pour maintenir la cohérence de poids avec le reste de la police. Accessibles via le tag smcp.

**Fausses petites capitales** : capitales réduites mécaniquement à la hauteur d'x. Les traits deviennent trop fins, l'espacement est incohérent. La plupart des traitements de texte génèrent des fausses petites capitales même quand de vraies sont disponibles dans la police.

### Chiffres : quatre combinaisons

Les chiffres varient sur deux axes indépendants :
- **Alignés (lining)** vs. **Elzéviriens (oldstyle)** : hauteur uniforme (cap height) vs. hauteur variable avec ascendantes/descendantes.
- **Proportionnels** vs. **Tabulaires** : chasse variable vs. chasse fixe.

Quatre combinaisons possibles : proportionnels alignés, tabulaires alignés, proportionnels elzéviriens, tabulaires elzéviriens. Les tabulaires s'alignent verticalement en colonnes (tableaux financiers). Les proportionnels se fondent dans le texte courant. Les elzéviriens sont moins intrusifs visuellement dans la prose littéraire.

---

## 8. Technologies de rendu

### Hinting

**TrueType hinting** : instructions bytecode de bas niveau qui contrôlent le rendu pixel par pixel. Contrôle granulaire, précis. Complexe à produire (travail manuel de spécialistes).

**PostScript hinting** : informations abstraites sur la position des éléments (zones d'alignement, épaisseurs de traits). Le rastériseur interprète ces informations. Plus facile à créer, moins de contrôle direct.

### Rendu par plateforme

**Windows (ClearType)** : approche hinting-first. Aligne les traits horizontaux sur la grille de pixels. Rendu net, contrasté. Sous-pixel rendering RGB horizontal. Optimisé pour les écrans à résolution standard.

**macOS (Quartz)** : approche geometry-first. Préserve les contours originaux avec anti-aliasing en niveaux de gris. Rendu plus lisse, moins d'artefacts de couleur. Optimisé pour les écrans haute résolution (Retina).

C'est pour cette raison que la même police peut paraître différente entre Windows et macOS — ce ne sont pas les mêmes philosophies de rastérisation.

### Obsolescence progressive du hinting

Sur les écrans haute résolution (>300 DPI — Retina, 4K), la grille de pixels est suffisamment fine pour que les instructions de hinting deviennent imperceptibles. Le rendu vectoriel domine l'apparence visuelle. Le hinting reste pertinent uniquement pour les écrans basse résolution et l'impression à faible résolution.

---

## 9. Du plomb au numérique — transitions techniques

### Composition manuelle (Gutenberg — XIXe siècle)

Gutenberg (~1450) : alliage plomb-antimoine-étain à point de fusion bas, moules à main ajustables pour la fonte reproductible de caractères identiques. Composition manuelle par des ouvriers compositeurs travaillant avec des casses (compartiments en bois — origine des termes « haut de casse » / « bas de casse » pour majuscules/minuscules).

### Composition mécanique chaude (1886-1970s)

**Linotype** (Mergenthaler, 1886) : l'opérateur tape sur un clavier à 90 caractères. La machine assemble des matrices en laiton en une ligne complète, coule un lingot de métal (slug) pour toute la ligne, puis redistribue automatiquement les matrices. 3 à 5 fois plus rapide que la composition manuelle. Dominante dans la presse quotidienne.

**Monotype** (Lanston, 1887) : architecture à deux machines. Un clavier produit un ruban perforé encodant les caractères et l'espacement. Une fondeuse séparée lit le ruban et coule des caractères individuels. Avantage : corrections possibles sans refondre la ligne entière. Dominante dans l'édition de livres.

### Photocomposition (1950s-1980s)

Lumitype-Photon (Higonnet et Moyroud, 1946-1953) : polices stockées sur disque rotatif comme négatifs photo. Stroboscope, lentille d'agrandissement, projection sur papier photographique. Plus de contrainte physique de métal — les caractères peuvent être agrandis, réduits, déformés optiquement.

**Perdu à cette transition** : la relation physique directe entre le dessin du caractère et sa taille. En plomb, chaque corps était un dessin distinct (les poinçonnistes ajustaient les proportions par taille — ancêtre de l'optical sizing). La photocomposition a introduit l'agrandissement mécanique d'un dessin unique, perdant ces ajustements par taille.

### Numérique (1970s-présent)

IKARUS (Peter Karow, 1972) : premier système vectoriel/géométrique de représentation typographique. Transition des bitmaps (grille de pixels, un fichier par taille) aux contours vectoriels (une description mathématique, toutes les tailles). Fondation de la PAO et de la typographie contemporaine.

**Regagné récemment** : les Variable Fonts (2016) réintroduisent l'optical sizing via l'axe opsz, restaurant la pratique des poinçonnistes du XVIe siècle dans un cadre numérique.
