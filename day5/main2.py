from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
from rich import inspect
from selenium.webdriver.chrome.options import Options


def price_to_float(price):
    price = price.replace("฿", "")
    price = price.replace(",", "")
    price = float(price)
    return price

url = "https://www.lazada.co.th/"
#xpath = "/html/body/div[4]/div/div[3]/div[2]/div/div[1]/div[8]/div/div/span"
# ค้นหาด้วย xpath ของ search field ใน Lazada
search_field_xpath = "/html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div[1]/input[1]" 

options = Options()
driver = webdriver.Chrome()
driver.set_page_load_timeout(5)
try:
    driver.get(url)
except TimeoutException:
    pass
search_field = driver.find_element(By.XPATH, search_field_xpath)
search_field.send_keys("กระเป๋า")
search_field.submit()
els = driver.find_elements(By.CLASS_NAME, "oo0xS")

prices = []
for el in els:
    price = price_to_float(el.text)
    prices.append(price)

driver.close()

max_price = max(prices) # หาค่าสูงสุดใน list
min_price = min(prices) # หาค่าต่ำสุดใน list
average_price = sum(prices) / len(prices) # หาค่าเฉลี่ยใน list
print(f"Max price: {max_price}")
print(f"Min price: {min_price}")
print(f"Average price: {average_price}")
