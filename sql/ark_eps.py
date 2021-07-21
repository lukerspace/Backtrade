import os
import sys
from btalib.indicators.rsi import rsi
from flask import *
from datetime import *
import pandas as pd
from getpass import *
import mysql.connector
from mysql.connector import pooling
pre_path = os.path.abspath("../backtrade/data/ark/")
sys.path.append(pre_path)

connection_pool = pooling.MySQLConnectionPool(
    host = "localhost",
    user = getpass("SERVER_USER: "),
    password = getpass("SERVER_PASSWORD:"),
    
    # password = "0000",
    # user = "root",

    database = "fund",
    charset = "utf8",
    auth_plugin='mysql_native_password' )
connection_obj=connection_pool.get_connection()

def sql_disconnect(connection_obj,table):
    if connection_obj.is_connected():
        table.close()
        connection_obj.close

def ark_eps_insert(**kwarg):
    if connection_obj.is_connected():
        # sql_cmd=f"""INSERT INTO arkeps( date , est , act ,ticker) VALUES ('{a}',{b},{c},'{d}')"""
        sql_cmd="select * from arkeps"
        print("SQL CONNECTED")
        table_cursor=connection_obj.cursor()
        table_cursor.execute(sql_cmd)
        print(table_cursor.fetchall())
        # sql_disconnect(connection_obj,table_cursor)
        # print("SQL sign out")

    else:
        print("SQL IS DISCONNECT")


ark_eps_insert()

ark=open('data/csv/ark.csv').readlines()
symbols=[holding.strip() for holding in ark][1:]
num=len(symbols)
less_than_yaer=[]
for symbol in symbols:
    try:
        df=pd.read_csv(f'../backtrade/data/ark/{symbol}_EPS.txt'.format(symbol))
        if len(df)<5:
            df["ticker"]=symbol
            less_than_yaer.append(symbol)
            
        else:
            df["ticker"]=symbol
            df=df.head()
            for index,row in df.iterrows():
                # print(index,row["ticker"],row["Date"],row["Estimate"],row["Actual"])
                print("---")
        # ticker=df.loc[:,"ticker"]
        # act=df.loc[:,"Actual"]
        # md=df.loc[:,"Date"]
        # est=df.loc[:,"Estimate"]
        # print(ticker,act)
        
    except:
        print("----")
        print(symbol+" FIND NO EPS DATA")




