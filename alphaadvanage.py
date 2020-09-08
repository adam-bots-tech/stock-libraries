import requests
import matplotlib.pyplot as plt
import numpy as np
import cache

def add_description_to_profile(stock, ticker, api_key, data_folder):
	def response():
		return requests.get(f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&interval=5min&apikey={api_key}')

	fileCache = cache.get_cache('OVERVIEW', data_folder)
	resp = fileCache.get(key=ticker, createfunc=response)

	if 'Description' in resp.json().keys():
		stock['description']=resp.json()['Description']

	return stock

def create_quarterly_financials_chart(ticker, chart_path, api_key, data_folder):
	date = []
	revenue = []
	profit = []

	def response():
		return requests.get(f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&interval=5min&apikey={api_key}')

	fileCache = cache.get_cache('INCOME_STATEMENT', data_folder)
	resp = fileCache.get(key=ticker, createfunc=response)

	json = resp.json()

	if 'quarterlyReports' not in json.keys():
		return

	i = 0
	for report in json['quarterlyReports']:
		i += 1
		date.append(report['fiscalDateEnding'])
		revenue.append(int(report['totalRevenue']))
		profit.append(int(report['grossProfit']))
		if i >= 8:
			break

	x = np.arange(len(date))
	ax = plt.subplot(1,1,1)
	w = 0.3
	plt.xticks(x + w /2, date, rotation='vertical')
	rev =ax.bar(x, revenue, width=w, color='b', align='center')
	pro =ax.bar(x + w, profit, width=w,color='g',align='center')
	ax.xaxis_date()
	plt.legend([rev, pro],['Revenue', 'Profit'])
	plt.title("Quarterly Financial Reports")
	plt.savefig(chart_path)
	plt.close()


