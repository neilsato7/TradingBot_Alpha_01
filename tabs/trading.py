import streamlit as st
import alpacafuncs
import time


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
                <th style="border: 1px solid #303030; padding: 8px;">Bid (Sell price)</th>
                <th style="border: 1px solid #303030; padding: 8px;">Ask (Buy price)</th>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px; background-color: lightcoral; color: black;">${alpaca_ticker_info.get('bid_price', 0):,.2f}<br>{alpaca_ticker_info.get('bid_size', 0):,}</td>
                <td style="border: 1px solid #303030; padding: 8px; background-color: lightgreen; color: black;">${alpaca_ticker_info.get('ask_price', 0):,.2f}<br>{alpaca_ticker_info.get('ask_size', 0):,}</td>
            </tr>
        </table>
        """
        st.markdown(alpaca_price_table_html, unsafe_allow_html=True)

        st.header("Place an order")
        order_quantity = st.text_input("Quantity", value=1)

        market_order = None
        submitted_order = ""

        # Create a buy button
        if st.button(
            f"Buy {ticker} at market ask price: ${alpaca_ticker_info.get('ask_price', 0):,.2f}"
        ):
            alpaca_trader.market_order(
                ticker, order_quantity, "buy", time_in_force="gtc"
            )
            st.write(alpaca_trader.market_order_data)
            time.sleep(5)

        # Create a sell button
        if st.button(
            f"Sell {ticker} at bid price: ${alpaca_ticker_info.get('bid_price', 0):,.2f}"
        ):
            alpaca_trader.market_order(
                ticker, order_quantity, "sell", time_in_force="gtc"
            )
            st.write(alpaca_trader.market_order_data)
            time.sleep(5)

        # TODO: Submitting the order is not working. *Only tested after hours, maybe that's the issue?
        # if alpaca_trader.market_order_data:
        #     # Create a submit button
        #     if st.button("Submit Order"):
        #         alpaca_trader.submit_order()
        #         time.sleep(5)

        # st.write(alpaca_trader.submitted_order)

        # Get asset info
        asset_info = alpaca_trader.get_asset(ticker)

        # Write asset info to screen:
        # Create HTML table for asset information
        asset_table_html = f"""
        <table style="width: 100%; border-collapse: collapse; text-align: left;">
            <tr style="border: 1px solid #303030;">
                <th style="border: 1px solid #303030; padding: 8px;">Property</th>
                <th style="border: 1px solid #303030; padding: 8px;">Value</th>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Asset ID</td>
                <td style="border: 1px solid #303030; padding: 8px;">{asset_info.id}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Asset Class</td>
                <td style="border: 1px solid #303030; padding: 8px;">{asset_info.asset_class}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Exchange</td>
                <td style="border: 1px solid #303030; padding: 8px;">{asset_info.exchange}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Symbol</td>
                <td style="border: 1px solid #303030; padding: 8px;">{asset_info.symbol}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Name</td>
                <td style="border: 1px solid #303030; padding: 8px;">{asset_info.name}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Status</td>
                <td style="border: 1px solid #303030; padding: 8px;">{asset_info.status}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Tradable</td>
                <td style="border: 1px solid #303030; padding: 8px; background-color: {'lightcoral' if not asset_info.tradable else 'inherit'};">{asset_info.tradable}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Marginable</td>
                <td style="border: 1px solid #303030; padding: 8px;">{asset_info.marginable}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Shortable</td>
                <td style="border: 1px solid #303030; padding: 8px;">{asset_info.shortable}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Easy to Borrow</td>
                <td style="border: 1px solid #303030; padding: 8px;">{asset_info.easy_to_borrow}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Fractionable</td>
                <td style="border: 1px solid #303030; padding: 8px;">{asset_info.fractionable}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Min Order Size</td>
                <td style="border: 1px solid #303030; padding: 8px;">{asset_info.min_order_size if asset_info.min_order_size else 'N/A'}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Min Trade Increment</td>
                <td style="border: 1px solid #303030; padding: 8px;">{asset_info.min_trade_increment if asset_info.min_trade_increment else 'N/A'}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Price Increment</td>
                <td style="border: 1px solid #303030; padding: 8px;">{asset_info.price_increment if asset_info.price_increment else 'N/A'}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Maintenance Margin Requirement</td>
                <td style="border: 1px solid #303030; padding: 8px;">{asset_info.maintenance_margin_requirement}%</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Attributes</td>
                <td style="border: 1px solid #303030; padding: 8px;">{', '.join(asset_info.attributes) if asset_info.attributes else 'None'}</td>
            </tr>
        </table>
        """
        st.markdown(asset_table_html, unsafe_allow_html=True)
