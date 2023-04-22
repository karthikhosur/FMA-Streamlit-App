import streamlit as st
import pandas as pd
import plotly.express as px

def app(df: pd.DataFrame):
    st.title("Charts for Song and Artist Popularity, and Total Listens by Genre")

    # Convert the 'date_created' column to datetime format
    df['date_created'] = pd.to_datetime(df['date_created'], errors='coerce')

    # Find the minimum and maximum dates in the DataFrame
    min_date = df['date_created'].min()
    max_date = df['date_created'].max()

    # Add a date range slider
    date_range = st.date_input("Select date range:", [min_date, max_date])

    # Convert the selected date range to datetime64[ns]
    date_range = pd.to_datetime(date_range)

    # Filter the DataFrame based on the selected date range
    filtered_df = df[(df['date_created'] >= date_range[0]) & (df['date_created'] <= date_range[1])]

    # Allow the user to select multiple genres
    unique_genres = filtered_df['genre_top'].unique()
    selected_genres = st.multiselect("Select genres to plot:", unique_genres, default=unique_genres)

    # Filter the DataFrame based on selected genres
    filtered_df = filtered_df[filtered_df['genre_top'].isin(selected_genres)]


    # Plot 1: Song Popularity vs. Artist Popularity by Genre
    df_plot = filtered_df[['genre_top', 'song_hotttnesss', 'artist_hotttnesss']]
    df_grouped = df_plot.groupby('genre_top').mean().reset_index()

    fig1 = px.scatter(df_grouped, x='song_hotttnesss', y='artist_hotttnesss', color='genre_top', title='Song Popularity vs. Artist Popularity by Genre')
    fig1.update_xaxes(title_text='Song Popularity')
    fig1.update_yaxes(title_text='Artist Popularity')
    st.plotly_chart(fig1)

    # Plot 2: Median Song Popularity Rank by Genre
    df_plot = filtered_df[['genre_top', 'song_hotttnesss_rank']]
    df_grouped = df_plot.groupby('genre_top').median().reset_index()

    fig2 = px.bar(df_grouped, x='genre_top', y='song_hotttnesss_rank', title='Median Song Popularity Rank by Genre')
    fig2.update_xaxes(title_text='Genre')
    fig2.update_yaxes(title_text='Median Song Popularity Rank')
    st.plotly_chart(fig2)

    # Plot 3: Total Listens by Genre
    df_grouped = filtered_df.groupby('genre_top').sum().reset_index()

    fig3 = px.bar(df_grouped, x='genre_top', y='listens_1', title='Total Listens by Genre')
    fig3.update_xaxes(title_text='Genre')
    fig3.update_yaxes(title_text='Total Listens')
    st.plotly_chart(fig3)
