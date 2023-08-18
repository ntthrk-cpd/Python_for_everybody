import time
from time import sleep
form datetime import datetime

def job():
    print("I'm working...")

count = 0
while True:
    now = time.time()
    if now % 5 == 0:
        job()
        count += 1
    print(f'I worked {count} times')
    sleep(0.1) # หน่วงเวลา 0.1 วินาที