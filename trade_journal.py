import ezsheets

class TradeJournal():

	def __init__(self, title):
		self.bootstrapped = False
		self.title = title

	def bootstrap(self):
		if self.bootstrapped == False:
			self.journal = self.__get_trade_journal__()
			self.bootstrapped = True

	def __get_trade_journal__(self):
		spreadsheets = ezsheets.listSpreadsheets()

		for key,value in spreadsheets.items():
			if value == self.title:
				return ezsheets.Spreadsheet(key)

		return self.__create_trade_journal__();

	def __create_trade_journal__(self):
		ss = ezsheets.createSpreadsheet(self.title)
		queued_trades = ss[0]
		queued_trades.title = "Queued Trades"
		queued_trades.updateRow(1, ['Ticker', 'Type', 'Entry Price', 'Exit Price', 'Stop Loss', 'Notes', 'MACD 1 Month', 'MACD 1 Day', 'MACD 1 Year', 'RSI 1 Month', 'RSI 1 Day', 'RSI 1 Year', 'SMA 50 1 Month', 'SMA 100 1 Month', 'SMA 200 1 Month', 'Volume 1 Month' ])
		trades = ss.createSheet('Trades')
		trades.updateRow(1, ['ID', 'Create Date', 'Ticker', 'Type', 'Status', 'Entry Date', 'Exit Date', 'Planned Entry Price', 'Planned Exit Price', 
			'Stop Loss', 'Shares', 'Entry Price', 'Exit Price', 'Gain', 'Buy Order', 'Sell Order', 'Notes', 'Comments', 
			'MACD 1 Month', 'MACD 1 Day', 'MACD 1 Year', 'RSI 1 Month', 'RSI 1 Day', 'RSI 1 Year', 'SMA 50 1 Month', 'SMA 100 1 Month', 'SMA 200 1 Month', 'Volume 1 Month'])
		return ss

	def get_queued_trades(self):
		self.journal.refresh()
		return self.journal[0].getRows()

	def reset_queued_trades(self, headerRow):
		self.journal.refresh()
		self.journal[0].updateRows([headerRow])

	def create_queued_trade(self, row_num, ticker, type, entry, exit, stop_loss):
		self.journal.refresh()
		self.journal[0].updateRow(row_num, [ticker, type, entry, exit, stop_loss, '', '', '', '', '', '', '', '', '', '', ''])


	def create_trade_record(self, trade, notes, macd, rsi, sma, volume):
		self.journal.refresh()
		self.journal[1].updateRow(trade.id + 1, [trade.id, trade.create_date, trade.ticker, trade.type, trade.status, trade.entry_date, trade.exit_date, 
			trade.planned_entry_price, trade.planned_exit_price, trade.stop_loss, trade.shares, trade.actual_entry_price, trade.actual_exit_price, '', trade.buy_order_id, trade.sell_order_id, notes, '',
			macd['month'], macd['day'], macd['year'], rsi['month'], rsi['day'], rsi['year'], sma['fifty'], sma['hundred'], sma['two_hundred'], volume])

	def update_trade_record(self, trade):
		self.journal.refresh()
		row = self.journal[1].getRow(trade.id + 1)
		notes = row[15]
		comments = row[16]
		macd = {
			'month': row[17],
			'day': row[18],
			'year': row[19]
		}
		rsi = {
			'month': row[20],
			'day': row[21],
			'year': row[22]
		}
		sma = {
			'fifty': row[23],
			'hundred': row[24],
			'two_hundred': row[25]
		}
		volume = row[26]
		gain = False
		
		if trade.actual_exit_price > trade.actual_entry_price:
			gain = True

		self.journal[1].updateRow(trade.id + 1, [trade.id, trade.create_date, trade.ticker, trade.type, trade.status, trade.entry_date, trade.exit_date, 
			trade.planned_entry_price, trade.planned_exit_price, trade.stop_loss, trade.shares, trade.actual_entry_price, trade.actual_exit_price, gain, trade.buy_order_id, trade.sell_order_id, notes, comments,
			macd['month'], macd['day'], macd['year'], rsi['month'], rsi['day'], rsi['year'], sma['fifty'], sma['hundred'], sma['two_hundred'], volume])
