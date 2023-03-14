import pandas as pd
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


df = pd.read_csv('echonest.csv')

print(df.head())

features = df[["track_id", "acousticness","danceability","energy","instrumentalness","liveness","speechiness","tempo","valence"]]
metadata = df[["track_id","album_date","album_name","artist_latitude","artist_location","artist_longitude","artist_name","release","artist_discovery_rank","artist_familiarity_rank","artist_hotttnesss_rank","song_hotttnesss_rank","artist_discovery","artist_familiarity","artist_hotttnesss","song_hotttnesss"]]

location = metadata[["artist_latitude","artist_longitude","artist_location"]]
# location.columns=['lat','lon']
# st.map(location, use_container_width=True)
fig = px.scatter_mapbox(location, lat="artist_latitude", lon="artist_longitude",color="artist_location", zoom=3)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)

fig=make_subplots(rows=4,cols=2,subplot_titles=( '<i>danceability', '<i>energy','<i>instrumentalness',  '<i>speechiness', '<i>acousticness', '<i>liveness', '<i>valence', '<i>tempo'))
fig.add_trace(go.Histogram(x=df['danceability'],name='danceability'),row=1,col=1)
fig.add_trace(go.Histogram(x=df['energy'],name='energy'),row=1,col=2)
fig.add_trace(go.Histogram(x=df['speechiness'],name='speechiness'),row=2,col=1)
fig.add_trace(go.Histogram(x=df['acousticness'],name='acousticness'),row=2,col=2)
fig.add_trace(go.Histogram(x=df['liveness'],name='liveness'),row=3,col=1)
fig.add_trace(go.Histogram(x=df['valence'],name='valence'),row=3,col=2)
fig.add_trace(go.Histogram(x=df['tempo'],name='tempo'),row=4,col=1)
fig.update_layout(height=900,width=900,title_text='<b>Feature Distribution')
fig.update_layout(template='plotly_dark',title_x=0.5)
st.plotly_chart(fig)

fig = px.bar(df.groupby('artist_name',as_index=False).count().sort_values(by='track_id',ascending=False).head(50),x='artist_name',y='track_id',labels={'track_id':'Total Songs'},width=1000,color_discrete_sequence=['green'],text='track_id',title='<b> List of Songs Recorded by Each Singer')
st.plotly_chart(fig)


fig = px.scatter(df,x='tempo',y='song_hotttnesss',template='plotly_dark',title='<b>Tempo Versus Popularity')
st.plotly_chart(fig)

fig = px.scatter(df,x='danceability',y='song_hotttnesss',template='plotly_dark',title='<b>danceability Versus Popularity')
st.plotly_chart(fig)
fig = px.scatter(df,x='energy',y='song_hotttnesss',template='plotly_dark',title='<b>energy Versus Popularity')
st.plotly_chart(fig)
fig = px.scatter(df,x='speechiness',y='song_hotttnesss',template='plotly_dark',title='<b>speechiness Versus Popularity')
st.plotly_chart(fig)
fig = px.scatter(df,x='acousticness',y='song_hotttnesss',template='plotly_dark',title='<b>acousticness Versus Popularity')
st.plotly_chart(fig)
fig = px.scatter(df,x='liveness',y='song_hotttnesss',template='plotly_dark',title='<b>liveness Versus Popularity')
st.plotly_chart(fig)
fig = px.scatter(df,x='valence',y='song_hotttnesss',template='plotly_dark',title='<b>valence Versus Popularity')
st.plotly_chart(fig)