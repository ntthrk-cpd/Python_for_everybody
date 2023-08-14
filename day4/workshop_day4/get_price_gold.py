# เช็คราคาทองทุกๆ 3 วินาที
import schedule
from time import sleep
import time
from rich import inspect
import requests  # pip install requests
from bs4 import BeautifulSoup as BS  # pip install bs4

# def get_price_of(url):
#     data = requests.get(url)
#     soup = BS(data.text, 'html.parser')
#     ans = soup.find("div", class_ = "BNeawe s3v9rd AP7Wnd").text
#     return ans

count = 0

def job():
    global count
    count += 1
    # gold_price = get_price_of("https://www.google.com/search?q=gold+price")
    data = requests.get("https://www.google.com/search?q=gold+price")
    soup = BS(data.text, 'html.parser')
    print(soup)
    # ans = get_price_of(gold_price)
    # print(ans)

schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()  # ถ้ามีงานค้างอยู่รันมันซะ
    sleep(1)
