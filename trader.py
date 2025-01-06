import streamlit as st
import yahoo
import alpacafuncs
from datetime import datetime
from dotenv import load_dotenv
from tabs import stock_info, trading

load_dotenv()

# Make the app wide
st.set_page_config(layout="wide")

st.title("Trading Bot")
col1, col2, col3 = st.columns(3)
with col1:
    ticker = st.text_input("Enter a ticker symbol:")


if ticker:
    ticker = ticker.upper()
    yahoo_ticker_info = yahoo.get_ticker_info(ticker)

    # Create tabs
    stock_info_tab, trading_tab = st.tabs(["Stock Info", "Trading"])

    # Stock Info tab
    with stock_info_tab:
        stock_info.show(ticker, yahoo_ticker_info)

    # Trading tab
    with trading_tab:
        trading.show(ticker)
