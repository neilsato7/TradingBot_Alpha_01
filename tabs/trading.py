import streamlit as st
import alpacafuncs


def show(ticker):
    st.write("Trading functionality coming soon...")
    account_type = st.selectbox("Account Type", ["paper", "real"])
    alpaca_trader = alpacafuncs.AlpacaTrader(account_type)
    alpaca_ticker_info = alpaca_trader.get_quote(ticker)

    # Add your trading interface elements here
    # If account_type is real, show a warning
    if alpaca_trader.account_type == "real":
        st.warning("This is a real money account. Be careful!")
