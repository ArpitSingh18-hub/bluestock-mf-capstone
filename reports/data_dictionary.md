# Data Dictionary

## Project: Bluestock Mutual Fund Analytics Platform

### Purpose

This document describes the structure, business meaning, and data types of datasets used in the project.

---

# 1. FUND MASTER DATASET

Source File:
01_fund_master.csv

Description:
Contains master information for all mutual fund schemes.

| Column             | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier |
| fund_house         | Text      | Mutual fund company           |
| scheme_name        | Text      | Scheme name                   |
| category           | Text      | Fund category                 |
| sub_category       | Text      | Detailed fund category        |
| plan               | Text      | Direct or Regular plan        |
| launch_date        | Date      | Fund launch date              |
| benchmark          | Text      | Benchmark index               |
| expense_ratio_pct  | Float     | Expense ratio percentage      |
| exit_load_pct      | Float     | Exit load percentage          |
| min_sip_amount     | Integer   | Minimum SIP amount            |
| min_lumpsum_amount | Integer   | Minimum lump sum amount       |
| fund_manager       | Text      | Fund manager name             |
| risk_category      | Text      | Risk classification           |
| sebi_category_code | Text      | SEBI category identifier      |

---

# 2. NAV HISTORY DATASET

Source File:
02_nav_history.csv

Description:
Historical Net Asset Value records.

| Column    | Data Type | Description       |
| --------- | --------- | ----------------- |
| amfi_code | Integer   | Scheme identifier |
| date      | Date      | NAV date          |
| nav       | Float     | Net Asset Value   |

---

# 3. AUM BY FUND HOUSE

Source File:
03_aum_by_fund_house.csv

Description:
Assets Under Management information.

| Column         | Data Type | Description       |
| -------------- | --------- | ----------------- |
| date           | Date      | Reporting date    |
| fund_house     | Text      | Fund house name   |
| aum_lakh_crore | Float     | AUM in lakh crore |
| aum_crore      | Float     | AUM in crore      |
| num_schemes    | Integer   | Number of schemes |

---

# 4. MONTHLY SIP INFLOWS

Source File:
04_monthly_sip_inflows.csv

Description:
Monthly SIP investment trends.

| Column                    | Data Type | Description           |
| ------------------------- | --------- | --------------------- |
| month                     | Date      | Reporting month       |
| sip_inflow_crore          | Float     | SIP inflow amount     |
| active_sip_accounts_crore | Float     | Active SIP accounts   |
| new_sip_accounts_lakh     | Float     | New SIP accounts      |
| sip_aum_lakh_crore        | Float     | SIP AUM               |
| yoy_growth_pct            | Float     | Year-over-year growth |

---

# 5. CATEGORY INFLOWS

Source File:
05_category_inflows.csv

Description:
Fund category level inflows.

| Column           | Data Type | Description       |
| ---------------- | --------- | ----------------- |
| month            | Date      | Reporting month   |
| category         | Text      | Fund category     |
| net_inflow_crore | Float     | Net inflow amount |

---

# 6. INDUSTRY FOLIO COUNT

Source File:
06_industry_folio_count.csv

Description:
Industry-wide folio statistics.

| Column              | Data Type | Description     |
| ------------------- | --------- | --------------- |
| month               | Date      | Reporting month |
| total_folios_crore  | Float     | Total folios    |
| equity_folios_crore | Float     | Equity folios   |
| debt_folios_crore   | Float     | Debt folios     |
| hybrid_folios_crore | Float     | Hybrid folios   |
| others_folios_crore | Float     | Other folios    |

---

# 7. SCHEME PERFORMANCE

Source File:
07_scheme_performance.csv

Description:
Fund return and risk metrics.

| Column             | Data Type | Description             |
| ------------------ | --------- | ----------------------- |
| amfi_code          | Integer   | Scheme identifier       |
| return_1yr_pct     | Float     | One-year return         |
| return_3yr_pct     | Float     | Three-year return       |
| return_5yr_pct     | Float     | Five-year return        |
| alpha              | Float     | Alpha metric            |
| beta               | Float     | Beta metric             |
| sharpe_ratio       | Float     | Sharpe ratio            |
| sortino_ratio      | Float     | Sortino ratio           |
| std_dev_ann_pct    | Float     | Annualized volatility   |
| max_drawdown_pct   | Float     | Maximum drawdown        |
| aum_crore          | Float     | Assets under management |
| expense_ratio_pct  | Float     | Expense ratio           |
| morningstar_rating | Integer   | Morningstar rating      |
| risk_grade         | Text      | Risk classification     |

---

# 8. INVESTOR TRANSACTIONS

Source File:
08_investor_transactions.csv

Description:
Investor purchase and redemption records.

| Column             | Data Type | Description             |
| ------------------ | --------- | ----------------------- |
| investor_id        | Integer   | Investor identifier     |
| transaction_date   | Date      | Transaction date        |
| amfi_code          | Integer   | Scheme identifier       |
| transaction_type   | Text      | SIP/Lumpsum/Redemption  |
| amount_inr         | Float     | Transaction amount      |
| state              | Text      | Investor state          |
| city               | Text      | Investor city           |
| city_tier          | Text      | Tier classification     |
| age_group          | Text      | Investor age segment    |
| gender             | Text      | Investor gender         |
| annual_income_lakh | Float     | Annual income           |
| payment_mode       | Text      | Payment channel         |
| kyc_status         | Text      | KYC verification status |

---

# 9. PORTFOLIO HOLDINGS

Source File:
09_portfolio_holdings.csv

Description:
Underlying securities held by funds.

| Column            | Data Type | Description               |
| ----------------- | --------- | ------------------------- |
| amfi_code         | Integer   | Scheme identifier         |
| stock_symbol      | Text      | Stock ticker              |
| stock_name        | Text      | Company name              |
| sector            | Text      | Industry sector           |
| weight_pct        | Float     | Portfolio weight          |
| market_value_cr   | Float     | Market value              |
| current_price_inr | Float     | Current stock price       |
| portfolio_date    | Date      | Portfolio disclosure date |

---

# 10. BENCHMARK INDICES

Source File:
10_benchmark_indices.csv

Description:
Benchmark index history.

| Column      | Data Type | Description    |
| ----------- | --------- | -------------- |
| date        | Date      | Trading date   |
| index_name  | Text      | Benchmark name |
| close_value | Float     | Closing value  |

---

# SQLite Warehouse Tables

## dim_fund

Stores master scheme information used by analytical fact tables.

Primary Key:
amfi_code

---

## fact_nav

Stores historical NAV records for all schemes.

Foreign Key:
amfi_code

---

## fact_performance

Stores return and risk metrics.

Foreign Key:
amfi_code

---

## fact_transactions

Stores investor transaction records.

Foreign Key:
amfi_code

---

## Data Governance Notes

* All AMFI codes validated against NAV history.
* Duplicate records removed during cleaning.
* Missing values handled through median and business-rule imputation.
* Date fields standardized to datetime format.
* Processed datasets stored separately from raw source data.
