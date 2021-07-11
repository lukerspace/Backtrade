import talib
import yfinance as yf

data=yf.download("SPY",start="2021-01-01", end="2021-06-30")

morning_star=talib.CDLMORNINGSTAR(data["Open"],data["High"],data["Low"],data["Close"])
engulfing=talib.CDLENGULFING(data["Open"],data["High"],data["Low"],data["Close"])

data["Morning_star"]=morning_star
data["Engulfing"]=engulfing

# print(data[data["Morning_star"]!=0])
# 
print(data[data["Engulfing"]!=0])