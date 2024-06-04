import streamlit as st
import pyodbc
import pandas as pd  # Import pandas

st.set_page_config(
    page_title="Data Page",
    layout="wide"
)

st.title("Vodafone Customer Churn Database")


@st.cache_resource(show_spinner="connecting to database...")
def init_connection():
    return pyodbc.connect(
        f"DRIVER={{SQL Server}};SERVER={st.secrets['server']};DATABASE={st.secrets['database']};UID={st.secrets['username']};PWD={st.secrets['password']}"
    )


connection = init_connection()  # Fix indentation


@st.cache_data(show_spinner="running_query...")
def running_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        df = pd.DataFrame.from_records(rows, columns=[column[0] for column in cursor.description])
    return df


def get_all_column():
    sql_query = " SELECT * FROM LP2_Telco_churn_first_3000 "
    df = running_query(sql_query)
    return df


# Move get_all_column definition before st.selectbox (optional)

options = ["All columns", "Numerical columns", "Categorical columns"]
selected_option = st.selectbox("Select..", options=options, on_change=get_all_column)

st.write(get_all_column())  # Call the function to display data based on selection