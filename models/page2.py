import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


def app(df: pd.DataFrame):
    st.title("FMA Data Trends")
    st.write("Genres in music are categories that describe the style, form, and content of musical compositions.")

    # Visualization 1: Count of Tracks by Genre
    genre_counts = df['genre_top'].value_counts()
    fig1 = px.bar(x=genre_counts.index, y=genre_counts.values, labels={'x':'Genre', 'y':'Count'}, title='Count of Tracks by Genre')
    st.write("This bar chart shows the number of tracks in each music genre in the FMA dataset. The x-axis represents the different music genres and the y-axis represents the count of tracks in each genre.")
    st.plotly_chart(fig1)

    # Visualization 2: Count of Tracks by Year Created
    df['year_created'] = pd.DatetimeIndex(df['date_created']).year
    year_counts = df['year_created'].value_counts().sort_index()
    fig2 = px.line(x=year_counts.index, y=year_counts.values, labels={'x':'Year Created', 'y':'Count'}, title='Count of Tracks by Year Created')
    st.write("This line chart shows the number of tracks created each year in the FMA dataset. The x-axis represents the years and the y-axis represents the count of tracks created in each year.")
    st.plotly_chart(fig2)
    
    # Visualization 3: Count of Different Music Release Types
    fig3 = px.histogram(df, x='type', labels={'x':'Type', 'y':'Count'}, title='Count of Different Music Release Types')
    st.write("This histogram shows the count of different music release types in the FMA dataset. The x-axis represents the different types of music release and the y-axis represents the count of each type.")
    st.plotly_chart(fig3)

    # Visualization 4: Count of Different Bit Rates
    fig4 = px.histogram(df, x='bit_rate', labels={'x':'Bit Rate', 'y':'Count'}, title='Count of Different Bit Rates')
    st.write("This histogram shows the count of different bit rates in the FMA dataset. The x-axis represents the different bit rates and the y-axis represents the count of each bit rate.")
    st.plotly_chart(fig4)
