🛒 Customer Spend Prediction – Next 30 Days
📌 Project Overview

This project aims to predict how much a customer is likely to spend in the next 30 days based on their past transaction behavior.
The problem is framed as a supervised regression task and the solution is deployed using a Streamlit web application.

Since real production data was not available, we generated realistic synthetic transaction data and built a complete ML pipeline, from data generation to deployment.

🎯 Problem Statement

Given a customer’s historical transaction behavior:

How frequently they purchase

How recently they purchased

How much they spend

Their purchasing patterns

👉 Predict the total amount they will spend in the next 30 days

🧠 Machine Learning Framing

Type: Supervised Learning

Task: Regression

Input (X): Customer historical behavioral features

Output (y): Future 30-day spend

📁 Project Structure
Hackathon_project/
│
├── data/
│   └── transactions.csv        # Synthetic transaction data
│
├── models/
│   ├── spend_model.pkl         # Trained regression model
│   └── scaler.pkl              # Feature scaler
│
├── src/
│   └── (optional modular scripts)
│
├── app.py                      # Streamlit web app
├── README.md                   # Project documentation
└── *.ipynb                     # Notebooks (data, training, experiments)

🧪 Step 1: Synthetic Data Generation

Generated ~5000 customers

Each customer has multiple transactions

Simulated realistic:

Transaction dates

Purchase amounts

Quantities

Product counts

Promotion usage

Key columns:

transaction_id

customer_id

transaction_date

total_amount

quantity

num_products

promotion_used

This ensures privacy and allows full control over data quality.

🧹 Step 2: Data Preprocessing

Converted date columns to proper datetime format

Removed invalid transactions (negative or zero values)

Sorted data by customer and time

Ensured clean, model-ready data

✂️ Step 3: Cutoff Strategy (No Data Leakage)

To avoid data leakage:

Used a time-based cutoff

Transactions before cutoff → features

Transactions after cutoff (30 days) → target

This simulates a real-world prediction scenario.

🧩 Step 4: Feature Engineering

Created customer-level behavioral features:

RFM Features

recency_days

frequency

monetary

Behavioral Features

avg_order_value

max_order_value

std_order_value

total_quantity

avg_quantity

Diversity & Promotion

avg_products_per_order

promo_usage_ratio

Temporal

customer_lifetime_days

Each row in the final dataset represents one customer.

🎯 Step 5: Target Variable

Target:

future_spend_30d = total spend in the next 30 days


Customers with no purchases in the next 30 days were assigned a target value of 0.

⚖️ Step 6: Model Training & Comparison

We experimented with multiple regression models:

Linear Regression

Ridge Regression

Random Forest Regressor

Gradient Boosting Regressor

Final Model Selected

✅ Random Forest Regressor

Reasons:

Handles non-linear customer behavior

Robust to noise and outliers

Strong performance on tabular data

📊 Evaluation Metrics

Models were evaluated using:

MAE (Mean Absolute Error) – business friendly

RMSE (Root Mean Squared Error) – penalizes large errors

R² Score – explained variance

📦 Step 7: Model Serialization

For deployment:

Trained model saved as spend_model.pkl

Feature scaler saved as scaler.pkl

These artifacts are loaded directly by the Streamlit app.

🚀 Step 8: Deployment (Streamlit App)

A Streamlit web application was built where:

Users input customer behavior features

The app applies the same preprocessing & scaling

The trained model predicts next 30-day spend in real time

How to Run the App
streamlit run .\app.py

🖥️ Streamlit App Features

Interactive numeric inputs

Promotion usage slider

One-click prediction

Clear display of predicted spend

🧠 Key Learnings

Importance of time-based data splitting

Feature engineering drives model performance

Proper serialization enables smooth deployment

Separation of training and inference is critical

🎤 One-Line Project Explanation (For Hackathon / Interview)

“We built an end-to-end machine learning pipeline to predict customer spend in the next 30 days using historical behavior, trained a regression model, and deployed it as an interactive Streamlit application.”

✅ Future Improvements

Add customer segmentation

Use real production data

Experiment with XGBoost / LightGBM

Add API deployment (FastAPI)

🏁 Conclusion

This project demonstrates a complete real-world ML workflow:
from data generation → modeling → evaluation → deployment,
making it suitable for hackathons, interviews, and portfolio projects.
