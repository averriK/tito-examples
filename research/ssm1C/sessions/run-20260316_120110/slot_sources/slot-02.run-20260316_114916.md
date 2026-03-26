## SLOT 2: Source-Model Logic Tree Structure

The source-model logic tree (`ssmLT_IND.xml`) encodes epistemic uncertainty through three branch sets, collectively producing $3 \times 3 \times 3 = 27$ end-branches. Each branch set addresses a distinct type of epistemic uncertainty; branches within each set carry weights reflecting the relative credibility of each alternative [KB:source_model.md].^[Confidence: HIGH, Rationale: Logic tree structure and end-branch count are stated explicitly in KB:source_model.md; $3^3 = 27$ is arithmetically correct and confirmed by KB:site_sources_data.md.]

Branch set 1 (uncertainty type `sourceModel`) contains three branches selecting alternative source-model representations of the seismicity. Branch set 2 (uncertainty type `maxMagGRRelative`) applies simultaneous relative perturbations to the maximum magnitude of all sources. Branch set 3 (uncertainty type `bGRRelative`) applies simultaneous relative perturbations to the Gutenberg-Richter $b$-value of all sources. The tables below list the branch IDs, perturbation values or model file identities, and assigned weights for each branch set [KB:source_model.md].^[Confidence: HIGH, Rationale: Uncertainty types for all three branch sets and the branch-level details are explicitly tabulated in KB:source_model.md with no ambiguity.]

#### Branch Set 1: Source Model Selection (`sourceModel`)

| Branch | Model file | Weight |
|---|---|---|
| `b1m1` | `nt2012_areal_source_model_v1.xml` | 0.40 |
| `b1m2` | `nt2012_smoothed_source_model_v1_mmin4.5.xml` | 0.27 |
| `b1m3` | `nt2012_smoothed_source_model_v1_mmin5.5.xml` | 0.33 |

#### Branch Set 2: Maximum Magnitude Perturbation (`maxMagGRRelative`)

| Branch | Perturbation (Mw) | Weight |
|---|---|---|
| `b2m1` | -0.3 | 0.32 |
| `b2m2` | 0.0 | 0.36 |
| `b2m3` | +0.3 | 0.32 |

#### Branch Set 3: b-Value Perturbation (`bGRRelative`)

| Branch | Perturbation | Weight |
|---|---|---|
| `b3m1` | -0.1 | 0.32 |
| `b3m2` | 0.0 | 0.36 |
| `b3m3` | +0.1 | 0.32 |

The combined weights for each branch set sum to unity: the three source-model branches sum to 0.40 + 0.27 + 0.33 = 1.00, and both perturbation branch sets sum to 0.32 + 0.36 + 0.32 = 1.00. The higher weight of 0.36 assigned to the central (unperturbed) branch in sets 2 and 3 reflects the greater credibility attributed to the nominal parameter estimates relative to either perturbed extreme [KB:source_model.md][KB:site_sources_data.md].^[Confidence: HIGH, Rationale: Weight values are listed in KB:source_model.md and confirmed in KB:site_sources_data.md. All three arithmetic checks pass. The interpretation of the central weight as reflecting credibility of unperturbed estimates is consistent with standard epistemic logic-tree practice as described in the KB context.]

