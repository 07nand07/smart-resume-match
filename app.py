from flask import Flask, render_template, request
import pandas as pd
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import re
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

app = Flask(__name__)

df_jobs = pd.read_csv("jobs_large_dataset.csv")

def clean_text(text):
    stop_words = set(stopwords.words('english'))
    text = re.sub(r'\W+', ' ', text.lower())
    return ' '.join([word for word in text.split() if word not in stop_words])

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['resume']
        if file and file.filename.endswith('.pdf'):
            resume_text = extract_text_from_pdf(file)
            resume_cleaned = clean_text(resume_text)
            df_jobs['cleaned'] = df_jobs['Job Description'].apply(clean_text)

            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform([resume_cleaned] + df_jobs['cleaned'].tolist())
            scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
            df_jobs['Match Score (%)'] = (scores * 100).round(2)

            matches = df_jobs.sort_values(by='Match Score (%)', ascending=False)[['Job Title', 'Match Score (%)']].head(3)

            return render_template('index.html', matches=matches.to_dict(orient='records'))
        else:
            return "Please upload a .pdf file only."
    return render_template('index.html', matches=None)

if __name__ == '__main__':
    app.run(debug=True)
