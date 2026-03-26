## SLOT 2: Source-Model Logic Tree Structure

The source-model logic tree (`ssmLT_IND.xml`) encodes epistemic uncertainty through three branch sets, collectively producing $3 \times 3 \times 3 = 27$ end-branches. Each branch set addresses a distinct type of epistemic uncertainty; branches within each set carry weights reflecting the relative credibility of each alternative [@GemInd2012].

#### Branch Set 1: Source Model Selection (`sourceModel`)

Branch set 1 addresses source-model selection, offering three alternative source-model representations of the regional seismicity. Branch `b1m1` selects the 108-zone areal source model; branches `b1m2` and `b1m3` select spatially smoothed point-source grids with $M_{\min}$ thresholds of 4.5 Mw and 5.5 Mw respectively.

| Branch | Model file | Weight |
|---|---|---:|
| `b1m1` | `nt2012_areal_source_model_v1.xml` | 0.40 |
| `b1m2` | `nt2012_smoothed_source_model_v1_mmin4.5.xml` | 0.27 |
| `b1m3` | `nt2012_smoothed_source_model_v1_mmin5.5.xml` | 0.33 |

#### Branch Set 2: Maximum Magnitude Perturbation (`maxMagGRRelative`)

Branch set 2 applies simultaneous relative perturbations to the base $M_{\max}$ of all sources. The symmetric flanking branches ($\pm 0.3$ Mw) each carry weight 0.32; the unperturbed central branch carries the higher weight of 0.36, reflecting greater credibility attributed to the nominal parameter estimate.

| Branch | Perturbation ($\Delta M_{\max}$, Mw) | Weight |
|---|---:|---:|
| `b2m1` | $-0.3$ | 0.32 |
| `b2m2` | $0.0$ | 0.36 |
| `b2m3` | $+0.3$ | 0.32 |

#### Branch Set 3: $b$-Value Perturbation (`bGRRelative`)

Branch set 3 applies simultaneous relative perturbations to the Gutenberg-Richter $b$-value of all sources, with the same symmetric weight structure as branch set 2.

| Branch | Perturbation ($\Delta b$) | Weight |
|---|---:|---:|
| `b3m1` | $-0.1$ | 0.32 |
| `b3m2` | $0.0$ | 0.36 |
| `b3m3` | $+0.1$ | 0.32 |

The combined weights within each branch set sum to unity: source-model branches sum to $0.40 + 0.27 + 0.33 = 1.00$; both perturbation branch sets sum to $0.32 + 0.36 + 0.32 = 1.00$.
