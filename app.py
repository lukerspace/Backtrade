import os
from posixpath import abspath
import sys
from typing import Pattern
from flask import *
import csv
from flask_sqlalchemy import SQLAlchemy
import talib
import pandas as pd
from config import *
from pattern import *
from company import *

app=Flask(__name__)
db=SQLAlchemy(app)

class Company_Ark(db.Model):
    __tablename__="ark_company"
    id=db.Column(db.Integer,primary_key=True)
    company=db.Column(db.String(255))
    describe=db.Column(db.String(255))
    industry=db.Column(db.String(255))
    ceo=db.Column(db.String(255))
    def __init__(self,company,describe,industry,ceo):
        self.company=company
        self.describe=describe
        self.industry=industry
        self.ceo=ceo
    def __repr__(self):
        return "<Company %r>" %self.company

class Company_Spy(db.Model):
    __tablename__="spy_company"
    id=db.Column(db.Integer,primary_key=True)
    company=db.Column(db.String(255))
    describe=db.Column(db.String(255))
    industry=db.Column(db.String(255))
    ceo=db.Column(db.String(255))
    def __init__(self,company,describe,industry,ceo):
        self.company=company
        self.describe=describe
        self.industry=industry
        self.ceo=ceo
    def __repr__(self):
        return "<Company %r>" %self.company

class Company_Qqq(db.Model):
    __tablename__="qqq_company"
    id=db.Column(db.Integer,primary_key=True)
    company=db.Column(db.String(255))
    describe=db.Column(db.String(255))
    industry=db.Column(db.String(255))
    ceo=db.Column(db.String(255))
    def __init__(self,company,describe,industry,ceo):
        self.company=company
        self.describe=describe
        self.industry=industry
        self.ceo=ceo
    def __repr__(self):
        return "<Company %r>" %self.company


# CONFIG
app.secret_key="backtrader"
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True
app.config["JSON_SORT_KEYS"] = False
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:0000@localhost:3306/company"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"]={"pool_pre_ping":True}

# DB_INIT	



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




if __name__ == '__main__':

	app.run(host='127.0.0.1', port=3000)		



