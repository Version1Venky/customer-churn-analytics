Customer Churn Analytics

End-to-end data analytics and machine learning project that demonstrates skills in SQL, Python, and Power BI. The goal is to predict customer churn, analyze drivers, and present actionable insights through an interactive dashboard.

📌 Project Highlights

Built a complete data pipeline from raw CSV to feature-ready tables using SQL.

Performed exploratory data analysis (EDA) to identify churn trends and risk segments.

Developed and evaluated machine learning models (Logistic Regression and Random Forest).

Achieved 93% accuracy and 0.93 F1 score with the Random Forest classifier.

Designed a Power BI dashboard to present KPIs and churn insights for business decision-making.

📊 Results Summary

Best Model: Random Forest Classifier

Accuracy: 93%

F1 Score: 0.93

Precision (Churn=1): 0.96

Recall (Churn=1): 0.85

AUC: ~0.93

Confusion Matrix (Random Forest):

	Predicted Not Churn	Predicted Churn
Actual Not Churn	741	15
Actual Churn	67	377
📈 Dashboard Overview

Power BI dashboard designed for executives and business analysts to monitor churn KPIs and explore customer segments.




KPIs:

Total Customers

Churn Rate (%)

Retention Rate (%)

Visuals:

Churn by Contract Type

Churn by Tenure Bucket

Churn by Payment Method

📥 Download: customer_churn.pbix

🔑 Key Insights & Recommendations

High churn among month-to-month contracts → incentivize long-term contracts with discounts.

Early tenure customers (<6 months) are more likely to churn → strengthen onboarding and support.

Electronic check users churn more → promote auto-pay methods (bank transfer, credit card).

Lack of online security/tech support increases churn → bundle support and security add-ons.

⚙️ Tech Stack

SQL: Data cleaning, transformations, feature mart creation

Python (pandas, scikit-learn, matplotlib, shap): Data preparation, modeling, evaluation

Power BI: Dashboard development and KPI reporting

Git + GitHub: Version control, CI/CD

📂 Repository Structure
customer_churn_analytics/
├── data/             # Raw and processed data
├── sql/              # SQL scripts for cleaning and feature mart
├── src/              # Python code for data prep, training, evaluation
├── dashboard/        # Power BI file (.pbix) and screenshots
├── reports/          # Model metrics and business summary
└── README.md         # Documentation

▶️ How to Run
Setup
git clone https://github.com/Version1Venky/customer-churn-analytics.git
cd customer-churn-analytics
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt

Train Models
python -m src.train

Evaluate Model
python -m src.evaluate


Outputs are saved in the reports/ folder.

👤 Author

Venkatesh Kardile

LinkedIn

GitHub
