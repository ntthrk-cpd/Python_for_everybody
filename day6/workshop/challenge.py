# ให้สร้างไฟล์ .txt 5 ไฟล์ ชื่อไฟล์อะไรก็ได้ หลังจากนั้นให้เปลี่ยนชื่อไฟล์ให้ตามหน้าด้วย 0_ชื่อไฟล์ .. 1_ ชื่อไฟล์ ...

import shutil
import os 
from pathlib import Path 



os.mkdir('./test')
path_test = os.path.join(Path.home(), 'test')
# สร้างไฟล์ .txt

i = 0
for i in range(5):
    with open(path_test + f'/test{i}.txt', 'w') as f:
        i += 1
# แสดงไฟล์ทั้งหมดในโฟลเดอร์ test
os.listdir(path_test)
# เปลี่ยนชื่อไฟล์
for i in range(5):
    #os.rename(f'./test/test{i}.txt', f'./test/{i}_test{i}.txt')
    shutil.move(path_test + f'/test{i}.txt', path_test + f'/{i}_test{i}.txt')
    i += 1
# แสดงไฟล์ทั้งหมดในโฟลเดอร์ test
os.listdir('./test')


