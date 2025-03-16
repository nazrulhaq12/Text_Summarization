
from fastapi import FastAPI
from utils.preprocessing import preprocess_text
from utils.sentence_ranking import rank_sentences

app = FastAPI()

@app.get("/summarize/")
def summarize(text: str):
    sentences = text.split('.')
    processed_sentences = [preprocess_text(sentence) for sentence in sentences if sentence]
    ranked_sentences = rank_sentences(processed_sentences)
    summary = ' '.join(ranked_sentences[:3])
    return {"summary": summary}

# Start server:
# uvicorn app:app --host 127.0.0.1 --port 8000

