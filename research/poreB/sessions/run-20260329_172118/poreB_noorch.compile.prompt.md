# Structured Prompt: Shear Strain History from Seismic Base Acceleration

## Context

The overarching research objective is to formulate a simple proxy model for predicting pore pressure increase in a saturated fine-grained material subjected to a seismic acceleration record. The physical configuration consists of a homogeneous, fine-grained, saturated stratum of thickness $H_s$ resting on rock. The stratum exhibits depth-variable shear stiffness $G_o(z)$, with its maximum value $G_o = G(z=0)$ at the base. A seismic acceleration history $a_g(t)$ is applied at the base of the stratum. The KB/ directory contains analytical closed-form solutions for the site response, expressed in terms of instantaneous accelerations $a(z,t)$ at arbitrary depths within the stratum.


## SLOTS

### SLOT 1: Numerical R algorithm for instantaneous shear strain history

The required deliverable is a numerical algorithm implemented in R that, given a base acceleration time history $a_g(t)$, estimates the instantaneous shear strain history $\gamma(z,t)$ at any depth $z$ within the stratum. The computational procedure involves two coupled steps: (a) computing the instantaneous acceleration field $a(z,t)$ at any depth $z$ from the base excitation $a_g(t)$, using the analytical closed-form site response solutions available in KB/; and (b) deriving the instantaneous shear strain history $\gamma(z,t)$ from the computed acceleration field $a(z,t)$. The R implementation must use `data.table()` for data handling and must avoid snake_case naming convention throughout the code.


## CONSTRAINTS

- Output language: English.
- Document style: professional engineering methodology.


