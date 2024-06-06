#import pickle
#import streamlit as st#
#import pandas as pd#
#from PIL import Image#

import streamlit as st

# Set up Home page
st.set_page_config(
    page_title="CUSTOMER CHURN PREDICTION APPLICATION",
    page_icon='🏠',
    layout="wide"
)

# Title and introduction
st.title("CUSTOMER CHURN PREDICTION APPLICATION")
st.subheader("🔮 Predict the Future! 🔮")
# st.image("Assets\AI_Generated_Image_2024-06-03_455117497009201.png")
st.write(""" 
This application harnesses the power of data science to forecast if a customer 
is about to churn based on known characteristics. Our solution leverages data science 
to empower organizations with actionable insights, enabling proactive retention strategies
and sustainable growth.

**Key Features:**
- Accurate Prediction: Utilize predictive modeling to anticipate customer churn with precision.
- Data-Driven Decisions: Leverage comprehensive customer data to inform strategic initiatives.
- Proactive Retention: Take preemptive measures to retain valuable customers and foster long-term loyalty.
""")

st.markdown("Here is my new code for this application")

st.write("Hello world")
status = st.radio("Select gender:" ("male", "female"))
if (status == "male"):
    st.success("male")
else:
    st.success("female")