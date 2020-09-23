import stockstats
import pandas as pd

def analyze(ticker, brokerage):
	minute_df = brokerage.get_last_250_minutes_data_set(ticker)
	minute_15_df = brokerage.get_last_250_15minutes_data_set(ticker)
	minute_stock = stockstats.StockDataFrame.retype(minute_df)
	minutes_15_stock = stockstats.StockDataFrame.retype(minute_15_df)
	minute_count = minute_df.shape[0]
	minute_15_count = minute_15_df.shape[0]

	return {
		'1min': {
			'open': '{:.2f}'.format(minute_stock['open'][minute_count - 1]),
			'close': '{:.2f}'.format(minute_stock['close'][minute_count - 1]),
			'sma50': '{:.2f}'.format(minute_stock['close_50_sma'][minute_count - 1]),
			'sma100': '{:.2f}'.format(minute_stock['close_100_sma'][minute_count - 1]),
			'sma200': '{:.2f}'.format(minute_stock['close_200_sma'][minute_count - 1]),
			'rsi_10': '{:.2f}'.format(minute_stock['rsi_10'][minute_count - 1]),
			'rsi_250': '{:.2f}'.format(minute_stock['rsi_250'][minute_count - 1]),
			'macd': '{:.2f}'.format(minute_stock['macd'][minute_count - 1]),
			'atr_20': str(minute_stock['atr_20'][minute_count - 1]),
			'volume': str(minute_stock['volume'][minute_count - 1])
		},
		'15min': {
			'open': '{:.2f}'.format(minute_stock['open'][minute_count - 1]),
			'close': '{:.2f}'.format(minute_stock['close'][minute_count - 1]),
			'sma50': '{:.2f}'.format(minutes_15_stock['close_50_sma'][minute_15_count - 1]),
			'sma100': '{:.2f}'.format(minutes_15_stock['close_100_sma'][minute_15_count - 1]),
			'sma200': '{:.2f}'.format(minutes_15_stock['close_200_sma'][minute_15_count - 1]),
			'rsi_10': '{:.2f}'.format(minute_stock['rsi_10'][minute_count - 1]),
			'rsi_250': '{:.2f}'.format(minute_stock['rsi_250'][minute_count - 1]),
			'macd': '{:.2f}'.format(minutes_15_stock['macd'][minute_15_count - 1]),
			'atr_20': str(minutes_15_stock['atr_20'][minute_15_count - 1]),
			'volume': str(minutes_15_stock['volume'][minute_15_count - 1])
		}
	}

def rsi_10(bars):
	for bar in bars[ticker]:
		ds.append([bar.open, bar.close, bar.high, bar.low, bar.volume])

	df = pd.DataFrame(data=ds, index=range(0, len(bars[ticker])), columns=['open','close','high','low','volume'])
	stock = stockstats.StockDataFrame.retype(df)
	count = df.shape[0]

	return stock['rsi_250'][count - 1]

def sma_3(bars):
	for bar in bars[ticker]:
		ds.append([bar.open, bar.close, bar.high, bar.low, bar.volume])

	df = pd.DataFrame(data=ds, index=range(0, len(bars[ticker])), columns=['open','close','high','low','volume'])
	stock = stockstats.StockDataFrame.retype(df)
	count = df.shape[0]

	return stock['sma_3'][count - 1]