import streamlit as st
import pickle as pkl
import pandas as pd
import requests


# creating function to get poster of the movie
def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=d67981a83ab075de75c2c3ce7d417f40&language=en-US'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    
    return full_path




# creating function recommend: if one movie is mentioned, this function will give 5 similar movies
def recommend(movie):
    index = movies[movies['title']== movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse = True, key= lambda x:x[1])

    recommended_movies, movie_poster = [], []

    for i in distances[1:6]:
        index = movies[movies['title'] == movie].index[0]
        movie_id = movies.iloc[i[0]].movie_id
        
        recommended_movies.append(movies.iloc[i[0]].title) #getting the title of similar movie  
        movie_poster.append(fetch_poster(movie_id))  #fetch poster from API

    return recommended_movies, movie_poster


# loading movies and similarity pkl file
movies = pkl.load(open('data/movies_list.pkl', 'rb'))
similarity = pkl.load(open('data\similarity.pkl', 'rb'))
st.title("Movie Recommendation System")

movie_list = movies['title'].values
selected_movie = st.selectbox("Please select or type the movie from the dropdown", movie_list)

if st.button("Submit"):
    recommended_movies, movie_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(movie_poster[0])

    with col2:
        st.text(recommended_movies[1])
        st.image(movie_poster[1])
    
    with col3:
        st.text(recommended_movies[2])
        st.image(movie_poster[2]) 

    with col4:
        st.text(recommended_movies[3])
        st.image(movie_poster[3])
           
    with col5:
        st.text(recommended_movies[4])
        st.image(movie_poster[4])
        