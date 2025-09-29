
from src.prepare_data import load_data, make_features

def test_make_features_smoke():
    df = load_data()
    feats = make_features(df)
    assert "churn" in feats.columns
    assert len(feats) == len(df)
