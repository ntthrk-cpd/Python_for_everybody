# ให้สร้างไฟล์ .txt 5 ไฟล์ ชื่อไฟล์อะไรก็ได้ หลังจากนั้นให้เปลี่ยนชื่อไฟล์ให้ตามหน้าด้วย 0_ชื่อไฟล์ .. 1_ ชื่อไฟล์ ...
import os
import shutil

lsdirs = os.listdir()
count = 0
for file in lsdirs:
    if file.endswith('.txt'):
        shutil.move(file, str(count) + _ + file)
        count += 1
