# Data Cleaning Report

## Summary

| dataset                      |   rows |   duplicates_removed |   missing_before |   missing_after |
|:-----------------------------|-------:|---------------------:|-----------------:|----------------:|
| 01_fund_master.csv           |     40 |                    0 |                0 |               0 |
| 02_nav_history.csv           |  46000 |                    0 |                0 |               0 |
| 03_aum_by_fund_house.csv     |     90 |                    0 |                0 |               0 |
| 04_monthly_sip_inflows.csv   |     48 |                    0 |               12 |               0 |
| 05_category_inflows.csv      |    144 |                    0 |                0 |               0 |
| 06_industry_folio_count.csv  |     21 |                    0 |                0 |               0 |
| 07_scheme_performance.csv    |     40 |                    0 |                0 |               0 |
| 08_investor_transactions.csv |  32778 |                    0 |                0 |               0 |
| 09_portfolio_holdings.csv    |    322 |                    0 |                0 |               0 |
| 10_benchmark_indices.csv     |   8050 |                    0 |                0 |               0 |
| 125497_live_nav.csv          |      1 |                    0 |                0 |               0 |
| combined_live_nav.csv        |      5 |                    0 |                0 |               0 |

## Cleaning Steps Applied

1. Duplicate removal

2. Missing value treatment
   - Numeric columns → Median
   - Text columns → 'Unknown'

3. Date conversion

4. Text standardization

5. Weekend/Holiday NAV handling
   - Reindexed to full date range
   - Forward-filled NAV values

6. Exported cleaned datasets
