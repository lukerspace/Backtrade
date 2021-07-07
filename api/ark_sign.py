import os
import sys
from btalib.indicators.rsi import rsi
from flask import *
from datetime import *
pre_path = os.path.abspath("../backfix/json")
sys.path.append(pre_path)


appArkSign=Blueprint("appArkSign",__name__)

@appArkSign.route("/arksign")
def sign_data():
        with open(pre_path+"/arksignbuy.json") as f:
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

@appArkSign.route("/arksignsell")
def sign_sell():
    with open(pre_path+"/arksignsell.json") as f:
            data=json.load(f)
    # raw=signsell[["Date","ticker"]].sort_values(by=["Date"],ascending=False).reset_index(drop=True)
    stock={}
    all_data={}
    for i in range(len(data)):
        try:
            stock={
                "date":datetime.fromtimestamp(int(data[str(i)]["Date"])/1000).strftime('%Y-%m-%d %H:%M:%S'),
                "ticker":data[str(i)]["ticker"]
            }
            all_data[i]=stock
        except:
            pass
    return  jsonify({"data": all_data}) 