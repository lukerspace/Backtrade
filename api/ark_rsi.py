import os
import sys
from btalib.indicators.rsi import rsi
from flask import *

pre_path = os.path.abspath("../backtraded")
sys.path.append(pre_path)
from arkmodule import *

appArkRsi=Blueprint("appArkRsi",__name__)

@appArkRsi.route("/arkrsi")
def rsi_data():
    raw=rsibuy[["Date","ticker"]].sort_values(by=["Date"],ascending=False).reset_index(drop=True)
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
    return  jsonify({"data": data}) 
