# Spectral Matching of Pseudo-Acceleration Response Spectra via Weighted Linear Combination

## CONTEXT AND NOTATION

The overarching goal of this investigation is to formulate a robust framework for spectral matching of horizontal pseudo-acceleration response spectra $S_a(T_n)$ through weighted linear combination of recorded ground motion spectra.
^[Confidence: HIGH, Rationale: Directly paraphrases the purpose statement on TASK_FILE line 3, which establishes the scope as formulating a robust spectral matching framework for horizontal pseudo-acceleration response spectra.]

Traditional spectral matching methodologies modify recorded accelerograms to achieve conformity with target response spectra derived from probabilistic seismic hazard analysis (PSHA). These modifications fundamentally alter the frequency content, duration characteristics, and number of sign reversals present in the original ground motion records. Spectral matching also reduces the coefficient of variation among selected records, artificially suppressing record-to-record variability that reflects epistemic uncertainty in ground motion characteristics.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE lines 5-6, which describe how traditional spectral matching alters frequency content, duration, sign reversals, and suppresses record-to-record variability reflecting epistemic uncertainty.]

The seismic response of systems that accumulate damage under cyclic loading depends not only on peak amplitude but also on duration and the effective number of cycles - parameters recognized explicitly in liquefaction potential evaluation methods [@Green2005]. Time-domain and frequency-domain spectral matching often distorts the nonstationary characteristics of ground motion and may alter scalar parameters such as Arias intensity [@Akkar2010]. Numerous physical phenomena, including stiffness degradation and liquefaction, depend on the number of load reversals.
^[Confidence: HIGH, Rationale: Closely paraphrases TASK_FILE lines 10-11, preserving both citations [@Green2005] and [@Akkar2010] exactly as they appear in the source material.]

**Notation.** Given a candidate set of $m$ spectra $S_a(T_n)$ evaluated on a period mesh of $n$ points $\{T_1, \ldots, T_n\}$, the PSHA-derived target spectrum is encoded as the vector $\mathbf{y} \in \mathbb{R}^n$ with components $y_i = \ln S_a^{\mathrm{obj}}(T_i)$. The weights $w_k$ (for $k = 1, \ldots, m$) define the linear combination of candidate spectra whose discrepancy with respect to the target spectrum is to be minimized.
^[Confidence: HIGH, Rationale: Synthesizes notation from TASK_FILE lines 18-24, unifying the informal introduction (K spectra, N ordinates on lines 18-19) with the formal vector definitions on lines 21-22. The formal notation is preserved exactly; the informal variables are mapped to the formal ones for consistency.]

## SLOTS

### SLOT 1: Summary of spectral-content-modifying record selection methodologies

Provide a concise summary of seismic record selection methodologies that modify spectral content so that a linear combination of recorded spectra approximates a given target spectrum. The summary should distinguish the principal approaches (time-domain matching, frequency-domain matching, and selection-by-combination methods) and characterize their respective effects on ground motion properties.
^[Confidence: HIGH, Rationale: Directly addresses TASK_FILE line 12, which requests a brief summary of selection methodologies that modify spectral content to make the linear combination of spectra approximate the target spectrum. No content invented beyond what line 12 requests.]

### SLOT 2: Minimum record count and origin of the 7- and 11-record thresholds in seismic standards

Determine the minimum number of spectra required for spectral matching under the linear-combination approach described in SLOT 1. Explain the theoretical or empirical basis for the minimum record counts of 7 and 11 recommended by seismic design standards such as ASCE 7 for nonlinear structural analysis.
^[Confidence: HIGH, Rationale: Directly addresses TASK_FILE line 13, which asks two coupled questions: how many spectra are needed at minimum, and where the 7 or 11 minimum records recommended by standards like ASCE-7 originate. Both sub-questions are captured in this single slot.]

### SLOT 3: Classical linear regression formulation for spectral matching weights (RMSE)

Formulate the spectral matching problem as a classical linear regression problem in which the weights $w_k$ minimize the global root-mean-square error (RMSE) between the weighted linear combination of candidate spectra and the target spectrum $\mathbf{y}$. The formulation must employ the notation established in the Context and Notation section ($m$ candidates, $n$ periods, vector $\mathbf{y}$, weights $w_k$).
^[Confidence: HIGH, Rationale: Directly addresses TASK_FILE line 25, which requests a classical linear regression formulation seeking weights w that minimize global RMSE, explicitly requiring the notation defined earlier on lines 18-24.]

### SLOT 4: Reformulation of the regression problem in log-log space

Reformulate the linear regression problem from SLOT 3 in $\log(S_a)$-$\log(T_n)$ space, exploiting the observation that spectral functions are smoother in logarithmic coordinates. Maintain consistency with the notation from the Context section and relate the log-log formulation explicitly to the original-space formulation of SLOT 3.
^[Confidence: HIGH, Rationale: Directly addresses TASK_FILE lines 29-30. Line 29 provides the motivating context that functions are smoother in log-log space; line 30 requests reformulation of the same regression problem in that space using the established notation.]

### SLOT 5: Non-negative weight constraint extension with R implementation

The unconstrained regression from SLOTS 3-4 may yield negative weights, which lack physical interpretability as scaling factors for ground motion records. Extend the regression formulation to enforce strictly non-negative weights ($w_k \geq 0$ for all $k$). Address whether standard Ridge regression can directly accommodate a positivity constraint on the coefficients. Provide a working code example in R that implements the non-negative least squares solution.
^[Confidence: HIGH, Rationale: Directly addresses TASK_FILE lines 32-33. Line 32 provides context that some weights may be negative; line 33 poses three tightly coupled sub-questions: extending for non-negative weights, feasibility of Ridge with positivity constraints, and an R code example. All sub-questions are captured in this single slot.]

### SLOT 6: Bounded weight constraints ($w_{\min} \leq w_k \leq w_{\max}$) with Ridge/Lasso feasibility analysis

Beyond the non-negativity constraint of SLOT 5, impose box constraints $w_{\min} \leq w_k \leq w_{\max}$ on the weights, where $w_{\min}$ and $w_{\max}$ are user-specified bounds, to prevent excessively large or small scaling factors. Discuss whether Ridge or Lasso regression can enforce such box constraints on the coefficients. Provide a code example demonstrating the bounded-weight solution.
^[Confidence: HIGH, Rationale: Directly addresses TASK_FILE lines 36-37. Line 36 provides context requiring both lower and upper bounds on weights; line 37 asks about Ridge/Lasso applicability for this purpose and requests an example. The progression from SLOT 5 (non-negativity only) to SLOT 6 (full box constraints) mirrors the TASK_FILE structure.]

### SLOT 7: Convex optimization generalization with standard R libraries

Generalize the spectral matching problem as a convex optimization problem that subsumes the previous formulations (unconstrained, non-negative, and bounded weights) as special cases. Propose an explicit loss function formulation for the general case. Provide implementation examples using standard R optimization libraries (e.g., CVXR, quadprog, or equivalent).
^[Confidence: HIGH, Rationale: Directly addresses TASK_FILE line 39, which poses three sub-questions: whether the problem can be cast as convex optimization, what loss function to use, and requests examples using standard R libraries. All three are captured in this slot.]

## CONSTRAINTS

- The output document must be written entirely in English, in a professional engineering methodology style.
- All mathematical expressions must use LaTeX notation and follow the conventions established in the Context and Notation section (candidate set size $m$, period mesh size $n$, objective vector $\mathbf{y} \in \mathbb{R}^n$, weights $w_k$).
- All code examples (required by SLOTS 5, 6, and 7) must be implemented in the R programming language.
- Existing bibliographic citations ([@Green2005], [@Akkar2010]) must be preserved in the output.
^[Confidence: HIGH, Rationale: Each constraint derives from explicit TASK_FILE directives: English language and professional style from line 1; notation consistency from lines 18-24; R language from lines 33, 37, and 39; citation preservation from lines 10-11 where the citations appear.]
