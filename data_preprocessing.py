import pandas as pd
from sklearn.model_selection import train_test_split

# Load the MovieLens dataset
ratings = pd.read_csv('ratings.csv')

# Split the data into training and test sets
train_data, test_data = train_test_split(ratings, test_size=0.2, random_state=42)

# Print the shapes of the train and test data
print("Training data shape:", train_data.shape)
print("Testing data shape:", test_data.shape)
