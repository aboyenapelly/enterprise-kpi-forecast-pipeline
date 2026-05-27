"""
Feature builder for forecasting and model-ready datasets.
"""

from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
REPORTS_DIR = BASE_DIR / "reports"

def build_features():
    sales_orders = pd.read_csv(RAW_DIR / "sales_orders.csv")
    product_master = pd.read_csv(RAW_DIR / "product_master.csv")

    sales_orders = sales_orders.dropna(subset=["customer_id"])
    sales_orders = sales_orders[sales_orders["quantity"] > 0]
    sales_orders["order_month"] = pd.to_datetime(sales_orders["order_date"]).dt.to_period("M").astype(str)

    features = sales_orders.groupby(["product_id", "order_month"]).agg(
        monthly_units=("quantity", "sum"),
        monthly_revenue=("revenue", "sum"),
        avg_unit_price=("unit_price", "mean"),
        avg_discount=("discount_rate", "mean"),
        gross_margin=("gross_margin", "sum")
    ).reset_index()

    features = features.merge(
        product_master[["product_id", "category", "supplier_id", "margin_rate"]],
        on="product_id",
        how="left"
    )

    features["lag_1_units"] = features.groupby("product_id")["monthly_units"].shift(1)
    features["rolling_3mo_units"] = features.groupby("product_id")["monthly_units"].transform(
        lambda x: x.rolling(3, min_periods=1).mean()
    )
    features["forecast_ready_flag"] = np.where(features["lag_1_units"].notna(), 1, 0)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    features.to_csv(REPORTS_DIR / "forecast_feature_dataset.csv", index=False)
    return features

if __name__ == "__main__":
    feature_data = build_features()
    print(feature_data.head())
