import streamlit as st
import yahoo


def show(ticker, yahoo_ticker_info, alpaca_ticker_info):
    st.write(f"Ticker: {ticker}")
    # st.write(f"Last Price (Yahoo): ${yahoo_ticker_info.get('currentPrice'):,.2f}")

    st.write(f"Alpaca Ask Price: ${alpaca_ticker_info.ask_price:,.2f}")
    st.write(f"Alpaca Bid Price: ${alpaca_ticker_info.bid_price:,.2f}")
    st.write(f"Alpaca Ask Size: ${alpaca_ticker_info.ask_size:,.2f}")
    st.write(f"Alpaca Bid Size: ${alpaca_ticker_info.bid_size:,.2f}")
    st.write(f"Alpaca Ask Exchange: {alpaca_ticker_info.ask_exchange}")
    st.write(f"Alpaca Bid Exchange: {alpaca_ticker_info.bid_exchange}")
    st.write(f"Alpaca Conditions: {alpaca_ticker_info.conditions}")
    st.write(f"Alpaca Tape: {alpaca_ticker_info.tape}")
    st.write(f"Alpaca Timestamp: {alpaca_ticker_info.timestamp}")
    st.write(f"Alpaca Symbol: {alpaca_ticker_info.symbol}")

    st.write(
        f"Day Low: ${yahoo_ticker_info.get('dayLow'):,.2f}   Day High: ${yahoo_ticker_info.get('dayHigh'):,.2f}"
    )

    ticker_history = yahoo.get_ticker_history(ticker)
    st.line_chart(ticker_history["Close"])
    st.write(ticker_history)

    st.write("Full ticker info:")
    st.write(yahoo_ticker_info)
