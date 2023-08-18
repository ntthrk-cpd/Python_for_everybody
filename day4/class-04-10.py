global_val = 1234
global_val2 = 4567

def func():
    global global_val
    #global_val = 1
    print(f'inside: {global_val=}')

def func2():
    global global_val2
    #global_val2 = 2
    print(f'inside : {global_val2=}')

# def func3(): # ไม่มี global จะเป็นการสร้างตัวแปรใหม่ ใน scope ของ func3   
def func3(some_val): # ไม่มี global จะเป็นการสร้างตัวแปรใหม่ ใน scope ของ func3 
    global_val2 = 3
    print(f'inside : {global_val2=}')

func()
func2()
func3()
print(f'{global_val=}')
print(f'{global_val2=}')
