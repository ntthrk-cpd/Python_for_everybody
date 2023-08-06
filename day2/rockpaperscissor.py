##############################################################
# แนวทางการเขียนโปรแกรม rock paper scissor ด้วยภาษา Python 3 ดังนี้ 
# ให้เขียนเกม rock paper scissor
# เก็บคะแนนของผู้เล่น
# ผู้เล่นใส่ค่าที่เลือกมาได้
# เล่นเกมตามรอบ
# แสดงผลคะแนน
""" 
rock - paper = paper
rock - scissor = rock
paper - scissor = scissor
paper - rock = paper
scissor - rock = rock
scissor - paper = scissor
"""
#############################################################
import random

score_player: int = 0
score_Computer: int = 0
round = 0

print("__________________________________")
print("")
print("Welcome to Rock Paper Scissor Game")
print("__________________________________")
print("")
while round < 3:
    print("---------------------------------")
    print("\t[[[[ Round :", round, "]]]]\t")
    print("Please select your choice.")
    print("1 Rock")
    print("2 Paper")
    print("3 Scissor")
    print("0 Exit")
    player : str = input("---> Please select your choice : ")
    computer = random.randint(1,3)
    print("Player : ", player, "", "Computer : ", computer)
    if  player == '0':
        print("Exit Game")
        break
    elif player != '1' and player != '2' and player != '3':
        print("Choice wrong, Please try again")
        continue
    player = int(player)
    if player == computer:
        print("Draw")
    elif player == 1 and computer == 2:
        print("Computer Win")
        score_Computer += 1
    elif player == 1 and computer == 3:
        print("Player Win")
        score_player += 1
    elif player == 2 and computer == 1:
        print("Player Win")
        score_player += 1
    elif player == 2 and computer == 3:
        print("Computer Win")
        score_Computer += 1
    elif player == 3 and computer == 1:
        print("Computer Win")
        score_Computer += 1
    elif player == 3 and computer == 2:
        print("Player Win")
        score_player += 1
    else:
        print("Error")
    round += 1
print("__________________________________")
print("Game Over")
print("Player Score : ", score_player)
print("Computer Score : ", score_Computer)
if score_player > score_Computer:
    print("Player Win !!!")
elif score_player < score_Computer:
    print("Computer Win !!!")
else:
    print("Draw")
print("__________________________________")