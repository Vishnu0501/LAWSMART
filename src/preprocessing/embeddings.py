from sentence_transformers import SentenceTransformer
import json

CHUNKS_PATH = "D:/Vishnu files/LawSmartt/models/chunks.json"
EMBEDDINGS_PATH = "D:/Vishnu files/LawSmartt/models/embeddings.json"

def generate_embeddings(chunks_path, model_name="all-MiniLM-L6-v2"):
    with open(chunks_path, "r") as f:
        chunks = json.load(f)
    
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks, show_progress_bar=True)
    return chunks, embeddings

# Generate embeddings and save them
chunks, embeddings = generate_embeddings(CHUNKS_PATH)
with open(EMBEDDINGS_PATH, "w") as f:
    json.dump({"chunks": chunks, "embeddings": embeddings.tolist()}, f)
