import os 
import sys
import json
from config import *
import pandas as pd

from apps import db 
from apps.module import *
import datetime
from datetime import *

ark_path="info/eps/ark/"
ark_dir = os.listdir(ark_path)
data={}
eps={}
for ticker in ark_dir:
    df=pd.read_csv('info/eps/ark/{}'.format(ticker))
    df=df.head(4).reset_index()
    df["Date"]=pd.to_datetime(df["Date"],format='%Y/%m/%d')
    # print(df)
    symbol=ticker.split("_")[0]
    # print(symbol)
    if len(df)==0:
        pass
    else:
        time_first=df.loc[0:0,["Date"]].values
        time_second=df.loc[1:1,["Date"]].values
        time_third=df.loc[2:2,["Date"]].values
        time_fourth=df.loc[3:3,["Date"]].values
        
        est_first=df.loc[0:0,["Estimate"]]
        est_second=df.loc[1:1,["Estimate"]]
        est_third=df.loc[2:2,["Estimate"]]
        est_fourth=df.loc[3:3,["Estimate"]]
        
        act_first=df.loc[0:0,["Actual"]]
        act_second=df.loc[1:1,["Actual"]]
        act_third=df.loc[2:2,["Actual"]]
        act_fourth=df.loc[3:3,["Actual"]]

        ark_eps_insert=Eps_Ark(symbol,time_first,time_second,time_third,time_fourth)
        db.session.add(ark_eps_insert)
        db.session.commit()
        print(time_first)
    # print("=============================")
    # print(symbol)
    # print("---------")
    # print(time_first)
    # print("---------")
    # print(time_second)
    # print("---------")
    # print(time_fourth)
    # print(est_first)
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
