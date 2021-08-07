import os
from posixpath import abspath
import sys
from typing import Pattern
from flask import *
import csv
import talib
import pandas as pd

abs_path=os.path.abspath(os.getcwd())
pre_path = os.path.abspath("../backtrade/py/")
sys.path.append(pre_path)
sys.path.append(abs_path)

from pattern import *

app=Flask(__name__)

# SIGNAL API
from api.api_signal import appQqqSign,appArkSign,appSpySign
# EPS API
from api.api_eps import appArkEps
# Consolidate
from api.api_consolidate import appSpyConsolidate,appArkConsolidate,appQqqConsolidate


# REGISTER
app.register_blueprint(appQqqSign, url_prefix='/api')
app.register_blueprint(appArkSign, url_prefix='/api')
app.register_blueprint(appSpySign, url_prefix='/api')


# REGITSTER EPS
app.register_blueprint(appArkEps, url_prefix='/api')


# REGISTER CONSOLIDATE
app.register_blueprint(appSpyConsolidate , url_prefix='/api')
app.register_blueprint(appArkConsolidate , url_prefix='/api')
app.register_blueprint(appQqqConsolidate , url_prefix='/api')


# CONFIG
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True
app.config["JSON_SORT_KEYS"] = False
app.secret_key="backtrader"


@app.route("/")
def menu():
	return render_template("menu.html")

@app.route("/qqq")
def index():
	return render_template("qqq.html")

@app.route("/ark")
def ark():
	return render_template("ark.html")

@app.route("/spy")
def spy():
	return render_template("spy.html")

@app.route("/squeeze")
def squeeze():
	return render_template("squeeze.html")

@app.route("/spysnap")
def snap():
	pattern=request.args.get("pattern",None)
	stocks={}
	with open(abs_path+"\\data\\csv\\spy.csv") as f:
		for row in csv.reader(f):
			stocks[row[2]]={
				"company":row[1]

			}
	if "Ticker" in stocks:
		del stocks["Ticker"]

	if pattern:
		file1=os.listdir(abs_path+"\\data\\spy")

		for filename in file1:
			df=pd.read_csv(abs_path+"\\data\\spy\\{}".format(filename))
			# df=df.head()
			function_style=getattr(talib,pattern)
			symbol=filename.split(".")[0]
			try:
				style=function_style(df["Open"],df["High"],df["Low"],df["Close"])
				last=style.tail(1).values[0]
				if last >0:
					stocks[symbol][pattern]="bullish"
				elif last<0:
					stocks[symbol][pattern]="bearlish"
				else:
					stocks[symbol][pattern]=None
					# print("{} trigger style : {}".format(filename,url))
			except:
				pass

	return render_template("snap.html",patterns=patterns ,stocks=stocks , current_style=pattern)


@app.route("/arksnap")
def arksnap():
	pattern=request.args.get("pattern",None)
	stocks={}
	with open(abs_path+"\\data\\csv\\ark.csv") as f:
		for row in csv.reader(f):
    			# print(row)
			stocks[row[0]]={
				"company":row[0]

			}
	if "Ticker" in stocks:
		del stocks["Ticker"]

	if pattern:
		file1=os.listdir(abs_path+"\\data\\ark")

		for filename in file1:
			df=pd.read_csv(abs_path+"\\data\\ark\\{}".format(filename))
			# df=df.head()
			function_style=getattr(talib,pattern)
			symbol=filename.split(".")[0]
			try:
				style=function_style(df["Open"],df["High"],df["Low"],df["Close"])
				last=style.tail(1).values[0]
				if last >0:
					stocks[symbol][pattern]="bullish"
				elif last<0:
					stocks[symbol][pattern]="bearlish"
				else:
					stocks[symbol][pattern]=None
					# print("{} trigger style : {}".format(filename,url))
			except:
				pass

	return render_template("snap.html",patterns=patterns ,stocks=stocks , current_style=pattern)




app.run(host='127.0.0.1', port=3000)		



