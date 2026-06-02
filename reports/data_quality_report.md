# Data Quality Report

## Project

Bluestock Mutual Fund Analytics Platform

## Date

02 June 2026

## Objective

To profile and validate all provided datasets before data cleaning and database design.

---

# Dataset Summary

| Dataset                  | Rows  | Columns | Missing Values | Duplicates | Status |
| ------------------------ | ----- | ------- | -------------- | ---------- | ------ |
| 01_fund_master           | 40    | 15      | 0              | 0          | PASS   |
| 02_nav_history           | 46000 | 3       | 0              | 0          | PASS   |
| 03_aum_by_fund_house     | 90    | 5       | 0              | 0          | PASS   |
| 04_monthly_sip_inflows   | 48    | 6       | 12             | 0          | REVIEW |
| 05_category_inflows      | 144   | 3       | 0              | 0          | PASS   |
| 06_industry_folio_count  | 21    | 6       | 0              | 0          | PASS   |
| 07_scheme_performance    | 40    | 19      | 0              | 0          | PASS   |
| 08_investor_transactions | 32778 | 13      | 0              | 0          | PASS   |
| 09_portfolio_holdings    | 322   | 8       | 0              | 0          | PASS   |
| 10_benchmark_indices     | 8050  | 3       | 0              | 0          | PASS   |

---

# Key Findings

1. All 10 datasets were successfully loaded using Pandas.

2. No duplicate records were identified across any dataset.

3. No missing values were found except in the `yoy_growth_pct` column of `04_monthly_sip_inflows.csv`.

4. Dataset sizes match the project specification.

5. Data structure appears consistent and suitable for ETL processing.

6. All primary datasets contain expected columns and data types.

---

# Identified Data Quality Issues

## 04_monthly_sip_inflows.csv

Issue:

* 12 missing values in `yoy_growth_pct`

Proposed Action:

* Recalculate YoY growth using SIP inflow history
  OR
* Keep as NULL if historical comparison is unavailable

Impact:

* Low

---

# Overall Assessment

Data Quality Score: 99%

The provided datasets are highly structured and require minimal cleaning. The primary focus of Day 2 will be data standardisation, validation, type conversion, and database schema implementation rather than extensive error correction.
