# Étude de cas de portfolio (PM)

Lecteur : un hiring manager ou un CPO, cinq minutes au plus, souvent sur téléphone depuis LinkedIn. Il cherche une décision que Gildas a prise quand la réponse n'était pas évidente, ce qu'elle a coûté, et ce qui en est sorti. Il ne cherche ni la méthode ni les écrans. Un dossier de PM se distingue d'un dossier de designer par la place donnée aux preuves, aux options, aux arbitrages et aux résultats plutôt qu'aux maquettes.

Lire d'abord `publication.md` pour le registre. Ce fichier donne la structure et les règles propres au cas.

## Choisir les cas

Trois à cinq cas. Un cas entre s'il contient une décision à raconter avec au moins une alternative écartée. Un cas de pure exécution n'entre pas, même long ou bien payé. Le premier cas est le plus fort pour le poste visé, pas le plus récent. Pour un poste Senior ou Staff en SaaS B2B, les candidats naturels sont rôles et droits Lucca, SI Guinet-Derriaz, conformité Synaxe, Rungle (projet arrêté), Ornikar (candidat libre) ; BMI System et Chunk se traitent en cas courts.

## Gabarit long (800 à 1 500 mots)

Sous-titres de gabarit admis. Chaque section a une longueur cible et un contenu obligatoire.

1. Titre. L'objet ou le problème, sans slogan : "Administration des rôles et des permissions chez Lucca", "Un système d'information pour un groupe de quatorze carrières". Un titre d'article ("Les mots et les boîtes") reste sur l'article.

2. Chapeau, trois phrases, qui tiennent seules. Phrase 1 : l'entreprise et le problème, avec un chiffre. Phrase 2 : ce que Gildas a fait, passé composé, première personne. Phrase 3 : le résultat ou l'état (livré, conçu et remis, arrêté). Le chapeau est ce que lit celui qui ne lira rien d'autre.
Exemple : Lucca vend une suite RH à 9 000 clients ; son modèle de droits pouvait représenter n'importe quelle règle d'accès, au prix d'une administration que plus personne ne savait lire. En dix jours de cadrage puis six de design, j'ai redéfini le modèle mental des rôles sans toucher au moteur d'autorisation. Le guide de doctrine 2026 en est sorti ; la construction s'est faite après mon départ.

3. Contexte, 80 à 150 mots. L'entreprise (taille, marché, chiffres publics vérifiés dans entreprises/), ce qui était en jeu pour son activité (une vente bloquée, une obligation légale, une marge invisible), et une phrase de rôle obligatoire : "J'étais [rôle], [N] jours, en direct avec [fonctions]." Interdit : "en collaboration avec les équipes".

4. Le problème reçu et le problème réel, 100 à 200 mots. Formule : "La demande : X. [Ce qui a été fait pour comprendre] a montré que Y." Le décalage entre X et Y est le premier signal de jugement. S'il n'y en a pas, dire que la demande était juste et pourquoi.

5. Contraintes, 50 à 100 mots, en prose. Trois au plus : technique (ne pas toucher au moteur), moyens (deux développeurs, dix jours, 100 k€), politique ou réglementaire (une échéance légale, un client qui refuse). Chaque contrainte reviendra dans la décision ; une contrainte qui ne revient pas est supprimée.

6. Options et arbitrage, 150 à 300 mots. C'est la section qui fait le niveau. Au moins une alternative écartée avec sa raison. Formule : "Deux voies. A : [ce qu'elle donnait], mais [ce qu'elle coûtait]. B : [ce qu'elle donnait], mais [ce qu'elle coûtait]. J'ai retenu B parce que [critère]. Ce que ça a coûté : [...]." Nommer qui poussait quelle option quand c'est vrai (le référent technique, le CS). Si Gildas a perdu un arbitrage, l'écrire : "J'ai plaidé pour X. Le dirigeant a tranché pour Y. [Ce qui s'est passé ensuite.]" C'est la phrase qu'un hiring manager lit deux fois.

7. Ce qui a été fait, 150 à 300 mots. Verbes, objets, ordre. La méthode n'apparaît que si elle a produit une décision ("les onze entretiens ont déplacé le problème de l'interface au modèle de données"). Pas de Double Diamond, pas de "phase de discovery" comme étape en soi, pas de liste d'ateliers.

8. Statut, une à trois phrases, obligatoire. Trois formules au choix :
- Livré : "L'outil de facturation est en production depuis [date] chez [N] clients."
- Conçu et remis : "Les parcours et le guide de doctrine ont été remis en juillet 2025 ; la construction s'est faite après mon départ et je ne prétends pas en connaître chaque arbitrage."
- Proposé, non retenu : "J'ai recommandé X. L'entreprise a retenu Y."
Ne jamais laisser croire qu'une proposition a été livrée. Le lecteur senior teste ce point en entretien.

9. Résultat, 50 à 150 mots. Dans l'ordre de préférence :
- Mesuré : le chiffre, sa source, sa période. "Dix contrats signés la première année [à confirmer]."
- Observé : le fait et qui l'a constaté. "La revue de salaires sert aujourd'hui de démonstration commerciale, d'après le responsable de suite."
- Compté : ce qui se compte sans instrumentation. Écrans (vingt à trois), jours, contrats, personnes formées, sites, applications couvertes.
- Plan de mesure : "Ce qui aurait permis de vérifier : la part d'utilisateurs avec un seul rôle, le nombre d'accès temporaires encore présents trente jours après un go-live." Au conditionnel passé, une phrase, jamais présenté comme un résultat.
Interdits : "impact significatif", "forte adoption", "retours très positifs", "a permis d'améliorer" sans objet mesuré.

10. Ce que je referais autrement, 50 à 100 mots. Un fait et une décision qu'il prendrait différemment, sans morale. "Je ferais les entretiens sur site avant l'audit du produit, pas après : deux semaines passées à auditer un outil dont le blocage était réglementaire."

## Gabarit court (120 à 200 mots, carte ou liste)

Chapeau (les trois phrases), une phrase de décision ("J'ai retenu B plutôt que A parce que..."), le statut, le lien vers le cas long. Rien d'autre.

## Métriques absentes

Ne pas combler. Quatre techniques, dans l'ordre :
1. Compter ce qui se compte (section 9, "compté").
2. Rapporter un résultat observé avec sa source.
3. Écrire le plan de mesure au conditionnel passé.
4. Dire l'absence en une phrase et passer : "Aucune métrique n'a été instrumentée sur cette refonte."

Un cas sans chiffre est possible s'il a une décision forte. Un cas avec un chiffre inventé disqualifie tout le dossier.

## Projet arrêté

Rungle est le cas type. Structure propre :
1. La thèse de départ, une phrase.
2. Le signal cherché et le seuil fixé d'avance ("un client pilote signé fin janvier 2026, sinon nous arrêtions").
3. Ce qui a été fait pour l'obtenir (entretiens, démos, MVP), avec les chiffres réels.
4. Ce qui a été observé, y compris ce qui a réorienté le produit.
5. La décision d'arrêt à la date fixée, écrite comme une décision : "À la date fixée, aucun pilote n'était signé. Nous avons arrêté."
6. Ce qui reste vrai : une découverte de marché, un modèle réutilisé.

Interdits : "malheureusement", "échec", "malgré tout", "riche d'enseignements", "n'a pas abouti". L'arrêt à la date prévue est un critère de décision tenu et se raconte comme tel.

## Confidentialité

- Nommer le client si le fait est public (site, LinkedIn, factures : Lucca, Synaxe, Guinet-Derriaz, GetPro). Sinon, secteur et échelle : "un éditeur de logiciels pour l'industrie pharmaceutique", "un groupe industriel de 10 M€".
- Chiffres confidentiels en relatif ou en ordre de grandeur.
- Visuels : schémas refaits (SVG, niveaux de gris) plutôt que captures ; légende "Schéma refait d'après les maquettes d'origine" quand c'est le cas. Jamais de zone noircie.
- Ce qui reste au niveau entretien (captures réelles, boards Lucca, Dune, BMI System) ne va pas sur la page publique ; le cas public le dit en une phrase : "Les maquettes se montrent en entretien."
- Cas composite ou hypothétique : possible seulement en le déclarant en tête du cas.

## Signaux Senior et Staff

Faire apparaître, en faits, dans chaque cas où c'est vrai :
- L'ambiguïté de départ : la demande reçue n'était pas le problème.
- Le périmètre : nombre d'applications, d'équipes, de sites, de clients concernés.
- L'influence sans autorité : qui il a fait changer d'avis, avec quel argument, sans lien hiérarchique.
- L'arbitrage avec un coût pour l'activité : ce qui a été refusé ou retardé, et pour quoi.
- Ce qu'il a arrêté ou refusé de faire.
- Le lien avec le chiffre d'affaires, la marge, la rétention ou la conformité quand il est établi ; sinon, ne pas le fabriquer.

Aucune qualité auto-attribuée ("j'ai fait preuve de leadership", "avec rigueur") : le fait seul.

## Visuels et légendes

Un visuel entre s'il porte une information que le texte ne donne pas : un modèle, un flux, un avant/après d'écran. Sa légende dit en une phrase ce qu'il montre et la décision qu'il illustre : "Le tableau des six objets : le premier livrable, avant tout écran." Pas de visuel d'ambiance, pas de capture floue pour faire riche.

## Français puis anglais

Deux textes, pas une traduction. Le texte anglais repart de la structure et des faits, pas des phrases françaises. Le PDF anglais reprend les faits de la page web à l'identique.

## Faits

Statuts, crochets et liste des faits interdits : section Faits du tronc. Avant d'écrire un cas, lire la fiche experiences/ correspondante dans ~/dev/job-hunting et la fiche entreprises/ pour les chiffres publics.
