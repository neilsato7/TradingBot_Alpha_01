import yfinance as yf
import json


def get_ticker_data(ticker):
    print(f"Getting {ticker} data")
    return yf.Ticker(ticker)


def get_ticker_info(ticker):
    print(f"Getting {ticker} info")
    return yf.Ticker(ticker).info


def get_ticker_history(ticker, period="3mo"):
    print(f"Getting {ticker} history for {period}")
    ticker_history = yf.Ticker(ticker).history(period=period)
    ticker_history = ticker_history.rename_axis("Date").reset_index()
    # ticker_history["Date"] = ticker_history["Date"].dt.strftime("%Y-%m-%d")
    return ticker_history


def get_ticker_recommendations(ticker):
    return yf.Ticker(ticker).recommendations


def get_news(ticker):
    return yf.Ticker(ticker).news


####### ANALYSIS #######################################################
class YahooAnalysis:
    def __init__(self, ticker):
        self.ticker = ticker
        self.ticker_info = get_ticker_info(ticker)
        self.ticker_history = get_ticker_history(ticker)

    def new_high_volume_scanner(self, range_days=30):
        # get the volume for the last range_days
        volume = self.ticker_history["Volume"].tail(range_days)
        # get the max volume
        max_volume = volume.max()

        # get the average volume for the last range_days
        average_volume = volume.mean()

        # get the current volume
        current_volume = self.ticker_history["Volume"].iloc[-1]
        # calculate the difference between the current volume and the max volume
        if current_volume >= 0 and max_volume >= 0:
            volume_diff = current_volume - max_volume
            # calculate the percentage difference
            volume_diff_pct = volume_diff / max_volume

            # calculate the percentage difference between the current volume and the average volume
            volume_diff_pct_avg = (current_volume - average_volume) / average_volume

            # If the current volume is greater than the max volume, return True
            if current_volume >= max_volume:
                signal = True
            else:
                signal = False

            vol_scanner = {
                "current_volume": f"{current_volume:,.0f}",
                "average_volume": f"{average_volume:,.0f}",
                "max_volume": f"{max_volume:,.0f}",
                "volume_diff": f"{volume_diff:,.0f}",
                "volume_diff_pct": f"{volume_diff_pct:.2%}",
                "volume_diff_pct_avg": f"{volume_diff_pct_avg:.2%}",
                "signal": signal,
            }
            return vol_scanner
        else:
            return None


# ### TESTING ##########################################################
# news = get_news("AAPL")
# # print(news)
# # format the news as json
# print(json.dumps(news, indent=4))

# content = news[0].get("content", {})
# print(content.get("title", ""))

# analysis = YahooAnalysis("AAPL")
# print(analysis.new_high_volume_scanner(range_days=30))
