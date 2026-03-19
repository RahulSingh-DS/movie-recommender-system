import streamlit as st
import pickle
import pandas as pd


# Page Config

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 Movie Recommender System")
st.markdown("Get top 5 movie recommendations instantly 🚀")


# Load Data

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


# Recommendation Function

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# UI - Dropdown

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "🎥 Select a movie",
    movie_list
)


# Button

if st.button("Recommend 🎯"):

    recommendations = recommend(selected_movie)

    st.subheader("✨ Top Recommendations:")

    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")