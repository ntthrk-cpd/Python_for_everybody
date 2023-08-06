# for loop 

my_string = "Hello world"
fruits_box: list[str]= ["apple", "banana", "cherry"]

for fruit in fruits_box:
    print("ผลไม้:", fruit)

# for i in [1, 2, 3, 4]:
for i in range(1, 5):
   print(i)

# range(1, 10) แปลว่า 1 ถึง 9
for i in range(1, 10):
    if i == 3:
        print("skipping!") # เจอ 3 ข้ามไป
        continue
    print(i)

for i in range(1, 10):
    if i == 3:
        print("skipping!") # เจอ 3 หยุดการทำงาน
        break
    print(i)

# range(10, 0, -1) แปลว่า 10 ถึง 1 โดยลดลงทีละ 1
for i in range(10, 0, -1):
    if i == 3:
        print("skipping!")
        continue
    print(i)

# for loop ใช้งานได้ดีกว่า while loop เพราะ while loop จะมีโอกาสติด loop Infinity มากกว่า for loop และ for loop ใช้งานง่ายกว่า while loop ด้วย 