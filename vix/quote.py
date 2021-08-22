import pandas as pd
import btalib
import yfinance as yf

df_vix= yf.download("^VIX", start="2020-3-1",progress=False) 
df_spy=yf.download("SPY", start="2020-3-1",progress=False) 
df_qqq=yf.download("QQQ", start="2020-3-1",progress=False)
df_arkk=yf.download("ARKK", start="2020-3-1",progress=False)

df_spy["VIX Open"]=df_vix["Open"]
df_spy["VIX High"]=df_vix["High"]
df_spy["VIX Low"]=df_vix["Low"]
df_spy["VIX Close"]=df_vix["Close"]

df_qqq["VIX Open"]=df_vix["Open"]
df_qqq["VIX High"]=df_vix["High"]
df_qqq["VIX Low"]=df_vix["Low"]
df_qqq["VIX Close"]=df_vix["Close"]


df_arkk["VIX Open"]=df_vix["Open"]
df_arkk["VIX High"]=df_vix["High"]
df_arkk["VIX Low"]=df_vix["Low"]
df_arkk["VIX Close"]=df_vix["Close"]

df_vix=df_vix.rename(columns={"Close":"vixclose","Open":"vixopen","Low":"vixlow","High":"vixhigh"})

df_spy.reset_index(level=0, inplace=True)
df_spy.to_csv("vix/spy2021.csv",index = False)

df_vix.reset_index(level=0, inplace=True)
df_vix.to_csv("vix/vix2021.csv",index = False)

df_qqq.reset_index(level=0, inplace=True)
df_qqq.to_csv("vix/qqq2021.csv",index = False)

df_arkk.reset_index(level=0, inplace=True)
df_arkk.to_csv("vix/arkk2021.csv",index = False)
