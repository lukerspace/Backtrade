import pandas as pd
# for filename in os.listdir("data/spy"):
#     df=pd.read_csv("data/spy/{}".format(filename))

def is_consolidate(df,symbol):
    # df["ticker"]=symbol
    monthly_close=df[-30:]
    monthly_volume=monthly_close["Volume"].mean()
    
    latest_close=df[-15:]
    latest_volume=latest_close["Volume"].mean()

    latest_max=latest_close["Close"].max()
    latest_min=latest_close["Close"].min()
    # if (latest_max/latest_min-1 < 0.025 ) & (latest_volume/monthly_volume>=1):
    #     return print(symbol,"is consolidated :" + str(round((latest_max/latest_min-1),4)), round(latest_volume/monthly_volume-1,3))
    if (latest_max/latest_min-1 <0.03 ) & (latest_volume/monthly_volume<1):
        # return print(symbol,"is consolidated & volume condensed:" + str(round((latest_max/latest_min-1),4)),round(latest_volume/monthly_volume-1,3))
        return True
    return  None


def is_breaking(df,symbol):
    try:
        last_close=df[-1:]["Close"].values[0]
        if is_consolidate(df[:-1],symbol):
            close=df[-16:-1]
            if last_close>close["Close"].max():
                return True
    except:
        return False
    

holdings = open('data/csv/spy.csv').readlines()
symbols = [holding.split(',')[2].strip() for holding in holdings][1:]

for symbol in symbols:
    df=pd.read_csv("data/spy/{}.txt".format(symbol))
    if (is_consolidate(df,symbol)):
        if (is_breaking(df,symbol)):
            print("{} is breaking out".format(symbol))
        else:
            print("{} is consolidating".format(symbol))
    




