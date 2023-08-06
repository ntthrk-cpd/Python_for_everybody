'''
## FizzBuzz fizzbuzz.py
- [] รับค่าด้วย input() เป็นตัวเลข
- [] พิมพ์ตัวเลขที่รับเข้ามา จนถึง 0
- [] ถ้าเลขหาร 3 ลงตัว ให้พิมพ์ Fizz แทนที่จะพิมพ์ตัวเลข
- [] ถ้าเลขหาร 5 ลงตัว ให้พิมพ์ Buzz แทนที่จะพิมพ์ตัวเลข
'''

num = int(input("Enter your number: "))
while num >= 0:
    if num == 0:
        print("0")
        break
    elif num % 3 == 0 and num % 5 == 0: 
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
    num: int = num - 1