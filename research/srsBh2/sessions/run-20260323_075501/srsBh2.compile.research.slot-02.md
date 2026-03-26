## SLOT 2: Validate normalization approach vs. mathematical treatment

### Problem Statement

A natural question in weight calibration is whether the sum-to-one constraint can be enforced post-hoc by solving an unconstrained or non-negativity-constrained problem and then normalizing the result, rather than solving a fully constrained optimization problem. Specifically, if an unconstrained least-squares solution $\hat{\mathbf{w}}_{\text{unc}}$ is obtained, whether dividing each weight by their sum $\hat{\mathbf{w}}_{\text{norm}} = \hat{\mathbf{w}}_{\text{unc}} / \sum_k \hat{w}_k$ yields a valid approximation to the true constrained solution requires careful mathematical analysis [@KBSpecCompile].

### Mathematical Non-Equivalence

The post-hoc normalization approach operates in two steps. First, solve an unconstrained or non-negativity-constrained least-squares problem:

$$\hat{\mathbf{w}}_{\text{unc}} = \arg\min_{\mathbf{w} \geq 0} \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2$$

Then rescale the weights:

$$\tilde{\mathbf{w}} = \frac{\hat{\mathbf{w}}_{\text{unc}}}{\sum_{k=1}^{K} \hat{\mathbf{w}}_{\text{unc},k}}$$

By construction, $\sum_k \tilde{w}_k = 1$, and the normalization constraint is satisfied. However, the normalized weights do not satisfy the first-order optimality conditions for the constrained problem with sum-to-one constraint. The residuals differ:

$$\|\tilde{\mathbf{A}}\tilde{\mathbf{w}} - \mathbf{y}\|_2^2 \neq \|\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}\|_2^2$$

where $\mathbf{w}^*$ is the true constrained minimizer [@KBSpecCompile].

The fundamental issue is that normalization is a nonlinear operation that does not preserve optimality conditions. Let $S = \sum_{k=1}^{K} \hat{\mathbf{w}}_{\text{unc},k}$ denote the sum of the unconstrained solution. The residual after normalization scales as:

$$\left\|\tilde{\mathbf{A}}\tilde{\mathbf{w}} - \mathbf{y}\right\|_2^2 = \frac{1}{S^2}\left\|\tilde{\mathbf{A}}\hat{\mathbf{w}}_{\text{unc}} - S\mathbf{y}\right\|_2^2$$

Unless $S = 1$ (meaning the unconstrained solution already sums to unity), post-hoc normalization yields a suboptimal fit relative to the constrained minimizer. The constrained solution, by definition, achieves the minimum residual over all feasible points on the simplex.

### Optimality Conditions

The constrained and unconstrained problems enforce fundamentally different optimality conditions. At the unconstrained optimum, the gradient of the loss function is zero:

$$\nabla f(\hat{\mathbf{w}}_{\text{unc}}) = 2\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\hat{\mathbf{w}}_{\text{unc}} - \mathbf{y}) = \mathbf{0}$$

At the constrained optimum with Lagrange multiplier $\lambda$ for the sum-to-one constraint, the gradient is parallel to the constraint normal:

$$2\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}) = -\lambda \mathbf{1}$$

Post-hoc normalization of $\hat{\mathbf{w}}_{\text{unc}}$ merely rescales the weights without adjusting the residual vector to satisfy this constrained optimality condition. Normalization cannot recover $\mathbf{w}^*$ unless by coincidence the unconstrained solution already satisfies the simplex constraint [@KBSpecCompile].

### Geometric Perspective

Geometrically, the unconstrained problem seeks the point in $\mathbb{R}^K$ closest to the target spectrum in the least-squares sense. The constrained problem restricts the search to the probability simplex, the feasible region where all weights are non-negative and sum to unity. Scaling (normalization) is a linear operation that preserves rays from the origin. If the unconstrained solution lies on a ray from the origin, normalization keeps it on that same ray. However, the constrained optimum lies on the affine hyperplane $\sum w_k = 1$ and, in general, does not coincide with the ray containing the unconstrained solution. Thus, the normalized unconstrained solution and the constrained solution are geometrically distinct, lying at different points in weight space [@KBSpecCompile].

The constrained solution represents the orthogonal projection onto the feasible region in the metric induced by the loss function, whereas post-hoc normalization applies only a hyperplane projection, which does not minimize the objective on the constrained set.

### Practical Significance

The magnitude of suboptimality introduced by post-hoc normalization depends on how far $S$ deviates from unity. If the unconstrained solution naturally sums close to unity (e.g., $S \approx 1.1$), the rescaling factor $1/S$ is near unity and the additional error is small. Conversely, if the unconstrained solution exhibits weights summing substantially above or below unity (e.g., $S \approx 2$ or $S \approx 0.5$), normalization introduces significant discrepancy from the true constrained optimum.

When the non-negativity constraint alone is applied (as in non-negative least-squares, NNLS), the unconstrained problem becomes sparse because the optimization forces some weights to zero. In this case, the remaining positive weights often sum to a value substantially different from unity, and post-hoc normalization can introduce substantial bias into the weight estimates. Furthermore, if the unconstrained OLS solution includes negative weights (which is typical), the effect of normalization on the direction and magnitude of the weight vector becomes more pronounced. The normalized solution may not preserve the relative contribution structure intended by the regression [@KBSpecCompile].

In the context of epistemic logic trees for probabilistic seismic hazard analysis, where weights represent relative plausibility assignments to competing ground-motion prediction equations, using suboptimal weights can introduce systematic bias into hazard calculations and structural response estimates.

### Conclusion

While post-hoc normalization is computationally simpler and may provide a practical approximation in some applications where the unconstrained sum is already close to unity, it does not solve the constrained optimization problem and introduces potentially significant suboptimality. The constrained solution, obtained by enforcing both the non-negativity and sum-to-one constraints simultaneously during optimization, minimizes the objective residual on the feasible region. For epistemic logic tree construction in probabilistic seismic hazard analysis, where the sum-to-one constraint is a fundamental requirement reflecting the probabilistic interpretation of weights, constrained optimization via Lagrange multipliers or equivalent quadratic programming formulations is the theoretically sound and practically preferable approach [@KBSpecCompile]. Practitioners should employ dedicated constrained optimization solvers (such as active-set methods, interior-point methods, or convex quadratic programming packages) rather than normalizing the output of unconstrained or non-negativity-constrained solvers.
