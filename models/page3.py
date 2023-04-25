import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def app(df: pd.DataFrame):
    st.title("Producers Trends")

    # Add a slider to select the number of producers, default to 50
    num_producers = st.slider("Select the number of top producers to display:", min_value=1, max_value=100, value=50)

    # Bar chart: Top N most common producers
    st.write(f"This bar chart shows the top {num_producers} most common producers in the dataset, based on the number of times they appear.")
    top_producers = df['producer'].value_counts().nlargest(num_producers)
    fig = px.bar(top_producers, x=top_producers.index, y=top_producers.values, labels={'x': 'Producer', 'y': 'Count'})
    fig.update_layout(title=f"Top {num_producers} Most Common Producers")
    st.plotly_chart(fig)

    # Scatter plot: Relationship between producer and favorites
    st.write(f"This scatter plot shows the relationship between the top {num_producers} producers (based on count) and the average number of favorites their tracks receive.")

    # Group the data by 'producer' and calculate the average 'favorites'
    producer_favorites = df.groupby('producer')['favorites'].mean().reset_index()

    # Count the number of tracks by each producer
    producer_counts = df['producer'].value_counts().reset_index()
    producer_counts.columns = ['producer', 'track_count']

    # Merge the average favorites and track count DataFrames
    producer_summary = pd.merge(producer_favorites, producer_counts, on='producer')

    # Sort the merged DataFrame by track count and select the top N producers
    top_producers = producer_summary.sort_values(by='track_count', ascending=False).head(num_producers)

    # Create a scatter plot using Plotly Express
    fig = px.scatter(top_producers, x='producer', y='favorites', hover_name='producer', size='track_count')
    fig.update_layout(title=f"Top {num_producers} Producers vs. Favorites")

    st.plotly_chart(fig)

    # Histogram: Top N producers by number of listens
    st.write(f"This bar chart shows the top {num_producers} producers in the dataset based on the total number of listens their tracks have received.")

    # Group the data by 'producer' and calculate the total 'listens'
    df_producer = df[['producer', 'listens']].groupby('producer').sum().reset_index()

    # Get the top N producers based on listens
    df_top_producers = df_producer.sort_values('listens', ascending=False)[:num_producers]

    # Create a bar chart using Plotly Express with custom colors
    fig = px.bar(df_top_producers, x='producer', y='listens',
                labels={'producer': 'Producer', 'listens': 'Number of Listens'},
                title=f'Top {num_producers} Producers by Number of Listens',
                color='listens',
                color_continuous_scale=px.colors.sequential.Bluered)

    # Customize the appearance of the chart
    fig.update_layout(coloraxis_showscale=False)

    st.plotly_chart(fig)

    # Word cloud: Producers
    st.write("This word cloud shows the most frequent producers in the dataset, based on the number of times their tracks appear.")
    text = " ".join(df_top_producers['producer'].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400, max_words=50, background_color='white').generate(text)
    plt.figure(figsize=(16, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    fig = go.Figure(go.Image(z=wordcloud.to_array()))
    fig.update_layout(title="Word Cloud of Producers")
    st.plotly_chart(fig)
