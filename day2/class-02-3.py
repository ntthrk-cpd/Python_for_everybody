# Loop
# while loop
"""
while loop ตรวจสอบ candition ก่อน ถ้าเป็นจริงจะทำงาน ถ้าเป็นเท็จจะไม่ทำงาน
"""
num = 2
while num > 0:
    print("num:", num)
    num: int = num - 1

# continue คือ การข้ามไปทำงานบรรทัดถัดไป
num = 5
while num > 0:
    if num == 3:
        num: int = num - 1
        print("เจอ 3 ข้ามไป")
        continue
    num: int = num - 1
    print("hello")

# break คือ การหยุดการทำงานของ loop
num = 5
while num > 0:
    if num == 3:
        num: int = num - 1
        print("เจอ 3 หยุดการทำงาน")
        break
    num: int = num - 1
    print("hello")