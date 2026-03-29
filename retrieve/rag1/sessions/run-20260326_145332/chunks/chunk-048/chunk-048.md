### D.7.2.2 Normal Distribution

The most commonly used probability distribution in statistics is the normal distribution (or Gaussian distribution). Its PDF, which plots as the familiar bell-shaped curve of Figure D.5a, describes sets of data produced by a wide variety of physical processes. The normal distribution is completely defined by two parameters: the mean and standard deviation. Mathematically, the PDF of a normally distributed random variable $X$ is given by

$$f_X(x) = \frac{1}{\sigma_x \sqrt{2\pi}} \exp\!\left(-\frac{(x - \mu_x)^2}{2\sigma_x^2}\right), \quad -\infty < x < \infty \tag{D.51}$$

The PDF and CDF for a normal distribution are illustrated in Figure D.5. Examples of normal PDFs for random variables with different means and standard deviations are shown in Figure D.7. Integration of the PDF of the normal distribution does not produce a simple expression for the CDF, so values of the normal CDF are usually expressed in tabular form. The normal CDF is most efficiently expressed in terms of the standard normal variable, which can be computed for any random variable $X$ using the transformation

$$Z = \frac{x - \mu_X}{\sigma_x} \tag{D.52}$$

Whenever $X$ has a value, $x$, the corresponding value of $Z$ is $z = (x - \mu_x)/\sigma_x$. Thus, the mean value of $Z$ is $\mu_z = 0$ and the standard deviation is $\sigma_z = 1$. Tabulated values of the standard normal CDF are presented in Table D.1.

**Figure D.7** Normal distribution: (a) different means and same standard deviation, (b) same mean and different standard deviations.

**Table D.1** Values of the CDF of the Standard Normal Distribution, $F_Z(z) = 1 - F_Z(-z)$

z: 0.00 0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09

−3.4: 0.0003 0.0003 0.0003 0.0003 0.0003 0.0003 0.0003 0.0003 0.0003 0.0002
−3.3: 0.0005 0.0005 0.0005 0.0004 0.0004 0.0004 0.0004 0.0004 0.0004 0.0003
−3.2: 0.0007 0.0007 0.0006 0.0006 0.0006 0.0006 0.0005 0.0005 0.0005 0.0005
−3.1: 0.0010 0.0009 0.0009 0.0009 0.0008 0.0008 0.0008 0.0008 0.0007 0.0007
−3.0: 0.0013 0.0013 0.0013 0.0012 0.0012 0.0011 0.0011 0.0011 0.0010 0.0010
−2.9: 0.0019 0.0018 0.0017 0.0017 0.0016 0.0016 0.0015 0.0015 0.0014 0.0014
−2.8: 0.0026 0.0025 0.0024 0.0023 0.0023 0.0022 0.0021 0.0021 0.0020 0.0019
−2.7: 0.0035 0.0034 0.0033 0.0032 0.0031 0.0030 0.0029 0.0028 0.0027 0.0026
−2.6: 0.0047 0.0045 0.0044 0.0043 0.0041 0.0040 0.0039 0.0038 0.0037 0.0036
−2.5: 0.0062 0.0060 0.0059 0.0057 0.0055 0.0054 0.0052 0.0051 0.0049 0.0048
−2.4: 0.0082 0.0080 0.0078 0.0075 0.0073 0.0071 0.0069 0.0068 0.0066 0.0064
−2.3: 0.0107 0.0104 0.0102 0.0099 0.0096 0.0094 0.0091 0.0089 0.0087 0.0084
−2.2: 0.0136 0.0139 0.0132 0.0129 0.0125 0.0122 0.0119 0.0116 0.0113 0.0110
−2.1: 0.0179 0.0174 0.0170 0.0166 0.0162 0.0158 0.0154 0.0150 0.0146 0.0143
−2.0: 0.0228 0.0222 0.0217 0.0212 0.0207 0.0202 0.0197 0.0192 0.0188 0.0183
−1.9: 0.0287 0.0281 0.0274 0.0268 0.0262 0.0256 0.0250 0.0244 0.0239 0.0233
−1.8: 0.0359 0.0352 0.0344 0.0336 0.0329 0.0322 0.0314 0.0304 0.0301 0.0294
−1.7: 0.0446 0.0436 0.0427 0.0418 0.0409 0.0401 0.0392 0.0384 0.0375 0.0367
−1.6: 0.0548 0.0537 0.0526 0.0516 0.0505 0.0495 0.0485 0.0475 0.0465 0.0455
−1.5: 0.0668 0.0655 0.0643 0.0630 0.0618 0.0606 0.0594 0.0582 0.0571 0.0559
−1.4: 0.0808 0.0793 0.0778 0.0764 0.0749 0.0735 0.0722 0.0708 0.0694 0.0681
−1.3: 0.0968 0.0951 0.0934 0.0918 0.0901 0.0885 0.0859 0.0853 0.0838 0.0823
−1.2: 0.1151 0.1131 0.1112 0.1093 0.1075 0.1056 0.1038 0.1020 0.1003 0.0985
−1.1: 0.1357 0.1335 0.1314 0.1292 0.1271 0.1251 0.1230 0.1210 0.1190 0.1170
−1.0: 0.1587 0.1562 0.1539 0.1515 0.1492 0.1469 0.1446 0.1423 0.1401 0.1379
−0.9: 0.1841 0.1814 0.1788 0.1762 0.1736 0.1711 0.1685 0.1660 0.1635 0.1611
−0.8: 0.2119 0.2090 0.2001 0.2033 0.2005 0.1977 0.1949 0.1922 0.1894 0.1867
−0.7: 0.2420 0.2389 0.2358 0.2327 0.2296 0.2266 0.2236 0.2206 0.2177 0.2148
−0.6: 0.2743 0.2709 0.2676 0.2043 0.2611 0.2578 0.2546 0.2514 0.2483 0.2451
−0.5: 0.3085 0.3050 0.3015 0.2981 0.2946 0.2912 0.2877 0.2843 0.2810 0.2776
−0.4: 0.3446 0.3409 0.3372 0.3336 0.3300 0.3264 0.3228 0.3192 0.3156 0.3121
−0.3: 0.3821 0.3783 0.3745 0.3707 0.3669 0.3032 0.3594 0.3557 0.3520 0.3483
−0.2: 0.4013 0.3974 0.3936 0.3897 0.3859 0.4207 0.4168 0.4129 0.4090 0.4052
−0.1: 0.4602 0.4562 0.4522 0.4483 0.4443 0.4404 0.4365 0.4325 0.4286 0.4247
−0.0: 0.5000 0.4960 0.4920 0.4880 0.4840 0.4801 0.4761 0.4721 0.4681 0.4641

Table D.1 shows that 15.87% of a normally distributed random variable's values are more than one standard deviation above the mean, and an equal fraction are more than one standard deviation below the mean. This means that 68.26% of the values are within one standard deviation of the mean; similarly, 95.44% of the values would be within two standard deviations of the mean.

### Example D.6

Given a normally distributed random variable, $X$, with $\mu_x = 270$ and $\sigma_x = 40$, compute the probabilities that (a) $X < 300$, $X > 350$, and (c) $200 < X < 240$.

### Solution:

The required probabilities can be determined with the aid of Table D.1 after conversion to standard normal variables.

a. For $X = 300$:

$$Z = \frac{x - \mu_X}{\sigma_x} = \frac{300 - 270}{40} = 0.75$$

Then $P[X < 300] = P[Z < 0.75] = 1 - F_Z(-0.75) = 1 - 0.2266 = 0.7734$.

b. For $X = 350$:

$$Z = \frac{x - \mu_X}{\sigma_x} = \frac{350 - 270}{40} = 2.0$$

Then $P[X > 350] = P[Z > 2.0] = 1 - F_Z(2.0) = F_Z(-2.0) = 0.0228$.

c. For $X = 200$:

$$Z = \frac{x - \mu_X}{\sigma_x} = \frac{200 - 270}{40} = -1.75$$

and for $X = 240$:

$$Z = \frac{x - \mu_X}{\sigma_x} = \frac{240 - 270}{40} = -0.75$$

Then $P[200 < X < 240] = P[-1.75 < Z < -0.75] = F_Z(-0.75) - F_Z(-1.75) = 0.2266 - 0.0401 = 0.1865$.

### D.7.2.3 Lognormal Distribution

Some problems, particularly those involving ground motion parameters (Chapter 3), are formulated in terms of the logarithm of a parameter rather than the parameter itself. If $X$ is a random variable, then $Y = \ln X$ is also a random variable. If $Y$ is normally distributed, then $X$ is lognormally distributed. In other words, a random variable is lognormally distributed if its logarithm is normally distributed. The PDF of a lognormally distributed random variable $X$ is given by

$$f_X(x) = \frac{1}{x\,\sigma_{\ln x}\sqrt{2\pi}} \exp\!\left(-\frac{(\ln x - \mu_{\ln x})^2}{2\sigma_{\ln x}^2}\right), \quad 0 \leq x < \infty \tag{D.53a}$$

or, letting $\lambda_X = \mu_{\ln X}$ and $\zeta_X = \sigma_{\ln X}$:

$$f_X(x) = \frac{1}{x\,\zeta_X\sqrt{2\pi}} \exp\!\left(-\frac{(\ln x - \lambda_X)^2}{2\zeta_X^2}\right), \quad 0 \leq x < \infty \tag{D.53b}$$

The shape of the lognormal distribution is shown in Figure D.8. Note that the lognormal distribution assigns zero probability to negative values of the random variable. These characteristics can be very useful for some random variables [the normal distribution, for example, assigns nonzero probabilities for values ranging from $-\infty$ to $+\infty$; when applied to a random variable with a relatively high COV, it can assign some probability that the variable will have a negative value. For a parameter such as undrained shear strength, which may have a COV on the order of 35% [@PhoonKulhawy1999], a normal distribution would imply a 0.2% probability (low, but potentially significant for design purposes where low probabilities of failure are of interest) that the undrained strength is negative, a result that is physically meaningless. It should also be noted that the lognormal distribution is skewed and that the amount of skew increases with increasing $\sigma_{\ln X}$. Values of the CDF of the lognormal distribution are usually obtained from Table D.1, using the modified transformation

$$Z = \frac{\ln x - \mu_{\ln X}}{\sigma_{\ln X}} = \frac{\ln x - \lambda_X}{\zeta_X} \tag{D.54}$$

It therefore follows that the median and mean values of a lognormal distribution are given by

$$\hat{X} = \exp(\lambda_X) = \exp(\mu_{\ln X}) \tag{D.55a}$$

$$\mu_X = \exp\!\left(\lambda_X + \frac{\zeta_X^2}{2}\right) \tag{D.55b}$$

Equation (D.55) indicates that the mean of a lognormally distributed random variable is always greater than the median. The values of $X$ corresponding to common percentiles are given by

$$x_{+1\sigma} = \exp(\lambda_X + \zeta_X) = \mu_X \exp(\sigma_{\ln X}) \tag{D.56a}$$

$$x_{-1\sigma} = \exp(\lambda_X - \zeta_X) = \mu_X \exp(-\sigma_{\ln X}) \tag{D.56b}$$

**Figure D.8** Lognormal distribution. Note that degree of asymmetry increases with increasing $\sigma_{\ln X}$.

A lognormally distributed random variable with $\zeta = \sigma_{\ln X} = \alpha$ would have 68% of its values within a factor of $e^\alpha$ of its median value.

### Example D.7

A random variable, $X$, is lognormally distributed with $\lambda = 5$ and $\zeta = 1.2$. Compute (a) the probability that $X < 100$, and (b) the value of $X$ that has a 10% probability of being exceeded.

### Solution:

As in the previous example, (a) for $X = 100$:

$$Z = \frac{\ln 100 - \lambda_X}{\zeta_X} = \frac{\ln 100 - 5}{1.2} = -0.33$$

From Table D.1, $P[X < 100] = P[Z < -0.33] = F_Z(-0.33) = 0.3707$.

For (b), Table D.1 indicates that the value of $Z$ that would have a 10% probability of exceedance is 1.282, i.e., $F_Z(1.282) = 0.90$. Then, rearranging Equation (D.52) yields

$$\ln X = \lambda_X + \zeta_X Z = 5 + (1.282)(1.2) = 6.54$$

so $X = e^{6.54}$.

### D.7.2.4 Exponential Distribution

The exponential distribution is often used to model random variables in which small values occur more frequently than higher values. A common application in earthquake engineering is to model the distribution of earthquake magnitudes. It can also be used to model the time elapsed between events – in particular, it represents the probability distribution of the time between events in a Poisson process. A continuous random variable, $X$, is exponentially distributed with rate parameter, $\alpha$, if its PDF is given by

$$f_X(x) = \begin{cases} \alpha\, e^{-\alpha x} & x > 0 \\ 0 & x \leq 0 \end{cases} \tag{D.57}$$

The PDF of an exponential distribution with different rate parameter values is shown in Figure D.9. The CDF of an exponential distribution is given by

$$F_X(x) = \begin{cases} 1 - e^{-\alpha x} & x > 0 \\ 0 & x \leq 0 \end{cases}$$

**Figure D.9** PDFs for exponential distribution with rate parameters of 0.5, 1.0, and 2.0.

and the first three moments are

$$\mu_x = \frac{1}{\alpha} \tag{D.58a}$$

$$\sigma_x = \frac{1}{\alpha} \tag{D.58b}$$

$$\theta_3 = \frac{2}{\alpha^3} \tag{D.58c}$$

### D.7.2.5 Joint Normal Distribution

The normal distribution can be extended to multiple random variables. Two random variables, $X$ and $Y$, that are joint normally distributed have a joint probability density function

$$f_{XY}(x,y) = \frac{1}{2\pi\sigma_X\sigma_Y\sqrt{1-\rho_{XY}^2}} \exp\!\left(-\frac{a}{2(1-\rho_{XY}^2)}\right) \tag{D.59}$$

where

$$a = \frac{(x-\mu_X)^2}{\sigma_X^2} - \frac{2\rho_{XY}(x-\mu_X)(y-\mu_Y)}{\sigma_X\sigma_Y} + \frac{(y-\mu_Y)^2}{\sigma_Y^2}$$

Note that the shape of the PDF is influenced by the correlation between $X$ and $Y$. Figure D.10 shows joint normal distributions for two correlation coefficients. The conditional PDF of $Y$ given $X = x$ is given by

$$f_{Y|X}(y|x) = \frac{1}{\sigma_Y\sqrt{1-\rho_{XY}^2}\,\sqrt{2\pi}} \exp\!\left(-\frac{\bigl(y - \mu_Y - \rho_{XY}(\sigma_Y/\sigma_X)(x-\mu_X)\bigr)^2}{2\sigma_Y^2(1-\rho_{XY}^2)}\right) \tag{D.60}$$

which indicates that the conditional PDF is normal with

$$\mu_{Y|X=x} = \mu_Y + \rho_{XY}\frac{\sigma_Y}{\sigma_X}(x - \mu_X) \tag{D.61a}$$

$$\sigma_{Y|X=x} = \sigma_Y\sqrt{1 - \rho_{XY}^2} \tag{D.61b}$$

**Figure D.10** Illustration of joint normal PDFs with (a) $\rho_{XY} = 0$ and (b) $\rho_{XY} = 0.7$. For both cases, $\mu_X = 10$, $\sigma_X = 3$, $\mu_Y = 15$, $\sigma_Y = 4$.

### D.8 RANDOMNESS AND UNCERTAINTY

In hazard analysis and performance-based earthquake engineering, it is important to understand the various sources of uncertainty that can contribute to the uncertainty in performance predictions. The terms "randomness" and "uncertainty" are often used in a colloquial manner to cover a range of sources of variability or uncertainty, and it is sometimes necessary to break them down into specific categories. Randomness, which is frequently described by the term aleatory variability, refers to the inherent or intrinsic variability of some quantity or phenomenon; as a result, it cannot be reduced by additional data or through more investigation. Randomness can manifest itself, for example, in the variability of response produced by different ground motions, even when scaled to the same level of intensity. This record-to-record variability, which results from the apparently random, unpredictable nature of earthquakes, is a very significant component of the overall uncertainty in a seismic performance evaluation. Uncertainty due to lack (or ignorance) of data or knowledge concerning a quantity or phenomenon is frequently referred to as epistemic uncertainty. Epistemic uncertainty differs from aleatory uncertainty in that it can be reduced by the acquisition of new information, e.g., by additional data, more extensive investigation, or by new research. Aleatory variability and epistemic uncertainty are handled differently in probabilistic performance-based earthquake engineering analyses and are discussed with respect to several topics within this text. The distinction between aleatory and epistemic uncertainties can be difficult, ambiguous, and confusing. In practice, the distinction can depend on pragmatic as well as theoretical factors. While arguments can be made that all uncertainty is epistemic, practical considerations require that some be treated as aleatory; one could, for example, gain knowledge of the inherent variability of a natural soil deposit by drilling and sampling the entire site with boreholes on a 6-inch spacing – an action so obviously impractical (and destructive) that it illustrates why such variability is treated as aleatory. The assignment of aleatory vs. epistemic can also be situation-dependent. For example, suppose the shear wave velocity profile at a soil site has been measured using multiple defensible methods (e.g., downhole, suspension logging, surface wave inversions). Differences between these measured profiles are epistemic because the knowledge to identify which individual profile, or which combination of profiles, represents the "true" condition is lacking. Suppose one-dimensional ground response analyses are to be performed at this site. Such analyses assume laterally continuous layers with constant properties, which is never the case in natural soils. The inevitable heterogeneities that cause variations in the shear wave velocity profile, which cannot be accurately captured in one-dimensional analyses, are effectively irreducible and random and are generally considered to be aleatory. The nature of the models used to predict performance will also affect the aleatory-epistemic distinction. All predictive models should be recognized as mathematical idealizations of reality – they are not perfect. Model uncertainty, i.e., errors in model predictions, has two primary components: (1) the effect of missing predictive variables, and (2) the effects of inaccurate model form. Missing variables may be those not recognized as being influential or those that cannot be measured or otherwise characterized. Inaccurate model form may result from practical consideration of computational complexity/effort or lack of understanding of the basic physics of the problem. For example, one-dimensional site response analyses are commonly used in engineering practice even though waves other than the vertically propagating shear waves assumed by those analyses are known to exist at nearly all sites. Both components of model uncertainty can potentially be reduced, by including additional predictive variables and/or the use of improved mathematical expressions, but there will usually be a limit to the number of variables that can be identified and/or measured or to the understanding of the physics of the problem of interest that will limit the degree to which uncertainty can be reduced. Therefore, model uncertainty will generally have both aleatory and epistemic components. The fact that different models are frequently of different forms and use different predictive variables means that they will predict different output values. The variability of mean (or median) predictions from different plausible models, therefore, represents another component of epistemic uncertainty. To properly account for epistemic uncertainty in response, multiple predictive models, where available, should also be used with their results combined using a logic tree where the weights assigned to the branches reflect judgments of the relative merits of the alternative models. It should be recognized, however, that the branches of a logic tree are those thought to be relevant by its developer and they may be incomplete if some unrecognized (hence ignored) but relevant physical mechanism is not included [@Stafford2015]; this form of uncertainty (due to "unknown unknowns") is known as ontological uncertainty (e.g., [@MarzocchiJordan2014]). Even when only the mean response is being used, however, it is still useful to consider which components of uncertainty can and cannot be reduced and to also consider the costs and benefits of doing so. Increasing uncertainty tends to drive the ground motions, response, damage, and losses for a given return period higher in a performance-based evaluation. The ability to show the benefits of increased investment, for example, in additional subsurface investigation or more sophisticated response modeling, represents a tremendous opportunity for geotechnical earthquake engineering practitioners. More detailed treatments of randomness and uncertainty in hazard analysis and earthquake engineering can be found in [@PateCornell1996], [@AbrahamsonBommer2005], [@Faber2005], [@DerKiureghianDitlevsen2009], and [@Stafford2015], and [@BakerEtAl2021].

### D.9 PROPAGATION OF VARIABILITY/UNCERTAINTY

Engineers are frequently interested in how the uncertainty in inputs affects uncertainty in the corresponding output of some analysis or process. Since the output may be required for design, or as input to further analyses, it is necessary to characterize the uncertainty in the output. In its simplest sense, the problem becomes one of computing the uncertainty in a function of one or more random variables given the uncertainty in the random variables themselves. In the discussion that follows, the propagation of uncertainty will be discussed in the framework of a response model (Figure D.11) into which one or more input variables are applied to produce a response variable. The intent of this section is not to present all methods by which uncertainties can be propagated but rather to provide the reader with some intuitive "feel" for how uncertainties work their way through problems likely to be encountered in earthquake engineering practice.

**Figure D.11** Propagation of uncertainty.

### D.9.1 Sensitivity Analysis and Tornado Diagrams

Before undertaking a detailed probabilistic analysis, it can be useful to investigate the sensitivity of the output of interest to the various input parameters used in a predictive model. Sensitivity analyses can be used to determine the relative importance of the inputs and to identify inputs for which errors or changes could significantly affect the model predictions and conclusions drawn from them. The simplest form of a sensitivity analysis involves permuting each of the inputs individually by ± some common percentage (e.g., 10%) of their expected value. The sensitivity is indicated by the range of the computed output values (the "swing") for each permuted input parameter. A more informative analysis can be performed by tying the degree of the parameter permutation to the uncertainty/variability of the input parameter. In a tornado diagram analysis, the mean value of each input is individually permuted by the same fraction of its standard deviation (e.g., $\mu \pm p\sigma$ where $p$ would typically be 0.5 or 1.0). In this manner, the swing is influenced by both the sensitivity of the output to each input and the uncertainty in the input. The values of the output are then tabulated for each parameter and arranged graphically (Figure ED.8b) in order of their swing (highest on top) centered on the output value obtained with all inputs set to their mean values. Note that a high sensitivity to a parameter with low uncertainty, or a high uncertainty in a parameter to which the output is not sensitive, will produce a low swing. Input parameters with a high swing, particularly when produced by high uncertainty, may benefit from more detailed exploration or testing in order to reduce that uncertainty.

### Example D.8

The ultimate settlement of a slightly overconsolidated soft clay site to be readied for development by placement of 5 ft of fill material is of interest. The site conditions, shown below, indicate the presence of a crust of desiccated clay with thickness, $h_1$, which is not expected to consolidate noticeably. The clay is underlain by a dense gravel, which will also not consolidate (Figure ED.8a). A subsurface investigation revealed the properties shown in the table below. Many of the properties are uncertain, either due to scatter in the data from which they were developed, or due to the judgment of the engineers who were involved in the acquisition of the data. Nevertheless, the uncertainty associated with each property is indicated in the table and each is normally distributed. Construct a tornado diagram to show the sensitivity of settlement to variations in the tabulated input variables.

**Figure ED.8A** Site profile considered in Example D.8.

Parameter mean values and COV (%):

$h_1$ = 3 ft; $h_2$ = 25 ft; $C_c$ = 0.75; $e_0$ = 1.54; $C_r$ = 0.05; $\sigma'_p$ and $\sigma'_v$ = 200 psf; $\gamma_\text{fill}$ = 130 pcf; $h_\text{fill}$ = 5 ft.

### Solution:

The tornado diagram is constructed by first calculating the ultimate settlement using the mean values of all input parameters – in this case, that settlement is 17.37 inches. The higher and lower values of each input parameter are then obtained by adding and subtracting one standard deviation from its mean value. The settlements are then calculated by changing the value of each parameter to its higher and then lower value while holding all other parameters at their mean values, as tabulated below.

Parameter: $\mu - \sigma$ / $\mu + \sigma$ / $\Delta H_{\mu-\sigma}$ / $\Delta H_{\mu+\sigma}$ / |Swing|

$h_1$: 2.85 / 3.15 / 17.53 / 17.21 / 0.32
$h_2$: 23.75 / 26.25 / 16.82 / 18.69 / 1.87
$C_c$: 0.60 / 0.90 / 14.05 / 20.70 / 6.65
$e_0$: 1.43 / 1.65 / 17.67 / 17.08 / 0.59
$C_r$: 0.04 / 0.06 / 17.22 / 17.52 / 0.30
$\sigma'_p$: — / — / 22.14 / 13.23 / 8.91
$\gamma_\text{fill}$: 120.9 / 139.1 / 16.00 / 18.69 / 2.69
$h_\text{fill}$: 4.9 / 5.1 / 16.98 / 17.75 / 0.77

The computed settlements are then shown graphically, from top to bottom, in order of highest to lowest absolute swing as illustrated in Figure ED.8b. For this example, the amount by which the soft clay is overconsolidated is the most influential input parameter followed closely by the compression index, $C_c$.

**Figure ED.8B** Tornado diagram indicating sensitivities of settlement to variations of input parameters.

These results indicate that additional consolidation testing to reduce uncertainty in the preconsolidation pressure, $\sigma'_p$, and compression index, $C_c$, may be the most efficient way to reduce uncertainty in the computed settlement.

### D.9.2 Functions of Random Variables – Analytical Solutions

When a function of one or more random variables (i.e., a response model) is relatively simple, the uncertainty of the response variable can be expressed in terms of the uncertainties of the input variables in closed form. While nearly all practical problems are too complicated to allow an analytical solution, the analytical solution offers useful insight into general uncertainty propagation behavior.

### D.9.2.1 Single Input Variable

In certain cases, a response parameter may be a function of a single input parameter, or a function of multiple parameters of which only one is uncertain. If the uncertain parameter is described by the random variable, $X$, and the response by the random variable, $Y$, the response model can be expressed as $Y = g(X)$. The inverse response function (which gives the input parameter that produces a particular level of response) can be expressed as $X = g^{-1}(Y)$. For a monotonically increasing function (i.e., increases in $X$ produce increases in $Y$ for all $x$), the probability that $Y$ is less than or equal to some value, $y$, is equal to the probability that $X$ is less than or equal to the corresponding value of $x$, i.e.,

$$P[Y \leq y] = P\!\left[X \leq g^{-1}(y)\right] \tag{D.62}$$

The probability that $Y$ is between $y$ and $y + dy$, then is equal to the probability that $X$ is between the corresponding $x$ and $x + dx$, which means that

$$f_Y(y) = f_X(x)\left|\frac{dx}{dy}\right| \tag{D.63}$$

where the absolute value is required to ensure positive values of the PDF when $Y$ is a decreasing function of $X$. These relationships show that a response model that is simple enough to be analytically inverted and then differentiated can allow exact determination of the entire distribution of the response parameter if the distribution of the input parameter is known. More importantly, it succinctly illustrates an important characteristic of uncertainty propagation: uncertainty in the output depends on both the uncertainty in the input (represented by spread of the $f_X(x)\,dx$ term in Equation D.63) and the sensitivity of the output to the input (inverse of the $dy/dx$ term). If the uncertainty in an input variable is small, its probability densities will be large, which will produce large response probability densities $f_Y(y)$ per Equation (D.63); this indicates that variability in $x$ does not contribute much to uncertainty in the output. Similarly, if the uncertainty in the input is high (low values of $f_X(x)$) but the sensitivity of the output to the input is very low (very low $dy/dx$ and very high $dx/dy$), large response probability densities will again occur per Equation (D.63), indicating that variable does not contribute much to uncertainty in the output.

**Linear Function**

When the response model is linear, the moments of the response variable can be related to those of the input variable in a simple manner. Suppose

$$Y = a + bX \tag{D.64}$$

where the intercept, $a$, and the gradient (slope), $b$, are known constants. Then $g^{-1}(y) = (y - a)/b$, which means that $dx/dy = 1/b$. Then, the PDF of $Y$ can be expressed, using Equation (D.63), as

$$f_Y(y) = \frac{1}{|b|}\,f_X\!\left(\frac{y-a}{b}\right) \tag{D.65}$$

**Figure D.12** Effect of a linear function on the propagation of uncertainty from $X$ to $Y$.

It can further be shown for the linear model that

$$\mu_Y = a + b\mu_X \tag{D.66a}$$

$$\sigma_Y = |b|\,\sigma_X \tag{D.66b}$$

Figure D.12 graphically illustrates the relationship between $f_X(x)$ and $f_Y(y)$ when $Y$ is a linear function of $X$. The shaded areas represent the probability that $X$ is between the values at the left and right boundaries of the shaded area. That probability is equal to the probability that $Y$ is between the corresponding values on the $Y$-axis, i.e. $f_X(x)\,dx = f_Y(y)\,dy$, which means that $f_Y(y) = f_X(x)\,dx/dy$. In Figure D.12, the probabilities are equal, so the shaded areas must be equal. Because the slope of the line is relatively flat, $dy < dx$, so the corresponding value of $f_Y(y)$ must be greater than that of $f_X(x)$. So for a linear model, the form of the distribution of $Y$ will be the same as that of $X$ (e.g., if $X$ is normally distributed, $Y$ will also be normally distributed). The mean of $Y$ is obtained by plugging the mean of $X$ into the model, and the standard deviation of $Y$ is equal to the standard deviation of $X$ multiplied by the slope of the linear model, $b$. Note that $\sigma_Y$ depends on $\sigma_X$ and the sensitivity of $Y$ to $X$, as captured by the gradient, $b$.

**Nonlinear Function**

When the response model is nonlinear, the gradient is not constant and, hence, the form of the $Y$ distribution will be different than that of the $X$ distribution. Figure D.13 illustrates the relationship graphically. Because $Y$ increases monotonically with $X$, the probability that $X$ is between two particular values of $X$ is equal to the probability that $y$ is between the corresponding values of $Y$, as in Equation (D.62). Hence, as in the linear case, the shaded areas, $A_1$, are equal as are the areas, $A_2$. The variable gradient, however, causes the shape of $f_X(x)$ to differ from that of $f_Y(y)$.

### D.9.2.2 Multiple Input Variables

The propagation of uncertainty becomes more complicated when the response variable is a function of more than one random variable. Closed-form analytical solutions can be obtained only for a limited number of special cases. Consider the general case where $Y = g(X_1, X_2)$ and $X_1$ and $X_2$ are jointly distributed with the pdf $f_{X_1 X_2}(x_1, x_2)$. If $X_1$ and $X_2$ are continuous, then

$$F_Y(y) = \iint_{g(x_1,x_2) < y} f_{X_1 X_2}(x_1,x_2)\,dx_1\,dx_2 \tag{D.67}$$

**Figure D.13** Effect of a nonlinear function on the propagation of uncertainty from $X$ to $Y$.

where $g^{-1}(y, x_2)$ denotes the inverse of $g$ with respect to $x_1$. Changing the variable of integration from $x_1$ to $y$, the CDF of $Y$ can be expressed as

$$F_Y(y) = \int_{-\infty}^{\infty}\int_{-\infty}^{y} f_{X_1 X_2}\!\left(g^{-1}(y,x_2),\,x_2\right)\left|\frac{\partial\, g^{-1}(y,x_2)}{\partial y}\right|dy\,dx_2 \tag{D.68}$$

Taking the derivative with respect to $y$ gives the PDF of $Y$:

$$f_Y(y) = \int_{-\infty}^{\infty} f_{X_1 X_2}\!\left(g^{-1}(y,x_2),\,x_2\right)\left|\frac{\partial\, g^{-1}(y,x_2)}{\partial y}\right|dx_2 \tag{D.69}$$

Thus, the availability of a true closed-form solution requires the ability to analytically integrate the joint pdf in Equation (D.59), which is not possible for all cases. Two cases, however, occur frequently enough to warrant a brief description.

**Sums of Random Variables**

Many design problems involve response models whose output can be expressed as the sum of a series of random variables. If $X_1$ and $X_2$ are statistically independent and $Y = g(X_1, X_2) = X_1 + X_2$, then the joint PDF of $X_1$ and $X_2$ is equal to the product of the individual PDFs, so

$$F_Y(y) = \int_{-\infty}^{\infty}\int_{-\infty}^{y - x_2} f_{X_1}(x_1)\,f_{X_2}(x_2)\,dx_1\,dx_2 \tag{D.70}$$

The corresponding PDF can then be calculated as

$$f_Y(y) = \int_{-\infty}^{\infty} f_{X_1}(y - x_2)\,f_{X_2}(x_2)\,dx_2 \tag{D.71}$$

If $X_1$ and $X_2$ are normally distributed with means $\mu_1$ and $\mu_2$, and standard deviations $\sigma_1$ and $\sigma_2$, the PDF can be integrated analytically to obtain

$$f_Y(y) = \frac{1}{\sqrt{\sigma_{X_1}^2+\sigma_{X_2}^2}\,\sqrt{2\pi}} \exp\!\left(-\frac{(y - \mu_{X_1} - \mu_{X_2})^2}{2(\sigma_{X_1}^2+\sigma_{X_2}^2)}\right) \tag{D.72}$$

This result can be extended to show that the sum (or difference) of a set of $n$ independent, normally distributed random variables is also a normally distributed random variable with mean

$$\mu_Y = \mu_{X_1} + \mu_{X_2} + \cdots + \mu_{X_n} \tag{D.73a}$$

and standard deviation

$$\sigma_Y = \sqrt{\sigma_{X_1}^2 + \sigma_{X_2}^2 + \cdots + \sigma_{X_n}^2} \tag{D.73b}$$

This result can be very useful in engineering practice. It means that the mean value of the output is the sum of the mean values of the input variables, and the variance of the output is equal to the sum of the variances of the inputs.

**Products of Random Variables**

Other response models can take the form of products of random variables, e.g., $Y = X_1 \cdot X_2 \cdots X_n$. In such cases, the fact that the logarithms of lognormally distributed random variables are normally distributed allows the results of the previous section to be applied, so the product can be rewritten as $\ln Y = \ln X_1 + \ln X_2 + \cdots + \ln X_n$. This fact indicates that the product (or ratio) of two independent, lognormally distributed random variables will also be lognormally distributed with logarithmic mean

$$\lambda_Y = \mu_{\ln Y} = \lambda_{X_1} + \lambda_{X_2} + \cdots + \lambda_{X_n} \tag{D.74a}$$

and logarithmic standard deviation

$$\zeta_Y = \sigma_{\ln Y} = \sqrt{\zeta_{X_1}^2 + \zeta_{X_2}^2 + \cdots + \zeta_{X_n}^2} \tag{D.74b}$$

### D.9.3 Function of Random Variables – Approximate Solutions

Most problems in earthquake engineering are so nonlinear and/or otherwise complicated that closed-form solutions are not practical. In such cases, the propagation of uncertainty is usually handled numerically. A number of techniques, some with a variety of refinements, are available to evaluate the propagation of uncertainty. The following sections briefly introduce a few that require different levels of computational effort and provide different levels of information about the distribution of the response variable.

### D.9.3.1 Direct Integration

The most accurate and informative approach would be to numerically integrate the response function over the ranges of all of the input variables. The required summation would be of the form

$$F_Y(y) \approx \sum_{i=1}^{N_1}\sum_{j=1}^{N_2}\cdots\sum_{n=1}^{N_n} f_{X_1,X_2,\ldots,X_n}(x_i,x_j,\ldots,x_n)\,\Delta x_1\,\Delta x_2\cdots\Delta x_n \tag{D.75}$$

where $N_1, N_2, \ldots, N_n$ are the numbers of increments (of width $\Delta x_1, \Delta x_2, \ldots, \Delta x_n$) that the range of each variable is divided into, $x_i, x_j, \ldots, x_n$ are the mid-values of each increment, and the summations are over ranges of variables that produce $Y < y$. For large values of $Y$, the number of function evaluations would be equal to $N_1 \cdot N_2 \cdots N_n$. This procedure would produce the entire distribution of $Y$ with an accuracy that would increase with increasing numbers of input variable increments. With five variables divided into 20 increments each, 3.2 million response function evaluations would be required to obtain the complete distribution of $Y$. If the response was computed by an empirical model expressed as an algebraic equation requiring 1 ms to compute, direct integration would take about 53 minutes. However, if response was computed by a finite element model requiring 10 minutes for each analysis, about 61 years of computer time would be required. While direct integration can provide accurate and complete propagation of uncertainty, it is often prohibitively time-consuming.

### D.9.3.2 First Order, Second Moment Method

Because direct integration is usually impractical for real design problems, a number of approximate procedures have been developed. The approximate procedures all make (or require) assumptions that reduce (often greatly) the number of response model evaluations required to characterize uncertainty in the response variable, but they also provide less complete information about the actual distribution of that variable. Nevertheless, the approximations are often reasonable and the results sufficiently accurate for many purposes. In some cases, knowledge of the entire probability distribution may not be required. Instead, estimation of the moments (i.e., mean, variance, skewness, etc.) of the response variable distribution may be sufficient. If the moments are known and the form of the distribution (e.g., normal, lognormal, etc.) is known or can be assumed, an estimated response variable distribution can be computed. The First Order Second Moment (FOSM) reliability method is based on a first-order Taylor series approximation of the response function linearized at the mean values of the random variables. FOSM uses only first and second moment statistics (means and covariances) of the input variables to compute the mean and variance of the response variable. FOSM is popular because it requires only a small number of response function evaluations and it reveals the relative contribution of each input variable to the computed uncertainty in the response variable.

The function $Y = g(\mathbf{X}) = g(X_1, X_2, \ldots, X_n)$ can be expanded about the means of the random variables, $\mu_{X_i}$, as a Taylor series

$$y = g(\mu_{X_1},\ldots,\mu_{X_n}) + \frac{1}{1!}\sum_{i}\frac{\partial g}{\partial x_i}(x_i - \mu_{X_i}) + \frac{1}{2!}\sum_{i}\sum_{j}\frac{\partial^2 g}{\partial x_i\,\partial x_j}(x_i-\mu_{X_i})(x_j-\mu_{X_j}) + \frac{1}{3!}\sum_{i}\sum_{j}\sum_{k}\frac{\partial^3 g}{\partial x_i\,\partial x_j\,\partial x_k}(x_i-\mu_{X_i})(x_j-\mu_{X_j})(x_k-\mu_{X_k}) + \cdots \tag{D.76}$$

where all partial derivatives are taken at the mean values of the random variables. In the vicinity of the mean, the $(x_i - \mu_{X_i})$ terms will be small, so squares, cubes and higher powers of $(x_i - \mu_{X_i})$ will be much smaller and can, for many practical purposes, be neglected. Keeping only first-order terms, the truncated series provides the approximation (although it is exact when $g$ is a linear function)

$$y \approx g(\mu_{X_1},\mu_{X_2},\ldots,\mu_{X_n}) + \sum_{i=1}^{n}\frac{\partial g}{\partial x_i}(x_i - \mu_{X_i}) \tag{D.77}$$

The mean and variance of the approximated function can be computed to provide the approximate moments
