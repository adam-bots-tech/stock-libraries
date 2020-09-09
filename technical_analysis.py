import stockstats

def analyze(ticker, brokerage):
	minute_df = brokerage.get_last_200_minutes_data_set(ticker)
	minute_15_df = brokerage.get_last_200_15minutes_data_set(ticker)
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
			'rsi': '{:.2f}'.format(minute_stock['rsi_14'][minute_count - 1]),
			'macd': '{:.2f}'.format(minute_stock['macd'][minute_count - 1]),
			'volume': str(minute_stock['volume'][minute_count - 1])
		},
		'15min': {
			'open': '{:.2f}'.format(minute_stock['open'][minute_count - 1]),
			'close': '{:.2f}'.format(minute_stock['close'][minute_count - 1]),
			'sma50': '{:.2f}'.format(minutes_15_stock['close_50_sma'][minute_15_count - 1]),
			'sma100': '{:.2f}'.format(minutes_15_stock['close_100_sma'][minute_15_count - 1]),
			'sma200': '{:.2f}'.format(minutes_15_stock['close_200_sma'][minute_15_count - 1]),
			'rsi': '{:.2f}'.format(minutes_15_stock['rsi_14'][minute_15_count - 1]),
			'macd': '{:.2f}'.format(minutes_15_stock['macd'][minute_15_count - 1]),
			'volume': str(minutes_15_stock['volume'][minute_15_count - 1])
		}
	}