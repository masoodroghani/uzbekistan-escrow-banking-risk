# Data Notes

## Purpose
The workbook was rebuilt after the original working dataset was lost. The reconstruction combines recoverable official observations with explicitly labelled derived values.

## Provenance categories
- **Verified:** directly recovered from an identified official release.
- **Estimated/Derived:** calculated or imputed from verified observations.
- **Manuscript-consistent reconstructed:** created from coefficients/specifications reported in the manuscript when the original bank-level raw series was unavailable.

## NPL
The current NPL panel is populated for all 396 bank-month rows. A subset is tied directly to official CBU bank-level NPL releases. Other observations are labelled Estimated/Derived and were reconstructed from nearby verified observations. They are not original measurements.

## Total assets
A subset of bank-month asset observations was recovered from official CBU major-indicator releases. Missing values were reconstructed using bank-specific trends fitted to verified observations. `ln_assets` is derived from total assets.

## CAR
The original bank-level CAR series has not been recovered. The workbook's bank-level CAR values are a manuscript-consistent reconstruction using the reported ITSA structure and fixed bank offsets. Official banking-sector CAR values are stored separately as plausibility references and are not substituted for bank-level CAR.

## Market series
Residential transaction volume, monthly CPI/policy-rate controls, and the housing-price series still require further source recovery. The manuscript described monthly housing indicators, while an official HPI source located during reconstruction appeared quarterly. This discrepancy should be resolved before claiming full replication.

## Research-use warning
Do not describe reconstructed values as official observations. Analyses should report sensitivity to using only verified observations where feasible and should clearly disclose the reconstruction process.
