---
name: muller-brockmann-grid
description: >
  Référence opérationnelle extraite de "Grid Systems in Graphic Design" de Josef Müller-Brockmann (Niggli, 1981).
  Utiliser ce skill dès qu'une demande implique : construire une grille typographique, calculer des marges ou des colonnes, 
  choisir un corps de texte en relation avec une colonne, concevoir un layout éditorial (magazine, rapport, affiche, catalogue), 
  comprendre les systèmes de mesure typographique (points, cicéros), aligner images et texte sur une grille, 
  ou produire un document au style Swiss International Typographic Style.
  Ce skill est aussi pertinent pour conseiller sur la construction d'interfaces visuelles, de slides, ou de PDF qui appliquent une logique de grille stricte.
  À utiliser en complément du skill swiss-designer pour la production de fichiers PDF/PPTX.
---

# Grid Systems in Graphic Design — Référence Müller-Brockmann

Source : Josef Müller-Brockmann, *Grid Systems in Graphic Design / Rastersysteme für die visuelle Gestaltung*, Niggli Verlag, 1981, 162 pages.

Ce skill documente les principes de construction de grilles tels qu'exposés dans le livre. Il est organisé en trois couches : philosophie, mécanique, application. Pour les calculs détaillés et les tableaux de formats DIN, voir `references/CALCULS.md`.

---

## 1. Philosophie de la grille

La grille n'est pas un outil neutre : c'est l'expression d'une attitude mentale. Utiliser la grille, c'est affirmer que le travail du designer doit être **clair, transparent, objectif, fonctionnel et esthétique** — toutes qualités qui dépendent d'une pensée mathématique.

Müller-Brockmann formule l'éthique du designer en grille comme une série de volontés :

- Volonté d'ordre et de clarté
- Volonté de concentrer l'essentiel, d'éliminer le superflu
- Volonté de substituer l'objectivité à la subjectivité
- Volonté de rationaliser les processus créatifs et techniques
- Volonté d'intégrer couleur, forme et matière dans un système cohérent
- Volonté de domination architecturale de la surface et de l'espace

Toute œuvre visuelle créative est une manifestation du caractère du designer : son savoir, sa capacité, sa mentalité.

**Conséquence opérationnelle** : une grille ne se choisit pas après coup pour ranger un contenu existant. Elle se déduit en amont, à partir de la nature du problème (type de texte, volume d'images, usage du document).

---

## 2. Le système de mesure typographique

### Unités fondamentales

| Unité | Valeur |
|---|---|
| 1 point (pt) | 0,376 mm |
| 1 cicéro | 12 points = 4,51 mm |
| 1 m (typomètre) | 798 points = 66⅔ cicéros |
| 1 mm | 2,66 points |

**Règle d'or** : toutes les dimensions d'une grille (hauteur de champ, gouttière, interligne, marge) doivent être exprimées en points ou cicéros, jamais en millimètres seuls. Cela garantit que le texte et les images s'alignent exactement sur les lignes de la grille.

### Corps de texte courants

| Contexte | Corps recommandé |
|---|---|
| Texte courant (livre, rapport) | 8–10 pt |
| Texte courant (magazine) | 9–11 pt |
| Légendes | 6–8 pt |
| Titres display | 18–60 pt |
| Gros titres | au-delà de 60 pt |

Chaque corps existe en ~12 à 20 grades (tailles précises). La hauteur d'une ligne de texte = corps + interligne. L'interligne standard est de 1 à 3 lignes vides entre champs.

### Formats DIN

La norme DIN repose sur un principe d'auto-similarité : chaque format est le double du format inférieur. A0 = 841 × 1189 mm, A1 = 594 × 841 mm, etc. Avantages : stock normalisé, machines calibrées, enveloppes normalisées, tarifs postaux alignés. Un format hors-DIN impose une coupe avec perte matière.

---

## 3. Mécanique de la grille

### Définition structurelle

Une grille divise une surface en **champs** (fields) séparés par des **gouttières** (gutters). Chaque champ reçoit du texte, des images ou des illustrations. La plus petite image correspond au plus petit champ. Une image sur 2 champs, 3 champs, 4 champs, etc.

**Paramètres à fixer** :
1. Format de la page
2. Nombre de colonnes
3. Largeur des colonnes
4. Hauteur des champs (en nombre de lignes de texte)
5. Largeur de la gouttière horizontale (séparation entre colonnes)
6. Hauteur de la gouttière verticale (séparation entre rangées de champs)
7. Marges (haut, bas, intérieur, extérieur)

### Choix du nombre de colonnes

| Colonnes | Usage principal | Avantages | Risques |
|---|---|---|---|
| 1 | Texte pur, peu d'images | Simplicité absolue | Impossible de varier les tailles d'image |
| 2 | Rapport, brochure | Texte col. 1, images col. 2 — ou imbrication | Modéré |
| 3 | Magazine, catalogue | Flexibilité (peut se subdiviser en 6) | Colonnes étroites → petit corps obligatoire |
| 4 | Beaucoup d'images, statistiques | Richesse compositionnelle | Fragmentation si mal maîtrisé |
| 6 / 8 | Journaux, statistiques denses | Finesse maximale | Exige rigueur totale, petit corps |

**Règle** : moins il y a de différences de taille entre les illustrations, plus la composition paraît calme. La grille est un système de contrôle — elle rend la surface rationnellement organisable.

### Calcul des marges

Müller-Brockmann suit la règle classique de Jan Tschichold (basée sur la section d'or) :

```
Marge intérieure  : 1 unité
Marge haute       : 1,5 unité
Marge extérieure  : 2 unités
Marge basse       : 3 unités
```

Cette progression crée une tension optique naturelle qui "tient" la page. Toute marge égale de tous côtés est une erreur optique (elle paraît déséquilibrée visuellement).

Pour les formats courants, voir `references/CALCULS.md`.

### Alignement texte-grille

**Principe fondamental** : les lignes supérieures et inférieures de chaque champ de la grille doivent coïncider exactement avec une ligne de texte. Cela signifie que :

- la hauteur d'un champ = N × (corps + interligne)
- la gouttière verticale = M × (corps + interligne), avec M = 1, 2 ou 3 selon la densité voulue

**Méthode de construction** :
1. Choisir le corps du texte courant (ex. 9 pt) et l'interligne (ex. 12 pt → 9/12)
2. En déduire la hauteur d'une ligne (12 pt = 1 cicéro)
3. Définir combien de lignes tient chaque champ (ex. 12 lignes × 12 pt = 144 pt = 12 cicéros)
4. Fixer la gouttière = 1 ou 2 lignes vides (12 pt ou 24 pt)
5. Vérifier que la somme (champs + gouttières + marges) = hauteur imprimable

### Gouttières : règle des espaces vides

Pour N champs dans une colonne, il faut (N-1) espaces de gouttière. Pour 3 champs → 2 gouttières = 2 lignes vides. Pour 4 champs → 3 lignes vides. Les images dans un champ sont séparées par une seule ligne, ou plus si explicitement choisies.

---

## 4. Typographie dans la grille

### Corps et largeur de colonne

La largeur de colonne détermine mécaniquement le corps maximum utilisable. Une colonne trop étroite avec un corps trop grand produit trop peu de mots par ligne, ce qui force les césures et fatigue l'œil. Règle empirique :

- Une ligne de texte courant doit contenir 50–70 caractères
- En dessous de 35 caractères → lecture difficile
- Au-dessus de 80 caractères → l'œil perd le retour à la ligne

### Titres

Müller-Brockmann présente quatre positions possibles du titre par rapport au texte :

1. **En tête de page**, séparé du texte par du blanc — discret, élégant
2. **Gras au-dessus du texte**, même corps, séparé par une ligne vide — neutre
3. **Corps plus grand en tête** — accent fort, lecture hiérarchisée
4. **Corps encore plus grand**, contraste maximal entre titre et corps — le blanc entre les deux amplifie l'effet

### Polices recommandées (système Swiss)

Müller-Brockmann travaille principalement avec **Univers** (Adrian Frutiger, 1957) — famille complète, 21 graisses/largeurs, parfaite cohérence optique à toutes les tailles. Alternativement : Helvetica. Pour le corps serif : Garamond, Times, Clarendon (pour titres forts).

**Règle** : ne pas mélanger plus de 2 familles. Utiliser les variations de graisse et de corps d'une même famille plutôt que des polices différentes.

---

## 5. Application pratique — exemples du livre

### Magazine *Casabella* (architecture)
- Grille : 12 champs (3 colonnes × 4 rangées)
- Subdivision possible : 18 champs (3 × 6) selon la thématique
- Texte et images alignés
- Interligne entre image et texte : 2 lignes vides
- 3 tailles de caractères : titre, texte, légende
- Format : 31 × 24,5 cm, 108 pages

### Magazine *CCA Today* (USA)
- Grille : 65 champs — grille très fine pour maximum de flexibilité
- Grandes images alternant avec petites
- 3 corps : titres en noir ou bleu, medium et semi-bold
- Format : 43,1 × 28 cm, 4 pages
- Risque identifié par Müller-Brockmann : une grille trop fine peut induire le designer à négliger clarté et logique au profit de la variété

### Pictogrammes (CFF suisses, 1980)
- Basés sur une grille carrée (module de base)
- Longueur et épaisseur fixées par le module → cohérence du système
- Réduction à l'information minimale nécessaire

---

## 6. Grille et identité d'entreprise

La grille s'applique à tous les supports visuels d'une entreprise : carte de visite, affiche, formulaire, véhicule, signalétique bâtiment. L'unité visuelle repose sur la cohérence du système de grille, pas sur la répétition d'un logo seul.

---

## 7. Modes d'échec à éviter

| Erreur | Conséquence |
|---|---|
| Marges égales sur 4 côtés | Déséquilibre optique, page qui "flotte" |
| Champs non alignés sur l'interligne | Texte et image jamais exactement sur la même ligne de base |
| Trop de colonnes sans discipline | Fragmentation, lisibilité dégradée |
| Mélange de 3+ familles de caractères | Bruit visuel, perte de hiérarchie |
| Grille ignorée dans les sous-parties (légendes, encarts) | Rupture du système, cohérence perdue |
| Corps trop grand pour la largeur de colonne | Trop peu de mots/ligne, césures forcées |
| Gouttière insuffisante | Images qui se touchent → lecture impossible des légendes |

---

## 8. Références complémentaires

Lire `references/CALCULS.md` pour :
- Tableau complet des formats DIN (A0 → A7, B-series)
- Grilles types calculées pour A4 en 2, 3, 4 colonnes avec corps 9/12
- Conversions points ↔ mm ↔ cicéros
- Exemples de calcul complet (hauteur page → champs → interligne → vérification)
