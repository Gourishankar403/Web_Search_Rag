from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP

def chunk_documents(pages):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    docs = []
    for url, text in pages:
        chunks = splitter.split_text(text)

        for chunk in chunks:
            docs.append({
                "content": chunk,
                "source": url
            })

    return docs