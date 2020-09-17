import sqlite3
import json

class StateDB:
	def __init__(self, database):
		self.database = database

	def __connect__(self):
		return sqlite3.connect(self.database)

	def __create_table__(self, c):
		c.execute('''CREATE TABLE IF NOT EXISTS properties (key TEXT PRIMARY KEY, value TEXT)''')

	def get_market_open(self):
		conn = self.__connect__()
		c = conn.cursor()
		self.__create_table__(c)
		c.execute(f"SELECT * FROM properties WHERE key='market_open'")
		data = c.fetchone()
		if (data == None):
			c.execute('''INSERT INTO properties VALUES ('market_open', 'False')''')
			conn.commit()
			conn.close()
			return False
		else:
			conn.close()
			return data[1] == 'True'

	def get_last_prices(self):
		conn = self.__connect__()
		c = conn.cursor()
		self.__create_table__(c)
		c.execute(f"SELECT * FROM properties WHERE key='last_prices'")
		data = c.fetchone()
		if (data == None):
			c.execute('''INSERT INTO properties VALUES ('last_prices', '{}')''')
			conn.commit()
			conn.close()
			return {}
		else:
			conn.close()
			return json.loads(data[1])

	def set_market_open(self, is_open):
		conn = self.__connect__()
		c = conn.cursor()
		self.__create_table__(c)
		c.execute(f"UPDATE properties SET value = '{is_open}' WHERE key = 'market_open'")
		conn.commit()
		conn.close()

	def set_last_prices(self, last_prices):
		conn = self.__connect__()
		c = conn.cursor()
		self.__create_table__(c)
		c.execute(f"UPDATE properties SET value = '{json.dumps(last_prices)}' WHERE key = 'last_prices'")
		conn.commit()
		conn.close()

	def remove_buy_price_marker(self, ticker, id):
		prices = self.get_last_prices()
		if 'buy'+ticker+str(id) in prices.keys():
			del prices['buy'+ticker+str(id)]
		self.set_last_prices(prices)

	def remove_sale_price_marker(self, ticker, id):
		prices = self.get_last_prices()
		if 'buy'+ticker+str(id) in prices.keys():
			del prices['buy'+ticker+str(id)]
		self.set_last_prices(prices)

	def set_sale_price_marker(self, ticker, id):
		prices = self.get_last_prices()
		prices['sell'+ticker+str(id)] = True
		self.set_last_prices(prices)

	def get_sale_price_marker(self, ticker, id):
		prices = self.get_last_prices()
		if 'sell'+ticker+str(id) not in prices.keys() or prices['sell'+ticker+str(id)] == False: 
			return False
		else:
			return True

	def set_buy_price_marker(self, ticker, id):
		prices = self.get_last_prices()
		prices['buy'+ticker+str(id)] = True
		self.set_last_prices(prices)

	def get_buy_price_marker(self, ticker, id):
		prices = self.get_last_prices()
		if 'buy'+ticker+str(id) not in prices.keys() or prices['buy'+ticker+str(id)] == False: 
			return False
		else:
			return True