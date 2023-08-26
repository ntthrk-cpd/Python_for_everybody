import streamlit as st

def main():
    header_app()

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