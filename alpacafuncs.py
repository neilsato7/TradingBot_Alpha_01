import requests
import time
import pandas as pd
import os
import pytz
from dotenv import load_dotenv
from alpaca.data import (
    CryptoHistoricalDataClient,
    StockHistoricalDataClient,
    OptionHistoricalDataClient,
    StockLatestQuoteRequest,
    OptionLatestQuoteRequest,
)
from alpaca.trading import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

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
            self.trading_client = TradingClient(
                self.api_key, self.api_secret, paper=False
            )

        else:
            print("Paper account")
            self.api_key = os.getenv("ALPACA_PAPER_API_KEY")
            self.api_secret = os.getenv("ALPACA_PAPER_API_SECRET")
            self.api_base_url = "https://paper-api.alpaca.markets"
            self.assets_endpoint = f"{self.api_base_url}/v2/assets"
            self.trading_client = TradingClient(
                self.api_key, self.api_secret, paper=True
            )
        self.headers = self.get_alpaca_headers()

        self.stock_client = StockHistoricalDataClient(self.api_key, self.api_secret)
        self.option_client = OptionHistoricalDataClient(self.api_key, self.api_secret)
        self.crypto_client = CryptoHistoricalDataClient()
        self.market_order_data = None
        self.submitted_order = None

    def get_alpaca_headers(self):
        return {"APCA-API-KEY-ID": self.api_key, "APCA-API-SECRET-KEY": self.api_secret}

    def get_account_info(self):
        print("Getting account info")
        account = self.trading_client.get_account()

        return account

    def get_quote(self, ticker: str):
        """Get the latest quote for a given ticker"""
        print(f"Getting quote for {ticker}")
        request = StockLatestQuoteRequest(symbol_or_symbols=ticker)

        try:
            response = self.stock_client.get_stock_latest_quote(request)
            if ticker in response and response[ticker]:
                quote = response[ticker]  # Get the Quote object for the ticker

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
        except Exception as e:
            print(f"Error getting quote for {ticker}: {str(e)}")
        return {"error": "Error getting quote for ticker"}

    def get_asset(self, ticker: str):
        """Get the asset info for a given ticker"""
        print(f"Getting asset info for {ticker}")
        asset = self.trading_client.get_asset(ticker)
        if asset:
            return asset
        else:
            return {"error": "Error getting asset info for ticker"}

    def market_order(
        self, ticker: str, quantity: int, side: str, time_in_force: str = "gtc"
    ):
        """Prepares a market order to be submitted to the trading client"""
        print(
            f"Preparing market order for {ticker} with quantity {quantity} and side {side}"
        )
        if side == "buy":
            side = OrderSide.BUY
        elif side == "sell":
            side = OrderSide.SELL
        else:
            raise ValueError("Invalid side. Must be 'buy' or 'sell'.")

        if time_in_force == "gtc":
            time_in_force = TimeInForce.DAY
        else:
            raise ValueError("Invalid time in force. Must be 'gtc' or 'gtc'.")

        self.market_order_data = MarketOrderRequest(
            symbol=ticker, qty=quantity, side=side, time_in_force=time_in_force
        )
        return self.market_order_data

    def submit_order(self):
        """Submit an order to the trading client"""
        print(f"Submitting order: {self.market_order_data}")
        self.submitted_order = self.trading_client.submit_order(self.market_order_data)
        print(self.submitted_order)
        return self.submitted_order


# alpacatest = AlpacaTrader(account_type="paper")
# account_info = alpacatest.get_account_info()
# print(account_info)

# market_order = alpacatest.market_order("AAPL", 15, "buy")
# print(market_order)

# submitted_order = alpacatest.submit_order()
# print(submitted_order)


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
