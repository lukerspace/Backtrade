import os
from flask import *
from apps import app
from config import *
from vix import *

import csv
from pattern import *
import talib
import pandas as pd
from apps.module import *
from apps import db



# PATH
abs_path=os.path.abspath(os.getcwd())
sys.path.append(abs_path)  # abs_path=abs_path+"\\apps\\"

# DB INITIATE
db.create_all()

# route
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
def spysnap():
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

@app.route("/qqqsnap")
def qqqsnap():
	pattern=request.args.get("pattern",None)
	stocks={}
	with open(abs_path+"\\data\\csv\\qqq.csv") as f:
		for row in csv.reader(f):
			stocks[row[2].replace(" ","")]={
				"company":row[2].replace(" ","")
			}
		# print(stocks)
	if "HoldingTicker" in stocks:
		del stocks["HoldingTicker"]
		# print(stocks)
	if pattern:
		file1=os.listdir(abs_path+"\\data\\qqq")
	
		for filename in file1:
			try:
				df=pd.read_csv(abs_path+"\\data\\qqq\\{}".format(filename))
				function_style=getattr(talib,pattern)
				symbol=filename.split(".")[0]
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



# # ESTABLISH TABLE & INSERT DATA

# from model.company_insert import *
# from model.eps_insert import *
# from model.rev_insert import *
# from model.div_insert import *



# FETCH THE DATA

# test=Rev_Spy.query.filter_by(ticker="AAPL").first()
# print(test)