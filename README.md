# 📈 EquityLens

**EquityLens** is a stock analysis platform for technical investors. It calculates **12+ financial ratios** across multiple categories — **Valuation, Profitability, Leverage, and Liquidity** — and delivers a **final verdict using a weighted scoring system**, providing actionable insights tailored to different investor profiles.

---

## 🌟 Features

### 👤 Investor Profiles
- **Conservative, Balanced, Risk-Oriented**  
- Tailor insights according to your risk tolerance. Different profiles influence the scoring and recommendations.

### 💹 Stock Tickers
- Supports **any ticker available on [yfinance](https://pypi.org/project/yfinance/)**  
- Fetches real-time data and computes financial ratios automatically.

### 📊 Financial Ratio Analysis

| Category        | Ratio               | Description                               | Preference        |
|-----------------|-------------------|-------------------------------------------|-----------------|
| **Valuation**   | P/E               | Price relative to earnings                | Lower preferred |
|                 | Forward P/E       | Expected price-to-earnings ratio          | Lower preferred |
|                 | P/B               | Price relative to book value              | Lower preferred |
|                 | EV/EBITDA         | Enterprise value to EBITDA ratio          | Lower preferred |
| **Profitability** | ROE              | Return on shareholder equity              | Higher preferred |
|                 | ROA               | Return on total assets                     | Higher preferred |
|                 | Net Profit Margin | Profit as a % of revenue                  | Higher preferred |
|                 | Operating Margin  | Operating income relative to revenue      | Higher preferred |
| **Leverage**    | Debt-to-Equity    | Total debt relative to equity             | Lower preferred |
|                 | Interest Coverage | Ability to cover interest expenses        | Higher preferred |
| **Liquidity**   | Quick Ratio       | Liquid assets relative to current liabilities | Higher preferred |
|                 | Current Ratio     | Current assets relative to current liabilities | Higher preferred |

### 🏆 Weighted Scoring System
- Combines all ratios according to investor profile and category weights  
- Provides a **final verdict** on each stock, helping investors make informed decisions

---

### ‼️ Disclaimer
EquityLens is an independent analysis tool and is not financial advice. It is not affiliated with any financial institution or data provider.
