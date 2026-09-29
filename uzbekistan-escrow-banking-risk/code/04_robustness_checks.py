from pathlib import Path
import pandas as pd
import statsmodels.formula.api as smf

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "data" / "Uzbekistan_Housing_Banking_Dataset_v5.xlsx"

df = pd.read_excel(FILE, sheet_name="Bank_Panel")
df["Date"] = pd.to_datetime(df["Date"])

def placebo_break(date_string):
    d = pd.Timestamp(date_string)
    x = df.copy()
    x["placebo"] = (x["Date"] >= d).astype(int)
    m = smf.ols("CAR_pct ~ time + placebo + ln_assets + C(Bank)", data=x).fit(cov_type="HC1")
    return m.params.get("placebo"), m.bse.get("placebo")

for d in ["2024-04-01", "2025-04-01"]:
    coef, se = placebo_break(d)
    print(d, "placebo CAR break:", coef, "SE:", se)

print("\nCAUTION: bank-level CAR is reconstructed from manuscript parameters; placebo results are therefore descriptive reconstruction checks.")
