import os 
import sys
from config import *
import pandas as pd
import datetime
from datetime import *

from apps import db 
from apps.module import *

ark_path="info/eps/ark/"
ark_dir = os.listdir(ark_path)
data={}

for ticker in ark_dir:
    df=pd.read_csv('info/eps/ark/{}'.format(ticker))
    df=df.head(3).reset_index()
    # df["Date"]=pd.to_datetime(df["Date"],format='%Y-%m-%d')
    symbol=ticker.split("_")[0]

    if len(df)!=3:
        pass
    else:
        time_first=df.at[0,"Date"]
        time_second=df.at[1,"Date"]
        time_third=df.at[2,"Date"]

        est_first=df.at[0,"Estimate"]
        est_second=df.at[1,"Estimate"]
        est_third=df.at[2,"Estimate"]
      
        act_first=df.at[0,"Actual"]
        act_second=df.at[1,"Actual"]
        act_third=df.at[2,"Actual"]

        eps_dic={"first":{"date":time_first,"estimate":est_first,"actual":act_first},"second":{"date":time_second,"estimate":est_second,"actual":act_second},\
            "third":{"date":time_third,"estimate":est_third,"actual":act_third}}
        data[symbol]=eps_dic

for ticker in ark_dir:
    symbol=ticker.split("_")[0]
    try:
        first=(data[symbol]["first"])
        second=(data[symbol]["second"])
        third=(data[symbol]["third"])
        ark_eps_insert=Eps_Ark(symbol,first,second,third)
        db.session.add(ark_eps_insert)
        db.session.commit()
    except:
        pass


spy_path="info/eps/spy/"
spy_dir = os.listdir(spy_path)
data={}

for ticker in spy_dir:
    df=pd.read_csv('info/eps/spy/{}'.format(ticker))
    df=df.head(3).reset_index()
    # df["Date"]=pd.to_datetime(df["Date"],format='%Y-%m-%d')
    symbol=ticker.split("_")[0]
    if len(df)!=3:
        pass
    else:
        time_first=df.at[0,"Date"]
        time_second=df.at[1,"Date"]
        time_third=df.at[2,"Date"]

        est_first=df.at[0,"Estimate"]
        est_second=df.at[1,"Estimate"]
        est_third=df.at[2,"Estimate"]
      
        act_first=df.at[0,"Actual"]
        act_second=df.at[1,"Actual"]
        act_third=df.at[2,"Actual"]

        eps_dic={"first":{"date":time_first,"estimate":est_first,"actual":act_first},"second":{"date":time_second,"estimate":est_second,"actual":act_second},\
            "third":{"date":time_third,"estimate":est_third,"actual":act_third}}
        data[symbol]=eps_dic

for ticker in spy_dir:
    symbol=ticker.split("_")[0]
    try:
        first=(data[symbol]["first"])
        second=(data[symbol]["second"])
        third=(data[symbol]["third"])
        spy_eps_insert=Eps_Spy(symbol,first,second,third)
        db.session.add(spy_eps_insert)
        db.session.commit()
    except:
        pass


qqq_path="info/eps/qqq/"
qqq_dir = os.listdir(qqq_path)
data={}

for ticker in qqq_dir:
    df=pd.read_csv('info/eps/qqq/{}'.format(ticker))
    df=df.head(3).reset_index()
    # df["Date"]=pd.to_datetime(df["Date"],format='%Y-%m-%d')
    symbol=ticker.split("_")[0]
    if len(df)!=3:
        pass
    else:
        time_first=df.at[0,"Date"]
        time_second=df.at[1,"Date"]
        time_third=df.at[2,"Date"]

        est_first=df.at[0,"Estimate"]
        est_second=df.at[1,"Estimate"]
        est_third=df.at[2,"Estimate"]
      
        act_first=df.at[0,"Actual"]
        act_second=df.at[1,"Actual"]
        act_third=df.at[2,"Actual"]

        eps_dic={"first":{"date":time_first,"estimate":est_first,"actual":act_first},"second":{"date":time_second,"estimate":est_second,"actual":act_second},\
            "third":{"date":time_third,"estimate":est_third,"actual":act_third}}
        data[symbol]=eps_dic

for ticker in qqq_dir:
    symbol=ticker.split("_")[0]
    try:
        first=(data[symbol]["first"])
        second=(data[symbol]["second"])
        third=(data[symbol]["third"])
        qqq_eps_insert=Eps_Qqq(symbol,first,second,third)
        db.session.add(qqq_eps_insert)
        db.session.commit()
    except:
        pass
        


 