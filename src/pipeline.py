import pandas as pd
import pickle
import os

# ----------------------------
# Load model and scaler
# ----------------------------
def load_artifacts():
    if not os.path.exists("models/spend_model.pkl"):
        raise FileNotFoundError("spend_model.pkl not found")

    if not os.path.exists("models/scaler.pkl"):
        raise FileNotFoundError("scaler.pkl not found")

    model = pickle.load(open("models/spend_model.pkl", "rb"))
    scaler = pickle.load(open("models/scaler.pkl", "rb"))
    return model, scaler


# ----------------------------
# Prediction pipeline
# ----------------------------
def predict_next_30_days_spend(
    recency_days,
    frequency,
    monetary,
    avg_order_value,
    max_order_value,
    std_order_value,
    total_quantity,
    avg_quantity,
    avg_products_per_order,
    promo_usage_ratio,
    customer_lifetime_days,
):
    model, scaler = load_artifacts()

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

    return prediction
