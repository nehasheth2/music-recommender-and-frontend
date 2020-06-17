import numpy as np
import pandas as pd
import streamlit as st 

st.title('Music Recommendation System')
st.write('by *Neha Sheth*')
st.markdown('<style> div {background-color: #ccffcc;}</style>', unsafe_allow_html=True)

@st.cache
def load_data():
    df = pd.read_csv("df.csv")
    return df
   
@st.cache
def load_item():
    item_similarity_df = pd.read_csv("item_similarity_df.csv")
    return item_similarity_df.values

df = load_data()
item_similarity_df = load_item()
  
@st.cache
def loaddemo():
    dfdemo = pd.read_csv("dfdemo.csv")
    return dfdemo

dfdemo = loaddemo()
st.subheader("Here are the songs available - ")
st.dataframe(dfdemo)
   
@st.cache
def get_title_from_index(index):
    return df[df.index== index]["name"].values[0]

@st.cache
def get_index_from_title(name):
    return df[df.name == name]["index"].values[0]

@st.cache
def get_artist_from_index(index):
    return df[df.index== index]["artist"].values[0]

@st.cache
def get_index_from_artist(artist):
    return df[df.artist == artist]["index"].values[0]

choice = st.selectbox('What would you like your music recommendations based on?', ('Artist Name', 'Song Name'))

st.write("You selected", choice)


if choice == 'Artist Name' :
    artist_user_likes = st.text_input("Please refer to database and type name of artist to get recommendations on", 'Led Zeppelin')
    st.write("Artist selected is", artist_user_likes)
    song_index = get_index_from_artist(artist_user_likes)
    similar_songs = list(enumerate(item_similarity_df[song_index]))
    
    sorted_similar_songs = sorted(similar_songs,key=lambda x:x[1],reverse=True)[1:]
    i=0
    st.subheader("Top 10 similar songs to "+artist_user_likes+ " are -")
    for element in sorted_similar_songs:
        x=str(get_title_from_index(element[0]))
        y=str(get_artist_from_index(element[0]))
        st.write(x + " by " + y)
        i=i+1
        if i>10:
            break   
        
    
elif choice =='Song Name':
    song_user_likes = st.text_input("Please refer to database and type name of song to get recommendations on", "Stairway To Heaven")
    st.write("Song selected is", song_user_likes)
    song_index = get_index_from_title(song_user_likes)
    similar_songs = list(enumerate(item_similarity_df[song_index]))
        
    sorted_similar_songs = sorted(similar_songs,key=lambda x:x[1],reverse=True)[1:]
    i=0
    st.subheader("Top 10 similar songs to "+ song_user_likes+ " are -")
    for element in sorted_similar_songs:
        x=str(get_title_from_index(element[0]))
        y=str(get_artist_from_index(element[0]))
        st.write(x + " by " + y)
        i=i+1
        if i>10:
            break
else:
    st.write("Wrong Choice")