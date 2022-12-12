
import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import base64
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
from streamlit_extras.app_logo import add_logo
import requests



#Set initial page configurations
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)

#Condense with padding
padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

# Add background image    
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
    font-family: 'Showtime';
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

st.write("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Zen+Dots');
html, body, [class*="css"]  {
   font-family: 'Zen+Dots';
}
</style>
""", unsafe_allow_html=True)

# Add columns with logo and Omniflicks title

col1, mid, col2 = st.columns([2,1,8])
with col1:
    st.image("OmniFlicksLogo.png", width=110)

with col2:
    st.markdown('''
    <style>.showtime{
        font-size:60px; font-family: 'Showtime'
    }
    </style> ''', unsafe_allow_html=True)
    st.markdown('<h1 class="showtime">OmniFlicks</h1>', 
                unsafe_allow_html=True)

st.header('Top 6 movie recommendations based on popular and highly-rated titles')



@st.cache
def movie_recommender(movie_title):
    
    # find movie id
    index = highly_rated_movies.index[highly_rated_movies['title'] == movie_title][0]
    
    # get selected movie poster

    poster = f'https://image.tmdb.org/t/p/w500/{highly_rated_movies.loc[index,"poster_path"]}'
    
    
    
   # get movie similarities and sort descending
    similarity_scores = list(enumerate(
        cosine_similarity(tfidf_matrix,
                          tfidf_matrix[index])))
    
    # Sort descending based on scores
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    # get top 6 similar movies
    similarity_scores = similarity_scores[1:7]
    
    # Get movie indices
    indices = [i[0] for i in similarity_scores]
    
    # Return top 6 movies
    result = highly_rated_movies.iloc[indices]
    
    recommended_movie_titles = []
    recommended_movie_posters = []
    recommended_movie_descriptions = []
    
    # get recommendations movie titles, posters, descriptions
    
    for i, j in enumerate(result.poster_path):
        recommended_movie_titles.append(result.iloc[i].title)
        recommended_movie_posters.append(f'https://image.tmdb.org/t/p/w500/{j}')
        recommended_movie_descriptions.append(result.iloc[i].description)
    
    return poster, recommended_movie_titles, recommended_movie_posters, recommended_movie_descriptions


highly_rated_movies = pickle.load(open('movie_list.pkl', 'rb'))
tfidf_matrix = pickle.load(open('tfidf_matrix.pkl', 'rb'))
    

movies_list = highly_rated_movies['title'].values

selected_movie = st.selectbox('Type and Choose Movie', movies_list)


if st.button('Recommend'):
    
    poster,recommended_movie_titles,recommended_movie_posters,recommended_movie_descriptions = movie_recommender(selected_movie)
    st.markdown('''
    <style>.output_font{
        font-size:30px; font-family: 'Showtime'
    }
    </style> ''', unsafe_allow_html=True)
    st.markdown('<p class="output_font">Selected Movie</p>', 
                unsafe_allow_html=True)
    
    st.image(poster,width=160)
    
    st.markdown('<p class="output_font">Top 6 Recommendations</p>', 
                unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(recommended_movie_posters[0])
        st.markdown(recommended_movie_titles[0])
        with st.expander("Synopsis"):
            st.write(recommended_movie_descriptions[0])

        st.image(recommended_movie_posters[3])
        st.markdown(recommended_movie_titles[3])
        with st.expander("Synopsis"):
            st.write(recommended_movie_descriptions[3])

            
    with col2:
        st.image(recommended_movie_posters[1])
        st.markdown(recommended_movie_titles[1])
        with st.expander("Synopsis"):
            st.write(recommended_movie_descriptions[1])

        st.image(recommended_movie_posters[4])
        st.markdown(recommended_movie_titles[4])
        with st.expander("Synopsis"):
            st.write(recommended_movie_descriptions[4])

            
    with col3:
        st.image(recommended_movie_posters[2])
        st.markdown(recommended_movie_titles[2])
        with st.expander("Synopsis"):
            st.write(recommended_movie_descriptions[2])

        st.image(recommended_movie_posters[5])
        st.markdown(recommended_movie_titles[5])
        with st.expander("Synopsis"):
            st.write(recommended_movie_descriptions[5])
