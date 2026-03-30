# Adaptive Web RAG Chatbot

An intelligent system that can crawl any website and answer questions using an Adaptive Retrieval-Augmented Generation (RAG) pipeline.

## Features
- Multi-page website crawling
- Adaptive retrieval (query refinement + reranking)
- FAISS vector database with persistence
- Chat memory
- Groq LLM integration
- Streamlit chat interface

## Tech Stack
- Python
- FAISS
- Sentence Transformers
- Groq API
- Streamlit

## How to Run

```bash
pip install -r requirements.txt
streamlit run app/app.py