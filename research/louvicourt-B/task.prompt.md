# STRUCTURED PROMPT: LOUVICOURT PSHA REVIEW

## SLOTS

### SLOT 1: Identify point sources for Louvicourt site in CanadaSHM6

Identify the specific point sources in the CanadaSHM6 source model where the Louvicourt site is located. This addresses the question from Chapter 4.0 (Site Specific Seismic Source Model) regarding the seismotectonic context (Stable Crustal) and the source model details (SHM6).

### SLOT 2: Determine maximum magnitude (Mmax) for source zone

Determine the maximum magnitude (Mmax) assigned to the identified source zone in the CanadaSHM6 model. This directly follows from identifying the source zone in SLOT 1.

### SLOT 3: Determine PGA range for 1/10,000 year return period

Determine the range of Peak Ground Acceleration (PGA) values obtained for rare events with a 1/10,000 year return period. This addresses the PSHA results presented in Chapter 5 for different site conditions and return periods.

### SLOT 4: Compare PGA values with NBCC Canada

Compare the PGA values obtained in the PSHA with those reported by the National Building Code of Canada (NBCC). This comparison addresses how site-specific hazard results relate to national code provisions.

### SLOT 5: Summarize spectral matching methodologies

Provide a brief summary of state-of-practice methodologies for performing spectral matching in ground motion selection. This covers the general background on spectral matching approaches, including methods that apply scalar amplification factors versus methods that modify frequency content across different periods.

### SLOT 6: Investigate PEER NGA spectral matching methodology

Investigate the specific spectral matching methodology employed by the PEER online application for the NGA East and West databases. Confirm whether this application alters the frequency content of original ground motion records or applies only scalar scaling factors.

### SLOT 7: Verify magnitude ranges for rare event selection

Verify whether ground motions with magnitude ranges other than those from the 10,000-year deaggregation were selected for rare events. The task context indicates concern that only deaggregation-based magnitude and distance ranges were used, without considering site conditions (Vs30).

### SLOT 8: Explain spectral matching drift at short periods

Explain the reason for poor spectral matching at short periods (PGA and nearby periods) despite good matching at medium and long periods. Confirm or refute the hypothesis that this drift occurred because hard soil site conditions (Vs30) were not properly constrained in the selection, and that imposing specific magnitude and distance constraints limited the availability of suitable records even in active shallow crustal zones.

### SLOT 9: Validate recommendation to relax magnitude constraints

Validate whether the proposed recommendation to relax magnitude constraints (from deaggregation) while focusing on distance ranges and harder site Vs30 values is technically sound. Assess whether this approach would yield records with better spectral matching at short periods, and identify any potential errors or limitations in this recommendation.

## CONSTRAINTS

- All responses, analyses, and outputs derived from this structured prompt must be written in English.
- The final structured prompt document and all downstream research outputs must be in English only.
- Apply professional document formatting standards per FORMAT_RULES (LaTeX math notation where applicable, ASCII characters for English text, academic voice, no instructional language).
- Include audit-style footnotes per AUDIT_RULES using `^[Confidence: HIGH|MEDIUM|LOW, Rationale: ...]` format at the end of each paragraph in downstream outputs.
