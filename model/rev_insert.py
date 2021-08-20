import os 
import sys
from config import *
import pandas as pd
import datetime
from datetime import *
import json



from apps import db 
from apps.module import *


# ark_path="info/revenue/ark/"
# ark_dir = os.listdir(ark_path)
# for ticker in ark_dir:
#    with open('info/revenue/ark/{}'.format(ticker)) as f:
#         line=f.read()
#         rev_json=json.loads(line)
#         if len(rev_json)!=0:
            
#             symbol=ticker.split("_")[0]
#             first=(rev_json["0"])
#             second=(rev_json["1"])
#             third=(rev_json["2"])
#             ark_rev_insert=Rev_Ark(symbol,first,second,third)
#             db.session.add(ark_rev_insert)
#             db.session.commit()
#         else:
#             pass


ark_path="info/revenue/spy/"
ark_dir = os.listdir(ark_path)
for ticker in ark_dir:
   with open('info/revenue/spy/{}'.format(ticker)) as f:
        line=f.read()
        rev_json=json.loads(line)
        if len(rev_json)!=0:
            
            symbol=ticker.split("_")[0]
            first=(rev_json["0"])
            second=(rev_json["1"])
            third=(rev_json["2"])
            spy_rev_insert=Rev_Spy(symbol,first,second,third)
            db.session.add(spy_rev_insert)
            db.session.commit()
        else:
            pass


ark_path="info/revenue/qqq/"
ark_dir = os.listdir(ark_path)
for ticker in ark_dir:
   with open('info/revenue/qqq/{}'.format(ticker)) as f:
        line=f.read()
        rev_json=json.loads(line)
        if len(rev_json)!=0:
            
            symbol=ticker.split("_")[0]
            first=(rev_json["0"])
            second=(rev_json["1"])
            third=(rev_json["2"])
            qqq_rev_insert=Rev_Qqq(symbol,first,second,third)
            db.session.add(qqq_rev_insert)
            db.session.commit()
        else:
            pass
