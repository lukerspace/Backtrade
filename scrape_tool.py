import numpy as np
import pandas as pd
import btalib
import yfinance as yf
import matplotlib.pyplot as plt
import requests
import config
from datetime import *

class IndexScraper:
    sma_period = 5

    def __init__(self):
        self.index_ticker = None
        self.tickers = None
        self.path = None

    def set_index_ticker(self, index_ticker):
        self.index_ticker = index_ticker.lower()
        index_csv = open('data/csv/' + self.index_ticker + '.csv')
        if self.index_ticker == 'ark':
            self.tickers = [holding.strip() for holding in index_csv.readlines()][1:]
        else:
            self.tickers = [holding.split(',')[2].strip() for holding in index_csv.readlines()][1:]
        self.path = 'data/' + index_ticker + '/'

    def start(self):
        if not self.index_ticker:
            print('Please set index')
            return

        print('Start scraping ' + self.index_ticker)
        print('Found %d tickers' % len(self.tickers))

        self.quote()

        buy_signals_df = pd.DataFrame()
        sell_signals_df = pd.DataFrame()
        history_df = pd.DataFrame()

        for ticker in self.tickers:
            try:
                raw_df = self.read_raw_data(ticker)
                buy_signal = self.generate_buy_signal(raw_df)
                sell_signal = self.generate_sell_signal(raw_df)
                self.generate_chart(ticker)

                buy_signal = buy_signal[1:]
                buy_signal['ticker'] = ticker
                buy_signals_df = buy_signals_df.append(buy_signal)

                sell_signal = sell_signal[-1:]
                sell_signal['ticker'] = ticker
                sell_signals_df = sell_signals_df.append(sell_signal)

                raw_df.sort_values(by=["Date"],ascending=False, inplace=True)
                raw_df.reset_index(drop=True, inplace=True)
                raw_df["ticker"] = ticker
                raw_df = raw_df.loc[:5, ["Date", "histogram", "ticker"]]
                history_df = history_df.append(raw_df)

                print('Finish ' + ticker)
            except:
                print('Skip ' + ticker)

        buy_signals_df.sort_values(by=["Date"], ascending=False, inplace=True)
        buy_signals_df.drop_duplicates(subset=["ticker"], keep="first", inplace=True)
        buy_signals_df.reset_index(drop=True, inplace=True)
        buy_signals_df.to_json('./json/' + self.index_ticker + 'signbuy.json',
                               orient="index")

        sell_signals_df.sort_values(by=["Date"], ascending=False, inplace=True)
        sell_signals_df.drop_duplicates(subset=["ticker"], keep="first", inplace=True)
        sell_signals_df.reset_index(drop=True, inplace=True)
        sell_signals_df.to_json('./json/' + self.index_ticker + 'signsell.json',
                                orient="index")

        history_df.reset_index(drop=True, inplace=True)
        history_df.to_json('./json/' + self.index_ticker + 'hist.json',
                           orient="index")

        print('Finish scraping')

    def quote(self):
        tickers_str = ",".join(self.tickers)

        num = len(self.tickers)
        start = 0
        end = 0
        while start < num:
            end = min(end + config.API_MAX_LENGTH, num)
            day_bars_url = '{}/day?symbols={}&limit=300'.format(config.BARS_URL, tickers_str[start:end])
            start = end

            r = requests.get(day_bars_url, headers=config.HEADERS)
            data = r.json()

            for symbol in data:
                filename = 'data/' + self.index_ticker + '/{}.txt'.format(symbol)
                f = open(filename, 'w+')
                f.write('Date,Open,High,Low,Close,Volume,OpenInterest\n')
                # print(data[symbol])

                for bar in data[symbol]:
                    t = datetime.fromtimestamp(bar['t'])
                    day = t.strftime('%Y-%m-%d')

                    line = '{},{},{},{},{},{},{}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
                    f.write(line)

        print(self.index_ticker + ' is loaded')

    def read_raw_data(self, ticker):
        print(self.path + ticker + '.txt')
        df = pd.read_csv(self.path + ticker + '.txt',
                         parse_dates=True,
                         index_col='Date')
        sma = btalib.sma(df, period=self.sma_period)
        rsi = btalib.rsi(df)
        macd = btalib.macd(df)
        df['sma'] = sma.df
        df['rsi'] = rsi.df
        df['macd'] = macd.df['macd']
        df['signal'] = macd.df['signal']
        df['histogram'] = macd.df['histogram']
        df = df.reset_index()
        return df

    def generate_buy_signal(self, df):
        buy_signal = pd.DataFrame()

        for i in range(len(df) - 1):
            if df.loc[i, "macd"] < 0:
                if df.loc[i + 1., "macd"] > 0:
                    if df.loc[i + 1, "macd"] > df.loc[i + 1, "signal"]:
                        buy_signal = buy_signal.append(df.loc[i + 1])

        return buy_signal

    def generate_sell_signal(self, df):
        sell_signal = pd.DataFrame()
        for i in range(1, len(df) - 1):
            if df.loc[i, "macd"] < 0:
                if df.loc[i - 1., "macd"] > 0:
                    if df.loc[i, "macd"] < df.loc[i, "signal"]:
                        sell_signal = sell_signal.append(df.loc[i + 1])
        return sell_signal

    def generate_chart(self, ticker):
        ma1 = "5"
        ma2 = "6"
        MA1 = int(ma1)
        MA2 = int(ma2)
        name = ticker
        df = yf.download(name, start="2021-1-1",progress=False)
        df[ma1] = df["Adj Close"].rolling(MA1).mean()
        df[ma2] = df["Adj Close"].rolling(MA2).mean()
        df = df[["Adj Close", ma1, ma2]]
        df = df.dropna()
        buy = []
        sell = []
        for i in range(len(df)):
            if df[ma1].iloc[i] > df[ma2].iloc[i] and df[ma1].iloc[i - 1] < df[ma2].iloc[i - 1]:
                buy.append(i)
            elif df[ma1].iloc[i] < df[ma2].iloc[i] and df[ma1].iloc[i - 1] > df[ma2].iloc[i - 1]:
                sell.append(i)

        plt.style.use("dark_background")
        plt.figure(figsize=(10, 5))
        plt.grid(linestyle='-', linewidth=0.1, data=(10, 10))
        plt.plot(df['Adj Close'], label="stock price", c="orange", alpha=1)
        plt.plot(df[ma1], label="MA" + ma1, c="white", alpha=1)
        plt.plot(df[ma2], label="MA" + ma2, c="skyblue", alpha=0.5)
        plt.scatter(df.iloc[buy].index, df.iloc[buy]["Adj Close"], marker="^", color="green", s=40, zorder=10)
        plt.scatter(df.iloc[sell].index, df.iloc[sell]["Adj Close"], marker="v", color="red", s=40, zorder=10)
        plt.legend(fontsize=8)
        plt.savefig("./static/png/" + name + ".png")
        plt.close('all')