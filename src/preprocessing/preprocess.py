import PyPDF2
import json

PDF_PATH = "D:/Vishnu files/LawSmartt/Bharatiya Nyaya Sanhita, 2023.pdf"
CHUNKS_PATH = "D:/Vishnu files/LawSmartt/models/chunks.json"

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def split_text_into_chunks(text, chunk_size=500, overlap=50):
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return splitter.split_text(text)

# Preprocess the PDF and save chunks
text = extract_text_from_pdf(PDF_PATH)
chunks = split_text_into_chunks(text)
with open(CHUNKS_PATH, "w") as f:
    json.dump(chunks, f)
