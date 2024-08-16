import pandas as pd
import numpy as np
import yfinance as yf
import xlsxwriter as xlsx
import openpyxl
from modify_data.get_info import trend
from modify_data.get_info import get_rsi
from modify_data.get_start_date import modify_date

#if sheet exists call this function
#read from yfinance
# overlay to the excel file
# close and reopen excel file
# modify the excel data

def update_stock_data(filename, stock_name, start_date, end_date):
    # 새로운 데이터 다운로드
    print(start_date)
    new_data = yf.download(stock_name, start=start_date, end=end_date)
    new_data.index = pd.to_datetime(new_data.index).date

    new_data = new_data.drop(columns=['Open', 'Adj Close'])
    new_data = new_data.iloc[::-1]

    # fill dummy data
    new_data['short_avg'] = pd.NA
    new_data['med_avg'] = pd.NA
    new_data['long_avg'] = pd.NA
    new_data['trend'] = pd.NA
    new_data['rsi'] = pd.NA
    # get old data to merge with new one
    try:
        old_data = pd.read_excel(filename, sheet_name=stock_name, index_col=0)
        old_data.index = pd.to_datetime(old_data.index).date
    except FileNotFoundError:
        old_data = pd.DataFrame()
    
    # merge and set index name
    combined_data = pd.concat([new_data, old_data])
    combined_data.index.name = 'date'
    # reverse to modify
    combined_data = combined_data[::-1]

    #modify cells with dummy data
    combined_data['short_avg'] = combined_data['short_avg'].fillna(combined_data['Close'].rolling(window=20).mean())
    combined_data['med_avg'] = combined_data['med_avg'].fillna(combined_data['Close'].rolling(window=60).mean())
    combined_data['long_avg'] = combined_data['long_avg'].fillna(combined_data['Close'].rolling(window=200).mean())
    combined_data['trend'] = combined_data.apply(
        lambda row: trend(row) if pd.isna(row['trend']) else row['trend'], axis=1
    )
    combined_data['rsi'] = combined_data['rsi'].fillna(get_rsi(combined_data))

    # write the change
    combined_data = combined_data[::-1]
    with pd.ExcelWriter(filename, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        combined_data.to_excel(writer, sheet_name=stock_name)

