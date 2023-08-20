# ให้เขียนบอทขยับเมาส์ไปเรื่อย ๆ จะได้ไม่โดนดีดออกจากเกม
import pyautogui
import random

while True:
    rand_num_x = random.randint(1, 10)
    rand_num_y = random.randint(1, 10)
    pyautogui.moveRel(10 * rand_num_x, 10 * rand_num_y, duration=1)
    pyautogui.sleep(5)
