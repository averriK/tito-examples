# Structured Prompt: Performance-Based Horizontal Seismic Coefficients for Tailings Storage Facilities

The KB contains chapters of a technical report on performance-based horizontal seismic coefficients ($k_{\max}$, $k_h$) for tailings storage facilities. The chapters were assembled by independent agents and contain approximately 50% content overlap. The objective is to produce a single restructured document that eliminates all overlaps while preserving 100% of the unique technical content. The output document contains seven sections, specified below as individual slots, in the order listed.


## SLOTS

### SLOT 1: Introduction

Assemble the Introduction section from KB source content. Include project context covering MCQ, Quebradona, and tailings storage facilities (TSFs). Relocate the ANLA regulatory context from standards.qmd (lines 18-20) into this section. Include one paragraph stating the document objective. Delete the Scope section entirely. Place the pseudo-static method description in this section only; it must not appear in any subsequent section of the document. Write in flowing paragraphs.


### SLOT 2: Standards

Assemble the Standards section covering international codes and standards only: USACE, NCHRP, Eurocode 8, ICOLD, and CDA/FEMA. Delete the opening paragraph about pseudo-static history, as it duplicates content assigned to the Introduction (SLOT 1). Delete the Colombian regulatory framework subsection, as that content has been relocated to the Introduction (SLOT 1). Delete the Performance-Based Professional Guidance subsection, which describes methodology rather than a standard. Write in flowing paragraphs.


### SLOT 3: Performance-Based Seismic Coefficient Selection

Assemble the Performance-Based Seismic Coefficient Selection section. Define $k_{\max}$ as an inverse problem, using the equation from pbsd.qmd. Present the parameter groups: annual exceedance probability (AEP), consequence class, yield coefficient ($k_y$), fundamental period ($T_n$), and the intensity measure (IM) connection. Delete the pseudo-static preamble from pbsd.qmd, as that content belongs exclusively in the Introduction (SLOT 1). Include one citation sentence referencing Bray and Travasarou and one referencing Macedo et al. Write in flowing paragraphs.


### SLOT 4: Newmark Displacement Models

Assemble the Newmark Displacement Models section by fully absorbing model.qmd content. Begin with the lognormal functional form equation from model.qmd (lines 8-12). Follow with the rigid-block models (four models with their equations from newmark.qmd), then the flexible-block models (three models with their equations from newmark.qmd). Delete all cross-references to a "Probabilistic Model section" that no longer exists in the restructured document. The entirety of model.qmd is absorbed into this section. Write in flowing paragraphs.


### SLOT 5: Weighted Ensemble Model

Assemble the Weighted Ensemble Model section. Begin with the weighting strategy; do not re-list the seven individual models. Cover IM sampling from PSHA, Monte Carlo realization mechanics, and $k_{\max}$ tabulation. Delete any re-definition of $k_{\max}$, as that definition belongs exclusively in the Performance-Based Seismic Coefficient Selection section (SLOT 3). Write in flowing paragraphs.


### SLOT 6: Fundamental Period Estimation

Reproduce the Fundamental Period Estimation section using periods.qmd content verbatim. No overlaps with other sections exist. Write in flowing paragraphs.


### SLOT 7: Summary and Results

Reproduce the Summary and Results section using summary.qmd content verbatim. No overlaps with other sections exist. Write in flowing paragraphs.


## CONSTRAINTS

- The document language is English.


- Every sentence in the output must originate from the KB source files. No technical statements, equations, references, or definitions may be invented.


- No value judgments are permitted. The words "robust", "significant", "improved", "cornerstone", and similar evaluative terms are prohibited.


- No roadmap language is permitted. Phrases such as "the following section presents" or "as described above" are prohibited.


- Each concept appears exactly once across the entire document. When a concept is assigned to a specific section by the slot instructions, it must be deleted from all other sections.


- All citations use [@key] format drawn from the KB. No citations may be invented.


- All equations are preserved in LaTeX display math format.


- All existing citations from the KB sources are preserved in the output.


- The output is written in flowing paragraphs throughout.

