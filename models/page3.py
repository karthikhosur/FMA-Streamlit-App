import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def app(df: pd.DataFrame):
    st.title("Producers Visualizations")

    # Bar chart: Top 10 most common producers
    st.write("This bar chart shows the top 10 most common producers in the dataset, based on the number of times they appear.")
    top_producers = df['producer'].value_counts().nlargest(10)
    fig = px.bar(top_producers, x=top_producers.index, y=top_producers.values, labels={'x': 'Producer', 'y': 'Count'})
    fig.update_layout(title="Top 10 Most Common Producers")
    st.plotly_chart(fig)

    # Scatter plot: Relationship between producer and favorites
    st.write("This scatter plot shows the relationship between producers and the average number of favorites their tracks receive.")
    producer_favorites = df.groupby('producer')['favorites'].mean().reset_index()
    fig = px.scatter(producer_favorites, x='producer', y='favorites')
    fig.update_layout(title="Producer vs. Favorites")
    st.plotly_chart(fig)

    # Histogram: Top 10 producers by number of listens
    st.write("This histogram shows the top 10 producers in the dataset based on the total number of listens their tracks have received.")
    df_producer = df[['producer', 'listens']].groupby('producer').sum().reset_index()
    df_top_producers = df_producer.sort_values('listens', ascending=False)[:10]
    fig = px.histogram(df_top_producers, x='producer', y='listens', 
                    nbins=len(df_top_producers), 
                    labels={'producer': 'Producer', 'listens': 'Number of Listens'},
                    title='Top 10 Producers by Number of Listens')
    st.plotly_chart(fig)

    # Word cloud: Producers
    st.write("This word cloud shows the most frequent producers in the dataset, based on the number of times their tracks appear.")
    text = " ".join(df['producer'].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400, max_words=50, background_color='white').generate(text)
    plt.figure(figsize=(16, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    fig = go.Figure(go.Image(z=wordcloud.to_array()))
    fig.update_layout(title="Word Cloud of Producers")
    st.plotly_chart(fig)
