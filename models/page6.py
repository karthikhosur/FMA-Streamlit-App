import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def app(df: pd.DataFrame):
    st.title("Audio Features ")

    st.markdown("""
    This app allows you to explore the relationships between different audio features and various attributes within the given dataset.
    Audio features include acousticness, danceability, energy, instrumentalness, liveness, speechiness, and valence.
    Attributes include interest, listens, and duration.
    """)

    # Group the data by genre_top and calculate the mean value for each column
    df_plot = df[['genre_top', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence']]
    df_grouped = df_plot.groupby('genre_top').mean().reset_index()

    # Create a dropdown menu for the user to select multiple features
    features = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence']
    selected_features = st.multiselect("Select features to plot:", features, default=features)

    # Create a box plot using the selected features
    box_fig = go.Figure()

    for feature in selected_features:
        box_fig.add_trace(go.Box(y=df[feature], name=feature.capitalize(), boxmean=True))

    box_fig.update_layout(title="Box Plot of Selected Audio Features ", xaxis_title="Features", yaxis_title="Feature Value")
    st.markdown("""
    A box plot is a standardized way of displaying the distribution of data based on five number summary ("minimum", first quartile (Q1), median, third quartile (Q3), and "maximum").
    """)
    # Display the box plot
    st.plotly_chart(box_fig)

    st.title("Interactive Charts for Audio Features and Attributes")
    st.markdown("""
The scatter plot below shows the relationship between the selected audio features and the selected attribute. Each point represents the mean value of the attribute for a given feature value.
""")

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
    st.markdown("""
    The scatter plot below shows the relationship between the selected audio features and genre. Each point represents the mean value of the feature for a given genre.
    """)
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
    
    st.title("Music Feature Descriptions")

    st.markdown("""
    The following features are commonly used to describe various characteristics of music tracks. They are often used in music information retrieval and recommendation systems.
    """)

    with st.expander("Acousticness"):
        st.markdown("""
        **Acousticness**: A measure of how acoustic a song is. Acousticness represents the likelihood of a track being played with acoustic instruments, as opposed to electronic or synthesized instruments. Higher values indicate a higher probability of the track being acoustic.
        """)

    with st.expander("Danceability"):
        st.markdown("""
        **Danceability**: A measure of how suitable a song is for dancing. This metric is based on several musical elements, such as tempo, rhythm stability, beat strength, and overall regularity. Higher values indicate that a song is more danceable.
        """)

    with st.expander("Energy"):
        st.markdown("""
        **Energy**: A measure of the intensity and activity of a song. Energetic tracks typically feel fast, loud, and noisy. This feature is based on various aspects like dynamic range, perceived loudness, timbre, onset rate, and general entropy. Higher values indicate more energetic songs.
        """)

    with st.expander("Instrumentalness"):
        st.markdown("""
        **Instrumentalness**: A measure of the absence of vocals in a track. Instrumentalness represents the likelihood that a track contains no vocal content (e.g., spoken word, rap, or singing). Higher values indicate a higher probability that the track is purely instrumental.
        """)

    with st.expander("Liveness"):
        st.markdown("""
        **Liveness**: A measure of the presence of an audience in the recording. Liveness detects the presence of a live audience, such as applause or crowd noise, and can differentiate between studio recordings and live concert recordings. Higher values indicate a higher probability of the track being a live recording.
        """)

    with st.expander("Speechiness"):
        st.markdown("""
        **Speechiness**: A measure of the presence of spoken words in a track. Speechiness detects the amount of spoken words or rapping in a song, as opposed to singing or instrumental content. Higher values indicate a higher proportion of spoken words in the track.
        """)

    with st.expander("Valence"):
        st.markdown("""
        **Valence**: A measure of the musical positiveness or happiness conveyed by a track. Valence describes the emotional content of a song, ranging from sad or depressed (low valence) to happy or euphoric (high valence). This feature is based on various musical aspects such as melody, harmony, lyrics, and rhythm.
        """)