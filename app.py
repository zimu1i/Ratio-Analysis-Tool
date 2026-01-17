#!/usr/bin/env python
# coding: utf-8

# In[19]:

import yfinance as yf
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# ratio dictionary including key, low, high, direction and category for each ratio learned in comm101 (University of Waterloo Course)
 
# ratio dictionary

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


# investor profiles (conservative, neutral, risky)

investor_profiles = {
    "Conservative": {"Liquidity": 0.35, "Leverage": 0.30, "Profitability": 0.20, "Valuation": 0.15},
    "Balanced": {"Valuation": 0.25, "Profitability": 0.25, "Liquidity": 0.25, "Leverage": 0.25},
    "Growth-Oriented": {"Profitability": 0.40, "Valuation": 0.30, "Leverage": 0.20, "Liquidity": 0.10}
}


explain_df = pd.DataFrame()


# insight generator

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

# use for streamlit ui

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

        # category scores
        score_map = {"Positive": 1, "Neutral": 0, "Negative": -1}
        category_scores = {}
        for category, rows in grouped_results.items():
            scores = [score_map[r["Insight"]] for r in rows if r["Insight"] in score_map]
            if scores:
                category_scores[category] = sum(scores) / len(scores)


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
        
        
        #summary
            
        summary_counts = {
            "Positive": sum(1 for rows in grouped_results.values() for r in rows if r["Insight"] == "Positive"),
            "Neutral": sum(1 for rows in grouped_results.values() for r in rows if r["Insight"] == "Neutral"),
            "Negative": sum(1 for rows in grouped_results.values() for r in rows if r["Insight"] == "Negative")
        }

        summary_df = pd.DataFrame(summary_counts.items(), columns=["Rating", "Count"])
        st.subheader("Rating Breakdown")
        st.dataframe(summary_df, use_container_width=True)

        #final verdict
        st.subheader("Final Verdict")
        if "fundamentally strong" in overall:
            st.success(overall)
        elif "mixed but acceptable" in overall:
            st.info(overall)
        else:
            st.error(overall)

        # score table
        st.subheader("Category Scores (Profile-Adjusted)")
        score_df = pd.DataFrame.from_dict(category_scores, orient="index", columns=["Score"]).reset_index().rename(columns={"index": "Category"})
        st.dataframe(score_df)

        # explanation
        explain_rows = []
        for category, score in category_scores.items():
            weight = weights.get(category, 0)
            contribution = score * weight
            if score > 0.3:
                explanation = f"{category} metrics are strong and align well with a {profile.lower()} strategy."
            elif score >= 0:
                explanation = f"{category} metrics are mixed but acceptable for a {profile.lower()} investor."
            else:
                explanation = f"{category} metrics weaken the stock under a {profile.lower()} strategy."
            explain_rows.append({
                "Category": category,
                "Category Score": round(score, 2),
                "Profile Weight": weight,
                "Weighted Contribution": round(contribution, 3),
                "Explanation": explanation
            })
        explain_df = pd.DataFrame(explain_rows)

        st.write(f"This table explains how the **{profile} investor profile** weighted each category and how it contributed to the final verdict.")
        st.dataframe(explain_df, use_container_width=True)

        best = explain_df.loc[explain_df["Weighted Contribution"].idxmax()]
        worst = explain_df.loc[explain_df["Weighted Contribution"].idxmin()]

        st.info(f"**Biggest Strength:** {best['Category']} contributed most positively.\n\n**Biggest Risk:** {worst['Category']} had the largest negative impact.")

    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {e}")

# pdf download

st.subheader("Download Analyst Report")

def generate_pdf_report(ticker, profile, overall, grouped_results, category_scores, summary_counts, explain_df):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)

    elements = []
    styles = getSampleStyleSheet()
    if "Heading1" not in styles:
        styles.add(ParagraphStyle(name="Heading1", fontSize=16, leading=20, spaceAfter=10, spaceBefore=10))
    if "Heading2" not in styles:
        styles.add(ParagraphStyle(name="Heading2", fontSize=14, leading=18, spaceAfter=8, spaceBefore=8))
    if "NormalSmall" not in styles:
        styles.add(ParagraphStyle(name="NormalSmall", fontSize=10, leading=12))

    elements.append(Paragraph(f"Stock Ratio Analysis Report: {ticker.upper()}", styles["Heading1"]))
    elements.append(Paragraph(f"Investor Profile: {profile}", styles["Normal"]))
    elements.append(Paragraph(f"Date: {datetime.today().strftime('%Y-%m-%d')}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # final verdict
    elements.append(Paragraph("Final Verdict", styles["Heading2"]))
    if "fundamentally strong" in overall:
        verdict_color = "green"
    elif "mixed but acceptable" in overall:
        verdict_color = "blue"
    else:
        verdict_color = "red"
    elements.append(Paragraph(f"<font color='{verdict_color}'>{overall}</font>", styles["NormalSmall"]))
    elements.append(Spacer(1, 12))

    # Category Scores
    elements.append(Paragraph("Category Scores (Profile-Adjusted)", styles["Heading2"]))
    cat_data = [["Category", "Score"]] + [[c, f"{s:.2f}"] for c, s in category_scores.items()]
    table = Table(cat_data, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Rating Breakdown
    elements.append(Paragraph("Rating Breakdown", styles["Heading2"]))
    rating_data = [["Rating", "Count"]] + [[r, c] for r, c in summary_counts.items()]
    table = Table(rating_data, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Category Explanations
    elements.append(Paragraph("Category Explanations", styles["Heading2"]))
    explanation_data = [["Category", "Score", "Weight", "Contribution", "Explanation"]] + [
    [
        row["Category"],
        f"{row['Category Score']:.2f}",
        f"{row['Profile Weight']:.2f}",
        f"{row['Weighted Contribution']:.2f}",
        Paragraph(row["Explanation"], styles["NormalSmall"])  # wrap text
    ]
    for _, row in explain_df.iterrows()
]

    table = Table(explanation_data, hAlign="LEFT", colWidths=[80,50,50,70,300])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("ALIGN", (0,0), (-1,-1), "LEFT"),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Ratios by Category
    elements.append(Paragraph("Ratios by Category", styles["Heading2"]))
    for category, rows in grouped_results.items():
        elements.append(Paragraph(category, styles["NormalSmall"]))
        ratio_data = [["Ratio", "Value", "Insight"]] + [[r["Ratio"], str(r["Value"]), r["Insight"]] for r in rows]
        table = Table(ratio_data, hAlign="LEFT", colWidths=[150,80,150])
        table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.grey),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),
            ("ALIGN", (0,0), (-1,-1), "LEFT"),
            ("GRID", (0,0), (-1,-1), 0.5, colors.black),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 6))

    doc.build(elements)
    buffer.seek(0)
    return buffer

# -------------------
# PDF Download Button
# -------------------
if ticker:
    pdf_buffer = generate_pdf_report(ticker, profile, overall, grouped_results, category_scores, summary_counts, explain_df)
    st.download_button(
        label="📥 Download PDF Report",
        data=pdf_buffer,
        file_name=f"{ticker.upper()}_Stock_Analysis_Report.pdf",
        mime="application/pdf"
    )
