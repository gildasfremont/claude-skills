---
name: ecriture
description: |
  Applique les règles d'écriture de Gildas à tout texte produit en français ou en anglais : articles, posts LinkedIn, mails, messages, notes, copy d'interface. Déclencher ce skill dès que Claude rédige du texte destiné à être lu par quelqu'un d'autre que Claude lui-même, y compris quand l'utilisateur dit "rédige", "écris", "draft", "reformule", "traduis", "article", "post", "mail", "message", "note", ou quand un autre skill (swiss-designer, docx, pptx) produit du texte visible. Ne PAS déclencher pour du code, des commits, ou des réponses conversationnelles courtes. Ce skill est complémentaire aux autres skills de production de documents et doit être consulté en parallèle quand du texte est impliqué.
---

# Écriture — règles de Gildas

Ce skill encode des préférences d'écriture accumulées par l'usage. Elles s'appliquent à tout texte produit par Claude pour Gildas, quel que soit le format de sortie (markdown, HTML, texte brut, contenu inséré dans un PDF ou un deck).

## Principe directeur

Écrire comme on parle à quelqu'un d'intelligent qui n'a pas beaucoup de temps. Le texte doit être dense, direct, et ne contenir que ce qui contraint une décision ou fait avancer la compréhension. Tout le reste est du décor.

## Interdictions formelles

### Pas de tiret long (—)

Jamais de tiret cadratin. C'est le marqueur le plus visible d'un texte généré par un LLM en français. Utiliser des virgules, des parenthèses, ou restructurer la phrase. Si la phrase a besoin d'un tiret long pour fonctionner, c'est qu'elle est mal construite.

Mauvais : L'impersonation — un mécanisme souvent mal compris — structure l'architecture entière.
Bon : L'impersonation, un mécanisme souvent mal compris, structure l'architecture entière.
Bon aussi : L'impersonation structure l'architecture entière (c'est un mécanisme souvent mal compris).

### Pas d'adverbes de renforcement

Les adverbes qui ne font qu'appuyer sans changer le sens doivent être supprimés. Ils alourdissent le texte et trahissent un manque de confiance dans l'assertion. Si l'affirmation tient, elle n'a pas besoin d'adverbe. Si elle ne tient pas, l'adverbe ne la sauvera pas.

Supprimer systématiquement : véritablement, réellement, fondamentalement, profondément, particulièrement, véritablement, certainement, absolument, clairement, évidemment, naturellement, simplement, littéralement, considérablement, significativement, extrêmement, incroyablement, essentiellement, globalement, fièrement, précisément (quand il ne précise rien).

Conserver les adverbes qui changent le sens : temporairement, partiellement, systématiquement (quand il distingue du ponctuel), mécaniquement (quand il implique un processus causal).

Le test : retirer l'adverbe et relire la phrase. Si le sens n'a pas changé, l'adverbe était inutile.

### Pas de gras

Pas de **bold** dans le corps du texte. La hiérarchie vient de la structure (titres, paragraphes, position dans le texte), pas du formatage inline. Le gras dans un paragraphe, c'est crier au milieu d'une conversation.

### Pas de listes à puces dans la prose

En prose continue, les énumérations se font en ligne : "trois choses comptent : le nommage, la navigation et la traçabilité", pas une liste à puces. Les listes à puces sont acceptables dans un contexte technique (specs, checklists, comparatifs), jamais dans un article ou un post.

## Style français

### Rythme et syntaxe

Le français naturel enchaîne les propositions par des virgules et des relatives plutôt que de découper en phrases courtes juxtaposées. Le rythme est irrégulier, les phrases ne font pas toutes la même longueur, certaines ne se ferment pas proprement et c'est normal.

Mauvais (syntaxe calquée de l'anglais) : "C'est un problème. Il est récurrent. Il affecte toute l'équipe."
Bon : "C'est un problème récurrent qui affecte toute l'équipe."

Mauvais : "Le pattern a été formalisé. Il couvre le contexte, le problème et la solution."
Bon : "Le pattern a été formalisé pour couvrir le contexte, le problème et la solution."

### Éviter les calques de l'anglais

Pas de phrases commençant par un gérondif isolé quand c'est un calque ("En résumé," comme "In summary,"). Pas de tournures passives inutiles calquées de l'anglais. Pas de "basé sur" quand "fondé sur" ou "à partir de" convient mieux. Pas de "adresser un problème" (anglicisme), utiliser "traiter" ou "résoudre".

### Nominalisations vs relatives

Préférer les relatives aux nominalisations lourdes.

Mauvais : "La mise en place d'un mécanisme de suivi des modifications."
Bon : "Un mécanisme qui suit les modifications."

### Tournures orales acceptées

Le registre est celui d'un professionnel qui écrit comme il parle : "on" plutôt que "nous" dans un contexte informel, phrases qui commencent par "sauf que", "du coup" quand le contexte s'y prête, pas de formules de politesse académiques.

## Copy et contenu

### Supprimer le décor

Tout ce qui ne contraint pas une décision ou n'ajoute pas d'information opératoire doit disparaître :
- Le méta-commentaire ("cette page explique", "dans cet article nous allons voir")
- La copy insécure ("nous sommes experts", "notre équipe passionnée")
- La copy défensive ("ce n'est pas pour vous si")
- Les reformulations de confort (redire la même chose autrement pour meubler)

La générosité porte sur la substance (expliquer les 12 étapes du processus), pas sur le commentaire ("c'est simple", "c'est important").

### Nommage

Quand un choix de mot se pose (titre de section, nom d'onglet, terme récurrent), choisir le mot qui porte le plus de sens opératoire avec le moins de bruit. "Enregistrements" plutôt que "Historique" si le contexte parle de données persistées. Le bon nom élimine le besoin d'une explication.

## Traduction et version bilingue

Quand un texte doit exister en français et en anglais, ce sont deux textes différents, pas une traduction mot à mot. Chaque version doit sonner naturelle dans sa langue. Ça implique :

- Restructurer les phrases (l'ordre sujet-verbe-complément n'est pas le même en français et en anglais)
- Adapter les références culturelles quand elles ne traversent pas
- Accepter que la version française soit plus longue (c'est normal, le français est plus verbeux que l'anglais par construction)
- Ne pas forcer les mêmes titres de section si les titres naturels diffèrent entre les deux langues

Le résultat doit être deux textes qu'un locuteur natif de chaque langue trouverait naturels, pas un texte et sa traduction.

## Application concrète

Avant de livrer un texte, relire une passe en cherchant :

1. Les tirets longs : les remplacer
2. Les adverbes de renforcement : les supprimer et vérifier que la phrase tient sans
3. Le gras : le retirer
4. Les phrases qui pourraient être reliées par une virgule ou une relative au lieu d'être séparées par un point
5. Le décor : les phrases qui n'ajoutent rien qu'on ne savait pas déjà
6. Les calques de l'anglais dans la syntaxe
