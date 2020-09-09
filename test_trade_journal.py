import trade_journal
import trade

TITLE = 'TEST TRADE JOURNAL'

j = trade_journal.TradeJournal(TITLE)
j.bootstrap()
ss = j.journal

assert j.bootstrapped == True, 'Bootstrapped is false'
assert ss[0].title == "Queued Trades", 'Queued Trades title is wrong'
assert ss[1].title == "Trades", 'Trades title is wrong'

j.create_queued_trade(2, 'TSLA', 'long', 10.0, 15.0, 5.0, 'notes', 4, 'metadata', 'base64')
rows = queued_trades = j.get_queued_trades()


assert rows[0][0] == 'Ticker', f'Queued Trade [0][0]: {rows[0][0]}'
assert rows[0][1] == 'Type', f'Queued Trade [0][1]: {rows[0][1]}'
assert rows[0][2] == 'Entry Price', f'Queued Trade [0][2]: {rows[0][2]}'
assert rows[0][3] == 'Exit Price', f'Queued Trade [0][3]: {rows[0][3]}'
assert rows[0][4] == 'Stop Loss', f'Queued Trade [0][4]: {rows[0][4]}'
assert rows[0][5] == 'Notes', f'Queued Trade [0][5]: {rows[0][5]}'
assert rows[0][6] == 'Expiration in Days', f'Queued Trade [0][6]: {rows[0][6]}'
assert rows[0][7] == 'Metadata', f'Queued Trade [0][7]: {rows[0][7]}'
assert rows[0][8] == 'Base64', f'Queued Trade [0][8]: {rows[0][8]}'

assert rows[1][0] == 'TSLA', f'Queued Trade [1][0]: {rows[1][0]}'
assert rows[1][1] == 'long', f'Queued Trade [1][1]: {rows[1][1]}'
assert rows[1][2] == '10', f'Queued Trade [1][2]: {rows[1][2]}'
assert rows[1][3] == '15', f'Queued Trade [1][3]: {rows[1][3]}'
assert rows[1][4] == '5', f'Queued Trade [1][4]: {rows[1][4]}'
assert rows[1][5] == 'notes', f'Queued Trade [1][5]: {rows[0][5]}'
assert rows[1][6] == '4', f'Queued Trade [1][6]: {rows[1][6]}'
assert rows[1][7] == 'metadata', f'Queued Trade [1][7]: {rows[1][7]}'
assert rows[1][8] == 'base64', f'Queued Trade [1][8]: {rows[1][8]}'

j.reset_queued_trades(rows[0])
rows = queued_trades = j.get_queued_trades()

assert rows[0][0] == 'Ticker', f'Queued Trade [0][0]: {rows[0][0]}'
assert rows[0][1] == 'Type', f'Queued Trade [0][1]: {rows[0][1]}'
assert rows[0][2] == 'Entry Price', f'Queued Trade [0][2]: {rows[0][2]}'
assert rows[0][3] == 'Exit Price', f'Queued Trade [0][3]: {rows[0][3]}'
assert rows[0][4] == 'Stop Loss', f'Queued Trade [0][4]: {rows[0][4]}'
assert rows[0][5] == 'Notes', f'Queued Trade [0][5]: {rows[0][5]}'
assert rows[0][6] == 'Expiration in Days', f'Queued Trade [0][6]: {rows[0][6]}'
assert rows[0][7] == 'Metadata', f'Queued Trade [0][7]: {rows[0][7]}'
assert rows[0][8] == 'Base64', f'Queued Trade [0][8]: {rows[0][8]}'

assert rows[1][0] == '', f'Queued Trade [1][0]: {rows[1][0]}'
assert rows[1][1] == '', f'Queued Trade [1][1]: {rows[1][1]}'
assert rows[1][2] == '', f'Queued Trade [1][2]: {rows[1][2]}'
assert rows[1][3] == '', f'Queued Trade [1][3]: {rows[1][3]}'
assert rows[1][4] == '', f'Queued Trade [1][4]: {rows[1][4]}'
assert rows[1][5] == '', f'Queued Trade [1][5]: {rows[0][5]}'
assert rows[1][6] == '', f'Queued Trade [1][6]: {rows[1][6]}'
assert rows[1][7] == '', f'Queued Trade [1][7]: {rows[1][7]}'
assert rows[1][8] == '', f'Queued Trade [1][8]: {rows[1][8]}'

t = trade.Trade(10, 'TSLA', 2, 3, 50, 300, 200, 150, 305, 199.5, 'CLOSED', 4, 5,'long',1, 4)
j.create_trade_record(t, 'notes', 'metadata', 'base64')
j.update_trade_record(t, buy_metadata='Test')
rows = ss[1].getRows()

assert rows[0][0] == 'ID', f'Queued Trade [0][0]: {rows[0][0]}'
assert rows[0][1] == 'Create Date', f'Queued Trade [0][1]: {rows[0][1]}'
assert rows[0][2] == 'Ticker', f'Queued Trade [0][2]: {rows[0][2]}'
assert rows[0][3] == 'Type', f'Queued Trade [0][3]: {rows[0][3]}'
assert rows[0][4] == 'Status', f'Queued Trade [0][4]: {rows[0][4]}'
assert rows[0][5] == 'Entry Date', f'Queued Trade [0][5]: {rows[0][5]}'
assert rows[0][6] == 'Exit Date', f'Queued Trade [0][6]: {rows[0][6]}'
assert rows[0][7] == 'Planned Entry Price', f'Queued Trade [0][7]: {rows[0][7]}'
assert rows[0][8] == 'Planned Exit Price', f'Queued Trade [0][8]: {rows[0][8]}'
assert rows[0][9] == 'Stop Loss', f'Queued Trade [0][9]: {rows[0][9]}'
assert rows[0][10] == 'Shares', f'Queued Trade [0][10]: {rows[0][10]}'
assert rows[0][11] == 'Entry Price', f'Queued Trade [0][11]: {rows[0][11]}'
assert rows[0][12] == 'Exit Price', f'Queued Trade [0][12]: {rows[0][12]}'
assert rows[0][13] == 'Gain', f'Queued Trade [0][13]: {rows[0][13]}'
assert rows[0][14] == 'Buy Order', f'Queued Trade [0][14]: {rows[0][14]}'
assert rows[0][15] == 'Sell Order', f'Queued Trade [0][15]: {rows[0][15]}'
assert rows[0][16] == 'Notes', f'Queued Trade [0][16]: {rows[0][16]}'
assert rows[0][17] == 'Comments', f'Queued Trade [0][17]: {rows[0][17]}'
assert rows[0][18] == 'Metadata', f'Queued Trade [0][19]: {rows[0][18]}'
assert rows[0][19] == 'Buy Metadata', f'Queued Trade [0][19]: {rows[0][19]}'
assert rows[0][20] == 'Sale Metadata', f'Queued Trade [0][19]: {rows[0][20]}'

assert str(rows[1][0]) == '1', f'Queued Trade [1][0]: {rows[1][0]}'
assert str(rows[1][1]) == '10', f'Queued Trade [1][1]: {rows[1][1]}'
assert str(rows[1][2]) == 'TSLA', f'Queued Trade [1][2]: {rows[1][2]}'
assert str(rows[1][3]) == 'long', f'Queued Trade [1][3]: {rows[1][3]}'
assert str(rows[1][4]) == 'CLOSED', f'Queued Trade [1][4]: {rows[1][4]}'
assert str(rows[1][5]) == '2', f'Queued Trade [1][5]: {rows[1][5]}'
assert str(rows[1][6]) == '3', f'Queued Trade [1][6]: {rows[1][6]}'
assert str(rows[1][7]) == '200', f'Queued Trade [1][7]: {rows[1][7]}'
assert str(rows[1][8]) == '300', f'Queued Trade [1][8]: {rows[1][8]}'
assert str(rows[1][9]) == '150', f'Queued Trade [1][9]: {rows[1][9]}'
assert str(rows[1][10]) == '50', f'Queued Trade [1][10]: {rows[1][10]}'
assert str(rows[1][11]) == '199.5', f'Queued Trade [1][11]: {rows[1][11]}'
assert str(rows[1][12]) == '305', f'Queued Trade [1][12]: {rows[1][12]}'
assert str(rows[1][13]) == 'True', f'Queued Trade [1][13]: {rows[1][13]}'
assert str(rows[1][14]) == '4', f'Queued Trade [1][14]: {rows[1][14]}'
assert str(rows[1][15]) == '5', f'Queued Trade [1][15]: {rows[1][15]}'
assert str(rows[1][16]) == 'notes', f'Queued Trade [1][16]: {rows[1][16]}'
assert str(rows[1][17]) == '', f'Queued Trade [1][17]: {rows[1][17]}'
assert str(rows[1][18]) == 'metadata', f'Queued Trade [1][18]: {rows[1][18]}'
assert str(rows[1][19]) == 'Test', f'Queued Trade [1][19]: {rows[1][19]}'
assert str(rows[1][20]) == '', f'Queued Trade [1][20]: {rows[1][20]}'

t.ticker = 'AAPL'
j.update_trade_record(t, sale_metadata='Test 2')

rows = ss[1].getRows()

assert rows[0][0] == 'ID', f'Queued Trade [0][0]: {rows[0][0]}'
assert rows[0][1] == 'Create Date', f'Queued Trade [0][1]: {rows[0][1]}'
assert rows[0][2] == 'Ticker', f'Queued Trade [0][2]: {rows[0][2]}'
assert rows[0][3] == 'Type', f'Queued Trade [0][3]: {rows[0][3]}'
assert rows[0][4] == 'Status', f'Queued Trade [0][4]: {rows[0][4]}'
assert rows[0][5] == 'Entry Date', f'Queued Trade [0][5]: {rows[0][5]}'
assert rows[0][6] == 'Exit Date', f'Queued Trade [0][6]: {rows[0][6]}'
assert rows[0][7] == 'Planned Entry Price', f'Queued Trade [0][7]: {rows[0][7]}'
assert rows[0][8] == 'Planned Exit Price', f'Queued Trade [0][8]: {rows[0][8]}'
assert rows[0][9] == 'Stop Loss', f'Queued Trade [0][9]: {rows[0][9]}'
assert rows[0][10] == 'Shares', f'Queued Trade [0][10]: {rows[0][10]}'
assert rows[0][11] == 'Entry Price', f'Queued Trade [0][11]: {rows[0][11]}'
assert rows[0][12] == 'Exit Price', f'Queued Trade [0][12]: {rows[0][12]}'
assert rows[0][13] == 'Gain', f'Queued Trade [0][13]: {rows[0][13]}'
assert rows[0][14] == 'Buy Order', f'Queued Trade [0][14]: {rows[0][14]}'
assert rows[0][15] == 'Sell Order', f'Queued Trade [0][15]: {rows[0][15]}'
assert rows[0][16] == 'Notes', f'Queued Trade [0][16]: {rows[0][16]}'
assert rows[0][17] == 'Comments', f'Queued Trade [0][17]: {rows[0][17]}'
assert rows[0][18] == 'Metadata', f'Queued Trade [0][18]: {rows[0][18]}'
assert rows[0][19] == 'Buy Metadata', f'Queued Trade [0][19]: {rows[0][19]}'
assert rows[0][20] == 'Sale Metadata', f'Queued Trade [0][20]: {rows[0][20]}'

assert str(rows[1][0]) == '1', f'Queued Trade [1][0]: {rows[1][0]}'
assert str(rows[1][1]) == '10', f'Queued Trade [1][1]: {rows[1][1]}'
assert str(rows[1][2]) == 'AAPL', f'Queued Trade [1][2]: {rows[1][2]}'
assert str(rows[1][3]) == 'long', f'Queued Trade [1][3]: {rows[1][3]}'
assert str(rows[1][4]) == 'CLOSED', f'Queued Trade [1][4]: {rows[1][4]}'
assert str(rows[1][5]) == '2', f'Queued Trade [1][5]: {rows[1][5]}'
assert str(rows[1][6]) == '3', f'Queued Trade [1][6]: {rows[1][6]}'
assert str(rows[1][7]) == '200', f'Queued Trade [1][7]: {rows[1][7]}'
assert str(rows[1][8]) == '300', f'Queued Trade [1][8]: {rows[1][8]}'
assert str(rows[1][9]) == '150', f'Queued Trade [1][9]: {rows[1][9]}'
assert str(rows[1][10]) == '50', f'Queued Trade [1][10]: {rows[1][10]}'
assert str(rows[1][11]) == '199.5', f'Queued Trade [1][11]: {rows[1][11]}'
assert str(rows[1][12]) == '305', f'Queued Trade [1][12]: {rows[1][12]}'
assert str(rows[1][13]) == 'True', f'Queued Trade [1][13]: {rows[1][13]}'
assert str(rows[1][14]) == '4', f'Queued Trade [1][14]: {rows[1][14]}'
assert str(rows[1][15]) == '5', f'Queued Trade [1][15]: {rows[1][15]}'
assert str(rows[1][16]) == 'notes', f'Queued Trade [1][16]: {rows[1][16]}'
assert str(rows[1][17]) == '', f'Queued Trade [1][17]: {rows[1][17]}'
assert str(rows[1][18]) == 'metadata', f'Queued Trade [1][18]: {rows[1][18]}'
assert str(rows[1][19]) == 'Test', f'Queued Trade [1][19]: {rows[1][19]}'
assert str(rows[1][20]) == 'Test 2', f'Queued Trade [1][20]: {rows[1][20]}'


ss.delete()