import backtrader as bt
import os
from datetime import *
import config
from config import *

from VIXStrategy import VIXStrategy
import yfinance as yf

from quote import *


def saveplots(cerebro, numfigs=1, iplot=True, start=None, end=None,
             width=16, height=9, dpi=300, tight=True, use=None, file_path = '', **kwargs):

        from backtrader import plot
        if cerebro.p.oldsync:
            plotter = plot.Plot_OldSync(volume=False,**kwargs)
        else:
            plotter = plot.Plot(volume=False,**kwargs)

        figs = []
        for stratlist in cerebro.runstrats:
            for si, strat in enumerate(stratlist):
                rfig = plotter.plot(strat, figid=si * 100,
                                    numfigs=numfigs, iplot=iplot,
                                    start=start, end=end, use=use)
                figs.append(rfig)

        for fig in figs:
            for f in fig:
                f.savefig(file_path, bbox_inches='tight')
        return figs

def vix_spy():
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100000)


    class SPYVIXData(bt.feeds.GenericCSVData):
        lines = ('vixopen', 'vixhigh', 'vixlow', 'vixclose',)

        params = (
            ('dtformat', '%Y-%m-%d'),
            ('date', 0),
            ('spyopen', 1),
            ('spyhigh', 2),
            ('spylow', 3),
            ('spyclose', 4),
            ('spyadjclose', 5),
            ('spyvolume', 6),
            ('vixopen', 7),
            ('vixhigh', 8),
            ('vixlow', 9),
            ('vixclose', 10)
        )
    class VIXData(bt.feeds.GenericCSVData):
            params = (
    
            ('dtformat', '%Y-%m-%d'),
            ('date', 0),
            ('vixopen', 1),
            ('vixhigh', 2),
            ('vixlow', 3),
            ('vixclose', 4),
            ('volume', -1),
            ('openinterest', -1)
        )

    csv_file = os.path.dirname(os.path.realpath(__file__)) + "\\spy2021.csv"
    vix_csv_file = os.path.dirname(os.path.realpath(__file__)) + "\\vix2021.csv"

    spyVixDataFeed = SPYVIXData(dataname=csv_file)
    vixDataFeed = VIXData(dataname=vix_csv_file)

    cerebro.adddata(spyVixDataFeed)
    cerebro.adddata(vixDataFeed)

    cerebro.addstrategy(VIXStrategy)
    cerebro.run()

    saveplots(cerebro, file_path = 'apps/static/vix/spy.png') #run it
    return print("=== update the latest VIX on DATE : {} ===".format(datetime.now()))

def vix_qqq():
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100000)


    class SPYVIXData(bt.feeds.GenericCSVData):
        lines = ('vixopen', 'vixhigh', 'vixlow', 'vixclose',)

        params = (
            ('dtformat', '%Y-%m-%d'),
            ('date', 0),
            ('spyopen', 1),
            ('spyhigh', 2),
            ('spylow', 3),
            ('spyclose', 4),
            ('spyadjclose', 5),
            ('spyvolume', 6),
            ('vixopen', 7),
            ('vixhigh', 8),
            ('vixlow', 9),
            ('vixclose', 10)
        )
    class VIXData(bt.feeds.GenericCSVData):
            params = (
    
            ('dtformat', '%Y-%m-%d'),
            ('date', 0),
            ('vixopen', 1),
            ('vixhigh', 2),
            ('vixlow', 3),
            ('vixclose', 4),
            ('volume', -1),
            ('openinterest', -1)
        )

    csv_file = os.path.dirname(os.path.realpath(__file__)) + "\\qqq2021.csv"
    vix_csv_file = os.path.dirname(os.path.realpath(__file__)) + "\\vix2021.csv"

    spyVixDataFeed = SPYVIXData(dataname=csv_file)
    vixDataFeed = VIXData(dataname=vix_csv_file)

    cerebro.adddata(spyVixDataFeed)
    cerebro.adddata(vixDataFeed)

    cerebro.addstrategy(VIXStrategy)
    cerebro.run()

    saveplots(cerebro, file_path = 'apps/static/vix/qqq.png') #run it
    return print("=== update the latest VIX on DATE : {} ===".format(datetime.now()))


def vix_arkk():
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100000)


    class SPYVIXData(bt.feeds.GenericCSVData):
        lines = ('vixopen', 'vixhigh', 'vixlow', 'vixclose',)

        params = (
            ('dtformat', '%Y-%m-%d'),
            ('date', 0),
            ('spyopen', 1),
            ('spyhigh', 2),
            ('spylow', 3),
            ('spyclose', 4),
            ('spyadjclose', 5),
            ('spyvolume', 6),
            ('vixopen', 7),
            ('vixhigh', 8),
            ('vixlow', 9),
            ('vixclose', 10)
        )
    class VIXData(bt.feeds.GenericCSVData):
            params = (
    
            ('dtformat', '%Y-%m-%d'),
            ('date', 0),
            ('vixopen', 1),
            ('vixhigh', 2),
            ('vixlow', 3),
            ('vixclose', 4),
            ('volume', -1),
            ('openinterest', -1)
        )

    csv_file = os.path.dirname(os.path.realpath(__file__)) + "\\arkk2021.csv"
    vix_csv_file = os.path.dirname(os.path.realpath(__file__)) + "\\vix2021.csv"

    spyVixDataFeed = SPYVIXData(dataname=csv_file)
    vixDataFeed = VIXData(dataname=vix_csv_file)

    cerebro.adddata(spyVixDataFeed)
    cerebro.adddata(vixDataFeed)

    cerebro.addstrategy(VIXStrategy)
    cerebro.run()

    saveplots(cerebro, file_path = 'apps/static/vix/arkk.png') #run it
    return print("=== update the latest VIX on DATE : {} ===".format(datetime.now()))


vix_spy()
vix_qqq()
vix_arkk()

# cerebro.plot(volume=False, savefig=True, figfilename='vix.png')
# figure = cerebro.plot(iplot=False,volume=False)[0][0].savefig('vix/vix.png')
# figure.savefig('vix.png')





