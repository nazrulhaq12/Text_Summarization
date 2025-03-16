## **Extractive Text Summarization Using NLP Techniques**  

This project implements an **Extractive Text Summarization** system using modern NLP techniques such as **BERT embeddings**, **TF-IDF**, and **PageRank** to extract and rank the most important sentences from a given text. The project is built using **FastAPI** for the API, **spaCy** and **NLTK** for text preprocessing, and **Scikit-learn** and **NetworkX** for similarity calculations and sentence ranking.  

---

## **Project Structure**  
```
📂 Text_Summarization
├── 📂 __pycache_
    |── app.cpython-310.pyc
├── 📂 utils
│   ├── feature_extraction.py
│   ├── preprocessing.py
│   ├── sentence_ranking.py
│   └── evaluation.py
├── 📂 env
├── app.py
├── main.py
├── .gitignore
├── requirements.txt
└── README.md

```

---

## **Features**  
✅ Preprocessing:  
- Converts text to lowercase  
- Removes special characters and digits  
- Removes stopwords  
- Applies lemmatization using **spaCy**  

✅ Embedding Extraction:  
- Uses **TF-IDF** for traditional text representation  
- Uses **BERT embeddings** for context-based representation  

✅ Sentence Ranking:  
- Computes sentence similarity using **cosine similarity**  
- Ranks sentences using **PageRank algorithm**  

✅ API Endpoint:  
- FastAPI-based `/summarize/` endpoint for summarization  

✅ Evaluation:  
- Measures summarization quality using **ROUGE scores**  

---

## **Installation**  

### **1. Create Virtual Environment**
```bash
python -m venv env
source env/bin/activate      # For Linux/Mac
.\env\Scripts\activate       # For Windows
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Download NLTK and SpaCy Data**
```python
import nltk
nltk.download('stopwords')

python -m spacy download en_core_web_sm
```

---

## **Usage**  

### **1. Start the API Server**  
Run the following command to start the FastAPI server:  
```bash
uvicorn app:app --host 127.0.0.1 --port 8000
```

### **2. Test the Endpoint**  
Send a `GET` request to test the summarization endpoint:  
```bash
curl "http://127.0.0.1:8000/summarize/?text=This%20is%20the%20first%20sentence.%20This%20is%20the%20second%20sentence.%20This%20is%20the%20third%20sentence."
```
Example Response:  
```json
{
    "summary": "This is the second sentence. This is the third sentence. This is the first sentence."
}
```

---

## **Evaluation**  
Use the `evaluate_summary` function to measure ROUGE scores:  
```python
from utils.evaluation import evaluate_summary

reference = "AI is transforming industries and improving automation."
summary = "AI is transforming industries. Machine learning improves automation."
scores = evaluate_summary(summary, reference)
print(scores)
```

---

## **Dependencies**  
- Python 3.7+  
- FastAPI  
- TensorFlow  
- SpaCy  
- NLTK  
- NetworkX  
- Scikit-learn  
- Transformers  

---

## **Troubleshooting**  
### ✅ *Port Already in Use*  
If you encounter the error `Only one usage of each socket address`, stop the existing process:  
```bash
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### ✅ *SpaCy Model Not Found*  
If the `en_core_web_sm` model is missing:  
```bash
python -m spacy download en_core_web_sm
```

### ✅ *BERT Model Download Error*  
If BERT models fail to load, try:  
```bash
pip install transformers
```

---

## **Author**  
👨‍💻 **Md Nazrul Haq** – B.Tech in CSE (AI & ML)  

---

## **License**  
This project is licensed under the **MIT License**.