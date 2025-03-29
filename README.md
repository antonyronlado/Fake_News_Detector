# FakeOut - Fake News Detection System

## Overview
FakeOut is an AI-powered fake news detection website that helps users verify the credibility of news articles. It utilizes advanced machine learning models to analyze text and determine whether a piece of news is real or fake. The project is designed to combat misinformation, promote factual reporting, and provide users with a comprehensive analysis of news content.

## Features
- **AI-Powered Fake News Detection**: Analyzes the credibility of news articles using advanced machine learning models.
- **Article Summarization**: Generates concise summaries of news articles for quick understanding.
- **AI Chatbot**: Assists users in analyzing news, answering queries, and providing explanations about fake news detection.
- **User-Friendly Interface**: Designed with Tailwind CSS for a clean, responsive, and interactive experience.
- **Real-Time Analysis**: Allows users to input text or URLs to check the authenticity of news articles instantly.
- **Interactive Results Display**: Provides detailed insights, including a confidence score and reasoning behind the classification.
- **Multi-Language Support (Upcoming Feature)**: Future plans to support multiple languages for broader accessibility.

## Technologies Used
### Frontend
- **Tailwind CSS**: For responsive and modern UI design.
- **HTML, JavaScript**: Core web technologies for structure and interactivity.

### Backend
- **Python (Flask/Django)**: Manages API endpoints and backend logic.
- **Machine Learning Models**: Implements NLP-based classification techniques:
  - **BERT (Bidirectional Encoder Representations from Transformers)**
  - **TF-IDF with Logistic Regression**

### Data Collection
- **Web Scraping Model**: Extracts news articles from various online sources for real-time fake news detection.
- **OpenAI API (or equivalent)**: Powers the AI chatbot for enhanced interactions.

## Installation & Setup
Follow these steps to set up FakeOut on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/antonyronlado/Fake_News_Detector.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd fakeout
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Train the Machine Learning Model**:
   Run the training script to generate necessary data files for the backend.
   ```bash
   python train_model.py
   ```
5. **Ensure API Key Integration**:
   - Add your API key to the AI chatbot before running the service.
   - This step is crucial for enabling chatbot functionality.

6. **Run the Application Servers**:
   The `run_service.py` file will start both the backend and frontend services.
   ```bash
   python run_service.py
   ```
7. **Access the Website**:
   - Open your browser and go to `http://localhost:5000`

## Usage Guide
1. **Fake News Detection**:
   - Enter a news article or provide a URL.
   - Click the "Analyze" button.
   - View the result, including a confidence score and classification as real or fake.

2. **Article Summarization**:
   - Enter a news article to get a concise summary.
   - Useful for quickly understanding long articles.

3. **AI Chatbot Assistance**:
   - Ask questions about news credibility.
   - Get explanations about how the detection system works.
   - Engage in real-time discussions about misinformation.

## Contributing
We welcome contributions! Follow these steps to contribute:
1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature-branch
   ```
3. **Make your changes and commit them**:
   ```bash
   git commit -m "Add new feature"
   ```
4. **Push to your fork**:
   ```bash
   git push origin feature-branch
   ```
5. **Create a pull request**.

## Contact
For any inquiries or support, contact antonyronaldoa2006@gmail.com .

