
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
# this file contains constant values for modifing data functions
stock_names = ['^GSPC', 'AAPL']
file_path = 'stock_data.xlsx'
columns_to_normalize = ['High', 'Low', 'Close', 'Volume', 'short_avg', 'med_avg', 'long_avg', 
                            'rsi', 'macd']
value_placeholder = np.nan

msg_normalize_complete = "data normalization complete"
normalize_filenotfound = "no file found while executing normalization"
scaler = StandardScaler()

# High
# Low
# Close	
# Volume
# short_avg
# med_avg	
# long_avg
# rsi	
# macd
