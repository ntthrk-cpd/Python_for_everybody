# create dummy Income_and_Expenses_Account data between 01/01/2023-present to google sheet
# Create file name is Income_and_Expenses_Account on google sheet and assign email from json to share
###########################################################################################
## import library
import gspread 
import time
import random

###########################################################################################
## connect to google sheet
gc = gspread.service_account(filename='./json/grounded-tine-396404-c1b582e331cc.json')
sh = gc.open("Income_and_Expenses_Account")
###########################################################################################
## set variable
month_list : list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
header_list : list = ["Date", "Description", "Income", "Expenses", "Balance"]
Description_list_income : list = ["Salary", "Extra Income", "Income Other"]
Deprecation_list_regular_payment : list = ["Rent", "Electricity", "Water", "Internet", "Phone"]
Description_list_expenditure : list = ["Food", "Transportation", "Education", "Health", "Entertainment", "Expenditure Other"]
###########################################################################################
## test connect to google sheet
# worksheet = sh.sheet2
# print(worksheet.get('A1'))
###########################################################################################
## create worksheet for each month
# for month in month_list:
#     try :
#         worksheet = sh.add_worksheet(title="Sheet_" + month, rows="100", cols="20")
#     except gspread.exceptions.APIError as e:
#         print("Error:", str(e))
#         raise SystemExit(e)
#     pass
# print all worksheet
# worksheet_list = sh.worksheets()
# print(worksheet_list)
###########################################################################################
## delete worksheet sheet1
# sh.del_worksheet(sh.sheet1)
###########################################################################################
## add hearer to each worksheet
# for worksheet in worksheet_list:
#     try :
#         worksheet.update('A1:E1', [["Date", "Description", "Income", "Expenses", "Balance"]])
#     except gspread.exceptions.APIError as e:
#         print("Error:", str(e))
#         raise SystemExit(e)
#     pass
# #print hearer of each worksheet
# for worksheet in worksheet_list:
#     print(worksheet.get('A1:E1'))
#     pass
###########################################################################################
## add dummy data to each worksheet but error gspread.exceptions.APIError: code: 429
'''
    add data each colum add date of day by date between date 01/01/2023-present 
    and if salary,extra income add income and if other add expenses
'''
day_now = time.strftime("%d") # day now
month_now = time.strftime("%B") # month now
worksheet_list = sh.worksheets() # get all worksheet
salary : float = 15000.00 # set salary
balance_all : float = 0 # balance from the previous month
for worksheet in worksheet_list: # loop all mouth in worksheet_list 
    day : int = 1 # set day of day start 1
    mouth : str = worksheet.title.split("Sheet_")[1] # get month of worksheet now
    column : int = 2 # set column input start 2
    print(f'mouth_sheet_now: {mouth}') # print month of worksheet now for check
    random_range = random.randint(10, 40) # random range of input data each month
    # loop input date day 1-31 each month have random_range
    while (column <= random_range):
        sleep_time = random.randint(1, 5) # random sleep time
        time.sleep(sleep_time) # sleep time
        print(f'sleep_time: {sleep_time}') # print sleep time for check
        print(f'column: {column}') # print column for check
        print(f'random_range: {random_range}') # print random_range for check
        if day > 31:
            continue
        set_date = f"{day}-{mouth}-2023"
        #set first date of each month
        if day == 1:
            # input balance from the previous month
            worksheet.update_cell(column, 1, set_date) # date
            worksheet.update_cell(column, 2, "Balance from the previous month") # description
            worksheet.update_cell(column, 3, balance_all) # income
            worksheet.update_cell(column, 4, 0) # expenses
            worksheet.update_cell(column, 5, balance_all) # balance is equal to the balance from the previous month
            column += 1
            # input salary
            worksheet.update_cell(column, 1, set_date) # date
            worksheet.update_cell(column, 2, "Salary") # description
            worksheet.update_cell(column, 3, salary) # income
            worksheet.update_cell(column, 4, 0) # expenses
            balance_all += salary
            worksheet.update_cell(column, 5, balance_all) # balance is equal to the balance from the previous month
            column += 1
            # input regular payment
            for D_reg_p in Deprecation_list_regular_payment:
                time.sleep(6)
                pay : float = 0
                worksheet.update_cell(column, 1, set_date)
                worksheet.update_cell(column, 2, D_reg_p)
                worksheet.update_cell(column, 3, 0)
                if (D_reg_p == "Rent"):
                    pay = 3000
                elif (D_reg_p == "Electricity"):
                    pay = random.randint(300, 1000)
                elif (D_reg_p == "Water"):
                    pay = random.randint(100, 500)
                elif (D_reg_p == "Internet"):
                    pay = 400
                elif (D_reg_p == "Phone"):
                    pay = 300
                worksheet.update_cell(column, 4, pay)
                balance_all -= pay
                worksheet.update_cell(column, 5, balance_all)
                column += 1
        # random input income or expenditure
        rd = random.randint(1, 3)
        i = 0
        while (i < rd):
            worksheet.update_cell(column, 1, set_date)
            random_input = random.randint(1, 10) # random input income or expenditure
            ds : str = ""
            if random_input <= 2: #extra income or income other
                ds = Description_list_income[random.randint(0, 2)]
                income : float = random.randint(100, 3000)
                worksheet.update_cell(column, 3, income)
                worksheet.update_cell(column, 4, 0)
                balance_all += income
            else : #expenditure or expenditure other
                ds = Description_list_expenditure[random.randint(0, 5)]
                expenditure : float = random.randint(100, 3000)
                worksheet.update_cell(column, 3, 0)
                worksheet.update_cell(column, 4, expenditure)
                balance_all -= expenditure
            print(f'description: {ds}')
            worksheet.update_cell(column, 2, ds)
            worksheet.update_cell(column, 5, balance_all)
            column += 1
            i += 1
        if mouth == month_now and day_now == day:
            break
        day += 1
    # next worksheet
    pass
###########################################################################################
