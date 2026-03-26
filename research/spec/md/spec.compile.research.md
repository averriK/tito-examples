# Spectral Matching via Linear Combination of Pseudo-Acceleration Response Spectra

## SLOT 1: Overview of Record Selection Methodologies Based on Spectral Content Modification

The earthquake engineering literature recognizes four principal classes of ground motion record selection methodology that manipulate or exploit spectral content to approximate a target response spectrum: uniform amplitude scaling, frequency-content modification of individual records, weighted linear combination of candidate spectra, and optimization-based ensemble selection. A fifth approach - conditional mean spectrum (CMS) selection - is probabilistically motivated and does not itself modify spectral content, but it determines the target spectral shape against which the other methods operate and is therefore methodologically complementary to all of them. [@Ref001]



Uniform amplitude scaling is the most widely applied and least invasive approach. Each accelerogram is multiplied by a single scalar factor chosen so that the resulting response spectrum satisfies a code-specified amplitude criterion over a defined period range. Under ASCE/SEI 7-10, the requirement is that the average square-root-of-the-sum-of-squares (SRSS) spectrum computed from all horizontal component pairs does not fall below the corresponding ordinate of the design spectrum over the period range $0.2T_1$ to $1.5T_1$, where $T_1$ is the fundamental period of the structure [@Ref002]. Amplitude scaling preserves the inherent frequency content, duration, and number of sign reversals of each record. Its primary limitation is the inability to correct spectral shape inconsistencies across the full period range; very large scale factors become necessary when the selected records exhibit spectral shapes that are substantially different from the target, and such factors can inflate structural demand through the amplification of frequency components that would otherwise be minor.



Frequency-content modification methods alter the Fourier amplitude spectrum - while preserving or approximately preserving the phase spectrum - so that the resulting record matches the target spectrum at all spectral periods. Wavelet-based algorithms, including the approach of Abrahamson (1992), the refinement by Hancock et al. (2006), and the formulation by Atik and Abrahamson (2010) implemented in tools such as SeismoMatch, are among the most widely adopted implementations [@Ref003]. These methods achieve near-perfect spectral conformity but fundamentally alter the frequency content, phasing, and input energy of the original records. Spectrally matched suites consequently exhibit reduced record-to-record variability in spectral amplitude, suppressing the epistemic component of ground motion uncertainty [@Akkar2010]. The non-stationary character of the original strong-motion phase is also affected, which may alter cumulative inelastic demand in systems whose response depends on the number of load reversals, including structures subject to stiffness degradation and soils susceptible to liquefaction [@Green2005].



Weighted linear combination of unmodified spectra constitutes a methodologically distinct alternative that avoids any alteration of individual accelerograms. A suite of $K$ candidate records is retained in its original form; the spectral ordinates $Sa_k(T_n)$ of the constituent records are combined as a weighted sum, and the weight vector $\mathbf{w} = (w_1, \ldots, w_K)^\top$ is selected to minimize the misfit between the combined spectrum and the target $Sa^*(T_n)$ over the period mesh $\{T_1, \ldots, T_n\}$. In frequency-domain implementations, this linear superposition is performed after Fourier transformation of each accelerogram, and the composite acceleration time history is reconstructed by inverse transformation [@Ref004]. This formulation preserves the non-stationary amplitude and phase characteristics inherent in the original records and avoids the creation of artificial strong-motion cycles. The determination of $\mathbf{w}$ reduces naturally to a constrained or unconstrained regression problem, which is the subject of the formulations developed in SLOTS 3 through 7.



Optimization-based record selection generalizes the weight-determination problem by embedding it within a broader framework that may include combinatorial search over the candidate pool, multi-objective criteria, and physical or code-based constraints on individual scale factors. Genetic algorithms have been applied to identify subsets of records and weighting coefficients that simultaneously satisfy acceleration spectrum targets and energy-equivalent velocity spectrum targets, thus accounting for duration and energy content alongside spectral shape [@Ref004]. These metaheuristic methods are computationally intensive but naturally generalize to objectives that are difficult to formalize within simple least-squares regression, making them attractive when spectral shape conformity must be balanced against other ground motion characteristics.



Conditional mean spectrum selection, formalized by Baker and Cornell, is probabilistically motivated and operates by determining a physically realistic target spectral shape rather than by modifying the spectral content of candidate records [@Ref005]. The CMS conditions on the spectral acceleration $Sa(T^*)$ at a single controlling period $T^*$ and derives the expected spectral shape at all other periods through empirical inter-period correlations, explicitly accounting for the parameter $\varepsilon$ - the normalized deviation of the observed $\ln Sa(T^*)$ from the median prediction of a ground motion model [@Ref006]. Because the uniform hazard spectrum simultaneously imposes rare spectral amplitudes from multiple seismic sources, the CMS produces a less conservative and more physically consistent spectral shape for structural performance assessment [@Ref007]. The CMS is entirely compatible with the linear combination framework: the CMS-derived target constitutes the reference vector $\mathbf{y}$ in the regression formulations of subsequent slots.



## SLOT 2: Minimum Number of Records and Normative Origins of the 7- and 11-Record Requirements

The minimum number of ground motion records required for nonlinear response history analysis has been subject to successive revision in successive editions of ASCE/SEI 7 as the statistical basis for the requirement has become better understood. ASCE/SEI 7-10 establishes an absolute floor of three pairs of horizontal acceleration components for nonlinear time-history analysis under Chapter 16. Three records, however, carry a strong statistical penalty: because the sample size is too small to estimate the mean response reliably, ASCE/SEI 7-10 requires that the design value of each engineering demand parameter (EDP) be taken as the maximum value observed across the three analyses rather than the mean [@Ref002]. This maximum-value rule introduces an implicit conservatism that compensates, in a largely empirical fashion, for the large sampling uncertainty associated with very small suites.



The 7-record threshold represents the specific sample size at which ASCE/SEI 7-10 permits the analyst to substitute the mean EDP for the maximum EDP. When at least seven ground motions are analyzed, the design values of EDPs are taken as the average of the values determined from the suite, resulting in a less conservative and more statistically grounded design basis [@Ref002]. The normative text of ASCE/SEI 7-10 does not provide an explicit mathematical derivation for the choice of 7; Reyes and Kalkan document that the limiting values in the ASCE/SEI-7 scaling procedure are "based on engineering experience" rather than on a formal statistical analysis at the time of their adoption [@Ref008]. The 7-record rule thus originated as a practitioner consensus, reflecting accumulated experience with the variability observed in structural response when modest suites of records are used.



The statistical rationale for the 7-record threshold was subsequently validated by Reyes and Kalkan through a systematic numerical study published in Earthquake Spectra (volume 28, number 3). Applying the ASCE/SEI-7 scaling procedure to 480 sets of ground motions with suite sizes ranging from 3 to 10 records, they demonstrated that the procedure is conservative when fewer than 7 ground motions are used, and that using 7 or more randomly selected records that satisfy the scaling criteria provides dependable estimates of structural responses relative to benchmark values [@Ref008]. The study also found that selecting records on the basis of spectral shape and conformity with the design spectral acceleration at the fundamental period increases both the accuracy and the efficiency of the procedure, meaning that a well-selected suite of 7 records provides greater statistical stability than a randomly assembled suite of the same size.



ASCE/SEI 7-16 and its successor ASCE/SEI 7-22 introduced a more demanding minimum of 11 pairs of horizontal ground motion records for nonlinear response history analysis at the maximum considered earthquake risk (MCER) hazard level [@Ref009]. The elevation from 7 to 11 reflects the stricter performance objectives associated with MCER-level analysis, where the statistical uncertainty in the estimated mean response must be sufficiently small to support code-compliant design decisions at the collapse prevention performance objective. With 11 records, the coefficient of variation of the sample mean is further reduced relative to the 7-record case, providing a more reliable estimate of the average structural demand under a rare intensity level. ASCE/SEI 7-22 additionally modifies the target spectrum from the two-period MCER spectrum used in earlier editions to the multi-period MCER spectrum, and adjusts the scaling period range to extend from the superstructure first-mode period to $1.25$ times the effective period, further tightening the spectral conformity requirements [@Ref009].



From a statistical perspective, the progression from 3 to 7 to 11 records reflects the trade-off between the cost of acquiring and analyzing additional records and the reliability of the resulting structural demand estimate. The sample mean of $r$ independent and identically distributed response values has a standard error proportional to $\sigma / \sqrt{r}$, where $\sigma$ is the record-to-record standard deviation of the response. Increasing the suite size from 3 to 7 records reduces the standard error of the mean by a factor of approximately $\sqrt{3/7} \approx 0.65$; increasing from 7 to 11 achieves a further reduction by a factor of approximately $\sqrt{7/11} \approx 0.80$ [@Ref008]. Within the linear combination methodology, the minimum record requirements serve as a lower bound on the size of the candidate pool $K$; sufficient diversity among the $K$ spectra is necessary to span the range of spectral shapes encountered in the target period range, ensuring that the regression system is not ill-conditioned.



## SLOT 3: Classical Linear Regression Formulation for Spectral Matching Weights

The spectral matching problem admits a direct formulation as a classical linear regression. Given $K$ candidate spectra with spectral ordinates $Sa_k(T_i)$ for $k = 1, \ldots, K$ and $i = 1, \ldots, n$, the target spectrum is represented by the vector $\mathbf{y} \in \mathbb{R}^n$ with components $y_i = \ln Sa^{\mathrm{obj}}(T_i)$ as established in the BACKGROUND notation. The design matrix $\mathbf{A} \in \mathbb{R}^{n \times K}$ is assembled by taking the spectral ordinates of the candidate records as columns:

$$A_{ik} = Sa_k(T_i), \quad i = 1, \ldots, n, \quad k = 1, \ldots, K.$$

The linear model then seeks a weight vector $\mathbf{w} \in \mathbb{R}^K$ such that the weighted combination $\mathbf{A}\mathbf{w}$ approximates the target $\mathbf{y}$, and the global root-mean-square error is minimized over all $n$ spectral ordinates.

The global RMSE objective is defined as:

$$\mathrm{RMSE}(\mathbf{w}) = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left(\sum_{k=1}^{K} w_k Sa_k(T_i) - y_i\right)^2} = \sqrt{\frac{1}{n} \|\mathbf{A}\mathbf{w} - \mathbf{y}\|_2^2}.$$

Minimizing $\mathrm{RMSE}(\mathbf{w})$ is equivalent to minimizing the sum of squared residuals $\|\mathbf{A}\mathbf{w} - \mathbf{y}\|_2^2$, since the factor $1/n$ is constant with respect to $\mathbf{w}$. The OLS problem is therefore:

$$\min_{\mathbf{w} \in \mathbb{R}^K} \|\mathbf{A}\mathbf{w} - \mathbf{y}\|_2^2.$$

This is a convex quadratic program in $\mathbf{w}$ with no constraints, and the global minimum is attained at any solution to the normal equations $\mathbf{A}^\top \mathbf{A} \hat{\mathbf{w}} = \mathbf{A}^\top \mathbf{y}$.

When the design matrix $\mathbf{A}$ has full column rank - equivalently, when the $K$ candidate spectral vectors are linearly independent over the $n$ period points - the matrix $\mathbf{A}^\top \mathbf{A} \in \mathbb{R}^{K \times K}$ is positive definite and invertible, and the unique OLS solution is:

$$\hat{\mathbf{w}} = (\mathbf{A}^\top \mathbf{A})^{-1} \mathbf{A}^\top \mathbf{y}.$$

In practice, when the number of candidate records $K$ is large relative to the number of spectral periods $n$, or when two or more candidate spectra are nearly collinear, $\mathbf{A}^\top \mathbf{A}$ may be numerically rank-deficient or ill-conditioned, rendering the direct inversion unstable. In these situations, the minimum-norm least-squares solution obtained via the Moore-Penrose pseudoinverse $\mathbf{A}^+ = (\mathbf{A}^\top \mathbf{A})^+ \mathbf{A}^\top$ provides a unique and numerically stable generalization. The unconstrained OLS solution does not restrict the signs of the weights $w_k$, so individual weights may be negative; this is addressed in SLOTS 5 and 6 through constrained formulations.



## SLOT 4: Log-Log Space Reformulation of the Regression Problem

The classical formulation of SLOT 3 constructs the design matrix using raw spectral acceleration ordinates $Sa_k(T_i)$, which typically span several orders of magnitude across the period range of engineering interest (commonly $0.05\ \mathrm{s}$ to $10\ \mathrm{s}$). Spectral acceleration values in this range may vary by two to three orders of magnitude, so columns of $\mathbf{A}$ corresponding to short-period and long-period ordinates differ dramatically in scale. Response spectra are, however, well known to exhibit substantially smoother and more nearly linear behavior when plotted in the $\log(Sa)$-$\log(T)$ coordinate system, as the power-law decay of spectral amplitude with period produces approximately linear trends on log-log axes [@Ref001]. This motivates a reformulation in which both the spectral ordinates and the period axis are represented in their logarithmic forms.



The log-log reformulation replaces each column of the design matrix with its logarithm. Define the modified design matrix $\mathbf{X} \in \mathbb{R}^{n \times K}$ by:

$$X_{ik} = \ln Sa_k(T_i), \quad i = 1, \ldots, n, \quad k = 1, \ldots, K.$$

The target vector $\mathbf{y} \in \mathbb{R}^n$ retains its BACKGROUND definition $y_i = \ln Sa^{\mathrm{obj}}(T_i)$, so both the predictors and the response are now expressed in the $\ln Sa$ domain evaluated on the period mesh $\{T_1, \ldots, T_n\}$. The full log-log character is established by the convention that the period mesh itself is chosen as a log-uniformly spaced grid, meaning the abscissa values $\{\ln T_1, \ldots, \ln T_n\}$ are equally spaced; this ensures that the regression assigns equal weight to each decade of the period range rather than concentrating influence on the denser clusters of a linearly spaced grid.

The log-log OLS problem takes the same structural form as the classical formulation but now operates entirely within the logarithmic coordinate system:

$$\min_{\mathbf{w} \in \mathbb{R}^K} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2.$$

The normal equations become $\mathbf{X}^\top \mathbf{X} \hat{\mathbf{w}} = \mathbf{X}^\top \mathbf{y}$, and under full column rank of $\mathbf{X}$ the closed-form solution is:

$$\hat{\mathbf{w}} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y}.$$

The matrix $\mathbf{X}^\top \mathbf{X}$ is generally better conditioned than $\mathbf{A}^\top \mathbf{A}$ because the log transformation compresses the dynamic range of spectral ordinates: entries that differed by orders of magnitude in $\mathbf{A}$ differ by at most a few natural-log units in $\mathbf{X}$, reducing the spread of singular values and improving numerical stability.

In the log-log representation, the product $\mathbf{X}\mathbf{w}$ represents the vector with components $\sum_k w_k \ln Sa_k(T_i)$. Exponentiating the fitted value at period $T_i$ gives:

$$\widehat{Sa^*}(T_i) = \exp\left(\sum_{k=1}^K w_k \ln Sa_k(T_i)\right) = \prod_{k=1}^K Sa_k(T_i)^{w_k},$$

which is a geometric weighted mean of the candidate spectral ordinates at each period. This interpretation is physically natural: in the log domain, the combined spectrum is a power-weighted geometric combination of the individual spectra, and each weight $w_k$ controls the fractional influence of record $k$ in the logarithmic sense. When the weights are constrained to be non-negative and to sum to unity, the geometric mean collapses to a conventional mixture, making the log-log formulation the algebraically natural basis for the constrained extensions developed in SLOTS 5 through 7.



## SLOT 5: Non-Negative Least Squares Extension and Ridge Regression with Positivity Constraints

In the unconstrained OLS solutions of SLOTS 3 and 4, the weight vector $\hat{\mathbf{w}}$ may contain negative components. Negative weights $w_k$ imply that the contribution of record $k$ acts to subtract spectral content from the combined spectrum, which lacks a direct physical counterpart when the ensemble is interpreted as a convex combination of ground motion records. In settings where the practitioner requires $w_k \geq 0$ for all $k$ - either because the weights represent record probabilities, mixing proportions, or because negative contributions are considered physically inadmissible - the unconstrained solution must be replaced by a non-negative least squares formulation.



The non-negative least squares (NNLS) problem extends the log-log OLS formulation of SLOT 4 by imposing the constraint that each component of $\mathbf{w}$ is non-negative:

$$\min_{\mathbf{w} \in \mathbb{R}^K} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad w_k \geq 0, \quad k = 1, \ldots, K.$$

This problem is a convex quadratic program with linear inequality constraints. No closed-form solution exists in general; the optimal weights are found by iterative active-set methods. The seminal algorithm for NNLS was published by Lawson and Hanson in 1974 and implements an active-set strategy in which the solver maintains a partition of the index set $\{1, \ldots, K\}$ into a passive set (indices with $w_k > 0$) and an active set (indices with $w_k = 0$), iteratively expanding or contracting the passive set until the Karush-Kuhn-Tucker optimality conditions are satisfied [@Ref010]. The Lawson-Hanson algorithm is the canonical reference implementation and is available in the R `nnls` package.



Standard ridge regression does not enforce non-negativity of the coefficient vector. Ridge regression modifies the OLS objective by adding an $\ell_2$ penalty on the weight magnitudes with regularization parameter $\lambda > 0$:

$$\min_{\mathbf{w} \in \mathbb{R}^K} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda \|\mathbf{w}\|_2^2.$$

This unconstrained problem has the closed-form solution:

$$\hat{\mathbf{w}}_{\mathrm{ridge}} = (\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^\top \mathbf{y}.$$

The ridge penalty shrinks all components of $\hat{\mathbf{w}}$ toward zero by adding $\lambda$ to the diagonal of the Hessian, improving conditioning and controlling overfitting when $K$ is large or $\mathbf{X}^\top \mathbf{X}$ is ill-conditioned. However, because the ridge solution is the unconstrained minimizer of an objective with no sign restrictions, individual components $\hat{w}_k$ remain free to take negative values. Ridge regression alone therefore cannot serve as a mechanism for enforcing positivity; an additional non-negativity constraint must be imposed separately, converting the problem from an unconstrained ridge problem to a constrained quadratic program that can no longer be solved by the closed-form ridge formula.



The following R implementation uses the `nnls` package to solve the NNLS problem in log-log space. The matrix `X` has $n$ rows and $K$ columns with entries `X[i,k] = log(Sa_k(T_i))`, and the vector `y` has $n$ entries with `y[i] = log(Sa_obj(T_i))`.

```r
library(nnls)

# Inputs:
#   X : n x K design matrix, X[i,k] = log(Sa_k(T_i))
#   y : n-vector, y[i]   = log(Sa_obj(T_i))

fit_nnls <- nnls(A = X, b = y)
w_hat    <- fit_nnls$x          # K-vector of non-negative weights
residuals <- fit_nnls$residuals # n-vector of fitted residuals

# Reconstruct the fitted log-spectrum and verify non-negativity
log_Sa_fitted <- X %*% w_hat
stopifnot(all(w_hat >= -1e-10)) # tolerance for numerical zero
```



## SLOT 6: Box-Constrained Weights and Applicability of Ridge/Lasso Regularization

In many practical applications, an analyst may wish to impose not only a lower bound $w_{\min} \geq 0$ on each weight but also an upper bound $w_{\max}$. An upper bound prevents any single record from dominating the combined spectrum, enforcing a diversification requirement analogous to portfolio allocation constraints. The box-constrained least squares problem generalizes the NNLS formulation by replacing the simple non-negativity constraint with bilateral bounds:

$$\min_{\mathbf{w} \in \mathbb{R}^K} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad w_{\min} \leq w_k \leq w_{\max}, \quad k = 1, \ldots, K.$$

This is again a strictly convex quadratic program, and its solution exists and is unique provided $w_{\min} < w_{\max}$ and $K \leq n$. The feasible set is a $K$-dimensional box (hypercube), and the optimum may lie at an interior point, on a face, or at a vertex of that box, depending on the unconstrained OLS solution and the width of the interval $[w_{\min}, w_{\max}]$.



Standard ridge regression, as established in SLOT 5, produces coefficients that may be negative and unbounded from above; it addresses neither a lower bound nor an upper bound on individual weights. Lasso regression, which replaces the $\ell_2$ penalty with an $\ell_1$ penalty $\lambda \|\mathbf{w}\|_1$, similarly operates without sign or magnitude constraints on individual coefficients: it shrinks some components to exactly zero (sparse solutions) but does not prevent the remaining components from being negative or from exceeding $w_{\max}$ [@Ref011]. Neither standard ridge nor standard lasso can therefore enforce box constraints $[w_{\min}, w_{\max}]$ directly. Enforcing such constraints requires either a dedicated bounded-variable least squares algorithm or a general convex optimizer.



Two principal algorithmic strategies are available in R for box-constrained least squares. The first uses the Stark-Parker bounded-variable least squares (BVLS) algorithm, available through the R `bvls` package, which generalizes the Lawson-Hanson active-set strategy to accommodate both lower and upper bounds simultaneously [@Ref012]. The second reformulates the problem as a quadratic program and solves it with the `quadprog` package. In the `quadprog` convention, the objective $\|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 = \mathbf{w}^\top (\mathbf{X}^\top \mathbf{X}) \mathbf{w} - 2 (\mathbf{X}^\top \mathbf{y})^\top \mathbf{w} + \mathbf{y}^\top \mathbf{y}$ is cast in the form $\frac{1}{2} \mathbf{w}^\top \mathbf{D} \mathbf{w} - \mathbf{d}^\top \mathbf{w}$, where $\mathbf{D} = 2 \mathbf{X}^\top \mathbf{X}$ and $\mathbf{d} = 2 \mathbf{X}^\top \mathbf{y}$, and the box constraints are encoded as a set of $2K$ linear inequality constraints.



The following R code implements the box-constrained problem using the `bvls` package and separately using `quadprog`, with both formulations producing equivalent solutions.

```r
# --- Method 1: BVLS (bounded-variable least squares) ---
library(bvls)

# Inputs:
#   X      : n x K design matrix (log-log space)
#   y      : n-vector of log target values
#   w_min  : scalar lower bound (e.g. 0)
#   w_max  : scalar upper bound (e.g. 1)

K       <- ncol(X)
w_lower <- rep(w_min, K)
w_upper <- rep(w_max, K)

fit_bvls <- bvls(A = X, b = y, bl = w_lower, bu = w_upper)
w_hat    <- fit_bvls$x


# --- Method 2: quadprog ---
library(quadprog)

Dmat <- 2 * t(X) %*% X   # K x K positive definite matrix
dvec <- 2 * t(X) %*% y   # K-vector

# Constraint matrix: w >= w_min (first K columns) and -w >= -w_max (next K)
Amat <- cbind(diag(K), -diag(K))   # K x 2K
bvec <- c(rep(w_min, K), rep(-w_max, K))  # 2K-vector

result <- solve.QP(Dmat = Dmat, dvec = dvec, Amat = Amat, bvec = bvec)
w_hat  <- result$solution
```



## SLOT 7: Convex Optimization Generalization and R Implementation

The formulations of SLOTS 3 through 6 are all special cases of a single convex optimization problem. The general framework accommodates the RMSE criterion, non-negativity constraints, box constraints, and optional $\ell_2$ (ridge) or $\ell_1$ (lasso) regularization within a unified objective, parameterized by the bounds $w_{\min}$ and $w_{\max}$ and the regularization coefficients $\lambda_2$ and $\lambda_1$:

$$\min_{\mathbf{w} \in \mathbb{R}^K} \;\; \frac{1}{n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda_2 \|\mathbf{w}\|_2^2 + \lambda_1 \|\mathbf{w}\|_1 \quad \text{subject to} \quad w_{\min} \leq w_k \leq w_{\max}, \quad k = 1, \ldots, K.$$

Setting $\lambda_2 = \lambda_1 = 0$ and $w_{\min} = -\infty$, $w_{\max} = +\infty$ recovers the unconstrained OLS of SLOT 4; setting $\lambda_2 = \lambda_1 = 0$ and $w_{\min} = 0$, $w_{\max} = +\infty$ recovers the NNLS of SLOT 5; setting $w_{\min} > 0$ or finite $w_{\max}$ recovers the box-constrained problem of SLOT 6. In all cases the objective is a sum of convex terms and the feasible set is a convex polytope, so the problem is convex and any local minimum is global [@Ref013].



The `CVXR` package for R implements disciplined convex programming (DCP), a compositional rule system that verifies the convexity of user-specified objective functions and constraints before passing the canonicalized problem to a cone solver such as CLARABEL, SCS, or OSQP [@Ref013][@Ref014]. The user expresses the optimization problem in a syntax that mirrors the mathematical formulation directly, through the functions `Variable()`, `Minimize()`, `Problem()`, and `solve()`. Constraints are added as a list appended to the `Problem` constructor, and arbitrary combinations of $\ell_1$, $\ell_2$, and mixed penalties are specified through the `norm()`, `sum_squares()`, and `abs()` atoms defined by the DCP library. The `sum_squares(v)` atom computes $\|\mathbf{v}\|_2^2$ and is recognized as convex by the DCP checker, making it the natural choice for the RMSE criterion.



The following R implementation uses CVXR to solve the general convex spectral matching problem. Parameters $\lambda_2$, $\lambda_1$, $w_{\min}$, and $w_{\max}$ are exposed as arguments, allowing the code to reproduce any of the formulations from SLOTS 3 through 6 by setting the appropriate parameter values.

```r
library(CVXR)

# Inputs:
#   X        : n x K design matrix (log-log space), X[i,k] = log(Sa_k(T_i))
#   y        : n-vector, y[i] = log(Sa_obj(T_i))
#   lambda2  : ridge penalty coefficient  (set 0 for no ridge)
#   lambda1  : lasso penalty coefficient  (set 0 for no lasso)
#   w_min    : scalar lower bound  (set -Inf for unconstrained below)
#   w_max    : scalar upper bound  (set  Inf for unconstrained above)

spectral_match_cvxr <- function(X, y, lambda2 = 0, lambda1 = 0,
                                 w_min = 0, w_max = Inf) {
  K   <- ncol(X)
  n   <- nrow(X)
  w   <- Variable(K)

  # Objective: RMSE criterion plus optional regularization
  loss      <- (1 / n) * sum_squares(X %*% w - y)
  ridge_pen <- lambda2 * sum_squares(w)
  lasso_pen <- lambda1 * sum(abs(w))
  objective <- Minimize(loss + ridge_pen + lasso_pen)

  # Box constraints (drop if w_min = -Inf or w_max = Inf)
  constraints <- list()
  if (is.finite(w_min)) constraints <- c(constraints, list(w >= w_min))
  if (is.finite(w_max)) constraints <- c(constraints, list(w <= w_max))

  prob   <- Problem(objective, constraints)
  result <- solve(prob, solver = "CLARABEL")

  list(
    weights  = result$getValue(w),
    status   = result$status,
    obj_val  = result$value
  )
}

# --- Usage examples ---

# SLOT 4 equivalent: unconstrained OLS in log-log space
fit_ols  <- spectral_match_cvxr(X, y, lambda2=0, lambda1=0, w_min=-Inf, w_max=Inf)

# SLOT 5 equivalent: NNLS (non-negative weights)
fit_nnls <- spectral_match_cvxr(X, y, lambda2=0, lambda1=0, w_min=0, w_max=Inf)

# SLOT 6 equivalent: box-constrained (e.g. 0 <= w_k <= 0.5)
fit_box  <- spectral_match_cvxr(X, y, lambda2=0, lambda1=0, w_min=0, w_max=0.5)

# General: box-constrained with ridge regularization
fit_reg  <- spectral_match_cvxr(X, y, lambda2=0.01, lambda1=0, w_min=0, w_max=0.5)
```



The unified convex program subsumes all formulations in this document and retains strict convexity for any $\lambda_2 > 0$ or for any bounded feasible set, guaranteeing a unique global minimum. When $\lambda_2 = 0$ and the box is absent (unconstrained OLS), the problem degenerates to the normal equations of SLOT 4, and the CVXR solver will return the minimum-norm solution when $\mathbf{X}^\top \mathbf{X}$ is singular. The $\ell_1$ penalty ($\lambda_1 > 0$) induces sparsity in $\mathbf{w}$, automatically selecting a subset of the $K$ candidate records that suffices to approximate the target spectrum; this is particularly useful when $K$ is large and an analyst wishes to identify the smallest effective subset without a separate combinatorial search. The combination $\lambda_2 > 0$, $\lambda_1 > 0$ with $0 \leq w_{\min} < w_{\max}$ represents the most general regularized, box-constrained elastic net formulation, and all parameters can be tuned jointly by cross-validation over a grid of period-range subsets or by leave-one-record-out schemes adapted to the seismic record selection context [@Ref013][@Ref014].


