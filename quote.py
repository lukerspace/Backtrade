
import requests
import config
import datetime
from datetime import *



def spydata():
    holdings = open('data/csv/spy.csv').readlines()
    symbols = [holding.split(',')[2].strip() for holding in holdings][1:]

    ticker = ",".join(symbols)
    # time_interval

    day_bars_1 = '{}/day?symbols={}&limit=300'.format(config.BARS_URL, ticker[1:800])

    day_bars_2 = '{}/day?symbols={}&limit=300'.format(config.BARS_URL, ticker[801:1598])

    day_bars_3 = '{}/day?symbols={}&limit=300'.format(config.BARS_URL, ticker[1599:2113])

    # minute_bars_url = config.BARS_URL + '/5Min?symbols=MSFT&limit=1000'

    day_bar_list=[day_bars_1,day_bars_2,day_bars_3 ]

    for url in day_bar_list:
        r = requests.get(url, headers=config.HEADERS)
        data=r.json()


        for symbol in data:
            filename = 'data/spy/{}.txt'.format(symbol)
            f = open(filename, 'w+')
            f.write('Date,Open,High,Low,Close,Volume,OpenInterest\n')

            for bar in data[symbol]:
                t = datetime.fromtimestamp(bar['t'])
                day = t.strftime('%Y-%m-%d')

                line = '{},{},{},{},{},{},{}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
                f.write(line)
    return  print("spy loaded")
spydata()



def read_qqq():
    # read_ticker
    holdings = open('data/csv/qqq.csv').readlines()
    symbols = [holding.split(',')[2].strip() for holding in holdings][1:]
    symbols = ",".join(symbols)

    # time_interval
    day_bars_url = '{}/day?symbols={}&limit=1000'.format(config.BARS_URL, symbols)
    # minute_bars_url = config.BARS_URL + '/5Min?symbols=MSFT&limit=1000'


    # # read_data
    r = requests.get(day_bars_url, headers=config.HEADERS)

    ## minute_data
    # r = requests.get(minute_bars_url, headers=config.HEADERS)
    # print(json.dumps(r.json(),indent=4))


    #data_form 
    # print(json.dumps(r.json(), indent=4))
    data=r.json()

    # show_stock_in_etf_QQQ
    for symbol in data:
        filename = 'data/qqq/{}.txt'.format(symbol)
        f = open(filename, 'w+')
        f.write('Date,Open,High,Low,Close,Volume,OpenInterest\n')
        # print(data[symbol])

        for bar in data[symbol]:
            t = datetime.fromtimestamp(bar['t'])
            day = t.strftime('%Y-%m-%d')

            line = '{},{},{},{},{},{},{}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
            f.write(line)
    return print("qqq loaded")

read_qqq()




def arkdata():
    holdings = open('data/csv/ark.csv').readlines()
    symbols=[i.strip() for i in holdings][1:]
    ticker = ",".join(symbols)
    # print(len(ticker))

    # time_interval


    day_bars_url = '{}/day?symbols={}&limit=300'.format(config.BARS_URL, ticker[1:])

    # minute_bars_url = config.BARS_URL + '/5Min?symbols=MSFT&limit=1000'


    # # # read_data
    r = requests.get(day_bars_url, headers=config.HEADERS)
    data=r.json()


    for symbol in data:
        filename = 'data/ark/{}.txt'.format(symbol)
        f = open(filename, 'w+')
        f.write('Date,Open,High,Low,Close,Volume,OpenInterest\n')
        # print(data[symbol])

        for bar in data[symbol]:
            t = datetime.fromtimestamp(bar['t'])
            day = t.strftime('%Y-%m-%d')

            line = '{},{},{},{},{},{},{}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
            f.write(line)
    return print("ark loaded")

arkdata()


