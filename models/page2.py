import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


def app(df: pd.DataFrame):
    st.title("FMA Data Trends")
    st.write("Genres in music are categories that describe the style, form, and content of musical compositions.")

    genre_counts = df['genre_top'].value_counts()
    fig1 = px.bar(x=genre_counts.index, y=genre_counts.values, labels={'x':'Genre', 'y':'Count'}, title='Count of Tracks by Genre')
    st.plotly_chart(fig1)


    df['year_created'] = pd.DatetimeIndex(df['date_created']).year
    year_counts = df['year_created'].value_counts().sort_index()
    fig2 = px.line(x=year_counts.index, y=year_counts.values, labels={'x':'Year Created', 'y':'Count'}, title='Count of Tracks by Year Created')
    st.plotly_chart(fig2)
    
    fig3 = px.histogram(df, x='type', labels={'x':'Type', 'y':'Count'}, title='Count of Different Music Release Types')
    st.plotly_chart(fig3)

    fig4 = px.histogram(df, x='bit_rate', labels={'x':'Bit Rate', 'y':'Count'}, title='Count of Different Bit Rates')
    st.plotly_chart(fig4)
