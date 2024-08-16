import pandas as pd
import numpy as np
import yfinance as yf
import xlsxwriter as xlsx
from modify_data.get_info import trend
from modify_data.get_info import get_rsi
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
	data['long_avg'] = data['Close'].rolling(window=200).mean()

	# 이동평균에 따른 추세 추가
	data['trend'] = data.apply(trend, axis = 1)
	# add RSI
	data['rsi'] = get_rsi(data)
	# add MACD
	
	# remomve duplicate data
	data = data.dropna()
	data = data.drop(columns = ['Open','Adj Close'])
	data = data.iloc[::-1]

	

	# write to excel file
	with pd.ExcelWriter('stock_data.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
		data.to_excel(writer, sheet_name=stock_name, index=True)
	