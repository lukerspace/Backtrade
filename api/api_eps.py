import os
# from sql.sql_eps_ark import ark_eps_insert, ark_eps_select
import sys
from flask import *
from datetime import *
pre_path = os.path.abspath("../backtrade/sql")
sys.path.append(pre_path)
from sql_eps_ark import *

ark=open('data/csv/ark.csv').readlines()
symbols=[holding.strip() for holding in ark][1:]
# print(ark_eps_select("TSLA"))

appArkEps=Blueprint("appArkEps",__name__)

@appArkEps.route("/arkeps") 
def ark_eps():
    data={}
    for i in symbols:
        try:
            # if  len(ark_eps_select(i)["info"])==5:
            est_date=[ark_eps_select(i)["info"][0][0],ark_eps_select(i)["info"][1][0],\
                ark_eps_select(i)["info"][2][0],ark_eps_select(i)["info"][3][0],ark_eps_select(i)["info"][4][0]]

            est_eps=[ark_eps_select(i)["info"][0][1],ark_eps_select(i)["info"][1][1],\
                ark_eps_select(i)["info"][2][1],ark_eps_select(i)["info"][3][1],ark_eps_select(i)["info"][4][1]]

            act_eps=[ark_eps_select(i)["info"][0][2],ark_eps_select(i)["info"][1][2],\
                ark_eps_select(i)["info"][2][2],ark_eps_select(i)["info"][3][2],ark_eps_select(i)["info"][4][2]]
            eps={"date":est_date,"estimate":est_eps,"actual":act_eps}

            data[i]=eps
        except:
            eps={"error":"NO_EPS_DATA"}
            data[i]=eps
    return  jsonify({"data": data}) 

