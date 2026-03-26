# Spectral Matching as Linear Regression: Structured Prompt

## CONTEXT

Traditional spectral matching methods modify recorded accelerograms to achieve conformity with target response spectra derived from probabilistic seismic hazard analysis (PSHA), but in doing so they alter the frequency content, duration characteristics, and number of sign reversals present in the original ground-motion records. Spectral matching in the time or frequency domain frequently distorts the non-stationary characteristics of ground motion and can alter scalar parameters such as Arias intensity. Phenomena including stiffness degradation and liquefaction depend on the number of load reversals, and the seismic response of systems that accumulate damage under cyclic loading depends not only on peak amplitude but also on duration and effective cycle count.

### Notation

Given a candidate set of $m$ spectra $S_a(T_n)$ and a period mesh of $n$ points $\{T_1, \dots, T_n\}$, each spectrum $k = 1, \dots, K$ is defined by spectral ordinates $S_{a,k}(T_i)$ for $i = 1, \dots, n$. The PSHA-derived target spectrum is encoded as the vector $\mathbf{y} \in \mathbb{R}^n$ with components $y_i = \ln S_a^{\mathrm{obj}}(T_i)$. The objective is to find weights $w_k$ such that the weighted linear combination of the candidate spectra minimizes the discrepancy with respect to the target spectrum.

## SLOTS

### SLOT 1: Summary of spectral-matching record-selection methodologies

Provide a concise summary of ground-motion record-selection methodologies that modify spectral content so that a linear combination of response spectra approximates the target spectrum. The summary should cover the principal approaches recognized in the earthquake engineering literature, distinguishing them from time-domain or frequency-domain waveform-modification techniques.

<!-- Coverage: TASK_FILE line 12 ("Resume brevemente las metodologias de seleccion de registros sismicos que modifican el contenido espectral para que la combinacion lineal de espectros sea 'parecida' al espectro objetivo"). Fully covered. -->

### SLOT 2: Minimum number of records and code-based requirements

Address two sub-questions: (a) according to the linear-combination methodology described in SLOT 1, what is the theoretical minimum number of spectra required to achieve an adequate spectral match, and (b) what is the origin of the 7- and 11-record minima recommended by design codes such as ASCE 7 for nonlinear structural analysis - i.e., the statistical or engineering rationale behind those specific thresholds.

<!-- Coverage: TASK_FILE line 13 ("segun esta metodologia, cuantos espectros se necesitan como minimo para lograr el match? De donde vienen los 7 u 11 registros minimos recomendados por algunas normativas como el ASCE-7"). Fully covered. -->

### SLOT 3: Classical linear regression formulation (RMSE minimization)

Formulate the spectral-matching problem as a classical linear regression problem in which the weight vector $\mathbf{w} = (w_1, \dots, w_K)^\top$ minimizes the global root-mean-square error (RMSE) between the weighted linear combination of candidate spectra and the target spectrum. Use the notation established in the Context section above (spectral ordinates $S_{a,k}(T_i)$, target vector $\mathbf{y}$, period mesh $\{T_1, \dots, T_n\}$). Present the design matrix, the objective function, and the closed-form least-squares solution.

<!-- Coverage: TASK_FILE lines 18-25 (notation setup and "Formula el problema como un problema clasico de regresion lineal, donde se buscan los pesos w que minimizan el error global RMSE. Emplea la notacion anterior"). Fully covered. -->

### SLOT 4: Log-log space reformulation

Reformulate the linear regression problem from SLOT 3 in the $\log S_a$ - $\log T_n$ space, noting that spectral functions are smoother in log-log coordinates. Present the transformed design matrix, the transformed target vector, and the resulting objective function, using the same notation framework.

<!-- Coverage: TASK_FILE lines 29-30 ("En el espacio Log(Sa) - Log(Tn), las funciones son mas suaves. ... formula el mismo problema anterior en el espacio log-log en esta notacion"). Fully covered. -->

### SLOT 5: Non-negative weight constraint and R implementation

Extend the regression formulation to enforce strictly non-negative weights ($w_k \geq 0$ for all $k$), addressing the physical implausibility of negative scaling factors for ground-motion spectra. Discuss whether Ridge regression can directly incorporate a non-negativity constraint on the coefficients. Provide a working code example in R that solves the non-negative least-squares (NNLS) problem.

<!-- Coverage: TASK_FILE lines 32-33 ("Extiende el problema de regresion lineal en donde se busquen unicamente los pesos positivos. Implementa la solucion? Es posible resolverlo directamente con Ridge pidiendo la restriccion de pesos positivos? Proponga un ejemplo de codigo en R"). Fully covered. -->

### SLOT 6: Bounded weights with Ridge/Lasso feasibility

Extend the formulation further to impose box constraints on the weights: $w_{\min} \leq w_k \leq w_{\max}$ for all $k$. Discuss whether Ridge or Lasso regularization can enforce explicit upper and lower bounds on individual coefficients. Provide a code example (in R) demonstrating the bounded-weight formulation.

<!-- Coverage: TASK_FILE lines 36-37 ("extiende la formulacion del problema para limitar los tamanos de los pesos. Es posible aplicar Ridge/Lasso para esto? propon un ejemplo"). Fully covered. -->

### SLOT 7: Convex optimization generalization with R libraries

Generalize the spectral-matching problem as a convex optimization problem. Propose an explicit loss function that subsumes the constraints from SLOTS 5 and 6 (non-negativity, box bounds) and accommodates additional convex penalty terms. Provide implementation examples using standard R optimization libraries (e.g., CVXR, quadprog, or similar).

<!-- Coverage: TASK_FILE line 39 ("Es posible plantear generalizar este problema matematico a un problema de optimizacion convexa? Propon la funcion de perdida que debo plantear. Dame ejemplos mediante librerias estandar de R"). Fully covered. -->

## CONSTRAINTS

- The output document must be written entirely in English, in a professional engineering methodology style.
- Mathematical expressions must use LaTeX notation ($...$ for inline, $$...$$ for display).
- All formulations must use the shared notation defined in the Context section (spectral ordinates $S_{a,k}(T_i)$, target vector $\mathbf{y}$, weight vector $\mathbf{w}$, period mesh $\{T_1, \dots, T_n\}$) to maintain consistency across slots.
