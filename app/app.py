import sys
import os

# 🔥 Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from services.rag_service import RAGService

st.set_page_config(page_title="Adaptive Web RAG", layout="wide")

st.title("🌐 Adaptive Web RAG Chatbot")

# ✅ Initialize RAG
if "rag" not in st.session_state:
    st.session_state.rag = RAGService()

# ✅ Chat history (UI level)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🌐 URL input
url = st.text_input("Enter Website URL")

if st.button("Process Website"):
    with st.spinner("Processing website..."):
        msg = st.session_state.rag.ingest(url)
        st.success(msg)

# 💬 Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 💬 Chat input
user_input = st.chat_input("Ask something about the website...")

if user_input:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.rag.query(user_input)
            st.markdown(response)

    # Add assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })