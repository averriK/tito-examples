# Weight Calibration in Epistemic Logic Trees: Sum-to-One Constraint Formulation and Validation

## SLOT 1: Extend weight formulation with sum-to-1 constraint

The spectral-matching problem for epistemic logic trees in probabilistic seismic hazard analysis requires assigning a weight $w_k$ to each of $K$ candidate ground-motion prediction equations or records such that their weighted linear combination approximates a PSHA-derived target spectrum. [KB:spec.compile.research.md] The baseline formulation seeks to minimize the root-mean-square error between the weighted combination and the target across a discretized period mesh. [KB:spec.compile.research.md] To incorporate the constraint that weights must sum to unity---a requirement that enforces that the combined suite is a normalized probability distribution over the candidate records---the optimization problem is extended to include an affine constraint $\sum_{k=1}^{K} w_k = 1$ alongside the existing non-negativity requirement $w_k > 0$ for all $k$. [WEB:https://www.stata.com/manuals13/rcnsreg.pdf][WEB:https://www.mathworks.com/matlabcentral/answers/113709-multiple-linear-regression-with-constraint]
^[Confidence: HIGH, Rationale: The KB provides the baseline weight formulation and regression objective. The affine constraint sum-to-one is standard in portfolio optimization and constrained regression, well-documented in statistical software manuals (Stata, MATLAB) and educational resources for constrained least squares.]

The extended constrained least-squares formulation is:

$$\min_{\mathbf{w} \in \mathbb{R}^K} \; \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad \sum_{k=1}^{K} w_k = 1, \quad w_k > 0 \; \text{for all} \; k = 1, \dots, K,$$

where $\tilde{\mathbf{A}} \in \mathbb{R}^{n \times K}$ is the log-transformed design matrix with entries $\tilde{A}_{ik} = \ln S_{a,k}(T_i)$, $\mathbf{y} \in \mathbb{R}^n$ is the log-domain target vector with components $y_i = \ln S_a^{\mathrm{obj}}(T_i)$, and the constraint set defines a standard probability simplex (the intersection of the unit hyperplane with the positive orthant). [KB:spec.compile.research.md]
^[Confidence: HIGH, Rationale: This formulation directly extends the KB's unconstrained NNLS problem (SLOT 5) by adding the affine equality constraint. The notation and structure are consistent with the KB's established mathematical framework for spectral-matching regression.]

The Lagrange multiplier method provides a natural framework for solving this affine-constrained problem. [WEB:https://jonathan-hui.medium.com/machine-learning-lagrange-multiplier-dual-decomposition-4afe66158c9][WEB:https://math.libretexts.org/Bookshelves/Calculus/Vector_Calculus_(Corral)/02:_Functions_of_Several_Variables/2.07:_Constrained_Optimization_-_Lagrange_Multipliers] Introduce a Lagrange multiplier $\lambda \in \mathbb{R}$ associated with the equality constraint and form the Lagrangian:

$$\mathcal{L}(\mathbf{w}, \lambda) = \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda \left(\sum_{k=1}^{K} w_k - 1\right) = \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda (\mathbf{1}^\top \mathbf{w} - 1),$$

where $\mathbf{1}$ denotes the $K$-vector of ones. [WEB:https://math.libretexts.org/Bookshelves/Calculus/Vector_Calculus_(Corral)/02:_Functions_of_Several_Variables/2.07:_Constrained_Optimization_-_Lagrange_Multipliers]
^[Confidence: HIGH, Rationale: The Lagrangian formulation is standard in constrained optimization and directly applies the method of Lagrange multipliers to affine equality constraints. External sources confirm this is the canonical approach for such problems.]

Setting the gradient with respect to $\mathbf{w}$ equal to zero yields the first-order optimality condition:

$$\nabla_{\mathbf{w}} \mathcal{L} = 2\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}) + \lambda \mathbf{1} = \mathbf{0}.$$

Rearranging:

$$2\tilde{\mathbf{A}}^\top \tilde{\mathbf{A}}\, \mathbf{w} + \lambda \mathbf{1} = 2\tilde{\mathbf{A}}^\top \mathbf{y}.$$

This is a system of $K$ linear equations in $K+1$ unknowns ($\mathbf{w}$ and $\lambda$). Combined with the constraint $\sum_{k=1}^{K} w_k = 1$, the system becomes:

$$\begin{pmatrix} 2\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}} & \mathbf{1} \\ \mathbf{1}^\top & 0 \end{pmatrix} \begin{pmatrix} \mathbf{w} \\ \lambda \end{pmatrix} = \begin{pmatrix} 2\tilde{\mathbf{A}}^\top\mathbf{y} \\ 1 \end{pmatrix}.$$

This is a $(K+1) \times (K+1)$ augmented system that can be solved directly via Gaussian elimination or, if additional inequality constraints (such as $w_k \geq w_{\min} > 0$) are required, through quadratic programming solvers. [WEB:https://www.stata.com/manuals13/rcnsreg.pdf][WEB:https://www.excelforum.com/excel-general/1171141-options-to-do-multiple-linear-regression-with-constraints-coefficients-0-and-sum-1-a.html]
^[Confidence: HIGH, Rationale: The augmented system arises directly from the method of Lagrange multipliers. The matrix formulation is standard in constrained least-squares theory and confirmed in applied statistical software documentation (Stata, Excel Solver) that handles exactly this problem structure.]

An alternative parametrization avoids the need for an explicit Lagrange multiplier by substituting the constraint directly. Setting $w_K = 1 - \sum_{k=1}^{K-1} w_k$, the problem reduces to an unconstrained least-squares problem in the $(K-1)$ variables $(w_1, \dots, w_{K-1})$: [WEB:https://www.mathworks.com/matlabcentral/answers/113709-multiple-linear-regression-with-constraint][WEB:https://imyashhere.medium.com/linear-regression-with-added-constraints-on-coefficients-cca7d843d26c]

$$\min_{w_1, \dots, w_{K-1}} \; \left\| \tilde{\mathbf{A}}_{:,1:K-1} \begin{pmatrix} w_1 \\ \vdots \\ w_{K-1} \end{pmatrix} + \tilde{\mathbf{A}}_{:,K}(1 - \sum_{k=1}^{K-1} w_k) - \mathbf{y} \right\|_2^2.$$

This reformulation is equivalent to the Lagrange multiplier approach but offers computational simplicity when only the sum-to-one constraint is present. [WEB:https://imyashhere.medium.com/linear-regression-with-added-constraints-on-coefficients-cca7d843d26c]
^[Confidence: HIGH, Rationale: The reparameterization is a standard technique in constrained optimization and reduces the problem to a standard OLS in lower dimensions. This is confirmed by discussion in machine learning and statistical optimization literature.]

Both formulations guarantee a unique solution when $\tilde{\mathbf{A}}$ has full column rank, as the objective function remains strictly convex under the affine constraint. The non-negativity requirement $w_k > 0$ is not enforced by the Lagrangian alone; if strict positivity is required (rather than mere non-negativity), inequality constraints must be included, converting the problem to a constrained quadratic program. [KB:spec.compile.research.md][WEB:https://www.mathworks.com/matlabcentral/answers/113709-multiple-linear-regression-with-constraint]
^[Confidence: HIGH, Rationale: Convexity of the objective and strict positivity requirements are well-established properties. The KB discusses convexity in the context of bounded-weight problems (SLOT 6 and 7), and the external sources confirm that quadratic programming is needed when inequality constraints are added.]

---

## SLOT 2: Validate normalization approach vs. mathematical treatment

A common practical question in weight calibration is whether the sum-to-one constraint can be satisfied through post-hoc normalization of an unconstrained solution, rather than solving the constrained optimization problem directly. Specifically, if an unconstrained least-squares solution $\hat{\mathbf{w}}_{\text{unconstrained}}$ is obtained (e.g., via NNLS or OLS), whether dividing each weight by the sum $\hat{\mathbf{w}}_{\text{normalized}} = \hat{\mathbf{w}}_{\text{unconstrained}} / \sum_k \hat{w}_k$ yields a valid approximation to the true constrained solution requires careful analysis.
^[Confidence: MEDIUM, Rationale: The question of post-hoc normalization is practical and motivated, but the KB does not directly address this comparison. The answer requires theoretical analysis combining unconstrained and constrained formulations.]

The post-hoc normalization approach operates as follows: solve the unconstrained problem $\min_{\mathbf{w}} \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2$ to obtain $\hat{\mathbf{w}}_{\text{unc}}$, then set $\hat{\mathbf{w}}_{\text{norm}} = \hat{\mathbf{w}}_{\text{unc}} / \|\hat{\mathbf{w}}_{\text{unc}}\|_1$ where $\|\cdot\|_1$ is the $\ell^1$ norm (sum of absolute values). By construction, $\sum_k \hat{w}_{\text{norm},k} = 1$. However, this normalized solution is not, in general, the solution to the constrained problem $\min_{\mathbf{w}: \sum w_k = 1} \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2$ because the normalization operation is a nonlinear function that does not preserve the optimality condition $\nabla \mathcal{L}(\mathbf{w}, \lambda) = \mathbf{0}$.
^[Confidence: HIGH, Rationale: The distinction between unconstrained and constrained optimization is fundamental. The post-hoc normalization operates on the solution to a different optimization problem (unconstrained), so it cannot automatically satisfy the first-order conditions of the constrained problem.]

To analyze the error introduced by normalization, consider the unconstrained optimum $\hat{\mathbf{w}}_{\text{unc}}$. If $\sum_k \hat{w}_{\text{unc},k} = 1$ already holds at the unconstrained solution, then normalization has no effect and the two approaches coincide. However, in general $\sum_k \hat{w}_{\text{unc},k} \neq 1$; the unconstrained OLS or NNLS solution is not constrained to lie on the probability simplex. When normalization is applied, the resulting vector $\hat{\mathbf{w}}_{\text{norm}}$ is a scaled version of $\hat{\mathbf{w}}_{\text{unc}}$, lying on the same ray from the origin in weight space. The constrained optimum, by contrast, lies on the affine hyperplane $\sum w_k = 1$ and, in general, does not lie on the same ray as the unconstrained solution.
^[Confidence: HIGH, Rationale: This geometric argument is rigorous. Scaling (normalization) is a linear operation that preserves rays from the origin; the constrained optimum lies on an affine hyperplane and only coincidentally lies on the same ray.]

The key theoretical difference is that the constrained problem $\min_{\mathbf{w}: \sum w_k = 1} \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2$ involves minimizing the squared error over all points on the simplex, whereas post-hoc normalization rescales a solution obtained by minimizing over the entire space and projects it onto the simplex via a scaling operation. Research on constrained optimization and weight normalization confirms that normalization choices can introduce bias-variance trade-offs and that constrained formulations directly enforce requirements more accurately than post-hoc scaling. [WEB:https://arxiv.org/html/2501.03821v2][WEB:https://academic.oup.com/imaiai/article/13/3/iaae022/7754106]
^[Confidence: MEDIUM, Rationale: The KB does not directly compare constrained vs post-hoc approaches for the sum-to-one case. The external sources confirm that constraint enforcement directly is preferable to post-hoc normalization, though they address broader regularization and weight normalization contexts.]

From a practical standpoint, there are several reasons to prefer constrained optimization over post-hoc normalization. First, the constrained solution directly minimizes error on the simplex, the feasible region of interest; post-hoc normalization may introduce unnecessary suboptimality because the unconstrained minimum is not on the simplex. Second, when inequality constraints on individual weights (such as $w_k > w_{\min}$) are added alongside the sum-to-one requirement, post-hoc normalization of an unconstrained solution does not account for those inequality constraints and may produce weights outside the feasible region. Third, if the unconstrained solution includes negative weights (which occurs in OLS but is suppressed in NNLS), normalization can produce unexpected behavior: e.g., scaling a vector with mixed signs and then dividing by its $\ell^1$ norm can distort the relative contribution structure intended by the regression. [KB:spec.compile.research.md][WEB:https://www.excelforum.com/excel-general/1171141-options-to-do-multiple-linear-regression-with-constraints-coefficients-0-and-sum-1-a.html]
^[Confidence: HIGH, Rationale: The KB discusses negative weights in the context of NNLS (SLOT 5), confirming that unconstrained OLS admits negative weights. The practical issues with post-hoc normalization follow directly from these observations and are grounded in standard optimization theory.]

A mathematical treatment that applies directly to the spectral-matching context is to recognize that the constrained problem, when solved via the Lagrangian with an affine constraint, yields the condition $2\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}_{\text{const}} - \mathbf{y}) = -\lambda \mathbf{1}$, meaning that at the constrained optimum, the gradient of the loss function is parallel to the constraint normal (pointing in the direction $\mathbf{1}$). In contrast, the unconstrained optimum satisfies $2\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}_{\text{unc}} - \mathbf{y}) = \mathbf{0}$, a fundamentally different condition. Post-hoc normalization of $\mathbf{w}_{\text{unc}}$ does not adjust the residual vector to satisfy this optimality condition; it merely rescales the weights. Thus, normalization cannot recover the constrained solution unless by coincidence the unconstrained solution already satisfies the simplex constraint.
^[Confidence: HIGH, Rationale: This is a direct application of the method of Lagrange multipliers. The optimality conditions for constrained and unconstrained problems are fundamentally different, confirming that post-hoc normalization is not equivalent to constrained optimization.]

In conclusion, while post-hoc normalization is computationally simpler and may provide a practical approximation in some applications, it does not solve the constrained optimization problem and introduces potentially significant suboptimality. For the weight-calibration problem in epistemic logic trees, constrained optimization via Lagrange multipliers (or equivalent quadratic programming formulations) is the theoretically sound and practically preferable approach. [WEB:https://arxiv.org/html/2501.03821v2][WEB:https://www.mathworks.com/matlabcentral/answers/113709-multiple-linear-regression-with-constraint]
^[Confidence: HIGH, Rationale: This conclusion synthesizes the theoretical analysis (SLOT 1 formulation) with practical considerations and is supported by external research emphasizing that constrained formulations are superior to post-hoc normalization, combined with the KB's foundation on optimization principles.]

---

## References

The following sources were consulted in preparing this research document:

- **Knowledge Base:** spec.compile.research.md provides the foundational linear regression and constrained optimization framework for spectral-matching weight calibration, including NNLS and bounded-weight formulations.

- **Web Sources:**
  - Constrained Linear Regression Documentation: https://www.stata.com/manuals13/rcnsreg.pdf
  - MATLAB Constrained Regression: https://www.mathworks.com/matlabcentral/answers/113709-multiple-linear-regression-with-constraint
  - Lagrange Multipliers in Machine Learning: https://jonathan-hui.medium.com/machine-learning-lagrange-multiplier-dual-decomposition-4afe66158c9
  - Calculus III Constrained Optimization: https://math.libretexts.org/Bookshelves/Calculus/Vector_Calculus_(Corral)/02:_Functions_of_Several_Variables/2.07:_Constrained_Optimization_-_Lagrange_Multipliers
  - Excel Forum on Constrained Regression: https://www.excelforum.com/excel-general/1171141-options-to-do-multiple-linear-regression-with-constraints-coefficients-0-and-sum-1-a.html
  - Linear Regression with Constraints (Medium): https://imyashhere.medium.com/linear-regression-with-added-constraints-on-coefficients-cca7d843d26c
  - Normalization in Regularized Regression (ArXiv): https://arxiv.org/html/2501.03821v2
  - Implicit Regularization via Weight Normalization (Oxford Academic): https://academic.oup.com/imaiai/article/13/3/iaae022/7754106
