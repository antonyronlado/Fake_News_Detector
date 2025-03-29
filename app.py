from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import os
import logging
import nltk

nltk.download('punkt')

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__, static_folder=os.getcwd())
CORS(app)

def summarize_text(paragraph, sentence_count=3):
    try:
        logging.info(f"Summarizing text: {paragraph[:100]}...")

        if not paragraph or len(paragraph.split()) < 10:
            return "Text is too short to summarize."

        return extractive_summary(paragraph, sentence_count)

    except Exception as e:
        logging.error(f"Summarization failed: {e}")
        return basic_summarization(paragraph, sentence_count)

def extractive_summary(paragraph, sentence_count=3):
    parser = PlaintextParser.from_string(paragraph, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, sentence_count)

    summary_text = " ".join(str(sentence) for sentence in summary)
    return summary_text if summary_text.strip() else basic_summarization(paragraph, sentence_count)

def basic_summarization(paragraph, sentence_count=3):
    sentences = nltk.tokenize.sent_tokenize(paragraph)
    return " ".join(sentences[:sentence_count])

@app.route('/')
def serve_index():
    return send_from_directory(os.getcwd(), "index.html")

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.json
        paragraph = data.get("text", "").strip()

        if not paragraph:
            return jsonify({"error": "No text provided"}), 400

        summary = summarize_text(paragraph, sentence_count=3)
        return jsonify({"summary": summary})

    except Exception as e:
        logging.error(f"Error in /summarize: {e}", exc_info=True)
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
