from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
from rich import inspect


def get_price(
    url,
    xpath,
):
    """Scrape price from Lazada product page ด้วย xpath
    คืนค่าเป็น float
    """
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(5)
    try:
        driver.get(url)
    except TimeoutException:
        pass
    el = driver.find_element(By.XPATH, xpath)
    price_text = el.text
    price_text = price_text.replace("฿", "")
    price = float(price_text)
    driver.close()

    return price


url = "https://www.lazada.co.th/products/jeep-spirit-1941-estd-i4613435953-s18915753136.html"
xpath = "/html/body/div[4]/div/div[3]/div[2]/div/div[1]/div[8]/div/div/span"

previous_price = None
while True:
    price = get_price(url, xpath)
    if previous_price is None:
        previous_price = price
    elif price < previous_price:
        print("Price down!")
        previous_price = price
    elif price == previous_price:
        print("Price same!")
        previous_price = price
    else:
        print("Price up!")
        previous_price = price
    print(price)
    sleep(1)