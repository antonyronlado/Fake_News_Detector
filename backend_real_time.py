from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import joblib
import requests
from bs4 import BeautifulSoup
from googlesearch import search

# Load trained model & vectorizer
model_path = "D:/Work/Project/Fake News Detection/Real Time/Real Time Sources/fake_news_model.pkl"
vectorizer_path = "D:/Work/Project/Fake News Detection/Real Time/Real Time Sources/vectorizer.pkl"

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

app = FastAPI()

# ✅ Enable CORS properly
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all frontend requests
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, etc.
    allow_headers=["*"],  # Allows all headers
)

# ✅ Fix Google Search Function
def get_news_sources(query):
    search_results = list(search(query, num_results=5))  # Updated argument name
    sources = {}
    for url in search_results:
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            text = ' '.join([p.text for p in soup.find_all('p')])
            sources[url] = text[:500]  # Store first 500 characters
        except:
            continue
    return sources

@app.get("/predict/")
async def predict_news(news_text: str):
    if not news_text:
        raise HTTPException(status_code=400, detail="News text is required")

    # Convert text to feature vector
    transformed_text = vectorizer.transform([news_text])
    prediction = model.predict(transformed_text)[0]

    # Get real-time news sources
    sources = get_news_sources(news_text)

    return {"prediction": prediction, "sources": sources}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
