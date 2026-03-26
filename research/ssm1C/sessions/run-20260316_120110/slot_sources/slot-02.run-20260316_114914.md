## SLOT 2: Source-Model Logic Tree Structure

The source-model logic tree encodes epistemic uncertainty by defining alternative realisations of the SSM. Each branch set addresses a specific source of uncertainty, and branches within each set carry weights reflecting the relative credibility of each alternative. The primary logic tree (`ssmLT_IND.xml`) contains three branch sets that together produce 27 end-branches; the two additional files (`ssmLT_IND_collapsed.xml` and `ssmLT_IND_garage_v1.xml`) are variant representations of the same structure. [KB:source_model.md]^[Confidence: HIGH, Rationale: All logic-tree details are directly stated in source_model.md. Weights within each branch set sum to 1.00, confirming internal consistency.]

Branch set 1 addresses source-model selection (uncertainty type: `sourceModel`, applies to all sources). Three alternative source-model realisations are offered: the 108-zone areal model and two smoothed-seismicity grids differing in their minimum magnitude threshold. [KB:source_model.md]^[Confidence: HIGH, Rationale: Branch set 1 composition is explicitly described in source_model.md with branch IDs, file names, and weights. Weights sum to 0.40 + 0.27 + 0.33 = 1.00.]

| Branch | Source-model file | Weight |
|---|---|---:|
| `b1m1` | `nt2012_areal_source_model_v1.xml` | 0.40 |
| `b1m2` | `nt2012_smoothed_source_model_v1_mmin4.5.xml` | 0.27 |
| `b1m3` | `nt2012_smoothed_source_model_v1_mmin5.5.xml` | 0.33 |

Branch set 2 addresses maximum-magnitude perturbation (uncertainty type: `maxMagGRRelative`, applies to all sources). A relative adjustment is applied to the base $M_{\max}$ of every source simultaneously, spanning a symmetric range of $\pm 0.3$ magnitude units. [KB:source_model.md]^[Confidence: HIGH, Rationale: Branch set 2 parameters are explicitly stated in source_model.md. Weights sum to 0.32 + 0.36 + 0.32 = 1.00, internally consistent.]

| Branch | Perturbation ($\Delta M_{\max}$) | Weight |
|---|---:|---:|
| `b2m1` | $-0.3$ | 0.32 |
| `b2m2` | $0.0$ | 0.36 |
| `b2m3` | $+0.3$ | 0.32 |

Branch set 3 addresses $b$-value perturbation (uncertainty type: `bGRRelative`, applies to all sources). A relative adjustment is applied to the base $b$-value of every source simultaneously, spanning a symmetric range of $\pm 0.1$. [KB:source_model.md]^[Confidence: HIGH, Rationale: Branch set 3 parameters are explicitly stated in source_model.md. Weights sum to 0.32 + 0.36 + 0.32 = 1.00, internally consistent.]

| Branch | Perturbation ($\Delta b$) | Weight |
|---|---:|---:|
| `b3m1` | $-0.1$ | 0.32 |
| `b3m2` | $0.0$ | 0.36 |
| `b3m3` | $+0.1$ | 0.32 |

