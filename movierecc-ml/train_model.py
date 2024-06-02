import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.model_selection import train_test_split

# Load the data into a pandas dataframe
ratings = pd.read_csv('ratings.csv')

# Split the data into training and test sets
train_data, test_data = train_test_split(ratings, test_size=0.25)

# Create user-item matrices
train_matrix = train_data.pivot(index='userId', columns='movieId', values='rating')
test_matrix = test_data.pivot(index='userId', columns='movieId', values='rating')

# Center the data by subtracting the mean rating
mean_user_rating = train_data.groupby(by='userId')['rating'].mean()
train_matrix_centered = train_matrix.sub(mean_user_rating, axis=0)

# Perform Singular Value Decomposition (SVD)
n_components = 50  # Number of latent factors
svd = TruncatedSVD(n_components=n_components, random_state=42)
U = svd.fit_transform(train_matrix_centered)
Vt = svd.components_

# Reconstruct the original matrix
predicted_ratings = np.dot(U, Vt) + mean_user_rating.values.reshape(-1, 1)
