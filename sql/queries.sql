-- ==========================================
-- QUERY 1
-- Total Funds
-- ==========================================

SELECT COUNT(*) AS total_funds
FROM dim_fund;


-- ==========================================
-- QUERY 2
-- Fund Count By Category
-- ==========================================

SELECT
    category,
    COUNT(*) AS fund_count
FROM dim_fund
GROUP BY category;


-- ==========================================
-- QUERY 3
-- Top 10 NAV Values
-- ==========================================

SELECT *
FROM fact_nav
ORDER BY nav DESC
LIMIT 10;


-- ==========================================
-- QUERY 4
-- Average 3 Year Return
-- ==========================================

SELECT
AVG(return_3yr_pct)
AS avg_return_3yr
FROM fact_performance;


-- ==========================================
-- QUERY 5
-- Highest Sharpe Ratio
-- ==========================================

SELECT
amfi_code,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;


-- ==========================================
-- QUERY 6
-- Total Transaction Amount
-- ==========================================

SELECT
SUM(amount_inr)
AS total_transaction_amount
FROM fact_transactions;


-- ==========================================
-- QUERY 7
-- Top States By Transactions
-- ==========================================

SELECT
state,
COUNT(*) AS txn_count
FROM fact_transactions
GROUP BY state
ORDER BY txn_count DESC
LIMIT 10;