import os 
import sys
from config import *
import pandas as pd
import datetime
from datetime import *
import json

from apps import db 
from apps.module import *

ark_path="info/dividends/ark/"
ark_dir = os.listdir(ark_path)
for ticker in ark_dir:
   with open('info/dividends/ark/{}'.format(ticker)) as f:
        line=f.read()
        div_json=json.loads(line)
        if len(div_json)>=3:
            
            symbol=ticker.split("_")[0]
            first=(div_json["0"])
            second=(div_json["1"])
            third=(div_json["2"])

            ark_div_insert=Div_Ark(symbol,first,second,third)
            db.session.add(ark_div_insert)
            db.session.commit()
        else:
            pass


spy_path="info/dividends/spy/"
spy_dir = os.listdir(spy_path)
for ticker in spy_dir:
   with open('info/dividends/spy/{}'.format(ticker)) as f:
        line=f.read()
        div_json=json.loads(line)
        if len(div_json)>=3:
            
            symbol=ticker.split("_")[0]
            first=(div_json["0"])
            second=(div_json["1"])
            third=(div_json["2"])

            spy_div_insert=Div_Spy(symbol,first,second,third)
            db.session.add(spy_div_insert)
            db.session.commit()
        else:
            pass


qqq_path="info/dividends/qqq/"
qqq_dir = os.listdir(qqq_path)
for ticker in qqq_dir:
   with open('info/dividends/qqq/{}'.format(ticker)) as f:
        line=f.read()
        div_json=json.loads(line)
        if len(div_json)>=3:
            
            symbol=ticker.split("_")[0]
            first=(div_json["0"])
            second=(div_json["1"])
            third=(div_json["2"])

            qqq_div_insert=Div_Qqq(symbol,first,second,third)
            db.session.add(qqq_div_insert)
            db.session.commit()
        else:
            pass

        