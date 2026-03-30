from services.rag_service import RAGService

rag = RAGService()

print(rag.ingest("https://example.com"))
print(rag.query("What is this website about?"))