import re
import spacy
from nltk.corpus import stopwords

nlp = spacy.load('en_core_web_sm')
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)       
    text = re.sub(r'\d', '', text)        
    text = re.sub(r'\s+', ' ', text).strip()
    
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if token.text not in stop_words]
    
    return ' '.join(tokens)

if __name__ == "__main__":
    sample_text = "The AI model is working perfectly in 2025!"
    print(preprocess_text(sample_text))
