import yfinance as yf


def get_ticker_data(ticker):
    return yf.Ticker(ticker)


def get_ticker_info(ticker):
    return yf.Ticker(ticker).info


def get_ticker_history(ticker, period="3mo"):
    ticker_history = yf.Ticker(ticker).history(period=period)
    ticker_history = ticker_history.rename_axis("Date").reset_index()
    # ticker_history["Date"] = ticker_history["Date"].dt.strftime("%Y-%m-%d")
    return ticker_history


def get_ticker_recommendations(ticker):
    return yf.Ticker(ticker).recommendations
