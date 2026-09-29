from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "data" / "Uzbekistan_Housing_Banking_Dataset_v5.xlsx"

df = pd.read_excel(FILE, sheet_name="Bank_Panel")
print("Rows:", len(df))
print("Banks:", df["Bank"].nunique())
print("Dates:", df["Date"].nunique())
print("Date range:", df["Date"].min(), "to", df["Date"].max())

assert len(df) == 396, "Expected 396 bank-month observations."
assert df["Bank"].nunique() == 6, "Expected six banks."
assert df["Date"].nunique() == 66, "Expected 66 monthly dates."

for col in ["CAR_pct", "NPL_pct", "Total_Assets_UZS_bn", "ln_assets"]:
    print(f"{col}: {df[col].notna().sum()}/396 populated")

print("\nVerification status:")
print(df["Verification_Status"].value_counts(dropna=False))
print("\nValidation complete.")
