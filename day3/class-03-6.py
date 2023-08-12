import tomllib # ใช้งานใน python version 3.11 ขึ้นไป
from rich import print

# with open("input.toml", "rb") as file:
#     data = tomllib.load(file)

with open("/home/ntthrk-ch/Documents/Ntthrk_UBUNTU/LearningSkill/Python/Python_for_everybody/day3/input.txt") as file:
    data = tomllib.load(file)

print(data)