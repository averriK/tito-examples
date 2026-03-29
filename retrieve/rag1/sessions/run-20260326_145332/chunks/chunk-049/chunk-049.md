$$\mu_Y \approx g(\mu_{X_1}, \mu_{X_2}, \ldots, \mu_{X_n}) \tag{D.78}$$

and

$$\sigma_Y^2 \approx \sum_{i=1}^{n} \sum_{j=1}^{n} \frac{\partial g}{\partial x_i} \frac{\partial g}{\partial x_j} \text{Cov}(X_i, X_j) \tag{D.79}$$

Separating the variances (found on the diagonal of the covariance matrix) and using the correlation coefficient (Equation D.34)

$$\sigma_Y^2 \approx \sum_{i=1}^{n} \left(\frac{\partial g}{\partial x_i}\right)^2 \sigma_{X_i}^2 + \sum_{i=1}^{n} \sum_{j \neq i} \frac{\partial g}{\partial x_i} \frac{\partial g}{\partial x_j} \rho_{X_i X_j} \sigma_{X_i} \sigma_{X_j} \tag{D.80}$$

where $\rho_{X_i X_j}$ is the correlation coefficient as described in Section D.6.4. For the case of independent variables, the off-diagonal terms of the covariance matrix are zero, so the expression for the variance simplifies to

$$\sigma_Y^2 \approx \sum_{i=1}^{n} \left(\frac{\partial g}{\partial x_i}\right)^2 \sigma_{X_i}^2 \approx \sum_{i=1}^{n} \left(\frac{g(x_i + \Delta x_i) - g(x_i - \Delta x_i)}{2\Delta x_i}\right)^2 \sigma_{X_i}^2 \tag{D.81}$$

The second part of Equation (D.81) uses a central difference approximation to the gradient where $\Delta x_i$ is some small increment of $x_i$. With this approach, the FOSM method requires $2n + 1$ response function evaluations to obtain the first two moments of $Y$. For the previous case of five input variables, a total of 11 (rather than 3 million for direct integration) function evaluations would be required. Note the similarity of Equation (D.81) to Equation (D.66b). In both cases, the uncertainty in the computed response depends on the uncertainty of the input variable and on the sensitivity of the response to the input variable. In this case, each input variable contributes to $\sigma_Y$ in relative amounts that are easily identified. The FOSM method can be used to identify which variables are more and less important from the standpoint of response model uncertainty. Note that all partial derivatives are taken at the mean value of each input variable so the problem is "linearized" about the mean, which means that the FOSM approximation is most accurate for the "middle" of the distribution and is less accurate at the tails; the low probabilities of failure used in typical design scenarios, however, mean that the tails of the distributions are the regions of greatest interest. For design purposes, therefore, FOSM techniques have limited utility. Other approximate techniques, such as the first-order reliability method (FORM), which linearizes the problem in the region of interest, can be more useful for design purposes.

### D.9.3.3 Monte Carlo Simulation

Another approach to the propagation of uncertainty is to use randomization techniques such as Monte Carlo simulation (MCS). Randomization involves the generation of multiple sets, or "realizations," of all random variables used as inputs to the problem of interest. The input variables are simulated in a series of "realizations" that match desired probability distributions (and, if necessary, desired covariances between correlated input variables). The problem is then solved deterministically for each realization. The resulting response variable values can be collected in a histogram which, as the number of simulations increases, eventually approximates the PDF of the response variable. The distribution of the response variable, therefore, reflects the distributions of the input variables and the sensitivities of the response to each of the input variables. The computed response values can be analyzed statistically, either by computation of their moments or by fitting a distribution to them.

A relatively small number of simulations may be required to obtain a reasonably accurate estimate of the mean or median response, but many more may be required to adequately characterize the tails of the distribution. Recognizing that hundreds, if not thousands, of simulations are typically performed in Monte Carlo analyses and that Student's t-distribution closely approximates the normal distribution for more than about 50 samples, Equation (D.43) can be rearranged and put in the form

$$n^* = \left(\frac{z_{\alpha/2} \cdot s_x}{(U - L)/2}\right)^2 \tag{D.82}$$

where $z$ is the standard normal variate and $L$ and $U$ are the lower and upper values of the confidence interval, i.e., $L = \bar{x} - z_{\alpha/2} s_x$ and $U = \bar{x} + z_{\alpha/2} s_x$. On this basis, the minimum number of simulations required to provide $100(1 - \alpha)\%$ confidence that $\mu_x$ is between $L$ and $U$ is the next integer greater than $n^*$.

**Simulation of Single Variables**

The process of simulating a single random variable is best illustrated graphically. In order to ensure that the simulated values follow the desired distribution, a set of random numbers, $u_i$, between 0 and 1 are generated. These values are then assigned as CDF values for the random variable being simulated, i.e., $F_X(x_i) = u_i$. Solving for $x_i = F_X^{-1}(u_i)$ produces simulated $X$ values with the desired distribution. Figure D.14 illustrates this process for a generically distributed random variable. The reason why more simulations are required to accurately represent the tails of the distribution are apparent from the figure. For example, normally distributed random variables can be generated easily in Excel using the statement

`=NORMINV(RAND(), mean, stdev)`

FIGURE D.14 Simulation of distributed random variable values using random numbers, $U$, and CDF of target distribution. As the number of random numbers increases, histogram of target values approaches PDF of target distribution.

where mean is the mean value of the variable and stdev is its standard deviation. A lognormally distributed random variable can be generated using

`=LOGNORM.INV(RAND(), σ_ln x, σ_ln x)`

where $\sigma_{\ln x}$ and $\sigma_{\ln x}$ are the mean and standard deviation of $\ln x$.

**Simulation of Multiple, Independent Random Variables**

When the response is affected by more than one random variable, simulation of each random variable is required. If the random variables are independent, the simulation process can be performed individually as described in the preceding section. Before proceeding with the Monte Carlo simulations, checking the random variables for unintended correlation is advisable.

**Simulation of Two Correlated Random Variables**

It is often necessary to generate randomized pairs of variables with some desired level of correlation. This can be accomplished relatively easily. Assume it is desired to generate multiple realizations of two random variables, $X$ and $Y$, which have means, $\mu_x$ and $\mu_y$, standard deviations, $\sigma_x$ and $\sigma_y$, and a correlation coefficient, $\rho_{xy}$. $N$ pairs of properly correlated values of $X$ and $Y$ can be obtained from the following steps:

1. Generate $N$ pairs of uncorrelated standard normal ($\mu = 0$, $\sigma = 1$) random variables, $\varepsilon_1$ and $\varepsilon_2$.
2. Define $\varepsilon_3$ as a linear combination of $\varepsilon_1$ and $\varepsilon_2$ using

$$\varepsilon_3 = \rho_{xy} \varepsilon_1 + \sqrt{1 - \rho_{xy}^2}\, \varepsilon_2$$

3. Then compute

$$X = \mu_x + \sigma_x \varepsilon_3$$

$$Y = \mu_y + \sigma_y \varepsilon_3$$

$X$ and $Y$ will then approach their desired respective means, standard deviations, and correlation coefficient as $N$ becomes large.

**Discrete Representation of Continuous Distributions**

In some cases, it is computationally convenient to represent continuous probability density functions by "equivalent" discrete PMFs. The equivalence of the two representations is generally evaluated in terms of differences in their statistical moments. Discrete approximations of continuous distributions are most commonly represented by a set of weights assigned to specific values of the variable of interest. Miller and Rice (1983) [@MillerRice1983] used Gaussian quadrature to solve for the weights and values of different numbers of discrete points representing common distributions, as shown in Table D.2.

**TABLE D.2 Values and Associated Weighting Factors for Discrete Approximation of Continuous Distributions (from Miller and Rice, 1983) [@MillerRice1983]**

Distribution: Uniform {0 ≤ x ≤ 1}

Number of Values: 2 — Value, x: 0.211325, 0.788675; Weight, wx: 0.500000, 0.500000

Number of Values: 3 — Value, x: 0.112702, 0.500000, 0.887298; Weight, wx: 0.277778, 0.444444, 0.277778

Number of Values: 4 — Value, x: 0.069432, 0.330009, 0.669991, 0.930568; Weight, wx: 0.173927, 0.326073, 0.326073, 0.173927

Distribution: Standard Normal {f(z) = e^(−z²/2) / √π, −∞ ≤ z ≤ ∞}

Number of Values: 2 — Value, z: −1.000000, 1.000000; Weight, wz: 0.500000, 0.500000

Number of Values: 3 — Value, z: −1.732051, 0.000000, 1.732051; Weight, wz: 0.166667, 0.666667, 0.166667

Number of Values: 4 — Value, z: −2.334414, −0.741964, 0.741964, 2.334414; Weight, wz: 0.045876, 0.454124, 0.454124, 0.045876

Distribution: Exponential {f(x) = e^(−x), x ≥ 0}

Number of Values: 2 — Value, x: 0.585768, 3.414214; Weight, wx: 0.853553, 0.146447

Number of Values: 3 — Value, x: 0.415775, 2.294280, 6.289945; Weight, wx: 0.711093, 0.278518, 0.010389

Number of Values: 4 — Value, x: 0.322548, 1.745761, 4.536620, 9.395071; Weight, wx: 0.603154, 0.357419, 0.038888, 0.000539

---

## Index

Note: Bold page numbers refer to tables and italic page numbers refer to figures.

abutment, for bridges 594–596
acceleration histories 67, 68, 75, 76, 78, 478, 584
accelerometer 68–74
- data acquisition and digitization 73–74
- instrument configurations 69–70
- system dynamics 70–73, 72
active earth pressure see lateral earth pressure
active fault 181, 182
active pile length 565–566, 585–586
active tectonic region 41
aftershock 52, 53, 187, 667
age effects 642, 691, 693
aleatory variability 129, 129–131, 245, 266–267, 488, 489, 517–520, 523, 1016
- components 129, 129, 518–519, 518, 523
- ground motion 129–131, 517–520
- single station standard deviations 519, 519–520
- site response 520, 520
Alquist-Priolo Act 24
alteration of ground motion (liquefaction) 719, 719–720
amplification factor 435–436, 445
amplitude, of ground motion 67, 71, 85, 110
analog accelerometer 69, 71, 73–74, 75, 77–79, 78–79
anchored bulkheads 600–602
anelastic attenuation 101, 103, 114–116, 115, 137
anisotropy 376
apparent propagation velocity 157, 577–579, 843
areal extent of densification 878, 881
Arias intensity 94, 97, 123, 126, 130
aseismic movement 33, 41, 51, 53
asperities 51, 52
at-rest earth pressure see lateral earth pressure
attenuation relationship see ground motion model
Atterberg limits 337, 667
autocorrelation 260, 261, 262, 489

backbone curve 321–323, 322, 368–373, 376–378, 379, 385–386, 487
bandwidth 93
baseline drift see baseline error
baseline error 73–74, 77–79
basement walls 594, 600
base shear 543, 547, 549, 589–591, 619
base slab averaging 577–581
basin edge effects see basin effects
basin effects 104, 107, 118, 120–121, 121, 140, 428, 497–502, 991–992
Bay Area Rapid Transit (BART) system 886
Bayes' Theorem 999–1000
beam-on-nonlinear Winkler foundation see macro-element models
Becker penetration test (BPT) 342–343, 342–344, 891
bedrock within motion 444
bender element test 355, 358, 358
bending moment 597, 601, 601
Bessel function 579, 580
between-event term see event term
between-event variability 126–129, 518–519
bio-augmentation 889
biological techniques 889
blasting 869–873, 873
blind fault 44, 45
blind reverse fault see blind fault
body wave magnitude 58
body waves 27–28, 28, 961
bonded particle analysis 851–852
bored pile see pile foundations
boundary conditions 473, 481, 496–497, 961–964, 974–975, 984–985
bracketed duration see duration
bridges
- abutments response to lateral spreading 596–598
- response to ground motions 594–596
broadband seismometer see seismometer
buildings, seismic response analysis including SSI
- displacement-based method 591–593
- equivalent lateral force analysis 589–590
- response history analysis 593–594
- response spectrum analysis 590–591

calibration 140–143, 738, 837
California Strong Motion Instrumentation Program 80
Canterbury (New Zealand) earthquakes 22
cantilever walls 599, 601, 601
capacity 23, 249–252, 267–271, 563, 576–577, 576–577, 595
Caracas earthquake 429, 429
CDF see cumulative distribution function (CDF)
cellular containment 885–886
centrifuge tests 364, 366, 366, 367
characteristic earthquake 189–193, 189–190, 210
characteristic earthquake model see characteristic earthquake
characteristic site period 432, 991
Charleston 20
Chi-Chi (Taiwan) earthquake 4, 14, 22
Chile earthquake 19, 21, 58, 59
clay-like behavior 644, 645, 646, 756
clays
- compressibility 293–294, 294
- cyclic loading 316–317
- shearing behavior 300–303
CMS see conditional mean spectrum
coarse-grained soil 285, 286
coefficient of variation (COV) 372, 407, 1005
cohesion 282, 283, 604–605, 608, 1006, 1013
compaction grouting 877, 877–878
compaction piles 880, 880
complementary event 994
complex impedance ratio 452
complex stiffness see impedance function
compliant sliding block system 917
compound event 994
compressibility 284, 292, 961
- of clays 293–294, 294
- of intermediate soils 295, 682
- of sands 294, 294–295, 295
- and saturation 667–668, 693, 888–889
- of soil mixtures 295–296
compressibility ratio 621
compressive stress 291–296
computed tomography (CT) see geotomography
conditional mean spectrum see conditional spectrum
conditional probability 997–999
conditional spectrum 220, 221, 221
cone penetration test (CPT) 303, 344–351
- resistance 890–891
consolidation 280, 293, 660–661, 740–741
constitutive models 323, 475–476, 706–708, 738, 832–837
continental collision 38
continental drift 31–41, 32
continuous distribution 1009–1015
continuous random variable 1001–1003
convection 35, 35
convection currents, in mantle see convection
core, of earth 29, 29, 32–33, 36, 38–41
corner frequency
- ground motion filtering 76, 76, 78, 79
- source parameter 101, 135, 136
correction factors 338, 339–340, 350
co-seismic stability hazards 796–798, 798
Coulomb earth pressure theory 605–609
coupled compliant sliding block analysis 817
coupling 290, 368, 541
CPT see cone penetration test (CPT)
critical damping coefficient 549, 923
critical state 298–300, 299; see also steady state of deformation
critical void ratio 298
cross-hole test 333–335, 891
CRR see cyclic resistance ratio
crushable soils 711
crust, of earth 29, 29, 32–33, 36, 38–41
crustal damping 103, 121
CSR see cyclic stress ratio
cumulative absolute velocity 97, 124, 125–126, 126
cumulative distribution function (CDF) 188, 190, 1001, 1001, 1002, 1002
cyclic degradation 313, 317, 382, 383, 402–406
cyclic direct simple shear test 362–363
cyclic liquefaction 638, 638, 639, 651–653, 653, 664
cyclic mobility 319, 656, 706, 731
cyclic resistance ratio (CRR) 655, 672, 673, 684–687, 756–757
- age adjustment 691–693
- effective stress adjustment 689, 689, 689
- loading cycles 688, 688, 688
- saturation adjustment 693–696, 694, 695
- static shear stress adjustment 690–691, 691
cyclic response model 321–323
cyclic softening 402, 640, 755–759
- cyclic resistance ratio 756–757, 757
- cyclic stress ratio 756
- definition 636
- liquefaction resistance 702, 702–703, 703
cyclic strain approach 697–700
- earthquake loading 697–698
- liquefaction potential evaluation 700
- liquefaction resistance 698–700, 699
cyclic strain-based pore pressure model 705
cyclic strength curve 657
cyclic stress approach 671–697
- earthquake loading 675–680
- framework 674, 674–675
- in situ test parameters 681–684
- liquefaction resistance 684–696
- non-triggering implications 696, 696
- simplified method 696–697
cyclic stress-based pore pressure model 704
cyclic stress ratio (CSR) 655, 657, 660, 661, 662, 672, 673, 676–679, 680
cyclic torsional shear test 363
cyclic triaxial test 320, 359–362

damage measures (DMs) 23, 234–235, 238, 252–254
damage model 238
damage probability matrix 252, 253
damage state 235
damped soil
- on elastic bedrock 451–455
- on rigid bedrock 445–450
damping ratio 71, 387, 388, 389, 390–393, 391, 463, 484–488, 492, 544–549, 545, 551, 552, 554–555, 556–557, 558–559, 560–561, 565, 566, 568, 569, 572, 923, 930, 935, 937–939
database 78, 83–84, 126, 127, 669–671
deaggregation see disaggregation
decision variable (DV) 23, 235, 238, 239
deconvolution 459–461
decoupled sliding block analysis 816–817
deep foundations see pile foundations
deep soil mixing 884, 884–885
degradation index 317
degradation ratio 403
demand-and-capacity-factor (DCFD) 268–270
densification 869–878
density screen 667, 667
depth reduction factor 676–677
desaturation 888–889
design basis earthquake (DBE) 195
design ground motion 3, 176, 250
deterministic methods, of ground motion simulation 133, 138–140
deterministic seismic hazard analysis (DSHA) 193–196, 194
deviator stress 282, 290, 359–360, 655
digitization 73–77
digitizer 75–76
dilatancy 290–291, 306, 308, 310–311, 394, 396, 399, 475, 706, 708, 707, 707
dimensionless frequency 551, 565, 565, 585, 585
dip-slip movement 43–44, 44, 782–785
Dirac delta function 933–934
direct analysis, of soil-structure system 539
directionality 148–150, 827–828
direct loss 23, 235
disaggregation 214–216, 215, 218–220
discontinuous deformation analysis (DDA) 850
discrete Fourier transform (DFT) 913
discrete probability matrix 238–239, 252–254
discretization 834
discrete random variable 1001
dispersion curve 327
displacement-based procedures 591–593
displacement-related pseudostatic analyses 830–832
dissipated energy-based pore pressure model 705, 706
distance screen 666, 666–667
distinct element analysis 848–850
distributed deformations 783, 827, 834
Doppler effect 145, 145–146
double-corner model 136, 136–137
downdrag 744, 749–751
down-hole test 330–332, 331, 891
downtime 24, 235
drainage 668
- conditions 284
- screen 668
drained loading 284, 300
drilled shaft see pile foundations
dry pluviation 354
DSHA see deterministic seismic hazard analysis (DSHA)
ductility 940–941
- demand 573, 941
- of oscillator 96–97, 97, 573
Duhamel integral 934–935, 939
duration, of ground motion 67, 90, 93–97, 94–95, 123, 124, 125, 130–131, 133–135, 146, 154–155, 217–220
Duzce earthquake 22
DV see decision variable

Earth, internal structure 27–31, 29
earthquake energy release 61–62
earthquake engineering 1–25, 232–238
earthquake intensity 59–61, 60, 61, 86, 87, 88
earthquake, location 56–57
earthquake rate 180, 186–189, 187, 191–193, 196, 199–200, 202–203
earthquake-resistant design 176
earth-retaining structures 11, 599–602
EDP see engineering demand parameter (EDP)
effective shear strain 464, 464, 465
effective stress adjustment 681, 681, 686
efficiency 248, 821, 826, 826
efficiency factor, for pile groups 567, 568, 569
ejecta 722, 721, 742–743
elasticity 289–290
elastic rebound 50–54, 52, 179
El Centro 21
electrodynamic seismometer 69–71, 70, 74, 76
embedment effects 551–552, 553, 557, 581–583, 583
empirical Green's function 140
en echelon faults 783
energy dissipation 700–703, 937–938
- relationship to earthquake loading 701
- kappa 486–487
- liquefaction potential evaluation 703
- low-strain material damping 484
- material damping 105, 118, 137, 369, 387, 484, 546, 551, 979–982
- scattering 484–486
- stiffness and damping behaviors 487–488
energy flux 988
engineering demand parameter (EDP) 23, 84, 85, 207, 234, 244, 257–258
epicenter 42, 43, 56–57, 56
epicentral distance 42, 198
episodic tremor and slip (ETS) 37–38, 40
epistemic uncertainty 1016–1017
- ground response 488–489
- ground response model error 492–493
- non-ergodic site response 521–522
- probabilistic seismic hazard analysis 210–214, 213, 245
- site-to-site variability 518, 518, 518–519, 522
epsilon, of ground motion 96, 131–132, 132, 202, 214–215, 218, 219–221, 219
equivalent lateral force analysis, for buildings 589–590
equivalent linear soil model 321
equivalent linear site response analysis 463, 477–480
ergodic
- approach 434
- models, site response 511–516
Eurocode 8, 509
European Macroseismic Scale (EMS-98) 60
event term 127, 129, 129, 514, 518; see also between-event variability
exponential distribution 1014–1015
extended Masing model 322, 322

factor of safety 665, 673, 673, 800–802
failure mechanism 600–602
failure modes
- of retaining walls 600–602
- of rock block failure 844, 847–848
- of slopes 792–795, 801, 837
- of surface faulting 782–788
failure surface 800–802, 801
fast Fourier transform (FFT) 913–914
fault dip angle 98, 114–116
fault displacement hazard analysis 786–788
- avoidance 789–790
- diversion 791–792
- engineered fill 790–791, 791
fault movement
- dip-slip 43–44
- moment tensor 48–50
- oblique 47–48
- source inversion 50
- strike-slip 44–47, 46
fault rupture 3, 98, 138–139, 145–147, 183, 198–199, 782–786
- damage 4, 782, 788–789
faults 41–50, 176–179, 177–179, 180–183, 181, 182, 188, 189, 192–193
- displacement 782–792
- geometry 42, 42
- segments 181–182, 182
- strike 98, 150–151
Fermat's principle 975
fictitious depth see finite fault parameter
fine-grained soil 285, 353
fines content 309, 663
- adjustment 681
- effects on liquefaction see liquefaction, triggering, behavior of susceptible soils
finite fault 98–102, 99, 115–116, 133, 138
- parameter 102, 102, 115–116
first order second moment (FOSM) reliability method 1024–1025
fixed-base structure 538, 542, 542–543
flat instrument response 74, 76
flexibility ratio 621
flexible-base 542–545, 542, 545
fling step 145, 147–148, 149, 155–156, 155
flow liquefaction 6
flow failures 9, 10, 636, 637
flow slide deformation 840–843, 842, 843
- stability analysis 731, 839–840
- triggering 646–651, 722–723
flow liquefaction surface (FLS) 647–650
- cyclic loading 649–650, 650
- monotonic loading 647–649, 647–649
FLS see flow liquefaction surface
fluid injection 54–55
focal mechanism 48, 49, 101, 107, 111, 112–113, 114, 114, 116
focusing see basin effects
foot wall 43, 47, 47
force-balance accelerometer see accelerometer
foreshock 51–52, 187
fossil faults 39
foundation capacity 563, 576–577, 576–577, 595
foundation damping 544, 545, 546
foundation input motion 540, 577–588, 613
foundation settlement 744–751, 877
- deep foundations 748–751, 749–751
- shallow foundations 744–748, 745–747
Foundex Becker penetration test (FBPT) 342–343
Fourier series 88–90, 909–914, 910, 931
Fourier amplitude spectrum 75–76, 75–77, 88–90, 89, 90, 93, 133–135, 136, 468, 912, 914
Fourier phase spectrum 89, 89–90, 157
fracking 54
fragility curve 242, 253
Franki method 879
free-face model 732
free-field ground motion 538–542
free-field settlement 740–742
free surface effect 451, 452, 989
frequency content, of ground motion 67, 88–91, 435, 448, 719, 914–916
frequency-dependent site response approach 469
friction angle 282, 283, 283, 301, 301, 303, 304, 306
functional recovery 235, 255

gamma rays 324
gap element 570–571
GEER Association 19
gel-push sampling 354
geologic considerations 177–179, 189, 439, 440, 441, 641–642, 714–715, 799
geometric attenuation 101–102, 102, 114, 137, 140
geometric mean, of ground motion 86
geometric spreading see geometric attenuation
geophone 70
geophysical tests 325, 326, 326, 891–892
geospatial approach 708–709
GeoTech Tools 867
geotomography 334
global positioning system (GPS) 50, 72
Global Seismographic Network 79
GMMs see ground motion models (GMMs)
Good Friday earthquake 14, 19, 21, 636
grain size distribution 285
gravelly soils 709
gravity walls 599–601
Green's function 139–140
gross sliding 297
ground displacement 71
ground failure 288, 313
ground motion 1, 19–23, 67, 234
- aleatory variability of 129–131, 517–520
- amplification 987–991
- factors affecting 98–107
- free-field vs. foundation-level 538
- intensity measures see intensity measures (IMs)
- measurement 68–84
- models 107–132
- modification 217, 222–223
- near-fault 145–156
- polarization 148–150
- pulse-like 147–148, 152–156
- recordings see measurement
- selection 218–222
- simulations 132–145
- spatial distribution in near-fault regions 150–152
- spatial variability 156–160
- spectra 88–93, 89, 92, 134–137, 136
- variations between tectonic regimes 121–123
ground motion instrument networks see ground motion networks
ground motion models (GMMs) 107–132
- for amplitude parameters 110–123, 112–113, 114–115, 122–123
- data attributes and dispersion 126–132
- historical development 108–110
- other intensity measures (not solely amplitude parameters) 123–126
- for spectral accelerations see for amplitude parameters
ground motion networks 79–80, 81, 82, 83
- local arrays 80, 82, 83
- surface networks 79–80
- vertical arrays 80, 83
ground motion prediction equation see ground motion model
ground motion representation theorem 139
ground oscillation 638, 720
ground response analysis 313, 442, 443–493, 515–517, 675–677
- layered soil, on elastic rock 455–459
ground-slope model 733
groundwater level lowering 888
group effects see pile groups
group velocity 970–971
grouting 881–883
- compaction 877
- intrusion 883, 883
- jet 885
- permeation 882, 882–883
Gutenberg-Richter recurrence law 186–188, 187, 200

Haiti earthquake 12
halfspace 451, 451, 453, 454, 544, 550, 582
hanging wall 43, 114, 116–117, 116–117, 143, 144, 147–148
harmonic motion, simple
- complex notation 906, 907
- trigonometric notation 903–906, 905, 906
- tripartite plot 907, 908
hazard integrals 200–201, 216
hazard maps 209
HEA see horizontal equivalent acceleration (HEA)
healing front 146
Hebgen Lake 19, 21
high-cut filter see low-pass filter
high-pass filter 78–79, 78–79
high-strain element test 358–363
high-strain field test 337–352
historical earthquakes 19, 20–22
Hooke's law 957, 958
horizontal equivalent acceleration (HEA) 807–808, 808
Husid plot 94, 95
hybrid scalar IM 95, 96–97, 125–126
hybrid simulation procedure see deterministic methods, of ground motion simulation
hydraulic fill 642–643, 643
hydraulic fracturing see fracking
Hyogo-ken Nanbu earthquake 11, 15
hypocenter (focus) 42, 47, 47, 100, 216
hypocentral (focal) depth 42, 56, 57
hypocentral distance 42, 57

impedance function 540–541, 541, 548–569, 554–555, 556–557, 560–561, 565, 567–568, 569
impedance ratio 452, 453, 454, 457, 973, 974, 974
IMs see intensity measures (IMs)
inactive fault 182
Inangabua earthquake 61
indirect loss 235
induced seismicity 54–56
inelasticity 289–290
inelastic spectra 96–97, 97
inertial force 806, 806, 919
inertial interaction see soil-structure interaction (inertial interaction)
inertial seismic earth pressure 619
initial effective stress 656–658, 660
- effects on liquefaction see liquefaction, triggering, behavior of susceptible soils
initial liquefaction 319, 652–653
initial shear stress 661–663, 684
- effects on liquefaction see liquefaction, triggering, behavior of susceptible soils
input motions 480–484, 497
in-situ density 353
in-situ testing 890–891
instrumented Becker test (iBPT) 343–344, 344
instrument response 74, 75
intensity measures (IMs) 23, 67, 84, 95–97, 176, 200–203, 207–209, 214–217, 234, 238
- amplitude parameters 85–88
- combinations of 95–96
- dispersion 129–131
- duration parameters 93–94
- efficiency 84, 248
- frequency content parameters 88–93
- ground motion 234
- hybrid scalar 95–97, 125–126
- mixed scalar 823–825
- predictability 84, 248
- scalar 822, 822, 823
- sufficiency 84, 248–249
- vector 95, 825–826
interbedded soils 710, 711
interface event 36, 38, 41
interface flow failure 724
Interferometric Synthetic Aperture Radar (InSAR) 50
intermediate soils 308–309, 319–320
- compressibility 295
- cyclic loading 319–320
- shearing behavior 308–309
intra-slab event 36, 41
intrusion grouting 883, 883
inverse discrete Fourier transform (IDFT) 913
inversion 329
IRIS Data Management Center 79, 80
isoseismal map 61, 61
isoseisms 61
Izmit earthquake 22

Japanese Meteorological Agency magnitude 58
jet grouting 885
jointly distributed random variable 1003
joint mean rate density 208
joint normal distribution 1015

Kahrmanamaras (Turkey-Syria) earthquake 22
kappa 486–487
- for site attenuation 137–138
Kelvin-Voigt 456, 570–572, 571, 979, 980
Kik-net arrays 80, 83
kinematic interaction 538–542, 577–588
- application of transfer function 586–588
- base slab averaging 577–581
- embedment effects 581–583
- pile foundation 583–586
kinematic seismic earth pressure 613–619
kinematic source model 139
Kobe (Hyogo-Ken Nambu) earthquake 21, 499–500, 602
Kocaeli earthquake 46–47, 47

laboratory testing, for soil improvement 890
lagged coherency 158–159, 158, 577–581, 579
lagged distance 262
Lamé constant 958
lateral displacement index (LDI) 736
lateral earth pressure
- active 602–607, 603, 607
- at rest 603–604, 603
- passive 595–598, 596, 603, 603, 607, 607–610, 608–610
- seismic 610–619, 612, 615–616
lateral spreading 6, 12, 596–598, 597, 638, 638, 731–739
left-lateral movement 44, 46
lifeline hazards 11–15
Light Detection and Ranging (LIDAR) 177, 179
limit equilibrium analysis 800–802
limit state
- for design 249–252, 269
- for seismic earth pressure 611, 612
linearity 288–289
linear threshold shear strain 297, 298
liquefaction 3–7, 249, 636–763, 888
- consequences 713–752
  - geologic considerations 714–715
  - ground motion alteration 719–720
  - lateral spreading 6, 731–759
  - manifestation severity indicators 715–719
  - residual strength 724–731
  - sand boils 8–10, 720–722
  - settlement 739–751
- cyclic liquefaction 638–639, 651–697
- cyclic softening 402–406, 755–759
- flow liquefaction 636–637, 646–651, 722–724
- other factors 663–664
- probabilistic liquefaction hazard analysis (PLHA) 751–755
  - for consequences 753–755
  - for triggering 752–753
- soil density effects on liquefaction see liquefaction, triggering, behavior of susceptible soils
- susceptibility 641–646
  - compositional indicators 643–646
  - geological indicators 641–643
  - historical indicators 641
- triggering 651–713
  - behavior of susceptible soils 656–664
  - criteria 652–653
  - crushable soils 711
  - cyclic strain approach 697–700
  - cyclic stress approach 671–697
  - effective stress response analysis approach 703–708
  - empirical prediction 664–671
  - energy dissipation approach 700–703
  - geospatial approach 708–709
  - gravelly soils 709–710
  - historical perspective 653–655
  - interlayered soils 710–711
  - laboratory testing 655
  - near-fault motions 713
  - parametric uncertainty 687–696
  - simplified method 676–677
  - tailings 711–713
liquefaction potential index see liquefaction, consequences, manifestation severity indicators
liquefaction resistance see liquefaction, triggering
liquefaction severity number see liquefaction, consequences, manifestation severity indicators
liquid limit 286, 644, 667
lithosphere 29, 30, 35
load amplitude effects on liquefaction see liquefaction, triggering, behavior of susceptible soils
load and resistance factor design 267–268
local boundary 496
local ground response 103–106
local (Richter) magnitude 58
logic tree 210–212, 211
lognormal distribution 108, 131, 202, 208, 244–250, 1012–1014, 1013
Loma Prieta earthquake 15, 16, 21, 24, 48, 61, 429–430, 430, 449
longitudinal waves 951–953, 952
loss angle 549
loss model 238, 245, 248, 254–255
Love waves 28, 29, 499, 967–969
low-cut filter see high-pass filter
low-pass filter 76–78, 76
low-strain element test 355–358
low-strain field test 325–337
LPI see liquefaction, consequences, manifestation severity indicators
lumped mass model 470, 470–471

macro-element models 564, 569–572, 574, 576, 577
magnetic anomalies 36, 36–37, 39
magnitude
- maximum 183–184
- minimum 183
- probability density functions for 188–191, 189
- saturation 58, 58, 111
magnitude-area scaling relationships 183–184, 184
magnitude-recurrence 186–187, 187
magnitude scaling factor 678, 679, 679
mantle, of earth 29, 29–31, 31
Masing rules 322, 322, 487, 488
mass ratio 544
material damping see energy dissipation, material damping
material point method 843
Maule (Chile) earthquake 21
maximum component, of ground motion 85–86
maximum credible earthquake (MCE) 195
maximum magnitude model 188–189, 189
maximum probable earthquake (MPE) 195
maximum shear modulus, G_max 369, 370, 373
mean hazard 213–214, 213
mean period 93, 123–125, 124, 125
mean shear wave velocity (V_S30) see time-averaged shear wave velocity
mean squared error 222
median component, of ground motion 86, 150
mesh locking 834–836
Mexico City earthquake 5, 21, 431–432, 432
microbially induced calcite precipitation (MICP) 889
microseismic activity 67
mine tailings 711–713, 712, 713
mitigation 24–25
- of fault displacement hazards 789–792
- of ground failure hazards 867–892
mixed effects regression procedure 129
mixed scalar intensity measures 818–820, 820, 823–825
modal analysis see response spectrum analysis
model uncertainty 265–266, 492–493, 493
mode shape 447, 947–948
mode superposition 947–948
modified Mercalli intensity (MMI) 60, 60, 61
modulus reduction curve 369, 369, 376–378, 379, 380, 381, 381–382, 384, 385
Mohorovičić discontinuity 30
Mohr circle 276–284, 277, 278, 281, 283, 360
Mohr-Coulomb failure criterion 282–284, 283
moist tamping 354
moment balance 191, 200
moment of inertia 559, 584, 615, 621
moment magnitude 58, 58, 59, 59, 101, 111, 183, 184
moment tensor 48–50, 49
Monte Carlo simulation (MCS) 259, 260, 488, 1025–1027
multi-channel analysis of surface waves (MASW) 330
multi-dimensional ground response analyses 493–497
- basin effects 497–502
- topographic effects 502–511
- two- and three-dimension 493–497
multi-dimensional stress-deformation 834–836
multiple-block analyses 848–852
multiple-block rock slopes
- bonded particle analysis 851–852
- discontinuous deformation analysis 850
- distinct element method 848–850, 851
multiple-degree-of-freedom (MDOF) system 944–945
- equations of motion 945–946
- mode superposition method 947–948
- response spectrum analysis 948–949
- undamped free vibration 946–947
multiplication rule 998
municipal solid waste 384, 390

natural frequency, of oscillator 71, 542–543, 542
natural period, of oscillator see natural frequency
near-fault ground motion 145–156, 216–217, 713
- physical processes 145–148
- polarization 148–150
- pulse-like motions and effects 152–156
- spatial distribution 150–152
New Madrid earthquake 20
Next Generation Attenuation (NGA) 77–78, 83–84, 112–113, 127
NGA see Next Generation Attenuation (NGA)
Niigata earthquake 8, 9, 11, 21, 636, 639, 719–720
noise 74–79
- digitization 75–76
- high-frequency 74–77
- low-frequency 77–79
non-ergodic site response 434, 511–522
- aleatory variability of ground motion 517–520
- epistemic uncertainty 492–493, 521–522
- mean site response 513–517
nonlinear effective stress analysis 474, 480, 703
- advanced constitutive models 706–708, 707, 707
- cyclic response models 321–323
- pore pressure models 474, 704–706, 706
nonlinearity 288–289, 368
nonlinear site response 118
- analysis 469–477, 479, 480
non-planar failure surfaces 828
nonplastic silts 308–309
normal distribution 1010, 1010–1012, 1011
normal fault 43, 44
North Anatolian fault 40, 46, 47, 50
Northern California Seismic Network 80
Northridge earthquake 10, 21, 67–68, 91, 499, 500, 504
nuclear structures, SSI 598–599
nucleation point, of fault rupture 198
number of cycles, of ground motion 93–94
numerical stability evaluation
- multiple blocks 848–852
- single blocks 846, 845–848, 847–848
Nyquist frequency 74, 90

oblique slip movement 47, 47–48
off-fault areal sources see source zones
omega-square model 134, 136, 138
one-dimensional ground response analysis
- comparison of types 476–480
- energy dissipation 484–488
- equivalent linear approximation 463–469
- input motions 480–484
- linear analyses 444–463
- nonlinear analyses 469–476
- variability and uncertainty 488–493
one-dimensional wave propagation 951–955, 952
ontological uncertainty 1017
operating basis earthquake (OBE) 195
ordinary standard bridges (OSB) 595
organic soils 286–287, 383–384, 390, 392
outcrop motion 481–482
overconsolidation ratio (OCR) 293, 301, 302, 405–407

paleoliquefaction 641
paleoseismology 177
Pangaea 31
Parseval's theorem 90, 468
passive earth pressure see lateral earth pressure, passive
path effects, on ground motion 98, 101–103, 107, 114–117, 132, 135–137, 136, 139–140
PBEE see performance-based earthquake engineering (PBEE)
peak acceleration see peak ground acceleration
peak ground acceleration (PGA) 85–87, 86, 87, 108–110, 435
peak ground displacement (PGD) 85, 88
peak ground strain 159
peak ground velocity (PGV) 85, 87–88, 159
PEER triple integral 243
perfectly matched layer 497
performance 25, 232
- components 233–235
- criteria 235–237
- prediction 237–246
performance-based design 232–233, 246–255
- damage-level implementation 252–254
- ground motion intensity 248–249
- loss-level implementation 254–255
- response-level implementation 249–252
- scalar and vector approaches 246–248
performance-based earthquake engineering (PBEE) 232, 233, 236, 246
performance criteria 235–237
period lengthening 543–545, 545, 547, 590
permeation grouting 882, 882–883
Peru earthquake 5, 13
PGA see peak ground acceleration (PGA)
PGD see peak ground displacement (PGD)
PGV see peak ground velocity (PGV)
phase transformation 304, 305, 656
phase velocity 970–971
physical damage 234–235
piezoelectric bender element 358, 358
pile driving analyzer (PDA) 342
pile foundations 563–572, 583–586, 585, 596–598, 597–598, 744, 747–751, 749–751
pile groups 563–564, 564, 567–569, 569
planning 24, 24
plasticity 286, 287, 288, 643–645, 645
plasticity-based macro-element model 576
plasticity index 286
plastic limit 286
plastic spring 570–571, 571, 576
plate boundaries
- spreading ridge 35–36, 36
- subduction zone 36–38, 38
- transform faults 38–40, 40
plate tectonics 32–35, 33–35, 177, 179
PMF see probability mass function (PMF)
Poisson distribution 1009
Poisson source model see time-independent source model
Poisson's ratio 327, 544, 551, 621, 966, 970
policy 24, 24, 25
pore pressure generation 314, 315, 318, 474
pore pressure model 704–706, 706
- cyclic strains 705
- cyclic stresses 704
- dissipated energy 705, 706
pore pressure ratio 318, 647
pore pressure redistribution 839–840
post-seismic stability analysis 839–843
- flow slide deformations 840–843
- flow slide stability 839–840
power spectra 90, 158
power spectral density see power spectra
preconsolidation pressure 293
predictability 84, 97, 130, 248
prediction of performance
- closed-form approach 244–246
- discrete approach 238–240, 239
- integral approach 240–244
predominant period 92, 92
pressuremeter test (PMT) 351–352, 352
principal fault 782, 783
principal stresses 278–279
probabilistic response analyses
- aleatory variability 266–267, 1016–1017
- input motions 263–265
- model uncertainty 211, 265–266, 687
- randomization of input parameters 259–263, 1025–1028
- scalar intensity measure 263–264
- vector intensity measure 264–265, 821, 825–826
- vector response, damage, and loss 266, 821, 825–826, 852–854
probabilistic seismic hazard analysis (PSHA) 196–217, 524–525
- disaggregation 214–215
- earthquake rates 199–200
- epistemic uncertainty 210–214
- finite time periods 208–209
- independent variables, distributions of 198–199
- near-fault effects 216–217
- scalar 200–207
- vector 207–208
probability
- association measures 1005–1006
- axioms 995
- Bayes' Theorem 999–1000
- central tendency measures 1004
- conditional 997–999
- confidence intervals 1007–1008
- continuous distribution 1009–1015
- dispersion measures 1004–1005
- of events 996–1000
- Poisson model 191–193, 200–201, 208, 1009
- Poisson rate see Poisson model
- symmetry measures 1005
- total probability theorem 241–242, 999
- uniform distribution 1008–1010
- of unions and intersections 996, 996–997
probability density function (PDF) 183, 186, 188, 190, 198, 201, 1001–1003
probability mass function (PMF) 149, 1001, 1001, 1002, 1002
probable loss (PL) 255
probable maximum loss (PML) 254–255
progressive failure 723, 802, 802, 840
propagation of fault movement 788
propagation of uncertainty 266, 1017–1028
pseudo-acceleration 611, 611, 612
pseudo-reference strain 378
pseudo-spectral acceleration see spectral acceleration
pseudostatic coefficient 804, 809, 831
pseudostatic stability analysis 806
PSHA see probabilistic seismic hazard analysis (PSHA)
pulse period 93, 153–154, 153
pushover analysis see displacement-based procedures
pushover curve see displacement-based procedures

quality factor see crustal damping
quarter wavelength method see square root impedance method
quasi-steady state 305, 305–307, 649

radiation damping 451, 452, 544, 546, 552, 554–555, 556–557, 557–561, 560–561, 982–983
radiation pattern 135, 146, 147, 147
rake angle 47, 47
Ramberg-Osgood model 322
rammed aggregate piers 881, 881
randomization 259–263, 489–492, 491, 1025–1028
random variable
- continuous 1001–1003
- discrete 1001
- functions 1020–1028
- jointly distributed 1003
random vibration theory approach 467–469
Rankine earth pressure theory 598, 604–605, 605, 607–608, 608
rapid impact compaction 876, 876–877
rate dependence 314, 316, 376, 402, 406
rate effects 828–829
ratio of response spectra 586, 587
Rayleigh damping 484, 948
Rayleigh wave 28, 29, 327–330, 499, 962–964
- displacement amplitude 965–966
- velocity 965
ray path 975, 975
recurrence interval 186, 191–193
recurrent liquefaction 641
reference strain 378
refraction microtremor (ReMi) test 330
reinforced soil walls 599
reinforcement techniques
- compaction piles 880, 880
- rammed aggregate piers 881, 881
- stone columns 878, 878–880, 879
relative density 309, 310, 311, 394–395, 658–659
relative dilatancy index 311
relative state parameter index 311, 396–397
reliability-based design 267–271
- closed-form solution 270–271
- demand and capacity factors 268–270
- load and resistance factors 267–268
reservoir-induced earthquake 55
residual strength 722, 725–731, 726, 726, 727, 728, 729, 840
resonance 443, 444, 926, 988–989
resonance effects 104, 105, 988–991
resonant column test 355, 355–358
response history analyses 67, 217, 222–223, 593–594
response model 237
response spectra 939–940; see also spectral acceleration
response spectral matching 222–223
response spectrum analysis, for buildings 589–591
retaining structures see earth retaining structures
retaining walls see earth retaining structures
return period of ground motion 203, 240
reverse fault 43–44, 45, 783–784
right-lateral movement 44, 46, 46, 48, 783–784
rigid base see fixed base
rigid block analysis
- behavior 815, 815–816, 816
- decoupled procedure 816–817
- mechanics 811–813, 811–814, 815
rigid block displacements 818
- mixed scalar IMs 819–820, 820
- scalar IMs 818–819
- vector IMs 821, 821
rigid foundation 538, 541–542, 541
rigid system 917
rise time 98–99, 100, 123, 146, 148
risk-targeted maximum considered earthquake 195, 250
rock outcropping motion 444
rock slope failure types 844
rock slope stability 844–852
- empirical evaluation 845, 845
- numerical evaluation 845–852
root-mean-square (rms) value 467–468
Rossi-Forel (RF) scale 60
rupture directivity effect 145–147, 147, 216
- pulse characterization 153
rupture front 100, 146, 146, 147
rupture velocity 100, 138

safe shutdown earthquake (SSE) 195
Sammon's map 212, 212
sample disturbance 324, 353, 355, 379, 407, 654, 890
sample space 994
San Andreas fault 39–40, 42, 43, 44, 46, 48, 51, 53, 53, 178, 188, 215
sand
- compressibility 294, 294–295, 295
- cyclic loading 317–319
- shearing behavior 303–308
sand boils 6, 8, 638, 639, 720–722
sand-like behavior 644, 645, 646
San Fernando earthquake 6, 6, 7, 10, 21
San Francisco earthquake 15, 16, 21, 58, 59, 430, 431
Santa Barbara earthquake 9
saturation 667–668, 688, 693–695
saturation screen 667–668
scalar hazard analysis 96
scalar intensity measures 818–819, 822
scaled backbone approach 212
scattering see wave scattering
screening procedures 666–668
- density screen 667, 667
- distance screen 666, 666–667
- drainage screen 668
- saturation screen 667–668
- shear strain screen 667
secant shear modulus 369
seiche 15–19
seismic compression 318, 394, 397–400
seismic cone test 332
seismic cross-hole test 333–335
seismic deformation 33
seismic demand 267–271
seismic down-hole (up-hole) test 330–332, 331
seismic earth pressure see lateral earth pressure, seismic
seismic energy 61, 62
seismic gap 53, 53
seismic hazard 2, 867
- analysis 67, 98, 176, 522, 524
- curves 200, 203, 204, 525
seismic input 67, 93
seismic moment 57, 135, 138, 184, 184, 185, 186, 191
seismic reflection test 326–327
seismic refraction test 326–327
seismic risk 2
seismic safety evaluation earthquake 195
seismic stability analysis 803–839
- displacement 838–839
- pseudostatic 804–810
- sliding block 810–832
- stress-deformation 832–838
seismic waves 27–28, 28–29, 31, 951–987
seismometer 68–73
- data acquisition and digitization 73–74
- instrument configurations 69–70
- system dynamics 70–73, 72
semivariogram 262, 262
sensitivity analysis 1018–1020
sensors see accelerometers, seismometers
settlement due to ejecta 742–743
settlement due to instability 743–744
shadow zone 31, 31
shaking table tests 364–365, 365
shallow foundation 548–563, 744–748, 745–747
- capacity 563
- flexible structural elements 559–563, 561–562
- nonlinear models for 572–577
- non-uniform soil 558–559
- stiffness and damping 548–558, 553–555, 556, 557
- uniform soil 548–558
shear strain 464, 464–467
shear strength 282–284, 301–306, 351, 369, 385–386, 401–408, 724–791, 800–802
shear stress 279, 281, 282
- cyclic 311–320
- dilative and contractive behavior 290, 290
- static 296–311
shear wave velocity 326–329, 332, 335, 336, 368, 371, 372, 373, 375, 437, 551, 566, 613, 652, 671, 672, 684, 686, 687, 692, 961
signal-to-noise ratio 74
significant duration see duration
single-degree-of-freedom (SDOF) system 69–71, 72, 91, 218, 219, 542, 542, 917–918
- equation of motion 918–921
- general loading 932–935
- harmonic loading 925–930
- linear 921–925
- nonlinear 941–944
- periodic loading 930–932
single station variability see aleatory variability, single station standard deviation
site classification 436–441
- geology-based 439, 440–441
- geotechnical-based 439–441, 441
- V_S30-based 436–439, 438, 439, 551
slowness 371
Snell's law 103, 976
soil behavior type index 346, 347, 347–349, 646
soil classification 284–288
soil density 324–325, 368, 656, 658, 659, 660, 667
soil fabric 324, 353–354, 654
soil hysteretic damping see material damping
soil improvement 867–868, 868
- applicability 867–868, 868
- biological techniques 889
- densification techniques 869–878
- drainage techniques 887–889
- grain size characteristics 868, 868
- grouting techniques 881–883
- mixing techniques 883–887
- reinforcement techniques 878–881
- verification techniques 890–892
stability analysis
- landslide monitoring 799
- pseudostatic 804–810, 830–832
- rock slopes 844–852
- sliding block analysis 810–830
- static 800–803
