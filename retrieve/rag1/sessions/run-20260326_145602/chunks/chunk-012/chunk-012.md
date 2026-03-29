$\lambda = -\frac{\ln(1-p)}{t} = 0.001026$ per year

which corresponds to a return period of 974.8 years. Approximating the PGA hazard curve in the vicinity of this hazard level by a power law function, two points that bracket the mean annual rate of exceedance of interest can be selected. From Figure E4.4b, the PGA values for return periods of 475 years (10% probability of exceedance in 50 years) and 2,475 years (2% probability of exceedance in 50 years) are 0.18g and 0.29g, respectively. Then from Equation (5.22),

$$k = -\frac{\ln\!\bigl(\lambda_{IM}(im_1)/\lambda_{IM}(im_2)\bigr)}{\ln(im_2/im_1)} = -\frac{\ln(0.000404/0.00211)}{\ln(0.29/0.18)} = 3.466$$

$$\lambda_{IM}(im) = \lambda_{IM}(im_1)\cdot\!\left(\frac{im}{im_1}\right)^{-k} = 0.00211 \times (0.18)^{3.466} = 0.00000553 = 5.53\times10^{-6} \text{ per year}$$

Expressing the settlement model in the power law form of Equation (5.23), $a = 20$ and $b = 0.2$. Then, making use of Equation (5.24) and solving for $\mathrm{edp} = s$, with $\lambda_S(s) = 0.001026$,

$$s = \left[\frac{\lambda_S(s)}{k\,a^{-k/b}\exp\!\left(\dfrac{k^2\beta_R^2}{2b^2}\right)}\right]^{b/k} = \left[\frac{0.001026}{5.53\times10^{-6}\,\exp\!\left(\dfrac{3.466}{2(0.5)}\,(0.2)^2\right)}\right]^{1/2.479} = 5.41\text{ cm}$$

## 5.6 Implementation of Performance-Based Design and Evaluation

Performance-based design and evaluation can be implemented into engineering practice in a number of different ways. Different implementation approaches must address two main matters – the manner in which earthquake loading is specified and the manner in which performance is evaluated. The design process involves an iterative series of performance evaluations after each of which the predicted performance is compared with the performance objectives, and the design is modified until all performance objectives have been met. The performance evaluations may be based on measures of response, damage, or loss. The primary elements of alternative implementation procedures are illustrated in Table 5.2 and described in the following sections. In the simplest approach, PBEE can be implemented at the response level, i.e., by specifying performance in terms of EDP values at different response return periods. In this approach, physical damage must be inferred from the computed response and loss must be inferred from the inferred damage. These compounded inferences may be guided by judgment and experience but must be recognized as leading to highly variable loss estimates. An intermediate approach would be to specify performance in terms of response limit states, which involves the explicit comparison of predicted and allowable response; this approach could also be used to predict DMs with consideration of response and damage model dispersions. Loss would still need to be inferred, but inferring loss from computed damage levels is more accurate than inferring it from computed response levels. The most complete level of implementation would involve defining performance in terms of losses (DVs), which would then require explicitly modeling response, damage, and loss with consideration of the dispersion inherent in each. While requiring more information and more effort, this approach would provide the most accurate (i.e., least biased) and most precise estimate of loss.

### 5.6.1 Scalar and Vector Approaches

The range of soil-structure systems to which performance-based principles can be applied is broad, varying from small, individual structures or soil deposits to large bridges or buildings with many structural and non-structural components. The scope and complexity of the system can influence the manner in which performance-based concepts are implemented, but the basic components are consistent.

**TABLE 5.2 — Main Elements of Alternative Performance Design Procedures**

Performance Evaluation Level: Loading / Response / Damage / Loss

Select ground motion intensity measures (IMs). Develop performance criteria in terms of EDPs. Select response parameters (EDPs). Select response parameters (EDPs). Select response parameters (EDPs). Select damage measures (DMs). Select damage measures (DMs). Select loss measures (DVs). Select ground motion hazard. Select response model. Characterize damage limit states. Characterize loss levels. Develop initial design. Develop performance criteria in terms of DVs. Compute ground motion hazard curve. Compute response. Develop performance criteria in terms of DMs. Select response model. Compare computed response with performance criteria. Select response model. Select damage model. Iterate until performance criteria satisfied. Select damage model. Select loss model. Develop initial design. Develop initial design. Compute response. Compute response. Compute damage. Compute damage. Infer damage from computed response. Compare computed damage with performance criteria. Compute loss. Compare computed loss with performance criteria. Infer loss from inferred damage. Iterate until performance criteria satisfied. Iterate until performance criteria satisfied. Infer loss from computed damage. Loss directly computed.

Losses borne by the simplest systems can often be dominated by a single quantity (such as repair cost) that results from a single damage mechanism (e.g., floor slab cracking). If that damage mechanism is associated with a single measure of response (post-earthquake settlement) that is closely correlated to a particular ground motion intensity measure (peak ground velocity), a scalar approach (one IM, one EDP, one DM, and one DV) to performance-based design/evaluation may be reasonable and appropriate. The scalar approach is relatively simple and straightforward, and will be used to illustrate implementation of performance-based concepts in the following sections. More complex systems, however, may need multiple IMs, EDPs, DMs, and DVs in order to evaluate performance more accurately and thoroughly. Consider a large building, for example. The building has multiple structural components – beams, girders, columns, braces, shear walls, foundations, and their respective connections – each or all of which can be damaged by earthquake shaking. The building also has essential non-structural systems – exterior cladding, internal partitions, piping, electrical, fire suppression (sprinkler), stairway, elevator, and other systems – each or all of which can also be damaged by earthquake shaking. There are also the contents of the building – people (the number of which can vary dramatically over the course of a day or week, depending on the type of building) and inventory (which may be fixed or variable and may, for example in the case of a museum, have a value greater than that of the building itself). Thus, the "building" itself is a quite complicated system with a variety of important components. The different components of a building may have different dynamic response characteristics. Depending on its stiffness and mass, the building's response may be governed by its fundamental mode of vibration or may also be influenced by higher modes, in which case spectral accelerations at multiple periods may be required as IMs. The residual drift of the building can be another important measure of response since excessive permanent drift can lead to significant damage resulting in high repair costs, or even require demolition of the structure. The foundation system's response may be more closely related to ground deformation/strain, so ground displacement may be required as an IM to accurately predict its performance. The dynamic response of piping systems, suspended ceilings, etc., and of the contents of the building are going to depend on the motions of their supports, which will vary from floor to floor; hence, individual floor spectra may be required as inputs to their analysis. While some components of the building that have similar response characteristics can be aggregated into performance groups, it is clear that multiple IMs and multiple EDPs may be required for accurate prediction of response. All of these measures of response must be recognized as having substantial aleatory variability and many of them as being correlated to each other. Damage is even more difficult to quantify than response – it results from highly nonlinear processes that depend on complex material behavior that is often difficult to characterize, and there is often little actual damage data from which to construct empirical damage models. While response tends to occur on continuous scales, damage tends to be more discrete and is often described in a categorical manner. The different components of the building are also susceptible to different forms of damage. Damage to a reinforced concrete column is different than damage to a welded connection or to a statue on a pedestal in an art museum, so multiple DMs are needed for different structural and non-structural components of a building. The complexity of damage processes leads to significant uncertainty even when the response is known. Additional uncertainty comes from the fact that the future contents and/or uses of the building may not be known as tenants and technologies change. A loss-level implementation requires a probabilistic loss model, and loss models can have different degrees of complexity. The notion of losses having direct and indirect economic, and casualty-related components (Section 5.3.4) implies that three loss models may be required, or that the three components of loss must be expressed in consistent (usually economic) terms, which involves the extremely difficult problem of defining economic losses associated with casualties. However, even direct economic losses can have multiple components – structural damage, non-structural damage, damage to contents, etc. – and these components interact with each other in complex, correlated manners that must be accounted for in a complete loss model. Similarly, indirect losses can have multiple components that are correlated with each other, and with direct losses. Losses also have the additional complexity of time-dependence as important factors such as local material and labor costs (particularly in the period shortly after a major earthquake), inflation, interest rates, and other economic factors can vary significantly over the time scales of interest in performance-based evaluation and design. These factors can introduce very high levels of variability and uncertainty into loss models.

### 5.6.2 Characterization of Ground Motion Intensity

Characterization of earthquake loading first requires selection of one or more ground motion intensity measures. The selection, however, must be made with consideration of the system response of greatest interest. Ground motion intensity measures should ideally be predictable, efficient, and sufficient (Section 3.3). Intensity measure predictability refers to the aleatory variability associated with an IM prediction given an earthquake scenario; this variability is characterized by the standard deviation term in the ground motion model (GMM) for that IM. Different IMs have been shown to have different levels of predictability (Section 3.5.4.3). The predictabilities are highly variable – cumulative absolution velocity, CAV, has very good predictability while the predictability of Arias intensity is poor. Intensity measure efficiency refers to the conditional aleatory variability in response given ground motion intensity (Section 3.3). Efficient intensity measures (Section 3.3) are those to which the response of interest is closely related, i.e., for which $\sigma_{\ln EDP|IM}$ is low. In a sense, efficiency can be thought of as a measure of the relevance of an IM to the problem of interest. Figure 5.6 shows examples of inefficient and efficient intensity measures for computed foundation settlement; here, CAV can be seen to be a more efficient predictor of displacement than PGA and D5-75 duration by itself to be quite inefficient.

FIGURE 5.6 Correlation between computed foundation settlement and (a) CAV, (b) PGA, and (c) D5-75. (Courtesy of Z. Bullock.) Lower dispersion of settlement corresponds to higher efficiency of its prediction.

Sufficient IMs are those for which consideration of additional parameters does not reduce the uncertainty in predicted response. Some measures of response are so strongly correlated to a single ground motion characteristic that their values can be accurately predicted based on a single IM. Other problems, however, may be influenced by multiple ground motion characteristics. Soil liquefaction (Chapter 9), for example, is affected by both the amplitude and duration of a ground motion, hence PGA alone is an insufficient predictor of liquefaction. In such cases, more than one parameter (e.g., PGA and earthquake magnitude, which serves as a proxy for duration) may be required to predict response efficiently. The second important aspect of earthquake loading characterization concerns the number of hazard levels, or return periods, to be considered in the design. Earthquake loading can be specified in terms of a discrete number of hazard levels, such as the four levels (frequent, occasional, rare, and very rare) proposed by Vision2000 (Figure 5.2), or integrated over a continuous scale as utilized in the PEER approach (Section 5.5.2.2). Using a discrete hazard level approach requires evaluation of performance at each hazard level, hence the level of engineering effort required to develop an acceptable design increases with increasing number of discrete hazard levels. With the integral hazard approach, the variation of response over a wide range of ground shaking (i.e., that associated with all anticipated hazard levels), is required. This may involve many more response analyses than would be performed in a conventional design process, but it provides a more complete characterization of performance.

### 5.6.3 Response-Level Implementation

A response-level implementation of PBEE assumes that performance can be judged in terms of response variables such as interstory drift for buildings, peak lateral displacement for bridges, permanent ground displacement for slopes, etc. In this approach, predicted values of the response parameters, i.e., the EDPs, are compared with allowable values of those parameters (also known as acceptance criteria in structural applications) to determine whether performance objectives have been met. Exceedances of allowable values imply some level of damage, and consequently some level of loss. As illustrated in Table 5.2, however, the damage has to be inferred from the computed response, and the loss is inferred from the inferred damage. The allowable level of response can be viewed as a capacity, i.e., a threshold beyond which some levels of damage and loss are anticipated. Such capacity thresholds are often referred to as limit states since they represent a limit beyond which a different consequence is expected. For most problems, particularly in geotechnical earthquake engineering, the capacities themselves must be considered to be variable. Representing an EDP level, $C$, as a random variable that describes a response capacity, the mean annual rate at which a scalar value of that capacity, $C = c$, would be exceeded can be computed using the total probability theorem,

$$\lambda_{EDP}(c) = \sum_{i=1}^{N_{IM}} P[EDP > c \mid IM = im_i]\,P[IM = im_i]\,\lambda_M^{\min} \tag{5.29}$$

where $\lambda_M^{\min}$ is the mean annual rate of earthquakes exceeding some minimum magnitude. If $C$ is not accurately known, it can be treated as a random variable so the mean annual rate of the capacity exceedance limit state, i.e., $LS = EDP > C = c$, would be given by

$$\lambda_{LS}(c) = \int_0^{\infty} \lambda_{EDP}(c)\,f_C(c)\,dc \tag{5.30}$$

where $f_C(c)$ is the probability density function for capacity $C$ (equivalent to the derivative of a fragility curve). Equations (5.29) and (5.30) show that a hazard curve for limit state exceedance can be evaluated from the IM hazard curve, the (probabilistic) relationship between IM and EDP, and the distribution of capacity. Design ground motions used in current U.S. building codes (e.g., NEHRP, 2020) [@NEHRP2020] are derived using Equation (5.30). The design objective is a specific rate of collapse (1% probability of collapse in 50 years), and calculations are performed to find a capacity that meets that objective. In these calculations, a ground motion hazard curve is combined with a collapse fragility curve that is assumed to be lognormal with a specified variability ($\lambda_{EDP|IM}$). The median of that fragility curve depends on the structural capacity or strength (which, in turn, is related to the design spectral acceleration level). For each location in a grid across the U.S., the integration is performed repeatedly for different design spectral accelerations (and hence capacities) until the target collapse risk is achieved [@LucoEtAl2007]. The resulting ground motion is referred to as a risk-targeted maximum considered earthquake ground motion (MCER). The closed-form solution of Section 5.5.3 can be extended to account for lognormally distributed capacity [@Jalayer2003]. Using Equation (5.24), the mean annual rate at which some known load capacity, $C = c$, would be exceeded is

$$\lambda_{EDP}(c) = \frac{k}{a^{k/b}}\,c^{-k/b}\exp\!\left(\frac{k^2\beta_R^2}{2b^2}\right) \tag{5.31}$$

Using Equation (5.30) to account for dispersion in load capacity, the mean annual rate of limit state (capacity) exceedance is given by

$$\lambda_{LS} = \int_0^{\infty} \frac{k}{a^{k/b}}\,c^{-k/b}\exp\!\left(\frac{k^2\beta_R^2}{2b^2}\right) f_C(c)\,dc \tag{5.32}$$

Extracting $c$ from the first term and moving capacity-independent terms out of the integral,

$$\lambda_{LS} = \frac{k}{a^{k/b}}\exp\!\left(\frac{k^2\beta_R^2}{2b^2}\right)\int_0^{\infty} c^{-k/b}\,f_C(c)\,dc \tag{5.33}$$

The remaining term inside the integral is, by definition, the mean value of $c^{-k/b}$. Since the expected value of a lognormal random variable, $Y$, with median $\hat{Y}$ and dispersion $\beta_Y = \sigma_{\ln Y}$, raised to the power $\alpha$ is given by

$$E[Y^\alpha] = E[e^{\alpha\ln Y}] = \hat{Y}^\alpha \exp\!\left(\tfrac{1}{2}\alpha^2\beta_Y^2\right) \tag{5.34}$$

Equation (5.33) becomes

$$\lambda_{LS} = \frac{k}{a^{k/b}}\,\hat{C}^{-k/b}\exp\!\left(\frac{k^2\beta_R^2}{2b^2}\right)\exp\!\left(\frac{k^2\beta_C^2}{2b^2}\right) \tag{5.35}$$

where $\hat{C}$ is the median capacity. This relationship can be simplified to

$$\lambda_{LS} = \frac{k}{a^{k/b}}\,\hat{C}^{-k/b}\exp\!\left(\frac{k^2(\beta_R^2+\beta_C^2)}{2b^2}\right) \tag{5.36}$$

Thus, the mean annual rate of limit state exceedance can be seen to increase with increasing aleatory variability in capacity as well as in response.

#### Example 5.3

The building for which settlement was estimated in Example 5.2 is expected to experience severe damage at a settlement that exceeds 20 cm. Assuming this descriptive measure of capacity to be lognormally distributed with $\sigma_{\ln C} = 0.3$, estimate the return period at which severe damage is likely to occur.

#### Solution

Taking the 20 cm severe damage limit state boundary as the median capacity and using Equation (5.36), the mean annual rate of limit state exceedance is calculated as

$$\lambda_{LS} = \frac{k}{a^{k/b}}\,\hat{C}^{-k/b}\exp\!\left(\frac{k^2(\beta_R^2+\beta_C^2)}{2b^2}\right) = \frac{0.0027\times(30)^{-2.479/0.5}}{\exp(2.479)\,\cdot\,0.2\,\cdot\,0.3} = 0.000547\text{ per year}$$

which gives a limit state return period of 370.4 years.

This closed-form solution, while conceptually quite clear and simple, must be recognized as being based on a local approximation to the hazard curve because actual ground motion hazard curves tend to be nonlinear (concave-down) in log-log space. Its accuracy, therefore, is influenced by how the assumed power law IM hazard curve is fit to the actual IM hazard curve. The original approach of fitting a line tangent to the IM hazard curve at the IM level corresponding to the median capacity [@Jalayer2003], i.e., at $im = (\hat{C}/a)^{1/b}$, provides a conservative result since the tangent will always be above a concave-down hazard curve. At short return periods, where actual IM hazard curves tend to be more linear, the approach is more accurate than at long return periods. However, with the exception of highly vulnerable structures that can fail under weak shaking, earthquake engineers are usually more interested in performance at relatively long return periods. The error associated with the tangent approach becomes excessive with increasing IM hazard curve curvature and dispersion of capacity [@AslaniMiranda2005][@BradleyDhakal2008]. It can be substantially reduced, however, by selecting biased (toward shorter return periods) values of the points, $im_1$ and $im_2$, used to define a secant approximation (in Equation 5.22) to the IM hazard curve [@Vamvatsikos2014]. Letting $edp_C$ represent the EDP value corresponding to the median capacity $\hat{C}$, the IM values

$$im_1 = \left(\frac{edp_C}{a}\right)^{1/b}\exp\!\left(-\frac{\beta_R^2+\beta_C^2}{b}\right) \tag{5.37a}$$

$$im_2 = \left(\frac{edp_C}{a}\right)^{1/b}\exp\!\left(+\frac{\beta_R^2+\beta_C^2}{b}\right) \tag{5.37b}$$

can be used with Equation (5.22) to develop an IM hazard curve approximation that produces a more accurate estimate of $\lambda_{LS}$.

The issue of IM hazard curve curvature can be more appropriately addressed, however, by relaxing the power law restriction. Bradley et al. (2007) [@BradleyEtAl2007] developed a semi-analytical solution based on a hyperbolic representation of the IM hazard curve. Vamvatsikos (2013) [@Vamvatsikos2013] derived a closed-form solution for a ground motion hazard curve that is quadratic in log-log space:

$$\ln\lambda_{IM}(im) = -k_0 - k_1\ln(im) - k_2[\ln(im)]^2 \tag{5.38}$$

The mean annual rate of limit state exceedance for this case can be expressed most compactly as

$$\lambda_{LS} = \phi\,\lambda_{IM}(\hat{im}_C)\exp\!\left(\frac{q\,k_1^2\beta_R^2\beta_C^2}{2b^2}\right) \tag{5.39}$$

where $\hat{C}$ is the median capacity, $\hat{im}_C$ is the intensity measure corresponding to the EDP value that produces the median capacity, i.e., $\hat{im}_C = (\hat{C}/a)^{1/b}$, and

$$\phi = \exp\!\left[\frac{(k_1/b+k_2\beta_R^2)^2}{2k_2}\right]\bigg/\sqrt{k_2}$$

$$q = k_1 + k_2\beta_R^2/b$$

$$\lambda_{IM}(\hat{im}_C) = \exp\!\bigl[-k_0 - k_1\ln(\hat{im}_C) - k_2(\ln\hat{im}_C)^2\bigr]$$

If the coefficient of the quadratic term in the hazard curve is set to zero, the values of $\phi$ and $q$ go to 1.0 and the limit state exceedance rate becomes equal to the first order rate given in Equation (5.36).

### 5.6.4 Damage-Level Implementation

While response tends to occur on continuous, quantifiable scales, damage tends to be divided into discrete, and often descriptive, damage states. Thus damage can be described by damage probability matrices [@WhitmanEtAl1973] or by a finite number of fragility curves, each corresponding to a particular damage state, or category. A damage probability matrix is a type of discrete probability matrix (Section 5.5.1) that describes the probabilities of various damage levels (or states) conditional upon various response levels. In a discrete damage-level implementation, EDP and DM take the places of X and Y in Equations (5.1)–(5.3); for an evaluation with five damage states being caused by five response levels, Equation (5.40) expresses the matrix relationship between the damage state probability vector and the EDP probability vector through the damage probability matrix whose columns must each sum to 1.0.

The probabilities in each of the columns of the damage probability matrix must sum to 1.0, indicating that the damage measures are exhaustive, i.e., that a given EDP value must fall into one of the discrete damage levels. As an example, damage to a five-span bridge typical of that designed by the California Department of Transportation supported by piles extending through liquefiable soils that were susceptible to lateral spreading was assessed using a sophisticated finite element analysis [@KramerEtAl2008]. The pile foundations interacted with the soil through p-y, t-z, and Q-z springs. With an absence of empirical or analytical damage data, a group of experts was polled to aid in identifying five discrete, descriptive foundation damage states based on computed pile head displacement. The results of that poll were used in development of the discrete probability matrix shown in Table 5.3. It should be noted that the values in Table 5.3 applied to the specific soil/foundation/structure system being considered, and that a different damage probability matrix would need to be defined for a different system. For structural elements of the bridge, experimental data from the PEER structural performance database [@BerryEtAl2004] were used to establish fragility curve data for discrete damage states. For the bridge columns, four damage states were related to maximum drift ratio, as shown in Figure 5.7. Whereas the damage states and probabilities in the pile foundation damage model were both discrete, in this approach the damage states were discrete but the probabilities were continuous.

**TABLE 5.3 — Damage Probability Matrix for Pile Foundations Supporting Bridge in Liquefiable Soils [@KramerEtAl2008]**

Pile Head Displacement Range (cm), EDP / Damage State, DM / <4 / 4−10 / 10−30 / 30−100 / >100

Negligible: 0.95, 0.05, 0.00, 0.00, 0.00. Slight: 0.05, 0.80, 0.20, 0.05, 0.00. Moderate: 0.00, 0.10, 0.60, 0.25, 0.05. Severe: 0.00, 0.05, 0.15, 0.55, 0.10. Catastrophic: 0.00, 0.00, 0.05, 0.15, 0.85.

FIGURE 5.7 Fragility curves for discrete column damage states.

FIGURE 5.8 Categorical damage hazard curve for pile foundations supporting bridge in liquefiable soil profile.

Alternatively, damage states can be defined in terms of levels at which different expected repair actions would be triggered or at which different levels of casualties would be expected (e.g., collapse vs. non-collapse). Both the pile foundation and bridge column damage models were convolved with the EDP hazard curve to produce damage hazard curves (Figure 5.8). Since the damage states are categorical, the DM hazard curves are also categorical in nature. By assigning a numerical damage intensity to each categorical damage state (e.g., negligible = 0, slight = 0.1, … catastrophic = 1.0), the damage model can be formulated so that DM is a continuous function of EDP; such assignments, however, may require considerable judgment.

### 5.6.5 Loss-Level Implementation

The most complete evaluation of performance can be accomplished by specifying it in terms of losses. Such evaluations represent the ultimate expression of PBEE and are likely to be justified primarily for particularly large and/or important projects in the near future. Nevertheless, they provide a useful and instructive look into the future of earthquake engineering practice. They also can be used to demonstrate the economic value of earthquake engineering services. As with damage models, loss models are often expressed in terms of discrete ranges, or categories, of loss. In such cases, the loss model can be expressed in terms of a loss probability matrix. Loss models can also be complicated by discontinuities. While response increases with increasing ground motion level, and damage increases with increasing response, the loss for some components of a soil-structure system can increase or decrease with increasing ground motion intensity and can do so in large jumps or drops. Consider a reinforced concrete bridge column, for example. The cost of repair for relatively weak shaking can consist of that associated with epoxying cracks or repairing spalls that appear under somewhat stronger shaking. Under strong shaking, rebar may buckle and repair may involve adding a steel jacket and grouting the annular space, in which case the cost of repairing spalls drops to zero. Finally, under very strong shaking, the column could be damaged beyond repair, in which case would need to be replaced and the previously described repairs would become irrelevant and their cost would drop to zero. Loss-level implementation must also consider the specific form of the decision variable(s) used to describe the loss. Insurers and real estate investors, who may be making decisions on performance objectives for design or retrofit, have preferred metrics for describing potential losses. Probable maximum loss (PML) is a term that was defined differently by different entities until ASTM developed standards (E2026 for seismic risk assessments and E2557 for PML reports) in 1999. Recent updates to these standards suggest replacement of the term PML with Scenario Expected Loss (SEL) and Scenario Upper Loss (SUL), which represent losses with exceedance probabilities of 50% and 10% in either probabilistic scenarios (e.g., 475-year ground motion) or specific deterministic scenario events. The term, probable loss (PL) is also used to describe the loss value itself that has a 10% probability of exceedance in 50 years. The preceding measures of loss refer primarily to individual structures or facilities. From a regional standpoint, however, the losses suffered by a community can be associated with multiple, interdependent systems such as buildings, bridges, pipelines, and electrical lines. Lifeline infrastructure systems such as transportation, water and wastewater, energy, and communications systems, are critical to the safety, security, and economic prosperity of a region and the amount of time such systems are out of service represents a loss that may dwarf the direct costs of repairing their physical damage. The concept of functional recovery (Section 5.3.4) has been developed to improve community resilience. Design for functional recovery involves consideration of both safety and recovery time and can be applied to both individual structures or regional building/infrastructure systems.

## 5.7 Vector PBEE Analyses

The implementation procedures discussed in the preceding section focused on scalar measures of response, damage, and loss, and such scalar measures may be reasonable and appropriate. For complex soil-structure systems, however, different components of the overall system may require individual measures of response, damage, and/or loss. Permanent displacements of unstable slopes (Chapter 10) can, for example, be predicted more accurately using a vector (PGA and PGV) intensity measure than using either (PGA or PGV) by themselves as scalar IMs. Flexible structures may have multiple modes of shaking excited by a given ground motion, in which case accurate prediction of their response may require determination of spectral acceleration at multiple periods. Scalar performance evaluations can be extended to consider multiple measures of ground motion, response, damage, and loss. Such analyses are often referred to as vector analyses since the IMs, EDPs, DMs, and/or DVs are represented as vector, rather than scalar, quantities. Section 4.4.3.2 discussed vector PSHAs, which produce a vector of IMs with some mean annual rate (or return period) of joint exceedance. The benefit of a vector IM is that it can describe the characteristics of an earthquake ground motion more completely than a single, scalar IM. For example, a vector IM consisting of spectral accelerations at two periods can describe the ground motion amplitude over a broad range of frequencies that may significantly affect the response of a structure (particularly if its natural period lengthens due to damage-induced softening, or if a higher mode at a shorter period contributes significantly to its response), whereas a scalar spectral acceleration may represent the amplitude of the motion over only a narrow range of frequencies.

### 5.7.1 Scalar EDP from Vector PSHA

The results of a vector PSHA may allow more accurate (and less variable) estimates of a single EDP. A response (demand) hazard curve for a scalar EDP can be computed for a two-component vector IM as

$$\lambda_{EDP}(edp) = \int\!\int P\bigl[EDP > edp \mid IM_1 = im_1,\,IM_2 = im_2\bigr]\,MRD_{IM_1,IM_2}(im_1,im_2)\,d\,im_1\,d\,im_2 \tag{5.41}$$

where $MRD_{IM_1,IM_2}(im_1,im_2)$ is the joint mean rate density (Equation 4.36), or equivalently,

$$\lambda_{EDP}(edp) = \int_1\!\int P\bigl[EDP > edp \mid IM_1 = im_1,\,IM_2 = im_2\bigr]\,f_{IM_2|IM_1}(im_2\mid im_1)\,MRD_{IM_1}(im_1)\,d\,im_2\,d\,im_1 \tag{5.42}$$

where the conditional IM distribution can be computed as

$$f_{IM_2|IM_1,M,R}(im_2\mid im_1,m,r) = \int\!\int f_{IM_2|IM_1,M,R}(im_2\mid im_1,r,m)\,f_{M,R|IM_1}(m,r\mid im_1)\,dr\,dM \tag{5.43}$$

and the quantity $f_{IM_2|IM_1,M,R}$ depends on the GMMs for $IM_1$ and $IM_2$ and on the correlation between the two IMs. Discretizing $IM_1$ and $IM_2$ into $N_{IM_1}$ and $N_{IM_2}$ values, the mean annual rate of EDP exceedance can be approximated as

$$\lambda_{EDP}(edp) \approx \sum_{i=1}^{N_{IM_1}}\sum_{j=1}^{N_{IM_2}} P\bigl[EDP > edp \mid IM_1 = im_{1,i},\,IM_2 = im_{2,j}\bigr]\cdot P\bigl[IM_2 = im_{2,j}\mid IM_1 = im_{1,i}\bigr]\cdot\Delta\lambda_{IM_1}(im_{1,i}) \tag{5.44}$$

where $P[EDP > edp \mid IM_1 = im_{1,i},\,IM_2 = im_{2,j}]$ is obtained from probabilistic response analyses (Section 5.7.3), and the conditional probability of $im_2$ given $im_1$ is computed as

$$P\bigl[IM_2 = im_{2,j}\mid IM_1 = im_{1,i}\bigr] = \sum_{k=1}^{N_M}\sum_{n=1}^{N_R} P\bigl[IM_2 = im_{2,j}\mid IM_1 = im_{1,i},\,M = m_k,\,R = r_n\bigr]\cdot P\bigl[R = r_n\mid IM_1 = im_{1,i}\bigr] \tag{5.45}$$

and

$$\Delta\lambda_{IM_1}(im_{1,j}) = \lambda_{IM_1}(im_{1,j}) - \lambda_{IM_1}(im_{1,j+1}) \tag{5.46}$$

Assuming $IM_1$ and $IM_2$ are jointly lognormal [@JayaramBaker2008], the first term in the summation of Equation (5.45) can be computed as

$$P\bigl[IM_2 = im_{2,j}\mid IM_1 = im_{1,i},\,M = m_k,\,R = r_n\bigr] = \Phi\!\left(\frac{\ln im_{2,j+1} - \mu_{\ln IM_2|IM_1,m,r}}{\sigma_{\ln IM_2|IM_1,m,r}}\right) - \Phi\!\left(\frac{\ln im_{2,j} - \mu_{\ln IM_2|IM_1,m,r}}{\sigma_{\ln IM_2|IM_1,m,r}}\right) \tag{5.47}$$

where

$$\mu_{\ln IM_2|IM_1,m_k,r_n} = \mu_{\ln IM_2|m,r} + \rho_{\ln IM_1,\ln IM_2}\,\sigma_{\ln IM_1|m,r}\,\frac{im_{1,i} - \mu_{\ln IM_1|m,r}}{\sigma_{\ln IM_1|m,r}} \tag{5.48}$$

$$\sigma_{\ln IM_2|IM_1,m_k,r_n} = \sigma_{\ln IM_2|m,r}\sqrt{1 - \rho_{\ln IM_1,\ln IM_2}^2} \tag{5.49}$$

and $\Phi(\cdot)$ is the cumulative distribution function of the standard Gaussian distribution.

### 5.7.2 Vector EDP from Vector PSHA

The results of a vector PSHA can also be used to compute a vector response (demand) hazard relationship, which can be useful when the relevant response of a system is described by more than one engineering demand parameter. The ability to predict multiple EDPs can lead to more accurate (i.e., less variable) damage estimates. Considering a two-component vector of response, $\mathbf{EDP} = \{EDP_1, EDP_2\}$, the response hazard can be defined in different ways [@Barbosa2011], for example as (i) the mean annual joint rate of events $\{(EDP_1 > edp_1)\text{ or }(EDP_2 > edp_2)\}$, or (ii) the mean annual rate of joint events $\{(EDP_1 > edp_1)\text{ and }(EDP_2 > edp_2)\}$, which obviously have different meanings and implications.

#### 5.7.2.1 Joint Rate of Events

In some situations, a given level of damage may occur if any one of a set of multiple potential levels of response is exceeded. Considering the rate at which either $EDP_1 > edp_1$ or $EDP_2 > edp_2$ for a two-component EDP vector, the scalar formulation can be extended as

$$\lambda_{EDP}(edp_1,edp_2) = \int P\bigl[EDP_1 > edp_1 \cup EDP_2 > edp_2 \mid IM = im\bigr]\,d\lambda_{IM}(im) \tag{5.50}$$

which can be written, changing from the union to the intersection of events, as

$$\lambda_{EDP}(edp_1,edp_2) = \int P\bigl[1 - (EDP_1 \leq edp_1 \cap EDP_2 \leq edp_2) \mid IM = im\bigr]\,d\lambda_{IM}(im) \tag{5.51}$$

or

$$\lambda_{EDP_1\text{ or }EDP_2}(edp_1,edp_2) = \int \bigl[1 - F_{EDP_1,EDP_2|IM}(edp_1,edp_2)\bigr]\,d\lambda_{IM}(im) \tag{5.52}$$

where $F_{EDP_1,EDP_2|IM}(edp_1,edp_2)$ is the joint CDF of $EDP_1$ and $EDP_2$ conditional upon $IM$, and can be computed as

$$F_{EDP_1,EDP_2|IM}(edp_1,edp_2) = \int_0^{edp_1}\!\int_0^{edp_2} f_{EDP_1,EDP_2|IM}(u_1,u_2)\,du_1\,du_2 \tag{5.53}$$
