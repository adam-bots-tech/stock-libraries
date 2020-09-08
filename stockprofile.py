import finviz
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import cache

def build_profile(ticker, data_folder):
	def response():
		return finviz.get_stock(ticker)

	fileCache = cache.get_cache('STOCK', data_folder)
	stock = fileCache.get(key=ticker, createfunc=response)

	return {
		'ticker': ticker,
		'industry': stock['Industry'],
		'name': stock['Company'],
		'pe': stock['P/E'],
		'eps': stock['EPS (ttm)'],
		'eps_q': stock['EPS next Q'],
		'mc': stock['Market Cap'],
		'forward_pe': stock['Forward P/E'],
		'income': stock['Income'],
		'sales': stock['Sales'],
		'52w': stock['52W Range'],
		'roe': stock['ROE'],
		'avg_vol': stock['Avg Volume'],
		'vol': stock['Volume'],
		'shares' : stock['Shs Outstand'],
		'debt_eq': stock['Debt/Eq'],
		'short_perc' : stock['Short Float'],
		'earnings': stock['Earnings']
	}

def get_news_feed(ticker, data_folder):
	def response():
		return finviz.get_news(ticker)

	fileCache = cache.get_cache('NEWS', data_folder)
	return fileCache.get(key=ticker, createfunc=response)

def get_analyst_feed(ticker, data_folder):
	def response():
		return finviz.get_analyst_price_targets(ticker)

	fileCache = cache.get_cache('PRICE_ANALYSIS', data_folder)
	return fileCache.get(key=ticker, createfunc=response)

def parse_news(news):
	rendered_news = []
	for article in news:
		rendered_article = {}
		rendered_article['title'] = article[0]
		rendered_article['link'] = article[1]
		rendered_news.append(rendered_article)
	return rendered_news

def build_bar_charts(news, chart_path):
	news_sentiment=[0.0,0.0,0.0,0.0]
	analyzer = SentimentIntensityAnalyzer()

	for article in news:
		scores = analyzer.polarity_scores(article)
		news_sentiment[0] += scores['neg'] 
		news_sentiment[1] += scores['neu'] 
		news_sentiment[2] += scores['pos'] 
		news_sentiment[3] += scores['compound'] 

	# Use sentiment data to create a bar chart
	news_sentiment_labels=['Negative', 'Neutral', 'Positive', 'Mixed']

	plt.style.use('ggplot')
	plt.bar([i for i, _ in enumerate(news_sentiment)], news_sentiment, color='yellow')
	plt.xlabel("Sentiment")
	plt.ylabel("Polarity Scores")
	plt.title("News Feed Sentiment Analysis")
	plt.xticks([i for i, _ in enumerate(news_sentiment_labels)], news_sentiment_labels)
	plt.savefig(chart_path)
	plt.close()