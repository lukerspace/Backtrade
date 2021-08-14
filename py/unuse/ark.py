import btalib
import pandas as pd
import datetime 
from datetime import *
import numpy as np
import json
# date check

sdate=np.datetime64(date(2020,1,1))
ark=open('data/csv/ark.csv').readlines()
symbols=[holding.strip() for holding in ark][1:]
num=len(symbols)

# raw_data
def main():
    try:
        df = pd.read_csv('data/ark/'+ticker+'.txt', parse_dates=True, index_col='Date')
        sma = btalib.sma(df, period=5)
        rsi = btalib.rsi(df)
        macd = btalib.macd(df)

        df['sma'] = sma.df
        df['rsi'] = rsi.df
        df['macd'] = macd.df['macd']
        df['signal'] = macd.df['signal']
        df['histogram'] = macd.df['histogram']
        df=df.reset_index()
        return df
    except:
        pass


# module
# sign__buy


# # filter_signal
def signalbuy():
    df=main()
    signalbuy=pd.DataFrame()
    try:
        for i in range(len(df)):
            if df.loc[i,"macd"]<0:
                if df.loc[i+1.,"macd"]>0:
                    if df.loc[i+1,"macd"]>df.loc[i+1,"signal"]:
                        signalbuy=signalbuy.append(df.loc[i+1])
        return signalbuy
    except:
        pass

# to_json
signbuytojson=pd.DataFrame()
for i in range(num):
    ticker=symbols[i]
    df=signalbuy()
    try:
        df=df[1:]
        df["ticker"]=ticker
        signbuytojson=signbuytojson.append(df)
        signbuytojson=signbuytojson.sort_values(by=["Date"],ascending=False)
        signbuytojson=signbuytojson.drop_duplicates(subset=["ticker"],keep="first")
    except:
        pass

# load
signbuytojson=(signbuytojson.reset_index(drop=True))
signbuytojson.to_json("./json/arksignbuy.json",orient="index")


### sign__sell
### filter_sell

def signalsell():
    df=main()
    signalsell=pd.DataFrame()
    try:
        for i in range(len(df)):
            if df.loc[i,"macd"]<0:
                if df.loc[i-1.,"macd"]>0:
                    if df.loc[i,"macd"]<df.loc[i,"signal"]:
                        signalsell=signalsell.append(df.loc[i+1])
        return signalsell
    except:
        pass

#sell_tojosn
signselltojson=pd.DataFrame()
for i in range(num):
    ticker=(symbols[i])
    df=signalsell()
    try:
        df=df[-1:]
        df["ticker"]=ticker
        signselltojson=signselltojson.append(df)
        signselltojson=signselltojson.sort_values(by=["Date"],ascending=False)
        signselltojson=signselltojson.drop_duplicates(subset=["ticker"],keep="first")
    except:
        pass
# load   
signselltojson=(signselltojson.reset_index(drop=True))
signselltojson.to_json("./json/arksignsell.json",orient="index")


print("ark json loaded")


histable=pd.DataFrame()
hist_api={}
for i in range(num):
    try:
        date_index=[]
        ticker=(symbols[i])
        hist_data=main()
        hist_data=hist_data.sort_values(by=["Date"],ascending=False)
        hist_data=hist_data.reset_index(drop=True)
        hist_data["ticker"]=ticker
        hist_data=hist_data.loc[:5,["Date","histogram","ticker"]]
        # print(hist_data)
        histable=histable.append(hist_data).reset_index(drop=True)
    except:
        pass
    
histable.to_json("./json/arkhist.json",orient="index")    



# chart

from matplotlib import *
import yfinance as yf
import matplotlib.pyplot as plt 
from datetime import *


def chart(name):
    ma1="5"
    ma2="6"
    MA1=int(ma1)
    MA2=int(ma2)
    name=name
    df = yf.download(name,start="2021-1-1")
    df[ma1]=df["Adj Close"].rolling(MA1).mean()
    df[ma2]=df["Adj Close"].rolling(MA2).mean()
    df=df[["Adj Close",ma1,ma2]]
    df=df.dropna()
    buy=[]
    sell=[]
    for i in range(len(df)):
        if df[ma1].iloc[i]>df[ma2].iloc[i] and df[ma1].iloc[i-1]<df[ma2].iloc[i-1]:
            buy.append(i)
        elif df[ma1].iloc[i]<df[ma2].iloc[i] and df[ma1].iloc[i-1]>df[ma2].iloc[i-1]:
            sell.append(i)
    plt.style.use("dark_background")
    plt.figure(figsize=(10,5))
    plt.grid(linestyle='-', linewidth=0.1,data=(10,10))
    plt.plot(df['Adj Close'],label="stock price",c="orange",alpha=1)
    plt.plot(df[ma1],label="MA"+ma1,c="white",alpha=1)
    plt.plot(df[ma2],label="MA"+ma2,c="skyblue",alpha=0.5)
    plt.scatter(df.iloc[buy].index,df.iloc[buy]["Adj Close"],marker="^",color="green",s=40,zorder=10)
    plt.scatter(df.iloc[sell].index,df.iloc[sell]["Adj Close"],marker="v",color="red",s=40,zorder=10)
    plt.legend(fontsize=8)
    
    
    return plt.savefig("./static/png/"+name+".png")



ark=open('data/csv/ark.csv').readlines()
symbols=[holding.strip() for holding in ark][1:]
for i in symbols:
    try:
        chart(i)
    except:
        pass
print("img done")