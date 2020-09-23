import bar
import position
import order
import alpaca_trade_api as tradeapi
import logging
import pandas as pd
import cache

class Brokerage:

	def __init__(self, paper_trading_on, key_id, secret_key, data_folder):
		if (paper_trading_on == True):
			self.api = tradeapi.REST(key_id, secret_key, base_url='https://paper-api.alpaca.markets')
		else:
			self.api = tradeapi.REST(key_id, secret_key)
		self.data_folder = data_folder

	def is_open(self):
		try:
			return self.api.get_clock().is_open
		except tradeapi.rest.APIError as err:
			logging.error(f'POST /clock API Code: {err.code} HTTP Code: {err.status_code} Message: {str(err)}')
			return None

	# Return a Position object or None if 404
	def get_position(self, ticker):
		try:
			p = self.api.get_position(ticker)
			return position.Position(p.symbol, p.qty, p.avg_entry_price)
		except tradeapi.rest.APIError as err:
			logging.error(f'POST /position API Code: {err.code} HTTP Code: {err.status_code} Message: {str(err)}')

			if err.code == '404':
				return None
			else:
				return False

	# Return a list with last three Bar objects or None if 404
	def get_last_ten_bars(self, ticker):
		def bars():
			try:
				barset = self.api.get_barset(ticker, 'minute', 10)
				bars = []

				for b in barset[ticker]:
					bars.append(bar.Bar(b))

				return bars
			except tradeapi.rest.APIError as err:
				logging.error(f'POST /bars/minute API Code: {err.code} HTTP Code: {err.status_code} Message: {str(err)}')
				return None


		fileCache = cache.get_cache('LAST_THREE_BARS', self.data_folder)
		return fileCache.get(key=ticker, createfunc=bars)

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

	# Return order id or None if failed
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

	# Return order id or None if failed
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

	# Return Order object or None if 404
	def get_order(self, order_id):
		try:
			o = self.api.get_order_by_client_order_id(order_id)
			return order.Order(o.client_order_id, o.status, o.filled_avg_price, o.qty, o.replaced_by)
		except tradeapi.rest.APIError as err:
			logging.error(f'GET /order API Code: {err.code} HTTP Code: {err.status_code} Message: {str(err)}')
			return None

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