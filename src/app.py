# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import pickle
import os

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="Customer Spend Prediction",
    layout="centered"
)

st.title("🛒 Customer Spend Prediction (Next 30 Days)")
st.write(
    "Predict how much a customer is likely to spend in the next 30 days "
    "based on their past transaction behavior."
)

# -------------------------------------------------
# Load model and scaler
# -------------------------------------------------
@st.cache_resource
def load_artifacts():
    model_path = "D:\Hackathon_project\src\models\spend_model.pkl"
    scaler_path = "D:\Hackathon_project\src\models\scaler.pkl"

    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        st.error("Model files not found. Train the model in notebook first.")
        st.stop()

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    with open(scaler_path, "rb") as f:
        scaler = pickle.load(f)

    return model, scaler


model, scaler = load_artifacts()

# -------------------------------------------------
# User inputs
# -------------------------------------------------
st.subheader("Enter Customer Past Behavior")

recency_days = st.number_input("Recency (days since last purchase)", 0, 365, 5)
frequency = st.number_input("Total past transactions", 1, 500, 20)
monetary = st.number_input("Total past spend", 0.0, 1e7, 30000.0)

avg_order_value = st.number_input("Average order value", 0.0, 1e6, 1500.0)
max_order_value = st.number_input("Maximum order value", 0.0, 1e6, 4000.0)
std_order_value = st.number_input("Std deviation of order value", 0.0, 1e6, 500.0)

total_quantity = st.number_input("Total quantity purchased", 0, 5000, 80)
avg_quantity = st.number_input("Average quantity per order", 0.0, 100.0, 4.0)
avg_products_per_order = st.number_input("Average products per order", 1.0, 20.0, 3.0)

promo_usage_ratio = st.slider("Promotion usage ratio", 0.0, 1.0, 0.3)
customer_lifetime_days = st.number_input("Customer lifetime (days)", 1, 2000, 150)

# -------------------------------------------------
# Prediction
# -------------------------------------------------
if st.button("🔮 Predict Spend"):
    input_df = pd.DataFrame([{
        "recency_days": recency_days,
        "frequency": frequency,
        "monetary": monetary,
        "avg_order_value": avg_order_value,
        "max_order_value": max_order_value,
        "std_order_value": std_order_value,
        "total_quantity": total_quantity,
        "avg_quantity": avg_quantity,
        "avg_products_per_order": avg_products_per_order,
        "promo_usage_ratio": promo_usage_ratio,
        "customer_lifetime_days": customer_lifetime_days
    }])

    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]

    st.success(f"💰 Predicted spend in next 30 days: ₹ {prediction:,.2f}")
