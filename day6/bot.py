# cheatsheet for pyautogui from https://pyautogui.readthedocs.io/en/latest/quickstart.html
import pyautogui # pip install pyautogui

curr_mouse_posn = pyautogui.position() # get current mouse position
print(curr_mouse_posn) 
print(curr_mouse_posn[0]) # x coordinate
print(curr_mouse_posn[1]) # y coordinate

x , y = pyautogui.position() # get current mouse position
print(x, y) # x coordinate, y coordinate

width, height = pyautogui.size() # get screen resolution
print(width, height) # width, height

# move mouse to x, y
pyautogui.moveTo(0, 0) # move mouse to x, y (top left corner)
pyautogui.moveTo(0, 0, duration=5) # move mouse to x, y (top left corner) in 5 seconds

# หยุดชั่วคราว
pyautogui.sleep(3) # sleep for 3 seconds

# ขยับเมาส์ไปกลางจอ
pyautogui.moveTo(int(width/2), int(height/2), duration=5) # move mouse to x, y (center of screen) in 5 second

# ขยับจากที่อยู่ปัจจุบัน
pyautogui.moveRel(100, 100, duration=1) # move mouse to x+100, y+100 (current position + 100) in 1 second

# คลิก
pyautogui.moveTo(100, 100, duration=1) # move mouse to x, y (top left corner) in 1 second
pyautogui.click() # click at current position
pyautogui.click(50, 175, duration=1) # click at x, y in 1 second

# พิมพ์ข้อความ
pyautogui.click() # click at current position
pyautogui.typewrite('Hello world!', interval=0.1) # type 'Hello world!' with 0.1 second interval between each character

# ฟังก์ชันอื่น ๆ 
pyautogui.alert('Hello World') # show alert box
pyautogui.confirm('Hello World') # show confirm box

###################################################################################################3
# ฟังก์ชันอื่น ๆ ที่น่าสนใจ
pyautogui.screenshot() # take screenshot
pyautogui.locateOnScreen('calc7key.png') # find image on screen
pyautogui.locateCenterOnScreen('calc7key.png') # find image on screen and return center position
pyautogui.locateAllOnScreen('calc7key.png') # find all image on screen
pyautogui.pixelMatchesColor(50, 200, (130, 135, 144)) # check if pixel at x, y is the same color as (130, 135, 144)
pyautogui.pixel(50, 200) # get color of pixel at x, y

#opneCV
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html