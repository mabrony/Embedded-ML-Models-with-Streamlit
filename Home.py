import streamlit as st

st.title("Customer Churn App")

# Assuming authenticator is a custom function or library for handling authentication
def authenticator():
    return True  # Replace with actual authentication logic

if authenticator():  # Call your authentication function
  st.sidebar.button("Signup", key="Signup-button")
  st.sidebar.button("Login", key="login-button")
  st.sidebar.button("Logout", key="logout-button")
  col1, col2 = st.columns(2)
  with col1:
    # Add your desired content here (text, charts, etc.)
    st.write("**About us**")
    st.write("Kryton consultancy is a team of Data scientist with a combined experience of 10 years."
             "We build applications for industries that are interested in seeing continouos improvement and value creation by identifying areas of growth and reducing wastage")
  with col2:
    st.write("### Follow the instructions below on how to run application")
    st.code("""
    activate virtual environment
    env/scripts/activate
    streamlit run Home.py
    """)
    st.write("**Additional Information for Logged-in Users (Right Column)**")
    st.link_button('Repository on Github', url='https://github.com/mabrony/EMBEDDED-ML-MODELS-WITH-STREAMLIT')
else:
  st.error('Username/password is incorrect')