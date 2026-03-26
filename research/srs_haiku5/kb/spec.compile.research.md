# Spectral-Matching Record Selection: Methodology, Linear Regression Formulation, and Constrained Optimization

## SLOT 1: Summary of Spectral-Matching Record-Selection Methodologies

Ground-motion record-selection methodologies aimed at achieving conformity between
the spectral properties of a selected suite and a PSHA-derived target spectrum fall
into two broad and conceptually distinct families, differentiated by whether the
physical time histories of the candidate accelerograms are altered before analysis.

The first family encompasses waveform-modification techniques, in which the time
history of a recorded accelerogram is directly altered either in the time domain or
in the frequency domain. Time-domain spectral matching, introduced by Lilhanand and
Tseng (1988) and extended by Abrahamson and subsequent authors, adds frequency-
localised wavelet pulses to the original accelerogram in an iterative fashion until
the response spectrum of the augmented record converges to the target spectrum; this
approach forms the basis of widely used tools such as RSPMatch and SeismoMatch
[@BakerCornell2006][@BEESelection2022]. Frequency-domain approaches iteratively
rescale the Fourier amplitude spectrum of the record while retaining its phase
spectrum. Both waveform-modification families alter the non-stationary amplitude
envelope, cycle count, and Arias intensity of the original recording. These
modifications compromise the accuracy of structural response estimates for systems
whose behaviour depends on cumulative damage accumulation, liquefaction potential,
or effective cycle count, because those response quantities are sensitive not only to
spectral amplitude but also to the duration and sequence of loading cycles
[@GMReview2023][@BEESelection2022].

The second family -- to which the linear-combination formulation belongs --
preserves the physical waveforms of the candidate accelerograms intact or applies
only a single global amplitude scale factor, achieving spectral conformity at the
suite level rather than at the individual-record level. In its most direct form this
approach assigns a weight $w_k$ to each of $K$ candidate records drawn from
databases such as PEER NGA-West2 and requires that the weighted linear combination
of spectral ordinates $\sum_{k=1}^{K} w_k S_{a,k}(T_i)$ approximates the target
spectral acceleration $S_a^{\mathrm{obj}}(T_i)$ across the full period mesh
$\{T_1, \dots, T_n\}$; the records themselves are never modified and the only
degrees of freedom are the components of the weight vector $\mathbf{w} =
(w_1, \dots, w_K)^\top$ [@BakerEtAl2011][@NIST2011]. The defining advantage over
waveform modification is that the original time histories -- including their
non-stationary amplitude content, phase structure, duration characteristics, and
frequency variation over time -- remain unchanged, making the selected suite
suitable for analyses sensitive to cumulative inelastic demands, ground-motion
duration, and effective number of load cycles.

Amplitude scaling is the simplest variant of the record-selection family: each
candidate accelerogram is multiplied by a single constant factor chosen so that a
representative spectral ordinate, or a geometric mean over a designated period
range, approaches the target value. The ASCE 7 procedure requires that the average
of the square-root-of-sum-of-squares (SRSS) spectra from all selected horizontal-
component pairs does not fall below the corresponding ordinate of the design
response spectrum over the period range $[0.2T_1,\, 1.5T_1]$ [@StructureMag].
While amplitude scaling preserves the original waveform, large scale factors can
bias nonlinear structural response, motivating more principled selection methods.

Probabilistic record-selection frameworks refined the suite-level matching objective
by anchoring the target spectrum to PSHA. Baker and Cornell (2006) demonstrated that
records selected to match the conditional mean spectrum (CMS) -- defined as the
expected value of $\ln S_a(T)$ at all periods conditioned on a target hazard level
and the spectral shape parameter $\varepsilon$ -- produce structural response
estimates that are unbiased relative to hazard-consistent benchmarks, whereas
records chosen to envelope the uniform hazard spectrum (UHS) introduce systematic
conservatism [@BakerCornell2006]. All such target spectra enter the linear-
combination methodology as the target vector $\mathbf{y} \in \mathbb{R}^n$ with
components $y_i = \ln S_a^{\mathrm{obj}}(T_i)$.

The Jayaram-Lin-Baker (2011) algorithm generalised the target to include both the
conditional mean and variance of $\ln S_a(T)$ across all periods, formulating
record selection as a greedy iterative optimisation in which records are swapped into
and out of the suite to reduce the total squared deviation between the suite
log-mean spectrum and the target [@BakerEtAl2011][@JayaramBaker2011]. Energy-
compatible selection methods extended the target criterion further to include the
input energy equivalent velocity spectrum, reducing bias for long-duration records
and records from stiff-soil sites [@Frontiers2019]. Multi-objective optimisation
algorithms based on harmony search, genetic algorithms, or stochastic meta-
heuristics address the selection problem with multiple simultaneous fitness criteria
without requiring a scalar weighting between competing objectives [@BEEMultiObj2022].
The linear-regression formulation described in the subsequent sections provides a
unified algebraic framework for the suite-level matching problem in its most direct
form.

---

## SLOT 2: Minimum Number of Records and Code-Based Requirements

### Algebraic Minimum

In the linear-combination framework, the minimum number of candidate spectra $K$
required to obtain a feasible spectral match can be analysed from two perspectives:
the algebraic structure of the optimisation problem and the statistical quality of
the resulting ensemble. The design matrix $\mathbf{A} \in \mathbb{R}^{n \times K}$
has $n$ rows corresponding to period ordinates and $K$ columns corresponding to
candidate records. When $K < n$ the system is overdetermined and the ordinary
least-squares solution minimises the residual norm $\|\mathbf{A}\mathbf{w} -
\mathbf{b}\|_2$ without reducing it to zero in general, with the residual decreasing
monotonically as $K$ increases provided the additional records contribute linearly
independent spectral shapes. When $K = n$ and $\mathbf{A}$ has full rank, an exact
zero-residual solution exists; when $K > n$ the system is underdetermined and
additional constraints or regularisation are required for uniqueness. In the
spectral-matching context, the period mesh typically contains $n = 50$ to $100$
points while $K$ rarely exceeds 20, so the operative regime is always overdetermined
and the theoretical algebraic minimum for a valid regression is $K = 1$.

In practice, a single well-chosen record with appropriate scaling can satisfy only
simple mean-spectrum compatibility criteria; it provides no information about
spectral variability and is statistically unreliable for structural response
estimation. The adequacy of the spectral match depends on how well the span of the
$K$ candidate log-spectral vectors covers the region of log-spectral-shape space
containing $\mathbf{y}$, so a minimum number of records with diverse magnitudes,
distances, site conditions, and spectral shapes is needed to prevent systematic
underrepresentation of any frequency sub-range of the target mesh.

### Seven-Record Minimum (ASCE 7-10)

The minimum-record thresholds embedded in modern seismic design codes originate from
statistical and engineering-judgement studies on the variability of structural
response estimates as a function of suite size. Early editions of ASCE/SEI 7
(through ASCE 7-05 and ASCE 7-10) required a minimum of three ground-motion pairs
for nonlinear response history analysis, with an important conditional: if fewer than
seven ground motions are analysed, the design engineer must base the design on the
maximum structural response among all records in the suite rather than the average,
whereas if seven or more records are used, the average response is permitted
[@StructureMag]. The seven-record threshold was originally established based on
engineering experience rather than a systematic statistical study, as explicitly
acknowledged in the USGS open-file report that subsequently provided empirical
justification [@ReyesKalkan2011].

Jayaram and Baker (2010) demonstrated through Monte Carlo experiments assembling 480
ground-motion sets by random sampling from a large database that suites of fewer than
seven records yield engineering demand parameter (EDP) estimates that are
statistically conservative relative to benchmark values computed from large ensembles,
and that utilising seven or more randomly selected records produces suite-mean EDPs
that converge to within acceptable bounds of the benchmark [@JayaramBaker2010].
Selecting records on the basis of spectral shape and design spectral acceleration
rather than randomly further improves efficiency, allowing equivalent accuracy with
fewer records. The underlying statistical rationale for the seven-record rule is
therefore a sample-mean convergence criterion: the standard error of the mean EDP
scales as $\sigma / \sqrt{K}$, and seven records represent an empirically calibrated
balance between computational cost and the reliability of the suite mean as a proxy
for the hazard-consistent expected response.

### Eleven-Record Minimum (ASCE 7-16 and ASCE 7-22)

ASCE/SEI 7-16 introduced a substantially revised Chapter 16 for nonlinear response
history analysis (NRHA), increasing the minimum suite size to eleven ground-motion
pairs for buildings subject to site-specific maximum considered earthquake (MCER)
hazard analysis [@ASCE716Comparison]. This requirement was retained in ASCE/SEI 7-22
[@ASCE2022]. The engineering rationale for the increase from seven to eleven records
reflects the recognition that eleven records provide a statistically more robust
basis for computing structural response statistics, particularly for the
displacement-controlled limit states and collapse margin assessments that underlie
the ASCE 7-16 Chapter 16 framework. Under ASCE/SEI 7-16, three-dimensional NRHA
requires a minimum of eleven ground-motion pairs (two horizontal components per
pair), and with eleven records the coefficient of variation of the estimated mean
response is sufficiently small that no additional conservatism factor analogous to
the maximum-over-suite rule is required.

The shift from seven to eleven also aligns with the recommendations of NIST GCR
11-917-15, which advocated for larger suite sizes to improve the fidelity of
nonlinear analysis outcomes [@NIST2011]. The eleven-record minimum is therefore a
regulatory threshold calibrated to ensure that mean-based design is statistically
defensible under the revised acceptance criteria of ASCE/SEI 7-16, rather than a
number derived analytically from the linear-combination optimisation theory itself.

---

## SLOT 3: Classical Linear Regression Formulation (RMSE Minimization)

The spectral-matching problem is cast as a classical ordinary least-squares (OLS)
regression by assembling the spectral ordinates of the $K$ candidate records into a
design matrix and the target spectral ordinates into a response vector. Define the
design matrix $\mathbf{A} \in \mathbb{R}^{n \times K}$ with entries

$$A_{ik} = S_{a,k}(T_i), \quad i = 1, \dots, n, \quad k = 1, \dots, K,$$

where $S_{a,k}(T_i)$ is the pseudo-spectral acceleration of the $k$-th candidate
record at period $T_i$. Each column $\mathbf{A}_{\cdot k}$ contains the discretised
response spectrum of the $k$-th candidate record, and each row $\mathbf{A}_{i \cdot}$
contains the spectral accelerations of all $K$ records at the single period $T_i$.
Define the target vector $\mathbf{b} \in \mathbb{R}^n$ with components
$b_i = S_a^{\mathrm{obj}}(T_i)$, the spectral ordinate of the PSHA-derived target
at period $T_i$ in physical units; note that $b_i = \exp(y_i)$ where $\mathbf{y}$ is
the log-domain target vector from the context with $y_i = \ln S_a^{\mathrm{obj}}(T_i)$.
The predicted spectral combination is $\hat{\mathbf{b}} = \mathbf{A}\mathbf{w}$
[@BEESelection2022].

The objective of the spectral-matching regression is to find the weight vector
$\mathbf{w} = (w_1, \dots, w_K)^\top$ that minimises the global root-mean-square
error (RMSE) between the weighted linear combination of candidate spectra and the
target spectrum across all $n$ period ordinates:

$$\mathrm{RMSE}(\mathbf{w}) = \sqrt{\frac{1}{n} \sum_{i=1}^{n}
\left(\sum_{k=1}^{K} w_k S_{a,k}(T_i) - b_i\right)^2}
= \frac{1}{\sqrt{n}} \|\mathbf{A}\mathbf{w} - \mathbf{b}\|_2.$$

Since $n$ is a fixed positive constant, minimising RMSE is equivalent to minimising
the residual sum of squares (RSS):

$$\min_{\mathbf{w} \in \mathbb{R}^K} \|\mathbf{A}\mathbf{w} - \mathbf{b}\|_2^2.$$

The objective is a convex quadratic in $\mathbf{w}$ with gradient
$2\mathbf{A}^\top(\mathbf{A}\mathbf{w} - \mathbf{b})$. Setting the gradient to zero
yields the normal equations:

$$\mathbf{A}^\top \mathbf{A}\, \hat{\mathbf{w}} = \mathbf{A}^\top \mathbf{b}.$$

Provided $\mathbf{A}$ has full column rank (i.e., $\mathrm{rank}(\mathbf{A}) = K$,
which requires $n \geq K$ and the candidate spectra to be linearly independent over
the period mesh), the Gram matrix $\mathbf{A}^\top\mathbf{A} \in \mathbb{R}^{K\times K}$
is invertible and the unique closed-form OLS solution is:

$$\hat{\mathbf{w}} = \left(\mathbf{A}^\top \mathbf{A}\right)^{-1} \mathbf{A}^\top
\mathbf{b}.$$

The $(j,k)$-th entry of the Gram matrix, $\sum_{i=1}^n S_{a,j}(T_i) S_{a,k}(T_i)$,
measures the spectral similarity between records $j$ and $k$ over the period mesh,
and the vector $\mathbf{A}^\top\mathbf{b} \in \mathbb{R}^K$ contains the cross-
correlations between each candidate spectrum and the target. When $K > n$ the Gram
matrix is singular; the minimum-norm solution $\hat{\mathbf{w}} = \mathbf{A}^+\mathbf{b}$
is then obtained via the Moore-Penrose pseudoinverse. Near-collinearity in the
candidate set renders the Gram matrix ill-conditioned; QR decomposition or SVD of
$\mathbf{A}$ provide numerically stable alternatives to explicit inversion
[@BEESelection2022].

The unconstrained OLS solution does not restrict the sign or magnitude of
$\hat{\mathbf{w}}$; negative weights, which imply subtraction of a scaled
accelerogram from the combination, can appear and are physically meaningless for
real ground-motion records. Regularised and constrained extensions of this
formulation are developed in the subsequent sections.

---

## SLOT 4: Log-Log Space Reformulation

### Motivation

Pseudo-spectral acceleration values span several orders of magnitude across the
period range of engineering interest, and the scatter of recorded spectra about a
median curve is well described by a log-normal distribution -- the distributional
model underlying all modern GMPEs. This log-normality reflects the approximately
power-law scaling of spectral content with period: beyond the spectral plateau,
$S_a(T)$ decays roughly as $T^{-\alpha}$ for some positive exponent $\alpha$, so
that $\ln S_a$ varies nearly linearly with $\ln T$. Performing the regression in the
linear domain (SLOT 3) therefore assigns disproportionate leverage to large absolute
spectral values at short periods, distorting the match at longer periods where
inelastic displacement demands are typically most relevant. Representing both spectral
ordinates and periods on logarithmic scales produces a space in which spectral curves
are approximately linear, smoother, and more homoscedastic, and aligns with the
standard PSHA convention of treating $\ln S_a(T)$ as normally distributed
[@BakerCornell2006][@BEESelection2022].

### Transformed Design Matrix and Target Vector

The log-log reformulation applies the natural logarithm to all spectral ordinates.
Define the transformed design matrix $\tilde{\mathbf{A}} \in \mathbb{R}^{n \times K}$
with entries

$$\tilde{A}_{ik} = \ln S_{a,k}(T_i), \quad i = 1, \dots, n, \quad k = 1, \dots, K,$$

and the transformed target vector $\tilde{\mathbf{y}} \in \mathbb{R}^n$ with
components

$$\tilde{y}_i = \ln S_a^{\mathrm{obj}}(T_i) = y_i,$$

which is identical to the log-space target $\mathbf{y}$ defined in the context. The
weight vector $\mathbf{w} = (w_1, \dots, w_K)^\top$ retains the same definition. The
transformed regression model is $\tilde{\mathbf{y}} \approx \tilde{\mathbf{A}}\mathbf{w}$.

### Objective Function

$$\mathrm{MSE}_{\mathrm{LL}}(\mathbf{w}) = \frac{1}{n}
\|\tilde{\mathbf{A}}\mathbf{w} - \tilde{\mathbf{y}}\|_2^2
= \frac{1}{n} \sum_{i=1}^{n} \left(\sum_{k=1}^{K} w_k \ln S_{a,k}(T_i)
- \ln S_a^{\mathrm{obj}}(T_i)\right)^2.$$

The closed-form solution retains the same structural form as in SLOT 3:

$$\hat{\mathbf{w}} = \left(\tilde{\mathbf{A}}^\top \tilde{\mathbf{A}}\right)^{-1}
\tilde{\mathbf{A}}^\top \tilde{\mathbf{y}},$$

provided $\tilde{\mathbf{A}}$ has full column rank. The period mesh is typically
chosen log-uniform (equally spaced in $\ln T$), ensuring that each decade of the
period axis contributes equally to the objective, which further improves the
conditioning of $\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}$ relative to the linearly
spaced formulation [@BEESelection2022].

The fitted log-spectral value at period $T_i$ is
$\hat{y}_i = \sum_{k=1}^K w_k \ln S_{a,k}(T_i)$, which in the original spectral
domain corresponds to a geometric weighted combination:

$$\hat{S}_a(T_i) = \exp(\hat{y}_i) = \prod_{k=1}^{K} S_{a,k}(T_i)^{w_k}.$$

The minimised $\mathrm{RMSE}_{\log}$ measures discrepancy in log spectral amplitude
units -- the natural units for PSHA-derived targets -- with a unit residual
corresponding approximately to a factor-of-$e$ error in spectral acceleration
[@BakerEtAl2011].

---

## SLOT 5: Non-Negative Weight Constraint and R Implementation

### Physical Motivation

The unconstrained OLS solution $\hat{\mathbf{w}} = (\tilde{\mathbf{A}}^\top
\tilde{\mathbf{A}})^{-1}\tilde{\mathbf{A}}^\top\mathbf{y}$ admits negative
components whenever two or more candidate spectra are highly correlated. A negative
weight $w_k < 0$ would imply subtracting a scaled version of record $k$ from the
spectral combination, which corresponds to adding an accelerogram with negated
amplitude -- a construct with no physical meaning in seismic hazard analysis. No
anti-record exists in any strong-motion database. Physical plausibility therefore
requires $w_k \geq 0$ for all $k = 1, \dots, K$ [@WikipediaNNLS]. An additional
practical consequence is that the non-negativity constraint promotes sparse solutions:
many $w_k$ will be driven to exactly zero at the optimum, effectively performing
simultaneous record selection and weight assignment.

### NNLS Problem Formulation

$$\min_{\mathbf{w} \in \mathbb{R}^K} \;\|\tilde{\mathbf{A}}\mathbf{w} -
\mathbf{y}\|_2^2 \quad \text{subject to} \quad w_k \geq 0, \quad
k = 1, \dots, K.$$

The feasible region is the non-negative orthant, a closed convex cone. The objective
is a strictly convex quadratic, guaranteeing a unique global minimiser (when
$\tilde{\mathbf{A}}$ has full column rank). The canonical algorithm is the active-set
method of Lawson and Hanson (1974), which partitions the index set $\{1, \dots, K\}$
into an active set $\mathcal{Z}$ (indices where $w_k = 0$) and a passive set
$\mathcal{P}$ (indices free to be positive), solves the unconstrained OLS sub-problem
restricted to $\mathcal{P}$ at each iteration, and updates the partition until the
Karush-Kuhn-Tucker (KKT) conditions are satisfied [@Mullen2012].

### Ridge and Lasso Cannot Enforce Non-Negativity

Ridge regression produces $\hat{\mathbf{w}}^{\mathrm{Ridge}} =
(\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}} + \lambda\mathbf{I})^{-1}
\tilde{\mathbf{A}}^\top\mathbf{y}$, an unconstrained solution on $\mathbb{R}^K$. The
$\ell_2$ penalty shrinks coefficient magnitudes globally but cannot enforce $w_k \geq 0$
because the Euclidean ball is symmetric about the origin and does not exclude the
negative orthant. Lasso regression can drive individual coefficients to zero but does
not prevent negative non-zero coefficients; a non-negative Lasso variant (`nnlasso`)
exists as a separate CRAN package but is a distinct algorithm from the standard
solvers [@StarkBVLS][@WikipediaRegLS]. Standard Ridge and Lasso formulations cannot
substitute for the NNLS constraint; a dedicated inequality-constrained solver is
required.

### R Implementation

```r
library(nnls)

fit_nnls  <- nnls(A = A, b = y)
w_hat     <- fit_nnls$x          # non-negative weight vector (length K)
residuals <- fit_nnls$residuals  # n-vector of residuals y - A %*% w_hat
rmse      <- sqrt(mean(residuals^2))
cat("NNLS RMSE (log-spectral units):", rmse, "\n")
```

Indices where `w_hat[k] == 0` correspond to records eliminated by the active-set
constraint. An alternative using `glmnet` recovers the NNLS solution by setting
`lower.limits = 0` with `lambda = 0`:

```r
library(glmnet)

fit_glmnet   <- glmnet(x = A, y = y, lambda = 0,
                       lower.limits = 0, intercept = FALSE)
w_hat_glmnet <- as.numeric(coef(fit_glmnet))[-1]  # drop intercept slot
```

---

## SLOT 6: Bounded Weights with Ridge/Lasso Feasibility

### Motivation for Box Constraints

The NNLS formulation enforces a lower bound of zero on each weight but imposes no
upper bound. An excessively large weight assigned to a single record effectively
reduces the spectral combination to a single-record computation, negating the
statistical rationale for a multi-record suite. Conversely, a strictly positive lower
bound $w_{\min} > 0$ ensures that every record in a pre-screened library contributes
at least minimally to the combination. Box constraints

$$w_{\min} \leq w_k \leq w_{\max}, \quad k = 1, \dots, K,$$

where $w_{\min} \geq 0$ and $w_{\max} < \infty$, formalise both requirements.
Setting $w_{\min} = 0$ and $w_{\max} = +\infty$ recovers the NNLS case.

### Bounded-Variable Least-Squares Formulation

$$\mathbf{w}^* = \underset{\mathbf{w} \in \mathbb{R}^K}{\arg\min}
\;\|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to}
\quad w_{\min} \leq w_k \leq w_{\max} \; \text{for all} \; k = 1, \dots, K.$$

The feasible set is a compact convex polytope (an axis-aligned hyperrectangle in
$\mathbb{R}^K$), and the strictly convex quadratic objective guarantees a unique
global minimiser. The problem is equivalently cast as a quadratic program (QP) with
$2K$ linear inequality constraints [@GoldfarbIdnani1983].

### Why Ridge and Lasso Cannot Substitute for Box Constraints

Ridge's $\ell_2$ penalty provides no per-component upper bound and cannot enforce a
positive lower bound $w_{\min} > 0$. Lasso's $\ell_1$ penalty can drive coefficients
to zero (a zero lower bound) but cannot impose $w_{\min} > 0$ or $w_{\max} < \infty$.
A constrained Lasso formulation (James, Paulson, and Rusmevichientong) handles
arbitrary linear constraints but requires dedicated algorithms beyond the standard
coordinate-descent Lasso [@JamesEtAl2019]. Neither standard Ridge nor standard Lasso
can enforce general box constraints; a BVLS solver or a QP formulation is required
[@GoldfarbIdnani1983][@WikipediaRidge].

### R Implementation

```r
library(quadprog)

K     <- ncol(A_tilde)
Dmat  <- 2 * crossprod(A_tilde) + diag(K) * 1e-8  # 2*A'A plus small ridge for PD
dvec  <- 2 * as.vector(crossprod(A_tilde, y))       # 2*A'y
w_min <- 0.0
w_max <- 2.0

Amat    <- cbind(diag(K), -diag(K))
bvec    <- c(rep(w_min, K), rep(-w_max, K))
fit_box <- solve.QP(Dmat = Dmat, dvec = dvec, Amat = Amat, bvec = bvec)
w_box   <- fit_box$solution
```

The solution `w_box` satisfies $w_{\min} \leq w_k \leq w_{\max}$ by construction.
The small diagonal perturbation (`1e-8`) is standard numerical stabilisation for
near-singular Gram matrices, as `quadprog` requires `Dmat` to be positive definite.
When $w_{\min} = 0$ this formulation reduces to a non-negative LS problem, though
`nnls` is computationally preferable for the pure unpenalised non-negative case
[@GoldfarbIdnani1983]. The R `bvls` package (Stark-Parker algorithm) provides an
alternative solver that handles two-sided bounds directly without reformulation as a
general QP [@StarkBVLS].

---

## SLOT 7: Convex Optimization Generalization with R Libraries

### General Loss Function

The spectral-matching problem admits a unified convex formulation that subsumes the
unconstrained OLS, the NNLS, and the bounded-weight LS problems as special cases and
accommodates additional convex penalty terms. The general loss function combines a
squared-error fidelity term, a Lasso-type sparsity penalty with non-negative
coefficient $\lambda_1 \geq 0$, and a Ridge-type shrinkage penalty with non-negative
coefficient $\lambda_2 \geq 0$, all minimised over the box-constrained feasible set:

$$\mathcal{L}(\mathbf{w}) = \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2
+ \lambda_1 \|\mathbf{w}\|_1 + \lambda_2 \|\mathbf{w}\|_2^2 \quad \text{subject to}
\quad w_{\min} \leq w_k \leq w_{\max}, \quad k = 1, \dots, K.$$

The special-case reductions are exact: setting $\lambda_1 = \lambda_2 = 0$ with
$w_{\min} = 0$ and $w_{\max} = +\infty$ recovers the NNLS problem; setting
$\lambda_1 = \lambda_2 = 0$ with finite bounds recovers the bounded-weight QP of
SLOT 6; $\lambda_2 > 0$ with $\lambda_1 = 0$ produces a Ridge-regularised bounded
LS problem; $\lambda_1 > 0$ introduces a sparsity incentive that drives weights
toward $w_{\min}$ while the box constraint prevents violation of the lower bound,
producing a regularised sparse solution on $[w_{\min}, w_{\max}]$ [@FuEtAl2020].

### Convexity

$\mathcal{L}(\mathbf{w})$ is a sum of three convex functions: the squared $\ell_2$
norm (quadratic with positive-semidefinite Hessian $2\tilde{\mathbf{A}}^\top
\tilde{\mathbf{A}}$), the $\ell_1$ norm (convex polyhedral), and the scaled squared
$\ell_2$ norm (strongly convex for $\lambda_2 > 0$). The constraint set is a closed
convex box. Any local minimum is therefore a global minimum, and standard interior-
point or active-set solvers converge to the global solution in polynomial time
[@FuEtAl2020].

### R Implementation with CVXR

The `CVXR` package implements disciplined convex programming (DCP) in R, verifying
convexity using DCP composition rules and dispatching to solvers such as CLARABEL,
SCS, or OSQP [@FuEtAl2020]:

```r
library(CVXR)

K       <- ncol(A_tilde)
w       <- Variable(K)
lambda1 <- 0.01   # L1 (Lasso) penalty weight  (set to 0 for pure bounded LS)
lambda2 <- 0.001  # L2 (Ridge) penalty weight  (set to 0 for pure bounded LS)
w_min   <- 0.0    # lower bound (0 for NNLS)
w_max   <- 2.0    # upper bound

obj  <- Minimize(
          sum_squares(A_tilde %*% w - y) +
          lambda1 * norm1(w) +
          lambda2 * sum_squares(w)
        )
cons <- list(w >= w_min, w <= w_max)
prob <- Problem(obj, cons)
res  <- solve(prob)

w_opt <- as.vector(res$getValue(w))
cat("Optimal weights:", round(w_opt, 4), "\n")
cat("Objective value:", res$value, "\n")
```

### Solver Selection and Scalability

For problems in which $\lambda_1 = 0$, the problem reduces to a QP and `quadprog`
is computationally preferable for small to moderate problem sizes. When $\lambda_1 > 0$,
CVXR handles the non-smooth $\ell_1$ term automatically through epigraph
linearisation (introducing auxiliary variables $\mathbf{u}$ with $\mathbf{u} \geq
\mathbf{w}$ and $\mathbf{u} \geq -\mathbf{w}$, then minimising $\mathbf{1}^\top
\mathbf{u}$ in place of $\|\mathbf{w}\|_1$). For large candidate sets or fine period
meshes, the `osqp` package provides a scalable warm-started ADMM solver for the QP
sub-problems [@FuEtAl2020]. The CVXR approach is recommended for full generality
when explicit box constraints are combined with penalty terms; `nnls` remains the
computationally optimal choice for the pure unpenalised non-negative case.
