#!/usr/bin/env python3
"""Linter d'écriture pour les textes de Gildas (français).

Usage :
    python3 lint.py fichier.md
    cat texte.md | python3 lint.py

Compte les tics et signale les lignes. Ne corrige rien : chaque signalement
se traite à la main avec references/tics-ia.md. Les seuils sont exprimés
pour 1 000 mots. Les titres, tableaux, blocs de code et lignes de
frontmatter sont exclus des statistiques de phrases mais pas des
recherches de motifs.
"""
import re
import sys
import unicodedata

# ---------------------------------------------------------------- listes

ADVERBES = [
    "véritablement", "réellement", "fondamentalement", "profondément",
    "particulièrement", "certainement", "absolument", "clairement",
    "évidemment", "naturellement", "simplement", "littéralement",
    "considérablement", "significativement", "extrêmement", "incroyablement",
    "essentiellement", "globalement", "vraiment", "totalement", "parfaitement",
    "précisément", "largement", "pleinement",
]

CONNECTEURS = [
    "en effet", "par ailleurs", "ainsi", "de plus", "en outre", "dès lors",
    "c'est pourquoi", "dans ce contexte", "dans le cadre de", "il convient de",
    "force est de constater", "d'une part", "d'autre part", "premièrement",
    "deuxièmement", "en somme", "pour résumer", "au final", "en conclusion",
    "in fine", "de fait", "en résumé", "pour conclure", "toutefois",
    "cependant", "néanmoins",
]
CONNECTEURS_OK = re.compile(r"\b(?:dès lors|ainsi) que\b", re.IGNORECASE)

META = [
    "ce qui est intéressant", "il est important de", "notons que",
    "on voit que", "cela montre", "cela illustre", "ce projet montre",
    "ce projet illustre", "ce cas montre", "cette mission montre",
    "dans cet article", "cette page explique", "ce que j'ai appris",
    "la leçon", "ce qui compte", "autrement dit", "en d'autres termes",
    "il est à noter", "à noter que", "rappelons que", "soulignons que",
    "il faut noter", "on comprend que", "on constate que",
]

ANTITHESES = [
    r"\bce n'(?:est|était) pas [^.;]{0,80}?, (?:c'est|c'était|mais)\b",
    r"\bnon pas [^.;]{0,60}? mais\b",
    r"\bil ne s'agit (?:pas|plus) (?:de|d')\b",
    r"\bpas seulement [^.;]{0,60}?(?:mais|aussi)\b",
    r"\bau-delà d[eu']\b",
    r"\bplus qu'une? \w+\b",
    r"\bne se limite pas\b",
    r"\bn'est pas (?:qu'|seulement|simplement|juste)\b",
    r"\bmoins une? \w+ qu'une? \w+\b",
]

EMPHASE = [
    "crucial", "cruciale", "cruciaux", "cruciales", "clé", "clés", "majeur",
    "majeure", "majeurs", "majeures", "massif", "massive", "essentiel",
    "essentielle", "essentiels", "incontournable", "véritable", "véritables",
    "profond", "profonde", "puissant", "puissante", "indispensable",
    "déterminant", "déterminante", "stratégique", "stratégiques",
    "fondamental", "fondamentale", "remarquable", "exceptionnel",
    "exceptionnelle",
]

BROCHURE = [
    "accompagner", "accompagnement", "démarche", "approche", "enjeu",
    "enjeux", "levier", "leviers", "écosystème", "valeur ajoutée", "impact",
    "vision", "transformation", "dynamique", "synergie", "synergies",
    "agile", "agilité", "innovant", "innovante", "expertise", "excellence",
    "passion", "passionné", "passionnée", "au service de", "optimiser",
    "optimisation", "solutions",
]

METAPHORES = [
    "boussole", "fil rouge", "pierre angulaire", "voyage", "aventure",
    "bataille", "combat", "tempête", "jungle", "tremplin", "carrefour",
]

TEMPS_CREUX = [
    "désormais", "à l'heure où", "à l'ère de", "dans un monde où",
    "plus que jamais", "de nos jours", "aujourd'hui",
]

QUALITES = [
    "avec rigueur", "j'ai fait preuve", "mon sens de", "ma capacité à",
    "orienté résultats", "force de proposition", "curieux", "rigoureux",
    "leadership",
]

ANGLICISMES = [
    "adresser", "adressé", "adresse le", "faire sens", "fait sens",
    "font sens", "faire du sens", "supporter", "délivrer", "délivré",
    "impacter", "impacté", "impactée", "performer", "challenger", "driver",
    "initier", "initié", "assumer que", "réaliser que", "réalisé que",
    "focus", "focuser", "implémenter", "onboarder", "scaler", "shipper",
    "dealer", "upgrader", "benchmarker", "opportunité", "opportunités",
    "insight", "insights", "feedback", "feedbacks", "learning", "learnings",
    "stakeholder", "stakeholders", "use case", "use cases", "feature",
    "features", "deliverable", "process", "pain point", "ownership",
    "best practice", "dashboard", "template", "deadline", "challenge",
    "momentum", "trade-off", "scope", "en charge de", "basé sur", "basée sur",
    "basés sur", "basées sur", "au final", "au niveau de", "définitivement",
    "éventuellement", "actuellement", "en termes de", "ceci dit",
    "ceci étant", "dans le futur", "à date", "je suis excité",
    "je suis confiant", "pour être honnête", "honnêtement", "en tant que pm",
    "et/ou", "rendre disponible", "faire la différence", "digital",
    "digitale", "kpi", "call", "meeting", "workflow", "pain points",
    "scalable", "impactant", "impactante", "disruptif", "disruptive",
    "game changer", "mindset", "skills", "hard skills", "soft skills",
    "quick win", "quick wins", "top", "au top", "next step", "next steps",
    "one shot", "asap", "fyi", "roadmapper",
]

APPRECIATION = [
    "difficile", "complexe", "tendu", "tendue", "ambitieux", "ambitieuse",
    "fluide", "robuste", "élégant", "élégante", "riche", "solide",
    "efficace", "performant", "performante", "intuitif", "intuitive",
    "innovant", "innovante", "moderne", "simple mais", "sobre et",
    "important", "importante", "pertinent", "pertinente",
]

ABSTRAITS_FIN = re.compile(
    r"^(?:(?:la |le |l'|les |une? |c'est (?:la |le |l')?|c'était (?:la |le |l')?)"
    r"(?:vraie? |véritable |seule? |grande? |bonne? |bon )?"
    r"(?:valeur|vérité|confiance|leçon|différence|force|clé|sens|essentiel|"
    r"beauté|promesse|preuve|mot de la fin|vrai travail|vraie question|"
    r"bonne question|vraie réponse)\b"
    r"|c'est là |c'est ça |voilà |tout est là|tout le reste|rien de moins|"
    r"rien de plus|pas moins|et c'est tout)",
    re.IGNORECASE,
)

CLIVEE = re.compile(r"\b(?:ce (?:qui|que|dont)|le problème|la question|la réponse) [^.;:]{0,60}?, c'(?:est|était)\b",
                    re.IGNORECASE)
TRIADE = re.compile(r"\b[\w'’-]+(?: [\w'’-]+)?, [\w'’-]+(?: [\w'’-]+)? et [\w'’-]+(?: [\w'’-]+)?\b")
TIRET = re.compile(r"[—–]|(?<=\S) - (?=\S)")
GRAS = re.compile(r"\*\*[^*]+\*\*|__[^_]+__")
ON = re.compile(r"(?<![\w'’])on\b(?![\w'’-])", re.IGNORECASE)
LON = re.compile(r"\bl[’']on\b", re.IGNORECASE)
JE = re.compile(r"(?<![\w'’])(?:je|j[’'])(?=[\w\s])", re.IGNORECASE)
NOUS = re.compile(r"(?<![\w'’])nous\b", re.IGNORECASE)
NOMINALISATIONS = re.compile(
    r"\b(?:la |une |en )?(?:mise en place|mise en œuvre|mise en oeuvre|réalisation|"
    r"définition|élaboration|optimisation|prise en compte|mise en production|"
    r"mise à disposition|mise en cohérence) (?:de|d'|du|des)\b",
    re.IGNORECASE,
)
PASSIF = re.compile(r"\b(?:il a été|il est|ont été|a été|est|sont|avait été|avaient été) "
                    r"(?:décidé|observé|constaté|mis en place|réalisé|réalisée|choisi|"
                    r"retenu|retenue|livré|livrée|conçu|conçue|défini|définie|validé|validée)\b",
                    re.IGNORECASE)
GUILLEMETS_DROITS = re.compile(r'"')
PONCT_SANS_ESPACE = re.compile(r"\w[;!?]|\w:(?!\d|//)")
PONCT_ESPACE_NORMALE = re.compile(r"\S [;:!?](?!\S*//)")
VIRGULE_ET = re.compile(r"(?:\b[\w'-]+, ){2,}et\b")
TITLE_CASE = re.compile(r"^#{1,6}\s+(?:[A-ZÀ-Ý][\w'’-]*\s+){2,}[A-ZÀ-Ý]")
QUESTION = re.compile(r"\?\s*$")

SEUILS = {  # pour 1 000 mots
    "tirets": 0, "gras": 0, "adverbes": 0, "antithèses": 1, "triades": 2,
    "phrases < 6 mots": 2, "phrases > 35 mots": 5, "connecteurs": 3,
    "emphase": 1, "appréciation": 3, "brochure": 2, "on (hors l'on)": 0, "clivées": 1,
    "questions": 0, "méta": 0, "métaphores": 1, "temps creux": 1,
    "qualités": 0, "anglicismes": 1, "nominalisations": 2, "passifs": 2,
    "fins abstraites": 0,
}

# ---------------------------------------------------------------- outils


def lire():
    if len(sys.argv) > 1 and sys.argv[1] != "-":
        with open(sys.argv[1], encoding="utf-8") as f:
            return f.read()
    return sys.stdin.read()


def normaliser(s):
    return unicodedata.normalize("NFC", s).replace("’", "'")


def mots(s):
    return re.findall(r"[\wÀ-ÿ'-]+", s)


def couper_phrases(texte):
    texte = re.sub(r"\b(M|Mme|Mlle|Dr|St|etc|cf|p|ex|vs)\.", r"\1<pt>", texte)
    parts = re.split(r"(?<=[.!?…])\s+(?=[A-ZÀ-Ý«\"(\[])", texte)
    return [p.replace("<pt>", ".").strip() for p in parts if p.strip()]


def prose_lines(lines):
    """Lignes de prose : sans titres, tableaux, code, frontmatter, puces."""
    out, in_code, in_front = [], False, False
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if i == 1 and s == "---":
            in_front = True
            continue
        if in_front:
            if s == "---":
                in_front = False
            continue
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not s or s.startswith("#") or s.startswith("|") or s.startswith("<"):
            continue
        out.append((i, l))
    return out


def paragraphes(prose):
    paras, cur, start = [], [], None
    prev = None
    for i, l in prose:
        if prev is not None and i != prev + 1 and cur:
            paras.append((start, " ".join(cur)))
            cur = []
        if not cur:
            start = i
        cur.append(l.strip())
        prev = i
    if cur:
        paras.append((start, " ".join(cur)))
    return paras


def autour(l, a, b, n=55):
    """Extrait de la ligne centré sur le motif [a:b]."""
    deb, fin = max(0, a - n), min(len(l), b + n)
    return ("…" if deb else "") + l[deb:fin].strip() + ("…" if fin < len(l) else "")


def chercher_mots(liste, prose):
    hits = []
    for i, l in prose:
        low = l.lower()
        for m in liste:
            for mm in re.finditer(r"(?<![\w-])" + re.escape(m) + r"(?![\w'-])", low):
                hits.append((i, m, autour(l, mm.start(), mm.end())))
    return hits


def chercher_regex(rx, prose, flags=0):
    hits = []
    for i, l in prose:
        for mm in re.finditer(rx, l, flags):
            hits.append((i, mm.group(0), autour(l, mm.start(), mm.end())))
    return hits


def extrait(s, n=130):
    s = s.strip()
    return s if len(s) <= n else s[: n - 1] + "…"


# ---------------------------------------------------------------- analyse


def analyser(texte):
    texte = normaliser(texte)
    lines = texte.split("\n")
    toutes = [(i, l) for i, l in enumerate(lines, 1)]
    prose = prose_lines(lines)
    paras = paragraphes(prose)
    corps = " ".join(l for _, l in prose)
    n_mots = max(1, len(mots(corps)))
    phrases = couper_phrases(corps)
    longueurs = [len(mots(p)) for p in phrases]
    moy = sum(longueurs) / max(1, len(longueurs))

    R = {}
    R["tirets"] = chercher_regex(TIRET, toutes)
    R["gras"] = chercher_regex(GRAS, toutes)
    R["adverbes"] = chercher_mots(ADVERBES, prose)
    R["connecteurs"] = [h for h in chercher_mots(CONNECTEURS, prose)
                        if not CONNECTEURS_OK.search(h[2])]
    R["méta"] = chercher_mots(META, prose)
    R["antithèses"] = [h for rx in ANTITHESES for h in chercher_regex(rx, prose, re.IGNORECASE)]
    R["triades"] = chercher_regex(TRIADE, prose)
    R["emphase"] = chercher_mots(EMPHASE, prose)
    R["appréciation"] = chercher_mots(APPRECIATION, prose)
    R["brochure"] = chercher_mots(BROCHURE, prose)
    R["métaphores"] = chercher_mots(METAPHORES, prose)
    R["temps creux"] = chercher_mots(TEMPS_CREUX, prose)
    R["qualités"] = chercher_mots(QUALITES, prose)
    R["anglicismes"] = chercher_mots(ANGLICISMES, prose)
    R["clivées"] = chercher_regex(CLIVEE, prose)
    R["nominalisations"] = chercher_regex(NOMINALISATIONS, prose)
    R["passifs"] = chercher_regex(PASSIF, prose)
    on_hits = []
    for i, l in prose:
        for mm in ON.finditer(l):
            avant = l[max(0, mm.start() - 2):mm.start()].lower()
            if avant.endswith("l'") or avant.endswith("l\u2019"):
                continue
            on_hits.append((i, "on", autour(l, mm.start(), mm.end())))
    R["on (hors l'on)"] = on_hits

    courtes, longues = [], []
    for start, p in paras:
        for ph in couper_phrases(p):
            n = len(mots(ph))
            if n and n < 6:
                courtes.append((start, f"{n} mots", ph))
            elif n > 35:
                longues.append((start, f"{n} mots", ph))
    R["phrases < 6 mots"] = courtes
    R["phrases > 35 mots"] = longues

    R["questions"] = []
    R["fins abstraites"] = []
    for start, p in paras:
        phs = couper_phrases(p)
        for ph in phs:
            if QUESTION.search(ph):
                R["questions"].append((start, "?", ph))
        if phs and ABSTRAITS_FIN.match(phs[-1].strip()):
            R["fins abstraites"].append((start, "fin de paragraphe", phs[-1]))

    typo = []
    typo += [(i, "guillemets droits", l) for i, m, l in chercher_regex(GUILLEMETS_DROITS, prose)]
    typo += [(i, "pas d'espace avant ;:!?", l) for i, m, l in chercher_regex(PONCT_SANS_ESPACE, prose)]
    typo += [(i, "espace normale avant ;:!? (insécable attendue)", l)
             for i, m, l in chercher_regex(PONCT_ESPACE_NORMALE, prose)]
    typo += [(i, "virgule avant et", l) for i, m, l in chercher_regex(VIRGULE_ET, prose)]
    typo += [(i, "Title Case dans un titre", l) for i, m, l in chercher_regex(TITLE_CASE, toutes)]

    je = len(chercher_regex(JE, prose))
    nous = len(chercher_regex(NOUS, prose))
    return R, typo, n_mots, len(phrases), moy, longueurs, je, nous, paras


def rapport(texte):
    R, typo, n_mots, n_phr, moy, longueurs, je, nous, paras = analyser(texte)
    par_mille = lambda n: n * 1000 / n_mots
    out = []
    out.append(f"=== lint : {n_mots} mots, {n_phr} phrases, {moy:.1f} mots par phrase en moyenne ===")
    if longueurs:
        n_on = len(R["on (hors l'on)"])
        out.append(f"    plus courte {min(longueurs)} mots, plus longue {max(longueurs)} mots ; "
                   f"je/j' : {je}, nous : {nous}, on : {n_on}")
    lp = [len(mots(p)) for _, p in paras]
    if len(lp) >= 3:
        ecart = max(lp) - min(lp)
        out.append(f"    paragraphes : {len(lp)}, de {min(lp)} à {max(lp)} mots"
                   + (" ; longueurs très proches, vérifier la symétrie (tics-ia.md item 15)" if ecart < 25 else ""))
    out.append("")
    out.append("RÉSUMÉ                     nb    /1000   seuil")
    a_corriger = []
    for cle, seuil in SEUILS.items():
        n = len(R.get(cle, []))
        pm = par_mille(n)
        etat = "" if pm <= seuil else "   À CORRIGER"
        if etat:
            a_corriger.append(cle)
        out.append(f"  {cle:<24} {n:>3}  {pm:>6.1f}   {seuil:>3}{etat}")
    out.append(f"  {'typographie':<24} {len(typo):>3}")
    out.append("")
    out.append("DÉTAIL (ligne : motif : extrait)")
    for cle in SEUILS:
        hits = R.get(cle, [])
        if not hits:
            continue
        out.append(f"[{cle}]")
        for i, m, l in hits[:40]:
            out.append(f"  l.{i} : {m} : {extrait(l)}")
        if len(hits) > 40:
            out.append(f"  ... {len(hits) - 40} de plus")
    if typo:
        out.append("[typographie]")
        types = {}
        for i, m, l in typo:
            types.setdefault(m, []).append((i, l))
        for m, lst in types.items():
            out.append(f"  {m} : {len(lst)} occurrence(s)")
            for i, l in lst[:3]:
                out.append(f"    l.{i} : {extrait(l)}")
    out.append("")
    if a_corriger:
        out.append("À traiter en priorité : " + ", ".join(a_corriger) + ".")
    else:
        out.append("Aucun seuil dépassé. Relire à l'œil la symétrie des paragraphes, les fins de section et les métaphores.")
    return "\n".join(out)


if __name__ == "__main__":
    print(rapport(lire()))
