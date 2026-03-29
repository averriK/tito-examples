# Structured Prompt: Shear Strain History Estimation from Seismic Base Accelerations

## Context

The broader research objective is to formulate a simple proxy model for predicting the pore pressure increment in a saturated fine-grained material subjected to a seismic acceleration record. The physical domain consists of a homogeneous stratum of thickness $H_s$, with depth-varying shear modulus $G_o(z)$ attaining its maximum value $G_o = G(z = 0)$ at the base, composed of fine-grained saturated material overlying rock, and subjected to base accelerations $a_g(t)$. Analytical closed-form site response solutions, expressed in terms of instantaneous accelerations $a(z, t)$ at arbitrary depths within the stratum, are available in KB/.
^[Confidence: HIGH, Rationale: Every statement paraphrases explicit content from TASK_FILE. The purpose declaration (line 3) provides the proxy-model objective and material description. The context section (lines 4-5) specifies stratum geometry ($H_s$), depth-varying stiffness $G_o(z)$, boundary conditions (rock base, $a_g(t)$), and the reference to KB/ analytical formulations. No claims are introduced beyond what TASK_FILE states.]

## SLOTS

### SLOT 1: Numerical R algorithm for instantaneous shear strain history

Implement in R a numerical algorithm that, given a base acceleration time history $a_g(t)$, estimates the instantaneous shear strain history $\gamma(z, t)$ at any depth within the stratum. The algorithm derives $\gamma(z, t)$ from the instantaneous acceleration field $a(z, t)$, which is itself obtained from the base excitation through the analytical site response formulations documented in KB/. The implementation must employ the closed-form solutions available in KB/ for computing the acceleration response at arbitrary depths and then obtain the corresponding shear strain histories from those accelerations.
^[Confidence: HIGH, Rationale: This slot corresponds directly to the single "Pregunta" in TASK_FILE (lines 8-10), which requests a numerical R implementation to estimate instantaneous shear strain histories from a base acceleration record via the analytical site response solutions. The input ($a_g(t)$), output ($\gamma(z, t)$), and the intermediate computational step through $a(z, t)$ are all explicitly stated in TASK_FILE. No additional objectives are introduced.]

## CONSTRAINTS

- The output document is to be written in English, following a professional engineering methodology style.
^[Confidence: HIGH, Rationale: TASK_FILE line 1 explicitly states "DOCUMENT IN ENGLISH (PROFESSIONAL ENGINEERING METHODOLOGY STYLE)."]
- All R code must use `data.table()` for data manipulation.
^[Confidence: HIGH, Rationale: TASK_FILE line 11 explicitly requires "usa data.table()."]
- All R code must avoid snake_case naming convention.
^[Confidence: HIGH, Rationale: TASK_FILE line 11 explicitly requires "evita snake_case notation."]
