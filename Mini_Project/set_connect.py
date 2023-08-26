import gspread

def connect_to_google_sheet():
    gc = gspread.service_account(filename='./json/grounded-tine-396404-9681e8bfdff7.json')
    sh = gc.open("Income_and_Expenses_Account")
    return sh