import yfinance as yf
import numpy as np
import openpyxl
import pandas as pd
from constant import *
from func_average import *
#using yfinance, create new sheet with stock_name 
#fill with data from starting date to end date
def get_init_data(stock_name, end_date):
    data = yf.download(stock_name, start=init_start_date, end=end_date)

    #calculate moving average
    data['short_avg'] = data['Close'].rolling(window=20).mean()
    data['med_avg'] = data['Close'].rolling(window=60).mean()
    data['long_avg'] = data['Close'].rolling(window=120).mean()

    # add RSI
    data['rsi'] = get_rsi(data)
	# add MACD
    data['macd'] = data.apply(get_macd, axis = 1)

    # add normalized value using z-score
    
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        data.to_excel(writer, sheet_name=stock_name, index=True)
    if 'Sheet1' in file_path:
    	del file_path['Sheet1']