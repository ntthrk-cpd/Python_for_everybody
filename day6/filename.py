import shutil
import os 
from pathlib import Path 
import send2trash # ลบไฟล์ไปเก็บในถังขยะ

# สร้างโฟลเดอร์
os.mkdir('./test')

# ดูว่ามีโฟลเดอร์อะไรบ้าง ไฟล์อะไรบ้าง
os.listdir()

# หา home folder
# ถ้าระบบปฏิบัติการไม่เหมือนกัน path ที่ได้จะไม่เหมือนกัน 
Path.home()

# join path
os.path.join(Path.home(), 'test')


# copy file
shutil.copy('test.txt', 'test2.txt')

#เปลี่ยนชื่อ หรือย้ายที่
shutil.move('test2.txt', 'test3.txt')
os.mkdir('move')
shutil.move('test3.txt', os.path.join('move', 'test3.txt'))

# ลบไฟล์ (ลบเข้าถังขยะ)
send2trash.send2trash('test.txt')
