#https://pokeapi.co/
#วิธีใช้
#https://pokeapi.co/api/v2/pokemon/ditto
'''
ต้องติดตั้ง httpx ก่อน ดูวิธีติดตั้งได้ที่ https://pypi.org/project/httpx/ 
หรือใช้คำสั่ง pip install httpx ใน terminal หรือ command prompt ก็ได้
หลังจากติดตั้ง httpx เสร็จแล้ว ให้เรียกใช้งาน httpx โดยการ import httpx มาใช้งาน
และใช้คำสั่ง httpx.get(url) เพื่อดึงข้อมูลจาก url ที่ต้องการ โดยจะได้ข้อมูลกลับมาในรูปแบบ json
โดยจะเรียกใช้งาน httpx โดยไม่ต้องใส่ชื่อ library ด้วย
และจะเรียกใช้งานโดยการเรียก httpx ตามด้วยชื่อฟังก์ชันที่ต้องการใช้งาน
และตามด้วย (ตัวแปรที่ต้องการใช้งาน) โดยจะมีรูปแบบดังนี้

'''
#########################################################
import httpx 
from rich import print
from rich.progress import track

# r = httpx.get('https://pokeapi.co/api/v2/pokemon/ditto')
# print(r.json().keys()) # ดู key ทั้งหมดของ json ที่ได้จากการ get มา 
# print(r.json()['stats']) 
def get_total_stat(data):
    """
    คำนวนค่า total stat ของ pokemon
    """
    data = data['stats']
    total = 0
    for stat in data:
        total += stat['base_stat']
    return total


pokemons = ['ditto', 'pikachu', 'mewtwo', 'mew', 'charizard', 'bulbasaur', 'squirtle', 'eevee', 'snorlax', 'dragonite']
pokemon_data = {}
for pokemon in track(pokemons):
    url = 'https://pokeapi.co/api/v2/pokemon' + '/' + pokemon
    r = httpx.get(url)
    data = r.json()
    total_stat = get_total_stat(data)
    pokemon_data[pokemon] = total_stat
# print(pokemon_data)
pokemon_with_most_stat = ""
most_stat = 0
for pokemon, total_stat in pokemon_data.items():
    print(f'{pokemon} total stat: {total_stat}')
    if total_stat > most_stat:
        most_stat = total_stat
        pokemon_with_most_stat = pokemon
print(f'Pokemon with most stat is {pokemon_with_most_stat} with total stat {most_stat}')