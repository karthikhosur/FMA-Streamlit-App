import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def app(df: pd.DataFrame):
    st.title("Producers Visualizations")

    # Bar chart: Top 10 most common producers
    top_producers = df['producer'].value_counts().nlargest(10)
    fig = px.bar(top_producers, x=top_producers.index, y=top_producers.values, labels={'x': 'Producer', 'y': 'Count'})
    fig.update_layout(title="Top 10 Most Common Producers")
    st.plotly_chart(fig)

    # Scatter plot: Relationship between producer and favorites
    producer_favorites = df.groupby('producer')['favorites'].mean().reset_index()
    fig = px.scatter(producer_favorites, x='producer', y='favorites')
    fig.update_layout(title="Producer vs. Favorites")
    st.plotly_chart(fig)


    # Select the 'producer' and 'listens' columns and group by 'producer'
    df_producer = df[['producer', 'listens']].groupby('producer').sum().reset_index()

    # Sort by 'listens' in descending order and select the top 10 producers
    df_top_producers = df_producer.sort_values('listens', ascending=False)[:10]

    # Create a histogram using Plotly Express
    fig = px.histogram(df_top_producers, x='producer', y='listens', 
                    nbins=len(df_top_producers), 
                    labels={'producer': 'Producer', 'listens': 'Number of Listens'},
                    title='Top 10 Producers by Number of Listens')
    st.plotly_chart(fig)

    # Word cloud
    text = " ".join(df['producer'].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400, max_words=50, background_color='white').generate(text)

    # Plot word cloud
    plt.figure(figsize=(16, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    # Display in Plotly
    fig = go.Figure(go.Image(z=wordcloud.to_array()))
    fig.update_layout(title="Word Cloud of Producers")
    st.plotly_chart(fig)

  