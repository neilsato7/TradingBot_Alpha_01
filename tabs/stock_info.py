import streamlit as st
import yahoofuncs
import altair as alt
import plotly.graph_objects as go
from datetime import datetime
import pytz


def show(ticker, yanalysis):
    st.subheader(
        f"{ticker} - {yanalysis.ticker_info.get('longName','')} ({yanalysis.ticker_info.get('industry','')} / {yanalysis.ticker_info.get('sector','')})"
    )
    st.write(f"Market Cap: ${yanalysis.ticker_info.get('marketCap', 0):,}")
    st.write(f"Float: {yanalysis.ticker_info.get('floatShares', 0):,}")
    if yanalysis.ticker_info.get("shortRatio", 0) > 0:
        st.write(
            f"Short Ratio: {yanalysis.ticker_info.get('shortRatio', 0):.2f}  --- Short Percent of Float: {yanalysis.ticker_info.get('shortPercentOfFloat', 0):.2%}"
        )

    # Create table with stock price information
    # Create a plotly figure for price range visualization
    price_data = {
        "labels": [
            "Day's Low",
            "Bid",
            "Last",
            "Ask",
            "Day's High",
        ],
        "values": [
            yanalysis.ticker_info.get("dayLow", 0),
            yanalysis.ticker_info.get("bid", 0),
            yanalysis.ticker_info.get("currentPrice", 0),
            yanalysis.ticker_info.get("ask", 0),
            yanalysis.ticker_info.get("dayHigh", 0),
        ],
    }

    fig = go.Figure()

    # Add vertical lines for each price point
    for label, value in zip(price_data["labels"], price_data["values"]):
        color = (
            "lightcoral"
            if label == "Bid"
            else (
                "lightgreen"
                if label == "Ask"
                else (
                    "darkred"
                    if label == "Day's Low"
                    else "darkgreen" if label == "Day's High" else "white"
                )
            )
        )
        text_position = "bottom center" if label in ["Bid", "Ask"] else "top center"

        fig.add_trace(
            go.Scatter(
                x=[value],
                y=[0],
                mode="markers+text",
                name=label,
                text=[f"${value:,.2f}<br>{label}"],
                textposition=text_position,
                marker=dict(size=12, color=color),
                showlegend=False,
            )
        )

    chart_scale = yanalysis.ticker_info.get("dayHigh", 0) - yanalysis.ticker_info.get(
        "dayLow", 0
    )
    low_range = yanalysis.ticker_info.get("dayLow", 0) - chart_scale * 0.05
    high_range = yanalysis.ticker_info.get("dayHigh", 0) + chart_scale * 0.05

    # Add a range slider
    fig.update_layout(
        title="Price Range",
        xaxis=dict(
            range=[
                low_range,
                high_range,
            ],
            title="Price ($)",
        ),
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        height=200,
        margin=dict(t=20, b=20, l=10, r=10),  # Increased left and right margins
    )

    st.plotly_chart(fig, use_container_width=True)

    # Create an html table with volume, averageVolume, averageVolume10days
    volume_table_html = f"""
    <table style="width: 100%; border-collapse: collapse; text-align: center;">
        <tr style="border: 1px solid #303030;">
            <th style="border: 1px solid #303030; padding: 8px;">Volume</th>
            <th style="border: 1px solid #303030; padding: 8px;">Average Volume</th>
            <th style="border: 1px solid #303030; padding: 8px;">Average Volume 10 Days</th>
        </tr>
        <tr style="border: 1px solid #303030;">
            <td style="border: 1px solid #303030; padding: 8px;">{yanalysis.ticker_info.get('volume', 0):,}</td>
            <td style="border: 1px solid #303030; padding: 8px;">{yanalysis.ticker_info.get('averageVolume', 0):,}</td>
            <td style="border: 1px solid #303030; padding: 8px;">{yanalysis.ticker_info.get('averageVolume10days', 0):,}</td>
        </tr>
    </table>
    """
    st.markdown(volume_table_html, unsafe_allow_html=True)

    candlestick_chart = go.Figure(
        data=[
            go.Candlestick(
                x=yanalysis.ticker_history["Date"],
                open=yanalysis.ticker_history["Open"],
                high=yanalysis.ticker_history["High"],
                low=yanalysis.ticker_history["Low"],
                close=yanalysis.ticker_history["Close"],
            )
        ]
    )
    candlestick_chart.update_layout(xaxis_rangeslider_visible=False)
    st.plotly_chart(candlestick_chart, use_container_width=True)

    st.header("News:")
    news = yanalysis.get_news()
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

    st.header("Full ticker info for development:")
    st.write(yanalysis.ticker_info)
