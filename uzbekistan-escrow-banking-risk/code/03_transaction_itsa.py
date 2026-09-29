from pathlib import Path
import pandas as pd
import statsmodels.formula.api as smf

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "data" / "Uzbekistan_Housing_Banking_Dataset_v5.xlsx"

df = pd.read_excel(FILE, sheet_name="Market_Monthly")
needed = ["ln_Transaction_Volume", "Refinancing_Rate_pct", "CPI_Inflation_pct"]
missing = {c: int(df[c].isna().sum()) for c in needed}

if any(missing.values()):
    raise SystemExit(
        "Market-level replication is not ready. Missing values: " + str(missing) +
        ". Recover/document the official market series before estimating the model."
    )

model = smf.ols(
    "ln_Transaction_Volume ~ time + March_2026_Pulse + Refinancing_Rate_pct + CPI_Inflation_pct + C(Month)",
    data=df
).fit(cov_type="HC1")
print(model.summary())
