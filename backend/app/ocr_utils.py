from PIL import Image
import pytesseract
import pdfplumber
import docx
import os

# extracting the text from the files we have uploaded
# we have done exception handling also and checking the file type also
def extract_text_from_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()

    try:
        if ext in ['.jpg', '.jpeg', '.png']:
            return pytesseract.image_to_string(Image.open(filepath))

        elif ext == '.pdf':
            text = ""
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ''
            return text

        elif ext == '.docx':
            doc = docx.Document(filepath)
            return "\n".join([para.text for para in doc.paragraphs])

        else:
            return "Unsupported file type."

    except Exception as e:
        return f"❌ Error extracting text: {str(e)}"
