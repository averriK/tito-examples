## SLOT 1: Distance probability density function for the circular areal source

Consider a site located at the center of a circular areal source of radius $R$ with uniformly distributed seismicity. The source occupies a disk-shaped region in the horizontal plane, and earthquakes may originate at any location within this disk with equal probability per unit area. For the derivation of the distance probability density function, the seismicity is assumed to be homogeneously distributed over the source area, such that the probability of an earthquake occurring in a differential area element is proportional to that area element. [KB:hazard.qmd]

^[Confidence: HIGH, Rationale: This description of the circular areal source geometry and uniform seismicity assumption is consistent with the general PSHA framework provided in KB:hazard.qmd, which treats earthquakes as occurring according to spatial probability distributions over source regions.]

The differential area element at distance $r$ from the site, in a thin annulus of thickness $dr$, is given by the circumference times the radial thickness: $dA = 2\pi r\,dr$. Since the total area of the circular source is $A_{\text{total}} = \pi R^2$, the probability that a randomly chosen earthquake occurs in the annulus between $r$ and $r + dr$ is proportional to the ratio of the differential area to the total area. Normalization over the domain $[0, R]$ yields the probability density function for source-to-site distance. [KB:hazard.qmd]

^[Confidence: HIGH, Rationale: This is a straightforward geometric derivation from the area element of a disk. The uniform seismicity assumption and the geometric relationship are both clearly established in the KB hazard framework, and the normalization follows directly from the fundamental definition of a probability density function.]

$$
f_R(r) = \frac{2\pi r\,dr}{\pi R^2}\,\frac{1}{dr} = \frac{2r}{R^2}, \quad 0 \le r \le R.
$$

The cumulative distribution function $F_R(r)$, representing the probability that source-to-site distance is less than or equal to $r$, is obtained by integrating the probability density function over the interval $[0, r]$. [KB:hazard.qmd]

^[Confidence: HIGH, Rationale: The cumulative distribution is derived by integrating the probability density function. This operation is fundamental to probability theory and is applied to convert the PDF into its cumulative form.]

$$
F_R(r) = \int_0^r f_R(u)\,du = \int_0^r \frac{2u}{R^2}\,du = \frac{r^2}{R^2}, \quad 0 \le r \le R.
$$

The result satisfies the properties of a CDF: $F_R(0) = 0$ and $F_R(R) = 1$. This derivation is entirely consistent with standard probability theory and the geometric constraints of the circular source model.

^[Confidence: HIGH, Rationale: The mathematical result follows directly from integration and satisfies all required properties of a cumulative distribution function. The boundary conditions and limits of integration are correctly applied.]

