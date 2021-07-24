import os
import sys
from flask import *
from datetime import *
pre_path = os.path.abspath("../backtrade/sql")
sys.path.append(pre_path)
from ark_eps import ark_eps_select

ark=open('data/csv/ark.csv').readlines()
symbols=[holding.strip() for holding in ark][1:]


appArkEps=Blueprint("appArkEps",__name__)

@appArkEps.route("/arkeps") 

def ark_eps():
    data={}
    for i in symbols:
        try:
            date_eps=(ark_eps_select(i)["date"])
            est_eps=(ark_eps_select(i)["estimate"])
            act_eps=(ark_eps_select(i)["actual"])
            eps={"date":date_eps,"estimate":est_eps,"actual":act_eps}
            data[i]=eps
        except:
            eps={"error":"NO_EPS_DATA"}
            data[i]=eps
    return  jsonify({"data": data}) 



