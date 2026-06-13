# Performance Metrics Explained for Viva

## Introduction

In mutual fund and investment analysis, it is not sufficient to look only at returns. An investor must evaluate both the returns generated and the risks taken to achieve those returns.

To provide a complete evaluation of a mutual fund, the following performance metrics are commonly used:

1. CAGR (Compound Annual Growth Rate)
2. Volatility
3. Sharpe Ratio
4. Beta
5. Alpha
6. Value at Risk (VaR)

Together, these metrics help investors understand growth, risk, manager skill, and potential losses.

---

# 1. CAGR (Compound Annual Growth Rate)

## Definition

CAGR represents the annualized growth rate of an investment over a period of time, assuming that the investment grows at a constant rate every year.

Although investments do not grow uniformly in reality, CAGR provides a standardized way to compare investment performance.

## Formula

CAGR = (Ending Value / Beginning Value)^(1/n) - 1

Where:

* Beginning Value = Initial investment value
* Ending Value = Final investment value
* n = Number of years

## Example

Suppose an investment grows from ₹100,000 to ₹200,000 in 5 years.

CAGR = (200000 / 100000)^(1/5) - 1

CAGR = 14.87%

This means the investment effectively grew at an average annual rate of 14.87%.

## Interpretation

* Higher CAGR indicates stronger long-term growth.
* Lower CAGR indicates weaker growth.
* CAGR is useful when comparing multiple funds over the same time horizon.

## Viva Answer

"CAGR measures the annualized growth rate of an investment and helps compare long-term performance across different mutual funds."

---

# 2. Volatility

## Definition

Volatility measures how much returns fluctuate around their average value.

It is a measure of investment risk.

In finance, volatility is usually calculated using the standard deviation of returns.

## Why It Matters

Two funds may produce the same average return, but one may be much riskier.

Investors generally prefer stable returns over highly fluctuating returns.

## Example

Fund A Returns:

10%, 11%, 9%, 10%, 10%

Fund B Returns:

40%, -20%, 35%, -10%, 15%

Both may have similar average returns, but Fund B is significantly more volatile.

## Interpretation

* Low Volatility = Stable Investment
* High Volatility = Risky Investment

## Viva Answer

"Volatility measures the variability of returns and is commonly used as a measure of investment risk."

---

# 3. Sharpe Ratio

## Definition

The Sharpe Ratio measures how much excess return an investor receives for each unit of risk taken.

It is one of the most widely used performance metrics in finance.

## Formula

Sharpe Ratio = (Portfolio Return - Risk-Free Rate) / Portfolio Volatility

Where:

* Portfolio Return = Expected return of the fund
* Risk-Free Rate = Return from a risk-free asset such as government securities
* Volatility = Standard deviation of returns

## Example

Fund A:

Return = 15%

Volatility = 10%

Sharpe Ratio = 1.5

Fund B:

Return = 15%

Volatility = 30%

Sharpe Ratio = 0.5

Fund A is superior because it achieves the same return with much lower risk.

## Interpretation

* Sharpe > 1 = Good
* Sharpe > 2 = Very Good
* Sharpe > 3 = Excellent

## Why It Matters

Investors are interested not only in returns but also in how much risk was taken to achieve those returns.

## Viva Answer

"The Sharpe Ratio measures risk-adjusted return and indicates how efficiently a fund converts risk into returns."

---

# 4. Beta

## Definition

Beta measures a fund's sensitivity to overall market movements.

It indicates how aggressively or defensively a fund behaves relative to the market.

## Formula

Beta = Covariance(Fund Returns, Market Returns) / Variance(Market Returns)

## Interpretation

### Beta = 1

Fund moves in line with the market.

If market rises 10%, fund is expected to rise approximately 10%.

### Beta > 1

Aggressive Fund

If Beta = 1.5:

Market +10%

Fund +15%

### Beta < 1

Defensive Fund

If Beta = 0.5:

Market +10%

Fund +5%

## Why It Matters

Beta helps investors understand market-related risk.

Aggressive investors may prefer higher Beta funds, while conservative investors may prefer lower Beta funds.

## Viva Answer

"Beta measures market sensitivity and indicates whether a fund is more aggressive or more defensive than the market."

---

# 5. Alpha

## Definition

Alpha measures a fund manager's ability to generate returns beyond what is expected based on market risk.

It represents excess performance.

## Formula

Alpha = Actual Return - Expected Return

Expected Return is usually estimated using CAPM.

## Example

Expected Return = 12%

Actual Return = 16%

Alpha = +4%

The fund manager generated 4% additional return beyond market expectations.

## Interpretation

### Positive Alpha

Manager Outperformed

### Zero Alpha

Manager Performed As Expected

### Negative Alpha

Manager Underperformed

## Why It Matters

Alpha is often considered a measure of fund manager skill.

## Viva Answer

"Alpha measures excess return generated beyond market expectations and is used to evaluate fund manager performance."

---

# 6. Value at Risk (VaR)

## Definition

Value at Risk estimates the maximum expected loss over a specified period at a given confidence level.

It is one of the most important downside risk measures.

## Example

Suppose:

1-Day VaR = ₹10,000

Confidence Level = 95%

Interpretation:

There is a 95% probability that losses will not exceed ₹10,000 in a single day.

## Why It Matters

Investors want to know the worst expected loss under normal market conditions.

VaR provides a quantitative estimate of downside risk.

## Interpretation

Higher VaR:

* Greater potential losses
* Higher risk

Lower VaR:

* Smaller potential losses
* Lower risk

## Viva Answer

"Value at Risk estimates the maximum expected loss at a specified confidence level and is used to quantify downside risk."

---

# Relationship Between All Metrics

| Metric       | Measures             | Purpose                          |
| ------------ | -------------------- | -------------------------------- |
| CAGR         | Growth               | Long-term return measurement     |
| Volatility   | Risk                 | Return variability               |
| Sharpe Ratio | Risk-adjusted Return | Return earned per unit of risk   |
| Beta         | Market Sensitivity   | Aggressive vs defensive behavior |
| Alpha        | Manager Skill        | Excess return generation         |
| VaR          | Downside Risk        | Potential future loss            |

---

# Why Use All Metrics Together?

No single metric can fully evaluate a mutual fund.

A complete evaluation requires:

* CAGR to measure growth
* Volatility to measure risk
* Sharpe Ratio to evaluate efficiency
* Beta to understand market sensitivity
* Alpha to assess manager skill
* VaR to estimate potential losses

Together, these metrics provide a comprehensive view of investment performance and risk.

---

# Final Viva Answer

"In my project, I used CAGR, Volatility, Sharpe Ratio, Beta, Alpha, and VaR to evaluate mutual funds from multiple dimensions. CAGR measures growth, Volatility measures risk, Sharpe Ratio evaluates risk-adjusted performance, Beta measures market sensitivity, Alpha indicates manager skill, and VaR estimates potential losses. Using all six metrics together provides a comprehensive assessment of both return and risk."
