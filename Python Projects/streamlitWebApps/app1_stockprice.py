import yfinance as yf
import streamlit as st

# Markdown
st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

# get data on this ticker
tickerData = yf.Ticker('AAPL')
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)


st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)

# Run this Programm on the Browser
# Open Terminal
# $ streamlit run app1.py