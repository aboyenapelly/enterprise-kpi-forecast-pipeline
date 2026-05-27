"""
Enterprise KPI Pipeline & Forecast Accuracy Analytics
Main pipeline script.

This script reads raw operational datasets, cleans core records,
creates enriched reporting data, and exports KPI-ready outputs.
"""

from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
REPORTS_DIR = BASE_DIR / "reports"

def load_data():
    product_master = pd.read_csv(RAW_DIR / "product_master.csv")
    customer_master = pd.read_csv(RAW_DIR / "customer_master.csv")
    sales_orders = pd.read_csv(RAW_DIR / "sales_orders.csv")
    inventory = pd.read_csv(RAW_DIR / "inventory_snapshots.csv")
    procurement = pd.read_csv(RAW_DIR / "procurement_orders.csv")
    return product_master, customer_master, sales_orders, inventory, procurement

def clean_sales_orders(sales_orders):
    cleaned = sales_orders.copy()
    cleaned = cleaned.dropna(subset=["customer_id"])
    cleaned = cleaned[cleaned["quantity"] > 0]
    return cleaned

def build_sales_enriched(sales_orders, product_master, customer_master):
    enriched = sales_orders.merge(
        product_master[["product_id", "category", "supplier_id", "standard_cost", "list_price"]],
        on="product_id",
        how="left"
    )
    enriched = enriched.merge(customer_master, on="customer_id", how="left")
    enriched["order_month"] = pd.to_datetime(enriched["order_date"]).dt.to_period("M").astype(str)
    return enriched

def build_monthly_kpis(sales_enriched):
    kpis = sales_enriched.groupby(["order_month", "category"], dropna=False).agg(
        revenue=("revenue", "sum"),
        gross_margin=("gross_margin", "sum"),
        orders=("order_id", "nunique"),
        units=("quantity", "sum"),
        avg_discount=("discount_rate", "mean")
    ).reset_index()
    kpis["gross_margin_rate"] = np.round(kpis["gross_margin"] / kpis["revenue"], 4)
    return kpis

def main():
    product_master, customer_master, sales_orders, inventory, procurement = load_data()
    clean_orders = clean_sales_orders(sales_orders)
    sales_enriched = build_sales_enriched(clean_orders, product_master, customer_master)
    monthly_kpis = build_monthly_kpis(sales_enriched)

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    sales_enriched.to_csv(PROCESSED_DIR / "sales_enriched.csv", index=False)
    monthly_kpis.to_csv(REPORTS_DIR / "monthly_kpi_summary.csv", index=False)

    print("Pipeline completed successfully.")
    print(f"Sales enriched rows: {len(sales_enriched):,}")
    print(f"KPI rows: {len(monthly_kpis):,}")

if __name__ == "__main__":
    main()
