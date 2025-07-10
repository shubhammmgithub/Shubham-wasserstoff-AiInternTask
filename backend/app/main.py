from ocr_utils import extract_text_from_pdf, extract_text_from_image
from embedder import get_embedding
from faiss_utils import FAISSVectorStore
import os

# Paths to test files 
image_path = "../../data/sample_image.jpg"    #(jaun elia text)
pdf_path = "../../data/sample.pdf"            #(RDBMS pdf)


# Step 1:- Extract Text 
print("\n Extracting Text from PDF ")
pdf_text = extract_text_from_pdf(pdf_path)
print(pdf_text[:300])  # print first 300 characters

print("\n Extracting Text from Image")
image_text = extract_text_from_image(image_path)
print(image_text[:300])



# Step 2:- Generate Embeddings 
print("\n Creating Embeddings & FAISS Index ")
chunks = pdf_text.split(". ")[:10]  # first 10 sentences
embeddings = [get_embedding(chunk) for chunk in chunks]

# Step 3: Store in FAISS Database
faiss_store = FAISSVectorStore(dimension=384)
faiss_store.add(embeddings, chunks)

#  Step 4: Search the Query 
query = "What is the main topic?"
query_vector = get_embedding(query)
results = faiss_store.search(query_vector)

print("\n Top Matches ")
for match, score in results:
    print(f"→ {match[:100]}... (Score: {score:.2f})")
