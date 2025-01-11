import requests
import time
import pandas as pd
import os
import pytz
import streamlit as st
from dotenv import load_dotenv
from alpaca.data import (
    CryptoHistoricalDataClient,
    StockHistoricalDataClient,
    OptionHistoricalDataClient,
    StockLatestQuoteRequest,
    OptionLatestQuoteRequest,
)


MAX_RETRIES = 3
RETRY_DELAY = 3


# Get the API keys from the .env file
load_dotenv()


class AlpacaTrader:
    def __init__(self, account_type="paper"):
        self.account_type = account_type

        if account_type == "real":
            print("Real account")
            self.api_key = os.getenv("ALPACA_REAL_API_KEY")
            self.api_secret = os.getenv("ALPACA_REAL_API_SECRET")
            self.api_base_url = "https://api.alpaca.markets"
            self.assets_endpoint = f"{self.api_base_url}/v2/assets"

        else:
            print("Paper account")
            self.api_key = os.getenv("ALPACA_PAPER_API_KEY")
            self.api_secret = os.getenv("ALPACA_PAPER_API_SECRET")
            self.api_base_url = "https://paper-api.alpaca.markets"
            self.assets_endpoint = f"{self.api_base_url}/v2/assets"

        self.headers = self.get_alpaca_headers()

        self.stock_client = StockHistoricalDataClient(self.api_key, self.api_secret)
        self.option_client = OptionHistoricalDataClient(self.api_key, self.api_secret)
        self.crypto_client = CryptoHistoricalDataClient()

    def get_alpaca_headers(self):
        return {"APCA-API-KEY-ID": self.api_key, "APCA-API-SECRET-KEY": self.api_secret}

    #Share URL button
    def generate_share_url():
        base_url = "https://convalyticstradingbot.streamlit.app/"  #deployed app URL
        params = f"?filter={st.session_state.selected_filter}"

    return base_url + params
    
    def get_quote(self, ticker: str):
        """Get the latest quote for a given ticker"""
        request = StockLatestQuoteRequest(symbol_or_symbols=ticker)

        response = self.stock_client.get_stock_latest_quote(request)
        quote = response[ticker]  # Get the Quote object for the ticker

        #get ticker for the Share buttong
        st.session_state.selected_filter = ticker
        
        if st.button("Share"): 
        # Generate share URL based on current state 
            share_url = generate_share_url()
            st.write(f"Share this link: {share_url}")
      
        # Convert timestamp to eastern time:
        timestamp = quote.timestamp.astimezone(pytz.timezone("US/Eastern"))

        # Convert Quote object to dictionary
        return {
            "ask_price": quote.ask_price,
            "ask_size": quote.ask_size,
            "bid_price": quote.bid_price,
            "bid_size": quote.bid_size,
            "timestamp": timestamp,
        }

   


# alpacatest = AlpacaTrader(account_type="real")

# # testresponse = alpacatest.get_quote("AAPL")
# # print(testresponse)
# # print(type(testresponse))
# # print(testresponse.ask_price)


# symbol='AAPL'
# timestamp=datetime.datetime(2025, 1, 3, 20, 59, 59, 974248, tzinfo=TzInfo(UTC))
# bid_price=242.05
# bid_size=1.0
# bid_exchange='V'
# ask_price=256.28
# ask_size=2.0
# ask_exchange='V'
# conditions=['R']
# tape='C'
