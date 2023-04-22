import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


def app(df: pd.DataFrame):
    st.title("Page 2")
    st.write("Welcome to Page 2!")

    genre_counts = df['genre_top'].value_counts()
    fig1 = px.bar(x=genre_counts.index, y=genre_counts.values, labels={'x':'Genre', 'y':'Count'}, title='Count of Tracks by Genre')
    st.plotly_chart(fig1)


    df['year_created'] = pd.DatetimeIndex(df['date_created']).year
    year_counts = df['year_created'].value_counts().sort_index()
    fig2 = px.line(x=year_counts.index, y=year_counts.values, labels={'x':'Year Created', 'y':'Count'}, title='Count of Tracks by Year Created')
    st.plotly_chart(fig2)
    
    fig = px.histogram(df, x='type', title='Count of Different Types')
    st.plotly_chart(fig)

    fig = px.histogram(df, x='bit_rate', title='Count of Different BitRates')
    st.plotly_chart(fig)