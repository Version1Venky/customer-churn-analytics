
-- Create table
CREATE TABLE telecom_churn (
    customer_id VARCHAR(16) PRIMARY KEY,
    gender VARCHAR(10),
    senior_citizen INT,
    partner VARCHAR(3),
    dependents VARCHAR(3),
    tenure_months INT,
    phone_service VARCHAR(3),
    multiple_lines VARCHAR(32),
    internet_service VARCHAR(32),
    online_security VARCHAR(32),
    online_backup VARCHAR(32),
    device_protection VARCHAR(32),
    tech_support VARCHAR(32),
    streaming_tv VARCHAR(32),
    streaming_movies VARCHAR(32),
    contract_type VARCHAR(32),
    paperless_billing VARCHAR(3),
    payment_method VARCHAR(32),
    monthly_charges DECIMAL(10,2),
    total_charges DECIMAL(10,2),
    churn INT
);
