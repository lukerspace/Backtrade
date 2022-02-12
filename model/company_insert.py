import os 
import sys
import json
from config import *
from apps import db 
from apps.module import *

# abs_path=os.path.abspath(os.getcwd())
# sys.path.append(abs_path)

ark_path="info/company/ark/"
ark_dir = os.listdir(ark_path)

for ticker in ark_dir:
    try:
        with open("info/company/ark/{}".format(ticker)) as f:
            company_data=json.load(f)
            company_ticker=company_data["symbol"]
            company_name=company_data["companyName"]
            company_describe=company_data["description"][:3000]
            company_ind=company_data["industry"]
            company_web=company_data["website"]

            ark_company_insert=Company_Ark(company_ticker,company_name,company_describe,company_ind,company_web)
            db.session.add(ark_company_insert)
            db.session.commit()
    except:
        print(ticker,"ERROR")


spy_path="info/company/spy/"
spy_dir = os.listdir(spy_path)

for ticker in spy_dir:
#     # print(ticker)
    try:
        with open("info/company/spy/{}".format(ticker)) as f:
            company_data=json.load(f)
            company_ticker=company_data["symbol"]
            company_name=company_data["companyName"]
            company_describe=company_data["description"][:3000]
            company_ind=company_data["industry"]
            company_web=company_data["website"]
            # print(company_name,company_describe,company_ind,company_web)
            spy_company_insert=Company_Spy(company_ticker,company_name,company_describe,company_ind,company_web)
            db.session.add(spy_company_insert)
            db.session.commit()
    except:
        print(ticker,"ERROR")


qqq_path="info/company/qqq/"
qqq_dir = os.listdir(qqq_path)

for ticker in qqq_dir:
    try:
        with open("info/company/qqq/{}".format(ticker)) as f:
            company_data=json.load(f)
            # print(company_data)
            company_ticker=company_data["symbol"]
            company_name=company_data["companyName"]
            company_describe=company_data["description"][:3000]
            company_ind=company_data["industry"]
            company_web=company_data["website"]
            # print(company_name,company_describe,company_ind,company_web)
            spy_company_insert=Company_Qqq(company_ticker,company_name,company_describe,company_ind,company_web)
            db.session.add(spy_company_insert)
            db.session.commit()
    except:
        print(ticker,"ERROR")


