# 5-10 Minute Video Demo Script

## 0:00-0:45 | Introduction
Hi, my name is Abhishruth. This project is called Enterprise KPI Pipeline and Forecast Accuracy Analytics. I built it as a solo project to demonstrate how I collect, clean, validate, transform, and report operational data for business decision-making.

The project focuses on sales, inventory, product, procurement, and customer data. The final outputs include KPI reports, data quality checks, and a forecast-ready feature dataset.

## 0:45-1:45 | Business Problem
The business problem is that teams often use data from different systems, and those datasets can contain missing values, negative quantities, inconsistent mappings, or incomplete product information.

If those issues are not caught early, they can affect finance reporting, supply chain planning, inventory decisions, and forecasting accuracy.

The goal of this project is to create a reliable analytics workflow that turns raw data into clean reporting outputs and model-ready datasets.

## 1:45-3:15 | Project Structure
The repository is organized into raw data, processed data, source code, SQL, reports, assets, and documentation.

The raw data folder includes product master, customer master, sales orders, inventory snapshots, and procurement orders.

The source folder contains three main scripts:
- pipeline.py for the core ETL workflow
- data_quality_checks.py for validation checks
- feature_builder.py for preparing forecast-ready features

The reports folder contains the final business outputs.

## 3:15-5:15 | Code Walkthrough
In pipeline.py, I start by loading the raw files, cleaning invalid sales records, joining product and customer reference data, and creating an enriched sales dataset.

Then I aggregate monthly KPIs by product category. These KPIs include revenue, gross margin, orders, units, average discount, and gross margin rate.

In the data quality script, I check for missing customer IDs, negative quantities, and missing product categories. These checks are summarized in the data quality report so business teams can quickly understand what needs correction.

In the feature builder, I prepare product-month level features such as monthly units, monthly revenue, average unit price, average discount, lagged demand, and rolling three-month demand. This structure can support forecasting and future machine learning workflows.

## 5:15-7:00 | Output and Dashboard Explanation
The monthly KPI summary helps business users monitor revenue, margin, and product performance.

The data quality report shows where reporting issues exist before the data is used for decision-making.

The forecast feature dataset creates a clean structure for planning and demand analysis.

I also included visual assets showing monthly revenue trends, gross margin by category, and data quality issue counts.

## 7:00-8:30 | Business Impact
The value of this project is that it connects technical data preparation with business decision-making.

For finance teams, it supports revenue and margin review.
For supply chain teams, it supports inventory and demand analysis.
For operations teams, it highlights reporting exceptions and data quality issues.
For data science teams, it creates structured features that can be used for forecasting models.

## 8:30-9:30 | Future Improvements
If I were productionizing this workflow, I would schedule it using Airflow, scale transformations with PySpark, add automated alerts for data quality failures, and publish the dashboards to Power BI Service.

I would also create a more formal feature store so forecasting models can reuse consistent, validated features.

## 9:30-10:00 | Closing
This project reflects the type of analytics work I enjoy most: building reliable data workflows, improving reporting accuracy, preparing datasets for advanced analysis, and translating data into practical business insights.
