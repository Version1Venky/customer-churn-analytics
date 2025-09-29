
import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from .config import PROCESSED_DIR, MODELS_DIR, REPORTS_DIR
from .prepare_data import load_data, make_features

def train_models(random_state: int = 42):
    # Build features
    df_raw = load_data()
    feats = make_features(df_raw)

    y = feats["churn"].values
    X = feats.drop(columns=["churn"]).values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_state, stratify=y
    )

    # Baseline Logistic Regression
    logreg = LogisticRegression(max_iter=200, n_jobs=None)
    logreg.fit(X_train, y_train)
    proba_lr = logreg.predict_proba(X_test)[:,1]
    pred_lr = (proba_lr >= 0.5).astype(int)

    # Random Forest
    rf = RandomForestClassifier(n_estimators=300, max_depth=None, random_state=random_state, n_jobs=-1)
    rf.fit(X_train, y_train)
    proba_rf = rf.predict_proba(X_test)[:,1]
    pred_rf = (proba_rf >= 0.5).astype(int)

    metrics = {
        "logreg": {
            "auc": float(roc_auc_score(y_test, proba_lr)),
            "accuracy": float(accuracy_score(y_test, pred_lr)),
            "f1": float(f1_score(y_test, pred_lr))
        },
        "random_forest": {
            "auc": float(roc_auc_score(y_test, proba_rf)),
            "accuracy": float(accuracy_score(y_test, pred_rf)),
            "f1": float(f1_score(y_test, pred_rf))
        }
    }

    MODELS_DIR.mkdir(exist_ok=True, parents=True)
    REPORTS_DIR.mkdir(exist_ok=True, parents=True)

    joblib.dump(logreg, MODELS_DIR / "logreg.pkl")
    joblib.dump(rf, MODELS_DIR / "random_forest.pkl")

    Path(REPORTS_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2))
    print("Saved models to", MODELS_DIR, "and metrics to", REPORTS_DIR / "metrics.json")

    # Save feature names for later interpretation
    feature_names = list(pd.read_parquet(PROCESSED_DIR / "features.parquet").drop(columns=["churn"]).columns)
    Path(REPORTS_DIR / "feature_names.json").write_text(json.dumps(feature_names, indent=2))

if __name__ == "__main__":
    train_models()
