# Structured Prompt - Pore Pressure Proxy Model: Site Response and Shear Strains

## CONTEXT

The overarching research objective is to formulate a simple proxy model for predicting pore pressure increase in a saturated fine-grained material subjected to a seismic acceleration record. The two slots below address the foundational analytical components of that model: first the acceleration field within the stratum, then the shear strain field derived from it.

The physical setting common to both slots is as follows. A homogeneous, fine-grained, saturated soil stratum of thickness $H_s$ rests on rock. The small-strain shear modulus varies with depth according to a profile $G_o(z)$, reaching its maximum value $G_o = G(z=0)$ at the base. The stratum is subjected to a prescribed horizontal acceleration time history $a_g(t)$ applied at the rock interface.

## SLOTS

### SLOT 1: Closed-form analytical solutions for the seismic site acceleration response

Investigate and compile the different analytical (closed-form) formulations that describe the one-dimensional seismic site response of the stratum defined above in terms of instantaneous accelerations $a(z, t)$ at arbitrary depths within the deposit. The investigation should cover:

- The governing wave equation and boundary conditions (free surface at the top, prescribed base motion at rock).
- Closed-form solutions available in the literature for profiles where $G_o(z)$ varies with depth (e.g., linear, power-law, or other classical profiles) as well as the uniform-stiffness limiting case.
- The mathematical form of each solution, including modal decomposition, frequency-domain transfer functions, and any assumptions regarding linear viscoelastic or equivalent-linear soil behavior.
- Identification of the key parameters controlling the solution (stratum thickness $H_s$, base stiffness $G_o$, stiffness profile shape, damping ratio, impedance contrast at the base).

*Task-file justification*: This slot corresponds directly to the first "Pregunta" (lines 6-7 of the task file), which requests investigation of the different analytical closed-form solutions of the site response in terms of instantaneous accelerations $a(t, z)$ at different points of the stratum, given the stated material and geometric conditions.

### SLOT 2: Closed-form equations for seismic shear strains derived from the acceleration field

Starting from the instantaneous acceleration solutions $a(z, t)$ obtained in Slot 1, derive and present the closed-form expressions for the shear strain field $\gamma(z, t)$. The derivation should address:

- The kinematic relationship linking shear strain to the displacement or acceleration field through differentiation with respect to depth, i.e., $\gamma(z, t) = \partial u(z, t) / \partial z$, and the equivalent expression in terms of acceleration.
- Explicit closed-form strain equations for each analytical site-response model compiled in Slot 1.
- Discussion of how the stiffness profile $G_o(z)$ and the modal structure of the acceleration solution influence the depth distribution and time variation of shear strains.

*Task-file justification*: This slot corresponds directly to the second "Pregunta" (lines 10-11 of the task file), which requests formulation of the closed-form equations of the shear distortions $\gamma(z, t)$ defined as the derivative of the response with respect to depth, starting from the instantaneous accelerations at any point of the stratum.

## CONSTRAINTS

- The output document must be written entirely in English.
- The document must follow a professional engineering methodology style.
