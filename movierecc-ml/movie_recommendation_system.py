import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the data into a pandas dataframe
ratings = pd.read_csv('ratings.csv')

# Split the data into training and test sets
train_data, test_data = train_test_split(ratings, test_size=0.25)

# Create user-item matrices
train_matrix = train_data.pivot(index='userId', columns='movieId', values='rating')
test_matrix = test_data.pivot(index='userId', columns='movieId', values='rating')

# Fill missing values with 0
train_matrix_filled = train_matrix.fillna(0)

# Compute cosine similarity between users
user_similarity = cosine_similarity(train_matrix_filled)

# Create a DataFrame for user similarity
user_similarity_df = pd.DataFrame(user_similarity, index=train_matrix.index, columns=train_matrix.index)

# Load movies data
movies = pd.read_csv('movies.csv')

# Create a mapping from movieId to title
movie_titles = pd.Series(movies.title.values, index=movies.movieId).to_dict()

def get_movie_title(movie_id):
    return movie_titles.get(movie_id, "Unknown Title")

def predict_ratings(user_id):
    # Get the user's similarity scores
    user_similarities = user_similarity_df.loc[user_id]
    
    # Get the user's ratings
    user_ratings = train_matrix_filled.loc[user_id]
    
    # Compute the weighted average of ratings
    weighted_sum = np.dot(user_similarities, train_matrix_filled)
    sum_of_weights = np.array([np.abs(user_similarities).sum(axis=0)]).T
    
    # Avoid division by zero
    predicted_ratings = weighted_sum / (sum_of_weights + 1e-10)
    
    # Create a DataFrame for the predicted ratings
    predicted_ratings_df = pd.DataFrame(predicted_ratings, index=train_matrix.columns, columns=[user_id])
    
    return predicted_ratings_df

def get_recommendations(user_id, num_recommendations=5):
    # Predict ratings for the user
    predicted_ratings = predict_ratings(user_id)
    
    # Sort the predictions by rating
    sorted_predictions = predicted_ratings.sort_values(by=user_id, ascending=False)
    
    # Get the top 'num_recommendations' movie IDs
    top_movie_ids = sorted_predictions.head(num_recommendations).index.tolist()
    
    # Return the corresponding movie titles
    top_movie_titles = [get_movie_title(movie_id) for movie_id in top_movie_ids]
    
    return top_movie_titles

# Example usage
if __name__ == "__main__":
    user_id = 1
    print(get_recommendations(user_id))
