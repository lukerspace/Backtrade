import os
from btalib.indicators.rsi import rsi
from flask import *
from datetime import *
import pandas as pd

abs_path=os.path.abspath(os.getcwd())



# module
def is_consolidate(df,symbol):
    # df["ticker"]=symbol
    monthly_close=df[-30:]
    monthly_volume=monthly_close["Volume"].mean()
    
    latest_close=df[-15:]
    latest_volume=latest_close["Volume"].mean()

    latest_max=latest_close["Close"].max()
    latest_min=latest_close["Close"].min()
    # if (latest_max/latest_min-1 < 0.025 ) & (latest_volume/monthly_volume>=1):
    #     return print(symbol,"is consolidated :" + str(round((latest_max/latest_min-1),4)), round(latest_volume/monthly_volume-1,3))
    if (latest_max/latest_min-1 <0.03 ) & (latest_volume/monthly_volume<1):
        # return print(symbol,"is consolidated & volume condensed:" + str(round((latest_max/latest_min-1),4)),round(latest_volume/monthly_volume-1,3))
        return True
    return  None


def is_breaking(df,symbol):
    try:
        last_close=df[-1:]["Close"].values[0]
        if is_consolidate(df[:-1],symbol):
            close=df[-16:-1]
            if last_close>close["Close"].max():
                return True
    except:
        return False



# # LOAD DATA

spy = open('data/csv/spy.csv').readlines()
spy_list = [holding.split(',')[2].strip() for holding in spy][1:]
# REGISTER
appSpyConsolidate=Blueprint("appSpyConsolidate",__name__)
# ROUTE
@appSpyConsolidate.route("/spyconsolidate") 
def spy_consolidate():
    breakout_dict={}
    consolidate_dict={}
    index1=0
    index2=0
    for symbol in spy_list:
        df=pd.read_csv(abs_path+"\\data\\spy\\"+"{}.txt".format(symbol))
        if (is_consolidate(df,symbol)):
            if (is_breaking(df,symbol)):
                index1+=1
                breakout_dict[int(index1)]=symbol
                # print("{} is breaking out".format(symbol))
            else:
                index2+=1
                consolidate_dict[int(index2)]=symbol
                # print("{} is consolidating".format(symbol))
    api_breakout={"breakout":breakout_dict,"consolidate":consolidate_dict}
    return  jsonify({"data": api_breakout}) 




# LOAD DATA
qqq = open('data/csv/qqq.csv').readlines()
qqq_list = [holding.split(',')[2].strip() for holding in qqq][1:]
# REGISTER
appQqqConsolidate=Blueprint("appQqqConsolidate",__name__)
# ROUTE
@appSpyConsolidate.route("/qqqconsolidate") 
def qqq_consolidate():
    breakout_dict={}
    consolidate_dict={}
    index1=0
    index2=0
    for symbol in qqq_list:
        df=pd.read_csv(abs_path+"\\data\\qqq\\"+"{}.txt".format(symbol))
        if (is_consolidate(df,symbol)):
            if (is_breaking(df,symbol)):
                index1+=1
                breakout_dict[int(index1)]=symbol
                # print("{} is breaking out".format(symbol))
            else:
                index2+=1
                consolidate_dict[int(index2)]=symbol
                # print("{} is consolidating".format(symbol))
    api_breakout={"breakout":breakout_dict,"consolidate":consolidate_dict}
    return  jsonify({"data": api_breakout}) 


# LOAD DATA

ark=open('data/csv/ark.csv').readlines()
ark_list=[holding.strip() for holding in ark][1:]
# REGISTER
appArkConsolidate=Blueprint("appArkConsolidate",__name__)
# ROUTE
@appArkConsolidate.route("/arkconsolidate") 
def ark_consolidate():
    breakout_dict={}
    consolidate_dict={}
    index1=0
    index2=0
    for symbol in ark_list:
        df=pd.read_csv(abs_path+"\\data\\ark\\"+"{}.txt".format(symbol))
        if (is_consolidate(df,symbol)):
            if (is_breaking(df,symbol)):
                index1+=1
                breakout_dict[int(index1)]=symbol
                # print("{} is breaking out".format(symbol))
            else:
                index2+=1
                consolidate_dict[int(index2)]=symbol
                # print("{} is consolidating".format(symbol))
    api_breakout={"breakout":breakout_dict,"consolidate":consolidate_dict}
    return  jsonify({"data": api_breakout}) 

