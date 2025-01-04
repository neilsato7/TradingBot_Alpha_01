import streamlit as st
import yahoo

st.title("Trader")

st.write("Welcome to the Trader app!")


ticker = st.text_input("Enter a ticker symbol:")

if ticker:
    ticker_info = yahoo.get_ticker_info(ticker)
    st.write(ticker_info)
