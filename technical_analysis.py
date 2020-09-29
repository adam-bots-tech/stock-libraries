import stock_math

def analyze(ticker, brokerage):
	minute_bars = brokerage.get_last_bars(ticker, 250, 'minute')
	minute_15_bars = brokerage.get_last_bars(ticker, 250, '15Min')
	sm = stock_math.StockMath()

	return {
		'1min': {
			'open': '{:.2f}'.format(minute_bars[0].open),
			'close': '{:.2f}'.format(minute_bars[0].close),
			'sma50': '{:.2f}'.format(sm.sma_50_close(minute_bars)),
			'sma100': '{:.2f}'.format(sm.sma_100_close(minute_bars)),
			'sma200': '{:.2f}'.format(sm.sma_200_close(minute_bars)),
			'rsi_10': '{:.2f}'.format(sm.rsi_10_close(minute_bars)),
			'rsi_250': '{:.2f}'.format(sm.rsi_250_close(minute_bars)),
			'macd': '{:.2f}'.format(sm.macd_close(minute_bars)),
			'atr_20': str(sm.atr_20(minute_bars)),
			'volume': str(sm.volume_50(minute_bars))
		},
		'15min': {
			'open': '{:.2f}'.format(minute_15_bars[0].open),
			'close': '{:.2f}'.format(minute_15_bars[0].close),
			'sma50': '{:.2f}'.format(sm.sma_50_close(minute_15_bars)),
			'sma100': '{:.2f}'.format(sm.sma_100_close(minute_15_bars)),
			'sma200': '{:.2f}'.format(sm.sma_200_close(minute_15_bars)),
			'rsi_10': '{:.2f}'.format(sm.rsi_10_close(minute_15_bars)),
			'rsi_250': '{:.2f}'.format(sm.rsi_250_close(minute_15_bars)),
			'macd': '{:.2f}'.format(sm.macd_close(minute_15_bars)),
			'atr_20': str(sm.atr_20(minute_15_bars)),
			'volume': str(sm.volume_50(minute_15_bars))
		},
	}