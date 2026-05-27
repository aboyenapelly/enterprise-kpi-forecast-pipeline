-- KPI Framework SQL
-- Purpose: Build monthly KPI reporting logic for finance, supply chain, and operations teams.

WITH cleaned_sales AS (
    SELECT
        order_id,
        order_date,
        product_id,
        customer_id,
        quantity,
        unit_price,
        revenue,
        cogs,
        gross_margin,
        discount_rate
    FROM sales_orders
    WHERE customer_id IS NOT NULL
      AND quantity > 0
),

sales_enriched AS (
    SELECT
        s.order_id,
        DATE_TRUNC('month', s.order_date) AS order_month,
        s.product_id,
        p.category,
        p.supplier_id,
        s.customer_id,
        c.segment,
        c.region,
        s.quantity,
        s.revenue,
        s.cogs,
        s.gross_margin,
        s.discount_rate
    FROM cleaned_sales s
    LEFT JOIN product_master p
        ON s.product_id = p.product_id
    LEFT JOIN customer_master c
        ON s.customer_id = c.customer_id
)

SELECT
    order_month,
    category,
    region,
    COUNT(DISTINCT order_id) AS order_count,
    SUM(quantity) AS units_sold,
    SUM(revenue) AS total_revenue,
    SUM(gross_margin) AS total_gross_margin,
    SUM(gross_margin) / NULLIF(SUM(revenue), 0) AS gross_margin_rate,
    AVG(discount_rate) AS avg_discount_rate
FROM sales_enriched
GROUP BY
    order_month,
    category,
    region
ORDER BY
    order_month,
    category,
    region;
