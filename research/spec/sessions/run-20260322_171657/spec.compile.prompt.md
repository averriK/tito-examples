# Spectral Matching of Pseudo-Acceleration Response Spectra via Weighted Linear Combination

## CONTEXT AND NOTATION

The overarching goal of this investigation is to formulate a robust framework for spectral matching of horizontal pseudo-acceleration response spectra $S_a(T_n)$ through weighted linear combination of recorded ground motion spectra.


Traditional spectral matching methodologies modify recorded accelerograms to achieve conformity with target response spectra derived from probabilistic seismic hazard analysis (PSHA). These modifications fundamentally alter the frequency content, duration characteristics, and number of sign reversals present in the original ground motion records. Spectral matching also reduces the coefficient of variation among selected records, artificially suppressing record-to-record variability that reflects epistemic uncertainty in ground motion characteristics.


The seismic response of systems that accumulate damage under cyclic loading depends not only on peak amplitude but also on duration and the effective number of cycles - parameters recognized explicitly in liquefaction potential evaluation methods [@Green2005]. Time-domain and frequency-domain spectral matching often distorts the nonstationary characteristics of ground motion and may alter scalar parameters such as Arias intensity [@Akkar2010]. Numerous physical phenomena, including stiffness degradation and liquefaction, depend on the number of load reversals.


**Notation.** Given a candidate set of $m$ spectra $S_a(T_n)$ evaluated on a period mesh of $n$ points $\{T_1, \ldots, T_n\}$, the PSHA-derived target spectrum is encoded as the vector $\mathbf{y} \in \mathbb{R}^n$ with components $y_i = \ln S_a^{\mathrm{obj}}(T_i)$. The weights $w_k$ (for $k = 1, \ldots, m$) define the linear combination of candidate spectra whose discrepancy with respect to the target spectrum is to be minimized.


## SLOTS

### SLOT 1: Summary of spectral-content-modifying record selection methodologies

Provide a concise summary of seismic record selection methodologies that modify spectral content so that a linear combination of recorded spectra approximates a given target spectrum. The summary should distinguish the principal approaches (time-domain matching, frequency-domain matching, and selection-by-combination methods) and characterize their respective effects on ground motion properties.


### SLOT 2: Minimum record count and origin of the 7- and 11-record thresholds in seismic standards

Determine the minimum number of spectra required for spectral matching under the linear-combination approach described in SLOT 1. Explain the theoretical or empirical basis for the minimum record counts of 7 and 11 recommended by seismic design standards such as ASCE 7 for nonlinear structural analysis.


### SLOT 3: Classical linear regression formulation for spectral matching weights (RMSE)

Formulate the spectral matching problem as a classical linear regression problem in which the weights $w_k$ minimize the global root-mean-square error (RMSE) between the weighted linear combination of candidate spectra and the target spectrum $\mathbf{y}$. The formulation must employ the notation established in the Context and Notation section ($m$ candidates, $n$ periods, vector $\mathbf{y}$, weights $w_k$).


### SLOT 4: Reformulation of the regression problem in log-log space

Reformulate the linear regression problem from SLOT 3 in $\log(S_a)$-$\log(T_n)$ space, exploiting the observation that spectral functions are smoother in logarithmic coordinates. Maintain consistency with the notation from the Context section and relate the log-log formulation explicitly to the original-space formulation of SLOT 3.


### SLOT 5: Non-negative weight constraint extension with R implementation

The unconstrained regression from SLOTS 3-4 may yield negative weights, which lack physical interpretability as scaling factors for ground motion records. Extend the regression formulation to enforce strictly non-negative weights ($w_k \geq 0$ for all $k$). Address whether standard Ridge regression can directly accommodate a positivity constraint on the coefficients. Provide a working code example in R that implements the non-negative least squares solution.


### SLOT 6: Bounded weight constraints ($w_{\min} \leq w_k \leq w_{\max}$) with Ridge/Lasso feasibility analysis

Beyond the non-negativity constraint of SLOT 5, impose box constraints $w_{\min} \leq w_k \leq w_{\max}$ on the weights, where $w_{\min}$ and $w_{\max}$ are user-specified bounds, to prevent excessively large or small scaling factors. Discuss whether Ridge or Lasso regression can enforce such box constraints on the coefficients. Provide a code example demonstrating the bounded-weight solution.


### SLOT 7: Convex optimization generalization with standard R libraries

Generalize the spectral matching problem as a convex optimization problem that subsumes the previous formulations (unconstrained, non-negative, and bounded weights) as special cases. Propose an explicit loss function formulation for the general case. Provide implementation examples using standard R optimization libraries (e.g., CVXR, quadprog, or equivalent).


## CONSTRAINTS

- The output document must be written entirely in English, in a professional engineering methodology style.
- All mathematical expressions must use LaTeX notation and follow the conventions established in the Context and Notation section (candidate set size $m$, period mesh size $n$, objective vector $\mathbf{y} \in \mathbb{R}^n$, weights $w_k$).
- All code examples (required by SLOTS 5, 6, and 7) must be implemented in the R programming language.
- Existing bibliographic citations ([@Green2005], [@Akkar2010]) must be preserved in the output.

