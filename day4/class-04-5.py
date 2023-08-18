import time 
from time import sleep

#time.time()

prev_time = 0
while True:
    now = time.time()
    print(time.time())
    print(now - prev_time)
    prev_time = now
    sleep(1)