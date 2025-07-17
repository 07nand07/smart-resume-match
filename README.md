

---


# SmartResumeMatch – AI Resume-to-Job Matcher

SmartResumeMatch is an AI-powered application that matches resumes to job descriptions using Natural Language Processing (NLP). It processes resumes and job descriptions, extracts text, and calculates similarity scores using TF-IDF and Cosine Similarity to help recruiters find the best candidate fit.

---

## 🔧 Features

- Upload resumes in `.pdf` or `.docx` format
- Paste or upload a job description
- Extract and clean text using NLP techniques
- Compute match scores between job description and resumes
- Display top matching resumes

---

## 🛠 Tech Stack

- **Language**: Python  
- **Libraries**: NLTK, Scikit-learn, Pandas  
- **Algorithms**: TF-IDF, Cosine Similarity  
- **Other Tools**: Streamlit (or Flask), ETL Concepts

---

## 📁 Project Structure

```

SmartResumeMatch/
│
├── data/               # Sample resumes and job descriptions
├── utils/              # Text extraction and processing functions
├── app.py              # Main application file (Streamlit/Flask)
├── resume\_matcher.py   # Core logic for matching resumes
├── requirements.txt    # Python dependencies
└── README.md

````

---

## 🚀 How to Run

1. Clone the repo  
   ```bash
   git clone https://github.com/07nand07/SmartResumeMatch.git
   cd SmartResumeMatch
````

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app (for Streamlit)

   ```bash
   streamlit run app.py
   ``

## 📌 Future Improvements

* Add support for bulk resume upload
* Use BERT or other embeddings for better accuracy
* Store results in a database
* Add export to PDF/Excel

---



---

```

```
