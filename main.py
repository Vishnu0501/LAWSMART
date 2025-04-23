#Importing from another modules
from fastapi import FastAPI, Form, HTTPException
from sentence_transformers import SentenceTransformer
from src.retrieval.retrieve import retrieve_context
from src.generation.generate import generate_response
from src.utils.logger import setup_logger
import uvicorn
import json
import sys


sys.path.append("D:/Vishnu files/LawSmartt")
CHUNKS_PATH = "D:/Vishnu files/LawSmartt/models/chunks.json"
EMBEDDINGS_PATH = "D:/Vishnu files/LawSmartt/models/embeddings.json"

app = FastAPI()
logger = setup_logger()
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load chunks and embeddings
with open(CHUNKS_PATH, "r") as f:
    chunks = json.load(f)

with open(EMBEDDINGS_PATH, "r") as f:
    data = json.load(f)
    embeddings = data["embeddings"]


@app.post("/chat/")
async def chat(question: str = Form(...)):
    """
    Handle user queries, retrieve context, and generate responses.
    """
    try:
        # Retrieve context
        retrieved_context = retrieve_context(question, embeddings, chunks, model)
        # logger.info(f"Retrieved context: {retrieved_context}")

        # Generate response
        generated_response = generate_response(question, retrieved_context)
        # logger.info(f"Generated response: {generated_response}")

        return {
            "question": question,
            "context": retrieved_context,
            "answer": generated_response
        }
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

