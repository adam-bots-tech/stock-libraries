import bar
import math
import stockstats
import pandas as pd

#I wrapped the stockstats module in a class so I can mock out the math during testing
class StockMath:
	def sma_3_close(self, bars):
		return self.__sma__(bars, 3)

	def sma_5_close(self, bars):
		return self.__sma__(bars, 5)

	def sma_50_close(self, bars):
		return self.__sma__(bars, 50)

	def sma_100_close(self, bars):
		return self.__sma__(bars, 100)

	def sma_200_close(self, bars):
		return self.__sma__(bars, 200)

	def __sma__(self, bars, length):
		temp = self.__convert_bars__(bars)
		return temp['stats'][f'close_{length}_sma'][temp['len'] - 1]

	def rsi_10_close(self, bars):
		return self.__rsi__(bars, 10)

	def rsi_250_close(self, bars):
		return self.__rsi__(bars, 250)

	def __rsi__(self, bars, length):
		temp = self.__convert_bars__(bars)
		return temp['stats'][f'rsi_{length}'][temp['len'] - 1]


	def macd_close(self, bars):
		temp = self.__convert_bars__(bars)
		return temp['stats']['macd'][temp['len'] - 1]

	def volume_50(self, bars):
		return self.__volume__(bars, 50)

	def __volume__(self, bars, length):
		temp = self.__convert_bars__(bars)
		return temp['stats']['volume'][temp['len'] - 1]

	def atr_20(self, bars):
		return self.__atr__(bars, 20)

	def __atr__(self, bars, length):
		temp = self.__convert_bars__(bars)
		return temp['stats'][f'atr_{length}'][temp['len'] - 1]

	def __convert_bars__(self, bars):
		ds=[]

		for bar in bars:
			ds.append([bar.open, bar.close, bar.high, bar.low, bar.volume])

		df = pd.DataFrame(data=ds, index=range(0, len(bars)), columns=['open','close','high','low','volume'])

		return {
			'stats': stockstats.StockDataFrame.retype(df),
			'len': df.shape[0]
		}




