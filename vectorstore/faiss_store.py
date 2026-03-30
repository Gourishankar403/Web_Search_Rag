import faiss
import numpy as np
import pickle
import os
import hashlib

from vectorstore.embedding_model import embed


class VectorStore:
    def __init__(self, url=None):
        self.index = None
        self.documents = []

        self.db_dir = "data/db"
        if url:
            url_hash = hashlib.md5(url.encode()).hexdigest()
            self.db_path = f"{self.db_dir}/{url_hash}.index"
            self.meta_path = f"{self.db_dir}/{url_hash}.pkl"
        else:
            self.db_path = f"{self.db_dir}/default.index"
            self.meta_path = f"{self.db_dir}/default.pkl"

    def add(self, docs):

        if not docs:
            raise ValueError("No documents to add. Check crawler or parser.")

        texts=[d["content"] for d in docs if d["content"].strip()]

        if not texts:
            raise ValueError("All documents are empty after cleaning.")

        vectors=embed(texts)

        if len(vectors)==0:
            raise ValueError("Embedding returned empty vectors.")

        self.documents.extend(docs)

        # Initialize FAISS index
        if self.index is None:
            dim=len(vectors[0])
            self.index=faiss.IndexFlatL2(dim)

        self.index.add(np.array(vectors))

    def search(self, query, k=5):
        if self.index is None:
            raise ValueError("Vector store is empty. Ingest data first.")

        q_vec = embed([query])
        distances,indices=self.index.search(np.array(q_vec), k)

        return [self.documents[i] for i in indices[0]]

    def save(self):
        os.makedirs(self.db_dir,exist_ok=True)

        if self.index is not None:
            faiss.write_index(self.index, self.db_path)

            with open(self.meta_path, "wb") as f:
                pickle.dump(self.documents, f)

    def load(self):
        if os.path.exists(self.db_path) and os.path.exists(self.meta_path):
            self.index = faiss.read_index(self.db_path)

            with open(self.meta_path, "rb") as f:
                self.documents = pickle.load(f)

            return True

        return False