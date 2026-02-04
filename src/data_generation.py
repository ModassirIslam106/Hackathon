import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import uuid

# -----------------------------
# Helper Functions
# -----------------------------

def random_date(start, end):
    """Generate random datetime between `start` and `end`."""
    return start + (end - start) * random.random()

# constants
NUM_CUSTOMERS = 5000
NUM_TRANSACTIONS = 20000
NUM_PRODUCTS = 500
NUM_STORES = 50

product_categories = ["Electronics", "Apparel", "Grocery", "Home Decor", "Sports", "Beauty"]
regions = ["North", "South", "East", "West", "Central"]
cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Pune", "Kolkata"]
loyalty_status_list = ["Bronze", "Silver", "Gold", "Platinum"]
channels = ["Online", "In-Store", "Mobile App"]
countries = ["India", "USA", "UK", "UAE"]

# -----------------------------
# 1. stores Table
# -----------------------------
stores = pd.DataFrame({
    "store_id": range(1, NUM_STORES + 1),
    "store_name": [f"Store_{i}" for i in range(1, NUM_STORES + 1)],
    "store_city": np.random.choice(cities, NUM_STORES),
    "store_region": np.random.choice(regions, NUM_STORES),
    "opening_date": [random_date(datetime(2010,1,1), datetime(2023,1,1)).date() for _ in range(NUM_STORES)]
})

# -----------------------------
# 2. products Table
# -----------------------------
products = pd.DataFrame({
    "product_id": range(1, NUM_PRODUCTS + 1),
    "product_name": [f"Product_{i}" for i in range(1, NUM_PRODUCTS + 1)],
    "product_category": np.random.choice(product_categories, NUM_PRODUCTS),
    "unit_price": np.round(np.random.uniform(5, 5000, NUM_PRODUCTS), 2),
    "current_stock_level": np.random.randint(10, 500, NUM_PRODUCTS)
})

# -----------------------------
# 3. customer_details Table
# -----------------------------
customers = pd.DataFrame({
    "customer_id": range(1, NUM_CUSTOMERS + 1),
    "first_name": [f"Cust_{i}" for i in range(1, NUM_CUSTOMERS + 1)],
    "Email": [f"customer{i}@email.com" for i in range(1, NUM_CUSTOMERS + 1)],
    "loyalty_status": np.random.choice(loyalty_status_list, NUM_CUSTOMERS),
    "total_loyalty_points": np.random.randint(0, 5000, NUM_CUSTOMERS),
    "last_purchase_date": [random_date(datetime(2023,1,1), datetime(2024,1,1)).date() for _ in range(NUM_CUSTOMERS)],
    "country": np.random.choice(countries, NUM_CUSTOMERS),
    "channel_preference": np.random.choice(channels, NUM_CUSTOMERS)
})

# -----------------------------
# 4. promotion_details Table
# -----------------------------
promotions = pd.DataFrame({
    "promotion_id": range(1, 51),
    "promotion_name": [f"Promo_{i}" for i in range(1, 51)],
    "start_date": [random_date(datetime(2023,1,1), datetime(2023,6,1)).date() for _ in range(50)],
    "end_date": [random_date(datetime(2023,6,2), datetime(2023,12,31)).date() for _ in range(50)],
    "discount_percentage": np.round(np.random.uniform(5, 40, 50), 2),
    "applicable_category": np.random.choice(product_categories + ["ALL"], 50)
})

# -----------------------------
# 5. loyalty_rules Table
# -----------------------------
loyalty_rules = pd.DataFrame({
    "rule_id": range(1, 11),
    "rule_name": [f"Rule_{i}" for i in range(1, 11)],
    "points_per_unit_spent": np.round(np.random.uniform(0.5, 5.0, 10), 2),
    "min_spend_threshold": np.round(np.random.uniform(50, 500, 10), 2),
    "bonus_points": np.random.randint(10, 200, 10)
})

# -----------------------------
# 6. store_sales_header (20,000 transactions)
# -----------------------------
transactions = pd.DataFrame({
    "transaction_id": [str(uuid.uuid4()) for _ in range(NUM_TRANSACTIONS)],
    "customer_id": np.random.choice(customers["customer_id"], NUM_TRANSACTIONS),
    "store_id": np.random.choice(stores["store_id"], NUM_TRANSACTIONS),
    "transaction_date": [random_date(datetime(2023,1,1), datetime(2024,1,1)) for _ in range(NUM_TRANSACTIONS)],
    "total_amount": np.round(np.random.uniform(50, 10000, NUM_TRANSACTIONS), 2),
    "channel": np.random.choice(channels, NUM_TRANSACTIONS),
})

# -----------------------------
# 7. store_sales_line_items (Transaction Details)
# -----------------------------
line_items_list = []
line_item_id = 1

for t_id in transactions["transaction_id"]:
    num_items = np.random.randint(1, 5)   # each transaction has 1–4 items

    for _ in range(num_items):
        prod = products.sample(1).iloc[0]

        promo_choice = promotions.sample(1).iloc[0] if random.random() < 0.3 else None

        line_items_list.append({
            "line_item_id": line_item_id,
            "transaction_id": t_id,
            "product_id": prod["product_id"],
            "promotion_id": promo_choice["promotion_id"] if promo_choice is not None else None,
            "quantity": np.random.randint(1, 5),
            "line_item_amount": round(prod["unit_price"] * random.randint(1, 5), 2)
        })
        line_item_id += 1

store_sales_line_items = pd.DataFrame(line_items_list)

# -----------------------------
# SHOW OUTPUT SHAPES
# -----------------------------
print("Stores:", stores.shape)
print("Products:", products.shape)
print("Customers:", customers.shape)
print("Promotions:", promotions.shape)
print("Loyalty Rules:", loyalty_rules.shape)
print("Transactions:", transactions.shape)
print("Line Items:", store_sales_line_items.shape)