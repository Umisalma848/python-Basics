# Import necessary libraries
import pandas as pd  # For handling data in tables
from sklearn.model_selection import train_test_split  # For splitting data into training and testing
from sklearn.feature_extraction.text import TfidfVectorizer  # For converting text to numbers
from sklearn.linear_model import LogisticRegression  # The machine learning model
from sklearn.metrics import accuracy_score  # To check how good our model is

# 1. Create a simple dataset with news texts and their labels
data = {
    'text': [
        'NASA faked the moon landing.',
        'Vaccines are effective for health.',
        'Aliens landed on Earth yesterday.',
        'Scientists found water on Mars.',
        'Drinking bleach cures illness.'
    ],
    'label': ['FAKE', 'REAL', 'FAKE', 'REAL', 'FAKE']
}
df = pd.DataFrame(data)  # Make a table from our data

# 2. Split the data into training and testing parts
X_train, X_test, y_train, y_test = train_test_split(
    df['text'],      # The news text
    df['label'],     # The label (FAKE or REAL)
    test_size=0.2,   # 20% of data for testing, 80% for training
    random_state=1   # For the same split every time
)

# 3. Convert the text to numbers using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')  # Ignore common words
X_train_tfidf = vectorizer.fit_transform(X_train)   # Learn from train data and convert
X_test_tfidf = vectorizer.transform(X_test)         # Convert test data (do NOT learn)

# 4. Create and train the Logistic Regression model
model = LogisticRegression()        # Pick the model
model.fit(X_train_tfidf, y_train)  # Train the model on numbers and labels

# 5. Test the model on the test data
y_pred = model.predict(X_test_tfidf)  # Predict FAKE or REAL for test data

# 6. See how well the model did
accuracy = accuracy_score(y_test, y_pred)  # Compare true and predicted labels
print(f"Accuracy: {accuracy:.2f}")         # Print the accuracy

# 7. Try the model on new, made-up news headlines
new_news = [
    'The government launches a new space mission.',
    'Scientists say chocolate cures all diseases.'
]
new_news_tfidf = vectorizer.transform(new_news)     # Convert new news to numbers
predictions = model.predict(new_news_tfidf)         # Predict FAKE or REAL
for headline, pred in zip(new_news, predictions):
    print(f"News: '{headline}' is predicted as: {pred}")