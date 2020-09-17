import bar

def sma_close(bars):
	three_bar_avg = 0.0

	for bar in bars:
		three_bar_avg += bar.close

	return three_bar_avg / len(bars)

def sma_high(bars):
	three_bar_avg = 0.0

	for bar in bars:
		three_bar_avg += bar.high

	return three_bar_avg / len(bars)