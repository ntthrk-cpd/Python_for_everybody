# dictionary
'''
 เหมือนกล่องใส่ของ มี key และ value ในกล่อง
 ซึ่ง key จะเป็นตัวเลขหรือ string และ value จะเป็นอะไรก็ได้
    แต่ key จะไม่ซ้ำกัน
    และ value สามารถซ้ำกันได้
'''

pet_1 = {
    "name": "จอห์น",
    "kind": "แมว",
    "legs": 4,
    "ears": 2
}

pet_1["name"]
pet_1["kind"]
pet_1["legs"]
pet_1["ears"]

pet_1["age"] # ถ้าเราเรียกใช้ key ที่ไม่มีอยู่จะเกิด error
pet_1["age"] = 3 # เพิ่ม key ใหม่เข้าไปใน dictionary
pet_1["age"] # ถ้าเราเรียกใช้ key ที่ไม่มีอยู่จะเกิด error
del pet_1["age"] # ลบ key ออกจาก dictionary
pet_1["age"] # ถ้าเราเรียกใช้ key ที่ไม่มีอยู่จะเกิด error

for key, value in pet_1.items():    # วนลูปเพื่อแสดง key และ value ทั้งหมดใน dictionary
                                    # [("name", "จอห์น"), (key, "value), ...)]
    print(key, value) # แสดง key และ value ทั้งหมดใน dictionary ออกมา โดยแสดงทีละคู่ ตัวอย่าง: name จอห์น

paragraph = "The quick brown fox jumps over the lazy dog"

paragraph.split(" ") # แยกคำใน paragraph ออกมาเป็น list โดยแยกตามช่องว่าง ตัวอย่าง: ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
# print(paragraph.split())

# in operator เช็คดูว่ามีอยู่ใน list หรือไม่
my_list = [1, 2, 3, 4]
4 in my_list # ตรวจสอบว่า 4 อยู่ใน my_list หรือไม่ โดยใช้ in operator ซึ่งจะ return True หรือ False ถ้ามี return True ถ้าไม่มี return False
5 in my_list 
my_dictionarioes = {"a": 1, "b": 2, "c": 3}
"a" in my_dictionarioes
"X" in my_dictionarioes

