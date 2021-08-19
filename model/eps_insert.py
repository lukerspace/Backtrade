import os 
import sys
import json
from config import *
import pandas as pd

# from apps import db 
# from apps.module import *


ark_path="info/eps/ark/"
ark_dir = os.listdir(ark_path)
data={}
eps={}
for ticker in ark_dir:
    df=pd.read_csv('info/eps/ark/{}'.format(ticker))
    df=df.head(4).reset_index()
    # print(df)
    symbol=ticker.split("_")[0]
    # print(symbol)
    a=df.loc[:,["Date"]]
    print(a)
    # with open("info/eps/ark/{}".format(ticker)) as f:
            # for i in f.readline():
#                 dic[ticker]=i
                      
# #             company_data=json.load(f)
#             company_ticker=company_data["symbol"]
#             company_name=company_data["companyName"]
#             company_describe=company_data["description"][:3000]
#             company_ind=company_data["industry"]
#             company_web=company_data["website"]
#             # print(company_name,company_describe,company_ind,company_web)
#             ark_company_insert=Company_Ark(company_ticker,company_name,company_describe,company_ind,company_web)
#             db.session.add(ark_company_insert)
#             db.session.commit()
#     except:
#         print(ticker,"ERROR")


# spy_path="info/company/spy/"
# spy_dir = os.listdir(spy_path)

# for ticker in spy_dir:
# #     # print(ticker)
#     try:
#         with open("info/company/spy/{}".format(ticker)) as f:
#             company_data=json.load(f)
#             company_ticker=company_data["symbol"]
#             company_name=company_data["companyName"]
#             company_describe=company_data["description"][:3000]
#             company_ind=company_data["industry"]
#             company_web=company_data["website"]
#             # print(company_name,company_describe,company_ind,company_web)
#             spy_company_insert=Company_Spy(company_ticker,company_name,company_describe,company_ind,company_web)
#             db.session.add(spy_company_insert)
#             db.session.commit()
#     except:
#         print(ticker,"ERROR")


# qqq_path="info/company/qqq/"
# qqq_dir = os.listdir(qqq_path)

# for ticker in qqq_dir:
#     try:
#         with open("info/company/qqq/{}".format(ticker)) as f:
#             company_data=json.load(f)
#             # print(company_data)
#             company_ticker=company_data["symbol"]
#             company_name=company_data["companyName"]
#             company_describe=company_data["description"][:3000]
#             company_ind=company_data["industry"]
#             company_web=company_data["website"]
#             # print(company_name,company_describe,company_ind,company_web)
#             spy_company_insert=Company_Qqq(company_ticker,company_name,company_describe,company_ind,company_web)
#             db.session.add(spy_company_insert)
#             db.session.commit()
#     except:
#         print(ticker,"ERROR")
