# Business Validation Report

## Validation Rules

### Fund Master

* AMFI Code must be unique
* Expense Ratio > 0
* Risk Category must belong to:

  * Low
  * Moderate
  * High
  * Very High

### NAV History

* NAV must be greater than 0
* Date must be valid
* Every AMFI code should exist in fund_master

### Transactions

* Transaction Amount > 0
* Transaction Type:

  * SIP
  * Lumpsum
  * Redemption

### KYC Status

Allowed Values:

* Verified
* Pending

### Performance Metrics

* Beta > 0
* Sharpe Ratio should be numeric
* Expense Ratio between 0.1% and 2.5%

---

## Validation Results

All datasets passed structural validation.

No invalid AMFI codes detected.

No invalid transaction amounts detected.

No duplicate records detected.

No missing critical business fields detected.

Overall Status: PASS
