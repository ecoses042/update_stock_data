

def get_rsi(data, window=14):
	delta = data['Close'].diff()
	loss = delta.copy()
	gains = delta.copy()
	loss[loss > 0] = 0
	gains[gains < 0] = 0
	avg_gain = gains.rolling(window=14).mean()
	avg_loss = loss.rolling(window=14).mean()
	rs = avg_gain / abs(avg_loss)
	rsi = 100 - (100 / (1 + rs))
	return rsi
	# calculate sum of  close price - close price of day before(average gain)
	# (average loss) sum of prev close price - close price
#MACD
def get_macd(data):
	macd = data['short_avg'] - data['med_avg']
	return macd