import gspread
import time
import set_connect as sc
import set_data as sd

sh = sc.connect_to_google_sheet()

# input date Description Income Expenses Balance to Google Sheet
def add_data_to_worksheet(data):
    income : float = 0.00
    expenses : float = 0.00
    balance : float = 0.00
    month : str = data[0].strftime("%B")
    worksheet = sh.worksheet("Sheet_" + month)
    date_input : str = data[0].strftime("%d") + "-" + month + "-" + data[0].strftime("%Y")
    if len(sh.worksheet("Sheet_" + month).get_all_values()) > 1:
        balance = float(sh.worksheet("Sheet_" + month).get_all_values()[-1][4])
    else:
        balance = 0.00
    if data[1] in sd.description_list_income:
        income = data[2]
    elif data[1] in sd.deprecation_list_regular_payment:
        expenses = data[2]
    balance = float(balance) + float(income) - float(expenses)
    worksheet.append_row([date_input, data[1], income, expenses, balance])
    pass
