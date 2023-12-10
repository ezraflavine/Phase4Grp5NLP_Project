# app.py

import streamlit as st
import re
import nltk
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Download NLTK resources (do this once)
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')

# Load the pre-trained models and objects
GBM_tuned = pickle.load(open('GBM_tuned.pkl', 'rb'))
tfidf_vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))
smote = pickle.load(open('smote.pkl', 'rb'))

# Function to clean text
def clean_the_text(text):
    # Removing numbers
    text = re.sub(r'\d+', '', text)
    # Removing special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I | re.A)
    # Removing words with repeated characters
    text = re.sub(r'\b(\w)\1+\b', '', text)

    # Tokenizing text
    tokens = text.lower().split()

    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Lemmatizing
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return ' '.join(tokens)

# Function to predict using the tuned GBM model
def predict_hate_speech(tweet):
    cleaned_tweet = clean_the_text(tweet)
    tfidf_vectorized = tfidf_vectorizer.transform([cleaned_tweet])
    prediction = GBM_tuned.predict(tfidf_vectorized)[0]

    # Mapping dictionary for class labels
    class_labels = {0: "Not Hate Speech", 1: "Hate Speech"}

    return prediction, class_labels.get(prediction, "Unknown")

# Streamlit App
st.title("Hate Speech Identification App")

# User Input
user_input = st.text_input("Enter a tweet:")

# Prediction
if st.button("Predict"):
    if user_input:
        prediction, label = predict_hate_speech(user_input)
        st.success(f"The predicted class is: {prediction} - {label}")
    else:
        st.warning("Please enter a tweet for prediction.")