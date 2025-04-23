# LAWSMART
# LawSmartBot

**LawSmartBot** is a Retrieval-Augmented Generation (RAG) chatbot powered by **Ollama**. It leverages document retrieval and advanced language generation to answer questions based on the **Bharatiya Nyaya Sanhita** (Indian Penal Code). The chatbot evaluates retrieval accuracy and response quality to provide insightful responses.

---

## **Features**
1. **Document-Based Question Answering**:
   - Extracts relevant context from the **Bharatiya Nyaya Sanhita**.
   - Generates accurate, context-aware responses using **Ollama**.
   
2. **Evaluation Metrics**:
   - **Retrieval Accuracy**: Measures the relevance of retrieved context.
   - **Response Quality**: BLEU and ROUGE scores to evaluate generated answers.

3. **Modular Design**:
   - Preprocessing, retrieval, generation, and evaluation are organized into separate modules for scalability.

4. **Logging and Analytics**:
   - Tracks system performance and logs all interactions.

---

## **Directory Structure**

```plaintext
LawSmartBot/
├── src/
│   ├── preprocessing/
│   │   ├── preprocess.py         # PDF text extraction and chunking
│   │   ├── embeddings.py         # Generate and manage embeddings
│   ├── retrieval/
│   │   ├── retrieve.py           # Handle context retrieval
│   ├── generation/
│   │   ├── generate.py           # Generate responses using Ollama
│   ├── evaluation/
│   │   ├── metrics.py            # Evaluate retrieval and generation
│   ├── utils/
│   │   ├── logger.py             # Logging setup
├── models/
│   ├── chunks.json               # Preprocessed text chunks
│   ├── embeddings.json           # Embeddings for retrieval
├── logs/
│   ├── chatbot.log               # Log file
├── main.py                       # FastAPI application entry point
├── BharatiyaNyayaSanhita.pdf     # Dataset (PDF)
├── requirements.txt              # Python dependencies
└── README.md                     # Documentation
