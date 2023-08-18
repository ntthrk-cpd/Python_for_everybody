from rich import print

def five_divided_by(num):
    result = 5 / converted_num
    print(result)

def main():
    print("เดี๋ยวจะเอาเลขที่คุณให้มาหาร 5 นะ ex. 5 / (เลข)")
    num = int(input("Enter a number: "))

    try:
        converted_num = int(num)
    except ValueError:
        print("ใส่เลขมาให้ถูกต้อง")
        exit() # ออกจากโปรแกรม กรณีที่ใส่เลขไม่ถูกต้อง

    if converted_num == 0:
        print("ห้ามใส่ 0 นะ")
        exit()
    result = five_divided_by(converted_num)
    print(f'ผลลัพธ์คือ {result}')

if __name__ == '__main__': # ถ้าไฟล์แรกที่เรียกใช้งาน จะเป็น __main__ ถ้าเรียกใช้งานจากไฟล์อื่น จะไม่เป็น __main__ แต่จะเป็นชื่อไฟล์
    main() # ถ้าเป็น __main__ จะเรียกใช้งาน main() ได้