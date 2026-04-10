# Accessibilité : Référence Technique QA pour Design

## 1. Prévalence — les chiffres qui dimensionnent le problème

L'accessibilité n'est pas une feature pour une minorité. Les chiffres ci-dessous démontrent qu'une interface inaccessible casse pour des populations substantielles, et que ces populations se chevauchent.

### Daltonisme (Déficience de Vision des Couleurs)

- **Prévalence globale** : 8% des hommes, 0.5% des femmes (~300M de personnes dans le monde)
- **Répartition par type** (chez les hommes) :
  - Deutéranomalie (confusion rouge-vert, protanomalie : 5% des hommes
  - Protanomalie (confusion rouge-vert, réaction L-cône affaiblie) : 1% des hommes
  - Deutéranopie (absence complète perception vert) : 1% des hommes
  - Protanopie (absence complète perception rouge) : 1% des hommes
  - Tritanomalie/tritanopie (bleu-jaune) : très rare (<0.5%)

**Calcul d'impact** : un produit avec 1M d'utilisateurs a ~80,000 utilisateurs daltoniens. Une interface rouge-seule ne peut pas être lue par ces 80,000 personnes.

### Basse Vision (Vision non corrigible)

- **Prévalence** : 2.2 milliards de personnes (OMS 2019)
- **Causes principales** :
  - Erreur de réfraction non corrigée (myopie, hypermétropie)
  - Cataractes
  - Glaucome
  - Dégénérescence maculaire liée à l'âge (DMLA)
  - Rétinite pigmentaire
  - Diabète rétinopathie

**Mécanisme de rupture** : Ces utilisateurs nécessitent agrandissement de 200% à 400%, contraste élevé, ou tolérance au reflow à des résolutions extrêmes. Une interface cassant à 200% zoom élimine 2.2 milliards de potentiels utilisateurs.

### Cécité et Utilisateurs de Lecteur d'Écran

- **Prévalence directe** : ~40M personnes aveugles dans le monde
- **Utilisateurs de lecteur d'écran** : beaucoup plus large. Inclut aussi les personnes avec basse vision, trouble cognitif, ou handicap moteur. Estimation conservatrice : 150M+ personnes utilisent des lecteurs d'écran au moins occasionnellement

**Mécanisme de rupture** : L'interface n'est accessible que via l'arbre d'accessibilité. Si l'arborescence a11y est incorrecte, la personne ne peut pas naviguer.

### Handicap Moteur (Membre Supérieur)

- **Prévalence** : ~2.5% des adultes ont des limitations significatives du membre supérieur
- **Causes** :
  - Paralysie (spinal cord injury, AVC, cérébral palsy)
  - Amputation
  - Tremor (maladie de Parkinson, sclérose en plaques, alcoolisme chronique)
  - Blessures temporaires (bras cassé, entorse poignet, chirurgie)
  - Trouble musculo-squelettique / RSI (tendinite, syndrome du tunnel carpien)

**Calcul d'impact** : 1M utilisateurs = ~25,000 avec limitations motrices. Une interface requérant une précision 16px ou une coordination fine (double-click, drag-drop) casse pour ces 25,000 utilisateurs.

### Troubles Vestibulaires

- **Prévalence** : 35% des adultes 40+ ont expérimenté un dysfonctionnement vestibulaire
- **Déclencheurs** :
  - Parallaxe scrolling
  - Vidéo auto-play
  - Animations d'agrandissement/zoom
  - Infinite scroll avec scroll-jacking
  - Contenu clignotant ou en mouvement rapide

**Mécanisme de rupture** : Le système vestibulaire (inner ear) s'attend à une concordance entre le mouvement visuel et le mouvement physique. Si les yeux voient "le contenu scroll rapidement" mais le corps n'a pas bougé, nausée, vertiges, vomissement. Ce n'est pas une préférence — c'est une réaction physique involontaire.

### Handicap Cognitif

- **Prévalence** : 12.8% des adultes US ont un diagnostic de handicap cognitif
  - Dyslexie : ~10% de la population
  - ADHD : ~5% des adultes
  - Autisme : ~1-2% des adultes
  - Déficience intellectuelle : ~1% des adultes

**Mécanisme de rupture** : texte dense sans paragraphes, vocabulaire complexe, animations distrayantes, interfaces déroutantes sans landmarks clairs. Ces utilisateurs ont besoin de clarté extrême, de structures prévisibles, de feedback explicite.

### Temporaire et Situationnel

Ces contextes élargissent drastiquement la population affectée :

- **Soleil éclatant** : tout le monde a du mal à lire écrans bas-contraste en plein soleil
- **Un bras en plâtre** : n'importe qui peut temporairement être "handicapé moteur"
- **Environnement bruyant** : quelqu'un regardant une vidéo sans son a besoin de captions
- **Langue non-native** : vocabulaire complexe ou idiomatique crée une barrière cognitive
- **Batterie faible** : animations gourmandes affectent l'expérience sur batterie faible
- **Mauvaise connexion réseau** : contenu auto-play crée une latence et une consommation d'énergie

**Conclusion calcul** : Pour un produit avec 1M utilisateurs :
- ~80,000 daltoniens
- ~50,000 avec basse vision
- ~25,000 avec limitations motrices
- ~350,000 avec troubles vestibulaires
- ~128,000 avec handicap cognitif
- 100% ont vécu situationnel/temporaire

Une interface "classique" sans accessibilité casse pour **minimum 400,000+ des 1M utilisateurs**. Ce n'est pas une edge case.

---

## 2. Contraintes Visuelles

### Contraste

Le contraste est calculé, pas estimé. Les yeux trompent; les formules WCAG ne trompent pas.

#### Formule WCAG luminance

Le ratio de contraste est le ratio des luminances des deux couleurs (plus claire / plus foncée) :

1. Prendre les valeurs sRGB 0–255
2. Normaliser : diviser par 255 → valeurs 0–1
3. Linéariser chaque canal (R, G, B) :
   - Si C_sRGB ≤ 0.04045 : C_linear = C_sRGB / 12.92
   - Sinon : C_linear = ((C_sRGB + 0.055) / 1.055) ^ 2.4
4. Calculer luminance relative : L = 0.2126 × R_lin + 0.7152 × G_lin + 0.0722 × B_lin
5. Ratio de contraste : (L_plus_clair + 0.05) / (L_plus_fonce + 0.05)

**Exemple concret** : #767676 (gray) sur #FFFFFF (white)
- #767676 sRGB : R=118/255=0.463, G=118/255=0.463, B=118/255=0.463
- Linéarisation : (0.463 + 0.055)^2.4 / 1.055^2.4 ≈ 0.176
- L_gray = 0.2126 × 0.176 + 0.7152 × 0.176 + 0.0722 × 0.176 ≈ 0.176
- #FFFFFF : L_white = 1.0
- Ratio : (1.0 + 0.05) / (0.176 + 0.05) = 1.05 / 0.226 ≈ **4.65:1**

Outils pour calculer : WebAIM Contrast Checker, axe DevTools, Contrast Lab.

#### Seuils WCAG 2.1

- **AA (standard minimum)** :
  - Texte normal (< 18pt) : ≥ 4.5:1
  - Texte large (≥ 18pt ou ≥ 14pt gras) : ≥ 3:1
  - Composants UI et bordures focus : ≥ 3:1
- **AAA (enhanced)** :
  - Texte normal : ≥ 7:1
  - Texte large : ≥ 4.5:1

#### APCA (Advanced Perceptual Contrast Algorithm) — WCAG 3 draft

APCA modélise le contraste comme asymétrique : le texte clair sur fond foncé a des seuils différents du texte foncé sur fond clair. Aussi facteur pour : distance de lecture, fatigue, âge.

- Métrique : Lc (lightness contrast), -0 à ±110 (polarité incluse)
- **Texte de corps** : |Lc| ≥ 75
- **Texte large** : |Lc| ≥ 60
- **Non-texte (UI, icon)** : |Lc| ≥ 45

APCA est plus précis que WCAG 2 mais pas encore finalisé. Utilisé par des design systems modernes (Apple, Google).

#### Cas limites courants

- **Texte disabled** : WCAG ne requiert pas 4.5:1 pour les éléments disabled. Mais les utilisateurs doivent quand même percevoir qu'ils sont présents mais inactifs. Cible minimum : 3:1 même pour disabled.
- **Placeholder text** : #999 sur blanc ne passe pas 4.5:1. Les placeholders doivent être aussi contrastés que le texte saisi si c'est l'étiquette effective.
- **Bordures focus** : une bordure 2px non-contrastée est invisible. Focus outline doit passer 3:1 contre les couleurs adjacentes.

### Indépendance Couleur

**Règle WCAG 1.4.1** : La couleur ne doit pas être le seul moyen de transmettre l'information.

#### Défaillances courantes

- Statut rouge/vert sans icône ou texte ("✓" ou "Error")
- Lien distingué que par couleur (pas de soulignement)
- Erreur de form indiquée par une bordure rouge seule (pas de texte d'erreur)
- Graphique où les séries ne sont distinguées que par couleur

#### Solutions

Ajoutez un canal redondant : forme, motif, texte, soulignement, icône, notation.

**Exemple** : Au lieu de [Approved (vert)] [Rejected (rouge)]
→ [✓ Approved] [✗ Rejected] ou [Approved (check icon, green) Rejected (X icon, red)]

#### Test rapide

Convertissez la page en grayscale (OS settings ou DevTools filter). Si de l'information disparaît, la conception échoue.

### Mouvement et Vestibulaire

#### Media Query prefers-reduced-motion

CSS :
```css
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

JavaScript :
```javascript
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
```

Doit être respectée pour **tous** les contextes d'animation :
- Parallax scrolling : désactiver complètement
- Auto-play vidéo/animation : désactiver ou réduire
- Zoom transitions : devenir instantané
- Scroll-linked animations : disparaître
- Carousel auto-advance : arrêter

#### WCAG 2.3.1 (Seizure and Physical Reactions)

Aucun contenu ne doit clignoter plus de **3 fois par seconde**.

#### WCAG 2.2.2 (Pause, Stop, Hide)

Tout contenu auto-moving, blinking ou scrolling durant > 5 secondes doit avoir un mécanisme pause/stop accessible.

**Mécanisme physique** : Le système vestibulaire s'attend à une correspondance entre le signal visuel et la proprioception/accélération. Si les yeux voient du mouvement mais le corps ne bouge pas, conflit sensoriel → nausée, vertiges, vomissements. Ce n'est pas une préférence cosmétique.

### Taille de Texte et Reflow

#### Tailles lisibles

- Défaut navigateur : 16px
- Minimum sur écran : 12px (dépend du contexte)
- Corps texte web : 16–18px recommandé
- Distinction AA vs AAA texte n'existe que pour contraste, non pour taille

#### Zoom du navigateur

**WCAG 1.4.4** : Les utilisateurs doivent pouvoir zoomer à 200% sans perdre du contenu ou de la fonctionnalité.

- Layout ne doit pas casser (wrapping acceptable, hidden content pas acceptable)
- Contenu ne doit pas être caché
- Scroll horizontal ne doit pas être requis pour lire

#### Override OS/navigateur

Respectez les unités relatives (rem, em). N'utilisez pas `font-size: 12px` sur du corps texte. Utilisez `font-size: 1rem` ou `font-size: 0.875rem` si vous devez.

#### Reflow : WCAG 1.4.10

À 400% zoom (viewport équivalent 320px), le contenu doit reflow en colonne unique sans scroll horizontal **sauf** :
- Tableaux de données
- Toolbars complexes
- Images/vidéos complexes

Tester : DevTools → Device Emulation → responsive → 320px width, puis Ctrl+Shift+M pour zoom navigateur à 400%.

---

## 3. Contraintes Motrices

### Loi de Fitts

Mouvement vers une cible peut être modélisé mathématiquement :

**MT = a + b × log₂(1 + D/W)**

Où :
- **MT** = Movement Time (temps avant activation)
- **D** = Distance entre curseur et cible
- **W** = Largeur de la cible dans la direction du mouvement
- **a, b** = constantes empiriques (~0.1s et ~0.1s)

**Implication** : Une cible de 20px loin du curseur prend exponentiellement plus de temps à frapper qu'une cible de 44px près du curseur. Les coins/bords sont "infiniment larges" dans une direction (condition limite de Fitts).

**Failure example** : Close button 16×16px en haut-droite d'une modal. L'utilisateur tremor les manque régulièrement. Solution : 44×44px avec padding invisible pour l'hit target.

### Cibles Tactiles

#### Standards

- **WCAG 2.5.8 AA** : Minimum 24×24 CSS pixels (exceptions : inline text links, contexte phrase)
- **Apple HIG** : 44×44 points minimum
- **Material Design** : 48×48 dp minimum
- **Best practice** : 44×44 CSS px. La cible peut être plus large que le visual element (padding compte)

#### Espacement

Les cibles doivent avoir ≥ 8px d'espacement pour éviter l'activation accidentelle d'éléments adjacents.

#### Cas d'échec courants

- 16×16 icon buttons sans padding
- Close buttons dans les coins
- Menu items espacés de 4px
- Liens texte densément packés sans padding vertical

### Clavier

#### Opérabilité complète

Tous les éléments interactifs doivent être opérables au clavier :

- **Tab** : naviguer forward
- **Shift+Tab** : naviguer backward
- **Enter** : activer button
- **Space** : activer button (parfois checkbox, radio)
- **Escape** : fermer dialog, menu, tooltip
- **Arrow keys** : naviguer dans composite widgets (tabs, menu, radio group, listbox)

Aucun élément ne peut être accessible **uniquement** à la souris.

#### Focus visible

Focus doit être visible : outline du navigateur par défaut (acceptable) ou custom indicator qui passe 3:1 contrast contre les couleurs adjacentes.

Pas acceptable : `outline: none` sans replacement. Pas acceptable : outline 1px gris sur blanc (trop bas contraste).

#### Ordre de focus

**WCAG 2.4.3** : L'ordre de Tab doit correspondre à l'ordre visuel/lecture. Ne pas utiliser `tabindex > 0` (crée un ordre insane). `tabindex="0"` pour éléments custom qu'on veut dans l'ordre. `tabindex="-1"` pour éléments programmatiquement focusables (ex: alert dialogs).

#### No keyboard trap

**WCAG 2.1.2** : L'utilisateur doit pouvoir Tab AWAY de tous les composants. Cas courants d'erreur :

- Modal dialog sans gestion de focus (focus peut être piégé à l'intérieur)
- Custom video player sans Escape pour exiter
- Rich text editor (contenteditable) où Tab insère une indentation au lieu de quitter

Solution : À la fin du dernier focusable element de la dialog, Tab → first element. Escape toujours ferme la dialog.

#### Skip links

Le premier Tab stop de la page doit être "Skip to main content". Essentiel pour utilisateurs clavier qui naviguent répétitivement (header, nav, breadcrumbs prennent 20+ tabs).

CSS : `#skip { position: absolute; left: -9999px; } #skip:focus { left: 50%; transform: translateX(-50%); }`

HTML : `<a href="#main" id="skip">Skip to main content</a> ... <main id="main">`

### Interactions Hover-Dépendantes

#### Règle WCAG 1.4.13 : Hover/Focus Equivalent

Tout ce que vous déclenchez au **hover** doit aussi fonctionner au **focus**. Les utilisateurs clavier ne peuvent pas hover.

#### Tooltips

- Persistent : ne pas disparaître quand pointer quitte le trigger
- Dismissible : Escape ferme
- Hoverable : pointer peut se déplacer vers le contenu du tooltip sans qu'il disparaisse

Mauvais pattern : tooltip disparaît quand souris quitte l'icône.

#### Dropdown menus sur hover

Utilisateurs clavier ne peuvent pas hover. Solution :

- Open au Enter/Space
- Navigate avec Arrow Up/Down
- Escape ferme
- Enter/Space sur option la sélectionne

---

## 4. Mécanique des Screen Readers

### Arbre d'Accessibilité

Le navigateur construit une **accessibility tree** parallèle au DOM. Les lecteurs d'écran lisent CET arbre, pas le DOM visuel.

Chaque nœud de l'arbre a :
- **Role** : ce que l'élément est (button, link, heading, dialog, tab, etc.)
- **Name** : comment le lecteur l'annonce (text, aria-label, alt text)
- **State** : disabled, pressed, expanded, checked, etc.
- **Relations** : parent, children, controlledBy, labelledBy, etc.

**Si l'arbre a11y est incorrecte, l'experience du lecteur d'écran est incorrecte, peu importe l'apparence visuelle.**

Inspectez avec : Chrome DevTools → Accessibility tab, ou Firefox Accessibility Inspector.

### Headings et Document Outline

Les utilisateurs de lecteur d'écran naviguent par **H key** (NVDA, JAWS) ou rotor (VoiceOver). Les headings créent l'outline du document.

#### Hiérarchie

Doit être strictement hiérarchique : H1 > H2 > H3. Pas de sauts de niveaux.

Mauvais : H1 "Products" → H3 "Category A"
Bon : H1 "Products" → H2 "Category A" → H3 "Subcategory A.1"

#### Un H1 par page

Chaque page doit avoir exactement un H1. C'est la déclaration du sujet de la page.

#### Erreur courante

Utiliser heading tags pour styliser (h1 { font-size: 16px; } pour faire un titre petit). Utilisez un vrai heading et stylisez; pas un div avec une apparence de heading.

### Texte Alternatif (Alt Text)

#### Images informatives

Chaque `<img>` doit avoir un `alt` attribute.

- Décrivez l'**information communiquée**, pas l'apparence visuelle
- Bon : alt="Chart: sales increased 20% Q1 vs Q4"
- Mauvais : alt="graph", alt="image", alt="sales_chart.png"

#### Images décoratives

`alt=""` (vide, pas absent). L'attribut alt absent signale une omission; alt vide signale "ignorez ceci".

```html
<img src="divider.svg" alt="" /><!-- Decorative -->
<img src="chart.png" alt="Sales Q1: $50M" /><!-- Informative -->
```

#### Images complexes

Pour charts, diagrammes, infographiques : short alt + long description.

Options :
1. `<figcaption>` : `<figure><img alt="Chart"><figcaption>Full description…</figcaption></figure>`
2. `aria-describedby` : `<img alt="Chart" aria-describedby="desc"><div id="desc">Full description…</div>`
3. Lien de description : `<img alt="Chart"><a href="/chart-data">Full description</a>`

### ARIA (Accessible Rich Internet Applications)

#### Première règle

**Ne pas utiliser ARIA si un élément HTML natif le fait.** `<button>` > `<div role="button">`. Native elements ont :
- Keyboard handling intégré
- Focus management
- State communication (désactivé, enfoncé, étendu)

#### Roles

Définissent ce que l'élément **est** : button, link, heading, tab, dialog, menu, progressbar, slider, etc.

Exemples :
```html
<div role="button">Submit</div><!-- Only if no <button> possible -->
<div role="tab" aria-selected="true">Tab 1</div>
<div role="dialog" aria-modal="true">Modal content</div>
```

#### States et Properties

Communiquent l'état/propriété au lecteur :

- `aria-checked` : true/false/mixed (pour role="checkbox", radio, etc.)
- `aria-expanded` : true/false (pour role="button" contrôlant un contenu caché)
- `aria-selected` : true/false (pour role="tab", role="option")
- `aria-disabled` : true/false (pour tout élément qu'on veut appear disabled)
- `aria-hidden` : true (pour cacher du contenu de l'arbre a11y)
- `aria-label` : nom de l'élément quand pas de text visible
- `aria-labelledby` : pointeur vers un élément qui labelle celui-ci
- `aria-describedby` : pointeur vers un élément qui décrit celui-ci
- `aria-required` : true (pour input requise)
- `aria-errormessage` : pointeur vers un message d'erreur lié

#### Live Regions

`aria-live` annonce des mises à jour de contenu dynamique sans que l'utilisateur ne navigue vers :

```html
<div aria-live="polite" aria-label="Form validation">
  <!-- Error messages appear here -->
</div>
<div aria-live="assertive">
  <!-- Time-sensitive alerts: "Payment failed" etc -->
</div>
```

- `polite` : annonce quand l'utilisateur est inactif
- `assertive` : interrompt l'utilisateur immédiatement

Utilisé pour : validation form, toast notifications, loading states, chat messages.

#### Erreurs ARIA courantes

1. Role sans propriétés requises : `role="checkbox"` sans `aria-checked`
2. `aria-label` sur non-interactive : `<div aria-label="Title"></div>` n'a aucun effet
3. IDs dupliquées dans `aria-labelledby` ou `aria-describedby`
4. Trop de ARIA : 20+ rôles et propriétés sur 5 éléments = confusion
5. Pas de Native HTML : `<div onclick="..." role="button">` quand `<button>` est dispo

### Labels de Formulaire

#### Association programmatique

Chaque input doit avoir un label associé :

```html
<!-- Correct -->
<label for="email">Email address</label>
<input id="email" type="email" />

<!-- Also correct -->
<label>
  Email address
  <input type="email" />
</label>

<!-- ARIA fallback -->
<input aria-label="Email address" />
```

#### Placeholder n'est pas un label

Placeholder :
- Disparaît au typing
- Bas contraste souvent
- Pas annoncé comme label par tous les lecteurs d'écran

Seul placeholder
Label + placeholder (placeholder comme hint, "e.g. john@example.com")

#### Messages d'erreur

Associez avec `aria-describedby` ou `aria-errormessage` :

```html
<input id="zip" aria-describedby="zip-error" />
<span id="zip-error" role="alert">Zip must be 5 digits</span>
```

#### Champs requis

```html
<label for="name">
  Name <span aria-label="required">*</span>
</label>
<input id="name" required aria-required="true" />
```

---

## 5. Tests Automatisés vs Manuels

### Tests Automatisés

Outils : axe-core, Lighthouse, WAVE, Deque, Siteimprove.

#### Ce qu'ils détectent (~30–40% des enjeux WCAG)

- Alt text missing
- Form labels missing or incorrectly associated
- Insufficient contrast (computed, not visual)
- Heading hierarchy broken (h2 after h1 → h4)
- Duplicate IDs
- Invalid ARIA attributes or roles
- Missing lang attribute on html
- Missing form associations
- Empty buttons or links
- Color not sole info carrier (limited detection)

#### Ce qu'ils NE peuvent PAS détecter

- Qualité du alt text (syntaxiquement présent, sémantiquement mauvais)
- Logical reading order
- Meaningful focus order
- Keyboard operability de custom widgets (un slider custom avec role="slider" ne teste pas les arrow keys)
- Sensibility of heading structure (h1 → h2 → h2 → h2 vs h1 → h2 → h3 → h3)
- Correctness d'usage ARIA en contexte
- Whether color is sole info (rules sont trop basiques)

#### axe-core

Standard d'industrie. Zéro politique faux positif. Disponible comme :
- Browser extension (Chrome, Firefox, Edge)
- Playwright/Cypress integration
- CI/CD (GitHub Actions, Jenkins, etc.)
- API en ligne

#### Lighthouse

Google DevTools. Utilise axe-core en interne. Score 0–100. Couverture : ~30% des enjeux.

#### WAVE

WebAIM overlay visual. Bonne pour scans visuels rapides. Inclut plugins.

### Tests Manuels (Indispensables)

#### Keyboard Test

Débranchez la souris. Tab à travers toute la page.

Checklist :
- [ ] Pouvez-vous atteindre tous les éléments interactifs?
- [ ] Pouvez-vous activer chaque élément (Enter, Space, Arrows)?
- [ ] Voyez-vous toujours où le focus est?
- [ ] Pouvez-vous échapper de partout (Escape de modals, Shift+Tab, etc)?

#### Screen Reader Test

VoiceOver (Mac: Cmd+F5), NVDA (Windows, gratuit), TalkBack (Android).

Naviguer par :
- **Headings** (H key dans NVDA, rotor dans VO)
- **Landmarks** (D key, région principale)
- **Form controls** (F key)
- **Links** (K key)

Écoutez sans regarder l'écran. Est-ce logique? Manque-t-il du contexte?

#### Zoom Test

Zoom navigateur 200%, puis 400%. DevTools → Device Emulation ou native zoom.

- [ ] Content reflows ou hors viewport?
- [ ] Éléments se chevauchent?
- [ ] Scroll horizontal requis pour lire?
- [ ] Buttons/inputs restent cliquables?

#### Grayscale Test

OS settings (Accessibility → Display) ou DevTools filter.

- [ ] Statuts distingués sans couleur?
- [ ] Tous les liens identifiables?
- [ ] Focus visible sans couleur?

#### Color Vision Deficiency Simulation

DevTools → Rendering → Emulate CSS media feature prefers-color-scheme ou extension CVD (Color Oracle, Accessibility Inspector).

Teste deutéranomalie (red-green, 5% des hommes), tritanomalie (blue-yellow, rare).

#### Motion Test

OS setting prefers-reduced-motion ou DevTools. Vérifiez : animations arrêtent? Parallax disparaît? Auto-play désactif?

---

## 6. Checklist de Vérification par Pattern de Rupture

### "Je ne peux pas lire le texte"

- [ ] Contraste ≥ 4.5:1 pour all body text (computed via WebAIM)
- [ ] Texte scales 200% sans loss (DevTools zoom)
- [ ] Content reflows 400% zoom sans horizontal scroll
- [ ] Pas de texte in images (sauf logos)
- [ ] Font-size en relative units (rem, em, %) pour body
- [ ] Line-height ≥ 1.5
- [ ] Letter-spacing suffisant (pas < 0.12em)

### "Je ne peux pas distinguer les éléments"

- [ ] Couleur n'est pas le seul différenciateur
- [ ] Focus indicator visible (≥ 3:1 contrast)
- [ ] Éléments interactifs "look" interactifs (couleur, soulignement, padding)
- [ ] États distingués sans couleur seule (hover, disabled, selected)
- [ ] Bordures/shadows utilisés pour distinction
- [ ] Icons ont alt text ou aria-label

### "Je ne peux pas naviguer"

- [ ] Tous interactive elements Tab-reachable
- [ ] Focus order matches visual/reading order
- [ ] Pas de keyboard traps
- [ ] Skip link présent (first Tab stop)
- [ ] Headings h1→h2→h3 (pas de sauts)
- [ ] Un H1 par page
- [ ] Landmarks : main, nav, contentinfo présents
- [ ] Lang attribute sur html

### "Mon screen reader ne comprend pas"

- [ ] Images avec appropriate alt (descriptive, non "image")
- [ ] Form inputs avec labels (ou aria-label)
- [ ] ARIA roles, states, properties correctes
- [ ] Live regions pour contenu dynamique
- [ ] Tables avec th, caption, headers
- [ ] Buttons vs links (semantique correcte)
- [ ] Arbre a11y inspecté et logique

### "L'interface me rend malade"

- [ ] prefers-reduced-motion respected (animations 0.01ms ou disable)
- [ ] Pas auto-play video sans contrôles
- [ ] Pas content flashing > 3x/sec
- [ ] Scroll-linked animations disableable
- [ ] Parallax disabled ou très subtle
- [ ] Infinite scroll n'a pas scroll-jacking
- [ ] Carousel ne auto-advance ou pause sur focus

### "Je ne peux pas cliquer/tapper"

- [ ] Touch targets ≥ 44×44 CSS px
- [ ] Spacing ≥ 8px entre targets
- [ ] Hover content aussi available on focus
- [ ] Pas double-click required (single tap OK)
- [ ] Pas time-limited interactions sans extension option
- [ ] Drag-drop has keyboard alternative (ou paste, upload)
- [ ] No motion/gesture-only interactions

---

## 7. Workflow QA Recommandé

### Étape 1 : Scan Automatisé

Exécutez **axe-core** sur chaque page/état (empty, loading, error, filled, etc.).

- Corrigez tous issues "Critical" et "Serious"
- Note : "Minor" issues souvent faux négatifs manuellement; à investiguer
- Output : rapport CSV/JSON par page

### Étape 2 : Keyboard Walkthrough

Débranchez la souris. Tab à travers le flow entier.

Notez :
- Éléments non-accessible au Tab
- Keyboard traps
- Focus invisible ou mal-visible
- Focus order illogique
- Échecs d'opération (Enter ne soumet pas form, etc.)

### Étape 3 : Screen Reader Check

Lancez **VoiceOver** (Mac: Cmd+F5) ou **NVDA** (Windows).

- Naviguez par headings. Est-ce logique? Manque H1?
- Lisez les formulaires. Labels clairs? Messages d'erreur associés?
- Déclenchez contenu dynamique (dropdown, modal, toast). Annoncé?
- Écoutez page entière. Est-ce compréhensible sans vidéo?

### Étape 4 : Visual Checks

Ensemble :
- **Zoom** 200%, puis 400%. Reflow? Overlap? Horizontal scroll?
- **Grayscale**. Info disparaît?
- **CVD simulator**. Statuts distingués?
- **prefers-reduced-motion ON**. Animations arrêtent?
- **Contrast checker**. All text ≥ 4.5:1?

### Étape 5 : Rapport

Listez issues par sévérité (bloc vs major vs minor). Pour chaque :

- **Quoi est cassé** : "Form validation messages not announced"
- **Qui est affecté** : "1.2M users with screen readers (population + mechanism)"
- **Comment corriger** : "Add aria-live="polite" to validation container"
- **WCAG criterion** : WCAG 4.1.3 Status Messages

Exemple :
```
BLOCKER: Form error messages not announced
Affected: ~1.2M screen reader users cannot know validation failed
Mechanism: aria-live not present; screen reader reads outdated page state
Fix: Wrap error container in <div aria-live="polite" aria-atomic="true">
WCAG: 4.1.3 Status Messages (Level A)
```

---

## Notes Finales

Accessibilité est engineering constraint, non feature. Les chiffres ci-dessus — 80,000 daltoniens, 2.2B low-vision, 25,000 motor — ne sont pas politiquement corrects ou advocacy. Ce sont **les populations pour lesquelles votre design casse**, mesurées par **le mécanisme spécifique de rupture** (contrast ratio calculation, screen reader arbre a11y, keyboard reachability, vestibular mismatch).

Tester manuellement est non-négociable. Automatisé détecte 30–40%; le reste requiert des yeux et des oreilles (ou des outils d'accessibilité et un vrai utilisateur).

Commencez par les blockers : afficher, lire, naviguer, cliquer. Priorisez par population × impact.
