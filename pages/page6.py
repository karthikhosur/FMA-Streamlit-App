import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def app(df: pd.DataFrame):
    st.title("Audio Features ")

    # Group the data by genre_top and calculate the mean value for each column
    df_plot = df[['genre_top', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence']]
    df_grouped = df_plot.groupby('genre_top').mean().reset_index()

    # Create a dropdown menu for the user to select multiple features
    features = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence']
    selected_features = st.multiselect("Select features to plot:", features)

    # Create a box plot using the selected features
    box_fig = go.Figure()

    for feature in selected_features:
        box_fig.add_trace(go.Box(y=df[feature], name=feature.capitalize(), boxmean=True))

    box_fig.update_layout(title="Box Plot of Selected Audio Features ", xaxis_title="Features", yaxis_title="Feature Value")
        
    # Display the box plot
    st.plotly_chart(box_fig)

    st.title("Interactive Charts for Audio Features and Attributes")

    # Create multi-select dropdowns for features and attributes
    features = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence']
    attributes = ['interest', 'listens', 'duration']

    selected_attribute = st.selectbox("Select an attribute to plot:", attributes)

    # Create a scatter plot using the selected features and attribute
    fig = go.Figure()

    for feature in selected_features:
        aggregated_df = df.groupby(feature).agg({selected_attribute: 'mean'}).reset_index()
        fig.add_trace(go.Scatter(x=aggregated_df[feature], y=aggregated_df[selected_attribute], mode='markers', name=feature.capitalize()))

    fig.update_layout(title=f"Selected Audio Features vs {selected_attribute.capitalize()}", xaxis_title=selected_attribute.capitalize(), yaxis_title="Feature Value")
    
    # Display the scatter plot
    st.plotly_chart(fig)
   
    st.title("Scatter Plots of Audio Features vs Genre")

    # Group the data by genre_top and calculate the mean value for each column
    df_plot = df[['genre_top', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness','valence']]
    df_grouped = df_plot.groupby('genre_top').mean().reset_index()

    # Create a dropdown menu for the user to select multiple features
    features = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence']

    # Create a scatter plot using the selected features
    fig = go.Figure()

    for feature in selected_features:
        fig.add_trace(go.Scatter(x=df_grouped['genre_top'], y=df_grouped[feature], mode='markers', name=feature.capitalize()))

    fig.update_layout(title="Selected Audio Features vs Genre_top", xaxis_title="Genre_top", yaxis_title="Feature Value")
    
    # Display the scatter plot
    st.plotly_chart(fig)