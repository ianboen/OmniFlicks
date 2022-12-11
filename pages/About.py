
import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import numpy as np
import pandas as pd
import base64
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
from streamlit_extras.app_logo import add_logo


def add_bg_from_local(image_file):
    with open(image_file, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp{{
        background-image: url(data:image/{'jpeg'};base64,{encoded_string.decode()});
        background-size: cover;
    }}
    <style/>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('movie_background.jpeg')

# Update sidebar
updated_sidebar = '''
    <style>
    #stSidebarNav {
    font-family: "Showtime"
    }
    </style>
    '''
    
st.markdown('''
    <style>
        [data-testid="stSidebarNav"] {
        font-family: 'Showtime';
        }
        [data-testid="stSidebarNav"]::before {
        content: "OmniFlicks";
        margin-left: 20px;
        margin-top: 20px;
        font-size: 30px;
        position: relative;
        }
    </style>
    ''', unsafe_allow_html=True)


# Add columns with logo and Omniflicks title
col1, mid, col2 = st.columns([2,1,8])
with col1:
    st.image("OmniFlicksLogo.png", width=110)

with col2:
    st.markdown('''
    <style>.font{
        font-size:60px; font-family: 'Showtime'
    }
    </style> ''', unsafe_allow_html=True)
    st.markdown('<h1 class="font">About OmniFlicks</h1>', 
                unsafe_allow_html=True)

    


st.write('**_GitHub_** - [Link](https://github.com/ianboen/OmniFlicks) to GitHub documents')
st.write('''**About** - OmniFlicks pulls movie data from Movies Daily Update Dataset via _Kaggle.com_. The dataset originates from TMDb.
         \nThe application generates recommendations for the top 6 movies of a chosen title.
         \nNatural Language Processing (NLP) is used to generate content-based recommendations by creating cosine similarity values with Term Frequency-Inverse Document Frequency (TF-IDF) for all movie descriptions.
         \n**Future Enhancements** - Hybrid recommendations utilizing user- and- content-based filtering;
         User Accounts;
         API references for other sites such as OMDB;
         Functionality to determine streaming platforms for which each movie is currently streaming
         \n**Source:** https://www.kaggle.com/code/rohitshirudkar/movie-recommendation-system/data''')

st.write('''All film metadata used in **OmniFlicks** even from the Kaggle.com dataset comes from The Movie Database (TMDb).

**OmniFlicks** is not endorsed or certified by [TMDb](https://www.themoviedb.org/?language=en-US).

![image](https://user-images.githubusercontent.com/106556575/206061975-289af154-3e23-4ddb-b31e-7803cfe3c800.png)''')
