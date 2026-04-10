# Color Science — Référence technique

## 1. Physique de la lumière et perception

La lumière visible occupe la bande 380–700 nm du spectre électromagnétique. La rétine humaine contient trois types de cônes, chacun avec un pic de sensibilité spectrale distinct : cônes L (long, pic ~564 nm, sensibles au rouge-jaune), cônes M (medium, pic ~534 nm, sensibles au vert), cônes S (short, pic ~420 nm, sensibles au bleu-violet). La vision des couleurs émerge du rapport d'activation entre ces trois types — le signal de chaque cône seul ne code pas une couleur, c'est le ratio L:M:S qui produit la sensation chromatique.

Le métamérisme est la conséquence directe de ce système trichromatique : deux spectres physiquement différents peuvent produire le même triplet d'activation (L, M, S) et donc la même perception de couleur. C'est ce qui rend possible la reproduction couleur avec trois primaires (RGB, CMY). Mais un métamère sous illuminant D65 (lumière du jour, ~6500K) peut cesser d'en être un sous illuminant F11 (fluorescent) parce que la distribution spectrale de la source change les rapports d'activation. Conséquence pratique : deux matériaux qui "matchent" en magasin sous éclairage fluorescent peuvent diverger en lumière naturelle.

L'adaptation chromatique (modèle de von Kries) décrit comment le système visuel ajuste les gains des trois canaux de cônes en fonction de l'illuminant ambiant. Mécanisme : chaque canal est divisé par sa propre réponse moyenne à l'illuminant, ce qui normalise le point blanc perçu. C'est pourquoi une feuille blanche paraît blanche aussi bien en lumière tungstène (jaune) qu'en lumière du jour (bleue), bien que les longueurs d'onde réfléchies soient très différentes. Le modèle de von Kries est une approximation linéaire qui fonctionne raisonnablement pour les changements modérés d'illuminant, mais échoue pour les changements extrêmes.


## 2. Modèles et espaces couleur

### CIE XYZ (1931)

Le CIE XYZ est l'espace de référence absolu de la colorimétrie. Il est construit sur les fonctions de correspondance couleur x̄(λ), ȳ(λ), z̄(λ) dérivées expérimentalement avec un observateur standard 2° (champ visuel de 2° de diamètre, correspondant à la fovéa). Y correspond à la luminance. Le diagramme de chromaticité xy (x = X/(X+Y+Z), y = Y/(X+Y+Z)) projette toutes les couleurs sur un plan 2D en éliminant la luminance, mais n'est pas perceptuellement uniforme : des distances égales dans le diagramme ne correspondent pas à des différences perçues égales.

### sRGB

L'espace standard des écrans depuis 1996 (IEC 61966-2-1). Primaires définies dans CIE xy : R(0.64, 0.33), G(0.30, 0.60), B(0.15, 0.06). Point blanc D65 (0.3127, 0.3290). La fonction de transfert (gamma) est une fonction par morceaux, pas un simple gamma 2.2 :

- Encodage (linéaire → sRGB) : si C_linear ≤ 0.0031308, alors C_sRGB = 12.92 × C_linear ; sinon C_sRGB = 1.055 × C_linear^(1/2.4) − 0.055
- Décodage (sRGB → linéaire) : si C_sRGB ≤ 0.04045, alors C_linear = C_sRGB / 12.92 ; sinon C_linear = ((C_sRGB + 0.055) / 1.055)^2.4

Le segment linéaire en bas de la courbe évite une pente infinie à l'origine que produirait un gamma pur. Le gamma effectif moyen est ~2.2 mais l'approximation par un gamma simple introduit des erreurs mesurables dans les ombres.

### Display P3

Développé par Apple à partir du gamut cinéma DCI-P3. Mêmes primaires rouge et bleue que DCI-P3, mais point blanc D65 (comme sRGB) au lieu du point blanc vert du cinéma. Même fonction de transfert que sRGB. Le gamut est ~25 % plus large que sRGB, principalement dans les rouges et verts saturés. Supporté par tous les écrans Apple depuis 2016, et par la majorité des écrans OLED Android. En CSS : `color(display-p3 r g b)`.

### Adobe RGB (1998)

Gamut étendu par rapport à sRGB dans les cyans et verts. Fonction de transfert : gamma simple 2.199 (souvent arrondi à 2.2). Utilisé principalement en photographie et prepress pour couvrir une plus large portion du gamut CMYK. Peu pertinent pour le web (pas de support CSS natif), mais important pour les workflows d'impression.

### CIELAB (L*a*b*)

Tentative de 1976 de créer un espace perceptuellement uniforme. L* = luminosité (0 = noir, 100 = blanc), a* = axe vert-rouge, b* = axe bleu-jaune. La transformation depuis XYZ utilise une racine cubique (avec un segment linéaire pour les très faibles valeurs) pour modéliser la réponse compressive de la vision humaine.

Le problème majeur de CIELAB est le blue hue shift : un bleu saturé (a* négatif, b* très négatif) déplacé à chroma constant et lightness constante dérive visuellement vers le violet. Cela rend les gradients de teinte dans la zone bleue non uniformes — un arc de hue constant dans Lab n'est pas perçu comme une teinte constante. Ce problème est dû à la simplicité de la transformation (matrice linéaire + racine cubique) qui ne modélise pas correctement la non-linéarité de la réponse chromatique dans cette zone.

### CIELCH

Conversion polaire de CIELAB : C* = √(a*² + b*²) (chroma), h = atan2(b*, a*) (hue en degrés). Plus intuitif pour la manipulation : on peut tourner la teinte, augmenter la saturation, ou changer la luminosité indépendamment. Hérite des défauts de Lab, notamment le blue hue shift.

### HSL / HSV

Modèles de 1978 conçus comme interfaces utilisateur pour la sélection couleur, pas comme espaces de calcul. HSL : H (teinte 0-360°), S (saturation 0-100%), L (luminosité 0-100%). HSV : H, S, V (value/brightness).

Pourquoi ils sont cassés : HSL L=50% est censé être le milieu perceptuel, mais un jaune à L=50% est perceptuellement beaucoup plus lumineux qu'un bleu à L=50%. La "saturation" HSL n'a aucun rapport avec la saturation perceptuelle — c'est une mesure purement mathématique de la distance au gris dans le modèle RGB. Conséquence : des couleurs à S et L identiques en HSL peuvent avoir des vivacités perçues radicalement différentes. Utiliser HSL pour construire des palettes produit des résultats visuellement incohérents.

### OKLab (Björn Ottosson, 2020)

Corrige les défauts majeurs de CIELAB pour les applications écran. La transformation passe par un espace LMS intermédiaire (activation des cônes), applique une racine cubique, puis une seconde matrice linéaire. Cette double transformation capture mieux les non-linéarités de la perception, notamment dans la zone bleue.

Avantages par rapport à Lab : pas de blue hue shift, meilleure uniformité des gradients, meilleure prédiction de la luminosité perçue. Inconvénient : moins bien validé pour les applications print/industrielles (où CIELAB avec CIEDE2000 reste la référence).

### OKLCH

Conversion polaire d'OKLab : L (lightness, 0 à 1), C (chroma, 0 à ~0.37 pour les couleurs sRGB les plus saturées), H (hue, 0 à 360°). C'est l'espace de travail recommandé pour la construction de palettes numériques : on peut fixer L et C pour obtenir des teintes de luminosité et saturation perçues constantes, ce qui est impossible en HSL. En CSS : `oklch(L C H)`.


## 3. Uniformité perceptuelle

L'uniformité perceptuelle signifie qu'une distance numérique constante dans l'espace correspond à une différence perçue constante, quelle que soit la position dans l'espace. Aucun espace n'est parfaitement uniforme, mais certains sont beaucoup plus proches que d'autres.

### Ellipses de MacAdam

En 1942, MacAdam a mesuré les seuils de discrimination couleur autour de 25 points du diagramme de chromaticité CIE xy. Résultat : les zones de confusion (où deux couleurs sont indistinguables) forment des ellipses de taille et d'orientation très variables selon la position dans le diagramme. Les ellipses sont ~6× plus grandes dans la zone verte que dans la zone bleue-violette. Cela prouve que l'espace xy n'est pas uniforme et que les distances euclidiennes dans xy n'ont pas de signification perceptuelle.

### Delta E

Formules de différence de couleur dans CIELAB :

- **CIE76** (ΔE*ab) : distance euclidienne simple dans Lab. ΔE = √(ΔL² + Δa² + Δb²). Simple mais insuffisante — surestime les différences dans les couleurs saturées.
- **CIE94** (ΔE*94) : ajoute des termes de pondération pour le chroma et la teinte. Meilleure corrélation avec la perception pour les couleurs industrielles.
- **CIEDE2000** (ΔE*00) : la formule la plus précise pour CIELAB. Inclut des termes de rotation dans la zone bleue (pour compenser partiellement le blue hue shift), des pondérations dépendantes de la luminosité, du chroma et de la teinte, et un terme d'interaction chroma-teinte. Formule complexe (~15 lignes) mais la plus fiable pour la comparaison couleur industrielle.

### Seuils de perception

- ΔE < 1 : imperceptible pour la plupart des observateurs
- ΔE 1–2 : perceptible en comparaison directe côte à côte
- ΔE 2–5 : perceptible sans comparaison directe par un observateur attentif
- ΔE 5–10 : différence évidente
- ΔE > 10 : couleurs perçues comme clairement distinctes

OKLab résout la plupart des problèmes d'uniformité de Lab pour les applications écran. La distance euclidienne dans OKLab est une bonne approximation de la différence perçue, sans nécessiter les corrections complexes de CIEDE2000.


## 4. Contraste

### WCAG 2.x

La formule de contraste WCAG utilise la luminance relative, calculée en quatre étapes :

1. Prendre les valeurs sRGB (0–255), diviser par 255 pour obtenir des valeurs 0–1
2. Linéariser : si C_sRGB ≤ 0.04045, C_linear = C_sRGB / 12.92 ; sinon C_linear = ((C_sRGB + 0.055) / 1.055)^2.4
3. Calculer la luminance relative : L = 0.2126 × R_linear + 0.7152 × G_linear + 0.0722 × B_linear
4. Ratio de contraste = (L_plus_clair + 0.05) / (L_plus_sombre + 0.05)

Seuils WCAG 2.x :
- **AA texte normal** : ≥ 4.5:1
- **AA grand texte** (≥ 18pt ou ≥ 14pt bold) et **composants UI** : ≥ 3:1
- **AAA texte normal** : ≥ 7:1

Limites du modèle WCAG 2.x :
- Traite le contraste comme symétrique : noir sur blanc et blanc sur noir donnent le même ratio, mais le texte clair sur fond sombre est perceptuellement moins lisible à ratio égal (halation, étalement lumineux)
- Ignore la taille de police comme variable continue : le seuil saute de 4.5:1 à 3:1 au-dessus de 18pt, sans gradation
- La formule de luminance relative surestime le contraste pour certaines combinaisons de couleurs saturées

### APCA (Accessible Perceptual Contrast Algorithm)

Modèle développé pour WCAG 3 (en draft) par Andrew Somers. Différences fondamentales avec WCAG 2.x :

- **Asymétrique** : le fond contribue davantage que le texte à la perception de luminosité. Un fond clair "pousse" le texte sombre vers plus de contraste perçu qu'un fond sombre ne le fait pour le texte clair.
- **Échelle Lc** (Lightness Contrast) : valeur signée. Lc positif = texte sombre sur fond clair (mode lecture classique). Lc négatif = texte clair sur fond sombre.
- **Seuils approximatifs** : |Lc| ≥ 75 pour le body text, ≥ 60 pour le grand texte, ≥ 45 pour les éléments non-texte (icônes, bordures)
- Intègre la taille de police comme variable continue dans le modèle de contraste

### Fréquence spatiale

Le contraste perceptuel dépend de la taille des détails (fréquence spatiale). Le système visuel humain a une sensibilité au contraste en forme de bande passante, avec un pic autour de 3–5 cycles par degré d'angle visuel. Les petits caractères (haute fréquence spatiale) nécessitent plus de contraste lumineux que les grands caractères (basse fréquence spatiale) pour être également lisibles. C'est la justification physiologique des seuils différenciés par taille dans WCAG.


## 5. Gamut mapping

Le gamut d'un espace couleur est l'ensemble des couleurs qu'il peut représenter. Quand une couleur existe dans un espace source (ex: Display P3) mais pas dans l'espace cible (ex: sRGB), il faut la "mapper" — trouver la couleur représentable la plus proche.

### Clipping vs mapping

Le **clipping** tronque brutalement chaque composante à la borne la plus proche (ex: R=1.1 → R=1.0). Problème : le clipping change souvent la teinte perçue, parce que les trois composantes ne sont pas tronquées proportionnellement. Un orange saturé P3 clippé en sRGB peut virer au jaune.

Le **gamut mapping intelligent** réduit la saturation tout en préservant la teinte et la luminosité perçues. Le résultat est moins saturé mais reste "la même couleur" perceptuellement.

### Algorithme CSS Color Level 4

L'algorithme spécifié dans CSS Color Level 4 pour le gamut mapping opère dans OKLCH :

1. Convertir la couleur en OKLCH
2. Si la couleur est déjà dans le gamut cible → terminé
3. Sinon, fixer L (lightness) et H (hue), réduire C (chroma) par recherche binaire
4. À chaque étape, convertir en RGB du gamut cible et vérifier si toutes les composantes sont dans [0, 1]
5. Critère d'arrêt : la distance OKLab entre l'itération courante et la version clippée est ≤ 0.02

Ce seuil de 0.02 en distance OKLab est sous le seuil de perception pour la plupart des conditions, ce qui signifie que le résultat mappé est visuellement indistinguable du meilleur résultat possible.

### Cas pratique

Une couleur Display P3 `color(display-p3 0.9 0.2 0.1)` — un rouge très saturé — n'a pas d'équivalent exact en sRGB. Le mapping réduit le chroma dans OKLCH : la lightness et la teinte sont préservées, seule la vivacité diminue. Le résultat sRGB est le rouge le plus saturé possible à cette luminosité et cette teinte.


## 6. Déficience de vision des couleurs (CVD)

### Types et prévalence

La CVD résulte de l'absence ou du dysfonctionnement d'un type de cône rétinien. Les formes liées au chromosome X (protan, deutan) touchent ~8% des hommes et ~0.5% des femmes.

- **Protanopie** (absence de cônes L) : ~1% des hommes. Confusion rouge-vert, le rouge apparaît sombre (perte de sensibilité dans les grandes longueurs d'onde)
- **Protanomalie** (cônes L décalés vers M) : ~1% des hommes. Version atténuée de la protanopie
- **Deutéranopie** (absence de cônes M) : ~1% des hommes. Confusion rouge-vert, sans l'assombrissement du rouge
- **Deutéranomalie** (cônes M décalés vers L) : ~5% des hommes. La forme la plus fréquente de CVD. Réduction de la discrimination rouge-vert
- **Tritanopie** (absence de cônes S) : ~0.003% de la population. Confusion bleu-jaune, très rare, non liée au sexe
- **Achromatopsie** (absence de tous les cônes) : ~0.003%. Vision uniquement par les bâtonnets, en niveaux de gris, photophobie sévère

### Principes de conception

Règle fondamentale : ne jamais encoder une information uniquement par la teinte. Toute information chromatique doit être doublée par un autre canal : forme, motif, position, texte, icône.

Palette CVD-safe : le couple bleu + orange fonctionne pour les formes protan et deutan (les axes de confusion sont dans la direction rouge-vert, pas bleu-orange). Éviter le couple rouge pur vs vert pur (confusion maximale pour 8% des hommes).

Tests : simulateurs de CVD (Sim Daltonism sur Mac, Chrome DevTools > Rendering > Emulate vision deficiencies). Tester systématiquement avec protanopie et deutéranopie (les deux couvrent la grande majorité des cas).


## 7. Construction de palettes en OKLCH

OKLCH est l'espace de travail recommandé pour la construction de palettes numériques parce qu'il est (approximativement) perceptuellement uniforme : des valeurs identiques de L et C produisent des couleurs de luminosité et saturation perçues similaires quelle que soit la teinte.

### Palette séquentielle

Un seul hue (H constant), variation monotone de lightness (L). Exemple pour une rampe bleue (H ≈ 260) :

- L variant de 0.95 (très clair) à 0.25 (très sombre) par pas réguliers
- C ajusté pour rester dans le gamut sRGB à chaque niveau de L (les valeurs sombres et très claires ont un chroma maximum plus faible)
- Usage : cartes choroplèthes, heatmaps, toute donnée ordonnée

### Palette divergente

Deux hues opposés, pivot neutre au centre. Le pivot doit être à L élevé (0.93–0.97) et C proche de zéro (gris clair). Exemple classique : bleu (H ≈ 250) vers orange (H ≈ 70), pivot blanc cassé.

Les deux branches doivent être symétriques en lightness : la couleur à 3 pas du centre côté bleu doit avoir le même L que la couleur à 3 pas côté orange. Sinon, une branche attire visuellement plus l'attention que l'autre, ce qui biaise la lecture.

### Palette catégorielle

Hues espacés régulièrement à L et C constants. En théorie, on peut distinguer ~8–10 couleurs catégorielles. Au-delà, les distinctions perceptuelles deviennent fragiles et il faut utiliser d'autres encodages (forme, label, position).

Pour maximiser la distinguabilité : espacer les hues d'au moins 30–40° et vérifier avec un simulateur CVD. Certaines zones de hue (rouge-vert) se confondent pour les protans/deutans — distribuer les teintes en couvrant aussi les bleus et les jaunes.

### Tokens de surface

Pour les fonds et surfaces d'interface : L très élevé (0.97–0.99), C très bas (0.005–0.01). La teinte résiduelle donne de la chaleur ou de la froideur sans distraire. Ces micro-teintes sont perceptibles : un gris pur (C=0) paraît "mort" à côté d'un gris très légèrement teinté.

### Vérification

1. Simuler en protanopie et deutéranopie : les couleurs restent-elles distinguables ?
2. Convertir en niveaux de gris : la rampe de lightness reste-t-elle lisible ? (Si oui, l'information est portée par L, pas seulement par H)
3. Vérifier le contraste de chaque paire texte/fond : ratio WCAG ≥ 4.5:1 pour le texte, ≥ 3:1 pour les éléments UI
4. Vérifier que toutes les couleurs sont dans le gamut cible (sRGB pour le web standard)


## 8. Couleur pour le print

### Modèle soustractif

L'impression utilise un modèle soustractif : les encres absorbent (soustraient) des longueurs d'onde de la lumière blanche réfléchie par le papier. CMYK = Cyan (absorbe le rouge), Magenta (absorbe le vert), Yellow (absorbe le bleu), Key/Black (ajouté pour la densité et l'économie d'encre, parce que CMY mélangés ne produisent qu'un brun-noir boueux).

### Process vs Spot

**Process (CMYK)** : 4 encres standard, la couleur est simulée par des trames de points (demi-teintes) de tailles variables. Limité en gamut, surtout dans les oranges et violets saturés.

**Spot (Pantone)** : encres pré-mélangées pour une couleur exacte. Le Pantone Matching System (PMS) est le standard industriel. Plus cher (une plaque supplémentaire par couleur spot) mais plus fidèle. Indispensable pour les couleurs de marque qui doivent être reproductibles exactement.

Le nuancier physique Pantone est obligatoire : les versions numériques (écran) sont des approximations. Un Pantone 186 C (rouge Coca-Cola) sur écran et sur papier n'ont pas le même aspect — seul le nuancier imprimé fait foi.

### Profils ICC

Un profil ICC décrit le comportement couleur d'un device (scanner, écran, imprimante sur un papier donné). La conversion couleur entre devices suit la chaîne : couleur source → profil source → espace de connexion (PCS, généralement CIELAB ou XYZ) → profil destination → couleur destination.

Profils courants pour le print : Fogra39 (couché Europe), Fogra52 (nouvelle norme couché Europe), SWOP (US couché), GRACoL (US general). Le profil doit correspondre au couple imprimante + papier utilisé.

### Rendering intents

Quatre stratégies pour mapper les couleurs hors-gamut lors de la conversion :

- **Perceptuel** : compresse tout le gamut proportionnellement. Aucune couleur n'est exactement préservée, mais les relations entre couleurs sont maintenues. Bon pour les photographies avec beaucoup de couleurs hors-gamut.
- **Colorimétrique relatif** : préserve les couleurs in-gamut, mappe les couleurs hors-gamut vers le bord du gamut, adapte le point blanc. Le plus courant pour le branding et les aplats de couleur.
- **Colorimétrique absolu** : comme le relatif mais sans adaptation du point blanc. Utilisé pour les épreuves (proofing) — simuler l'aspect du papier final sur un autre support.
- **Saturation** : maximise la vivacité des couleurs dans le gamut cible, au détriment de la fidélité. Adapté aux graphiques business (camemberts, barres) où la vivacité compte plus que l'exactitude.

### Papier et dot gain

Le dot gain (engraissement du point) est l'étalement de l'encre sur le papier. Un point de trame à 50% peut imprimer à 65% sur du papier non couché, ce qui assombrit l'image.

- **Papier couché (coated)** : surface lissée, dot gain ~5–10%. Rendu net, couleurs vives, gamut le plus large. Utilisé pour les brochures, magazines, packaging premium.
- **Papier offset non couché (uncoated)** : surface poreuse, dot gain ~15–25%. Rendu plus doux, couleurs plus sourdes. Utilisé pour la papeterie, le livre, les rapports.
- **Papier journal (newsprint)** : très poreux, dot gain ~30–35%. Gamut très réduit, contraste limité. Les images doivent être préparées spécifiquement (réduction de densité, augmentation du contraste).

Le profil ICC intègre le dot gain attendu pour le couple presse + papier. Utiliser le mauvais profil produit des images trop sombres ou trop claires.

### Total ink coverage (TIC/TAC)

Le total ink coverage est la somme des pourcentages CMYK en un point. Exemples : C=100 M=80 Y=0 K=20 → TIC = 200%. Limites typiques :

- Papier couché : 300–340%
- Papier non couché : 280–300%
- Journal : 240%

Dépasser le TIC maximum → séchage impossible, maculage (l'encre se transfère sur la feuille en vis-à-vis), arrachage du papier.

### Rich black

K=100 seul produit un noir grisâtre en impression (les encres ne sont pas parfaitement opaques). Le rich black ajoute des couches CMY sous le K : une recette courante est C=40 M=30 Y=30 K=100 (TIC = 200%). La recette exacte dépend du profil ICC.

Ne jamais utiliser C=100 M=100 Y=100 K=100 (registration black, TIC=400%) sauf pour les repères de coupe : c'est un excès d'encre massif qui cause des problèmes de séchage et de registre.

### Écran vs print

Les gamuts sRGB et CMYK se chevauchent partiellement mais ne se contiennent pas mutuellement. Certains bleus et verts vifs visibles à l'écran sont hors gamut CMYK. Inversement, certains cyans profonds imprimables sont hors gamut sRGB. Le soft proofing (simulation écran du résultat print via profils ICC et rendering intent) est une approximation utile mais jamais exacte — les conditions d'éclairage, la calibration de l'écran, et les limites du profil ICC introduisent des écarts.


## 9. Formules de conversion de référence

### sRGB ↔ linéaire

Encodage (linéaire → sRGB) :
```
si C_linear ≤ 0.0031308 :
    C_sRGB = 12.92 × C_linear
sinon :
    C_sRGB = 1.055 × C_linear^(1/2.4) − 0.055
```

Décodage (sRGB → linéaire) :
```
si C_sRGB ≤ 0.04045 :
    C_linear = C_sRGB / 12.92
sinon :
    C_linear = ((C_sRGB + 0.055) / 1.055)^2.4
```

### RGB linéaire → XYZ (sRGB, D65)

```
| X |   | 0.4124564  0.3575761  0.1804375 |   | R_lin |
| Y | = | 0.2126729  0.7151522  0.0721750 | × | G_lin |
| Z |   | 0.0193339  0.1191920  0.9503041 |   | B_lin |
```

### XYZ → CIELAB

Avec le point blanc de référence (Xn, Yn, Zn) — pour D65 : Xn=0.95047, Yn=1.0, Zn=1.08883.

```
f(t) = t^(1/3)           si t > (6/29)³ ≈ 0.008856
f(t) = t/(3×(6/29)²) + 4/29   sinon

L* = 116 × f(Y/Yn) − 16
a* = 500 × (f(X/Xn) − f(Y/Yn))
b* = 200 × (f(Y/Yn) − f(Z/Zn))
```

### CIELAB → CIELCH

```
C* = √(a*² + b*²)
h = atan2(b*, a*)    (en degrés, ajuster pour 0–360)
```

### RGB linéaire → OKLab (via LMS)

Matrice M1 (RGB linéaire → LMS) :
```
| l |   | 0.4122214708  0.5363325363  0.0514459929 |   | R |
| m | = | 0.2119034982  0.6806995451  0.1073969566 | × | G |
| s |   | 0.0883024619  0.2817188376  0.6299787005 |   | B |
```

Racine cubique :
```
l' = l^(1/3),  m' = m^(1/3),  s' = s^(1/3)
```

Matrice M2 (LMS cube root → OKLab) :
```
| L |   |  0.2104542553  0.7936177850 -0.0040720468 |   | l' |
| a | = |  1.9779984951 -2.4285922050  0.4505937099 | × | m' |
| b |   |  0.0259040371  0.7827717662 -0.8086757660 |   | s' |
```

### OKLab → OKLCH

```
L = L (inchangé, 0–1)
C = √(a² + b²)
H = atan2(b, a)    (en degrés, ajuster pour 0–360)
```

Les conversions inverses s'obtiennent en inversant les matrices et en élevant au cube au lieu de la racine cubique.
