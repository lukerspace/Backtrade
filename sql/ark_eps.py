import os
import sys
from btalib.indicators.rsi import rsi
from flask import *
from datetime import *
import pandas as pd
from getpass import *
import mysql.connector
from mysql.connector import pooling
import numpy as np
pre_path = os.path.abspath("../backtrade/data/ark/")
sys.path.append(pre_path)


connection_pool = pooling.MySQLConnectionPool(
    host = "localhost",
    user = 'root',#getpass("SERVER_USER: "),
    password ='0000',#getpass("SERVER_PASSWORD:"),
    database = "fund",
    charset = "utf8",
    auth_plugin='mysql_native_password' )


def sql_disconnect(connection_obj,table):
    if connection_obj.is_connected():
        table.close()
        connection_obj.close


def syntax_str(**kwarg):
    insert_values_str=''
    for key in kwarg:
        if type(kwarg[key]==str):
            insert_values_str +=f"'{kwarg[key]}',"
    return (insert_values_str)


def syntax_int(**kwarg):
    insert_values_int=''
    for key in kwarg:
            insert_values_int +=f"{kwarg[key]},"
    return (insert_values_int[:-1])



def ark_eps_insert():
    ark=open('data/csv/ark.csv').readlines()
    symbols=[holding.strip() for holding in ark][1:]
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
                df["Actual"]=df["Actual"].replace(to_replace='None',value="null")
                df["Estimate"]=df["Estimate"].replace(to_replace='None',value="null")
                for index,row in df.iterrows():
                    tick=row["ticker"]
                    dt=str(row["Date"])
                    est=row["Estimate"]
                    act=row["Actual"]
                    val=syntax_str(ticker=tick,date=dt)+syntax_int(estimate=est,actual=act)
                    sql_cmd=f"""INSERT INTO arkeps(ticker,date,est,act) VALUES ({val})"""

                    connection_obj=connection_pool.get_connection()
                    if connection_obj.is_connected():
                        table_cursor=connection_obj.cursor()
                        table_cursor.execute(sql_cmd)
                        connection_obj.commit()
                        connection_obj.close()
                        print(sql_cmd)       
        except:
            print(symbol+" FIND NO EPS DATA")
    return print("ARK EPS UPDATE")



def ark_eps_select(symbols):
    connection_obj=connection_pool.get_connection()
    if connection_obj.is_connected():
        table_cursor=connection_obj.cursor()
        sql_cmd=f""" select date,est,act from arkeps where ticker ='{symbols}' order by date desc"""
        table_cursor.execute(sql_cmd)
        symbol_eps_data=table_cursor.fetchall()
        for i in range(len(symbol_eps_data)):
            eps_date=symbol_eps_data[i][0]
            eps_est=symbol_eps_data[i][1]
            eps_act=symbol_eps_data[i][2]
            # print(eps_date,eps_est,eps_act)
        connection_obj.close()
    return {"ticker":symbols,"date":eps_date,"estimate":eps_est,"actual":eps_act}
    # return print(eps_date,eps_est,eps_act)