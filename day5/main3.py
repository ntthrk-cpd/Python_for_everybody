# conda install -c conda-forge gspread
# pip install gspread from https://pypi.org/project/gspread/
# Create credentials in Google API Console
# https://console.developers.google.com/apis/credentials
# https://docs.gspread.org/en/v5.10.0/


# copy key.json to Python_for_everybody/day5/workshop
# Enable Google Drive API on chome Browser
# goto google sheet and share with service account email
# Enable Google Sheets API on chome Browser

import gspread

gc = gspread.service_account(filename='key.json')
sh = gc.open("MyNewSheet")

sh.sheet1.get('A1') # แสดงค่าใน cell A1 ของ sheet1
sh.sheet1.update('A1', [[1, 2], [3, 4]]) # ใส่ค่า 1,2 และ 3,4 ลงใน cell A1 ของ sheet1
sh.sheet1.append_row([1, 2, 3, 4]) # ใส่ค่า 1,2,3,4 ลงใน row ต่อจากข้อมูลเดิม ของ sheet1 

