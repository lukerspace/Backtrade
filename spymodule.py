import btalib
import pandas as pd
import datetime 
from datetime import *
import numpy as np

# date check
sdate=np.datetime64(date(2020,1,1))

# date check
holdings = open('data/csv/spy.csv').readlines()
symbols = [holding.split(',')[2].strip() for holding in holdings][1:]
num=len(symbols)



# raw_data
def main():
    try:
        df = pd.read_csv('data/spy/'+ticker+'.txt', parse_dates=True, index_col='Date')
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

# filter_signal
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
signbuytojson.to_json("spysignbuy.json",orient="index")


#sign__sell
# filter_sell

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
signselltojson.to_json("spysignsell.json",orient="index")

print("spy json loaded")















# def main():
#     try:
#         df = pd.read_csv('data/spy/'+ticker+'.txt', parse_dates=True, index_col='Date')
#         sma = btalib.sma(df, period=5)
#         rsi = btalib.rsi(df)
#         macd = btalib.macd(df)

#         df['sma'] = sma.df
#         df['rsi'] = rsi.df
#         df['macd'] = macd.df['macd']
#         df['signal'] = macd.df['signal']
#         df['histogram'] = macd.df['histogram']
#         df=df.reset_index()
#         return df
#     except:
#         pass

# # rsi_module
# def rsi_sell():
#     df=main()
#     try:
#         overbought_days = df[df['rsi'] > 70].reset_index()
#         sellday=pd.DataFrame()
#         for i in overbought_days["Date"]:
#             if i > sdate:
#                 over_b=overbought_days[overbought_days["Date"].isin([i])]
#                 sellday=sellday.append(over_b)
#         return sellday
#     except:
#         pass

# def rsi_buy():
#     df=main()
#     try:
#         oversold_days = df[df['rsi'] < 30].reset_index()
#         buyday=pd.DataFrame()
#         for i in oversold_days["Date"]:
#             if i > sdate:
#                 over_s=oversold_days[oversold_days["Date"].isin([i])]
#                 buyday=buyday.append(over_s)
#         return buyday
#     except:
#         pass

# # macd module
# def macdbuy():
#     df=main()
#     macdbuy=pd.DataFrame()
#     try:
#         for i in range(len(df)):
#             if df.loc[i,"histogram"]<0:
#                 if df.loc[i+1,"histogram"]>0:
#                     macdbuy=macdbuy.append(df.loc[i+1])
#         return macdbuy
#     except:
#         pass

# def macdsell():
#     df=main()
#     macdsell=pd.DataFrame()
#     try:
#         for i in range(len(df)):
#             if df.loc[i,"histogram"]<0:
#                 if df.loc[i+1,"histogram"]>0:
#                     macdsell=macdsell.append(df.loc[i+1])
#         return macdsell
#     except:
#         pass

# # signal module
# def signalbuy():
#     df=main()
#     signalbuy=pd.DataFrame()
#     try:
#         for i in range(len(df)):
#             if df.loc[i,"macd"]<0:
#                 if df.loc[i+1.,"macd"]>0:
#                     if df.loc[i+1,"macd"]>df.loc[i+1,"signal"]:
#                         signalbuy=signalbuy.append(df.loc[i+1])
#         return signalbuy
#     except:
#         pass

# def signalsell():
#     df=main()
#     signalsell=pd.DataFrame()
#     try:
#         for i in range(len(df)):
#             if df.loc[i,"macd"]<0:
#                 if df.loc[i-1.,"macd"]>0:
#                     if df.loc[i,"macd"]<df.loc[i,"signal"]:
#                         signalsell=signalsell.append(df.loc[i+1])
#         return signalsell
#     except:
#         pass

# #initiate_spy
# holdings = open('data/csv/spy.csv').readlines()
# symbols = [holding.split(',')[2].strip() for holding in holdings][1:]

# # print(symbols)
# num=len(symbols)

# # sign      
# signbuy=pd.DataFrame()
# for i in range(num):
#     ticker=symbols[i]
#     df=signalbuy()
#     try:
#         df=df[-1:]
#         df["ticker"]=ticker
#         signbuy=signbuy.append(df)
#     except:
#         pass
# # sign    
# signsell=pd.DataFrame()
# for i in range(num):
#     ticker=(symbols[i])
#     df=signalsell()
#     try:
#         df=df[-1:]
#         df["ticker"]=ticker
#         signsell=signsell.append(df)
#     except:
#         pass

# # rsi
# rsibuy=pd.DataFrame()
# for i in range(num):
#     ticker=(symbols[i])
#     df=rsi_buy()
#     try:
#         df=df[-1:]
#         df["ticker"]=ticker
#         rsibuy=rsibuy.append(df)
#     except:
#         pass

# # # rsi
# rsisell=pd.DataFrame()
# for i in range(num):
#     ticker=(symbols[i])
#     df=rsi_sell()
#     try:
#         df=df[-1:]
#         df["ticker"]=ticker
#         rsisell=rsisell.append(df)
#     except:
#         pass

# # macd
# histbuy=pd.DataFrame()
# for i in range(num):
#     ticker=(symbols[i])
#     df=macdbuy()
#     try:
#         df=df[-1:]
#         df["ticker"]=ticker
#         histbuy=histbuy.append(df)
#     except:
#         pass

# # macd
# histsell=pd.DataFrame()
# for i in range(num):
#     ticker=(symbols[i])
#     df=macdsell()
#     try:
#         df=df[-1:]
#         df["ticker"]=ticker
#         histsell=histsell.append(df)
#     except:
#         pass

