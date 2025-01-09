import streamlit as st
import yahoo
import altair as alt
import plotly.graph_objects as go
from datetime import datetime
import pytz


def show(ticker, yahoo_ticker_info):
    analysis = yahoo.YahooAnalysis(ticker)
    vol_scanner = analysis.new_high_volume_scanner(range_days=30)

    # if vol_scanner is not None, show the volume scanner
    if vol_scanner is not None:
        volume_table_html = f"""
        <table style="width: 100%; border-collapse: collapse; text-align: left;">
            <tr style="border: 1px solid #303030;">
                <th style="border: 1px solid #303030; padding: 8px;" colspan="2">New High Volume Scanner (30d)</th>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Current Volume</td>
                <td style="border: 1px solid #303030; padding: 8px;">{vol_scanner.get('current_volume')}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Average Volume</td>
                <td style="border: 1px solid #303030; padding: 8px;">{vol_scanner.get('average_volume')}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Max Volume</td>
                <td style="border: 1px solid #303030; padding: 8px;">{vol_scanner.get('max_volume')}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Current vs Avg Volume %</td>
                <td style="border: 1px solid #303030; padding: 8px;">{vol_scanner.get('volume_diff_pct_avg')}</td>
            </tr>            
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Current vs Max Volume %</td>
                <td style="border: 1px solid #303030; padding: 8px;">{vol_scanner.get('volume_diff_pct')}</td>
            </tr>
            <tr style="border: 1px solid #303030;">
                <td style="border: 1px solid #303030; padding: 8px;">Signal</td>
                <td style="border: 1px solid #303030; padding: 8px; color: black; background-color: {'lightgreen' if vol_scanner.get('signal') else 'lightcoral'};">
                    {vol_scanner.get('signal')}
                </td>
            </tr>
        </table>
        """
        st.markdown(volume_table_html, unsafe_allow_html=True)
