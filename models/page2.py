import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np

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

    # Create the figure for the track count data
    fig = px.line(x=year_counts.index, y=year_counts.values, labels={'x': 'Year Created', 'y': 'Count'}, title='Count of Tracks by Year Created and GDP Growth Rate')

    # Add a second y-axis for the GDP growth rate data
    fig.update_layout(
        yaxis2=dict(title='GDP Growth Rate (%)', overlaying='y', side='right', showgrid=False)
    )

    # Add GDP growth rate data to the figure
    x_data = np.arange(2008, 2016)
    y_data = [0.122188, -2.599888, 2.708857, 1.549895, 2.280688, 1.841875, 2.287776, 2.7063]
    fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines', yaxis='y2', name='GDP Growth Rate'))

    # Update the layout
    fig.update_layout(
        title='Count of Tracks by Year Created and GDP Growth Rate',
        xaxis_title='Year',
    )

    # Display the chart
    st.write("This combined line chart shows the number of tracks created each year in the FMA dataset (left y-axis) and the GDP growth rate from 2008 to 2016 (right y-axis). The x-axis represents the years.")
    st.plotly_chart(fig)

    # # Visualization 2: Count of Tracks by Year Created
    # df['year_created'] = pd.DatetimeIndex(df['date_created']).year
    # year_counts = df['year_created'].value_counts().sort_index()
    # fig2 = px.line(x=year_counts.index, y=year_counts.values, labels={'x':'Year Created', 'y':'Count'}, title='Count of Tracks by Year Created')
    # st.write("This line chart shows the number of tracks created each year in the FMA dataset. The x-axis represents the years and the y-axis represents the count of tracks created in each year.")
    # st.plotly_chart(fig2)
    
    # x_data = np.arange(2008, 2017)
    # y_data = [0.122188, -2.599888, 2.708857, 1.549895, 2.280688, 1.841875, 2.287776, 2.70637, 1.667472]
    # fig = go.Figure(data=go.Scatter(x=x_data, y=y_data, mode='lines'))
    # fig.update_layout(title='GDP Growth Rate from 2008 to 2016',
    #                xaxis_title='Year',
    #                yaxis_title='GDP Growth Rate (%)')
    # st.plotly_chart(fig)
    
    # Visualization 3: Count of Different Music Release Types
    fig3 = px.histogram(df, x='type', labels={'x':'Type', 'y':'Count'}, title='Count of Different Music Release Types')
    st.write("This histogram shows the count of different music release types in the FMA dataset. The x-axis represents the different types of music release and the y-axis represents the count of each type.")
    st.plotly_chart(fig3)
    
    

    # Visualization 4: Count of Different Bit Rates
    fig4 = px.histogram(df, x='bit_rate', labels={'x':'Bit Rate', 'y':'Count'}, title='Count of Different Bit Rates')
    st.write("This histogram shows the count of different bit rates in the FMA dataset. The x-axis represents the different bit rates and the y-axis represents the count of each bit rate.In digital audio and video, bit rate refers to the amount of data used to represent a given period of sound or video. A higher bit rate generally results in better quality audio or video, but also requires more storage space and may require higher bandwidth for transmission.")
    st.plotly_chart(fig4)
