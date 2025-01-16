import streamlit as st
import yahoofuncs

from datetime import datetime
from dotenv import load_dotenv
from tabs import stock_info, trading, analysis, account_info

load_dotenv()

# Make the app wide
st.set_page_config(layout="wide")


col1, col2, col3 = st.columns(3)
with col1:
    st.title("Trading Bot")
with col2:
    ticker = st.text_input("Enter a ticker symbol:")
with col3:
    account_type = st.selectbox("Account Type (Alpaca Only)", ["paper", "real"])


if ticker:
    ticker = ticker.upper()
    yanalysis = yahoofuncs.YahooAnalysis(ticker)

    # Create tabs
    stock_info_tab, analysis_tab, trading_tab, account_info_tab = st.tabs(
        ["Stock Info", "Analysis", "Trading", "Account Info"]
    )

    # Stock Info tab
    with stock_info_tab:
        stock_info.show(ticker, yanalysis)

    # Analysis tab
    with analysis_tab:
        analysis.show(ticker, yanalysis)

    # Trading tab
    with trading_tab:
        trading.show(ticker, yanalysis, account_type)

    # Account Info tab
    with account_info_tab:
        account_info.show(account_type)
