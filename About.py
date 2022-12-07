
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


st.set_page_config(layout='wide')
st.title('About OmniFlicks')

    
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

st.markdown('**_GitHub_** - Link to GitHub documents')


