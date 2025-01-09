import streamlit as st
import yahoo
import altair as alt
import plotly.graph_objects as go
from datetime import datetime
import pytz


def show(ticker, yahoo_ticker_info):
    st.subheader(
        f"{ticker} - {yahoo_ticker_info.get('longName','')} ({yahoo_ticker_info.get('industry','')} / {yahoo_ticker_info.get('sector','')})"
    )
    st.write(f"Market Cap: ${yahoo_ticker_info.get('marketCap', 0):,}")
    st.write(f"Float: {yahoo_ticker_info.get('floatShares', 0):,}")
    if yahoo_ticker_info.get("shortRatio", 0) > 0:
        st.write(
            f"Short Ratio: {yahoo_ticker_info.get('shortRatio', 0):.2f}  --- Short Percent of Float: {yahoo_ticker_info.get('shortPercentOfFloat', 0):.2%}"
        )

    # Create table with stock price information
    price_table_html = f"""
    <table style="width: 100%; border-collapse: collapse; text-align: center;">
        <tr style="border: 1px solid #303030;">
            <th style="border: 1px solid #303030; padding: 8px;">52week Low</th>
            <th style="border: 1px solid #303030; padding: 8px;">Day's Low</th>
            <th style="border: 1px solid #303030; padding: 8px;">Bid</th>
            <th style="border: 1px solid #303030; padding: 8px;">Last Price</th>
            <th style="border: 1px solid #303030; padding: 8px;">Ask</th>
            <th style="border: 1px solid #303030; padding: 8px;">Day's High</th>
            <th style="border: 1px solid #303030; padding: 8px;">52week High</th>
        </tr>
        <tr style="border: 1px solid #303030;">
            <td style="border: 1px solid #303030; padding: 8px;">${yahoo_ticker_info.get('fiftyTwoWeekLow', 0):,.2f}</td>
            <td style="border: 1px solid #303030; padding: 8px;">${yahoo_ticker_info.get('dayLow', 0):,.2f}</td>
            <td style="border: 1px solid #303030; padding: 8px; background-color: lightcoral; color: black;">${yahoo_ticker_info.get('bid', 0):,.2f}<br>{yahoo_ticker_info.get('bidSize', 0):,}</td>
            <td style="border: 1px solid #303030; padding: 8px;">${yahoo_ticker_info.get('currentPrice', 0):,.2f}</td>
            <td style="border: 1px solid #303030; padding: 8px; background-color: lightgreen; color: black;">${yahoo_ticker_info.get('ask', 0):,.2f}<br>{yahoo_ticker_info.get('askSize', 0):,}</td>
            <td style="border: 1px solid #303030; padding: 8px;">${yahoo_ticker_info.get('dayHigh', 0):,.2f}</td>
            <td style="border: 1px solid #303030; padding: 8px;">${yahoo_ticker_info.get('fiftyTwoWeekHigh', 0):,.2f}</td>
        </tr>
    </table>
    """
    st.markdown(price_table_html, unsafe_allow_html=True)

    # Create an html table with volume, averageVolume, averageVolume10days
    volume_table_html = f"""
    <table style="width: 100%; border-collapse: collapse; text-align: center;">
        <tr style="border: 1px solid #303030;">
            <th style="border: 1px solid #303030; padding: 8px;">Volume</th>
            <th style="border: 1px solid #303030; padding: 8px;">Average Volume</th>
            <th style="border: 1px solid #303030; padding: 8px;">Average Volume 10 Days</th>
        </tr>
        <tr style="border: 1px solid #303030;">
            <td style="border: 1px solid #303030; padding: 8px;">{yahoo_ticker_info.get('volume', 0):,}</td>
            <td style="border: 1px solid #303030; padding: 8px;">{yahoo_ticker_info.get('averageVolume', 0):,}</td>
            <td style="border: 1px solid #303030; padding: 8px;">{yahoo_ticker_info.get('averageVolume10days', 0):,}</td>
        </tr>
    </table>
    """
    st.markdown(volume_table_html, unsafe_allow_html=True)

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

    st.header("News:")
    news = yahoo.get_news(ticker)
    for news_item in news:
        item = news_item.get("content", {})
        st.subheader(item.get("title"))

        pub_date = item.get("pubDate")
        # convert pub_date from "2025-01-09T10:30:00Z" to datetime in eastern time
        pub_date = datetime.strptime(pub_date, "%Y-%m-%dT%H:%M:%SZ")
        pub_date = pub_date.astimezone(pytz.timezone("US/Eastern"))

        st.write(pub_date)

        st.write(item.get("summary"))

        canonical_url = item.get("canonicalUrl", {})
        news_url = canonical_url.get("url", "")
        st.markdown(f"{news_url}")
        st.divider()

    st.write(news)  # todo: doesn't work
