import pandas as pd
import numpy as np
import yfinance as yf
import xlsxwriter as xlsx
from init_data.get_trend import trend

# init_stock_data(stock name, start date, end date)
# will add new sheet to stock_data with stock name as name


def init_stock_data(stock_name, start_date, end_date):
	data = yf.download(stock_name, start=start_date, end=end_date)
	# 이동 평균 계산
	data['short_avg'] = data['Close'].rolling(window=20).mean()
	data['med_avg'] = data['Close'].rolling(window=60).mean()
	data['long_avg'] = data['Close'].rolling(window=200).mean()
	# remomve duplicate data
	data = data.dropna()
	data = data.drop(columns = ['Open', 'High', 'Low', 'Adj Close'])
	data = data.iloc[::-1]

	# 이동평균에 따른 추세 추가
	data['trend'] = data.apply(trend, axis = 1)
	with pd.ExcelWriter('stock_data.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
		data.to_excel(writer, sheet_name=stock_name)
	
	