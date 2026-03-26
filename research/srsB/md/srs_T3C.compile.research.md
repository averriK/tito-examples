# Constrained Weight Calibration for Epistemic Logic Trees

## SLOT 1: Extension of the Error Minimization Formulation with Sum-to-One Weight Constraint

### Problem Framing and Notation

The error minimization framework developed in the knowledge base casts the
spectral-matching record-selection problem as a constrained linear regression
in which a weight vector $\mathbf{w} = (w_1, \dots, w_K)^\top$ is chosen to
minimize the discrepancy between a weighted combination of candidate
predictions and a reference target. In the epistemic ground-motion logic tree
for PSHA, the same algebraic structure governs the weight calibration problem:
the weights $w_k$ of the $N$ alternative GMM branches multiply the
corresponding branch hazard rates $\lambda_I^{(k)}(i^*)$, and their weighted
sum defines the mean hazard $\bar{\lambda}_I(i^*) = \sum_{k=1}^{N} w_k
\lambda_I^{(k)}(i^*)$. The present derivation extends the knowledge-base
formulation from $K$ candidate records to $N$ logic tree branches while
appending the normalization constraint $\sum_{k=1}^{N} w_k = 1$ that renders
the weight vector a proper probability distribution over the branches.
[@Ref001]



Following the log-log space reformulation of the knowledge base, the derivation
operates on log-space GMM predictions. The design matrix $\mathbf{A} \in
\mathbb{R}^{m \times N}$ has entries $A_{ij} = \ln \lambda_I^{(j)}(T_i)$,
where $m$ is the number of evaluation points (spectral periods or intensity
levels) and $j = 1, \dots, N$ indexes the branches. The target vector
$\mathbf{b} \in \mathbb{R}^m$ collects the corresponding reference log-hazard
values $b_i = \ln \lambda_I^{\mathrm{ref}}(T_i)$. The predicted log-hazard
under weight vector $\mathbf{w}$ is $\hat{\mathbf{b}} = \mathbf{A}\mathbf{w}$,
and the Gram matrix is $\mathbf{G} = \mathbf{A}^\top \mathbf{A} \in
\mathbb{R}^{N \times N}$, which is positive semi-definite and invertible when
$\mathbf{A}$ has full column rank ($m \geq N$ with linearly independent
columns). [@Ref001]



### Unconstrained Baseline

The unconstrained ordinary least-squares formulation provides the baseline
against which the constrained extensions are developed. The objective is to
find the weight vector minimizing the residual sum of squares over all
$\mathbf{w} \in \mathbb{R}^N$: [@Ref001]



$$\min_{\mathbf{w} \in \mathbb{R}^N} \|\mathbf{A}\mathbf{w} - \mathbf{b}\|_2^2.$$

Setting the gradient $2\mathbf{A}^\top(\mathbf{A}\mathbf{w} - \mathbf{b}) =
\mathbf{0}$ gives the normal equations $\mathbf{G}\hat{\mathbf{w}} =
\mathbf{A}^\top \mathbf{b}$, whose unique solution under full column rank of
$\mathbf{A}$ is: [@Ref001]



$$\hat{\mathbf{w}}_{\mathrm{OLS}} = \mathbf{G}^{-1} \mathbf{A}^\top \mathbf{b}.$$

The unconstrained solution does not restrict the sign of individual components:
negative weights arise whenever two or more branch predictions are highly
correlated, and the quantity $\mathbf{1}^\top \hat{\mathbf{w}}_{\mathrm{OLS}}$
is not controlled by the optimization, so the normalization requirement can be
arbitrarily violated. These deficiencies motivate the constrained extensions
developed in the sections that follow. [@Ref001]



### Strict Positivity Constraint

A first constraint extension requires each component of $\mathbf{w}$ to be
strictly positive: $w_k > 0$ for all $k = 1, \dots, N$. In the epistemic
logic tree framework, a zero weight eliminates the corresponding branch from
the weighted combination, implying that the branch's scientific hypothesis
contributes no information to the mean hazard estimate. A negative weight has
no probabilistic interpretation, since no anti-GMPE exists -- a situation
structurally parallel to the absence of anti-records in ground-motion databases
discussed in the knowledge base. The strict positivity requirement therefore
constitutes a tightened form of the non-negativity constraint of the NNLS
formulation, restricted to the open interior of the positive orthant.
[@Ref001]



In practice, strict positivity is operationalized through the lower bound
$w_k \geq \epsilon$ for some $\epsilon > 0$, which converts the open feasible
region into a closed convex set amenable to standard solvers. With this
substitution, the constrained problem is a convex quadratic program on a
translated positive orthant: [@Ref001]



$$\min_{\mathbf{w} \in \mathbb{R}^N} \|\mathbf{A}\mathbf{w} - \mathbf{b}\|_2^2
\quad \text{subject to} \quad w_k \geq \epsilon, \quad k = 1, \dots, N.$$

This is a bounded-variable least-squares (BVLS) instance with $w_{\min} =
\epsilon$ and $w_{\max} = +\infty$, solvable by the active-set and quadratic
programming methods described in the knowledge base. [@Ref001]



### Sum-to-One Constraint: Final Step

The normalization condition $\sum_{k=1}^{N} w_k = 1$, written in vector form
as $\mathbf{1}^\top \mathbf{w} = 1$, is imposed as the final constraint,
restricting the feasible region to the probability simplex $\Delta_{N-1} =
\{\mathbf{w} \in \mathbb{R}^N : \mathbf{1}^\top \mathbf{w} = 1,\, w_k > 0\}$.
Under this constraint, the weight vector constitutes a proper discrete
probability distribution over the $N$ branches, rendering the mean hazard
$\bar{\lambda}_I(i^*) = \sum_{k=1}^{N} w_k \lambda_I^{(k)}(i^*)$ an
expectation of the branch-specific hazard with respect to this distribution.
Equal weights $w_k = 1/N$ satisfy the constraint trivially and represent the
state of maximum epistemic uncertainty, as noted in the task context.
[@Ref001]



The complete optimisation problem, combining the quadratic objective, the
strict positivity requirement, and the normalization constraint as the terminal
step, is as follows: [@Ref001]



$$\min_{\mathbf{w} \in \mathbb{R}^N} \|\mathbf{A}\mathbf{w} - \mathbf{b}\|_2^2
\quad \text{subject to} \quad \mathbf{1}^\top \mathbf{w} = 1, \quad
w_k \geq \epsilon, \quad k = 1, \dots, N.$$

This constitutes a generalization of the constrained ordinary least-squares
regression: the objective is a strictly convex quadratic, the equality
constraint is linear, and the bound constraints define a compact convex
feasible region. The problem subsumes all previously described formulations as
special cases: removing the equality constraint while setting $\epsilon = 0$
recovers the NNLS problem; substituting a finite $w_{\max}$ alongside
$w_{\min} = \epsilon$ recovers the BVLS formulation; and setting $\epsilon
\to 0$ while retaining $\mathbf{1}^\top \mathbf{w} = 1$ gives the
simplex-constrained regression without the strict positivity floor.
[@Ref001]



### Lagrange Multiplier Derivation

When the positivity constraints are not binding -- that is, when the solution
of the equality-only problem already satisfies $w_k > 0$ for all $k$ -- a
closed-form expression is available via the method of Lagrange multipliers.
The Lagrangian is formed by adjoining the normalization constraint to the
least-squares objective with multiplier $\mu \in \mathbb{R}$:



$$\mathcal{L}(\mathbf{w}, \mu) = \|\mathbf{A}\mathbf{w} - \mathbf{b}\|_2^2
+ \mu\!\left(\mathbf{1}^\top \mathbf{w} - 1\right).$$

Stationarity with respect to $\mathbf{w}$, $\nabla_{\mathbf{w}} \mathcal{L} =
\mathbf{0}$, gives $2\mathbf{A}^\top(\mathbf{A}\mathbf{w} - \mathbf{b}) +
\mu\,\mathbf{1} = \mathbf{0}$, which rearranges to the augmented normal
equations $\mathbf{G}\mathbf{w} = \mathbf{A}^\top \mathbf{b} -
(\mu/2)\,\mathbf{1}$. Under full column rank of $\mathbf{A}$, the weight
vector is expressed as a function of the multiplier:



$$\mathbf{w}(\mu) = \hat{\mathbf{w}}_{\mathrm{OLS}} - \frac{\mu}{2}\,
\mathbf{G}^{-1}\mathbf{1}.$$

Substituting $\mathbf{w}(\mu)$ into the constraint $\mathbf{1}^\top \mathbf{w}
= 1$ and solving for $\mu$ gives the expression below. The denominator
$\mathbf{1}^\top \mathbf{G}^{-1}\mathbf{1}$ is strictly positive when
$\mathbf{G}$ is positive definite, ensuring the multiplier is well defined.
Back-substitution into $\mathbf{w}(\mu)$ then yields the closed-form
equality-constrained solution:



$$\frac{\mu}{2} = \frac{\mathbf{1}^\top \hat{\mathbf{w}}_{\mathrm{OLS}} - 1}
{\mathbf{1}^\top \mathbf{G}^{-1}\mathbf{1}},$$

$$\hat{\mathbf{w}}_{\mathrm{eq}} = \hat{\mathbf{w}}_{\mathrm{OLS}}
- \frac{\mathbf{1}^\top \hat{\mathbf{w}}_{\mathrm{OLS}} - 1}
{\mathbf{1}^\top \mathbf{G}^{-1}\mathbf{1}}\,\mathbf{G}^{-1}\mathbf{1}.$$

The closed-form solution $\hat{\mathbf{w}}_{\mathrm{eq}}$ admits a
geometrically transparent interpretation. The correction term displaces the
unconstrained OLS solution along the direction $\mathbf{G}^{-1}\mathbf{1}$ in
weight space by precisely the amount needed to satisfy the normalization; the
displacement magnitude is proportional to the constraint violation
$|\mathbf{1}^\top \hat{\mathbf{w}}_{\mathrm{OLS}} - 1|$, and the correction
vanishes identically when $\mathbf{1}^\top \hat{\mathbf{w}}_{\mathrm{OLS}} = 1$.
This projection structure is a direct consequence of the orthogonality
conditions imposed by the equality constraint, and mirrors the projection form
of the constrained estimator in classical regression with linear equality
constraints. [@Ref002]



### Karush-Kuhn-Tucker Conditions

When the equality-constrained solution $\hat{\mathbf{w}}_{\mathrm{eq}}$
contains one or more non-positive components, the positivity constraints become
active and the closed form is no longer optimal. In that case, a feasible
point $\mathbf{w}^*$ is optimal for the problem $\min_{\mathbf{w}}
\|\mathbf{A}\mathbf{w} - \mathbf{b}\|_2^2$ subject to $\mathbf{1}^\top
\mathbf{w} = 1$ and $w_k \geq 0$ if and only if there exist $\mu^* \in
\mathbb{R}$ and $\boldsymbol{\nu}^* \in \mathbb{R}_+^N$ satisfying the
following Karush-Kuhn-Tucker (KKT) conditions:
[@Ref003]



$$2\mathbf{A}^\top(\mathbf{A}\mathbf{w}^* - \mathbf{b})
+ \mu^*\,\mathbf{1} - \boldsymbol{\nu}^* = \mathbf{0},$$

$$\mathbf{1}^\top \mathbf{w}^* = 1, \qquad w_k^* \geq 0, \qquad
\nu_k^* \geq 0, \qquad \nu_k^* w_k^* = 0 \quad \forall\, k,$$

where $\mu^* \in \mathbb{R}$ is the equality-constraint multiplier and
$\boldsymbol{\nu}^* \in \mathbb{R}_+^N$ collects the non-negative multipliers
for the bound constraints.



The complementary slackness condition $\nu_k^* w_k^* = 0$ yields the
active-passive partition: the passive set $\mathcal{P} = \{k : w_k^* > 0\}$
comprises branches with positive optimal weights (with $\nu_k^* = 0$), while
the active set $\mathcal{Z} = \{k : w_k^* = 0\}$ comprises branches driven to
zero by the binding constraint (with $\nu_k^* > 0$). The equality constraint
then requires $\sum_{k \in \mathcal{P}} w_k^* = 1$, since active-set weights
contribute nothing to the sum. This partition is structurally parallel to the
Lawson-Hanson active-set decomposition for the NNLS problem, with the
additional linkage that the equality constraint ties together all passive-set
weights through the normalization condition. [@Ref001]



Because the objective is strictly convex under full column rank of $\mathbf{A}$
(the Hessian $2\mathbf{G}$ is positive definite) and the feasible region
$\Delta_{N-1} = \{\mathbf{w} : \mathbf{1}^\top \mathbf{w} = 1,\,
\mathbf{w} \geq \mathbf{0}\}$ is a compact convex polytope, the KKT conditions
are both necessary and sufficient for global optimality and the global minimizer
is unique. Any interior-point or active-set QP solver therefore converges to
this unique optimal weight vector.
[@Ref004]



### Relationship to Constrained Linear Regression

The formulation establishes the normalised weight calibration problem as a
generalization of equality-constrained ordinary least-squares regression. The
general equality-constrained OLS problem, $\min_{\mathbf{w}}
\|\mathbf{A}\mathbf{w} - \mathbf{b}\|_2^2$ subject to $\mathbf{C}\mathbf{w}
= \mathbf{d}$, is solved by the bordered linear system:
[@Ref002]



$$\begin{pmatrix} 2\mathbf{G} & \mathbf{C}^\top \\ \mathbf{C} & \mathbf{0}
\end{pmatrix} \begin{pmatrix} \hat{\mathbf{w}} \\ \boldsymbol{\mu}
\end{pmatrix} = \begin{pmatrix} 2\mathbf{A}^\top \mathbf{b} \\ \mathbf{d}
\end{pmatrix}.$$

For the normalization constraint, the identification $\mathbf{C} =
\mathbf{1}^\top \in \mathbb{R}^{1 \times N}$ and $\mathbf{d} = 1$ reduces the
bordered system to the $(N+1) \times (N+1)$ scalar-multiplier problem derived
in the preceding section. The addition of the strict positivity constraints
$w_k \geq \epsilon$ makes the bordered linear system alone insufficient; a full
QP with one equality constraint and $N$ bound constraints is required. The
complete constrained weight calibration problem in its final form is:



$$\min_{\mathbf{w} \in \mathbb{R}^N} \|\mathbf{A}\mathbf{w} - \mathbf{b}\|_2^2
\quad \text{subject to} \quad \mathbf{1}^\top \mathbf{w} = 1, \quad
w_k \geq \epsilon, \quad k = 1, \dots, N.$$

This problem subsumes, as special cases, the unconstrained OLS (all
constraints removed), the NNLS (equality removed, $\epsilon = 0$), the BVLS
(equality removed, finite $w_{\max}$), and the equality-only constrained OLS
($\epsilon \to 0$). The progression from the unconstrained baseline through
strict positivity to the final normalisation constraint represents a sequence
of nested feasible regions, each strictly smaller than the preceding one, that
successively enforce the physical and probabilistic requirements of the PSHA
epistemic logic tree. The connection to data-driven GMM weight calibration
methods -- such as the log-likelihood approach, which derives branch weights
from the fit of each GMM to strong-motion records -- is that those methods
define the target vector $\mathbf{b}$ from observational log-likelihoods and
then apply the constrained regression framework to assign weights satisfying
the normalization condition. [@Ref001][@Ref005]


