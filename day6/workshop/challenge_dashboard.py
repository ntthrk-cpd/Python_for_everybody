# ใ่ช้ streamlit เขียนอะไรก็ได้
import streamlit as st
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
    st.title("Welcome to Anime Search") 
    st.caption("ค้นหาข้อมูลอนิเมะ ที่คุณต้องการ")
    try:
        anime_name = st.text_input("Enter the name of the anime: ")
    except Exception as e:
        print("Error: ", e)
        exit()
    anime_data = get_anime_data(anime_name)
    st.write("พบอนิเมะที่ตรงกันทั้งหมด ", len(anime_data) , " เรื่อง")
    for i in anime_data:
        st.write("Anime Name: ", anime_data[i]["Anime Name"])
        st.write("Anime Type: ", anime_data[i]["Anime Type"])
        st.write("Anime Rating: ", anime_data[i]["Anime Rating"])
        st.write("Anime Age Rating: ", anime_data[i]["Anime Age Rating"])
        st.write("Description: ", anime_data[i]["Description"])
        st.write("\n-----------------------------------------------\n")
    st.write("\n")
    

if __name__ == "__main__":
    main()