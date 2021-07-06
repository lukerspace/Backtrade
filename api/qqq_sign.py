import os
import sys
from btalib.indicators.rsi import rsi
from flask import *

from datetime import *
pre_path = os.path.abspath("../backfix")
sys.path.append(pre_path)

appQqqSign=Blueprint("appQqqSign",__name__)

@appQqqSign.route("/qqqsign")
def sign_data():
        with open(pre_path+"/qqqsignbuy.json") as f:
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

@appQqqSign.route("/qqqsignsell")
def sign_sell():
    with open(pre_path+"/qqqsignsell.json") as f:
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