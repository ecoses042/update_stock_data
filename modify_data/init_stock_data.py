import pandas as pd
import numpy as np
import yfinance as yf
import xlsxwriter as xlsx
from modify_data.get_info import trend
from modify_data.get_info import get_rsi, get_macd
from modify_data.get_start_date import modify_date

# init_stock_data(stock name, start date, end date)
# will add new sheet to stock_data with stock name as name


def init_stock_data(stock_name, start_date, end_date):
	data = yf.download(stock_name, start=start_date, end=end_date)
	data.index = data.index.date
	data.index.name = 'date'
	# 이동 평균 계산
	data['short_avg'] = data['Close'].rolling(window=20).mean()
	data['med_avg'] = data['Close'].rolling(window=60).mean()
	data['long_avg'] = data['Close'].rolling(window=120).mean()

	# add RSI
	data['rsi'] = get_rsi(data)
	# add MACD
	data['macd'] = data.apply(get_macd, axis = 1)
	data['signal'] = data['macd'].rolling(window=9).mean()
	data['macd_oscillator'] = data['macd'] - data['signal']
	# remomve duplicate data
	data = data.dropna()
	data = data.drop(columns = ['Open','Adj Close'])
	data = data.iloc[::-1]

	

	# write to excel file
	with pd.ExcelWriter('stock_data.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
		data.to_excel(writer, sheet_name=stock_name, index=True)
	