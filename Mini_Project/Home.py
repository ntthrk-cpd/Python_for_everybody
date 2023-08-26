import streamlit as st
import datetime
import time
import set_data as sd
import set_connect as sc
import gspread
import add_data_to_sheet as ad

def main():
    data : list = []
    header_app()
    data = form_input()
    show_data(data)

def show_data(data):
    if data[3] == True:
        st.write("Date :", data[0])
        st.write("Description :", data[1])
        st.write("Amount :", data[2])
        try:
            ad.add_data_to_worksheet(data)
            st.success("Add data to Google Sheet Success")
        except gspread.exceptions.APIError:
            st.exception("Add data to Google Sheet Fail")
    else:
        st.write("Date :", datetime.date.today())
        st.write("Description :")
        st.write("Amount :", 0.00)
    pass

def form_input():
    data_input : list = []
    date_seleted : str = st.date_input("Date :", datetime.date.today())
    description : str = st.selectbox("Description :", sd.description_list)
    number : float = st.number_input("Amount :", min_value=0.00, max_value=1000000.00, value=0.00, step=1.00)
    sumbmit_button = st.button("Submit")
    data_input.append(date_seleted)
    data_input.append(description)
    data_input.append(number)
    data_input.append(sumbmit_button)
    return data_input

def header_app():
    st.set_page_config(
        page_title = "Kapook Aomsin",
        page_icon=":pig:",
    )
    st.title(":pig: My Kapook Aomsin :pig:")
    st.write("Personal Income and Expenses Account")
    st.write("------------------------------------")


if __name__ == "__main__":
    main()