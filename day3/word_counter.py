# ให้เขียนโปรแกรมนับคำ รับคำผ่าน input จากนั้นพิมพ์คำที่นับได้ทั้งหมดออกมา
from pprint import pprint 

paragraph_input = input("Enter a paragraph: ")
words = paragraph_input.split(" ")
word_count = {}
count = 0
for word in words:
    if word in word_count:
        word_count[word] += count
    else:
        word_count[word] = count
    count += 1
print(word_count)