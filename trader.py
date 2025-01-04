import streamlit as st
import yahoo

# Make the app wide
st.set_page_config(layout="wide")

st.title("Trading Bot")


ticker = st.text_input("Enter a ticker symbol:")

if ticker:
    ticker_info = yahoo.get_ticker_info(ticker)
    st.write(f"Ticker: {ticker}")
    st.write(f"Last Price: ${ticker_info.get('currentPrice'):,.2f}")
    st.write(
        f"Bid: ${ticker_info.get('bid'):,.2f}   Ask: ${ticker_info.get('ask'):,.2f}"
    )
    st.write(
        f"Day Low: ${ticker_info.get('dayLow'):,.2f}   Day High: ${ticker_info.get('dayHigh'):,.2f}"
    )

    ticker_history = yahoo.get_ticker_history(ticker)

    # plot the history
    st.line_chart(ticker_history["Close"])

    st.write(ticker_history)

    st.write("Full ticker info:")
    st.write(ticker_info)

# ticker_info example:
# {"address1":"775 Heinz Avenue","city":"Berkeley","state":"CA","zip":"94710","country":"United States","phone":"510 210 5550","website":"https://www.rigetti.com","industry":"Computer Hardware","industryKey":"computer-hardware","industryDisp":"Computer Hardware","sector":"Technology","sectorKey":"technology","sectorDisp":"Technology","longBusinessSummary":"Rigetti Computing, Inc., through its subsidiaries, builds quantum computers and the superconducting quantum processors. The company offers cloud in a form of quantum processing unit, such as 9-qubit chip and Ankaa-2 system under the Novera brand name; and sells access to its quantum computers through quantum computing as a service. It also provides quantum cloud services that provides various range of support in programming, public or private clouds integration, and connectivity, as well as quantum operating system software that supports both public and private cloud architectures. In addition, the company offers professional services, such as algorithm development, benchmarking, quantum application programming, and software development. The company serves commercial enterprises, government organizations, and international government entities. It has operations in the United States and the United Kingdom. Rigetti Computing, Inc. was founded in 2013 and is headquartered in Berkeley, California.","fullTimeEmployees":134,"companyOfficers":[{"maxAge":1,"name":"Dr. Subodh K. Kulkarni Ph.D.","age":59,"title":"CEO, President & Director","yearBorn":1965,"fiscalYear":2023,"totalPay":1016690,"exercisedValue":0,"unexercisedValue":8663},{"maxAge":1,"name":"Mr. David  Rivas","age":62,"title":"Chief Technology Officer","yearBorn":1962,"fiscalYear":2023,"totalPay":428736,"exercisedValue":0,"unexercisedValue":262091},{"maxAge":1,"name":"Mr. Jeffrey A. Bertelsen","age":61,"title":"Chief Financial Officer","yearBorn":1963,"fiscalYear":2023,"exercisedValue":0,"unexercisedValue":0},{"maxAge":1,"name":"Ms. Jackie  Kaweck","title":"Senior Vice President of Human Resources","fiscalYear":2023,"exercisedValue":0,"unexercisedValue":0},{"maxAge":1,"name":"Mr. Mike  Pelstring","title":"Senior Vice President of Engineering","fiscalYear":2023,"exercisedValue":0,"unexercisedValue":0},{"maxAge":1,"name":"Dr. Andrew  Bestwick","title":"Senior Vice President of Quantum Systems","fiscalYear":2023,"exercisedValue":0,"unexercisedValue":0}],"auditRisk":10,"boardRisk":6,"compensationRisk":6,"shareHolderRightsRisk":8,"overallRisk":8,"governanceEpochDate":1735689600,"compensationAsOfEpochDate":1703980800,"maxAge":86400,"priceHint":2,"previousClose":20,"open":18.97,"dayLow":17.7,"dayHigh":20.37,"regularMarketPreviousClose":20,"regularMarketOpen":18.97,"regularMarketDayLow":17.7,"regularMarketDayHigh":20.37,"beta":2.138,"forwardPE":-95.1,"volume":161646814,"regularMarketVolume":161646814,"averageVolume":82704601,"averageVolume10days":189147040,"averageDailyVolume10Day":189147040,"bid":18.92,"ask":19.09,"bidSize":6600,"askSize":6600,"marketCap":5326532096,"fiftyTwoWeekLow":0.66,"fiftyTwoWeekHigh":20.37,"priceToSalesTrailing12Months":447.90884,"fiftyDayAverage":5.2738,"twoHundredDayAverage":2.10115,"currency":"USD","enterpriseValue":3587376384,"floatShares":165899363,"sharesOutstanding":280048992,"sharesShort":36308183,"sharesShortPriorMonth":26132461,"sharesShortPreviousMonthDate":1731628800,"dateShortInterest":1734048000,"sharesPercentSharesOut":0.1296,"heldPercentInsiders":0.010190001,"heldPercentInstitutions":0.3369,"shortRatio":0.35,"shortPercentOfFloat":0.1418,"impliedSharesOutstanding":280048992,"bookValue":0.64,"priceToBook":29.718752,"lastFiscalYearEnd":1703980800,"nextFiscalYearEnd":1735603200,"mostRecentQuarter":1727654400,"netIncomeToCommon":-60599000,"trailingEps":-0.37,"forwardEps":-0.33,"enterpriseToRevenue":301.663,"enterpriseToEbitda":-58.787,"52WeekChange":15.68421,"SandP52WeekChange":0.24749029,"exchange":"NCM","quoteType":"EQUITY","symbol":"RGTI","underlyingSymbol":"RGTI","shortName":"Rigetti Computing, Inc.","longName":"Rigetti Computing, Inc.","firstTradeDateEpochUtc":1619098200,"timeZoneFullName":"America/New_York","timeZoneShortName":"EST","uuid":"d5d039f8-2751-3be5-9d58-88da66d667ad","messageBoardId":"finmb_270093415","gmtOffSetMilliseconds":-18000000,"currentPrice":19.02,"targetHighPrice":5.5,"targetLowPrice":2,"targetMeanPrice":3.5,"targetMedianPrice":3.25,"recommendationKey":"none","numberOfAnalystOpinions":4,"totalCash":92580000,"totalCashPerShare":0.481,"ebitda":-61023000,"totalDebt":22490000,"quickRatio":4.612,"currentRatio":4.84,"totalRevenue":11892000,"debtToEquity":18.309,"revenuePerShare":0.073,"returnOnAssets":-0.26059,"returnOnEquity":-0.51458,"freeCashflow":-41299500,"operatingCashflow":-54504000,"revenueGrowth":-0.234,"grossMargins":0.60629004,"operatingMargins":-7.29437,"financialCurrency":"USD","trailingPegRatio":null}
