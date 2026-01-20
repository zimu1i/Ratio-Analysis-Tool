# 📊 Stock Ratio Analysis Tool

A stock analysis app that evaluates companies using 12+ financial ratios across valuation, profitability, leverage, and liquidity. It gives you personalized recommendations based on your risk tolerance. 

#### 👩🏻‍💻 Inspired by my coursework COMM101 (University of Waterloo)!

### ℹ️ **What It Does:**
This Streamlit app pulls real-time financial data from Yahoo Finance and calculates key financial ratios. It turns raw numbers into actual investment insights.

**Features:**
- Pulls live data for any publicly traded stock
- Adjusts analysis based on your investor profile (Conservative, Balanced, or Growth)
- Color-codes ratio interpretations so you can see what's good or bad at a glance
- Weights different ratios based on your risk tolerance
- Generates PDF reports you can save or share

## 🛠️ Built With
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
[![yfinance](https://img.shields.io/badge/yfinance-Download-blue?logo=yahoo)](https://pypi.org/project/yfinance/)
[![pandas](https://img.shields.io/badge/pandas-Data%20Analysis-blue?logo=pandas)](https://pypi.org/project/pandas/)
[![numpy](https://img.shields.io/badge/numpy-Array%20Math-blue?logo=numpy)](https://pypi.org/project/numpy/)
[![matplotlib](https://img.shields.io/badge/matplotlib-Plotting-blue?logo=matplotlib)](https://pypi.org/project/matplotlib/)
[![reportlab](https://img.shields.io/badge/reportlab-PDF%20Generation-blue?logo=python)](https://pypi.org/project/reportlab/)

## 📌 Project Details

### 👤 Investor Profiles
Pick Conservative, Balanced, or Growth-Oriented. Your choice changes how ratios are weighted and what recommendations you get.

### 💹 Stock Tickers
Works with any ticker on Yahoo Finance. Just enter the symbol and it fetches everything automatically!

### 📊 Financial Ratio Analysis

| Category        | Ratio               | Description                               | Preference        |
|-----------------|-------------------|-------------------------------------------|-----------------|
| **Valuation**   | P/E               | Price relative to earnings                | Lower is better |
|                 | Forward P/E       | Expected price-to-earnings ratio          | Lower is better |
|                 | P/B               | Price relative to book value              | Lower is better |
|                 | EV/EBITDA         | Enterprise value to EBITDA ratio          | Lower is better |
| **Profitability** | ROE              | Return on shareholder equity              | Higher is better |
|                 | ROA               | Return on total assets                     | Higher is better |
|                 | Net Profit Margin | Profit as a % of revenue                  | Higher is better |
|                 | Operating Margin  | Operating income relative to revenue      | Higher is better |
| **Leverage**    | Debt-to-Equity    | Total debt relative to equity             | Lower is better |
|                 | Interest Coverage | Ability to cover interest expenses        | Higher is better |
| **Liquidity**   | Quick Ratio       | Liquid assets relative to current liabilities | Higher is better |
|                 | Current Ratio     | Current assets relative to current liabilities | Higher is better |

### 🏆 Scoring System
Combines all ratios based on your profile and gives you a final verdict on whether the stock looks good.

### 📄 PDF Reports
Download reports with:
- Company info (sector, industry, market cap)
- All ratios with their values and what they mean
- Category scores showing how each area performed
- Rating breakdown
- Strengths and risks
- Final recommendation

## 📦 Installation & Usage

### What You Need
```bash
pip install streamlit yfinance pandas numpy matplotlib reportlab
```
### Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/zimu1i/Ratio-Analysis-Tool
cd Ratio-Analysis-Tool
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run it

```bash
streamlit run app.py
```
### 👩🏻‍💻 How to use it
1. Enter a stock ticker (like AAPL, MSFT, etc.)
2. Pick your investor profile
3. Review the analysis and ratios
4. Download a PDF if you want to keep it

### ‼️ Disclaimer
This is just an educational tool, not financial advice.

- I built this independently, it's not affiliated with any financial institution
- Past performance doesn't predict future results
- Talk to a real financial advisor before making investment decisions
- I'm not responsible if you lose money using this
- Always do your own research!!!
