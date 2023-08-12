# pretty print
from pprint import pprint 
'''
    การเรียกใช้งาน pprint จาก library pprint 
    โดยจะเรียกใช้งาน pprint โดยไม่ต้องใส่ชื่อ library ด้วย 
    และจะเรียกใช้งานโดยการเรียก pprint ตามด้วยชื่อฟังก์ชันที่ต้องการใช้งาน 
    และตามด้วย (ตัวแปรที่ต้องการใช้งาน) โดยจะมีรูปแบบดังนี้ 

    pprint(ตัวแปรที่ต้องการใช้งาน)
'''

# word counter

##########################################################
# paragraph = "The quick brown fox jumps over the lazy dog"
# words = paragraph.split(" ")
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# pprint(word_count)

# ให้เขียนโปรแกรมนับคำ รับคำผ่าน input จากนั้นพิมพ์คำที่นับได้ทั้งหมดออกมา (word_counter.py)

#########################################################


from rich import print # ใช้ rich print แทน pprint ได้ สวยกว่า แต่ต้องติดตั้ง rich ก่อน ดูวิธีติดตั้งได้ที่ https://pypi.org/project/rich/
from rich.progress import track 
from time import sleep # ใช้ sleep ในการทดสอบ progress bar ได้ ถ้าไม่ใช้ก็ comment ออกได้ 

paragraph_input = input("Enter a paragraph: ")
words = paragraph_input.split(" ")
word_count = {}
for word in words:
    # sleep(1)
    if word in word_count:
        word_count[word] += 1
        word_count[word] = 1
print(word_count)