# 📊 Stock Ratio Analysis Tool

An interactive stock analysis platform that evaluates companies using **12+ fundamental financial ratios** across four key categories: Valuation, Profitability, Leverage, and Liquidity. The tool delivers personalized investment **insights** through a weighted scoring system tailored to **different investor risk profiles**.

## 🌟 Project Overview
This Streamlit-based application automates fundamental analysis by fetching real-time financial data via the ***yfinance API*** and applying ratio-based scoring frameworks taught in financial analysis coursework ***(COMM 101, University of Waterloo)***. It transforms complex financial metrics into ***actionable*** investment recommendations.

**📚 Key Capabilities:**

- Real-time data retrieval from Yahoo Finance for any publicly traded stock
- Profile-based analysis adapting recommendations to Conservative, Balanced, or Growth-Oriented strategies
- Automated ratio interpretation with color-coded insights (Positive, Neutral, Negative)
- Weighted scoring model that prioritizes different ratio categories based on investor risk tolerance
- PDF report generation for comprehensive investment documentation

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
[![yfinance](https://img.shields.io/badge/yfinance-Download-blue?logo=yahoo)](https://pypi.org/project/yfinance/)
[![pandas](https://img.shields.io/badge/pandas-Data%20Analysis-blue?logo=pandas)](https://pypi.org/project/pandas/)
[![numpy](https://img.shields.io/badge/numpy-Array%20Math-blue?logo=numpy)](https://pypi.org/project/numpy/)
[![matplotlib](https://img.shields.io/badge/matplotlib-Plotting-blue?logo=matplotlib)](https://pypi.org/project/matplotlib/)
[![reportlab](https://img.shields.io/badge/reportlab-PDF%20Generation-blue?logo=python)](https://pypi.org/project/reportlab/)

## 📌 Features

### 👤 Investor Profiles
- **Conservative, Balanced or  Growth-Oriented**  
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

### 📄  Professional PDF Reports
Generate downloadable reports containing:

- Company overview (sector, industry, market cap)
- Complete ratio breakdown with values and interpretations
- Category-level scoring with weighted contributions
- Rating distribution summary
- Profile-adjusted explanations for each category
- Strengths and risk analysis
- Final investment verdict

## 📦 Installation & Usage

### Prerequisites
```bash
pip install streamlit yfinance pandas numpy matplotlib reportlab
```
### Running the tool

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/zimu1i/Ratio-Analysis-Tool
cd Ratio-Analysis-Tool
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app

```bash
streamlit run app.py
```
### 👩🏻‍💻 How to use
1. Enter Stock Ticker - Input any valid ticker symbol (e.g. AAPL, MSFT,...).
2. Select investor profile - Choose conservative, balanced or growth-oriented.
3. Review Analysis - Check the automated ratio calculation and insights.
4. Download Report - Generate a PDF for documentation or further use.

### ‼️ Disclaimer
This tool is for educational and informational purposes only and does not constitute financial advice.

- The analyzer is an independent analysis tool and is not affiliated with any financial institution or data provider
- Past performance and ratio analysis do not guarantee future results
- Investment decisions should be made in consultation with qualified financial professionals
- The author assumes no responsibility for investment losses resulting from use of this tool
- Always conduct thorough due diligence before making investment decisions
