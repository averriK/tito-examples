# Agent Prompt: Restructure Technical Document

## Context

You are restructuring a technical report about the determination of performance-based horizontal seismic coefficients (kmax, kh) for tailings storage facilities at a mining project in Colombia. The report was assembled by multiple independent agents and contains approximately 50% content overlap between chapters. Your task is to eliminate all overlaps while preserving 100% of the unique technical content.

## Critical Rules

1. **ZERO new content.** Every sentence you write must originate from the source files. You may delete, move, and minimally rephrase for transitions, but you CANNOT invent technical statements, equations, references, or definitions.
2. **ZERO value judgments.** No "robust", "significant", "improved", "cornerstone", "foundational", etc. This is a professional engineering report.
3. **ZERO roadmaps.** No "the following section presents", "as described above", "this report provides". Declarative, impersonal, present tense for established facts.
4. **ASCII only.** Straight quotes, standard hyphens (-), no em-dashes, no smart quotes.
5. **Citations:** Use [@key] or [-@key]. Multiple citations in one bracket: [@A; @B]. Never [@A][@B].
6. **Each concept appears ONCE.** If it appears in two files, decide which file owns it and delete from the other.

## Source Files

Read all files in `_chapters/` and `_chapters_old/` directories. The `_chapters/` versions are the working copies. The `_chapters_old/` versions are the original knowledge base from which all content was derived. If in doubt about wording, prefer `_chapters_old/`.

## Diagnostic: Paragraph-Level Overlap Audit

The following audit was conducted on all `_chapters/*.qmd` files. Each paragraph was classified by its relevance to the section it appears in and whether it duplicates content in another file.

### standards.qmd

| Lines | Content | Relevant to section? | Overlap |
|---|---|---|---|
| L4 | Pseudo-static method history, transition to performance-based | NO — general methodology context, not a standard/code | DUPLICATES introduction.qmd Background ¶1-2 AND pbsd.qmd ¶1 |
| L6 | Limit-equilibrium, Newmark as approach | NO — methodology description | DUPLICATES pbsd.qmd ¶1 |
| L10 | USACE EM 1110-2-1902, ER 1110-2-1806 | YES — regulatory code | Clean |
| L12 | NCHRP Report 611 | YES — regulatory code | Clean |
| L14 | Eurocode 8 (EN 1998-5) | YES — regulatory code | Clean |
| L16 | ICOLD Bulletin 148 | YES — regulatory code | Clean |
| L18-20 | Colombian Regulatory Framework (ANLA TDR-13, Concepto Tecnico 02268, NSR-10) | YES — regulatory, but PROJECT-SPECIFIC | DUPLICATES introduction.qmd Background ¶3 (same ANLA info in both places) |
| L22-24 | "Performance-Based Professional Guidance" — Bray & Travasarou (2009) kmax inversion, Macedo et al. (2018) PBEE extension | NO — this is methodology description, not a standard/code/guideline | DUPLICATES pbsd.qmd (kmax inverse problem) AND model.qmd/newmark.qmd (same Bray/Macedo citations with equations) |
| L28-32 | Dam Safety / Mining — CDA, FEMA, ICOLD for TSFs | YES — sector-specific regulatory guidance | Clean |

### pbsd.qmd

| Lines | Content | Relevant? | Overlap |
|---|---|---|---|
| L4-12 | Pseudo-static method description, kh definition | NO — preamble that repeats what introduction and standards already say | DUPLICATES standards L4+L6 AND introduction Background |
| L14-18 | kmax as inverse problem + equation $k_{\max} = \inf\{...\}$ | YES — this is the core definition, unique formalization | DUPLICATED in standards L22 ("inverting the criterion") and ensemble L12 (re-derives kmax) |
| L25-31 | Parameter group 1: AEP, consequence class | YES — unique here | Clean |
| L33-40 | Parameter group 2: ky, Tn | YES — unique here | Clean |
| L42-48 | IMs to displacement connection | YES — unique here | Clean |

### model.qmd

| Lines | Content | Relevant? | Overlap |
|---|---|---|---|
| L6 | Newmark rigid/flexible block conceptualization | YES — introduces the concepts | DUPLICATES newmark.qmd L5-7 (rigid intro) and L28-30 (flexible intro) |
| L8-12 | Lognormal form $\ln D = \mu + \epsilon\sigma$, explanation of IM, Tn, Mw, spectral period convention | YES — **UNIQUE CONTENT** — the equation and its full explanation appear ONLY here | Clean |
| L14 | 4 rigid-block models listed with citations and brief descriptions | REDUNDANT — newmark.qmd has the same models with full equations | DUPLICATES newmark.qmd L9-26 (same models, same citations, but newmark has equations) |
| L16 | 3 flexible-block models listed with citations and brief descriptions | REDUNDANT — same as above | DUPLICATES newmark.qmd L32-60 |
| L18 | Logic tree assembly, epistemic uncertainty, Monte Carlo integration | REDUNDANT — ensemble.qmd covers this | DUPLICATES ensemble.qmd L4-6 (logic tree) and L10 (MC) |

**Conclusion:** model.qmd is a summary of newmark.qmd + ensemble.qmd. Its ONLY unique content is L8-12 (lognormal form). The rest is duplicated.

### newmark.qmd

| Lines | Content | Relevant? | Overlap |
|---|---|---|---|
| L3 | Notation table (D, ky, PGA, PGV, AI, Tn, Sa, Mw, r, sigma) | YES — unique | Clean |
| L5-7 | Rigid-block idealization intro + "as described in the Probabilistic Model section" | YES for the intro; cross-reference is STALE if model.qmd is deleted | Intro text DUPLICATES model.qmd L14 (rigid description) |
| L9-26 | 4 rigid-block models with full equations | YES — **UNIQUE** equations | Citations duplicate model.qmd L14, but equations are unique |
| L28-30 | Flexible-block intro + "as described in the Probabilistic Model section" | Same as L5-7 | Intro text DUPLICATES model.qmd L16 |
| L32-60 | 3 flexible-block models with full equations | YES — **UNIQUE** equations | Citations duplicate model.qmd L16, but equations are unique |

### ensemble.qmd

| Lines | Content | Relevant? | Overlap |
|---|---|---|---|
| L4 | "weighted ensemble of seven...three flexible-block and four rigid-block...logic-tree weighting" | NO — re-lists what model.qmd and newmark.qmd already describe | DUPLICATES model.qmd L14+L16+L18 |
| L6 | Weighting strategy: more weight to recent models, larger databases | YES — **UNIQUE** | Clean |
| L8 | IM sampling from PSHA fractiles, site amplification, inter-period correlation | YES — **UNIQUE** | Clean |
| L10 | MC realization mechanics: sigma_lnD, epsilon, weighted sum, quantiles, displacement floor, sigma_lnF, uncertainty budget | YES — **UNIQUE** | Clean |
| L12 | kmax derivation: "minimum ky at which p-hat(ky) <= p...tabulated across return periods" | PARTIALLY redundant — the kmax DEFINITION (first sentence) duplicates pbsd.qmd L14-16; the TABULATION detail (second sentence onward) is unique | First sentence DUPLICATES pbsd.qmd kmax equation |

### periods.qmd — CLEAN, zero overlaps

### summary.qmd — CLEAN, zero overlaps

### Overlap Summary Map

| Concept | Appears in (current) | Should appear in (target) |
|---|---|---|
| Pseudo-static method description | introduction ¶1-2, standards L4+L6, pbsd L4-12 | introduction ONLY |
| ANLA TDR-13 requirements | introduction ¶3, standards L18-20 | introduction ONLY |
| kmax inverse-problem definition + equation | pbsd L14-16, standards L22-24, ensemble L12 | pbsd ONLY |
| Bray/Macedo methodology description | standards L22-26 | DELETE from standards (methodology, not a standard); one-line citation in pbsd; equations in newmark |
| Rigid/flexible block classification | model L6+L14+L16, newmark L5-7+L28-30, ensemble L4 | newmark ONLY (with lognormal preamble from model L8-12) |
| Lognormal form equation | model L8-12 | newmark ONLY (merged as preamble) |
| Logic-tree / ensemble description | model L18, ensemble L4-6 | ensemble ONLY |
| 7-model listing with citations | model L14+L16, ensemble L4, newmark L9-60 | newmark ONLY (has equations; others are summaries) |

## Slot 1: introduction.qmd

**Purpose:** Project context, regulatory context, and ONE objective.

**Build from:**
- _chapters/introduction.qmd (current Background paragraphs about MCQ, TSFs, Task 500)
- _chapters/standards.qmd L18-20 (ANLA TDR-13 content — MOVE here, delete from standards)
- _chapters/introduction.qmd (current methodology paragraph about kmax)

**Structure:**
```
## Introduction
### Background
¶1: Project — MCQ, Quebradona, NAG/PAG TSFs, filtered tailings (from ref/background.docx context already in current intro)
¶2: Task 500 — determination of kh through performance-based approach, alternative to ANLA TDR-13
¶3: ANLA regulatory context — TDR-13 requirements, Concepto Tecnico 02268, TdR quote allowing alternative methodologies (MOVE from standards.qmd L18-20)
¶4: kmax definition — one sentence defining what kmax is (from current intro)

### Objectives
ONE paragraph: The objective is the determination of kmax [PSA units] and kh [%PGA] for the Quebradona TSFs, across N geometry classes, N material scenarios, N return periods, and N displacement thresholds. The determination requires: (a) site-specific PSHA, (b) site-response amplification, (c) fundamental period estimation, and (d) Newmark displacement modeling through a weighted ensemble. Items (a)-(d) are listed as STEPS, not as separate objectives.
```

**Delete:** ### Scope section entirely.

## Slot 2: standards.qmd

**Purpose:** International codes and standards that govern seismic slope design. Factual summary of what each code requires.

**Build from:** _chapters/standards.qmd, keeping ONLY the regulatory/code paragraphs.

**Structure:**
```
## Standards, Guidelines, and Recommendations
### Regulatory and Code-Based Frameworks
- USACE EM 1110-2-1902 paragraph (current L10) — keep verbatim
- NCHRP 611 paragraph (current L12) — keep verbatim
- Eurocode 8 paragraph (current L14) — keep verbatim
- ICOLD Bulletin 148 paragraph (current L16) — keep verbatim

### Dam Safety and Mining Sector Practice
- CDA/FEMA/ICOLD for TSFs paragraph (current L28-32) — keep verbatim
```

**Delete from standards.qmd:**
- L4 (opening paragraph about pseudo-static history) — duplicates introduction and pbsd
- L6 (Newmark as approach) — duplicates pbsd
- L18-20 (### Colombian Regulatory Framework) — moved to introduction
- L22-26 (### Performance-Based Professional Guidance) — methodology content, not a standard; citations already in newmark.qmd

## Slot 3: pbsd.qmd

**Purpose:** Define the performance-based framework for kmax. The WHAT and WHY of the inverse-displacement approach.

**Build from:** _chapters/pbsd.qmd

**Structure:**
```
## Performance-Based Seismic Coefficient Selection
¶1: kmax as inverse problem + equation (current L14-18) — START here, no preamble about pseudo-static
¶2: Parameter group 1 — AEP, consequence class (current L25-31)
¶3: Parameter group 2 — ky, Tn (current L33-40)
¶4: IM connection — how IMs translate to displacement (current L42-48)
```

Add ONE citation sentence at the end of ¶1: "following the framework of Bray and Travasarou [-@BrayTravasarou2009] and its probabilistic extension by Macedo et al. [-@MacedoEtAl2018]." — this is the ONLY place these methodological citations appear outside of newmark.qmd.

**Delete:** ¶1 (L4-12) — the pseudo-static preamble. It duplicates introduction and standards.

## Slot 4: newmark.qmd (absorbs model.qmd)

**Purpose:** Complete specification of the 7 Newmark displacement models used. Equations, parameters, applicability.

**Build from:** _chapters/newmark.qmd + _chapters/model.qmd L6-12

**Structure:**
```
## Newmark Displacement Models

### Probabilistic Functional Form
- Newmark concept: rigid vs flexible block (from model.qmd L6, first 2 sentences ONLY — the conceptual intro, NOT the model listing)
- Lognormal equation and explanation (from model.qmd L8-12 verbatim — the equation, IM definition, spectral period convention)

### Rigid-Block Models
- Brief applicability statement (from current newmark.qmd L5-7, but DELETE "as described in the Probabilistic Model section" since that section no longer exists)
- Ambraseys & Menu — keep verbatim
- Yegian et al. — keep verbatim
- Jibson — keep verbatim
- Saygili & Rathje — keep verbatim

### Flexible-Block Models
- Brief applicability statement (from current newmark.qmd L28-30, DELETE cross-reference)
- Bray, Macedo, Travasarou 2017 — keep verbatim
- Bray & Macedo 2019 — keep verbatim
- Bray & Travasarou 2007 — keep verbatim

### Notation
- Move notation table (current L3) to the end or keep at top — your choice
```

**Delete model.qmd entirely.** Its unique content (lognormal form) is now in newmark.qmd. Everything else was a duplicate.

## Slot 5: ensemble.qmd

**Purpose:** How the 7 models are combined and how kmax is computed. The HOW — implementation details.

**Build from:** _chapters/ensemble.qmd

**Structure:**
```
## Weighted Ensemble Model
¶1: Weighting strategy (current L6) — START here. No re-listing of the 7 models.
¶2: IM sampling from PSHA (current L8) — keep verbatim
¶3: MC realization, sigma_lnD, epsilon, weighted sum, quantiles, displacement floor, sigma_lnF (current L10) — keep verbatim
¶4: kmax tabulation (current L12) — keep ONLY the implementation detail: "This calculation is performed for each combination of material scenario, slope geometry, and service level, producing kmax values tabulated across the range of return periods from AEP 1/100 to AEP 1/10,000." DELETE the re-definition of kmax (the infimum/probability statement — that is in pbsd.qmd).
```

**Delete:**
- L4 (opening paragraph listing 7 models + logic tree) — duplicates newmark.qmd and model.qmd content now in newmark
- First sentence of L12 that re-defines kmax

## Slot 6: periods.qmd — NO CHANGES

Keep verbatim. This file has zero overlaps.

## Slot 7: summary.qmd — NO CHANGES

Keep as-is. Content is parametric R code and results text.

## Output

Write each file to `_chapters/`. Preserve the exact filenames. Delete `_chapters/model.qmd` (its content is merged into newmark.qmd).

## Verification Checklist

After writing all files, verify:
1. Grep "pseudo-static slope stability" or "pseudo-static analysis" — appears in introduction ONLY (not in standards opening, not in pbsd opening)
2. Grep "ANLA" — appears in introduction ONLY (not in standards)
3. Grep "inverse problem" or "\\inf\\{" kmax equation — appears in pbsd ONLY (not in ensemble, not in standards)
4. Grep "logic.tree" — appears in ensemble ONLY (not in model.qmd which is deleted)
5. Grep "\\ln D.*=.*\\mu" (lognormal equation) — appears in newmark.qmd ONLY
6. Grep each model name "Ambraseys|Yegian|Jibson|Saygili|Bray" with equation context — appears in newmark.qmd ONLY
7. Grep "Performance-Based Professional Guidance" — appears NOWHERE
8. File model.qmd does NOT exist
9. Zero value judgments (grep for "robust|significant|improved|cornerstone|foundational|widely employed|widely adopted")
10. Zero roadmaps (grep for "following section|preceding section|as described|is presented|are detailed")
