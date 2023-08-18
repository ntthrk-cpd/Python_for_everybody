# ทำงานทุก ~10 วินาที
import time
from time import sleep
form datetime import datetime

def job():
    print("I'm working...")

while True:
    now = time.time()
    print(f'job started at {time.time()}')
    prinf(f'job started at {datetime.now()}')
    job()
    # sleep(10) # หน่วงเวลา 10 วินาที
    sleep(3) # หน่วงเวลา 3 วินาที