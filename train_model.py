import pandas as pd
import re
import string
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

dataset_path = "D:/Work/Project/Fake News Detection/Real Time/Real Time Sources/fake_or_real_news.csv"
df = pd.read_csv(dataset_path)

print("Columns in dataset:", df.columns)

df.columns = df.columns.str.strip()

print("Columns after stripping:", df.columns)

def clean_text(text):
    if not isinstance(text, str):  
        return ""  
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r'\w*\d\w*', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df['text'] = df['text'].fillna('')

df['text'] = df['text'].apply(clean_text)

X = df['text']

y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.4f}")
print("Classification Report:\n", classification_report(y_test, y_pred))

model_path = "D:/Work/Project/Fake News Detection/Real Time/Real Time Sources/fake_news_model.pkl"
vectorizer_path = "D:/Work/Project/Fake News Detection/Real Time/Real Time Sources/vectorizer.pkl"

joblib.dump(model, model_path)
joblib.dump(vectorizer, vectorizer_path)

print(f"Model saved to {model_path}")
print(f"Vectorizer saved to {vectorizer_path}")
