import requests
import time
import pandas as pd
import os
from dotenv import load_dotenv
from alpaca.data import (
    CryptoHistoricalDataClient,
    StockHistoricalDataClient,
    OptionHistoricalDataClient,
    StockLatestQuoteRequest,
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

    def get_quote(self, ticker: str):
        """Get the latest quote for a given ticker"""
        request = StockLatestQuoteRequest(symbol_or_symbols=ticker)
        print(request)
        response = self.stock_client.get_stock_latest_quote(request)
        print(response)
        response = response.get(ticker)
        print(response)
        return response


# alpacatest = AlpacaTrader(account_type="real")
# testresponse = alpacatest.get_quote("AAPL")
# print(testresponse)
# print(type(testresponse))
# print(testresponse.ask_price)

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
