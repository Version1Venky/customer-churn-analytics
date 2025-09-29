
# Customer churn analytics

Predict and reduce customer churn for a telecom style dataset with an end to end analytics pipeline using SQL Python and a BI dashboard.

## Highlights
- End to end pipeline data to decisions
- Reproducible features and models
- Business ready KPIs for a manager dashboard

## Quickstart
Create environment and install
```
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS or Linux
source .venv/bin/activate
pip install -r requirements.txt
```

Train models and generate metrics
```
python -m src.train
```

Evaluate a saved model
```
python -m src.evaluate
```

## Data
Synthetic dataset in data raw telecom_churn.csv with six thousand rows and twenty one columns including the target churn.

## Repo map
- data raw original CSV and processed parquet
- sql DDL cleaning CTEs and feature mart
- src Python code to prepare features train and evaluate
- dashboard screenshots for BI visuals
- reports metrics and business summary

## Results example
After first run check reports metrics.json for AUC accuracy and F1 for baseline and random forest.

## Dashboard
Use Power BI or Tableau to build KPIs churn rate by month retention cohorts CLV and at risk segments. Put screenshots in dashboard screenshots and commit the PBIX or TWBX if you prefer.
