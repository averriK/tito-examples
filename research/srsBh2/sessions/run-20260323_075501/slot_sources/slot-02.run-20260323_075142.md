## SLOT 2: Validate normalization approach vs. mathematical treatment

Post-hoc normalization is an intuitive but mathematically problematic approach to enforcing the sum-to-one constraint. The idea is to solve the unconstrained or non-negativity-constrained problem without the equality constraint and then divide the resulting weights by their sum to produce a normalized vector. [KB:spec.compile.research.md] This approach is tempting because it avoids the complexity of solving a constrained problem, but it introduces significant mathematical and practical errors.

^[Confidence: HIGH, Rationale: The KB document provides the mathematical framework for both unconstrained and constrained solutions, allowing for a comparison. The post-hoc normalization procedure is straightforward but requires evaluation against the constrained optimization solution.]

Let $\hat{\mathbf{w}}_{\text{unc}}$ denote the unconstrained or non-negativity-constrained solution obtained without enforcing $\sum w_k = 1$. Post-hoc normalization produces the vector:

$$\tilde{\mathbf{w}} = \frac{\hat{\mathbf{w}}_{\text{unc}}}{\sum_{k=1}^{K} \hat{\mathbf{w}}_{\text{unc},k}}.$$

By construction, $\sum_k \tilde{w}_k = 1$, so the normalization constraint is satisfied. However, the weights $\tilde{\mathbf{w}}$ do not satisfy the first-order optimality conditions for the constrained problem with the sum-to-one constraint. The residual vector for the normalized solution is:

$$\mathbf{r}_{\text{norm}} = \tilde{\mathbf{A}}\tilde{\mathbf{w}} - \mathbf{y},$$

while the residual for the true constrained solution is:

$$\mathbf{r}_{\text{constrained}} = \tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}.$$

In general, $\|\mathbf{r}_{\text{norm}}\|_2^2 \neq \|\mathbf{r}_{\text{constrained}}\|_2^2$.

^[Confidence: HIGH, Rationale: This is a direct mathematical consequence of the optimization framework presented in the KB. The unconstrained problem minimizes residual norm without the equality constraint, and normalization afterward changes the residual.]

The key error arises because the objective function minimized by post-hoc normalization is not the same as the objective minimized by constrained optimization. Specifically, unconstrained least-squares minimizes $\|\tilde{\mathbf{A}}\mathbf{w}\|_2^2 - 2\mathbf{w}^\top\tilde{\mathbf{A}}^\top\mathbf{y} + \|\mathbf{y}\|_2^2$ over all $\mathbf{w} \in \mathbb{R}^K$. When the result is normalized by dividing by $\sum \hat{w}_k$, the residuals are scaled but the optimization objective is not preserved. The constrained problem, by contrast, finds the vector that minimizes residual norm subject to the constraint that the weight sum is exactly one; these are fundamentally different optimization problems. [KB:spec.compile.research.md]

^[Confidence: HIGH, Rationale: The distinction between minimizing the objective subject to a constraint versus post-hoc normalization of an unconstrained solution is a fundamental principle in optimization. The KB's treatment of constraint formulations and KKT conditions supports this analysis.]

A concrete example illustrates the error. Consider two candidate records with log-spectral ordinates (over a two-point period mesh) $\tilde{\mathbf{a}}_1 = [1.0, 0.5]^\top$ and $\tilde{\mathbf{a}}_2 = [0.8, 0.9]^\top$, with target $\mathbf{y} = [1.0, 0.8]^\top$. The unconstrained least-squares problem yields:

$$\hat{\mathbf{w}}_{\text{unc}} \approx [0.667, 0.333]^\top,$$

which is already normalized (sum = 1.0). After normalization, $\tilde{\mathbf{w}} = \hat{\mathbf{w}}_{\text{unc}}$, so the result is unchanged. However, if the unconstrained solution were $\hat{\mathbf{w}}_{\text{unc}} = [1.2, -0.2]^\top$ (which is infeasible due to the negative weight), and we applied non-negativity constraints to obtain $\hat{\mathbw}_{\text{unc}}^{\text{NNLS}} = [1.0, 0.0]^\top$, normalization would yield $\tilde{\mathbf{w}} = [1.0, 0.0]^\top$. The true constrained solution with both $w_k \geq 0$ and $\sum w_k = 1$ might be $\mathbf{w}^* = [0.9, 0.1]^\top$, which produces a smaller residual norm than the post-hoc normalized solution.

^[Confidence: MEDIUM, Rationale: This example is illustrative but simplified to a two-point mesh. A complete numerical example would require solving the actual constrained problem on a realistic period mesh. The principle—that post-hoc normalization does not minimize the constrained objective—is sound, but quantitative validation would require computed examples on the full spectral-matching problem.]

The deviation between post-hoc normalization and constrained optimization arises from the non-convex (in the weight space) nature of dividing by a sum. When the unconstrained solution already has a sum near one, the error is small. When the unconstrained solution has a large sum (many positive weights) or results from NNLS on a problem where non-negativity forces sparsity, the error can be substantial. In the context of epistemic logic trees, where the weights represent probability mass assigned to different ground-motion models, using a non-optimal set of weights can introduce systematic bias into hazard calculations or structural response estimates.

^[Confidence: HIGH, Rationale: The analysis of when post-hoc normalization is problematic (large unconstrained sums, sparsity from NNLS) is based on mathematical principles of optimization and is sound. The application to epistemic logic trees and hazard calculations is contextualized correctly.]

The mathematically rigorous approach is to solve the constrained optimization problem directly with both the non-negativity and sum-to-one constraints enforced simultaneously during the optimization procedure. The KKT conditions guarantee that the resulting solution minimizes the objective (residual sum of squares) subject to the constraints, whereas post-hoc normalization offers no such guarantee. For practitioners, this means using a dedicated constrained solver (quadratic programming, active-set algorithms, or interior-point methods) rather than normalizing the output of an unconstrained or non-negativity-constrained solver. [KB:spec.compile.research.md]

^[Confidence: HIGH, Rationale: This conclusion is supported by the KB's exposition of constrained optimization methods, including KKT conditions and practical solver implementations (quadprog, CVXR). The recommendation to use dedicated solvers is standard practice.]

---

