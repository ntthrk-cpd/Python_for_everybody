'''
# # ให้เขียนเกม rock paper scissor
def play_rsp(player_choice, game_choice):
    """
    เล่นเกม rock paper scissor
    function จะดูว่าค่าที่ให้เข้ามาชนะ เสมอ หรือแพ้
    จากนั้นพิมพ์ผลลัพธ์ออกมา
    ถ้าชนะ จะคืนค่า 1
    ถ้าเสมอ จะคืนค่า 0
    ถ้าแพ้ จะคืนค่า -1
    """
    if player_choice == game_choice:
        print("เสมอ")
        return 0
    elif player_choice == 'rock' and game_choice == 'scissor':
        print("ชนะ")
        return 1
    elif player_choice == 'rock' and game_choice == 'paper':
        print("แพ้")
        return -1
    elif player_choice == 'paper' and game_choice == 'rock':
        print("ชนะ")
        return 1
    elif player_choice == 'paper' and game_choice == 'scissor':
        print("แพ้")
        return -1
    elif player_choice == 'scissor' and game_choice == 'paper':
        print("ชนะ")
        return 1
    elif player_choice == 'scissor' and game_choice == 'rock':
        print("แพ้")
        return -1
    print("ลืม handle กรณี :", player_choice, game_choice)



GAME_CHOICES = ['rock', 'paper', 'scissor']
# เก็บคะแนนของผู้เล่น
score = 0
# ผู้เล่นใส่ค่าที่เลือกมาได้
# เล่นเกมตามรอบ
for game_choice in GAME_CHOICES:
    player_choice = input("ออกอะไร​? (rock, paper, scissor): ")
    print(game_choice)
    round_score = play_rsp(player_choice, game_choice)
    score += round_score  # score = score + round_score
# # แสดงผลคะแนน
print("คะแนนของคุณคือ", score)
if score >= 2:
    print("ชนะ")
elif score < 2:
    print("แพ้")

ให้แก้ไข code ให้ตัวเกม random ค้อน กรรไกร กระดาษ ทุกรอบที่เล่น 

---
'''

import random # library ใช้สำหรับสุ่มเลข

# # ให้เขียนเกม rock paper scissor
def play_rsp(player_choice, game_choice) -> int: # return type ของ function นี้คือ int
    """
    เล่นเกม rock paper scissor
    function จะดูว่าค่าที่ให้เข้ามาชนะ เสมอ หรือแพ้
    จากนั้นพิมพ์ผลลัพธ์ออกมา
    ถ้าชนะ จะคืนค่า 1
    ถ้าเสมอ จะคืนค่า 0
    ถ้าแพ้ จะคืนค่า -1
    """
    result: int = 0
    if player_choice == game_choice:
        print("เสมอ")
        result = 0
    elif player_choice == 'rock' and game_choice == 'scissor':
        print("ชนะ")
        result = 1
    elif player_choice == 'rock' and game_choice == 'paper':
        print("แพ้")
        result = -1
    elif player_choice == 'paper' and game_choice == 'rock':
        print("ชนะ")
        result = 1
    elif player_choice == 'paper' and game_choice == 'scissor':
        print("แพ้")
        result = -1
    elif player_choice == 'scissor' and game_choice == 'paper':
        print("ชนะ")
        result = 1
    elif player_choice == 'scissor' and game_choice == 'rock':
        print("แพ้")
        result = -1
    print("ลืม handle กรณี :", player_choice, game_choice)
    return result


GAME_CHOICES = ['rock', 'paper', 'scissor']
# เก็บคะแนนของผู้เล่น
score: int = 0
# ผู้เล่นใส่ค่าที่เลือกมาได้
# เล่นเกมตามรอบ
for _ in GAME_CHOICES: # ทำซ้ำตามจำนวนของ GAME_CHOICES คือ 3 รอบ (โดยไม่สนใจค่าที่ได้ ใช้ _ แทนค่าที่ได้ และไม่ใช้ค่าที่ได้ในการทำงาน แต่ใช้ค่าที่ได้ในการวน loop 3 รอบ)
    player_choice = input("ออกอะไร​? (rock, paper, scissor): ")
    print("player", player_choice)
    game_choice = random.choice(GAME_CHOICES) # สุ่มเลือกตัวเลือกใน list GAME_CHOICES
    print("game", game_choice)
    score += int(play_rsp(player_choice, game_choice)) # เรียกใช้ function play_rsp และบวกคะแนนที่ได้เข้ากับ score
# # แสดงผลคะแนน
print("คะแนนของคุณคือ", score)
if score >= 2:
    print("ชนะ")
elif score < 2:
    print("แพ้")
else:
    print("เสมอ")
