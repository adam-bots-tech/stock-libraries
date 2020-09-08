import requests
import cache

def get_messages(ticker, data_folder):
	def response():
		return requests.get(f'https://api.stocktwits.com/api/2/streams/symbol/{ticker}.json')

	fileCache = cache.get_cache('STOCK_TWITS', data_folder)
	resp = fileCache.get(key=ticker, createfunc=response)
	return resp.json()['messages'];

def process_messages(messages):
	twits = []
	for message in messages:
		twits.append(message['body'])
	return twits
