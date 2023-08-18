import httpx

# r = httpx.get("https://www.google.com")
# print(r.text)
######################

# r = httpx.get("https://httpbin.org/status/400", timeout=60)
# if r.status_code not in [200, 201, 202, 203, 204, 205, 206]:
#     print("Error")
#     exit()
######################

def call_func(): 
    """
    random ฟังก์ชั่นที่สุ่มค่าออกมา ว่าพังหรือไม่พัง
    """
    random.choice([1, 'one']) # 1 -> ok, 'one' -> not ok 
    int('five')
    return {'status': 'ok'}

print('start program')
try: # จะทำงานใน try ถ้าไม่ error จะไม่เข้า except
    respond = call_func()
except ValueError as e: # ถ้า error จะเข้ามาทำงานใน except นี้
    respond = {'status' : 0}
finally:
    print('finally')
# try: # จะทำงานใน try ถ้าไม่ error จะไม่เข้า except
#     respond = call_func()
# except ValueError as e: # ถ้า error จะเข้ามาทำงานใน except นี้
#     respond = {'status' : 'not ok'}
# finally: # ไม่ว่าจะ error หรือไม่ก็ตามจะทำงานใน finally ก่อนจะออกจาก function นี้ 
#     print('from finally')
print(respond['status'])
print('end program')