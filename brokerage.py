import bar
import position
import order
import alpaca_trade_api as tradeapi
import logging
import pandas as pd
import cache

#All logic for connecting to the brokerage, submitting and receiving data is encapsulated in a single module and class.
#As a result, to use a different brokerage company with the bot, we just simply create a subclass of Brokerage and overwrite
#all the methods.
class Brokerage:

	def __init__(self, paper_trading_on, key_id, secret_key, data_folder):
		if (paper_trading_on == True):
			self.api = tradeapi.REST(key_id, secret_key, base_url='https://paper-api.alpaca.markets')
		else:
			self.api = tradeapi.REST(key_id, secret_key)
		self.data_folder = data_folder

	# Return True if the market is open, None if we receive an API error
	def is_open(self):
		try:
			return self.api.get_clock().is_open
		except tradeapi.rest.APIError as err:
			logging.error(f'POST /clock API Code: {err.code} HTTP Code: {err.status_code} Message: {str(err)}')
			return None

	def get_last_bars(self, ticker, length, time_segment):
		def bars():
			try:
				barset = self.api.get_barset(ticker, time_segment, length)
				bars = []

				for b in barset[ticker]:
					bars.append(bar.Bar(b))

				return bars
			except tradeapi.rest.APIError as err:
				logging.error(f'POST /bars/minute API Code: {err.code} HTTP Code: {err.status_code} Message: {str(err)}')
				return None


		fileCache = cache.get_cache(f'LAST_BARS_{length}_{time_segment}', self.data_folder)
		return fileCache.get(key=ticker, createfunc=bars)

	#Returns a panda.DataFrame with 250 minute bars worth of data or None if we received an API Err. Used for technical analysis of the stock at the time of sale.
	def get_last_250_minutes_data_set(self, ticker, with_time = False):
		try:
			bars = self.api.get_barset(ticker, 'minute', 250)
			ds=[]

			if with_time:
				for bar in bars[ticker]:
					ds.append([bar.o, bar.c, bar.h, bar.l, bar.v, bar.t])

				return pd.DataFrame(data=ds, index=range(0, len(bars[ticker])), columns=['open','close','high','low','volume', 'time'])
			else:
				for bar in bars[ticker]:
					ds.append([bar.o, bar.c, bar.h, bar.l, bar.v])

				return pd.DataFrame(data=ds, index=range(0, len(bars[ticker])), columns=['open','close','high','low','volume'])
		except tradeapi.rest.APIError as err:
			logging.error(f'POST /bars/minute API Code: {err.code} HTTP Code: {err.status_code} Message: {str(err)}')
			return None

	#Returns a panda.DataFrame with 250 15-minute bars worth of data or None if we received an API Err. Used for technical analysis of the stock at the time of sale.
	def get_last_250_15minutes_data_set(self, ticker, with_time=False):

		try:
			bars = self.api.get_barset(ticker, '15Min', 250)
			ds=[]

			if with_time:
				for bar in bars[ticker]:
					ds.append([bar.o, bar.c, bar.h, bar.l, bar.v, bar.t])

				return pd.DataFrame(data=ds, index=range(0, len(bars[ticker])), columns=['open','close','high','low','volume', 'time'])
			else:
				for bar in bars[ticker]:
					ds.append([bar.o, bar.c, bar.h, bar.l, bar.v])

				return pd.DataFrame(data=ds, index=range(0, len(bars[ticker])), columns=['open','close','high','low','volume'])
		except tradeapi.rest.APIError as err:
			logging.error(f'POST /bars/minute API Code: {err.code} HTTP Code: {err.status_code} Message: {str(err)}')
			return None

	# Submits a good to close market sell order. Returns order id or None if we received an API Error
	def sell(self, ticker, shares):
		try:	
			order = self.api.submit_order(
			    symbol=ticker,
			    side='sell',
			    type='market',
			    qty=f'{shares}',
			    time_in_force='gtc',
			    order_class='simple'
			)
			return order.client_order_id
		except tradeapi.rest.APIError as err:
			logging.error(f'POST /order API Code: {err.code} HTTP Code: {err.status_code} Message: {str(err)}')
			return None

	# Submits a day market buy order. Returns order id or None if we received an API Err
	def buy(self, ticker, shares):
		try:
			order = self.api.submit_order(
			    symbol=ticker,
			    side='buy',
			    type='market',
			    qty=f'{shares}',
			    time_in_force='day',
			    order_class='simple'
			)
			return order.client_order_id
		except tradeapi.rest.APIError as err:
			logging.error(f'POST /order API Code: {err.code} HTTP Code: {err.status_code} Message: {str(err)}')
			return None

	# Returns an Order object or None if 404
	def get_order(self, order_id):
		try:
			o = self.api.get_order_by_client_order_id(order_id)
			return order.Order(o.client_order_id, o.status, o.filled_avg_price, o.qty, o.replaced_by)
		except tradeapi.rest.APIError as err:
			logging.error(f'GET /order API Code: {err.code} HTTP Code: {err.status_code} Message: {str(err)}')
			return None

	# Returns the cash value of the brokerage account as a float, False if the brokerage account has maxed out it's day trades for the day or None of we receive an API error.
	def get_buying_power(self):
		try:
			account = self.api.get_account()
			cash = float(account.cash)
			if int(account.daytrade_count) >= 4 and cash <= 25000.0:
				return False
			return cash
		except tradeapi.rest.APIError as err:
			logging.error(f'GET /account API Code: {err.code} HTTP Code: {err.status_code} Message: {str(err)}')
			return None