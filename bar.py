class Bar:
	def __init__(self, data=None):

		if data is None:
			self.time = 0.0
			self.open = 0.0
			self.high = 0.0
			self.low= 0.0
			self.close = 0.0
			self.volume = 0.0
		elif type(data) is dict:
			self.time = data['t']
			self.open = data['o']
			self.high = data['h']
			self.low= data['l']
			self.close = data['c']
			self.volume = data['v']
		else:
			self.time = data.t
			self.open = data.o
			self.high = data.h
			self.low= data.l
			self.close = data.c
			self.volume = data.v