import yfinance as yf
import streamlit as st
from datetime import date
import pandas as pd


df = pd.read_csv('NSE-EQ-SYMOBOLS.csv')
symbol_tuple = tuple(list(df['SYMBOL']))

st.write("""
# Simple Stock Price App
""")

#define the ticker symbol
tickerSymbol = st.selectbox('Stock List', symbol_tuple) + '.NS'

st.write("""
Shown are the stock **closing price** and **volume** of
""" + tickerSymbol + "!")

#till today
today = date.today()

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end=today)
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.line_chart(tickerDf.Close)
st.bar_chart(tickerDf.Volume)
