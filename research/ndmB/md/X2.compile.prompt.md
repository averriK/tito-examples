# Structured Prompt: Performance-Based Seismic Coefficient Methodology

This prompt defines the scope and structure for a technical document that logically organizes the methodology for probabilistic estimation of performance-based seismic coefficients, including Newmark displacement methods, modern extensions, and assembly models for rigid and flexible blocks. The knowledge base includes a detailed Newmark displacement methodology (KB/newmark.md) and a methodology for estimating the fundamental period of a slope, both of which serve as primary input sources.


## SLOTS

### SLOT 1: Introduction - General Probabilistic Method for Performance-Based Seismic Coefficients

Produce an introductory section that proposes a general method for the probabilistic estimation of performance-based seismic coefficients. The introduction establishes the overall framework and motivates the document structure. It provides the conceptual foundation linking seismic hazard characterization, Newmark displacement estimation, and the derivation of seismic coefficients tied to acceptable displacement thresholds.


### SLOT 2: Foundations and History of Seismic Coefficient Analysis

Present the theoretical foundations and historical development of seismic coefficient analysis, beginning with the Makdisi-Seed method. The narrative traces the evolution of approaches from early deterministic models through subsequent refinements, establishing the context from which modern probabilistic methods emerged.


### SLOT 3: Probabilistic Functional Structure of Newmark Displacement Estimation Methods

Prepare a chapter-level section presenting the probabilistic functional structure of each method for estimating Newmark displacement ($D_n$). This slot addresses the overarching probabilistic framework - how each method formulates the relationship between seismic demand parameters and displacement - rather than the detailed mechanics of each method (which are covered in SLOT 4).


### SLOT 4: Detailed Newmark Displacement Estimation Methods

Present in detail the specific methods for estimating Newmark displacement. This section covers the mechanics, equations, input parameters, and assumptions of each established method. The level of detail is sufficient for a practitioner to understand the derivation, applicability, and limitations of each approach.


### SLOT 5: Modern Methods Post-Bray (2019) and Fundamental Period Estimation

This slot has two closely linked parts. First, present more recent Newmark displacement estimation methods developed after Bray (2019), including Saragoni and other contemporary contributors. Second, explain how to estimate the fundamental period of each slope, a key parameter for flexible-block Newmark methods. The fundamental period estimation depends on the base stiffness parameters addressed in SLOT 6, and SLOT 6 logically precedes this material in the exposition.


### SLOT 6: Maximum Base Stiffness Estimation (Shear Modulus and Shear Wave Velocity)

Explain the estimation of maximum base stiffness, specifically the small-strain shear modulus $G_0$ (or equivalently the shear wave velocity $V_{s0}$), using the methods of Ishihara and other relevant authors. This section serves as a prerequisite for the fundamental period estimation discussed in SLOT 5, as the TASK_FILE explicitly states this material must be presented first.


### SLOT 7: Flexible Block Assembly Model and Applicability

Summarize the assembly model that incorporates flexible block methods for Newmark displacement estimation. Explain the structure of the assembled model and specify for which types of slopes or geotechnical conditions the flexible block approach is appropriate, including the criteria that distinguish cases requiring flexible block analysis from those amenable to rigid block treatment.


### SLOT 8: Rigid Block Assembly Methods and Applicability

Summarize the assembly of methods based on the rigid block model for Newmark displacement estimation. Explain for which types of slopes the rigid block approach is applicable, including the geotechnical and geometric conditions under which rigid block assumptions hold. This section complements SLOT 7 by covering the alternative modeling framework.


## CONSTRAINTS

- The output document language is English, as explicitly required by TASK_FILE line 1.


- The document style is professional engineering methodology, appropriate for a technical audience in geotechnical earthquake engineering.


- The knowledge base files (KB/newmark.md and the slope fundamental period methodology in KB) serve as primary reference sources for all slots.


- Mathematical notation follows LaTeX conventions: inline expressions use $...$ format and display equations use $$...$$ format, with no Unicode mathematical symbols in running text.


- All prose maintains an impersonal, objective, academic voice with no instructional language, second-person address, or promotional claims.

