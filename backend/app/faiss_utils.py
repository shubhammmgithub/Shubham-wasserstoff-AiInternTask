import faiss
import numpy as np

class FAISSVectorStore:
    def __init__(self, dimension):
        # Create a flat (L2) index for the given dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.text_chunks = []

    def add(self, vectors, chunks):
        # Add new vectors and corresponding text chunks
        self.index.add(np.array(vectors).astype("float32"))
        self.text_chunks.extend(chunks)

    def search(self, query_vector, top_k=5):
        # It will perform a similarity search to find out the relevant data
        distances, indices = self.index.search(np.array([query_vector]).astype("float32"), top_k)
        return [(self.text_chunks[i], distances[0][idx]) for idx, i in enumerate(indices[0])]
