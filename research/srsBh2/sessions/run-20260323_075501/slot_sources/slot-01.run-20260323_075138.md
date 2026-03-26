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

