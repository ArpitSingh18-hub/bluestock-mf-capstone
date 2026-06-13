-- =====================================================
-- DROP EXISTING TABLES
-- =====================================================

DROP TABLE IF EXISTS dim_date;
DROP TABLE IF EXISTS dim_fund;
DROP TABLE IF EXISTS fact_nav;
DROP TABLE IF EXISTS fact_performance;
DROP TABLE IF EXISTS fact_transactions;

-- =====================================================
-- DIMENSION TABLES
-- =====================================================

CREATE TABLE dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    fund_house TEXT,
    scheme_name TEXT,

    category TEXT,
    sub_category TEXT,

    plan TEXT,
    risk_category TEXT,

    expense_ratio_pct REAL
);

CREATE TABLE dim_date (

    date_id INTEGER PRIMARY KEY,

    full_date DATE UNIQUE,

    year INTEGER,
    quarter INTEGER,
    month INTEGER,

    month_name TEXT
);

-- =====================================================
-- FACT TABLES
-- =====================================================

CREATE TABLE fact_nav (

    amfi_code INTEGER,

    nav_date DATE,

    nav REAL,

    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (

    amfi_code INTEGER,

    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,

    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,

    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (

    investor_id INTEGER,

    transaction_date DATE,

    amfi_code INTEGER,

    amount_inr REAL,

    state TEXT,
    city TEXT,

    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);