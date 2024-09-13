from constant import *
import os

def init_excel_file():
    if not os.path.exists('stock_data.xlsx'):
        workbook = xlsx.Workbook('stock_data.xlsx')
        workbook.close()
#init_stock_data(stock_name, start_date, end_date)

# check for sheet name with stock_name
# if found, get start_date from that sheet
# if not found, init_date with fixed start_date of 2020-01-01
end_date = date.today()
init_excel_file()
workbook = openpyxl.load_workbook(file_path)
for stock_name in stock_names:
    if stock_name in workbook.sheetnames:
        print(f"'{stock_name}' 시트가 존재합니다.")
        start_date = get_start_date(stock_name)
        # update data
    else:
        print(f"'{stock_name}' 시트가 존재하지 않습니다.")
        # init data
    # while end of file, call normalize_data in descending order
