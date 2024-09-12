
import pandas as pd
import numpy as np
import yfinance as yf
import xlsxwriter as xlsx
import openpyxl
import os
import statistics
from sklearn.preprocessing import StandardScaler
from datetime import date
from get_info import *
from get_start_date import *
from init_stock_data import *
from update_stock_data import *
file_path = 'stock_data.xlsx'

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
	# remomve duplicate data
	data = data.dropna()
	data = data.drop(columns = ['Open','Adj Close'])
	data = data.iloc[::-1]

	
	# write to excel file
	with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
		data.to_excel(writer, sheet_name=stock_name, index=True)
	if 'Sheet1' in file_path:
		del file_path['Sheet1']