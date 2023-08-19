#แก้ไขโค้ดจาก main.py

import selenium 
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from time import sleep
from rich import inspect
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import locale

def get_price(
    url,
    xpath,
):
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(10)
    try:
        driver.get(url)
    except TimeoutException:
        pass
    el = driver.find_element(By.XPATH, price_xpath)
    price_text = el.text
    price_text = price_text.replace("฿", "")
    price_text = price_text.replace(",", "")
    price = float(price_text)
    driver.close()
    return price

url = "https://anello.co.th/anello-backpack-size-regular-retro-r-ahb3771z.html"
price_xpath = "/html/body/div[2]/main/div[3]/div/div[1]/div[3]/div[2]/span[1]/span/span/span"

previous_price = None
count = 0

while count < 3:
    count += 1
    price = get_price(url, price_xpath)
    if previous_price is None:
        previous_price = price
    elif price < previous_price:
        print("Price down!")
    elif price == previous_price:
        print("Price is the same!")
    else:
        print("Price up!")
    previous_price = price
    print(price)
    sleep(1)