#############################################
# ใช้งาน google sheet ด้วย gspread
# สร้าง service account
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
# Enable Google cloud platform API 
# Enable Google Sheets API
# แล้วสร้าง key.json ให้ service account นั้น
# share google sheet ให้ service account (copy client_email ในไฟล์ key.json อนุญาติสิทธิ์ใน google sheet นั้น)
# dnuttest@gm 
#############################################
import gspread

gc = gspread.service_account('/home/ntthrk-ch/Documents/Ntthrk_UBUNTU/LearningSkill/Python/Python_for_everybody/day5/workshop/grounded-tine-396404-6fff91441d97.json')
sh = gc.open("MyNewSheet")
sh.sheet1.get('A1')

