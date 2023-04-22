import streamlit as st
import pandas as pd
from pages.page1 import app as page1_app
from pages.page2 import app as page2_app
from pages.page3 import app as page3_app
from pages.page4 import app as page4_app
from pages.page5 import app as page5_app
from pages.page6 import app as page6_app


def load_data(csv_file):
    return pd.read_csv(csv_file)

@st.cache_data
def get_data():
    csv_file = 'data/merged_file.csv'
    return load_data(csv_file)

PAGES = {
    "About the Data": page1_app,
    "Page 2": page2_app,
    "Page 3": page3_app,
    "Page 4": page4_app,
    "Page 5": page5_app,
    "Page 6": page6_app,
}

df = get_data()

st.sidebar.title("Navigation")
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))

page = PAGES[selection]
page(df)
