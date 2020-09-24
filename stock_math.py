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

		return three_bar_avg / 3

	def sma_5_close(self, bars):
		three_bar_avg = 0.0

		i = 0
		for bar in bars:
			if i >= 3:
				break

			three_bar_avg += bar.close
			i += 1

		return three_bar_avg / 5

	def rsi_10_close(self, bars):
		gain = 0.0
		gain_count = 0
		loss = 0.0
		loss_count = 0

		i = 0
		for bar in bars:
			if i >= 10:
				break

			diff = bar.close - bar.open

			if diff < 0.0:
				loss += diff
				loss_count += 1
			else:
				gain += diff
				gain_count += 1

			i += 1

		avg_gain = 0
		avg_loss = 0

		if gain_count != 0:
			avg_gain = gain / gain_count

		if loss_count != 0:
			avg_loss = loss / loss_count

		if avg_loss == 0:
			return 100 - (100 / (1 + avg_gain))
		else:
			return 100 - (100 / (1 + (avg_gain / -avg_loss)))
