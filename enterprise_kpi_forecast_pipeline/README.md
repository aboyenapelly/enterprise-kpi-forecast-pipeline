# Enterprise KPI Pipeline & Forecast Accuracy Analytics

## Project Overview
This solo project demonstrates an end-to-end analytics workflow for operational, inventory, finance, and supply chain data. The goal is to clean and validate raw business data, build KPI-ready reporting tables, prepare forecast-ready features, and communicate insights through dashboards and business summaries.

The project is designed around a realistic business scenario where leadership needs reliable reporting across sales, margin, inventory movement, supplier activity, and product-level demand trends.

## Business Problem
Business teams often rely on data from multiple systems, including sales, inventory, procurement, and product master data. When these sources contain missing values, duplicate records, inconsistent mappings, or negative quantities, reporting accuracy and planning decisions can be affected.

This project answers four key questions:

1. Which products and categories are driving revenue and margin?
2. Where are inventory or demand patterns creating planning risk?
3. What data quality issues need to be resolved before reporting?
4. How can clean historical data be structured for forecasting and modeling workflows?

## Tools Used
- SQL for KPI logic, joins, aggregation, and validation checks
- Python for data cleaning, transformation, and feature preparation
- Pandas and NumPy for analytical workflows
- PySpark-style DataFrame logic documented for scalable processing
- Power BI / Tableau-ready output files
- Excel-ready reports for business review
- Matplotlib for simple visual summaries

## Project Structure
```text
enterprise_kpi_forecast_pipeline/
├── data/
│   ├── raw/
│   │   ├── product_master.csv
│   │   ├── customer_master.csv
│   │   ├── sales_orders.csv
│   │   ├── inventory_snapshots.csv
│   │   └── procurement_orders.csv
│   └── processed/
│       └── sales_enriched.csv
├── reports/
│   ├── monthly_kpi_summary.csv
│   ├── data_quality_report.csv
│   └── forecast_feature_dataset.csv
├── src/
│   ├── pipeline.py
│   ├── data_quality_checks.py
│   └── feature_builder.py
├── sql/
│   └── kpi_framework.sql
├── assets/
│   ├── monthly_revenue_trend.png
│   ├── gross_margin_by_category.png
│   └── data_quality_issues.png
└── docs/
    ├── video_demo_script.md
    └── dashboard_walkthrough.md
```

## Workflow
### 1. Data Acquisition
The workflow starts with five raw datasets:
- Product master
- Customer master
- Sales orders
- Inventory snapshots
- Procurement orders

### 2. Data Cleaning and Validation
The pipeline checks for:
- Missing customer IDs
- Negative order quantities
- Missing product categories
- Inconsistent product mappings
- Reporting-ready completeness

### 3. KPI Development
The project builds KPI tables for:
- Revenue
- Gross margin
- Gross margin rate
- Units sold
- Average discount
- Product category performance
- Inventory and demand trends

### 4. Forecast-Ready Feature Dataset
The workflow prepares product-month level features such as:
- Monthly units
- Monthly revenue
- Average unit price
- Average discount
- Lagged demand
- Rolling three-month demand
- Forecast readiness flag

### 5. Reporting and Business Insights
Outputs are designed to support:
- Finance reviews
- Supply chain planning
- Product performance discussions
- Data governance reviews
- Forecasting and ML dataset preparation

## Key Outputs
- `monthly_kpi_summary.csv`: monthly category-level KPI table
- `data_quality_report.csv`: summary of data quality issues
- `forecast_feature_dataset.csv`: structured dataset for forecasting and modeling
- Dashboard screenshots in the `assets/` folder

## Business Impact
This project shows how raw operational data can be converted into reliable business reporting and model-ready datasets. It demonstrates practical data cleaning, validation, KPI design, reporting automation, and analytical storytelling for business stakeholders.

## What I Would Improve Next
If deployed in a production environment, I would extend this project by:
- Scheduling the pipeline using Airflow
- Scaling transformations with PySpark on EMR or Databricks
- Adding automated data quality alerts
- Publishing dashboards to Power BI Service
- Creating a formal feature store for downstream forecasting and ML workflows
