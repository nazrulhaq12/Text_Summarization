import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from .feature_extraction import get_bert_embedding

def rank_sentences(sentences):
    if not sentences:
        return []
    
    embeddings = np.array([get_bert_embedding(sentence)[0] for sentence in sentences])
    similarity_matrix = cosine_similarity(embeddings)
    
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph)

    ranked = sorted(((scores[i], i, s) for i, s in enumerate(sentences)), reverse=True)
    top_sentences = sorted(ranked[:3], key=lambda x: x[1])

    return [sentence for _, _, sentence in top_sentences]

if __name__ == "__main__":
    sentences = [
        "This is the first sentence.",
        "This is the second sentence.",
        "This is the third sentence."
    ]
    ranked_sentences = rank_sentences(sentences)
    print(ranked_sentences)
