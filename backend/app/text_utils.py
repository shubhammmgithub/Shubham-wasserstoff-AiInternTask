import re

# extracted text is splitted into chunks.
def chunk_text(text, doc_id="Unknown_Doc", chunk_size=500, overlap=100):
    """
    Splits input text into chunks with metadata including doc_id, page, and paragraph.
    Each chunk is approximately `chunk_size` characters with `overlap`.
    """
    chunks = []
    start = 0
    paragraph_number = 1
    page_number = 1
    page_length = 1800  # characters per "page" (approximation)

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]

        # Clean chunk
        cleaned_chunk = re.sub(r'\s+', ' ', chunk).strip()

        # Assign page & paragraph based on offset
        current_page = (start // page_length) + 1
        current_paragraph = paragraph_number

        chunks.append({
            "chunk_text": cleaned_chunk,
            "doc_id": doc_id,
            "page": current_page,
            "paragraph": current_paragraph
        })

        # Prepare for next iteration
        start += chunk_size - overlap
        paragraph_number += 1

    return chunks
