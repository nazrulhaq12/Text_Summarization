# main.py
from utils.preprocessing import preprocess_text
from utils.sentence_ranking import rank_sentences
from utils.evaluation import evaluate_summary

def generate_summary(text, num_sentences=3):
    sentences = text.split('.')
    processed_sentences = [preprocess_text(sentence) for sentence in sentences if sentence]
    ranked_sentences = rank_sentences(processed_sentences)
    summary = ' '.join(ranked_sentences[:num_sentences])
    return summary

if __name__ == "__main__":
    text = """
        AI is transforming industries. Machine learning improves automation.
        Natural Language Processing enhances communication. Computer vision is evolving rapidly.
    """
    
    reference = "AI is transforming industries and improving automation."
    
    summary = generate_summary(text)
    print("Summary:")
    print(summary)
    
    scores = evaluate_summary(summary, reference)
    print("ROUGE Scores:")
    print(scores)
