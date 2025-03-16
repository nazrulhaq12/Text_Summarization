from rouge_score import rouge_scorer

def evaluate_summary(summary, reference):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, summary)
    return scores

if __name__ == "__main__":
    reference = "AI is transforming industries and improving automation."
    summary = "AI is transforming industries. Machine learning improves automation."
    scores = evaluate_summary(summary, reference)
    print(scores)
