import streamlit as st
import pandas as pd
from models.page0 import app as page0_app
from models.page1 import app as page1_app
from models.page2 import app as page2_app
from models.page3 import app as page3_app
from models.page4 import app as page4_app
from models.page5 import app as page5_app
from models.page6 import app as page6_app

st.set_page_config(page_title="Your App Name", page_icon=":guardsman:", layout="wide")

PAGES = {
    "Home": page0_app,
    "About the Data": page1_app,
    "FMA Data Trends": page2_app,
    "Producers Trends": page3_app,
    "Geographic Trends": page4_app,
    "Genre Trends": page5_app,
    "Audio Features Trends": page6_app,
}

def load_data(csv_file):
    return pd.read_csv(csv_file)

def get_data():
    csv_file = 'data/merged_file.csv'
    return load_data(csv_file)


if 'df' not in st.session_state:
    df = get_data()
    st.session_state.df = df
else:
    df = st.session_state.df

st.sidebar.title("Navigation")
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))

page = PAGES[selection]
page(df)

st.sidebar.write("FMA Data Analysis project by Karthik Hosur and Diana Elizabeth Roy")

st.sidebar.header("Links")
st.sidebar.markdown(
        "[Download Dataset](https://github.com/mdeff/fma)",
        unsafe_allow_html=True,
    )
st.sidebar.markdown(
        "[Source Code](https://github.com/karthikhosur/FMA-Streamlit-App.git)",
        unsafe_allow_html=True,
    )
