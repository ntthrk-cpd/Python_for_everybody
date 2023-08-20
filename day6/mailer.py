# เปิด gmail Setting > Forwarding and POP/IMAP > Enable IMAP
# import smtplib

# smtp = smtplib.SMTP('smtp.gmail.com', 587)
# smtp.ehlo()
# smtp.starttls()
# smtp.login('dnuttest@gmail.com', 'dnuttest1234')
'''
####################################################
###### send mail with api sendinblue (brevo) #######
####################################################

ไม่ต้องเปิด IMAP แต่ต้องเปิด less secure app access ใน gmail ก่อน 
และต้องเปิด 2FA ก่อน แล้ว generate app password มาใช้ 
แล้วใส่ในตัวแปร password แทน รหัสผ่านของ gmail ตัวเอง และใส่ email ที่ต้องการส่งในตัวแปร to_email แทน 
email ของตัวเอง และใส่ email ที่ใช้สร้าง app password ในตัวแปร from_email แทน email ของตัวเอง 
และใส่ app password ในตัวแปร password แทน รหัสผ่านของ gmail ตัวเอง 
****ต้องมี domain ของตัวเองในต้อนสมัคร brovo ด้วย และต้องยืนยัน domain ก่อนใช้งาน 
ไปหน้า smapi ของ brovo แล้วกด verify domain แล้วใส่ domain ของตัวเอง แล้วกด verify แล้วจะได้ api key มาใช้
ติดตั้ง sib-api-v3-sdk 7.6.0  ก่อนใช้งาน pip install sib-api-v3-sdk
'''
'''
import sib_api_v3_sdk
form sib_api_v3_sdk.rest import ApiException
from pprint import pprint


sib_api_v3_sdk.configuration.api_key['api-key'] = 'your Key'
api_instance = sib_api_v3_sdk.TransactionalEmailsApi()
email_compaigns = sib_api_v3_sdk.CreateEmailCampaign(
name = "Campaign sent via the API"
subject = "My subject"
sender = {"name":"From name","email":"dnuttest@gmail.com"}
html_content = "Congratulations! You successfully sent this example campaign via the Sendinblue API."
recipients = {"listIds":[2,7],},
scheduled_at= "2018-01-01 00:00:01"
)
try:
    api_response = api_instance.send_transac_email(email_compaigns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
####################################################
###### send mail with api sendinblue (brevo) #######
####################################################
'''