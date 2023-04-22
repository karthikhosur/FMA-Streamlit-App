import streamlit as st
import pandas as pd
import altair as alt

def app(df: pd.DataFrame):
    st.title("Data Display")

    # Display DataFrame
    st.header("Data")
    st.write(df)

    # Display number of rows and columns
    st.header("Number of Rows and Columns")
    st.markdown(f"**Rows:** {df.shape[0]}")
    st.markdown(f"**Columns:** {df.shape[1]}")

    # Display DataFrame columns
    st.header("Columns")
    columns = ", ".join(df.columns)
    st.markdown(f"`{columns}`")

    # Display data types
    st.header("Data Types")
    st.write(df.dtypes)

    # Display descriptive statistics
    st.header("Descriptive Statistics")
    st.write(df.describe())

    # Display a bar chart of the count of unique values per column
    st.header("Unique Values per Column")
    unique_counts = df.nunique().reset_index().rename(columns={'index': 'Column', 0: 'Unique Values'})
    chart = alt.Chart(unique_counts).mark_bar().encode(
        x='Column',
        y='Unique Values',
        tooltip=['Column', 'Unique Values']
    ).properties(width=600, height=400)
    st.altair_chart(chart)
