import streamlit as st
import alpacafuncs


def show(ticker, yanalysis, account_type):
    st.write("Trading functionality coming soon...")

    # If account_type is real, show a warning
    if account_type == "real":
        st.warning("This is a real money account. Be careful!")

    alpaca_trader = alpacafuncs.AlpacaTrader(account_type)

    if ticker:
        alpaca_ticker_info = alpaca_trader.get_quote(ticker)

        st.write(f"Quote Timestamp: {alpaca_ticker_info.get('timestamp', 'N/A')}")
        # Create table with stock price information
        alpaca_price_table_html = f"""
        <table style="width: 100%; border-collapse: collapse; text-align: center;">
            <tr style="border: 1px solid #303030;">
                <th style="border: 1px solid #303030; padding: 8px;">Bid</th>
                <th style="border: 1px solid #303030; padding: 8px;">Ask</th>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px; background-color: lightcoral; color: black;">${alpaca_ticker_info.get('bid_price', 0):,.2f}<br>{alpaca_ticker_info.get('bid_size', 0):,}</td>
                <td style="border: 1px solid #303030; padding: 8px; background-color: lightgreen; color: black;">${alpaca_ticker_info.get('ask_price', 0):,.2f}<br>{alpaca_ticker_info.get('ask_size', 0):,}</td>
            </tr>
        </table>
        """
        st.markdown(alpaca_price_table_html, unsafe_allow_html=True)
