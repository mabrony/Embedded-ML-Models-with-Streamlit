import streamlit as st
import yaml
from yaml.loader import  SafeLoader
import streamlit_authenticator as stauth

# Set up Home page
st.set_page_config(
    page_title="Customer Churn App",
    layout="wide"
)

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

authenticator.login(location='sidebar')



if st.session_state["authentication_status"]:
    authenticator.logout(location='sidebar')
    st.write(f'Welcome *{st.session_state["name"]}*', location='sidebar')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
    st.info('Login to access Prediction Application')
    st.code('''
        Login Credentials for Test Account:
        Username: test
        Password: 1A2345e''')

if st.session_state["authentication_status"]:
    st.markdown("<h1 style='color: red;'>CUSTOMER CHURN APP</h1>", unsafe_allow_html=True)

    # Create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("Predict if a customer is about to churn based on known characteristics using Machine Learning.")
        
        st.write("**About us**")
        st.write("Kryton consultancy is a team of Data scientist with a combined experience of 10 years."
             "We build applications for industries that are interested in seeing continouos improvement and value creation by identifying areas of growth and reducing wastage")
        st.write("### Key Features",)
        st.write("""
        - **Data**: Access the data.
        - **Dashboard**: Explore interactive data visualizations for insghts.
        - **Predict**: See predictions for customer churn.
        - **History**: See past predictions.

        """)
        
        st.write("### Machine Learning Integration",)
        st.write("""
                - **Accurate Predictions**: Integrate advanced ML algorithms for accurate predictions.
                - **Data-Driven Decisions**: Leverage comprehensive customer data to inform strategic initiatives.
                - **Variety**: Choose between two advanced ML algorithms for predictions""")


    with col2:
        st.write("### Follow the instructions below on how to run application")
        st.code("""
          activate virtual environment
          env/scripts/activate
          streamlit run Home.py
    """)
        st.write("### User Benefits",)
        st.write("""
        - **Accurate Prediction**: Reduce churn rate.
        - **Data-Driven Decisions**: Inform strategic initiatives.
        - **Enhanced Insights**: Understand customer behavior.
        """)
        
        with st.expander("Need Help?", expanded=False):
            st.write("""
                     Additional Information for Logged-in Users""
            """)
        
        st.link_button('Repository on Github', url='https://github.com/mabrony/EMBEDDED-ML-MODELS-WITH-STREAMLIT')


      