import streamlit as st
import streamlit as st
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##Homepage##
#get libraries
import streamlit as st 
import requests
import json
from streamlit_lottie import st_lottie

#set page configuration
st.set_page_config(
    page_title= "Home Page",layout = 'wide'
)

#define function to get animation
def lottie_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_img = lottie_url("https://lottie.host/80d6a368-c787-4f59-8eca-9b649cf41b1b/VdfzfJeXsp.json")


#intro talking about title 
with st.container():
    st.title("Unveiling secrets contributing to customer churn")
    st.write("##")
    st.write("""Every company wants to increase its profit or revenue margin and customer retention is one key area industry players 
             focus their resources - and we at Vodafone are no different!!""")
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.header("About us")
        st.write("##")
        st.write("""
                 Our group of experts in the team operate with the following objectives:

                 - Explore our clients data thoroughly and decide on the most efficient classification models.
                 - Find the lifetime value of each customer and know what factors affect the rate at which customers stop using their network.
                 - Predict if a customer will churn or not.""")
    with col2:
        st_lottie(
    lottie_img,
    speed=1,
    reverse= False,
    loop=True,
    quality="high",
    key="coding",
    height=500,
    width=600

)

with st.container():
        st.write("---")
        st.header("Explore")
        st.write("##")
        st.write("With our powerful machine learning algorithms, you could also try to predict whether a customer will churn or not with you own dataset!")
        st.write("##")
        uploaded_file = st.file_uploader("Upload your file here")
        

###DATA PAGE###
import streamlit as st 
import pyodbc 
import pandas as pd
import time

st.set_page_config(
    page_title= "Data Hub", layout="wide"
)

st.title('Customer Churn Analysis')


@st.cache_resource(show_spinner='Please wait for a second...')

def init_connection():
    return pyodbc.connect(
        "DRIVER={SQL Server};SERVER="
        + st.secrets["DBS"]
        + ";DATABASE="
        + st.secrets["DBN"]
        + ";UID="
        + st.secrets["DBU"]
        + ";PWD="
        + st.secrets["DBP"]
    )

conn = init_connection()


@st.cache_data(show_spinner='Loading data, This will only take a minute..')
def running_query(query):
    with conn.cursor() as c:
        c.execute(query)
        rows = c.fetchall()
        df=pd.DataFrame.from_records(rows, columns=[column[0] for column in c.description])
    return df

def get_all_columns():
    sql_query = 'SELECT * FROM dbo.LP2_Telco_churn_first_3000'
    df = running_query(sql_query)
    return df

first_train = get_all_columns()

second_train = pd.read_csv("./Datasets/LP2_Telco-churn-second-2000.csv")

train_df = pd.concat([first_train,second_train])

# Define a dictionary for mapping boolean and None values to more meaningful categories
new_cat_values_mapping = {
    'multiple_lines': {True: 'Yes', False: 'No', None: 'No phone service'},
    'online_security': {True: 'Yes', False: 'No', None: 'No internet service'},
    'online_backup': {True: 'Yes', False: 'No', None: 'No internet service'},
    'device_protection': {True: 'Yes', False: 'No', None: 'No internet service'},
    'tech_support': {True: 'Yes', False: 'No', None: 'No internet service'},
    'streaming_tv': {True: 'Yes', False: 'No', None: 'No internet service'},
    'streaming_movies': {True: 'Yes', False: 'No', None: 'No internet service'},
    'churn': {True: 'Yes', False: 'No', None: 'No'},
    'partner': {True: 'Yes', False: 'No'},
    'dependents': {True: 'Yes', False: 'No'},
    'paperless_billing': {True: 'Yes', False: 'No'},
    'phone_service': {True: 'Yes', False: 'No'},
}

# Replace old categories with the new ones
train_df.replace(new_cat_values_mapping, inplace=True)


#create a progress bar to let user know data is loading
progress_bar = st.progress(0)
for perc_completed in range(100):
    time.sleep(0.05)
    progress_bar.progress(perc_completed+1)

st.success("Data loaded successfully!")



#grouping all numeric columns
numerics = train_df.select_dtypes("number").columns
#grouping all categorical columns
categoricals = train_df.select_dtypes("object").columns

option = st.selectbox(
    "How would you like to view data?",
    ("All data", "Numerical columns", "Categorical columns"),
    index=None,
    placeholder="Select contact method...",)
# Conditionally display data based on the selected option
if option == "All data":
    st.write("### All Data")
    st.dataframe(train_df)
elif option == "Numerical columns":
    st.write("### Numerical Columns")
    st.dataframe(train_df[numerics])
elif option == "Categorical columns":
    st.write("### Categorical Columns")
    st.dataframe(train_df[categoricals])


markdown_table = """
| Column Names|Description| Data Type|
|-------------|-----------|----------|
|Gender|Whether the customer is a male or a female|object|
|SeniorCitizen|Whether a customer is a senior citizen or not|int64|
|Partner|Whether the customer has a partner or not (Yes, No)|object|
|Dependents|Whether the customer has dependents or not (Yes, No)|object|
|Tenure|Number of months the customer has stayed with the company|int64|
|Phone Service|Whether the customer has a phone service or not (Yes, No)|object|
|MultipleLines|Whether the customer has multiple lines or not|object|
|InternetService|Customer's internet service provider (DSL, Fiber Optic, No)|object|
|OnlineSecurity|Whether the customer has online security or not (Yes, No, No Internet)|object|
|OnlineBackup|Whether the customer has online backup or not (Yes, No, No Internet)|object|
|DeviceProtection|Whether the customer has device protection or not (Yes, No, No internet service)|object|
|TechSupport|Whether the customer has tech support or not (Yes, No, No internet)|object|
|StreamingTV|Whether the customer has streaming TV or not (Yes, No, No internet service)|object|
|StreamingMovies|Whether the customer has streaming movies or not (Yes, No, No Internet service)|object|
|Contract|The contract term of the customer (Month-to-Month, One year, Two year)|object|
|PaperlessBilling|Whether the customer has paperless billing or not (Yes, No)|object|
|Payment Method|The customer's payment method (Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic))|object|
|MonthlyCharges|The amount charged to the customer monthly|float64|
|TotalCharges|The total amount charged to the customer|float64|
|Churn|Whether the customer churned or not (Yes or No)|object| 
"""

if st.button("Click here "):
     # Display the markdown table inside the expander
    st.markdown(markdown_table)
    
##KOANIM#
import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth


st.set_page_config(
    page_title = 'Home Page',
    page_icon = '💒',
    layout = 'wide'
)

st.title("Welcome to :violet[Telco Customer Churn Prediction App]")

# Check if the default Firebase app is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('.streamlit/telco-customer-churn-predict-f7f9ee24bfdc.json')
    firebase_admin.initialize_app(cred)


def app():
    email_address = ''

    def login():
        try:
            display_name = auth.get_user_by_email(email_address)
            #print(display_name.uid)
            st.write('Login Successfully')

        except:
            st.warning('Invalid email or password')

    col1, col2 = st.columns(2)

    with col1:
        st.write('## How to run application')
        st.code('''
        # activate virtual environment
        env/scripts/activate
        streamlit run home.py
        ''')
        st.link_button('Repository on Github', url='https://github.com/Koanim/LP4-Telco-Customer-Churn-Prediction-APP')
        choice = st.selectbox('Login/Sign Up', ['Login', 'Sign Up'], key='unique_selectbox_key')
     
        if choice == 'Login':
            with st.form("login_form"):
                email_address = st.text_input('Email Address')
                password = st.text_input('Password', type='password')
                login_button = st.form_submit_button('Login', on_click = login)

            if login_button:
                st.success(f'Logged in as {email_address}')
    
        else:
            with st.form("signup_form"):
                username = st.text_input('Username')
                password = st.text_input('Password', type='password')
                email_address = st.text_input('Email Address')
                signup_button = st.form_submit_button('Sign up')

            if signup_button:
                user = auth.create_user(email = email_address, password = password, uid = username)
                st.success(f'Signed up as {username}')
                st.markdown('Please Login using your email and password')
                st.balloons()
                
    with col2:
        #Your additional content goes here
        with  st.container():
            st.write('## :violet[Predict Customer Churn]')
            st.write('### About Us')
            st.write(" This App's aim is to use Machine learning Algorithm to predict whether a new Telco customer will churn or not churn.To understand the dataset and find the lifeline value of each customer and determine which factors affect the rate at which customers stop using their network.")
            
            st.write('### Feedback Form')
            st.write('If you have any feedback, please contact us via telco@churnapp.com.')
app()