import os
import sys
import requests
import dotenv
from dotenv import *
from json import *
import json

pre_path = os.path.abspath("../backtrade")
sys.path.append(pre_path)
print(sys.path)

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



stock=IEX(config.os.getenv("IEX_API"),symbol="AAPL")

dividend_list=stock.get_dividends()
dividend_dict={}
for i in range(len(dividend_list)):
    dividend_dict[i]=dividend_list[i]
with open(pre_path+'/info/dividends/aapl.json', 'w') as f:
    json.dump(dividend_dict, f)


company_dict=stock.get_company()
with open(pre_path+'/info/company/aapl.json', 'w') as f:
    json.dump(company_dict, f)



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