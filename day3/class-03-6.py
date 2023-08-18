import tomllib
from rich import print

'''
    การเรียกใช้งาน tomllib จาก library tomllib 
    ใช้งานใน python version 3.10 ขึ้นไป 
    แต่ต้องติดตั้ง tomllib ก่อน  ดูวิธีติดตั้งได้ที่ https://pypi.org/project/tomllib/  
'''
# with open("input.toml", "rb") as file:
#     data = tomllib.load(file)

# with open("input.toml", "rb") as file:
#     data = tomllib.load(file)

# print(data)

with open("input.toml", "rb") as f:
    data = tomllib.load(f)

print(data)