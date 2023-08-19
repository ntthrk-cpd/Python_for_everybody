'''
การเปิด service account
For Bots: Using Service Account
A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs [sic].

Since it’s a separate account, by default it does not have access to any spreadsheet until you share it with this account. Just like any other Google account.

Here’s how to get one:

Enable API Access for a Project if you haven’t done it yet.

Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.

Fill out the form

Click “Create” and “Done”.

Press “Manage service accounts” above Service Accounts.

Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”.

Select JSON key type and press “Create”.

You will automatically download a JSON file with credentials. It may look like this:

เปิด API ด้วย ลองยิง request ดูแล้ว google จะแจ้งเตือนเองว่าลืมเปิดอะไรบ้าง
'''
#############################################
# ใช้งาน google sheet ด้วย gspread
# ต้องสร้าง service account ก่อน
# แล้ว share google sheet ให้ service account นั้น
# แล้วเปิด google sheet api ให้ service account นั้นด้วย
# แล้วสร้าง key.json ให้ service account นั้น
# แล้วใช้งานได้
# dnuttest@gm 
#############################################
import gspread

# gc = gspread.service_account(filename='grounded-tine-396404-c98b6782ae12.json')
gc = gspread.service_account('grounded-tine-396404-c59ac431a7a1.json')
# sh = gc.open("MyNewSheet")

# sh.sheet1.get('A1') # แสดงค่าใน cell A1 ของ sheet1
# sh.sheet1.update('A1', [[1, 2], [3, 4]]) # ใส่ค่า 1,2 และ 3,4 ลงใน cell A1 ของ sheet1
# sh.sheet1.append_row([1, 2, 3, 4]) # ใส่ค่า 1,2,3,4 ลงใน row ต่อจากข้อมูลเดิม ของ sheet1 

