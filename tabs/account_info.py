import streamlit as st
import alpacafuncs


def show(account_type):
    st.write("Alpaca Account Info")

    # If account_type is real, show a warning
    if account_type == "real":
        st.warning("This is a real money account. Be careful!")

    alpaca_trader = alpacafuncs.AlpacaTrader(account_type)
    account_info = alpaca_trader.get_account_info()

    if account_info:
        account_num = account_info.account_number

        # Create HTML table with account info
        account_table_html = f"""
        <table style="width: 100%; border-collapse: collapse; text-align: left;">
            <tr style="border: 1px solid #303030;">
                <th style="border: 1px solid #303030; padding: 8px;">Account Details</th>
                <th style="border: 1px solid #303030; padding: 8px;">Status Information</th>
                <th style="border: 1px solid #303030; padding: 8px;">Trading Powers</th>
                <th style="border: 1px solid #303030; padding: 8px;">Account Values</th>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">
                    Account #: {account_num[:3]}...{account_num[-3:]}<br>
                    Currency: {account_info.currency}<br>
                    Created: {account_info.created_at}<br>
                    Multiplier: {account_info.multiplier}
                </td>
                <td style="border: 1px solid #303030; padding: 8px;">
                    Account Status: {account_info.status}<br>
                    Crypto Status: {account_info.crypto_status}<br>
                    Pattern Day Trader: {account_info.pattern_day_trader}<br>
                    Day Trade Count: {account_info.daytrade_count}
                </td>
                <td style="border: 1px solid #303030; padding: 8px;">
                    Buying Power: ${'{:,.2f}'.format(float(account_info.buying_power))}<br>
                    RegT Buying Power: ${'{:,.2f}'.format(float(account_info.regt_buying_power))}<br>
                    Day Trading Power: ${'{:,.2f}'.format(float(account_info.daytrading_buying_power))}<br>
                    Options Buying Power: ${'{:,.2f}'.format(float(account_info.options_buying_power))}
                </td>
                <td style="border: 1px solid #303030; padding: 8px;">
                    Portfolio Value: ${'{:,.2f}'.format(float(account_info.portfolio_value))}<br>
                    Cash: ${'{:,.2f}'.format(float(account_info.cash))}<br>
                    Equity: ${'{:,.2f}'.format(float(account_info.equity))}<br>
                    Last Equity: ${'{:,.2f}'.format(float(account_info.last_equity))}
                </td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">
                    Options Level: {account_info.options_approved_level}<br>
                    Trading Level: {account_info.options_trading_level}<br>
                    Shorting Enabled: {account_info.shorting_enabled}
                </td>
                <td style="border: 1px solid #303030; padding: 8px;">
                    Trading Blocked: {account_info.trading_blocked}<br>
                    Transfers Blocked: {account_info.transfers_blocked}<br>
                    Account Blocked: {account_info.account_blocked}<br>
                    Trade Suspended: {account_info.trade_suspended_by_user}
                </td>
                <td style="border: 1px solid #303030; padding: 8px;">
                    Non-Marginable Power: ${'{:,.2f}'.format(float(account_info.non_marginable_buying_power))}<br>
                    Initial Margin: ${'{:,.2f}'.format(float(account_info.initial_margin))}<br>
                    Maintenance Margin: ${'{:,.2f}'.format(float(account_info.maintenance_margin))}<br>
                    Last Maint. Margin: ${'{:,.2f}'.format(float(account_info.last_maintenance_margin))}
                </td>
                <td style="border: 1px solid #303030; padding: 8px;">
                    Long Market Value: ${'{:,.2f}'.format(float(account_info.long_market_value))}<br>
                    Short Market Value: ${'{:,.2f}'.format(float(account_info.short_market_value))}<br>
                    SMA: ${'{:,.2f}'.format(float(account_info.sma))}<br>
                    Accrued Fees: ${'{:,.2f}'.format(float(account_info.accrued_fees))}
                </td>
            </tr>
        </table>
        """
        st.markdown(account_table_html, unsafe_allow_html=True)
