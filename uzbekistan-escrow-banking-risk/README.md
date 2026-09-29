# Uzbekistan Escrow Reform and Banking Risk — Package

This repository supports the study **“Assessing Short-Run Banking Risk and Housing-Market Adjustment Following Mandatory Escrow Reform: Evidence from Uzbekistan.”**



This repository contains a **dataset**. 

Observations are classified as:

1. **Verified** — recovered from an identified official source, principally Central Bank of Uzbekistan releases.
2. **Estimated/Derived** — reconstructed from verified observations using documented procedures.
3. **Manuscript-consistent reconstructed** — values created from parameters reported in the manuscript where the original bank-level series was not recovered.


## Study design

- Period: January 2021–June 2026
- Frequency: monthly
- Banks: NBU, SQB/Uzpromstroybank, Asakabank, Ipoteka-Bank, Agrobank, Microcreditbank
- Bank panel target: 6 banks × 66 months = 396 observations
- Intervention: 1 April 2026
- Main variables: CAR, NPL, total assets / log assets, refinancing or policy rate, CPI inflation, residential transaction volume, and housing price index
- Design variables: time, post-policy indicator, post-policy trend, and March 2026 anticipation pulse

## Repository structure

- `data/` — reconstructed dataset and data documentation
- `code/` — Python scripts for validation and replication
- `docs/` — source and methodology notes
- `results/tables/` — generated regression tables
- `results/figures/` — generated figures

## Current reconstruction status

The current workbook has a complete 396-row bank-panel structure. NPL, assets and CAR have populated values, but their provenance differs. Consult `data/DATA_NOTES.md` and the workbook's `Verification_Status`, `Notes`, `Recovery_Log`, `Completeness`, and `Imputation_Method` sheets before analysis.

The market-level monthly series is not yet fully reconstructed. Scripts should not silently manufacture missing official data.

## Reproducibility

Create a Python environment and install:

```bash
pip install pandas numpy statsmodels openpyxl
```

Then run:

```bash
python code/01_validate_dataset.py
python code/02_bank_panel_itsa.py
python code/03_transaction_itsa.py
python code/04_robustness_checks.py
```

The transaction script stops with an explanatory message if the market series is incomplete.

## Citation

See `CITATION.cff`. Update author identifiers and publication metadata when the article receives its final bibliographic details.

## License

Code is released under the MIT License.
