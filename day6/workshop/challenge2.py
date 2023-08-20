# ให้เขียนบอทขยับเมาส์ไปเรื่อย ๆ จะได้ไม่โดนดีดออกจากเกม

import pyautogui
import time
import random

pyautogui.moveTo(100, 100, duration=1)

while True:
    x , y = pyautogui.position() 
    print(x, y)
    random_x : float = random.uniform(-100, 100)
    random_y : float = random.uniform(-100, 100)
    pyautogui.moveRel(random_x, random_y, duration=1)
    time.sleep(0.5)