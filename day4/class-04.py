from rich import print

# back to strings
some_string = "Hello World"
some_more_string = 'Hello World!'
long_string = """Hello 
Hello World!
Long 
""" 
string_with_newline = "Hello\nWorld"
single_quote_string = 'John\'s cat'
double_quote_string = "John's cat"
more_double_quote_string = "John said \"Hello\""
# \t: tab, \n: newline, \r: carriage return, \b: backspace, \f: form feed 
# string เป็น list-like
my_new_string = "Hello World1234"
print(my_new_string[0])
print(my_new_string[1])
print(my_new_string[2])
for charactor in my_new_string:
    print(charactor)
my_new_string[0:5] # 0, 1, 2, 3, 4
my_new_string[:5] # 0, 1, 2, 3, 4
my_new_string[-1:] # 12 ตัวสุดท้าย
my_new_string[5:] # ตัวที่ 5 ถึงตัวสุดท้าย
"hello" in my_new_string # True เช็คว่ามีคำว่า hello ใน my_new_string ไหม
"Hello" in my_new_string # False เพราะว่าเป็น case sensitive
"Hello" + "World" # Hello World
# f-string
name = "John"
age = 20
f"Hello {name}, you are {age} years old" 
f"Hello {name}, next year you will be {age+1} years old"
""" 
    อะไรที่แปลงเป็น string ได้ก็ใส่ได้ไม่จำเป็นต้องเป็นตัวแปร 
    แต่ต้องเป็น object ที่สามารถแปลงเป็น string ได้ 
    และใส่ {} ไว้ และใส่ f ไว้หน้า string ด้วย 
"""
symbol = "BTC"
price = 10000000.123456789
f"Symbol: {symbol}, Price: {price:.2f}" # format ทศนิยม 2 ตำแหน่ง

# string methods
some_more_string = "hello world"
my_new_string.upper() # HELLO WORLD
my_new_string.lower() # hello world
my_new_string.capitalize() # Hello world
my_new_string.title() # Hello World
my_new_string.swapcase() # hELLO wORLD
my_new_string.count("l") # 3
my_new_string.find("l") # 2 หาตัวแรกที่เจอ
my_new_string.rfind("l") # 9 หาตัวสุดท้ายที่เจอ
my_new_string.index("l") # 2 หาตัวแรกที่เจอ
my_new_string.rindex("l") # 9 หาตัวสุดท้ายที่เจอ
my_new_string.startswith("H") # True
my_new_string.endswith("d") # True
my_new_string.isalnum() # False เพราะว่ามี space
my_new_string.isalpha() # False เพราะว่ามี space
my_new_string.isdecimal() # False เพราะว่ามี space
my_new_string.isdigit() # False เพราะว่ามี space
my_new_string.isidentifier() # False เพราะว่ามี space
my_new_string.islower() # True
my_new_string.isnumeric() # False เพราะว่ามี space
my_new_string.isprintable() # True
my_new_string.isspace() # False เพราะว่ามี space
my_new_string.istitle() # False เพราะว่ามี space
my_new_string.isupper() # False เพราะว่ามี space
my_new_string.replace("l", "L") # HeLLo WorLd1234
my_new_string.replace("l", "L", 1) # HeLlo World1234
my_new_string.split() # ['Hello', 'World1234']
my_new_string.split("l") # ['He', '', 'o Wor', 'd1234']
my_new_string.splitlines() # ['Hello World1234']
my_new_string.strip() # ตัด space หน้า-หลัง
my_new_string.rstrip() # ตัด space ทางขวา
# ETC.

# heLlo world -> HELLO WORLD -> True
my_new_string.upper().isupper() # การ chain method

# basic check
all_alphabets = "abcdefghijklmnopqrstuvwxyz"
all_numbers = "0123456789"
all_alphabets.isalpha() # True
all_numbers.isnumeric() # True
all_numbers.isnumeric() # False
all_alphabets.isnumeric() # False
new_string = all_alphabets + all_numbers
new_string.isalnum() # True เป็นอักษรหรือตัวเลขทั้งหมด

# เริ่มด้วย ลงท้ายด้วย แยกคำ
hashtags = "#python #programming #coding #python $cat $dog"
claned_hashtags = []
for hashtag in hashtags.split():
    if hashtag.startswith("#"):
        print(hashtag)
        claned_hashtags.append(hashtag)
claned_hashtags # ['#python', '#programming', '#coding']

hello_in_other_languages = "HALA!"
hello_in_other_languages.endswith("!") # True

# split
"Hello World".split() # ['Hello', 'World'] แยกด้วย space
"#python, #programming, #coding".split(",") # ['#python', ' #programming', ' #coding'] แยกด้วย ,

# join
list_of_hashtags = ["#python", "#programming", "#coding"]
", ".join(list_of_hashtags) # '#python, #programming, #coding' (รวมด้วย , และเว้นวรรค 1 ช่อง)

# stripping
"   Hello World   ".strip() # 'Hello World' ตัด space หน้า-หลัง
"   Hello World   ".rstrip() # '   Hello World' ตัด space ทางขวา
"   Hello World   ".lstrip() # 'Hello World   ' ตัด space ทางซ้าย
