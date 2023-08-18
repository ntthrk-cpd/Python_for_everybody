import schedule
import time
from time import sleep


count = 0

def job():
    global count
    count += 1
    #print(f"I'm working...{count}")
    print(f"{int(time.time())} I'm working...{count}")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending() # ถ้ามีงานค้างอยู่รันงานนั้นก่อน
    sleep(3)