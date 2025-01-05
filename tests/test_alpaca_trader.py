import pytest
from alpacafuncs import AlpacaTrader
from dotenv import load_dotenv

load_dotenv()


class TestAlpacaTrader:
    def setup_method(self):
        self.testTrader = AlpacaTrader(account_type="paper")

    def test_init_paper_trading(self):
        """Test initialization with paper trading account"""
        assert self.testTrader.account_type == "paper"
        assert self.testTrader.api_base_url == "https://paper-api.alpaca.markets"
        assert (
            self.testTrader.assets_endpoint
            == "https://paper-api.alpaca.markets/v2/assets"
        )

    def test_get_quote(self):
        """Test get_quote method"""

        # Test the method
        result = self.testTrader.get_quote("AAPL")
        print(result)
        assert result.symbol == "AAPL"
        # Verify the result
        # assert result == {"symbol": "AAPL", "price": 150.0}
