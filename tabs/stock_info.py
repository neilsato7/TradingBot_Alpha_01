import streamlit as st
import yahoo
import altair as alt
import plotly.graph_objects as go


def show(ticker, yahoo_ticker_info, alpaca_ticker_info):
    st.subheader(f"{ticker} - {yahoo_ticker_info.get('longName','')}")
    st.write(f"Market Cap: ${yahoo_ticker_info.get('marketCap', 0):,}")
    # st.write(f"Last Price (Yahoo): ${yahoo_ticker_info.get('currentPrice'):,.2f}")

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        st.write("52week Low")
        st.write(f"${yahoo_ticker_info.get('fiftyTwoWeekLow', 0):,.2f}")

    with col2:
        st.write("Day's Low")
        st.write(f"${yahoo_ticker_info.get('dayLow', 0):,.2f}")

    with col3:
        st.write("Bid")
        st.markdown(
            f"<div style='background-color: lightcoral; color: black; padding: 5px; border-radius: 3px; text-align: center;'>${yahoo_ticker_info.get('bid', 0):,.2f}</div>",
            unsafe_allow_html=True,
        )
        st.write(f"{yahoo_ticker_info.get('bidSize', 0):,}")

    with col4:
        st.write("Last Price")
        st.write(f"${yahoo_ticker_info.get('currentPrice', 0):,.2f}")

    with col5:
        st.write("Ask")
        st.markdown(
            f"<div style='background-color: lightgreen; color: black; padding: 5px; border-radius: 3px; text-align: center;'>${yahoo_ticker_info.get('ask', 0):,.2f}</div>",
            unsafe_allow_html=True,
        )
        st.write(f"{yahoo_ticker_info.get('askSize', 0):,}")

    with col6:
        st.write("Day's High")
        st.write(f"${yahoo_ticker_info.get('dayHigh', 0):,.2f}")

    with col7:
        st.write("52week High")
        st.write(f"${yahoo_ticker_info.get('fiftyTwoWeekHigh', 0):,.2f}")

    ticker_history = yahoo.get_ticker_history(ticker)

    candlestick_chart = go.Figure(
        data=[
            go.Candlestick(
                x=ticker_history["Date"],
                open=ticker_history["Open"],
                high=ticker_history["High"],
                low=ticker_history["Low"],
                close=ticker_history["Close"],
            )
        ]
    )
    candlestick_chart.update_layout(xaxis_rangeslider_visible=False)
    st.plotly_chart(candlestick_chart, use_container_width=True)

    st.write("Full ticker info:")
    st.write(yahoo_ticker_info)
