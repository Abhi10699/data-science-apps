import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Price Ticker

Shown are the stock **closing price** and ***volume*** of Meta!

""")


ticker =  "META"
ticker_data = yf.Ticker(ticker)
ticker_df = ticker_data.history(period="1d", start="2010-1-1",end="2023-6-1")

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)