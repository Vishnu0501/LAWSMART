from ollama import chat
from src.utils.logger import setup_logger

logger = setup_logger()

def generate_response(question, context):
    """
    Generate a response using the Ollama library.
    """
    try:
        logger.info(f"Generate input: question={question}, context={context}")

        # Construct the prompt
        prompt = f"Context:\n{context}\n\nQuestion:\n{question}\n\nAnswer:"

        # Call the Ollama chat function
        response = chat(
            model="llama3.2",
            messages=[{'role': 'user', 'content': prompt}]
        )

        # Log the raw response structure for debugging
        logger.info(f"Raw response: {response}")

        # Access the response content from the `message` attribute
        if hasattr(response, "message") and hasattr(response.message, "content"):
            logger.info(f"Generated response: {response.message.content}")
            return response.message.content
        else:
            logger.error("Unexpected response structure: Missing `message.content`.")
            return "Unexpected response structure: Missing `message.content`."

    except Exception as e:
        logger.error(f"Error generating response: {e}")
        return f"An error occurred: {e}"
