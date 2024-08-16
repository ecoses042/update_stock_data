import openpyxl
from datetime import timedelta, datetime
def get_start_date(stockname):
    workbook = openpyxl.load_workbook('stock_data.xlsx')
    sheet = workbook[stockname]
    start_date = sheet['A2'].value
    start_date = str(start_date)[0:10]
    print(start_date)
    date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    start_date = date_obj + timedelta(days=1)
    start_date = str(start_date)[0:10]
    return start_date

def modify_date(row):
    date = str(row)[0:10]
    return date