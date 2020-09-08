import stockprofile
import re
from finviz.screener import Screener

def build_competitors_list(industry, ticker, data_folder):
	stock_profiles = []
	screened_stocks = Screener(filters=["ind_" + re.sub(r'\W+', '', industry).lower()], 
			table='Overview', order='-marketcap')

	i = 0
	for screened_stock in screened_stocks:
		i += 1

		# If the stock being screened is within the top 5 largest market cap, exclude it
		if screened_stock['Ticker'] == ticker:
			continue

		# Build a profile for use in comparison and add it to the list
		stock_profiles.append(stockprofile.build_profile(screened_stock['Ticker'], data_folder))

		if i > 5:
			break

	return stock_profiles