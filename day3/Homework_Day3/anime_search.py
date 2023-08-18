"""
find anime name from the api and print the data.
ref link : https://kitsu.docs.apiary.io/
https://kitsu.io/api/edge/anime?filter[text]=cowboy%20bebop
"""

import httpx
from rich import print
from rich.progress import track



def get_anime_data(anime_name) -> list:
    anime_data = {}
    i: int = 0
    url = f"https://kitsu.io/api/edge//anime?filter[text]={anime_name}"
    response = httpx.get(url)
    data = response.json()
    for i in range(len(data["data"])):
        anime_data[i] = {
            "Anime Name": data["data"][i]["attributes"]["canonicalTitle"],
            "Anime Type": data["data"][i]["attributes"]["showType"],
            "Anime Rating": data["data"][i]["attributes"]["averageRating"],
            "Anime Age Rating": data["data"][i]["attributes"]["ageRating"],
            "Description": data["data"][i]["attributes"]["synopsis"],
        }
    return anime_data


def main():
    anime_data: list = {}
    i: int = 0
    print("Welcome to Anime Search")
    try:
        anime_name = input("Enter the name of the anime: ")
    except Exception as e:
        print("Error: ", e)
        exit()
    anime_data = get_anime_data(anime_name)
    # print(anime_data)

    for i in anime_data:
        print(f"Anime {i+1} :")
        print("Anime Name: ", anime_data[i]["Anime Name"])
        print("Anime Type: ", anime_data[i]["Anime Type"])
        print("Anime Rating: ", anime_data[i]["Anime Rating"])
        print("Anime Age Rating: ", anime_data[i]["Anime Age Rating"])
        print("Description: ", anime_data[i]["Description"])
        print("\n-----------------------------------------------\n")
    print("\n")
    print("--------------------- End ------------------------")
    print("\n")

if __name__ == "__main__":
    main()