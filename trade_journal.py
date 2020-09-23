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
		queued_trades.updateRow(1, ['Ticker', 'Type', 'Entry Price', 'Exit Price', 'Stop Loss', 'Notes', 'Expiration in Days', 'Metadata', 'Sell At End of Day'])
		trades = ss.createSheet('Trades')
		trades.updateRow(1, ['ID', 'Create Date', 'Ticker', 'Type', 'Status', 'Entry Date', 'Exit Date', 'Planned Entry Price', 'Planned Exit Price', 
			'Stop Loss', 'Shares', 'Entry Price', 'Exit Price', 'Gain', 'Buy Order', 'Sell Order', 'Notes', 'Comments', 'Metadata', 'Buy Metadata','Sale Metadata'])
		return ss

	def get_queued_trades(self):
		self.journal.refresh()
		return self.journal[0].getRows()

	def reset_queued_trades(self, headerRow):
		self.journal.refresh()
		self.journal[0].updateRows([headerRow])

	def create_queued_trade(self, row_num, ticker, type, entry, exit, stop_loss, notes, expiration, metadata, end_of_day):
		self.journal.refresh()
		self.journal[0].updateRow(row_num, [ticker, type, entry, exit, stop_loss, notes, expiration, metadata, end_of_day])


	def create_trade_record(self, trade, notes, metadata):
		self.journal.refresh()
		self.journal[1].updateRow(trade.id + 1, [trade.id, trade.create_date, trade.ticker, trade.type, trade.status, trade.entry_date, trade.exit_date, 
			trade.planned_entry_price, trade.planned_exit_price, trade.stop_loss, trade.shares, trade.actual_entry_price, 
			trade.actual_exit_price, '', trade.buy_order_id, trade.sell_order_id, notes, '', metadata, '', ''])

	def update_trade_record(self, trade, sale_metadata=None, buy_metadata=None):
		self.journal.refresh()
		row = self.journal[1].getRow(trade.id + 1)
		notes = row[16]
		comments = row[17]
		metadata = row[18]
		gain = False

		if sale_metadata == None:
			sale_metadata = row[20]

		if buy_metadata == None:
			buy_metadata = row[19]
		
		if trade.actual_exit_price > trade.actual_entry_price:
			gain = True

		self.journal[1].updateRow(trade.id + 1, [trade.id, trade.create_date, trade.ticker, trade.type, trade.status, trade.entry_date, trade.exit_date, 
			trade.planned_entry_price, trade.planned_exit_price, trade.stop_loss, trade.shares, trade.actual_entry_price, 
			trade.actual_exit_price, gain, trade.buy_order_id, trade.sell_order_id, notes, comments, metadata, buy_metadata, sale_metadata])
