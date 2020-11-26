WITH new_sales AS(
-- #1 CTE to show the price effective date for each sale
SELECT sales.product,
		sales.quantity,
		sales.sales_date, 
		MAX(prices.price_effective_date) price_effective_date
		FROM sales sales
LEFT JOIN prices prices ON sales.product = prices.product 
                    AND sales.sales_date >= prices.price_effective_date
GROUP BY sales.product,
		sales.quantity,
		sales.sales_date),

-- #2 CTE to show join the specific pricing details with the new sales table
revenue_per_sale AS(
SELECT new_sales.*,
		prices.price,
		new_sales.quantity * prices.price AS revenue 
FROM new_sales
LEFT JOIN prices ON prices.product = new_sales.product AND
					prices.price_effective_date = new_sales.price_effective_date)

-- Aggregation to provide total revenue
SELECT sum(revenue) FROM revenue_per_sale  -- Total Revenue is £4,390
