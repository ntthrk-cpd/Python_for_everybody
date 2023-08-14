# ทุกๆ x วินาที เราจะเช็คราคาหุ้น
import yfinance as yf
import schedule
from time import sleep
import time
from rich import inspect


def get_price_of(symbol):
    """ดึงราคาหุ้น symbol
    คืนค่าราคาปัจจุบัน
    """
    ticker = yf.Ticker(symbol)
    history = ticker.history(period="1d")
    price = history['Close'][0]

    return price


count = 0


def job():
    global count
    count += 1
    price = get_price_of('PTT.BK')
    print(f"{int(time.time())} - PTT.BK = {price}")
    if price > 35:
        print('!!!!!!!!')


schedule.every(3).seconds.do(job)


while True:
    schedule.run_pending()  # ถ้ามีงานค้างอยู่รันมันซะ
    sleep(1)


ให้แก้ไขโค้ดให้ทำงานอะไรก็ได้ ทุกๆ x วินาทีแทนดึงราคาหุ้น
https://schedule.readthedocs.io/en/stable/