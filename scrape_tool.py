import numpy as np
import pandas as pd
import btalib
import yfinance as yf

import matplotlib
matplotlib.use('Agg') #
from matplotlib import pyplot as plt #
# import matplotlib.pyplot as plt

import requests
import config
from datetime import *
from tqdm.auto import tqdm
import yahoo_fin.stock_info as si
import re

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

        self.quote_all()
        
        
        # markdown
        
        buy_signals_df = pd.DataFrame()
        sell_signals_df = pd.DataFrame()
        history_df = pd.DataFrame()
        skip_list = []
        
        for ticker in tqdm(self.tickers, leave=False):
            try:
                raw_df = self.read_raw_data(ticker)
        
                if not len(raw_df)>0:
                    skip_list.append(ticker)
                    continue
        
                buy_signal = self.generate_buy_signal(raw_df)
                sell_signal = self.generate_sell_signal(raw_df)
                self.generate_chart(ticker)
        
                buy_signal = buy_signal[1:]
                buy_signal['ticker'] = ticker
                buy_signals_df = buy_signals_df.append(buy_signal)
        
                sell_signal = sell_signal[-1:]
                sell_signal['ticker'] = ticker
                sell_signals_df = sell_signals_df.append(sell_signal)
        
                raw_df.sort_values(by=["Date"], ascending=False, inplace=True)
                raw_df.reset_index(drop=True, inplace=True)
                raw_df["ticker"] = ticker
                raw_df = raw_df.loc[:5, ["Date", "histogram", "ticker"]]
                history_df = history_df.append(raw_df)
        
            except:
                skip_list.append(ticker)
        
        print('Skipped %d ticker: %s' % (len(skip_list), ", ".join(skip_list)))
        
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
        
        print('Finish scraping ' + self.index_ticker)

    def quote_all(self, eps=False, dividend=False, revenue=False, holder=False):
        num = len(self.tickers)
        start = 0
        end = 0
        
        while start < num:
            end = min(end + config.API_MAX_LENGTH, num)
            self.get_daily_bars(self.tickers[start:end], self.path)
            start = end

        if not eps and not dividend and not revenue and not holder:
            return

        for ticker in self.tickers:
            if eps:
                filename = 'info/eps/' + self.index_ticker + '/{}_EPS.txt'.format(ticker)
                self.get_earning(ticker, filename)

            if dividend:
                filename = 'info/dividends/' + self.index_ticker + '/{}_DIV.txt'.format(ticker)
                self.get_dividends(ticker, filename)

            if revenue:
                filename = 'info/revenue/' + self.index_ticker + '/{}_REV.txt'.format(ticker)
                self.get_revenue(ticker, filename)

            if holder:
                filename = 'info/holder' + self.index_ticker + '/{}_HOLD.txt'.format(ticker)
                self.get_holder(ticker, filename)

        print(self.index_ticker.upper() + ' IS FINISHED')

    @staticmethod
    def get_daily_bars(tickers, directory):
        tickers_str = ",".join(tickers)
        day_bars_url = '{}/day?symbols={}&limit=300'.format(config.BARS_URL, tickers_str)
        r = requests.get(day_bars_url, headers=config.HEADERS)
        data = r.json()

        for symbol in data:
            file_path = directory + '/{}.txt'.format(symbol)
            f = open(file_path, 'w')
            f.write('Date,Open,High,Low,Close,Volume,OpenInterest\n')
            for bar in data[symbol]:
                t = datetime.fromtimestamp(bar['t'])
                day = t.strftime('%Y-%m-%d')

                line = '{},{},{},{},{},{},{}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
                f.write(line)
            f.close()
            print('{} daily_quote is updated'.format(symbol))

    @staticmethod
    def get_earning(ticker, file_path):
        f = open(file_path, 'w')
        f.write('Date,Estimate,Actual\n')

        try:
            earnings = si.get_earnings_history(ticker)

            for eps in earnings:
                t = datetime.strptime(eps['startdatetime'], "%Y-%m-%dT%H:%M:%S.%fZ")
                day = t.strftime('%Y-%m-%d')

                line = '{},{},{}\n'.format(day, eps['epsestimate'], eps['epsactual'])
                f.write(line)

            print('{} eps is updated'.format(ticker))
        except:
            print('{} eps is failed'.format(ticker))

        f.close()

    @staticmethod
    def get_dividends(ticker, file_path):

        # if path.exists(filename):
        #     record = pd.read_csv(file_path)
        #     if len(record) > 0 and 'Date' in record.columns:
        #         recent_date = datetime.strptime(record['Date'][len(record) - 1], "%Y-%m-%d")
        #         if recent_date == datetime.today():
        #             return False
        try:
            dividends = si.get_dividends(ticker)
            dividends.reset_index(inplace=True)
            dividends.rename(columns={'index': 'paymentDate', 'dividend': 'amount'}, inplace=True)
            dividends.drop(['ticker'], inplace=True, axis=1)
            dividends.to_json(file_path, orient='index')
            print('{} dividend is updated'.format(ticker))

        except:
            empty_dict = {"index": [], 'paymentDate': [], 'amount': []}
            empty_df = pd.DataFrame.from_dict(empty_dict)
            empty_df.to_json(file_path, orient='index')
            print('{} dividend is failed'.format(ticker))

    @staticmethod
    def get_revenue(ticker, file_path):
        try:
            earnings = si.get_earnings_history(ticker)
            count = 0
            analyst_dict = {'date': [], 'actualRevenue': [None],
                            'estimateRevenue': [None] * 5}
            for eps in earnings:
                if eps['epsestimate'] is None:
                    continue

                if count > 4:
                    break

                t = datetime.strptime(eps['startdatetime'], "%Y-%m-%dT%H:%M:%S.%fZ")
                day = t.strftime('%Y-%m-%d')
                analyst_dict['date'].append(day)
                count += 1

            revenue = si.get_earnings(ticker)['quarterly_revenue_earnings']
            revenue = list(revenue['revenue'])
            revenue.reverse()
            analyst_dict['actualRevenue'].extend(revenue)

            for exchange in ['NASDAQ', 'NYSE']:
                try:
                    analyst_dict['estimateRevenue'] = get_estimate_revenue(exchange, ticker)
                    break
                except:
                    pass

            revenue_exp = si.get_analysts_info(ticker)['Revenue Estimate']
            s = revenue_exp[revenue_exp.columns[1]][1]
            try:
                num = float(s[:-1])
                if s[-1].lower() == 'b':
                    num = num * 1000000000
                elif s[-1].lower() == 'm':
                    num = num * 1000000
                elif s[-1].lower() == 't':
                    num = num * 1000000000000
            except:
                num = None
            analyst_dict['estimateRevenue'][0] = num
            analyst_df = pd.DataFrame.from_dict(analyst_dict)
            analyst_df.to_json(file_path, orient='index')
            print('{} revenue is updated'.format(ticker))
        except:
            empty_dict = {'date': [], 'actualRevenue': [], 'estimateRevenue': []}
            empty_df = pd.DataFrame.from_dict(empty_dict)
            empty_df.to_json(file_path, orient='index')
            print('{} revenue is failed'.format(ticker))

    @staticmethod
    def get_company_info(ticker, file_path):
        pass

    def get_holder(ticker, file_path):
        # if path.exists(file_path):
        #     return
        try:
            holders = si.get_holders(ticker)
            holders['Direct Holders (Forms 3 and 4)'].to_csv(file_path, index=False)
            print('{} holder is updated'.format(ticker))
        except:
            empty_dict = {'Holder': [], 'Shares': [], 'Date': [],
                          'Reported': [], '% Out': [], 'Value': []}
            empty_df = pd.DataFrame.from_dict(empty_dict)
            print('{} holder is failed'.format(ticker))

        return True

    def read_raw_data(self, ticker):
        # print(self.path + ticker + '.txt')
        df = pd.read_csv(self.path + ticker + '.txt',
                         parse_dates=True,
                         index_col='Date')
        if len(df) == 0:
            return None
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
        plt.savefig("./apps/static/png/" + name + ".png")
        plt.close('all')


def get_estimate_revenue(exchange, symbol):
    output = []
    url = 'https://www.marketbeat.com/stocks/' + exchange + '/' + symbol + '/earnings/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    content = resp.content.decode(encoding='utf-8', errors='strict')
    df = pd.read_html(content)[1]
    df = df.head(5)
    for s in df['Revenue Estimate']:
        if pd.isna(s):
            output.append(None)
            continue
        num = float(re.sub(r'[^\d.]', "", s))
        word = s.split(" ")[1]
        if word[0].lower() == 'b':
            num = num * 1000000000
        elif word[0].lower() == 'm':
            num = num * 1000000
        elif word[0].lower() == 't':
            num = num * 1000000000000
        output.append(num)

    return output