"""
find anime name from the api and print the data.
ref link : https://kitsu.docs.apiary.io/
"""

import httpx
from rich import print
from rich.progress import track

anime_data = {}
anime_name = input("Enter the name of the anime: ")
url = f"https://kitsu.io/api/edge//anime?filter[text]={anime_name}"
response = httpx.get(url)
data = response.json()
for i in track(range(len(data["data"])), description="Fetching data..."):
    anime_data[i] = {
        "Anime Name": data["data"][i]["attributes"]["canonicalTitle"],
        "Anime Type": data["data"][i]["attributes"]["showType"],
        "Anime Rating": data["data"][i]["attributes"]["averageRating"],
        "Anime Age Rating": data["data"][i]["attributes"]["ageRating"],
    }
print(anime_data)
