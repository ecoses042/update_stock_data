import openpyxl

def get_start_date(stockname):
    workbook = openpyxl.load_workbook('stock_data.xlsx')
    sheet = workbook[stockname]
    start_date = sheet['A2'].value
    start_date = str(start_date)[0:10]
    return start_date