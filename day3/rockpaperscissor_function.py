import random


def play_rsp(player_choice):
    """
    Play Rock Paper Scissor Game
    โปรแกรมจะดูว่าค่าที่ให้เข้ามาชนะ เสมอ หรือแพ้
    จากนั้นพิมพ์ผลลัพธ์ออกมา
    """
    result = 0
    computer_choice = random.randint(1,3)
    if player_choice == computer_choice:
        result = 0
    elif player_choice == 1 and computer_choice == 2:
        result = -1
    elif player_choice == 1 and computer_choice == 3:
        result = 1
    elif player_choice == 2 and computer_choice == 1:
        result = 1
    elif player_choice == 2 and computer_choice == 3:
        result = -1
    elif player_choice == 3 and computer_choice == 1:
        result = -1
    elif player_choice == 3 and computer_choice == 2:
        result = 1
    return result

def print_result(result):
    """
    แสดงผลลัพธ์จากการเล่นเกม Rock Paper Scissor
    """
    if result == 0:
        print("Draw")
    elif result == 1:
        print("Player Win")
    elif result == -1:
        print("Computer Win")
    else:
        print("Error")


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
    result = play_rsp(player)
    print_result(result)
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

