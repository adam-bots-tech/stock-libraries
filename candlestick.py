import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import base64

def create_15_minute_base64(ticker, brokerage):
	df = brokerage.get_last_200_15minutes_data_set(ticker, with_time=True)

	fig = go.Figure(data=[go.Candlestick(x=df['time'],
		open=df['open'],
		high=df['high'],
		low=df['low'],
		close=df['close'])])
  
	fig.update_layout(
		title= {
			'text': ticker,
			'y':0.9,
			'x':0.5,
			'xanchor': 'center',
			'yanchor': 'top'},
		font=dict(
		family='Courier New, monospace',
		size=20,
		color='#7f7f7f'
	))

	return base64.encodebytes(fig.to_image(format="png")).decode("utf-8").replace('\n','\t')

