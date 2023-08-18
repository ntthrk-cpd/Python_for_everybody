# ทุก x วินาที เราจะเช็คราคาหุ้น
# https://pypi.org/project/yfinance/ # pip install yfinance
######################################################

import yfinance as yf # as คือการตั้งชื่อย่อ
import schedule
import time
from time import sleep
from rich import inspect

def get_price_of(symbols):
    """ ดึงราคาหุ้น symbol
    คืนค่าราคาปัจจุบัน 
    """
    
    """ 
    scb = yf.Ticker("SCB.BK") 
    ดึงข้อมูลหุ้น scb มาเก็บไว้ในตัวแปร scb โดยใช้ yf.Ticker จาก yfinance โดยใช้ชื่อหุ้น SCB.BK จากตลาดหลักทรัพย์ โดยเราต้องตั้งชื่อตามที่เว็บไซต์ให้ ไม่งั้นจะ error นะ
    หุ้นไทยจะต้องใช้ .BK หุ้นต่างประเทศจะใช้ .SA
    """
    #inspect(scb) # ดูว่ามีอะไรในตัวแปร scb บ้าง
    ticker = yf.Ticker(symbols) # ดึงข้อมูลหุ้น symbols มาเก็บไว้ในตัวแปร ticker โดยใช้ yf.Ticker จาก yfinance
    history = inspect(ticker.history(period="1d")) # ดูราคาหุ้นวันนี้
    type(history) # ดูชนิดข้อมูล
    # history["Open"] # ดูราคาเปิด
    # history["Close"] # ดูราคาปิด
    price = history["Close"][0] # ดูราคาปิดวันนี้
    return price

count = 0

def job():
    global count
    count += 1
    price = get_price_of("PTT.BK")
    if (price > 35):
        print('!!!!!!')
    #print(f"I'm working...{count}") # ทุกๆ 3 วินาที จะ print ว่า I'm working...
    #print(f"{int(time.time())} - PTT.BK = {price}") # ดูราคาหุ้น PTT.BK..

schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending() # ถ้ามีงานที่ต้องทำ ให้ทำงาน
    sleep(1)
