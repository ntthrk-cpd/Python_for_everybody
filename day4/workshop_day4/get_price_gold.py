# get price of gold (from www.goldapi.io ) to thai baht every 3 seconds
import schedule
from time import sleep
import time
import requests
import forex_python # pip install forex-python
from forex_python.converter import CurrencyRates as cr 

count = 0

def get_price_gold() -> float:
    gold_price:float = 0
    api_key = "goldapi-fuxivrllgv64dj-io"
    symbol = "XAU"
    curr = "THB"
    date = f"/{time.strftime('%Y%m%d')}"
    #date = "/20230817"
    print(f'date: {date}')
    url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}"
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))
        raise SystemExit(e)
    if data == "error":
        print(f'Forex gold market close today: {date}')
        raise SystemExit(data["error"])
    #print(data)
    gold_price = data["price"]
    return gold_price

def transform_usd_to_baht(gold_price_usd) -> float:
    thb_per_usd = 0
    symbol_USD = "USD"
    symbol_THB = "THB"
    try:
        thb_per_usd = forex_python.converter.CurrencyRates().get_rate(symbol_USD, symbol_THB)
    except forex_python.converter.RatesNotAvailableError as e:
        print("Error:", str(e))
        raise SystemExit(e)
    return thb_per_usd * gold_price_usd

def job():
    global count
    count += 1
    gold_price:float = 0
    th_bath:float = 0
    print("I'm working...")
    print(f'count: {count}')
    date_now = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f'time now: {date_now}')
    gold_price = get_price_gold()
    print(f'Gold price: {gold_price:,.2f} USD')
    th_bath = transform_usd_to_baht(gold_price)
    print(f'Gold price: {th_bath:,.2f} bath')
    print("-------------------")

if __name__ == "__main__":
    schedule.every(3).seconds.do(job)
    while True:
        schedule.run_pending()
        sleep(1)