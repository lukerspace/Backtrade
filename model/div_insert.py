import os 
import sys
from config import *
import pandas as pd
import datetime
from datetime import *
import json

from apps import db 
from apps.module import *

ark_path="info/dividends/ark/"
ark_dir = os.listdir(ark_path)

for ticker in ark_dir:
   with open('info/dividends/ark/{}'.format(ticker)) as f:
        line=f.read()
        symbol=ticker.split("_")[0]
        div_json=json.loads(line)
        if len(div_json)>=3:
            parse_list=list(div_json.values())[-3:]
            db_dict={}
            i=0
            for item in parse_list:
                i+=1
                new_dict={} 
                mili_time=item["paymentDate"]
                date_time=datetime.fromtimestamp(mili_time/1000.0)
                date_time=date_time.strftime("%Y/%m/%d")
                div=item["amount"]
                new_dict["date"]=date_time
                new_dict["amt"]=div
                # print(date_time)
                db_dict[i]=new_dict
            # print(symbol)
            # print(db_dict)
            ark_div_insert=Div_Ark(symbol,db_dict[1],db_dict[2],db_dict[3])
            db.session.add(ark_div_insert)
            db.session.commit()   
        else:
            pass


spy_path="info/dividends/spy/"
spy_dir = os.listdir(spy_path)
for ticker in spy_dir:
       with open('info/dividends/spy/{}'.format(ticker)) as f:
        line=f.read()
        symbol=ticker.split("_")[0]
        div_json=json.loads(line)
        if len(div_json)>=3:
            parse_list=list(div_json.values())[-3:]
            db_dict={}
            i=0
            for item in parse_list:
                i+=1
                new_dict={} 
                mili_time=item["paymentDate"]
                date_time=datetime.fromtimestamp(mili_time/1000.0)
                date_time=date_time.strftime("%Y/%m/%d")
                div=item["amount"]
                new_dict["date"]=date_time
                new_dict["amt"]=div
                # print(date_time)
                db_dict[i]=new_dict
            spy_div_insert=Div_Spy(symbol,db_dict[1],db_dict[2],db_dict[3])
            db.session.add(spy_div_insert)
            db.session.commit()   
        else:
            pass


qqq_path="info/dividends/qqq/"
qqq_dir = os.listdir(qqq_path)
for ticker in qqq_dir:
       with open('info/dividends/qqq/{}'.format(ticker)) as f:
        line=f.read()
        symbol=ticker.split("_")[0]
        div_json=json.loads(line)
        if len(div_json)>=3:
            parse_list=list(div_json.values())[-3:]
            db_dict={}
            i=0
            for item in parse_list:
                i+=1
                new_dict={} 
                mili_time=item["paymentDate"]
                date_time=datetime.fromtimestamp(mili_time/1000.0)
                date_time=date_time.strftime("%Y/%m/%d")
                div=item["amount"]
                new_dict["date"]=date_time
                new_dict["amt"]=div
                # print(date_time)
                db_dict[i]=new_dict
            qqq_div_insert=Div_Qqq(symbol,db_dict[1],db_dict[2],db_dict[3])
            db.session.add(qqq_div_insert)
            db.session.commit()   
        else:
            pass