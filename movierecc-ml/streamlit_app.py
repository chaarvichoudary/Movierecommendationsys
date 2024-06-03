import streamlit as st
import pickle
import pandas as pd

# Load the model
model = pickle.load(open('movierecc-ml/saved_model1.pkl', 'rb'))

st.title("Movie Recommendation System")

# Dummy Data for Movies and Users
movies = ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"]
users = range(1, 11)

# Function to recommend movies
def recommend_movies(user_id):
    # Dummy logic to recommend movies for a user
    return [movies[i % len(movies)] for i in range(user_id, user_id + 5)]

# User input
user_id = st.number_input("Enter User ID", min_value=1, max_value=len(users))

if st.button("Recommend"):
    recommendations = recommend_movies(user_id)
    st.write("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)
