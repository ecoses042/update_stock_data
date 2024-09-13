import numpy as np

init_start_date = '2020-01-01'
stock_names = ['^GSPC', 'AAPL']
file_path = 'stock_data.xlsx'
columns_to_normalize = ['High', 'Low', 'Close', 'Volume', 'short_avg', 'med_avg', 'long_avg', 
                            'rsi', 'macd']
value_placeholder = np.nan