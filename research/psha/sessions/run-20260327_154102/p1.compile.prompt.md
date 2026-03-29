# Structured Prompt: Particularization of PSHA Equations for a Single Circular Areal Source

This prompt defines the scope and deliverables for an analytical derivation that particularizes the general probabilistic seismic hazard analysis (PSHA) equations to the case of a stable continental crust region with no known finite faults, a single circular areal source of radius $R$ (on the order of 600 km) with uniformly distributed seismicity surrounding the site of study, and negligible contribution from sources beyond $R$. The source is characterized by the Gutenberg-Richter parameters $a$ and $b$, a minimum engineering magnitude $M_{\min}$, and a maximum earthquake magnitude $M_{\max}$. The general equations in `kb/hazard.qmd`, `kb/disaggregation.qmd`, and `kb/uncertainty_model.qmd` serve as the starting point; all derivations particularize those expressions to the single circular source geometry.


## SLOTS

### SLOT 1: Distance probability density function for the circular areal source

Derivation of the probability density function of source-to-site distance, $f_R(r)$, for a site located at the center of a circular areal source of radius $R$ with uniformly distributed seismicity. The derivation proceeds from a geometric justification based on the differential area element $dA = 2\pi r\,dr$, followed by normalization over the domain $[0, R]$. The cumulative distribution function $F_R(r)$ is also required as part of this slot.


### SLOT 2: Particularized annual exceedance rate for the single circular source

Starting from the general hazard integral (@eq-hazard-integral in `kb/hazard.qmd`), development of the particularized annual exceedance rate $\lambda_I(i^*)$ for the single circular areal source with parameters $a$, $b$, and $M_{\max}$, incorporating the distance PDF $f_R(r)$ derived in SLOT 1. The derivation explicitly states the following intermediate components: (i) the annual occurrence rate $\nu_0 = 10^{a - b\,M_{\min}}$; (ii) the truncated Gutenberg-Richter magnitude PDF $f_M(m)$, consistent with @eq-branch-pdf in `kb/uncertainty_model.qmd`; (iii) the conditional exceedance probability $P[I > i^* \mid m, r]$ expressed through a generic GMPE in terms of the median $\hat{\eta}_I(m,r)$ and the logarithmic standard deviation $\sigma_{\ln I}$; and (iv) the final double integral expression over magnitude $m$ and distance $r$.


### SLOT 3: Maximum credible earthquake ground-motion intensity

Development of the expression that estimates the ground-motion intensity of the maximum credible earthquake (MCE) at the site. The derivation considers an event with magnitude $M_{\max}$ at distance $r$ and determines the intensity $i^*_{\text{MCE}}$ such that its annual exceedance probability equals a target AEP (for example, $\text{AEP} = 1/T_R$ for a given return period $T_R$). The AEP relation from @eq-aep in `kb/hazard.qmd` is referenced and linked within the derivation.


### SLOT 4: Joint magnitude-distance disaggregation for the circular source

Using the disaggregation framework from `kb/disaggregation.qmd` (@eq-disagg-rate, @eq-disagg-bin, @eq-disagg-prob), development of the joint $M$-$R$ disaggregation particularized for the circular areal source. Two formulations are required:


- (a) Disaggregation by rate contribution: the fraction of $\lambda_I(i^*)$ attributable to each magnitude-distance bin $(m_k, r_j)$, expressed as $\theta_{k,j}$.


- (b) Disaggregation including the $\varepsilon$ dimension of the GMPE residual: contributions from bins $(m_k, r_j, \varepsilon_\ell)$ together with the marginal distributions $P[M \in m_k \mid I > i^*]$ and $P[R \in r_j \mid I > i^*]$.


Both formulations particularize the PDFs and rates to the circular source with parameters $a$, $b$, $M_{\max}$, and $f_R(r) = 2r/R^2$.


## CONSTRAINTS

- The output document language is English, written in a professional engineering methodology style.


- All derivations adopt the notation established in the KB documents (`kb/hazard.qmd`, `kb/disaggregation.qmd`, `kb/uncertainty_model.qmd`); no alternative symbol conventions are introduced.


- Expressions are presented in analytical closed form whenever possible; cases requiring numerical integration are identified explicitly.


- No specific ground-motion prediction equation (GMPE) is assumed. The conditional exceedance probability is expressed in terms of the generic median $\hat{\eta}_I(m,r)$ and logarithmic standard deviation $\sigma_{\ln I}$.


- No site effects are included; all derivations assume reference rock conditions.

