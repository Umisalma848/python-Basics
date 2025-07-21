import pandas as pd
import numpy as np
import re
import string

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load your data (assume a CSV with 'text' and 'label' columns)
def load_data(csv_path):
    df = pd.read_csv(csv_path)
    df = df[['text', 'label']]
    return df

# Clean the text data
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

# Main function for fake news detection
def fake_news_detector(csv_path):
    df = load_data(csv_path)
    df['text'] = df['text'].apply(clean_text)
    
    X = df['text']
    y = df['label']
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Vectorize text data
    tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)
    tfidf_train = tfidf.fit_transform(X_train)
    tfidf_test = tfidf.transform(X_test)
    
    # Train PassiveAggressiveClassifier
    pac = PassiveAggressiveClassifier(max_iter=50)
    pac.fit(tfidf_train, y_train)
    
    # Predict on the test set
    y_pred = pac.predict(tfidf_test)
    
    # Accuracy and report
    score = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {round(score*100,2)}%')
    print('Classification Report:')
    print(classification_report(y_test, y_pred))
    print('Confusion Matrix:')
    print(confusion_matrix(y_test, y_pred))

if __name__ == '__main__':
    # Replace 'news.csv' with your dataset file path
    fake_news_detector('news.csv')