# Data Visualization — Référence technique

## 1. Canaux d'encodage visuel — Hiérarchie Cleveland & McGill

L'étude fondatrice de Cleveland et McGill (1984) a mesuré la précision des jugements perceptuels humains pour différents encodages graphiques. La hiérarchie résultante, du plus précis au moins précis :

1. Position sur une échelle commune (bar chart, dot plot)
2. Position sur des échelles non alignées (small multiples sans axe commun)
3. Longueur (barres)
4. Direction / angle (pie chart, diagrammes en étoile)
5. Surface (bubble chart, treemap)
6. Volume (graphiques 3D)
7. Courbure (courbes)
8. Couleur / saturation (heatmaps, choroplèthes)

Cette hiérarchie est ancrée dans deux lois psychophysiques fondamentales.

### Loi de Weber

La loi de Weber décrit le seuil de discrimination : le plus petit changement perceptible d'un stimulus (JND, Just Noticeable Difference) est proportionnel à l'intensité du stimulus. ΔS/S = k (constante). Les fractions de Weber varient par canal :

- Longueur : k ≈ 3–5 % (très précis — on discrimine deux barres qui diffèrent de 3–5 %)
- Surface : k ≈ 10–15 % (il faut 10–15 % de différence pour distinguer deux cercles)
- Saturation de couleur : k ≈ 20 % (très imprécis — les différences de saturation de moins de 20 % sont difficilement perceptibles)

Conséquence directe : la position (fraction de Weber ~1–2 %) bat la longueur, qui bat la surface, qui bat la couleur pour l'encodage de données quantitatives.

### Loi de Stevens

La loi de puissance de Stevens décrit la relation entre l'intensité physique et l'intensité perçue : P = k × S^n, où P est la perception, S le stimulus physique, et n l'exposant.

- Longueur : n ≈ 1.0 (perception proportionnelle — une barre deux fois plus longue est perçue comme deux fois plus longue)
- Surface : n ≈ 0.7 (compression — un cercle deux fois plus grand en surface est perçu comme seulement ~1.6× plus grand)
- Luminosité : n ≈ 0.5 (compression forte)
- Volume : n ≈ 0.7 (compression similaire à la surface)

L'exposant n < 1 pour la surface explique la sous-estimation systématique des bubble charts : un cercle d'aire 100 à côté d'un cercle d'aire 50 ne semble pas deux fois plus grand. Pour compenser, il faudrait encoder la racine carrée de la valeur dans le rayon, ce qui est rarement fait en pratique.


## 2. Traitement pré-attentif

Le traitement pré-attentif désigne la détection de propriétés visuelles qui se produit en moins de 200 ms, avant l'engagement de l'attention consciente, et indépendamment du nombre de distracteurs dans le champ visuel. Un point rouge parmi des points bleus est détecté instantanément, quel que soit le nombre de points bleus.

### Features pré-attentives

Les propriétés détectées pré-attentivement incluent : teinte de couleur, orientation, taille, mouvement, forme (ensemble limité), enclosure (être entouré d'un cadre), groupement spatial. Chacune est traitée par un canal spécialisé du cortex visuel (V1–V4).

### Feature Integration Theory (Treisman, 1980)

La FIT distingue deux étapes de traitement visuel :

1. **Étape pré-attentive** : chaque feature est détectée en parallèle par son canal dédié. La recherche est indépendante du nombre d'éléments (temps constant).
2. **Étape attentive** : les conjonctions de features (ex: "rouge ET vertical") nécessitent une recherche sérielle — l'attention doit se porter sur chaque élément individuellement. Le temps de recherche croît linéairement avec le nombre d'éléments.

Implication pour la dataviz : encoder une catégorie par une seule feature pré-attentive (couleur OU forme) est détectable instantanément. Encoder par une conjonction (forme ET couleur) nécessite une inspection consciente de chaque élément — c'est plus lent et plus sujet à erreur.

### Pop-out et interférence

Le pop-out se produit quand un unique élément diffère des autres sur une seule feature. Il disparaît quand l'élément cible est défini par une conjonction de features.

L'interférence entre canaux : utiliser trop de canaux pré-attentifs simultanément (couleur + taille + forme + orientation) crée du bruit visuel. Chaque canal ajouté réduit la saillance des autres. En pratique, 1 à 2 canaux pré-attentifs pour le highlighting dans une visualisation est le maximum efficace.


## 3. Principes de Gestalt comme mécanique perceptuelle

Les principes de Gestalt ne sont pas des guidelines esthétiques — ce sont des descriptions du fonctionnement du cortex visuel pour le groupement d'éléments. Ils opèrent automatiquement, en amont de l'attention consciente.

### Proximité

Les éléments proches sont perçus comme un groupe. Le groupement se brise quand la distance inter-groupe dépasse ~3× la distance intra-groupe. C'est le mécanisme qui fait fonctionner les scatterplots (clusters visibles) et le whitespace dans les layouts (séparation de sections sans lignes).

### Similarité

Les éléments partageant une propriété visuelle (couleur, forme, taille) sont perçus comme appartenant au même groupe. La différence de propriété doit dépasser le JND (Just Noticeable Difference) du canal concerné pour que le groupement opère. En dataviz : c'est ce qui fait fonctionner l'encodage couleur par catégorie dans un scatterplot.

### Continuité

Le système visuel préfère les contours lisses et continus aux ruptures brusques. Quand deux lignes se croisent, l'œil suit chaque ligne à travers le croisement plutôt que de voir un angle. C'est le mécanisme qui rend les line charts efficaces pour les séries temporelles : l'œil suit le contour de la courbe comme une trajectoire continue.

### Fermeture (closure)

Les formes incomplètes sont mentalement complétées. Un rectangle dont un côté manque est quand même perçu comme un rectangle. Conséquence en dataviz : les cadres de graphique n'ont pas besoin d'être fermés sur les quatre côtés — un axe X et un axe Y suffisent, le système visuel "complète" l'espace du graphique.

### Connectedness (Palmer & Rock, 1994)

Les éléments connectés par une ligne sont groupés plus fortement que par la proximité ou la similarité seules. C'est le mécanisme qui rend les connected scatterplots et les slopegraphs efficaces : la connexion physique entre les points est plus forte que la proximité spatiale pour établir une relation.

### Région commune

Les éléments à l'intérieur d'une frontière partagée sont perçus comme un groupe. Mécanisme sous-jacent des small multiples (chaque facette est une région commune) et du faceting en général. Plus fort que la proximité seule.

### Figure / fond

Le système visuel sépare le premier plan (figure) de l'arrière-plan (fond). Les éléments à fort contraste deviennent figure, les éléments à faible contraste deviennent fond. Application directe : des gridlines fines et grises restent "fond" et ne concurrencent pas les données (figure) à fort contraste.


## 4. Principes de Tufte

### Data-ink ratio

Data-ink ratio = encre consacrée aux données / encre totale. Le principe : maximiser ce ratio dans la mesure du raisonnable. Supprimer l'encre non-data qui n'aide pas la compréhension : chart junk décoratif, moiré patterns, gridlines lourdes, ombres portées, encodages redondants, bordures inutiles.

La nuance (Bateman et al., 2010) : une étude empirique a montré que les "chart junk" de Nigel Holmes amélioraient la mémorisation des visualisations sans dégrader la précision de lecture lors du rappel. Le data-ink ratio maximal n'est pas toujours l'optimum — la mémorabilité et l'engagement ont aussi de la valeur. Le principe reste utile comme outil d'édition (chaque élément non-data doit justifier sa présence), pas comme règle absolue.

### Lie factor

Lie factor = taille de l'effet dans le graphique / taille de l'effet dans les données. Un lie factor de 1 est fidèle. Au-dessus de 1 : exagération. En-dessous de 1 : minimisation.

Source fréquente : utiliser la surface ou le volume pour encoder des quantités linéaires sans correction. Si une valeur double et que le rayon d'un cercle double, la surface quadruple — le lie factor est 2. Pour être fidèle, le rayon devrait être multiplié par √2 (racine de la valeur).

Autre source courante : le saut d'axe Y dans un bar chart, qui amplifie visuellement les différences relatives.

### Small multiples

Le même type de graphique répété pour chaque catégorie ou période temporelle. Exploite les principes de Gestalt de similarité et de région commune : le lecteur apprend la structure une fois et peut comparer entre les panneaux. Plus efficace que l'animation ou l'interaction pour les tâches de comparaison, parce que tous les panneaux sont visibles simultanément (pas de charge mémoire).

### Sparklines

Graphiques de la taille d'un mot, intégrés dans du texte ou des tableaux. Résolution : ~1–2 mm par point de données. Pas d'axes, pas de labels — la forme pure des données. "Intense, simple, word-sized graphics" (Tufte, 2006). Utilisées dans les tableaux de bord pour montrer la tendance à côté du chiffre courant.

### Densité d'information

Information par unité de surface. Les cartes géographiques détaillées atteignent ~1000 points de données par cm². La plupart des graphiques de gestion : < 10. Il y a presque toujours de la place pour augmenter la densité en éliminant les éléments non-data et en réduisant les marges inutiles.

### Lectures micro / macro

Une visualisation bien conçue supporte à la fois la vue d'ensemble (macro : tendance générale, patterns) et l'inspection de détail (micro : valeurs individuelles, outliers) sans changer de mode. Les small multiples en sont un bon exemple : vue macro = le pattern global entre les panneaux, vue micro = les valeurs dans un panneau spécifique.


## 5. Sélection de graphique par structure de données

### Comparaison catégorielle

- Peu de catégories (< 7) : bar chart. Horizontal si les labels sont longs. L'encodage par position sur une échelle commune est le plus précis (rang 1 Cleveland & McGill)
- Beaucoup de catégories (7–30) : bar chart trié par valeur. Le tri exploite la position ordinale pour accélérer la lecture
- Groupes de catégories (2–3 groupes × quelques catégories) : grouped bar chart. Au-delà de 3 groupes, l'angle et la position se confondent — passer aux small multiples
- Ne jamais utiliser : pie chart pour la comparaison. L'angle (rang 4) est largement inférieur à la position (rang 1). Le pie chart n'est justifié que pour montrer un part-to-whole avec 2–3 segments dont un est dominant (> 50 %)

### Tendance temporelle

- Série unique : line chart. Le principe de continuité rend l'interpolation intuitive. L'area chart (surface remplie) n'est justifié que si la baseline à zéro est significative (cumul, stock)
- Séries multiples (2–4) : multi-line chart. Au-delà de 4 : highlight + gray strategy (une série en couleur, les autres en gris clair) ou small multiples
- Patterns cycliques : superposer les cycles (ex: chaque année en couleur sur le même axe de mois) ou heatmap avec le temps en deux axes (mois × année)

### Distribution

- Variable unique continue : histogramme. La largeur des bins influence fortement la lecture — règle de Sturges comme point de départ : k = 1 + 3.322 × log₁₀(n)
- Comparaison de distributions : violin plot, ridgeline plot (joy plot), ou courbes de densité superposées avec transparence. Le box plot montre médiane, IQR, whiskers et outliers — bon pour comparer entre catégories mais mauvais pour les distributions bimodales (il cache la forme)
- Variable unique discrète : bar chart des fréquences

### Relation bivariée

- Deux variables continues : scatterplot. Position × position = les deux canaux les plus précis. Si overplotting : transparence, binning hexagonal, contours de densité
- Troisième variable : encoder par la taille (bubble chart — mais la perception de surface est compressée, n ≈ 0.7) ou par la couleur (séquentielle pour quantitatif, catégorielle pour nominal)

### Composition (part-to-whole)

- Évolution temporelle : stacked area ou stacked bar chart. L'ordre des couches compte : la catégorie la plus importante ou la plus variable sur la baseline (seule couche dont la lecture est précise en position sur échelle commune)
- Statique : treemap (encodage par surface, peu précis mais gère beaucoup de catégories), waffle chart (100 unités, encodage par position — plus précis que le pie), ou simplement un tableau avec sparklines de barres

### Hiérarchie

- Treemap : encodage par surface, usage efficace de l'espace, fonctionne pour > 20 nœuds
- Sunburst : treemap radial, encodage par angle — moins précis mais montre les niveaux de hiérarchie clairement

### Flux

- Sankey diagram : la largeur encode la quantité, les connexions montrent source → destination. Fonctionne pour < 15 nœuds. Au-delà, illisible
- Chord diagram : flux par paires en disposition circulaire. Difficile à lire précisément mais bon pour la détection de patterns

### Géographie

- Choroplèthe : couleur sur des régions géographiques. Problème : les grandes régions dominent la perception indépendamment de leur valeur. Atténuation : projections à surface égale, cartogrammes
- Symboles proportionnels : cercles sur une carte. Meilleur pour comparer des valeurs (surface, rang 5 > couleur, rang 8). Mais la perception de surface est compressée (Stevens n ≈ 0.7)


## 6. Couleur en dataviz

### Trois types de palettes

- **Séquentielle** : pour les données ordonnées (low-to-high). Un seul hue, variation monotone de lightness. En OKLCH : fixer H, varier L de ~0.95 (valeur basse) à ~0.25 (valeur haute)
- **Divergente** : pour les données avec un point central significatif (écart à la moyenne, positif/négatif). Deux hues + midpoint neutre clair. Symétrie de lightness obligatoire entre les deux branches
- **Catégorielle** : pour les données nominales. Hues distincts à L et C constants. Maximum ~8–10 couleurs avant que la distinguabilité ne s'effondre

### Rainbow / jet est cassé

La palette rainbow (jet) a une lightness non-monotone : le jaune est beaucoup plus lumineux que le bleu et le rouge. Conséquences :

- Des frontières perceptuelles apparaissent là où la lightness change brusquement (la "bande jaune"), créant de faux patterns dans les données
- L'ordre perceptuel ne correspond pas à l'ordre des données (le jaune "saute" visuellement entre le vert et le orange)
- Inutilisable en niveaux de gris (la lightness n'est pas monotone, donc la rampe de gris n'est pas ordonnée)

Alternatives : viridis (perceptuellement uniforme, CVD-safe, monotone en lightness), turbo (rainbow perceptuel amélioré, meilleur que jet mais pas CVD-safe), cividis (CVD-safe optimisé pour deutéranopie).

### Daltonisme

8 % des hommes ont une déficience de la vision des couleurs (CVD), principalement dans l'axe rouge-vert. Implications :

- Toujours tester les palettes avec un simulateur protanopie/deutéranopie
- Utiliser la variation de lightness comme discriminateur primaire, le hue comme secondaire. Si la palette est toujours lisible en niveaux de gris, elle fonctionnera pour la plupart des CVD
- Palette blue-orange : safe pour les types protan et deutan (les axes de confusion rouge-vert ne touchent pas le bleu ni l'orange)

### Interaction avec le fond

Le contraste simultané fait qu'une même couleur est perçue différemment sur un fond clair vs un fond sombre. Tester systématiquement les palettes sur le fond réel de la visualisation. Les couleurs à faible chroma sont particulièrement sensibles à cet effet.


## 7. Annotation et étiquetage

### Étiquetage direct > légende

L'étiquetage direct (label placé à côté ou sur la donnée) est toujours supérieur à une légende séparée. La légende impose un aller-retour visuel : identifier la couleur dans le graphique → chercher la couleur dans la légende → lire le label → retourner au graphique. Ce va-et-vient surcharge la mémoire de travail. L'étiquetage direct élimine ce coût cognitif.

### Annotation contextuelle

Annoter les données avec des événements, seuils ou benchmarks transforme un graphique descriptif en graphique explicatif. Un pic dans une série temporelle est une question sans annotation ; c'est une réponse avec. Exemples : dates de lancement produit, changements de politique, seuils réglementaires, moyennes de l'industrie.

### Lignes de référence

Baselines, moyennes, cibles. Stylées de manière subtile (fines, grises, pointillées) pour rester "fond" (Gestalt figure/fond) et ne pas concurrencer les données. La ligne de référence la plus utile est souvent la moyenne ou le zéro — elle donne un point d'ancrage pour évaluer les valeurs individuelles.

### Hiérarchie textuelle

Par ordre de lecture : titre (ce que le graphique montre ou son takeaway principal), sous-titre (précision méthodologique ou note clé), labels d'axes (unités et échelle), labels de données (valeurs individuelles si nécessaire), source (crédibilité et traçabilité).

Tous ne sont pas nécessaires à chaque fois. Le titre et un niveau de contexte suffisent dans la plupart des cas. Un graphique dans un dashboard peut n'avoir qu'un titre. Un graphique dans une publication scientifique aura tous les niveaux.


## 8. Erreurs courantes

### Double axe Y

Deux échelles différentes sur le même graphique. Le point de croisement entre les deux séries est arbitraire (il dépend des plages choisies pour chaque axe) et crée de fausses corrélations visuelles. Alternative : indexer les deux séries à 100 (montrer l'évolution relative) ou utiliser deux graphiques alignés verticalement (small multiples).

### Axe Y tronqué

Commencer l'axe Y à une valeur non-zéro. Légitime pour montrer la variation (line charts, cours boursiers — où le message est le changement, pas le niveau absolu). Trompeur pour la comparaison de magnitudes (bar charts — où l'encodage est la longueur, et une longueur tronquée fausse la proportion). Règle : les bar charts doivent commencer à zéro ; les line charts peuvent être tronqués si c'est clairement indiqué.

### Graphiques 3D

La 3D ajoute une distorsion de perspective à chaque encodage. Les barres en arrière-plan paraissent plus petites (perspective). Les tranches de pie au premier plan paraissent plus grandes (projection). Le volume (rang 6 Cleveland & McGill) est un encodage très imprécis. Ne jamais utiliser la 3D pour encoder des données — la 3D n'est justifiée que pour des données intrinsèquement tridimensionnelles (visualisation spatiale, modèles moléculaires).

### Pie chart à > 5 segments

La perception des angles est imprécise (rang 4), et les petites tranches adjacentes deviennent indistinguables. Un pie avec 8 segments dont 3 font < 5 % est une illusion de précision. Alternative : bar chart horizontal trié, où la position et la longueur (rangs 1 et 3) encodent les mêmes données avec plus de précision.

### Double encodage

Utiliser la couleur ET la hauteur pour la même variable gaspille un canal et peut créer de la confusion si les deux encodages divergent légèrement à cause de la compression perceptuelle (Stevens). Principe : un canal par variable. Le deuxième canal devrait encoder une deuxième dimension, pas la même.

### Spaghetti chart

Plus de 5 séries superposées dans un line chart. Impossible de tracer une série individuelle à travers les croisements. Solutions : highlight + gray (une série en couleur, les autres en gris clair), small multiples (une série par panneau), filtrage interactif, ou annotation directe de la série d'intérêt.
