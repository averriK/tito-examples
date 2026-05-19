DOCUMENT IN ENGLISH

The KB contains chapters of a technical report about the determination of performance-based horizontal seismic coefficients (kmax, kh) for tailings storage facilities at a mining project in Colombia. The report was assembled by multiple independent agents and contains approximately 50% content overlap between chapters. Produce a single restructured document that eliminates all overlaps while preserving 100% of the unique technical content.

The following paragraph-level overlap audit identifies what is duplicated and where.

standards.qmd:
- L4: Pseudo-static method history — NOT a standard. DUPLICATES introduction.qmd and pbsd.qmd.
- L6: Limit-equilibrium, Newmark as approach — NOT a standard. DUPLICATES pbsd.qmd.
- L10: USACE EM 1110-2-1902 — clean, regulatory code.
- L12: NCHRP Report 611 — clean, regulatory code.
- L14: Eurocode 8 (EN 1998-5) — clean, regulatory code.
- L16: ICOLD Bulletin 148 — clean, regulatory code.
- L18-20: Colombian Regulatory Framework (ANLA TDR-13) — regulatory but PROJECT-SPECIFIC. DUPLICATES introduction.qmd.
- L22-24: Performance-Based Professional Guidance (Bray, Macedo) — NOT a standard, methodology description. DUPLICATES pbsd.qmd and newmark.qmd.
- L28-32: Dam Safety / Mining (CDA, FEMA, ICOLD for TSFs) — clean, sector-specific guidance.

pbsd.qmd:
- L4-12: Pseudo-static method description — DUPLICATES introduction and standards.
- L14-18: kmax as inverse problem + equation — core definition, unique formalization. DUPLICATED in standards L22 and ensemble L12.
- L25-31: Parameter group 1 (AEP, consequence class) — unique, clean.
- L33-40: Parameter group 2 (ky, Tn) — unique, clean.
- L42-48: IMs to displacement connection — unique, clean.

model.qmd:
- L6: Newmark rigid/flexible block conceptualization — DUPLICATES newmark.qmd.
- L8-12: Lognormal form equation and explanation — UNIQUE CONTENT, appears ONLY here.
- L14: 4 rigid-block models listed — REDUNDANT, newmark.qmd has same models with full equations.
- L16: 3 flexible-block models listed — REDUNDANT, same as above.
- L18: Logic tree assembly — REDUNDANT, ensemble.qmd covers this.
Conclusion: model.qmd is a summary of newmark.qmd + ensemble.qmd. Its ONLY unique content is L8-12.

newmark.qmd:
- L3: Notation table — unique, clean.
- L5-7: Rigid-block intro + stale cross-reference to model.qmd — intro DUPLICATES model.qmd.
- L9-26: 4 rigid-block models with full equations — UNIQUE equations.
- L28-30: Flexible-block intro + stale cross-reference — DUPLICATES model.qmd.
- L32-60: 3 flexible-block models with full equations — UNIQUE equations.

ensemble.qmd:
- L4: Re-lists 7 models + logic-tree — DUPLICATES model.qmd and newmark.qmd.
- L6: Weighting strategy — UNIQUE.
- L8: IM sampling from PSHA — UNIQUE.
- L10: MC realization mechanics — UNIQUE.
- L12: kmax tabulation — first sentence DUPLICATES pbsd.qmd kmax definition; tabulation detail is unique.

periods.qmd — zero overlaps.
summary.qmd — zero overlaps.

Overlap summary:
| Concept | Appears in (current) | Should appear in (target) |
|---|---|---|
| Pseudo-static method description | introduction, standards, pbsd | introduction ONLY |
| ANLA TDR-13 requirements | introduction, standards | introduction ONLY |
| kmax inverse-problem definition + equation | pbsd, standards, ensemble | pbsd ONLY |
| Bray/Macedo methodology description | standards | DELETE from standards (not a standard) |
| Rigid/flexible block classification | model, newmark, ensemble | newmark ONLY (absorb model.qmd unique content) |
| Lognormal form equation | model | newmark ONLY |
| Logic-tree / ensemble description | model, ensemble | ensemble ONLY |
| 7-model listing with citations | model, ensemble, newmark | newmark ONLY (has equations) |
