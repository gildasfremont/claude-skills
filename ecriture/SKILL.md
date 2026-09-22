---
name: ecriture
description: |
  Règles d'écriture de Gildas pour tout texte lu par quelqu'un d'autre que Claude, en français ou en anglais : études de cas et pages de portfolio, articles pour gildas.fyi, entrées et résumé LinkedIn, CV, lettres et champs libres de candidature, mails directs, messages d'approche, notes, copy d'interface. Déclencher dès que l'utilisateur dit rédige, écris, draft, reformule, réécris, traduis, relis, corrige, améliore, "ça sonne IA", "trop scolaire", "pas clair", "trop pub", "trop lapidaire", article, post, use case, étude de cas, portfolio, LinkedIn, CV, lettre, mail, message, note, ou quand un autre skill (swiss-designer, docx, pptx, docs) produit du texte visible. Le skill a un tronc (ce fichier), des branches par genre dans references/ et un linter dans scripts/ à lancer avant de livrer. Ne pas déclencher pour du code, des commits, ou une réponse conversationnelle courte.
---

# Écriture

Tronc commun à tout texte produit pour Gildas. Lire ce fichier, puis la branche du genre (tableau ci-dessous), puis lancer le linter et suivre `references/relecture.md` avant de livrer.

## Routeur

| Texte | Lire | Registre |
|---|---|---|
| Étude de cas, use case, page ou PDF de portfolio | `references/portfolio-use-case.md` puis `references/publication.md` | publication |
| Article pour gildas.fyi, billet long | `references/publication.md` | publication |
| Entrée d'expérience LinkedIn, section Infos, CV une page, CV détaillé | `references/linkedin-cv.md` puis `references/publication.md` | publication |
| Lettre, champ libre d'un formulaire, mail direct à un recruteur ou un hiring manager, message d'approche réseau | `references/candidature.md` puis `references/publication.md` | publication |
| Mail, message Slack ou WhatsApp, note interne, brief pour un agent | ce fichier seul | conversationnel |
| Copy d'interface, nommage | ce fichier, section Nommage | interface |

En plus, dans tous les cas : `references/tics-ia.md` quand le texte vient d'un brouillon LLM ou que Gildas dit qu'il sonne artificiel, `references/anglicismes.md` à la relecture, `references/relecture.md` pour la passe finale, `scripts/lint.py` avant de livrer.

## Ce que le texte doit faire

Écrire comme on parle à quelqu'un d'intelligent qui n'a pas le temps. Chaque phrase apporte un fait, une décision, une contrainte ou une conséquence. Une phrase qui commente, résume, annonce ou tire la leçon est supprimée : le lecteur tire la leçon lui-même, et Gildas trouve vulgaire qu'on la tire à sa place.

Trois tests par phrase :
1. Retirer la phrase. Le lecteur perd-il un fait ? Sinon elle part.
2. La phrase contient-elle un élément vérifiable (fonction d'une personne, chiffre, date, durée, nom d'objet : écran, tableau, règle, import, contrat) ? Un paragraphe sans élément vérifiable est du décor.
3. Se dirait-elle telle quelle, à voix haute, à la personne visée ? Sinon la réécrire jusqu'à ce que oui.

## Interdictions, tous registres

Tiret long. Jamais de cadratin (—) ni de demi-cadratin (–) en incise, ni de trait d'union entouré d'espaces qui joue ce rôle. Virgule, parenthèses, deux-points, ou deux phrases.
Mauvais : L'impersonation — un mécanisme souvent mal compris — structure l'architecture.
Bon : L'impersonation, un mécanisme souvent mal compris, structure l'architecture.

Gras dans le corps du texte. La hiérarchie vient des titres et de l'ordre, pas du formatage inline.

Listes à puces dans la prose. Les énumérations se font en ligne : "trois choses comptent : le nommage, la navigation et la traçabilité". Les puces restent pour les specs, les checklists, les comparatifs et les documents adressés à un agent.

Adverbes de renforcement. Supprimer : véritablement, réellement, fondamentalement, profondément, particulièrement, certainement, absolument, clairement, évidemment, naturellement, simplement, littéralement, considérablement, significativement, extrêmement, incroyablement, essentiellement, globalement, vraiment, totalement, parfaitement, précisément (quand il ne précise rien). Garder ceux qui changent le sens : temporairement, partiellement, systématiquement, mécaniquement. Test : retirer l'adverbe ; si le sens tient, il était de trop.

Phrase qui commente, conclut ou annonce. Ouvertures interdites : "Ce qui est intéressant, c'est", "Il est important de", "Notons que", "On voit que", "Cela montre", "Autrement dit", "En d'autres termes", "Dans cet article", "Cette page explique". Fermetures interdites : "En somme", "Au final", "Pour résumer", "C'est ça, le produit", "Ce que j'ai appris", "La leçon". Une maxime en fin de paragraphe (sujet = nom abstrait : la valeur, la confiance, le vrai travail) est remplacée par le dernier fait.

Formule sibylline ou semi-stylée. Phrase nominale posée pour l'effet ("Six mots."), phrase de chute ("Et c'est là que tout s'est joué."), antithèse "ce n'est pas X, c'est Y", question rhétorique. Réécrire en phrase complète, sujet, verbe, complément, avec le fait que la formule cachait.
Mauvais : Un défi de taille. Une équipe réduite. Un résultat à la hauteur.
Bon : L'équipe tenait à trois personnes et a livré la première version en dix semaines.

Chiffre ou fait inventé. Voir Faits.

## Français

Rythme. Le français relie les propositions par des virgules, des relatives et des deux-points ; il ne juxtapose pas des phrases de six mots. Cible en registre de publication : phrases de 8 à 35 mots, moyenne autour de 20, paragraphes de trois à six phrases. Pas plus d'une phrase de moins de sept mots par section, jamais deux de suite. Une phrase longue garde une principale et au plus deux subordonnées ; au-delà, couper à la deuxième.
Mauvais : C'est un problème. Il est récurrent. Il affecte toute l'équipe.
Bon : C'est un problème récurrent qui affecte toute l'équipe.

Verbes plutôt que noms. "La mise en place d'un mécanisme de suivi" devient "un mécanisme qui suit" ou "j'ai mis en place un suivi". Traquer : mise en place de, réalisation de, mise en œuvre de, définition de, élaboration de, optimisation de, prise en compte de.

Voix active avec un acteur. "Il a été décidé de reporter" devient "j'ai reporté" ou "le dirigeant a reporté". Un passif sans agent cache qui a décidé ; dans un texte de candidature, c'est ce que le lecteur veut savoir.

Information en tête. La première phrase d'un paragraphe porte le fait principal, les circonstances viennent après. Pas de "Après plusieurs mois de travail avec les équipes, nous sommes parvenus à" : le résultat d'abord.

Calques. Table complète dans `references/anglicismes.md`. Les plus fréquents : adresser un problème (traiter), faire sens (avoir du sens), supporter (prendre en charge), délivrer (livrer), impacter (peser sur), opportunité (occasion), en charge de (responsable de), basé sur (fondé sur, à partir de), au final (finalement), définitivement (certainement).

"On". Jamais comme substitut de "nous" dans un écrit qui reste (mail, note, document, article, LinkedIn, CV, lettre). "Je" pour ce qu'il a décidé et fait, "nous" quand le collectif est nommé juste avant. Le "on" impersonnel général ("on ne supprime pas un objet en base sans migration") reste possible, une fois par section au plus. Test : remplacer par "nous" ; si la phrase reste vraie, c'est un substitut, réécrire. Détail dans `references/publication.md`.

Registres. Conversationnel (mails, messages, notes internes) : "sauf que", "du coup" sont admis, pas de formule de politesse académique. Publication (portfolio, article, LinkedIn, CV, lettre) : règles de `references/publication.md`.

## Faits

Tout texte de candidature repose sur des faits à trois statuts : établi, à confirmer, trou. Un chiffre ou un fait que Gildas n'a pas donné s'écrit entre crochets avec son statut : [à confirmer : trois développeurs], [trou : résultat chiffré]. Ne jamais remplir un trou avec une valeur vraisemblable sans le marquer, ne jamais présenter une hypothèse comme un résultat. La source de vérité est le dépôt ~/dev/job-hunting (CLAUDE.md, experiences/, entreprises/) ; le lire avant d'écrire sur une expérience.

Ne jamais affirmer : un LLM intégré en production chez un client (il forme, automatise, construit ses outils, rien en production), du management de PM (contributeur individuel), un MBA (diplôme de GEM, grade de master), GetPro 2016 comme poste (client Grandwork seulement), Decathlon, Payfit.

## Documents existants

Quand le texte existe déjà (Google Doc, page du site, entrée LinkedIn, fichier du dépôt), relire la version en ligne juste avant, puis retoucher par remplacements ciblés. Ne jamais reconstruire depuis ce que Claude a en tête : Gildas édite entre deux échanges.

## Raisonnement

Définition avant heuristique. Une définition dit ce qu'est un concept, une heuristique donne un test pour vérifier qu'on s'en approche. "Un bon système, c'est celui que l'utilisateur décrit en une phrase" est une heuristique ; la définition, c'est que le système forme un tout cohérent. Poser la définition d'abord, l'heuristique en découle.

Pas de débat plaqué. Un principe qui structure une décision n'a pas besoin d'être projeté dans un débat extérieur pour peser. "Le système est un" ne prend pas position dans best-of-breed contre intégré ; il dit que le résultat doit fonctionner comme un tout. Le débat plaqué rend le texte contestable là où il n'avait pas à l'être.

Pas de symétrie forcée. La longueur d'une section dépend de ce qu'il y a à dire. Deux paragraphes suivis de six, c'est le signe que le texte suit le sujet plutôt qu'un gabarit.

Pas de verbatim comme béquille. À partir d'une source (rapport, transcription, notes), extraire l'idée et la reformuler dans le mouvement du texte. Ne garder une citation que si sa formulation exacte compte.

## Nommage

Quand un choix de mot se pose (titre de section, nom d'onglet, terme récurrent), choisir le mot qui porte le plus de sens opératoire avec le moins de bruit. "Enregistrements" plutôt que "Historique" si le contexte parle de données persistées. Le bon nom élimine le besoin d'une explication.

## Bilingue

Un texte qui existe en français et en anglais, ce sont deux textes, pas une traduction. Chaque version repart des faits et de la structure : ordre des mots différent, références culturelles adaptées, titres de section propres à chaque langue, version française plus longue par construction. Le résultat est deux textes qu'un natif de chaque langue trouve naturels.

## Avant de livrer

1. `python3 /mnt/skills/user/ecriture/scripts/lint.py texte.md` (chemin du skill ; ou le texte sur stdin). Traiter chaque signalement : corriger, ou garder avec une raison. Ne jamais ignorer.
2. Suivre `references/relecture.md`, passes dans l'ordre.
3. Livrer le texte, puis à part la liste des crochets restants. Rien d'autre : pas de récit des passes, pas de "j'ai veillé à".
