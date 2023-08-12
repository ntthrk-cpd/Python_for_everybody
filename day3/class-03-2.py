# function 
'''
คือ การเขียนโปรแกรมแบบย่อย โดยจะมี input และ output และมีการเรียกใช้งานซ้ำๆได้ โดยจะมีรูปแบบดังนี้  
def ชื่อฟังก์ชัน(ตัวแปร input) -> ตัวแปร output:
    คำสั่งต่างๆ
    return ตัวแปร output
'''
# เขียน fuction บวกเลข a, b
def add(a, b):
    result = a + b
    '''
    บวกเลข a, b แล้วคืนค่าออกมาเป็น result
    '''
    return result

def subtract(a, b):
    """
    ลบเลข a, b แล้วคืนค่า a - b
    """
    print("a = ", a)
    print("b = ", b)
    return a - b

# add(5, 7) # การเรียกใช้งาน function
subtract(5, 7)

'''
library : https://docs.python.org/3/library/index.html
'''