from pathlib import Path
import pandas as pd
import statsmodels.formula.api as smf

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "data" / "Uzbekistan_Housing_Banking_Dataset_v5.xlsx"
OUT = ROOT / "results" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_excel(FILE, sheet_name="Bank_Panel")
df["Bank"] = df["Bank"].astype("category")

# IMPORTANT: CAR contains manuscript-consistent reconstructed values.
# Results using it are reconstruction checks, not independent validation of original raw data.
car = smf.ols(
    "CAR_pct ~ time + post + post_trend + ln_assets + Refinancing_Rate_pct + C(Bank)",
    data=df
).fit(cov_type="HC1")

npl = smf.ols(
    "NPL_pct ~ time + post + post_trend + ln_assets + Refinancing_Rate_pct + C(Bank)",
    data=df
).fit(cov_type="HC1")

print("\nCAR model\n", car.summary())
print("\nNPL model\n", npl.summary())

pd.DataFrame({
    "CAR_coef": car.params,
    "CAR_se": car.bse,
    "NPL_coef": npl.params.reindex(car.params.index),
    "NPL_se": npl.bse.reindex(car.params.index),
}).to_csv(OUT / "bank_panel_itsa.csv")
