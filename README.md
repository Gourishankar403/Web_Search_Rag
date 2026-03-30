
````md
# Adaptive Web RAG Chatbot

An intelligent system that can **crawl any website and answer questions about it** using an Adaptive Retrieval-Augmented Generation (RAG) pipeline.

---

##Features

-Multi-page website crawling  
-Adaptive RAG (query refinement + reranking + routing)  
- Fast LLM inference using Groq  
-  Conversational memory (chat history)  
- FAISS vector database with persistence  
-  Multi-website support (URL-specific storage)  
-  Interactive chat UI using Streamlit  

---

##  How It Works

```text
User Input (URL)
        ↓
Website Crawling (multi-page)
        ↓
Text Cleaning + Chunking
        ↓
Embeddings (Sentence Transformers)
        ↓
FAISS Vector Store
        ↓
Adaptive Retrieval:
   - Query Analysis
   - Query Refinement
   - Reranking
        ↓
LLM (Groq)
        ↓
Final Answer (with chat memory)
````

---

## Setup Instructions

### 1. Clone the Repository : https://github.com/Gourishankar403/Web_Search_Rag

```bash


### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Get Groq API Key

This project uses Groq LLM for fast inference.

1. Go to [https://console.groq.com](https://console.groq.com)
2. Sign up / log in
3. Generate an API key

---

### 4. Create `.env` File

In the root directory, create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 5. Run the Application

```bash
streamlit run app/app.py
```

---

## Usage

1. Enter a website URL
2. Click **Process Website**
3. Ask questions about the content
4. Continue chatting with memory

---

##  Project Structure

```
web_rag_agent/
│
├── app/                 # Streamlit UI
├── core/                # LLM + retrieval + adaptive logic
├── ingestion/           # Web scraping + parsing + chunking
├── vectorstore/         # FAISS + embeddings
├── services/            # Main pipeline orchestration
├── data/db/             # Stored vector databases
├── config/              # Settings
├── utils/               # Helpers
├── tests/               # Testing
```

---

##  Note

* Some websites may block scraping
* Large websites may take longer to process
* Ensure your `.env` file is properly configured
* API key is required for generating responses

---



## 🛠️ Tech Stack

* Python
* FAISS
* Sentence Transformers
* Groq API
* Streamlit
* BeautifulSoup

---

## Future Improvements

* Source citation display
* Confidence scoring
* Multi-query expansion
* Async crawling for speed
* UI enhancements

---

## Contributing

Feel free to fork this repo and improve it!

---

## If You Like This Project

Give it a ⭐ on GitHub — it helps a lot


