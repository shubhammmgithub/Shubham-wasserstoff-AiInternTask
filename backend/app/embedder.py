from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks):
    embeddings = model.encode(chunks, normalize_embeddings=True)
    return np.array(embeddings).astype("float32")


def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)  # Inner product
    index.add(embeddings)
    return index


def embed_query(query: str):
    embedding = model.encode([query], normalize_embeddings=True)
    return np.array(embedding).astype("float32")

# ✅ Updated for Render deployment
