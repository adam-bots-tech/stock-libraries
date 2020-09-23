import bar

class StockMath:
	def sma_3_close(self, bars):
		three_bar_avg = 0.0

		i = 0
		for bar in bars:
			if i >= 3:
				break

			three_bar_avg += bar.close
			i += 1

		return three_bar_avg / len(bars)

	def rsi_10_close(self, bars):
		gain = 0.0
		loss = 0.0

		i = 0
		for bar in bars:
			if i >= 10:
				break

			diff = bar.close - bar.open

			if diff < 0.0:
				loss += diff
			else:
				gain += diff

			i += 1

		avg_gain = gain / 10
		avg_loss = loss / 10

		return 100 - (100 / (1 + (avg_gain / -avg_loss)))
