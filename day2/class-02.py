# Built in functions
## Type casting (แปลงชนิดข้อมูล) str, int, float, bool
### example 
my_string = '123'
my_int = int(my_string)
my_float = float(my_string)
print("int: ", my_int,"","float:", my_float)
my_new_string = str(my_int)
print("str: ", my_new_string)

# Flow control
## โปรแกรมทำงานจากบนลงล่าง และจากซ้ายไปขวา

## boolean (True, False )
## Keyword คือ คำที่มีความหมายพิเศษ ใช้ในการเชียนโปรแกรม ไม่สามารถใช้เป็นชื่อตัวแปรได้
my_bool = True
my_other_bool = False
print("my_bool: ", type(my_bool))
print("my_bool: ", my_bool)
## Comparison operators
### >, <, >=, <=, ==, !=
### ใช้ได้กับทุกชนิดข้อมูล
1 > 0 # True
1 < 0 # False
1 >= 0 # True
1 <= 0 # False
1 == 0 # False
1 != 0 # True
a = '5' 
b = '5'
a != b # False
a == b # True
c = 5
b == c # True
age = 19
is_age_more_than_18: bool = age > 18
print("age_more_than_18: ", is_age_more_than_18) # True
## Truth table (and, or, not)
### and จะเป็น True เมื่อทั้งสองข้างเป็น True
### or จะเป็น True เมื่ออย่างน้อย 1 ข้างเป็น True
### not จะเป็น True เมื่อข้างหน้าเป็น False
print("True and True: ", True and True) # True
print("True and False: ", True and False) # False
print("False and True: ", False and True) # False
print("False and False: ", False and False) # False
is_age_more_than_18: bool = age > 18
is_age_less_than_20: bool = age < 20
print("Are you between 18 and 20?: ", is_age_more_than_18 and is_age_less_than_20) # True
print("True or True: ", True or True) # True
print("True or False: ", True or False) # True
print("False or True: ", False or True) # True
print("False or False: ", False or False) # False
# กลับด้าน bloolean
print("not True: ", not True) # False
print("not False: ", not False) # True
# boolean expression
(1 > 0) and (2 > 1) # True
(1 > 0) and (2 < 1) # False
(1 < 0) and (2 > 1) or (1 > 0) # True
