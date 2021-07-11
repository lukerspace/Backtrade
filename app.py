import os
import sys
from typing import Pattern
from flask import *
from pattern import *
import pandas as pd
pre_path = os.path.abspath("../backtraded")
sys.path.append(pre_path)
app=Flask(__name__)
import talib
import csv

from api.qqq_sign import appQqqSign
# from api.qqq_hist import appQqqHist

from api.ark_sign import appArkSign
from api.ark_hist import appArkHist

from api.spy_sign import appSpySign
# from api.spy_hist import appSpyHist

app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True
app.config["JSON_SORT_KEYS"] = False
app.secret_key="backtrader"

app.register_blueprint(appQqqSign, url_prefix='/api')
# app.register_blueprint(appQqqHist, url_prefix='/api')

app.register_blueprint(appArkSign, url_prefix='/api')
app.register_blueprint(appArkHist, url_prefix='/api')

app.register_blueprint(appSpySign, url_prefix='/api')
# app.register_blueprint(appSpyHist, url_prefix='/api')

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


@app.route("/snap")
def snap():
	pattern=request.args.get("pattern",None)
	stocks={}
	with open("data/csv/spy.csv") as f:
		for row in csv.reader(f):
			stocks[row[2]]={
				"company":row[1]

			}
	if "Ticker" in stocks:
		del stocks["Ticker"]

	if pattern:
		file1=os.listdir("data/spy/")

		for filename in file1:
			df=pd.read_csv("data/spy/{}".format(filename))
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
			# print(df)
		# ticker.add([i for i in file3])
		# print(len(list(ticker2)))
		# print(len(list(ticker)))
		# print(file1)
		# print(len(file1))
		# print(len(file2))
		# print(len(file3))

	return render_template("snap.html",patterns=patterns,stocks=stocks , current_style=pattern)

# app.run(port=3000)

app.run(host='0.0.0.0', port=3000)		



