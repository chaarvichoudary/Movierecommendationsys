
import streamlit as st
import pickle

# Load the model
model = pickle.load(open('saved_model.pkl', 'rb'))

st.title("Movie Recommendation System")

st.header("Enter the features to get a movie recommendation")

# Collect user input features
sepal_length = st.number_input('Sepal Length', min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input('Sepal Width', min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input('Petal Length', min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input('Petal Width', min_value=0.0, max_value=10.0, step=0.1)

# Predict button
if st.button('Predict'):
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    st.write(f'The predicted class is: {int(prediction[0])}')

if __name__ == '__main__':
    st.run()
