import os
import sys
import requests
import dotenv
from dotenv import *
from json import *
import json

pre_path = os.path.abspath("../backtrade")
sys.path.append(pre_path)

import config
from config import *


load_dotenv()

class IEX:
    def __init__(self,token,symbol):
        # in production
        self.BASE_URL="https://cloud.iexapis.com/stable"
        # in sandbox
        # self.BASE_URL = 'https://sandbox.iexapis.com/v1'
        self.token=token
        self.symbol=symbol

    def get_company(self):
        url=f"{self.BASE_URL}/stock/{self.symbol}/company?token={self.token}"
        r=requests.get(url)
        return r.json()

    def get_dividends(self):
        url=f"{self.BASE_URL}/stock/{self.symbol}/dividends/2y?token={self.token}"
        r=requests.get(url)
        return r.json()

    def get_company_news(self, last=3):
        url = f"{self.BASE_URL}/stock/{self.symbol}/news/last/{last}?token={self.token}"
        r = requests.get(url)
        return r.json()


# ark=open('data/csv/ark.csv').readlines()
# symbols=[holding.strip() for holding in ark][1:]
# for symbol in symbols:
#     try:
#         stock=IEX(config.os.getenv("IEX_API"),symbol=symbol)

#         dividend_list=stock.get_dividends()
#         dividend_dict={}
#         for i in range(len(dividend_list)):
#             dividend_dict[i]=dividend_list[i]
#         with open(pre_path+'/info/dividends/ark/{}.json'.format(symbol), 'w') as f:
#             json.dump(dividend_dict, f)
#     except:
#         pass
# for k in stock_list:
#     try:    
#         stock=IEX(config.os.getenv("IEX_API"),symbol=k)
#         company_dict=stock.get_company()
#         with open(pre_path+'/info/company/ark/{}.json'.format(k), 'w') as f:
#             json.dump(company_dict, f)

#     except:
#         pass

holdings = open('data/csv/spy.csv').readlines()
symbols = [holding.split(',')[2].strip() for holding in holdings][1:]
for ticker in symbols:
    try:
        stock=IEX(config.os.getenv("IEX_API"),symbol=ticker)        
        dividend_list=stock.get_dividends()
        dividend_dict={}
        for i in range(len(dividend_list)):
            dividend_dict[i]=dividend_list[i]
        with open(pre_path+'/info/dividends/spy/{}.json'.format(ticker), 'w') as f:
            json.dump(dividend_dict, f)
    except:
        pass
    # try:
        # stock=IEX(config.os.getenv("IEX_API"),symbol=i)
        # company_dict=stock.get_company()
        # with open(pre_path+'/info/company/spy/{}.json'.format(i), 'w') as f:
            # json.dump(company_dict, f)
    # except:
        # pass










# print(stock_list)
# for i in stock_list:
#     stock=IEX(config.os.getenv("IEX_API"),symbol=i)
#     print(i)

    # dividend_list=stock.get_dividends()
    # dividend_dict={}
    # for i in range(len(dividend_list)):
    #     dividend_dict[i]=dividend_list[i]
    # with open(pre_path+'/info/dividends/{}.json'.format(symbol), 'w') as f:
    #     json.dump(dividend_dict, f)


    # company_dict=stock.get_company()
    # with open(pre_path+'/info/company/aapl.json', 'w') as f:
    #     json.dump(company_dict, f)


#TEST

# def get_stats(self):
#     url = f"{self.BASE_URL}/stock/{self.symbol}/advanced-stats?token={self.token}"
#     r = requests.get(url)
    
#     return r.json()

    
# def get_ownership(self):
#     url = f"{self.BASE_URL}/stock/{self.symbol}/institutional-ownership?token={self.token}"
#     print(url)
#     r = requests.get(url)
#     return r

# def get_quarterly(self):
#     url = f"{self.BASE_URL}/time-series/fundamentals/{self.symbol}/quarterly?last=4&token={self.token}"
#     print(url)
#     r = requests.get(url)
#     return r.json()

# def get_insider_transactions(self):
#     url = f"{self.BASE_URL}/stock/{self.symbol}/insider-transactions?token={self.token}"
#     print(url)
#     r = requests.get(url)
#     return r.json()