from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import BertTokenizer, BertModel
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_tfidf_matrix(sentences):
    vectorizer = TfidfVectorizer(max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(sentences)
    return tfidf_matrix

def get_bert_embedding(sentence):
    inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    embedding = outputs.last_hidden_state.mean(dim=1)
    return embedding.detach().numpy()

if __name__ == "__main__":
    sentences = ["AI is transforming industries.", "Machine learning improves automation."]
    print(get_tfidf_matrix(sentences).toarray())
    print(get_bert_embedding(sentences[0]))
