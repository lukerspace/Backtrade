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
eps={}
for ticker in ark_dir:
    df=pd.read_csv('info/eps/ark/{}'.format(ticker))
    df=df.head(3).reset_index()
    df["Date"]=pd.to_datetime(df["Date"],format='%Y-%m-%d')
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
      
        ark_eps_insert=Eps_Ark(symbol,time_first,time_second,time_third,est_first,est_second,est_third,act_first,act_second,act_third)
        db.session.add(ark_eps_insert)
        db.session.commit()


spy_path="info/eps/spy/"
spy_dir = os.listdir(spy_path)
data={}
eps={}
for ticker in spy_dir:
    df=pd.read_csv('info/eps/spy/{}'.format(ticker))
    df=df.head(3).reset_index()
    df["Date"]=pd.to_datetime(df["Date"],format='%Y-%m-%d')
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
      
        spy_eps_insert=Eps_Spy(symbol,time_first,time_second,time_third,est_first,est_second,est_third,act_first,act_second,act_third)
        db.session.add(spy_eps_insert)
        db.session.commit()


qqq_path="info/eps/qqq/"
qqq_dir = os.listdir(qqq_path)
data={}
eps={}
for ticker in qqq_dir:
    df=pd.read_csv('info/eps/qqq/{}'.format(ticker))
    df=df.head(3).reset_index()
    df["Date"]=pd.to_datetime(df["Date"],format='%Y-%m-%d')
    symbol=ticker.split("_")[0]
    # print(df)
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
      
        qqq_eps_insert=Eps_Qqq(symbol,time_first,time_second,time_third,est_first,est_second,est_third,act_first,act_second,act_third)
        db.session.add(qqq_eps_insert)
        db.session.commit()



     