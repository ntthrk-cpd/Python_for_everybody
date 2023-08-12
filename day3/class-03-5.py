# เขียน function อ่านไฟล์ชื่อ input.txt แล้วแสดงผลออกมาทางหน้าจอ

def read_file():
    with open('input.txt', 'r') as file: 
        return file.read()
'''
    ใช้ with เพื่อป้องกันลืมปิดไฟล์ และใช้ r เพื่ออ่านไฟล์ 
    ใช้ as เพื่อตั้งชื่อตัวแปร file ให้เป็นตัวแทนของไฟล์ 
    ใช้ file.read() เพื่ออ่านไฟล์ 
    return ค่าที่ได้ ออกมา 
'''
