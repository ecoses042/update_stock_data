from constant import *

    #search for 20 day range data exists
    # if not found, set value to closest normalized_data
    # if found, apply z-score to argument date row
    # make change to excel file
def normalize_data(stock_name, date):
    original_data = pd.read_excel(file_path, sheet_name=stock_name)

    # selcect row with a given date
    #current_date_row_index = original_data.loc[original_data['date'] == date].index
    #print(current_date_row_index)

    #check if value pool is available and if not, find closest normalized_data

test_data = pd.read_excel(file_path, sheet_name=stock_names[0])
print(test_data['date'])
#normalize_data(stock_names[0], date)
