import streamlit as st
import Home as h
import datetime
import set_data as sd
import set_connect as sc
import gspread
import pandas as pd
import time
import add_data_to_sheet as ad

sh = sc.connect_to_google_sheet()

def main():
    h.header_app()
    sel_date_value : list = select_date()
    df = get_data_from_date(sel_date_value)
    set_data_to_manage(df)

# set data to manage page
def set_data_to_manage(df):
    #row 0 is header
    df = df.rename(columns=
                   {0: "Date", 1: "Description", 2: "Income", 3: "Expenses", 4: "Balance"}
                   )
    #set data type of column
    df["Date"] = pd.to_datetime(df["Date"])
    df["Income"] = pd.to_numeric(df["Income"])
    df["Expenses"] = pd.to_numeric(df["Expenses"])
    df["Balance"] = pd.to_numeric(df["Balance"])
    edited_df = st.data_editor(
        df,
        column_config={
            "Date": st.column_config.DateColumn(
                "Date",
                min_value=datetime.date(2023, 1, 1),
                max_value=datetime.date(2023, 12, 31),
                format="DD-MMMM-YYYY",
                required=True,
            ),
            "Description": st.column_config.SelectboxColumn(
                "Description",
                options=sd.description_list,
                required=True,
            ),
            "Income": st.column_config.NumberColumn(
                "Income",
                min_value=0.00,
                max_value=1000000.00,
                step=1.00,
                format="%.2f",
            ),
            "Expenses": st.column_config.NumberColumn(
                "Expenses",
                min_value=0.00,
                max_value=1000000.00,
                step=1.00,
                format="%.2f",
            ),
            "Balance": st.column_config.NumberColumn(
                "Balance",
                min_value=0.00,
                max_value=1000000.00,
                step=1.00,
                format="%.2f",
            ),
            "deleted_row": st.column_config.CheckboxColumn(
                "delete_row",
            ),
        },
        key="edit_data",
        width=1000,
        num_rows="dynamic",
        hide_index=True,
    )
    st.write("Here's the session state:")
    st.write(st.session_state["edit_data"]) # 👈 Access the edited data
    if st.button("Submit"):
        try:
            # if delete row
            # if (edited_df["delete_row"] == True).any():
            #     for i in range(len(edited_df)):
            #         if edited_df["delete_row"][i] == True:
            #             worksheet = sh.worksheet("Sheet_" + edited_df["Date"][i].strftime("%B"))
            #             if worksheet.delete_row(i + 2):
            #                 st.success("Delete data from Google Sheet Success")
            #                 worksheet.delete_row(i + 2)
            # if edit 
            # if add row
            st.success("Add data to Google Sheet Success")
        except gspread.exceptions.APIError:
            st.exception("Add data to Google Sheet Fail")
        pass
    
# select date for manage From - To
def select_date():
    sel_date_value : list = []
    st.write("Select Date (limit 16 day))")
    date1 = st.date_input("From :", datetime.date.today())
    date2 = st.date_input("To :", datetime.date.today())
    if date1 > datetime.date.today():
        st.error("Error: From date must fall before today.")
    elif date2 > datetime.date.today():
        st.error("Error: To date must fall before today.")
    elif date1 > date2:
        st.error("Error: To date must fall after From date.")
    elif (date2 - date1).days > 16:
        st.error("Error: Date range must be less than or equal to 16 days.")
    else:
        sel_date_value.append(date1)
        sel_date_value.append(date2)
        st.success(f'Success, Selected From {date1} to {date2}')
    return sel_date_value

# show data in manage page from google sheet by date
def get_data_from_date(sel_date_value):
    data_all : list = []
    data : list = []
    worksheet_list = sh.worksheets()
    for worksheet in worksheet_list:
        if worksheet.title == "Sheet_" + sel_date_value[0].strftime("%B"):
            if len(worksheet.get_all_values()) > 1:
                data_all = worksheet.get_all_values()
            if data_all != []:
                for i in range(1, len(data_all)):
                    if datetime.datetime.strptime(data_all[i][0], 
                                                  "%d-%B-%Y").date() >= sel_date_value[0] and datetime.datetime.strptime(data_all[i][0]
                                                   , "%d-%B-%Y").date() <= sel_date_value[1]:
                        data.append(data_all[i])
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    main()
    pass