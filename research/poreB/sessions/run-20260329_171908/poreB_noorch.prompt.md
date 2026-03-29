# Structured Prompt: Shear Strain History from Seismic Base Acceleration

## Context

The overarching research objective is to formulate a simple proxy model for predicting pore pressure increase in a saturated fine-grained material subjected to a seismic acceleration record. The physical configuration consists of a homogeneous, fine-grained, saturated stratum of thickness $H_s$ resting on rock. The stratum exhibits depth-variable shear stiffness $G_o(z)$, with its maximum value $G_o = G(z=0)$ at the base. A seismic acceleration history $a_g(t)$ is applied at the base of the stratum. The KB/ directory contains analytical closed-form solutions for the site response, expressed in terms of instantaneous accelerations $a(z,t)$ at arbitrary depths within the stratum.
^[Confidence: HIGH, Rationale: All statements are direct paraphrases of TASK_FILE lines 3-5, covering the stated research purpose, physical setup (stratum thickness, stiffness profile, material type, boundary condition), and the role of KB/ contents. No information was added beyond what TASK_FILE provides.]

## SLOTS

### SLOT 1: Numerical R algorithm for instantaneous shear strain history

The required deliverable is a numerical algorithm implemented in R that, given a base acceleration time history $a_g(t)$, estimates the instantaneous shear strain history $\gamma(z,t)$ at any depth $z$ within the stratum. The computational procedure involves two coupled steps: (a) computing the instantaneous acceleration field $a(z,t)$ at any depth $z$ from the base excitation $a_g(t)$, using the analytical closed-form site response solutions available in KB/; and (b) deriving the instantaneous shear strain history $\gamma(z,t)$ from the computed acceleration field $a(z,t)$. The R implementation must use `data.table()` for data handling and must avoid snake_case naming convention throughout the code.
^[Confidence: HIGH, Rationale: This slot is justified by TASK_FILE lines 8-11 (the "Pregunta" section). The two-step computational structure - acceleration computation from base excitation followed by strain derivation from the acceleration field - is explicitly stated in lines 9-10. The data.table() and snake_case constraints are taken verbatim from line 11. No additional objectives or sub-goals were introduced beyond what the task specifies.]

## CONSTRAINTS

- Output language: English.
- Document style: professional engineering methodology.

^[Confidence: HIGH, Rationale: Both constraints are directly stated in TASK_FILE line 1, which reads "DOCUMENT IN ENGLISH (PROFESSIONAL ENGINEERING METHODOLOGY STYLE)". No constraints were inferred or invented beyond the explicit text.]
