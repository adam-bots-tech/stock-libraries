
import pandas as pd
import stockstats

def analyze(bars):
	ds=[]

	for bar in bars:
		ds.append([bar.o, bar.c, bar.h, bar.l, bar.v])

	df = pd.DataFrame(data=ds, index=range(0, len(bars)), columns=['open','close','high','low','volume'])
	stock = stockstats.StockDataFrame.retype(df)

	stats = {}
	stats['rsi'] = stock['rsi_14'][len(bars) - 1]
	stats['macd'] = stock['macd'][len(bars) - 1]
	stats['sma50'] = stock['close_50_sma'][len(bars) - 1]
	stats['sma100'] = stock['close_100_sma'][len(bars) - 1]
	stats['sma200'] = stock['close_200_sma'][len(bars) - 1]
	stats['volume'] = stock['volume'][len(bars) - 1]
	return stats


