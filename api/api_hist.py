import os
import sys
from btalib.indicators.rsi import rsi
from flask import *
from datetime import *
pre_path = os.path.abspath("../backtrade/json")
sys.path.append(pre_path)


appArkHist=Blueprint("appArkHist",__name__)
appQqqHist=Blueprint("appQqqHist",__name__)
appSpyHist=Blueprint("appSpyHist",__name__)

@appArkHist.route("/arkhist")
def macd_data():
    with open(pre_path+"/arkhist.json") as f:
        data=json.load(f)
        # raw=signbuy[["Date","ticker"]].sort_values(by=["Date"],ascending=False).reset_index(drop=True)
        stock={}
        all_data={} 
        for i in range(len(data)):
        # for i in range(len(raw)+1):
            try:
                stock={
                    "date":datetime.fromtimestamp(int(data[str(i)]["Date"])/1000).strftime('%Y-%m-%d %H:%M:%S'),
                    "ticker":data[str(i)]["ticker"]
                }
                all_data[i]=stock
            except:
                pass
        return  jsonify({"data": all_data}) 


@appQqqHist.route("/qqqhist")
def macd_data():
    raw=histbuy[["Date","ticker"]].sort_values(by=["Date"],ascending=False).reset_index(drop=True)
    stock={}
    data={}
    for i in range(len(raw)+1):
        try:
            stock={
                "date":raw["Date"][i],
                "ticker":raw["ticker"][i]
            }
            data[i]=stock
        except:
            pass
    return jsonify({"data":data})


@appSpyHist.route("/spyhist")
def macd_data():
    raw=histbuy[["Date","ticker"]].sort_values(by=["Date"],ascending=False).reset_index(drop=True)
    stock={}
    data={}
    for i in range(len(raw)+1):
        try:
            stock={
                "date":raw["Date"][i],
                "ticker":raw["ticker"][i]
            }
            data[i]=stock
        except:
            pass
    return jsonify({"data":data})