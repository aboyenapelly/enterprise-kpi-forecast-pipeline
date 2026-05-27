"""
Data quality checks for operational reporting datasets.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
REPORTS_DIR = BASE_DIR / "reports"

def run_quality_checks():
    sales_orders = pd.read_csv(RAW_DIR / "sales_orders.csv")
    product_master = pd.read_csv(RAW_DIR / "product_master.csv")

    checks = [
        {
            "table": "sales_orders",
            "check": "missing_customer_id",
            "issue_count": int(sales_orders["customer_id"].isna().sum()),
            "business_risk": "Orders cannot be tied to customer-level reporting."
        },
        {
            "table": "sales_orders",
            "check": "negative_quantity",
            "issue_count": int((sales_orders["quantity"] < 0).sum()),
            "business_risk": "Negative quantities can distort demand and revenue reporting."
        },
        {
            "table": "product_master",
            "check": "missing_category",
            "issue_count": int(product_master["category"].isna().sum()),
            "business_risk": "Missing categories can affect product performance dashboards."
        }
    ]

    quality_report = pd.DataFrame(checks)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    quality_report.to_csv(REPORTS_DIR / "data_quality_report.csv", index=False)
    return quality_report

if __name__ == "__main__":
    report = run_quality_checks()
    print(report)
