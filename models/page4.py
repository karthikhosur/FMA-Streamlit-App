import streamlit as st
import pandas as pd
import plotly.express as px

def app(df: pd.DataFrame):
    st.title("USA Map")

    # Filter the DataFrame to include only the data within the boundaries of the USA
    usa_df = df[(df['latitude'] >= 24.396308) & (df['latitude'] <= 49.384358) &
                (df['longitude'] >= -125.000000) & (df['longitude'] <= -66.934570)]

    # Create a scatter plot using latitude and longitude
    fig = px.scatter_geo(usa_df, lat='latitude', lon='longitude', hover_name='title', color='genre_top')

    # Customize the appearance of the map
    fig.update_layout(title='Geographic Distribution of Music in the USA',
                      geo=dict(scope='usa',
                               showland=True, landcolor='rgb(217, 217, 217)',
                               subunitcolor='rgb(255, 255, 255)', countrycolor='rgb(255, 255, 255)',
                               showlakes=True, lakecolor='rgb(255, 255, 255)',
                               showsubunits=True, showcountries=True,
                               projection=dict(type='albers usa'),
                               bgcolor='white'))

    # Show the map
    st.plotly_chart(fig)
    
    fig = px.scatter_geo(df, lat='latitude', lon='longitude', hover_name='title', color='genre_top')

    # Customize the appearance of the map
    fig.update_layout(title='Geographic Distribution of Music', geo=dict(showland=True, landcolor='rgb(217, 217, 217)',
                                                        subunitcolor='rgb(255, 255, 255)', countrycolor='rgb(255, 255, 255)',
                                                        showlakes=True, lakecolor='rgb(255, 255, 255)',
                                                        showsubunits=True, showcountries=True,
                                                        projection=dict(type='natural earth'), coastlinewidth=0.5, lataxis=dict(range=[-90, 90]),
                                                        lonaxis=dict(range=[-180, 180]), bgcolor='white'))

    # Show the map
    st.plotly_chart(fig)
    st.write("The visualization displays the geographic distribution of music in the USA and worldwide. ")
