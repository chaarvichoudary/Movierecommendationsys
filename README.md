Movie Recommendation System using Machine Learning

This Movie Recommendation System is built using collaborative filtering techniques in Python. It suggests movies to users based on their past preferences and behavior, without relying on explicit ratings or content features.

Key Features:

Collaborative Filtering: The system analyzes user-item interaction data to identify patterns and similarities among users and items. It then recommends movies to users based on the preferences of similar users.

User-Item Matrices: The data is represented as user-item matrices, where each cell represents a user's rating for a particular movie. These matrices are used to compute similarities between users and items.

Cosine Similarity: The system calculates cosine similarity between users to measure how alike they are in terms of their movie preferences. This similarity score is then used to predict ratings for unseen movies.

Predictive Modeling: Predictive models are trained using the training data to estimate ratings for movies that users haven't watched yet. These predicted ratings are used to generate personalized movie recommendations.

Web Application: The recommendation system is deployed as a web application using Flask, allowing users to input their user ID and receive personalized movie recommendations.

How to Use:

Open your web browser and navigate to https://movierecommendationsys-7.onrender.com/ .

Input User ID: Users input their user ID into the web application.

Receive Recommendations: The system processes the user ID and generates a list of recommended movies based on the user's preferences and behavior.

Explore Recommendations: Users can explore the recommended movies and choose to watch them based on their interests.




