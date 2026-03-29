*(Fragment — continuation from previous chunk)*

$$P[B \cup A] = P[B] + P[A] - P[B \cap A]$$

$$P[B \cup C] = P[B] + P[C] - P[B \cap C]$$

### D.4.2 Conditional Probability

In many instances, events are related so the probability of one event conditional upon the occurrence of another event is of interest. The conditional probability of event A given the occurrence of event B is denoted $P[A|B]$ and is defined (for $P[B] > 0$) by

$$P[A|B] = \frac{P[A \cap B]}{P[B]} \tag{D.3a}$$

Similarly,

$$P[B|A] = \frac{P[A \cap B]}{P[A]} \tag{D.3b}$$

### Example D.3

One hundred field compaction tests were performed in the early stages of the construction of an earth dam. The results of the tests are presented in terms of the numbers that satisfied specifications for minimum relative compaction and for compaction water content in the table below.

Water Content — Relative Compaction:
Acceptable / Acceptable | Acceptable / Not Acceptable
Not Acceptable / Acceptable | Not Acceptable / Not Acceptable

Assume the contractor's performance in the future will be the same as in the first 100 tests and that the fill material does not change. Estimate the probability that the relative compaction specification will be satisfied in the next test if the water content specification is satisfied. Estimate that probability for the case in which the water content specification is not satisfied.

**Solution:**

Define two events, R and W, such that R = relative compaction specification satisfied; W = water content specification satisfied.

From the table the probability that both the relative compaction and water content specifications are satisfied can be estimated as $P[W \cap R] = 80/100$. Then the probability that the relative compaction specification will be satisfied in the next test if the water content specification is satisfied is the conditional probability $P[R|W]$, which can be computed as

$$P[R|W] = \frac{P[W \cap R]}{P[W]} = \frac{80/100}{80/100 + 10/100} = 0.889$$

The probability that the relative compaction specification is satisfied given that the water content specification is not satisfied can be estimated as $P[R|\overline{W}]$, or

$$P[R|\overline{W}] = \frac{P[\overline{W} \cap R]}{P[\overline{W}]} = \frac{6/100}{6/100 + 4/100} = 0.6$$

The conditional probability is easily visualized with the Venn diagram as the ratio of the area of $A \cap B$ to the area of $B$. Event A is statistically independent of event B if the occurrence does not affect the probability of occurrence of A, i.e., if

$$P[A] = P[A|B] \tag{D.4}$$

Rearranging Equation (D.3a), the probability of the intersection of the independent events A and B is given by

$$P[A \cap B] = P[B] \cdot P[A|B] \tag{D.5}$$

which, if A and B are statistically independent, becomes

$$P[A \cap B] = P[A] \cdot P[B] \tag{D.6}$$

This is known as the multiplication rule and can be extended to the multiple, mutually independent events A, B, C, … , N by

$$P[A \cap B \cap C \cap \cdots \cap N] = P[A] \cdot P[B] \cdot P[C] \cdots P[N] \tag{D.7}$$

The multiplication rule states that the probability of joint occurrence of independent events is equal to the product of their individual probabilities. For a set of mutually exclusive, but collectively exhaustive, events $B_1, B_2, \ldots, B_N$, like that shown in the Venn diagram of Figure D.3, the probability of another event A can be expressed as

$$P[A] = P[A \cap B_1] + P[A \cap B_2] + \cdots + P[A \cap B_N] \tag{D.8}$$

FIGURE D.3 Intersection of event A with collectively exhaustive events $B_i$.

Using Equation (D.4)

$$P[A] = P[A|B_1]P[B_1] + P[A|B_2]P[B_2] + \cdots + P[A|B_N]P[B_N] = \sum_{i=1}^{N} P[A|B_i] P[B_i] \tag{D.9}$$

which is known as the Total Probability Theorem. The Total Probability Theorem allows the unknown probability of an event to be "built" from a series of known conditional probabilities and forms the backbone of the probability calculations required for probabilistic seismic hazard analyses (Chapter 4). The Total Probability Theorem can also be extended to account for multiple dependencies. If, for example, Event C is conditionally dependent on Event B, which is in turn conditionally dependent on Event A, the probability of C can be computed as

$$P[C] = P[C|B] \cdot P[B|A] \cdot P[A] \tag{D.10}$$

This type of "chain" of conditional probabilities can be extended to any number of events; such calculations are performed along individual branches of logic trees (Section 4.4.3.4) in seismic hazard analyses.

### Example D.4

A structural engineer has determined that a structure will collapse in an earthquake that produces a peak acceleration of 0.3g. The probabilities that a given earthquake on fault A, B, or C would be strong enough to cause that level of ground shaking are 0.5, 0.2, and 0.1, respectively. The probabilities that such earthquakes will occur on faults A, B, and C during the life of the building are 0.01, 0.05, and 0.08, respectively. What is the probability that the structure will collapse in an earthquake?

**Solution:**

Define the following events as A = the structure collapses in an earthquake; $D_1$ = an earthquake capable of collapsing the structure occurs on fault A; $D_2$ = an earthquake capable of collapsing the structure occurs on fault B; $D_3$ = an earthquake capable of collapsing the structure occurs on fault C. Then the probability that the structure collapses in an earthquake is given by

$$P[A] = P[A|D_1]P[D_1] + P[A|D_2]P[D_2] + P[A|D_3]P[D_3]$$

$$= (0.5)(0.01) + (0.2)(0.05) + (0.1)(0.10) = 0.025$$

### D.4.3 Bayes' Theorem

Equations (D.3a) and (D.3b) can be solved for $P[A \cap B]$ and then set equal to obtain

$$P[A|B] P[B] = P[B|A] P[A] \tag{D.11}$$

or

$$P[B|A] = \frac{P[A|B] P[B]}{P[A]} \tag{D.12}$$

provided that $P[A] \neq 0$. Note that the order of the conditioning on the left and right sides of Equation (D.12) is reversed; Equation (D.12) allows calculation of $P[B|A]$ when only $P[A|B]$ is known. If B consists of a number of mutually exclusive and collectively exhaustive events, $B_1, B_2, \ldots, B_N$ (as in Figure D.3), the denominator in Equation (D.12) can be replaced by Equation (D.9), giving

$$P[B_i|A] = \frac{P[A|B_i] P[B_i]}{\sum_{j=1}^{N} P[A|B_j] P[B_j]} \tag{D.13}$$

Equation (D.13) is the most common form in which Bayes' Theorem is expressed. Bayes' Theorem provides another way of computing an unknown probability from a series of known conditional probabilities.

### Example D.5

Suppose that you are investigating a site in an area where 10% of the previous borings have indicated the presence of a liquefiable layer. You are using a testing procedure, however, that is 80% accurate in detecting the presence of a liquefiable layer (when a liquefiable layer exists, the test will indicate its presence 80% of the time; however, the test also indicates the presence of a liquefiable layer 20% of the time when it does not actually exist). If the testing procedure indicates the presence of a liquefiable layer, what is the probability that a liquefiable layer actually exists?

**Solution:**

First, the events of interest can be defined:

- Event A: Liquefiable layer is detected by testing procedure
- Event $B_1$: Liquefiable layer actually exists
- Event $B_2$: Liquefiable layer does not exist

Note that events $B_1$ and $B_2$ are mutually exclusive (the liquefiable layer cannot both exist and not exist) and collectively exhaustive (the liquefiable layer either has to exist or not exist). From the problem description, then

$P[A|B_1] = 0.8$ (when liquefiable layer exists, test will indicate it 80% of time)

$P[A|B_2] = 0.2$ (when liquefiable layer absent, test will indicate it exists 20% of time)

$P[B_1] = 0.1$ (10% of previous borings have encountered liquefiable soil)

$P[B_2] = 0.9$ (90% of previous borings have encountered no liquefiable soil)

With this data, the probability that a liquefiable layer actually exists, in light of prior knowledge about subsurface conditions in the area and the observation that a particular testing procedure (of imperfect, but known, accuracy) has indicated its presence, can be computed as

$$P[B_1|A] = \frac{P[A|B_1]P[B_1]}{P[A|B_1]P[B_1] + P[A|B_2]P[B_2]} = \frac{(0.8)(0.1)}{(0.8)(0.1) + (0.2)(0.9)} = 0.308$$

This probability is not intuitively obvious because it depends not only on the successful prediction (true-positive) rate of the testing procedure but also on the unsuccessful (false-positive) rate and the prior information about the existence of liquefiable soils in the region. Note that if the testing procedure gave 95% true-positive and 5% false-positive results, the probability that a liquefiable layer would exist given the test's indication would rise to 67.9%. If the testing procedure's accuracy is very low (say 20% true-positive and 80% false-positive), the probability of a liquefiable layer actually existing given its indication by the test would only be 2.7%.

### D.5 RANDOM VARIABLES

All fields of science and engineering attempt to describe various quantities or phenomena with numerical values. In most cases, the precise numerical value cannot be predicted in advance of some process, or experiment, of interest. In such cases, the quantity or phenomenon can be described by a random variable. The random variable is used to describe an event in a sample space in quantitative terms.

### D.5.1 Discrete Random Variables

A discrete random variable can take on only a finite or countable number of values. Each value has a probability, $p_i$, and the distribution of $p_i$ values constitutes a probability mass function, or PMF, usually written as

$$p_X(x_i) = P[X = x_i] = p_i \tag{D.14}$$

All values of $p_i$ must be non-negative and their collective sum must equal 1.0. Note that an upper-case letter is used to represent the random variable while lower case letters are used to describe specific values that the random variable can take on. The cumulative distribution function, or CDF, of a discrete random variable, is defined as the probability that the discrete random variable is less than or equal to a particular value

$$F_X(x) = P[X \leq x] \tag{D.15}$$

which means that

$$F_X(x_a) = \sum_{x_i \leq x_a} P[X = x_i] \tag{D.16}$$

Examples of probability mass and cumulative distribution functions for a discrete random variable are shown in Figure D.4.

FIGURE D.4 (a) Probability mass function (PMF) and (b) Cumulative distribution function (CDF) for arbitrary discrete random variable.

### D.5.2 Continuous Random Variables

A continuous random variable can take on any value within one or more intervals. Therefore, a continuous random variable can take on any of an infinite number of values and, as a consequence, the probability of it taking on any specific value is $1/\infty = 0$. The probability distribution of a continuous random variable can be described by its probability density function or PDF, $f_X(x)$, which must satisfy the conditions

$$f_X(x) \geq 0 \tag{D.17a}$$

$$\int_{-\infty}^{\infty} f_X(x)\, dx = 1 \tag{D.17b}$$

$$P[a \leq X \leq b] = \int_a^b f_X(x)\, dx \tag{D.17c}$$

According to these conditions, the area under the PDF between two values a and b represents the probability that the random variable will take on a value in the interval bounded by a and b. The probability distribution of a random variable can also be described by its CDF, which is given by

$$F_X(x) = P[X < x] = \int_{-\infty}^x f_X(x)\, dx \tag{D.18}$$

which, of course, means that

$$f_X(x) = \frac{d}{dx} F_X(x) \tag{D.19}$$

Therefore, the probability that a random variable, X, falls between two values, a and b, is

$$P[a \leq X \leq b] = F_X(b) - F_X(a) \tag{D.20}$$
