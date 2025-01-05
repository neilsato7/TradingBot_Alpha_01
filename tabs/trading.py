import streamlit as st


def show(ticker, alpaca_trader):
    st.write("Trading functionality coming soon...")
    # Add your trading interface elements here
    # If account_type is real, show a warning
    if alpaca_trader.account_type == "real":
        st.warning("This is a real money account. Be careful!")
