import streamlit as st
import pandas as pd

def app(df: pd.DataFrame):
    st.title("Visualizing the Free Music Archive")
    st.subheader("Uncovering Patterns & Insights in Independent and Experimental Music Through Data Visualization Techniques")


    section = st.sidebar.radio("Choose a section", ["Introduction", "Related Work", "Data Description", "Research", "Results", "Conclusion"])
    
    if section == "Introduction":
        st.write("""
        ## 1. Introduction

        The Free Music Archive (FMA) is a vital resource for free, high-quality music in today's digital era. Curated by WFMU, a non-commercial radio station in New Jersey, the FMA promotes and preserves independent and experimental music that might otherwise remain undiscovered.

        As social media platforms have revolutionized how we share and consume music, the complexity of copyright laws has made it increasingly difficult to find legal, free music. This is where visualization techniques applied to the FMA dataset become highly relevant.
        """)

    elif section == "Related Work":
        st.write("""
        ## 2. Related Work

        The study of FMA Data Analysis includes research from various sources such as:

        1. The Music Information Retrieval Evaluation eXchange (MIREX) [1]
        2. Music Information Retrieval: Recent Developments and Applications [2]
        3. Visualizing Music: The Problems with Optical Scores [3]
        4. Visualizing Music: A Model for Studying the History of Music [4]
        5. Essentia: An Audio Analysis Library for Music Information Retrieval [5]
        6. Task Taxonomy for Graph Visualization [6]
        7. Music and Schema Theory: Cognitive Foundations of Systematic Musicology [7]
        8. Visualizing Music: Exploring the Use of Self-Organizing Maps for Music Genre Classification [8]
        9. A Meta-Instrument for Interactive, On-the-Fly Machine Learning [9]
        10. Social Tagging and Music Information Retrieval [10]
        """)

    elif section == "Data Description":
        st.write("""
        ## 3. Data Description

        The FMA dataset is organized into the following four subsets:

        1. FMA Small: 8,000 tracks across 8 genres, with a 30-second audio clip per track (4.5 GB)
        2. FMA Medium: 25,000 tracks across 16 genres, with a 30-second audio clip per track (13.5 GB)
        3. FMA Large: 106,574 tracks across 161 genres, with a 30-second audio clip per track (56.5 GB)
        4. FMA Full: 106,574 tracks across 161 genres, with full-length audio files (879 GB)
        """)

    elif section == "Research":
        st.write("""
        ## 4. Research

        By focusing on the visualization of the FMA dataset, we can delve deeper into the significance of free music in the context of social media and copyright challenges.
        """)

    elif section == "Results":
        st.write("""
        ## 5. Results

        Visualization techniques not only provide a clearer understanding of the music landscape but also highlight the importance of supporting independent and experimental artists.
        """)

    elif section == "Conclusion":
        st.write("""
        ## 6. Conclusion
        
        Through these efforts, we contribute to the ongoing discourse surrounding music, technology, and the value of free music resources like the FMA.
        
        """)
        