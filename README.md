# 📈 Simple Moving Average Strategy Analyzer

This Streamlit app helps visualize the **performance of a stock index following simple moving average (MA) events**. It is designed to test the predictive power of basic technical analysis strategies — and to show their limitations.

🔗 **Live demo**: [alexis-simple-ma.streamlit.app](https://alexis-simple-ma.streamlit.app/)

---

## 🚀 Features

- Select any OHLC (Open/High/Low/Close) financial dataset
- Choose a simple moving average (MA) length
- Detect when the price crosses below the moving average after staying above for a set number of days
- Measure **maximum performance over the next _n_ days** after the event
- Plot a histogram of observed performances
- Visualize the distribution and spot **mixtures of Gaussian behavior**

---

## 📉 Insight

Despite identifying clear event-based entry points (e.g., price dropping below MA after X days above), the resulting performance histogram often **resembles a mixture of Gaussian distributions**, suggesting:

> Even seemingly clever strategies may not offer a consistent edge over the market.

This app is a reminder that **simple strategies do not beat randomness** — and emphasizes the need for deeper statistical modeling in financial forecasting.

---

## 📦 Requirements

The app runs on [Streamlit Cloud](https://streamlit.io/cloud), but if you want to run it locally:

```bash
pip install streamlit matplotlib pandas numpy
streamlit run simpleMA.py
```
