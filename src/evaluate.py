
import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from .config import PROCESSED_DIR, MODELS_DIR, REPORTS_DIR

def evaluate(model_name: str = "random_forest"):
    feats = pd.read_parquet(PROCESSED_DIR / "features.parquet")
    y = feats["churn"].values
    X = feats.drop(columns=["churn"]).values

    # Simple holdout split same as train default
    n = len(y)
    idx = np.arange(n)
    test_mask = (idx % 5 == 0)
    X_test = X[test_mask]
    y_test = y[test_mask]

    model_path = MODELS_DIR / (model_name + ".pkl")
    model = joblib.load(model_path)

    preds = model.predict(X_test)
    report = classification_report(y_test, preds, output_dict=True)
    cm = confusion_matrix(y_test, preds).tolist()

    out = {"model": model_name, "report": report, "confusion_matrix": cm}
    Path(REPORTS_DIR / f"evaluation_{model_name}.json").write_text(json.dumps(out, indent=2))
    print(f"Saved evaluation for {model_name} to", REPORTS_DIR / f"evaluation_{model_name}.json")

if __name__ == "__main__":
    evaluate("random_forest")
