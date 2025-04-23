from sklearn.metrics.pairwise import cosine_similarity
from src.utils.logger import setup_logger
logger = setup_logger()
def retrieve_context(question, embeddings, chunks, model):
    logger.info(f"Retrieve input: question={question}")
    question_embedding = model.encode([question])[0]
    similarities = cosine_similarity([question_embedding], embeddings)[0]
    top_indices = similarities.argsort()[-3:][::-1]
    context = " ".join([chunks[i] for i in top_indices])
    logger.info(f"Retrieved context: {context}")
    return context
