
-- Cleaning CTEs
WITH base AS (
  SELECT
    customer_id,
    LOWER(gender) AS gender,
    senior_citizen,
    CASE WHEN partner='Yes' THEN 1 ELSE 0 END AS partner,
    CASE WHEN dependents='Yes' THEN 1 ELSE 0 END AS dependents,
    tenure_months,
    CASE WHEN phone_service='Yes' THEN 1 ELSE 0 END AS phone_service,
    CASE WHEN multiple_lines LIKE 'Yes%%' THEN 1 ELSE 0 END AS multiple_lines,
    internet_service,
    CASE WHEN online_security='Yes' THEN 1 ELSE 0 END AS online_security,
    CASE WHEN online_backup='Yes' THEN 1 ELSE 0 END AS online_backup,
    CASE WHEN device_protection='Yes' THEN 1 ELSE 0 END AS device_protection,
    CASE WHEN tech_support='Yes' THEN 1 ELSE 0 END AS tech_support,
    CASE WHEN streaming_tv='Yes' THEN 1 ELSE 0 END AS streaming_tv,
    CASE WHEN streaming_movies='Yes' THEN 1 ELSE 0 END AS streaming_movies,
    contract_type,
    CASE WHEN paperless_billing='Yes' THEN 1 ELSE 0 END AS paperless_billing,
    payment_method,
    monthly_charges,
    total_charges,
    churn
  FROM telecom_churn
),
enriched AS (
  SELECT
    *,
    CASE WHEN tenure_months = 0 THEN NULL ELSE total_charges / NULLIF(tenure_months,0) END AS avg_charge_per_month,
    CASE WHEN contract_type='Two year' THEN 24
         WHEN contract_type='One year' THEN 12
         ELSE 1 END AS contract_length_months
  FROM base
)
SELECT * FROM enriched;
