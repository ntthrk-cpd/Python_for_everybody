import random

def get_random_number():
    """
        func คนอื่นเขียนมาแล้วแก้ไม่ได้ ใช้ได้เท่านั้น
    """
    return random.randint(1, 100)

random_number = get_random_number()
print(random_number)
# if random_number <= 50:
#     raise ValueError("random number is too small")
if random_number == 0:
    raise ValueError("Cannot be zero") 
# raise คือการโยน error ขึ้นไปให้คนที่เรียกใช้งาน function นี้จัดการต่อ โดยจะเข้าไปทำงานใน except ของคนที่เรียกใช้งาน function นี้   

# ทำงานอื่นตรงนี้ไปอีกหลายบรรทัด

result = 10 / random_number

# ทำงานอื่นตรงนี้ไปอีกหลายบรรทัด

print(result)