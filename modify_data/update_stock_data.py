
from constant import *
#if sheet exists call this function
#read from yfinance
# overlay to the excel file
# close and reopen excel file
# modify the excel data

def update_stock_data(stock_name, start_date, end_date):
    # 새로운 데이터 다운로드
    new_data = yf.download(stock_name, start=start_date, end=end_date)
    new_data.index = pd.to_datetime(new_data.index).date
    new_data = new_data.drop(columns=['Open', 'Adj Close'])
    new_data = new_data.iloc[::-1]

    # fill dummy data
    new_data['short_avg'] = value_placeholder
    new_data['med_avg'] = value_placeholder
    new_data['long_avg'] = value_placeholder
    new_data['rsi'] = value_placeholder
    new_data['macd'] = value_placeholder
    # get old data to merge with new one
    try:
        old_data = pd.read_excel(file_path, sheet_name=stock_name, index_col=0)
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
    combined_data['long_avg'] = combined_data['long_avg'].fillna(combined_data['Close'].rolling(window=120).mean())
    # rsi
    combined_data['rsi'] = combined_data['rsi'].fillna(get_rsi(combined_data))

    # macd
    combined_data['macd'] = combined_data.apply(
        lambda row: get_macd(row) if pd.isna(row['macd']) else row['macd'], axis=1
    )
    # write the change
    combined_data = combined_data[::-1]
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        combined_data.to_excel(writer, sheet_name=stock_name)

    #while data_normalize section is none, call normalize_data with descending date order.
