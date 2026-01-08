#!/usr/bin/env python
# coding: utf-8

# In[19]:

import yfinance as yf
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# ratio dictionary including key, low, high, direction and category for each ratio learned in comm101 (University of Waterloo Course)
 
ratios = {
    # Valuation
    "P/E Ratio": {
        "key": "trailingPE", "low": 15, "high": 25,
        "direction": "lower", "category": "Valuation"
    },
    "Forward P/E": {
        "key": "forwardPE", "low": 15, "high": 25,
        "direction": "lower", "category": "Valuation"
    },
    "P/B Ratio": {
        "key": "priceToBook", "low": 1.5, "high": 3,
        "direction": "lower", "category": "Valuation"
    },
    "EV/EBITDA": {
        "key": "enterpriseToEbitda", "low": 10, "high": 20,
        "direction": "lower", "category": "Valuation"
    },

    # Profitability
    "ROE": {
        "key": "returnOnEquity", "low": 0.10, "high": 0.15,
        "direction": "higher", "category": "Profitability"
    },
    "ROA": {
        "key": "returnOnAssets", "low": 0.05, "high": 0.10,
        "direction": "higher", "category": "Profitability"
    },
    "Net Profit Margin": {
        "key": "profitMargins", "low": 0.05, "high": 0.15,
        "direction": "higher", "category": "Profitability"
    },
    "Operating Margin": {
        "key": "operatingMargins", "low": 0.10, "high": 0.20,
        "direction": "higher", "category": "Profitability"
    },

    # Leverage
    "Debt-to-Equity": {
        "key": "debtToEquity", "low": 0.5, "high": 1.5,
        "direction": "lower", "category": "Leverage"
    },
    "Interest Coverage": {
        "key": "interestCoverage", "low": 2, "high": 5,
        "direction": "higher", "category": "Leverage"
    },

    # Liquidity
    "Current Ratio": {
        "key": "currentRatio", "low": 1.5, "high": 3,
        "direction": "higher", "category": "Liquidity"
    },
    "Quick Ratio": {
        "key": "quickRatio", "low": 1, "high": 2,
        "direction": "higher", "category": "Liquidity"
    }
}


def interpret_ratio(value, low, high, direction):
    if value is None:
        return "Data not available"
    if value < low:
        level = "Low"
    elif value > high:
        level = "High"
    else:
        level = "Medium"
        
    if direction == "lower": #ratios that are the lower the better
        if level == "Low":
            return "Positive"
        elif level == "Medium":
            return "Neutral"
        else:
            return "Negative"
    else: #ratios that are the higher the better
        if level == "High":
            return "Positive"
        elif level == "Medium":
            return "Neutral"
        else:
            return "Negative"

# web title
st.title("Stock Ratio Analyzer")

ticker = st.text_input("Enter stock ticker (e.g. AAPL, MSFT,...):") # users input 

if ticker:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        st.subheader("Company Overview")
        st.write(f"**Sector:** {info.get('sector', 'N/A')}")
        st.write(f"**Industry:** {info.get('industry', 'N/A')}")
        st.write(f"**Market Cap:** {info.get('marketCap', 'N/A')}$")
    
        result = []

        for name, rule in ratios.items():
            value = info.get(rule["key"])
            insight = interpret_ratio(value, rule["low"], rule["high"], rule["direction"])
            result.append({"Ratio":name,
                           "Value": value,
                           "Insight":insight})

        # ratios arranged in a table    
        df = pd.DataFrame(result)
        st.subheader("Fundamental Ratios")
        st.dataframe(df)

        score_map = {"Positive": 1, "Neutral": 0, "Negative": -1} #scoring dictionary
        total_score = sum(score_map[r["Insight"]] for r in result if r["Insight"] in score_map)
        valid_scores = [score_map[r["Insight"]] for r in result if r["Insight"] in score_map]
        average_score = sum(valid_scores) / len(valid_scores)

        if average_score > 0.5:
            overall = "Overall, the stock appears fundamentally strong and potentially attractive."
        elif average_score >= 0:
            overall = "Overall, the stock appears fairly valued with mixed signals."
        else:
            overall = "Overall, the stock shows potential risks based on fundamental metrics."

        # display number of positive, neutral and negative scores in a table (to be added)

        
        # providing insight according to the rating score
        
        st.subheader("Final Verdict")
        st.success(overall)
        
    except Exception as e:
        st.error(f"Error fetching data for {ticker}:{e}")
