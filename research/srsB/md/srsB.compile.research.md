# Weight Calibration under the Unit-Sum Constraint: Constrained Optimization Formulation and Validity of Post-Hoc Normalization

This document addresses two questions arising from the non-negative least-squares (NNLS) weight-calibration framework in the knowledge base. The first concerns the formal extension of that framework to the unit-sum equality constraint required by the probabilistic seismic hazard analysis (PSHA) logic tree. The second concerns whether the unit-sum weights can be obtained by solving the unconstrained NNLS problem and then dividing each component by the total, or whether the equality constraint requires a fundamentally different treatment.

---

## SLOT 1: Extension of error minimization formulation to the unit-sum weight constraint

### Baseline Non-Negative Least-Squares Formulation

The knowledge base formulates the weight-calibration problem as a non-negative least-squares (NNLS) minimization in the log-spectral domain. Let $\tilde{\mathbf{A}} \in \mathbb{R}^{n \times K}$ denote the log-transformed design matrix with entries $\tilde{A}_{ik} = \ln S_{a,k}(T_i)$, where $S_{a,k}(T_i)$ is the pseudo-spectral acceleration predicted by the $k$-th candidate ground-motion model (GMM) at spectral period $T_i$, for $i = 1, \dots, n$ period ordinates and $k = 1, \dots, K$ candidate models. The target vector $\mathbf{y} \in \mathbb{R}^n$ has components $y_i = \ln S_a^{\mathrm{obj}}(T_i)$. The weight vector $\mathbf{w} = (w_1, \dots, w_K)^\top$ is determined by solving the NNLS problem [@SpecCompileResearch]:

$$\min_{\mathbf{w} \in \mathbb{R}^K} \;\|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad w_k \geq 0, \quad k = 1, \dots, K.$$

The feasible region is the non-negative orthant $\mathbb{R}_{\geq 0}^K$, an unbounded closed convex cone. Setting $\mathbf{Q} = \tilde{\mathbf{A}}^\top\tilde{\mathbf{A}} \in \mathbb{R}^{K \times K}$ (the Gram matrix) and $\mathbf{c} = \tilde{\mathbf{A}}^\top\mathbf{y} \in \mathbb{R}^K$ (the cross-correlation vector), the objective expands as $\mathbf{w}^\top\mathbf{Q}\mathbf{w} - 2\mathbf{c}^\top\mathbf{w} + \|\mathbf{y}\|_2^2$. When $\tilde{\mathbf{A}}$ has full column rank---a condition satisfied when $n \geq K$ and no two candidate log-spectral vectors are collinear over the period mesh---$\mathbf{Q}$ is positive definite and the objective is strictly convex, guaranteeing a unique global minimizer. The Lawson-Hanson active-set algorithm solves this problem by maintaining a partition of the index set $\{1, \dots, K\}$ into a passive set $\mathcal{P} = \{k : w_k > 0\}$ and an active set $\mathcal{Z} = \{k : w_k = 0\}$, iteratively updating the partition until the Karush-Kuhn-Tucker (KKT) conditions are satisfied [@SpecCompileResearch][@LawsonHanson1974][@WikipediaNNLS].

The KKT stationarity conditions at the NNLS solution $\hat{\mathbf{w}}^{\mathrm{NNLS}}$ require:

$$\bigl[\mathbf{Q}\hat{\mathbf{w}}^{\mathrm{NNLS}} - \mathbf{c}\bigr]_k = 0 \quad \text{for all } k \in \mathcal{P}, \qquad \bigl[\mathbf{Q}\hat{\mathbf{w}}^{\mathrm{NNLS}} - \mathbf{c}\bigr]_k \geq 0 \quad \text{for all } k \in \mathcal{Z}.$$

### Unit-Sum Constraint and the Probability Simplex

The epistemic logic-tree framework requires branch weights to form a discrete probability measure over the $K$ candidate GMMs, imposing the equality constraint $\sum_{k=1}^K w_k = 1$, written in vector notation as $\mathbf{1}^\top\mathbf{w} = 1$. Adding this constraint to the NNLS baseline restricts the feasible region from the non-negative orthant $\mathbb{R}_{\geq 0}^K$ to the standard probability simplex [@BoydVandenberghe2004]:

$$\Delta^{K-1} = \left\{\mathbf{w} \in \mathbb{R}^K : \mathbf{1}^\top\mathbf{w} = 1,\; w_k \geq 0 \;\text{for all}\; k = 1, \dots, K\right\}.$$

The simplex $\Delta^{K-1}$ is a compact convex polytope of dimension $K-1$ embedded in $\mathbb{R}^K$: all components lie in $[0, 1]$ and the set is closed. Because $\Delta^{K-1}$ is compact and the objective is continuous, the Weierstrass extreme value theorem guarantees existence of a global minimizer; strict convexity under full column rank of $\tilde{\mathbf{A}}$ ensures uniqueness [@BoydVandenberghe2004][@NocedalWright2006].

### Fully Constrained Optimization Problem

The unit-sum-constrained extension of the KB NNLS formulation is [@SpecCompileResearch]:

$$\min_{\mathbf{w} \in \mathbb{R}^K} \;\|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad \mathbf{1}^\top\mathbf{w} = 1, \quad w_k \geq 0, \quad k = 1, \dots, K. \tag{P}$$

This is a convex quadratic program (QP) with one linear equality constraint and $K$ linear inequality constraints. The only structural modification relative to the NNLS baseline is the addition of the equality constraint $\mathbf{1}^\top\mathbf{w} = 1$; the objective function and the non-negativity constraints are carried over unchanged.

### Standard Quadratic Program Form

Dropping the constant $\|\mathbf{y}\|_2^2$, which does not affect the location of the minimizer, (P) is equivalent to the reduced QP over $\Delta^{K-1}$ [@BoydVandenberghe2004][@NocedalWright2006]:

$$\min_{\mathbf{w} \in \Delta^{K-1}} \;\mathbf{w}^\top\mathbf{Q}\mathbf{w} - 2\mathbf{c}^\top\mathbf{w}.$$

The Gram matrix $\mathbf{Q}$ is positive semidefinite for any $\tilde{\mathbf{A}}$ and positive definite when $\tilde{\mathbf{A}}$ has full column rank. The constraint set consists of one linear equality and $K$ linear inequalities, yielding $K + 1$ constraints in total. This QP is precisely the problem class handled by the Goldfarb-Idnani dual active-set algorithm [@GoldfarbIdnani1983].

### Lagrangian Formulation

The Lagrangian is formed by associating a scalar multiplier $\mu \in \mathbb{R}$, unrestricted in sign, with the equality constraint, and a non-negative multiplier vector $\boldsymbol{\lambda} = (\lambda_1, \dots, \lambda_K)^\top \geq \mathbf{0}$ with the $K$ non-negativity constraints [@BoydVandenberghe2004]:

$$\mathcal{L}(\mathbf{w}, \mu, \boldsymbol{\lambda}) = \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 + \mu\!\left(\mathbf{1}^\top\mathbf{w} - 1\right) - \boldsymbol{\lambda}^\top\mathbf{w}.$$

The gradient of $\mathcal{L}$ with respect to $\mathbf{w}$ is:

$$\nabla_{\mathbf{w}}\mathcal{L}(\mathbf{w}, \mu, \boldsymbol{\lambda}) = 2\tilde{\mathbf{A}}^\top\!\left(\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\right) + \mu\mathbf{1} - \boldsymbol{\lambda} = 2(\mathbf{Q}\mathbf{w} - \mathbf{c}) + \mu\mathbf{1} - \boldsymbol{\lambda}.$$

The Hessian $\nabla_{\mathbf{w}}^2\mathcal{L} = 2\mathbf{Q}$ is independent of $(\mu, \boldsymbol{\lambda})$, confirming convexity of $\mathcal{L}$ in $\mathbf{w}$ for any fixed multiplier values. Slater's constraint qualification holds because any strictly positive weight vector summing to unity---for instance, $\mathbf{w} = K^{-1}\mathbf{1}$---is a strictly feasible interior point of $\Delta^{K-1}$. Under Slater's condition, the KKT conditions are both necessary and sufficient for global optimality [@BoydVandenberghe2004].

### Karush-Kuhn-Tucker Optimality Conditions

At the unique global minimizer $\mathbf{w}^*$ with associated multipliers $(\mu^*, \boldsymbol{\lambda}^*)$, the complete KKT system comprises four groups of conditions [@BoydVandenberghe2004][@NocedalWright2006].

**Stationarity** ($\nabla_{\mathbf{w}}\mathcal{L} = \mathbf{0}$), component-wise for each $k = 1, \dots, K$:

$$2\bigl[\mathbf{Q}\mathbf{w}^* - \mathbf{c}\bigr]_k + \mu^* = \lambda_k^*.$$

**Primal feasibility:** $\mathbf{1}^\top\mathbf{w}^* = 1$ and $w_k^* \geq 0$ for all $k$.

**Dual feasibility:** $\lambda_k^* \geq 0$ for all $k$.

**Complementary slackness:** $\lambda_k^* w_k^* = 0$ for all $k$.

The equality-constraint multiplier $\mu^*$ is unrestricted in sign and provides the degree of freedom required by the unit-sum condition. In the NNLS baseline (no equality constraint), the corresponding multiplier is zero; the introduction of $\mu^*$ is the sole structural addition to the KKT system.

### Characterization of the Optimal Solution

The index set $\{1, \dots, K\}$ is partitioned at the optimum into the passive set $\mathcal{P}^* = \{k : w_k^* > 0\}$ and the active set $\mathcal{Z}^* = \{k : w_k^* = 0\}$. By complementary slackness, $\lambda_k^* = 0$ for $k \in \mathcal{P}^*$, so the stationarity condition reduces, for each $k \in \mathcal{P}^*$, to:

$$2\bigl[\mathbf{Q}\mathbf{w}^* - \mathbf{c}\bigr]_k = -\mu^*.$$

For each $k \in \mathcal{Z}^*$, dual feasibility requires $\lambda_k^* \geq 0$, giving [@BoydVandenberghe2004][@WangCarreiraPerpinan2013]:

$$2\bigl[\mathbf{Q}\mathbf{w}^* - \mathbf{c}\bigr]_k \geq -\mu^*.$$

At the optimum, the partial derivative of the squared-error objective with respect to each strictly positive-weight GMM equals the same constant $-\mu^*$, while the corresponding derivative for each zero-weight GMM is no smaller than $-\mu^*$. This gradient-equalization structure on $\mathcal{P}^*$ is the essential difference from the NNLS baseline, which requires those partial derivatives to equal zero (i.e., $\mu^* = 0$ in the NNLS case). The multiplier $\mu^*$ acts as a uniform gradient shift that compensates for the unit-sum requirement, ensuring that no excluded GMM could reduce the objective if admitted to the active support [@SpecCompileResearch].

### Bordered KKT Linear System for the Passive Set

For a known passive set $\mathcal{P}$, restricting the stationarity condition to indices in $\mathcal{P}$ (where $\lambda_k^* = 0$) and appending the unit-sum constraint $\mathbf{1}_{|\mathcal{P}|}^\top\mathbf{w}^*_\mathcal{P} = 1$ (since $w_k^* = 0$ for $k \in \mathcal{Z}^*$) yields a $(|\mathcal{P}|+1) \times (|\mathcal{P}|+1)$ bordered linear system in the unknowns $(\mathbf{w}^*_\mathcal{P}, \mu^*)$ [@NocedalWright2006][@GoldfarbIdnani1983]:

$$\begin{pmatrix} 2\mathbf{Q}_{\mathcal{P}\mathcal{P}} & -\mathbf{1}_{|\mathcal{P}|} \\ \mathbf{1}_{|\mathcal{P}|}^\top & 0 \end{pmatrix} \begin{pmatrix} \mathbf{w}^*_\mathcal{P} \\ \mu^* \end{pmatrix} = \begin{pmatrix} 2\mathbf{c}_\mathcal{P} \\ 1 \end{pmatrix},$$

where $\mathbf{Q}_{\mathcal{P}\mathcal{P}}$ is the principal submatrix of $\mathbf{Q}$ indexed by $\mathcal{P}$, $\mathbf{c}_\mathcal{P}$ is the corresponding sub-vector, and $\mathbf{1}_{|\mathcal{P}|}$ is the all-ones vector of length $|\mathcal{P}|$. The bordered matrix is invertible when $\mathbf{Q}_{\mathcal{P}\mathcal{P}}$ is positive definite---satisfied when the passive-set columns of $\tilde{\mathbf{A}}$ are linearly independent, a generic condition for distinct GMMs evaluated over a sufficiently rich period mesh. The full solution is completed by setting $w_k^* = 0$ for all $k \in \mathcal{Z}^*$.

### Algorithmic Solution

Since $\mathcal{P}^*$ is not known a priori, the bordered system cannot be solved directly, and an iterative procedure is required. If the candidate solution for a given trial passive set contains any negative components, those indices are transferred to $\mathcal{Z}$ and the iteration repeats; finite convergence is guaranteed because the number of distinct index partitions of $\{1, \dots, K\}$ is finite and the objective decreases monotonically at each non-degenerate step [@WikipediaNNLS].

In R, the Goldfarb-Idnani dual active-set algorithm implemented in `quadprog::solve.QP` handles equality constraints through the `meq` argument, accepting the unit-sum row $\mathbf{1}^\top\mathbf{w} = 1$ alongside the non-negativity inequalities; this approach has been adopted in recent seismological studies combining candidate GMPEs under the unit-sum requirement [@GoldfarbIdnani1983][@JangEtAl2023][@KwakEtAl2022]. The `lsei` package solves least-squares problems subject to simultaneous equality and inequality linear constraints via the Lawson-Hanson extension [@SpecCompileResearch]. The disciplined convex programming interface `CVXR` accommodates the simplex constraint via the constraint block `list(w >= 0, sum(w) == 1)`, dispatching to interior-point solvers such as CLARABEL or OSQP [@SpecCompileResearch][@FuEtAl2020]. All three approaches converge to the unique global minimizer $\mathbf{w}^*$ over $\Delta^{K-1}$, satisfying the logic-tree normalization requirement by construction.

---

## SLOT 2: Validity of post-hoc normalization versus constrained optimization

### The Post-Hoc Normalization Procedure

An operationally simpler alternative to solving (P) directly is to apply the NNLS algorithm---enforcing only $w_k \geq 0$---obtain $\hat{\mathbf{w}}^{\mathrm{NNLS}}$, and then rescale the result by its total weight. Let $s = \mathbf{1}^\top\hat{\mathbf{w}}^{\mathrm{NNLS}} > 0$ denote the sum of the NNLS weights. The condition $s > 0$ holds in any well-posed calibration instance: $s = 0$ would require all components to be zero, which cannot occur at the strictly convex minimum unless $\mathbf{y}$ lies in the null space of $\tilde{\mathbf{A}}$, excluded by the full column rank assumption. The post-hoc normalized vector is:

$$\tilde{\mathbf{w}} = \frac{\hat{\mathbf{w}}^{\mathrm{NNLS}}}{s} = \frac{\hat{\mathbf{w}}^{\mathrm{NNLS}}}{\mathbf{1}^\top\hat{\mathbf{w}}^{\mathrm{NNLS}}}.$$

By construction, $\mathbf{1}^\top\tilde{\mathbf{w}} = 1$ and $\tilde{w}_k \geq 0$ for all $k$, so $\tilde{\mathbf{w}} \in \Delta^{K-1}$ is a feasible point for (P). Feasibility alone, however, does not imply optimality in constrained optimization. Under the strict convexity of the objective and Slater's condition established for (P) in the preceding section, the KKT conditions are both necessary and sufficient for global optimality. The question of whether $\tilde{\mathbf{w}} = \mathbf{w}^*$ is completely determined by whether $\tilde{\mathbf{w}}$ satisfies those KKT conditions [@SpecCompileResearch].

### Gradient Analysis at the Normalized Point

The gradient of the objective $f(\mathbf{w}) = \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2$ is $\nabla f(\mathbf{w}) = 2(\mathbf{Q}\mathbf{w} - \mathbf{c})$. Since $s > 0$ preserves signs, the passive set of $\tilde{\mathbf{w}}$ equals that of $\hat{\mathbf{w}}^{\mathrm{NNLS}}$: $\mathcal{P} = \{k : \hat{w}_k^{\mathrm{NNLS}} > 0\}$. The NNLS KKT stationarity condition for $k \in \mathcal{P}$ states $[\mathbf{Q}\hat{\mathbf{w}}^{\mathrm{NNLS}} - \mathbf{c}]_k = 0$, equivalently $[\mathbf{Q}\hat{\mathbf{w}}^{\mathrm{NNLS}}]_k = c_k$. Evaluating the gradient of $f$ at $\tilde{\mathbf{w}} = \hat{\mathbf{w}}^{\mathrm{NNLS}}/s$ and applying this identity for each $k \in \mathcal{P}$ [@SpecCompileResearch]:

$$\bigl[\mathbf{Q}\tilde{\mathbf{w}} - \mathbf{c}\bigr]_k = \frac{1}{s}\bigl[\mathbf{Q}\hat{\mathbf{w}}^{\mathrm{NNLS}}\bigr]_k - c_k = \frac{c_k}{s} - c_k = \frac{c_k(1 - s)}{s}, \quad k \in \mathcal{P},$$

where $c_k = [\tilde{\mathbf{A}}^\top\mathbf{y}]_k = \sum_{i=1}^n \tilde{A}_{ik}\,y_i$ is the log-spectral inner product of the $k$-th GMM with the target log-spectrum.

### KKT Verification: Necessary and Sufficient Condition for Equivalence

The passive-set stationarity condition of (P) requires the existence of a scalar $\mu^* \in \mathbb{R}$ such that $2[\mathbf{Q}\tilde{\mathbf{w}} - \mathbf{c}]_k = -\mu^*$ is constant across all $k \in \mathcal{P}$. Substituting the gradient expression derived above:

$$\frac{2c_k(1 - s)}{s} = -\mu^* \quad \text{for all } k \in \mathcal{P}.$$

When $s \neq 1$, the prefactor $2(1-s)/s$ is a nonzero scalar common to all $k$, so this equation is satisfied simultaneously for all $k \in \mathcal{P}$ if and only if:

$$c_k = \bigl[\tilde{\mathbf{A}}^\top\mathbf{y}\bigr]_k \equiv \mathrm{const} \quad \text{for all } k \in \mathcal{P}.$$

The necessary and sufficient condition for post-hoc normalization to recover the constrained optimum therefore reduces to exactly one of two cases [@BoydVandenberghe2004][@LiEtAl2020]:

- **Case 1 ($s = 1$):** the NNLS solution already lies on the simplex and normalization is an identity transformation.
- **Case 2 (constant cross-correlations):** the log-spectral cross-correlation $[\tilde{\mathbf{A}}^\top\mathbf{y}]_k$ is the same constant for every $k \in \mathcal{P}$, i.e., all retained GMMs exhibit identical period-integrated log-spectral similarity to the hazard target.

### Non-Equivalence in the General Case

Neither condition holds generically in a well-posed PSHA calibration. Candidate GMMs are constructed from distinct empirical datasets, functional forms, anelastic-attenuation parameterizations, and site-amplification models; inter-model variability in log-spectral predictions is the defining characteristic of epistemic uncertainty and a prerequisite for a meaningful logic tree [@ScherbaumEtAl2009][@DelavaudEtAl2012]. The constant cross-correlation condition $[\tilde{\mathbf{A}}^\top\mathbf{y}]_k = \mathrm{const}$ is satisfied only on a measure-zero set in the joint space of design matrices and target vectors. For $s \neq 1$ and non-constant cross-correlations, the gradient of $f$ at $\tilde{\mathbf{w}}$ is not constant over $\mathcal{P}$, the KKT stationarity condition of (P) is violated, and by the strict convexity and uniqueness of $\mathbf{w}^*$, the normalized solution is strictly suboptimal: $f(\tilde{\mathbf{w}}) > f(\mathbf{w}^*)$ [@BoydVandenberghe2004][@LiEtAl2020].

### Counter-Example

A concrete numerical instance establishes the non-equivalence by direct computation. Let $K = 2$, $n = 2$, $\tilde{\mathbf{A}} = \mathbf{I}_2$, and $\mathbf{y} = (3,\,1)^\top$. The NNLS objective reduces to $(w_1 - 3)^2 + (w_2 - 1)^2$; the unconstrained minimum $(3,\,1)^\top$ is already non-negative, so $\hat{\mathbf{w}}^{\mathrm{NNLS}} = (3,\,1)^\top$, $s = 4$, and $\tilde{\mathbf{w}} = (3/4,\,1/4)^\top$. For the simplex-constrained problem (P), substituting $w_2 = 1 - w_1$ yields $f(w_1) = (w_1 - 3)^2 + w_1^2 = 2w_1^2 - 6w_1 + 9$ on $[0,\,1]$. Since $f'(w_1) = 4w_1 - 6 < 0$ for all $w_1 \in [0,\,1]$, the function is strictly decreasing on the feasible interval and the constrained minimum is at the right boundary $w_1^* = 1$, giving $\mathbf{w}^* = (1,\,0)^\top$. The objective values are:

$$f\!\left(\tilde{\mathbf{w}}\right) = \left(\tfrac{3}{4} - 3\right)^2 + \left(\tfrac{1}{4} - 1\right)^2 = \frac{81}{16} + \frac{9}{16} = \frac{90}{16} \approx 5.625,$$

$$f\!\left(\mathbf{w}^*\right) = (1 - 3)^2 + (0 - 1)^2 = 4 + 1 = 5.$$

The strict inequality $f(\tilde{\mathbf{w}}) > f(\mathbf{w}^*)$ confirms that $\tilde{\mathbf{w}} \neq \mathbf{w}^*$ and that post-hoc normalization yields a strictly suboptimal feasible point for (P) [@SpecCompileResearch][@WangCarreiraPerpinan2013].

### Geometric Interpretation

Post-hoc normalization is a radial rescaling: it moves $\hat{\mathbf{w}}^{\mathrm{NNLS}}$ along the ray from the origin through $\hat{\mathbf{w}}^{\mathrm{NNLS}}$ until the unit-sum hyperplane is intersected, preserving the direction in weight space while adjusting only the overall magnitude by the factor $1/s$. The NNLS problem optimizes simultaneously over direction and scale within the non-negative orthant; for any fixed direction $\mathbf{u} \in \Delta^{K-1}$, the scale minimizing $f(s\mathbf{u})$ over $s > 0$ is:

$$s^*(\mathbf{u}) = \frac{\mathbf{c}^\top\mathbf{u}}{\mathbf{u}^\top\mathbf{Q}\mathbf{u}}.$$

The NNLS problem therefore minimizes a nonlinear fractional objective in the direction variable $\mathbf{u}$ over $\Delta^{K-1}$ (after eliminating the optimal scale), whereas (P) is a strictly convex QP in $\mathbf{u}$ over $\Delta^{K-1}$ with scale fixed at unity. These are structurally distinct optimization problems, and their minimizers over $\Delta^{K-1}$ are generically different [@BoydVandenberghe2004].

The true simplex optimum $\mathbf{w}^*$ corresponds geometrically to the projection of the unconstrained OLS solution $\hat{\mathbf{w}}^{\mathrm{OLS}} = \mathbf{Q}^{-1}\mathbf{c}$ onto $\Delta^{K-1}$ in the metric induced by the Gram matrix $\mathbf{Q}$, a Mahalanobis-type projection. This operation is fundamentally different from the radial rescaling of $\hat{\mathbf{w}}^{\mathrm{NNLS}}$, which operates within the non-negative orthant rather than directly on $\Delta^{K-1}$ [@BoydVandenberghe2004][@WangCarreiraPerpinan2013].

### Special Case: NNLS Solution Already on the Simplex

When $s = 1$, the NNLS solution already satisfies the unit-sum constraint, $\tilde{\mathbf{w}} = \hat{\mathbf{w}}^{\mathrm{NNLS}}$, and normalization is an identity operation. In this case, inserting $\mu^* = 0$ into the passive-set stationarity condition of (P) recovers $[\mathbf{Q}\hat{\mathbf{w}}^{\mathrm{NNLS}} - \mathbf{c}]_k = 0$ for all $k \in \mathcal{P}$, which is satisfied by the NNLS optimality conditions. The active-set condition of (P)---$[\mathbf{Q}\hat{\mathbf{w}}^{\mathrm{NNLS}} - \mathbf{c}]_k \geq 0$ for all $k \in \mathcal{Z}$---coincides with the NNLS active-set condition, which holds by construction. All four KKT conditions of (P) are therefore satisfied at $\hat{\mathbf{w}}^{\mathrm{NNLS}}$ with $\mu^* = 0$, confirming that the two solutions coincide when $s = 1$ [@SpecCompileResearch][@LawsonHanson1974].

The condition $s = 1$ is non-generic: the NNLS objective imposes no sum constraint, and the event $\{\mathbf{1}^\top\hat{\mathbf{w}}^{\mathrm{NNLS}} = 1\}$ occupies a codimension-one surface in the joint space of problem instances $(\tilde{\mathbf{A}}, \mathbf{y})$. This coincidence does not represent a structural equivalence between the two optimization procedures; it occurs only when the log-spectral configuration of the candidate GMMs and the target jointly happen to produce a NNLS minimizer whose components sum to unity without any explicit enforcement of that requirement.

### Practical Consequence for PSHA Logic-Tree Weight Calibration

The mathematical non-equivalence carries direct practical consequences for GMPE logic-tree calibration in PSHA. Applying the NNLS algorithm and subsequently normalizing the output introduces a calibration error: the normalized weights satisfy the unit-sum requirement but are suboptimal in the least-squares sense, producing a larger mean squared log-spectral residual than the solution of (P) [@SpecCompileResearch][@BommerScherbaum2008]. The magnitude of this error is governed by two factors: the departure $|1 - s|$ of the NNLS total weight from unity, and the heterogeneity of the cross-correlations $\{c_k\}_{k \in \mathcal{P}}$ across retained models. For $|1-s|$ small and cross-correlations approximately equal, the normalization error may be negligible; for solutions where weight is concentrated on one or two models with large absolute cross-correlation values, the error can be substantial.

The mean hazard curve $\bar{\lambda}(i^*) = \sum_{k=1}^K w_k\,\lambda^{(k)}(i^*)$ depends on the weight vector, and deviations from the optimum $\mathbf{w}^*$ alter the relative contribution of each GMM to the epistemic-uncertainty band, particularly at low annual exceedance rates where divergence among candidate models is largest [@JangEtAl2023][@KwakEtAl2022]. The rigorous approach is to incorporate the unit-sum constraint directly into the optimization and solve (P) with a dedicated equality-inequality constrained solver as formulated in the preceding section. This requires only the addition of the equality row $\mathbf{1}^\top\mathbf{w} = 1$ to the solver's constraint matrix, with no change to the objective or the Gram matrix $\mathbf{Q}$ [@SpecCompileResearch].
