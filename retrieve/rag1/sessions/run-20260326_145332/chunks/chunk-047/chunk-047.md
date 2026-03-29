$P[a < X \leq b] = F_X(b) - F_X(a)$

Obviously, the PDF and CDF are closely related – one can be obtained from the other by integration or differentiation. The PDF and CDF of a simple probability distribution are shown in Figure D.5.

**FIGURE D.5** (a) Probability density function (PDF) and (b) Cumulative distribution function (CDF) for an arbitrary continuous random variable.

Conditional probability concepts can be extended to continuous variables. For example, if $Y$ depends on $X$ and $X$ can take on any possible value, the exceedance probability of $Y$, i.e., the probability that $Y$ exceeds some value, $y$, can be computed as

$$P[Y > y] = \int_{-\infty}^{\infty} P[Y > y \mid X]\, f_X(x)\, dx \tag{D.21}$$

Thus, the desired probability is obtained by integrating over the entire distribution of $X$.

## D.5.3 Jointly Distributed Random Variables

In some cases, the probability of more than one random variable occurring (or being exceeded) simultaneously is of interest. Such probabilities will depend not only on the distributions of the individual random variables but also on the relationships between the random variables. If two random variables, $X$ and $Y$, are continuous, their joint distribution can be described by the joint PDF defined such that

$$f_{X,Y}(x,y)\, dx\, dy = P[x < X \leq x+dx,\; y < Y \leq y+dy] \tag{D.22}$$

As in the case of a univariate PDF, a joint PDF must satisfy a number of conditions, namely that

$$f_{X,Y}(x,y) \geq 0 \tag{D.23a}$$

$$\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f_{X,Y}(x,y)\, dx\, dy = 1 \tag{D.23b}$$

$$P[a < X \leq b,\; c < Y \leq d] = \int_a^b \int_c^d f_{X,Y}(x,y)\, dx\, dy \tag{D.23c}$$

For continuous random variables, the extension of Equation (D.3) indicates conditional distributions

$$f_{X|Y}(x \mid y) = \frac{f_{X,Y}(x,y)}{f_Y(y)} \tag{D.24a}$$

$$f_{Y|X}(y \mid x) = \frac{f_{X,Y}(y,x)}{f_X(x)} \tag{D.24b}$$

from which the joint distribution can be expressed as

$$f_{X,Y}(x,y) = f_{X|Y}(x \mid y)\, f_Y(y) = f_{Y|X}(y \mid x)\, f_X(x) \tag{D.25}$$

In certain cases, it is convenient to determine an unknown joint distribution from known conditional and univariate distributions.

## D.6 MOMENTS OF A PROBABILITY DISTRIBUTION

The characteristics of a random variable are completely described by its distribution, i.e., its PMF (for a discrete random variable) or its PDF or CDF (for a continuous random variable). The description of a complete distribution can be unwieldy, and in many cases, the complete distribution may not be known; in such cases, the important characteristics of a distribution can often be described by a small number of moments of the distribution. The $k$-th moment of a probability distribution can be defined as

$$m_k = \sum_i p_i\, x_i^k \quad \text{if } X \text{ is discrete} \tag{D.26a}$$

$$m_k = \int_{-\infty}^{\infty} x^k f_X(x)\, dx \quad \text{if } X \text{ is continuous} \tag{D.26b}$$

### D.6.1 Measures of Central Tendency

Since random variables can take on a wide range of possible values, some measure of the "central" value is of interest. The mean, or expected value, of a random variable, $X$, can be computed as the first moment of $X$

$$\mu_x = \sum_i p_i\, x_i \quad \text{if } X \text{ is discrete} \tag{D.27a}$$

$$\mu_x = \int_{-\infty}^{\infty} x\, f_X(x)\, dx \quad \text{if } X \text{ is continuous} \tag{D.27b}$$

The mean, therefore, is simply the weighted average of all $X$ values, where the weighting factors are given by the PMF or PDF. Other measures of central tendency include the median, $\hat{x}$, which is the value for which there is a 50% probability of being smaller and a 50% probability of being larger, i.e., the value of the variable for which $F_X(x) = 0.5$. The mode of a random variable is the most probable single value, i.e., the value corresponding to the highest point on a PMF or PDF.

### D.6.2 Measures of Dispersion

It is also useful to know how the values of a random variable are distributed with respect to its mean value. For that reason, the second and higher moments are usually taken about the mean, i.e., as

$$m_k = \sum_i p_i\, (x_i - \mu_x)^k \quad \text{if } X \text{ is discrete} \tag{D.28a}$$

$$m_k = \int_{-\infty}^{\infty} (x - \mu_x)^k f_X(x)\, dx \quad \text{if } X \text{ is continuous} \tag{D.28b}$$

The second moment about the mean is the variance of the random variable and the square root of the variance is the standard deviation.

$$\text{Var}(X) = \sigma_x^2 = \sum_i p_i\, (x_i - \mu_x)^2 \quad \text{if } X \text{ is discrete} \tag{D.29a}$$

$$\text{Var}(X) = \sigma_x^2 = \int_{-\infty}^{\infty} (x - \mu_x)^2 f_X(x)\, dx \quad \text{if } X \text{ is continuous} \tag{D.29b}$$

Since the standard deviation has the same units as the random variable itself, the dispersion can be conveniently normalized by the mean to produce the coefficient of variation,

$$\text{COV}_x = \frac{\sigma_x}{\mu_x} \tag{D.30}$$

### D.6.3 Measures of Symmetry

The third moment can be used to define a skewness coefficient

$$\theta_X = \frac{\displaystyle\sum_i p_i\, (x_i - \mu_x)^3}{\sigma_x^3} \quad \text{if } X \text{ is discrete} \tag{D.31a}$$

$$\theta_X = \frac{\displaystyle\int_{-\infty}^{\infty} (x - \mu_x)^3 f_X(x)\, dx}{\sigma_x^3} \quad \text{if } X \text{ is continuous} \tag{D.31b}$$

A distribution for which $\theta = 0$ is symmetric; when $\theta > 0$, the distribution has a heavy positive tail and is said to be positively skewed.

### D.6.4 Measures of Association

At times, more than one random variable at a time will be of interest, frequently as input parameters to some analysis or as outputs from an analysis. It is often important to know the level to which the variables are associated with each other. The covariance of two random variables is a measure of the degree to which their values are simultaneously above or below their respective means. The covariance between two random variables, $X$ and $Y$, is defined by

$$\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)]$$

$$= \sum_i \sum_j (x_i - \mu_X)(y_j - \mu_Y)\, P_{X,Y}(x_i, y_j) \quad \text{for discrete } X \text{ and } Y \tag{D.32a}$$

$$= \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} (x - \mu_X)(y - \mu_Y)\, f_{X,Y}(x,y)\, dx\, dy \quad \text{for continuous } X \text{ and } Y \tag{D.32b}$$

Note that the covariance of a variable with itself is simply the variance of that variable. The covariance can also be computed as

$$\text{Cov}(X, Y) = E[XY] - \mu_X \mu_Y \tag{D.33}$$

It is important to distinguish between the covariance, Cov (usually written using lower-case letters), and the coefficient of variation, COV (usually written with all upper-case letters). It should be noted that the covariance between a random variable and itself is the variance of that random variable. The covariance can be normalized by the product of the standard deviations of the respective random variables, which produces the correlation coefficient.

$$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X\, \sigma_Y} \tag{D.34}$$

Figure D.6a shows an example of strong correlation between spectral accelerations ($S_a$) at closely spaced periods, while Figure D.6b shows an example of weaker correlation for $S_a$ at more widely spaced periods. The correlation coefficient ranges from $-1$ (in which case $X$ and $Y$ are linearly related with $dY/dX < 0$) to $+1$ (in which case $X$ and $Y$ are linearly related with $dY/dX > 0$). Note that the covariance (and correlation coefficient) describe the degree of linear association between two random variables. Two random variables may be uniquely related by some nonlinear function and have a low correlation coefficient (e.g., $\rho_{XY} = 0$ for $Y = \sin(X)$). The level of association between multiple random variables may be expressed in terms of a covariance matrix, which for a series of random variables, $X_1, X_2, \ldots, X_n$ would be

$$\Sigma = \begin{pmatrix} \text{Var}(X_1) & \text{Cov}(X_1,X_2) & \cdots & \text{Cov}(X_1,X_n) \\ \text{Cov}(X_2,X_1) & \text{Var}(X_2) & \cdots & \text{Cov}(X_2,X_n) \\ \vdots & \vdots & \ddots & \vdots \\ \text{Cov}(X_n,X_1) & \text{Cov}(X_n,X_2) & \cdots & \text{Var}(X_n) \end{pmatrix} \tag{D.35}$$

The corresponding correlation matrix would be

$$\rho = \begin{pmatrix} 1 & \rho_{X_1,X_2} & \cdots & \rho_{X_1,X_n} \\ \rho_{X_2,X_1} & 1 & \cdots & \rho_{X_2,X_n} \\ \vdots & \vdots & \ddots & \vdots \\ \rho_{X_n,X_1} & \rho_{X_n,X_2} & \cdots & 1 \end{pmatrix} \tag{D.36}$$

**FIGURE D.6** Scatter plots of spectral accelerations at different periods showing different levels of correlation: (a) $T = 0.25$ sec vs. $T = 0.20$ sec, which are highly correlated ($\rho = 0.97$) and (b) $T = 1.00$ sec vs. $T = 0.20$ sec, which are more weakly correlated ($\rho = 0.71$). All data from NGA database for sites with $V_{S30} > 500$ m/s.

### D.6.5 Confidence Intervals

The moments of a set of data can be computed for very small samples of data from a large population – only a single data point is required, for example, to compute a mean. Of course, one would logically be concerned about how well that estimated sample mean would correspond to the population mean. Consider a set of random samples from some large population, $X$, that is normally distributed with mean, $\mu_x$, and standard deviation, $\sigma_x$. The sample values, $x_1, x_2, \ldots, x_n$ can be thought of as single realizations from a set of independent, identically distributed random variables, $X_1, X_2, \ldots, X_n$. Therefore, the sample mean

$$\bar{X} = \frac{1}{n} \sum_{i=1}^{n} x_i \tag{D.37}$$

is itself a random variable with an expected value

$$E[\bar{X}] = \frac{1}{n} \sum_{i=1}^{n} \mu_x = \mu_x \tag{D.38}$$

This indicates that the expected value of the sample mean is equal to the population mean, so $\bar{X}$ is an unbiased estimator of $\mu_x$. The uncertainty in $\bar{X}$ may be of considerable interest; the variance of $\bar{X}$ is

$$\text{Var}(\bar{X}) = \text{Var}\!\left(\frac{1}{n}\sum_{i=1}^{n} x_i\right) = \frac{1}{n^2}\sum_{i=1}^{n} \text{Var}(x_i) = \frac{\sigma_x^2}{n} \tag{D.39}$$

Thus $\bar{X}$ is normally distributed with mean $\mu_x$ and standard deviation $\sigma_x / \sqrt{n}$. This result clearly indicates that the estimate of the population mean improves with increasing sample size, $n$. In most situations, the population variance, $\sigma_x^2$, is not known and must be estimated from the sample variance

$$s_x^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{X})^2 \tag{D.40}$$

When this is the case, the random variable $(\bar{X} - \mu_x) / (s_x / \sqrt{n})$ will not be normally distributed, particularly if $n$ is small. Instead, that variable will have the Student's $t$-distribution with $n - 1$ degrees of freedom, which can be written as

$$f_T(t) = \frac{\Gamma\!\left(\frac{f+1}{2}\right)}{\sqrt{\pi f}\;\Gamma\!\left(\frac{f}{2}\right)} \left(1 + \frac{t^2}{f}\right)^{-(f+1)/2} \tag{D.41}$$

where $f$ is the number of degrees of freedom and $\Gamma(\cdot)$ is the gamma function (values of the Student's $t$-distribution are generally looked up in published tables). The Student's $t$-distribution approaches the standard normal distribution as $f \to \infty$ and the two are very nearly the same for $f > 50$. For smaller numbers of degrees of freedom, the Student's $t$-distribution is bell-shaped but somewhat flatter/broader than the standard normal distribution. Then, the probability that the mean falls within certain bounds can be obtained from

$$P[t_{\alpha/2,\, n-1} < T \leq t_{1-\alpha/2,\, n-1}] = 1 - \alpha \tag{D.42}$$

where $T = (\bar{X} - \mu_x) / (s_x / \sqrt{n})$ and $t_{\alpha/2,\, n-1}$ and $t_{1-\alpha/2,\, n-1}$ are the lower and upper critical values of the $t$-distribution with $n - 1$ degrees of freedom at probabilities of $\alpha/2$ and $1 - \alpha/2$. Alternatively, we can say that the confidence interval for $\mu_x$ is

$$\bar{x} \pm t_{1-\alpha/2,\, n-1} \cdot \frac{s_x}{\sqrt{n}} \tag{D.43}$$

#### Example D.6

A set of 10 SPT measurements were made at the same depth in a particular layer of sand. The sample mean and standard deviation were computed as 15 and 3.5, respectively. Over what interval would one have a 95% confidence of capturing the actual (population) mean?

**Solution:**

Using a Student's $t$-distribution table, the lower and upper critical values would be $t_{0.025,9} = -2.2622$ and $t_{0.975,9} = +2.2622$. Using the definition of $T$, the 95% confidence interval would be

$$P\!\left[\mu_x \in \left(15 - \frac{2.2622 \times 3.5}{\sqrt{10}};\; 15 + \frac{2.2622 \times 3.5}{\sqrt{10}}\right)\right] = 0.95 \implies [12.5;\; 17.5]$$

If 20 measurements produced the same sample mean and standard deviation, the 95% confidence interval would be

$$P\!\left[\mu_x \in \left(15 - \frac{2.0930 \times 3.5}{\sqrt{20}};\; 15 + \frac{2.0930 \times 3.5}{\sqrt{20}}\right)\right] = 0.95 \implies [13.4;\; 16.6]$$

The increased number of tests has not changed the estimated mean, but they have narrowed the confidence interval significantly. Note that these confidence intervals correspond to the mean – the individual data can extend well beyond these intervals.

## D.7 COMMON PROBABILITY DISTRIBUTIONS

The results of statistical experiments often exhibit the same general type of behavior. As a result, the random variables associated with those experiments can be described by essentially the same PDF. Many PDFs exist, but only a few are required for the geotechnical earthquake engineering analyses described in this book.

### D.7.1 Discrete Distributions

Earthquake engineers typically deal with quantities such as force, mass, displacement, and acceleration that are measured on continuous scales. Discrete random variables usually appear in counting processes, where the number of occurrences of some event or condition is noted, or when some continuous region is divided into a finite number of sub-regions.

#### D.7.1.1 Uniform Distribution

The simplest probability distribution is one in which all possible values of the random variable are equally likely. Such a random variable is described by a uniform distribution. The PMF for a discrete random variable, $X$, with $n$ values uniformly distributed and equally spaced over the interval between two values $a$ and $b$ is

$$P_X(x) = \begin{cases} 0 & x < a \\ \dfrac{1}{n} & a \leq x \leq b \\ 0 & x > b \end{cases} \tag{D.44}$$

The first three moments of the PMF are

$$\mu_x = \frac{a + b}{2} \tag{D.45a}$$

$$\sigma_x = \frac{-(b - a + \cdots)}{\cdots} \tag{D.45b}$$

$$\theta = 0 \tag{D.45c}$$

#### D.7.1.2 Poisson Distribution

A Poisson distribution describes the probability of events that follow a Poisson process, i.e., one that yields values of a random variable describing the number of occurrences of a particular event in a specified time interval (or spatial region). Poisson processes have the following properties:

1. The number of occurrences in one time interval is independent of the number that occurs in any other time interval.
2. The probability of occurrence during a very short time interval is proportional to the length of the time interval.
3. The probability of more than one occurrence during a very short time interval is negligible.

If $\alpha$ is the average number of occurrences of the event of interest in a particular time interval, the number of occurrences in that interval will occur with probabilities

$$P[N = n] = \frac{\alpha^n e^{-\alpha}}{n!} \tag{D.46}$$

The first three moments of the PMF are

$$\mu_N = \alpha \tag{D.47a}$$

$$\sigma_N^2 = \alpha \tag{D.47b}$$

$$\theta_N = \alpha^{-1/2} \tag{D.47c}$$

If the events are characterized as occurring at a rate, $\lambda$, such that $\lambda t = \alpha$, then the probability in a time interval, $t$, can be expressed as

$$P[N = n] = \frac{(\lambda t)^n e^{-\lambda t}}{n!} \tag{D.48}$$

### D.7.2 Continuous Distributions

Most of the quantities dealt with by geotechnical earthquake engineers are measured on continuous scales. Many continuous distributions are available, but only a small number are commonly encountered in geotechnical earthquake engineering practice.

#### D.7.2.1 Uniform Distribution

The continuous uniform distribution is of similar form to its discrete counterpart with a PDF and CDF of the form

$$f_X(x) = \begin{cases} 0 & x < a \\ \dfrac{1}{b - a} & a \leq x \leq b \\ 0 & x > b \end{cases} \tag{D.49a}$$

$$F_X(x) = \begin{cases} 0 & x < a \\ \dfrac{x - a}{b - a} & a \leq x \leq b \\ 1 & x > b \end{cases} \tag{D.49b}$$

The first three moments of the uniform distribution are

$$\mu_x = \frac{a + b}{2} \tag{D.50a}$$

$$\sigma_x = \frac{b - a}{\cdots} \tag{D.50b}$$

$$\theta = 0 \tag{D.50c}$$
