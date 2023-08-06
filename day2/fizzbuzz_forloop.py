num = int(input("Enter your number: "))
for i in range(num, -1, -1):
    if i == 0:
        print("0")
        break
    elif i % 3 == 0 and i % 5 == 0: 
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)