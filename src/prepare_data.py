
import pandas as pd
from pathlib import Path
from .config import DATA_RAW, PROCESSED_DIR

CATEGORICAL = [
    "gender","partner","dependents","phone_service","multiple_lines",
    "internet_service","online_security","online_backup","device_protection",
    "tech_support","streaming_tv","streaming_movies","contract_type",
    "paperless_billing","payment_method"
]

NUMERIC = ["senior_citizen","tenure_months","monthly_charges","total_charges"]

def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_RAW)
    return df

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Replace spaces with underscores in category values for safe dummies
    for col in CATEGORICAL:
        df[col] = df[col].astype(str).str.lower().str.replace(" ", "_")
    # Basic cleaning
    df["avg_charge_per_month"] = df.apply(
        lambda r: r["total_charges"]/r["tenure_months"] if r["tenure_months"] else 0, axis=1
    )
    return df

def make_features(df: pd.DataFrame) -> pd.DataFrame:
    df = preprocess(df)
    X = pd.get_dummies(df[CATEGORICAL + NUMERIC + ["avg_charge_per_month"]], drop_first=True)
    y = df["churn"].astype(int)
    features = X.join(y)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    features.to_parquet(PROCESSED_DIR / "features.parquet", index=False)
    return features

if __name__ == "__main__":
    df = load_data()
    feats = make_features(df)
    print("Saved features to", PROCESSED_DIR / "features.parquet")
