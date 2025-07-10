from sentence_transformers import SentenceTransformer

# Loadin pretrained model (MiniLM)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embedding for given text
def get_embedding(text):
    return model.encode(text)
