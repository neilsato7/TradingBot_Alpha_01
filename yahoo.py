import yfinance as yf


def get_ticker_data(ticker):
    return yf.Ticker(ticker)


def get_ticker_info(ticker):
    return yf.Ticker(ticker).info


def get_ticker_history(ticker, period="1d"):
    return yf.Ticker(ticker).history(period=period)


def get_ticker_recommendations(ticker):
    return yf.Ticker(ticker).recommendations
