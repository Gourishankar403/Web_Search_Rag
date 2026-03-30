from ingestion.crawler.web_crawler import crawl_website
from ingestion.parser.html_parser import clean_text
from ingestion.chunking.text_chunker import chunk_documents
from vectorstore.faiss_store import VectorStore
from core.adaptive.strategy_router import route_query
from core.llm.groq_client import generate_answer
from core.memory.chat_memory import ChatMemory


class RAGService:
    def __init__(self):
        self.store=None
        self.memory=ChatMemory()
        self.current_url=None

    def ingest(self, url):
        try:

            if url != self.current_url:
                self.memory=ChatMemory()
                self.current_url=url


            self.store=VectorStore(url)

            # Try loading existing DB for this URL
            if self.store.load():
                return "Loaded existing data for this website."

            # Crawl website
            pages=crawl_website(url)
            print("Pages crawled:", len(pages))

            if not pages:
                return "No pages found. Website may block scraping."

            # Clean text
            pages = [(u,clean_text(t)) for u, t in pages]

            # Chunk
            docs = chunk_documents(pages)
            print("Chunks created:",len(docs))

            if not docs:
                return "No content extracted. Try another website."

            # Store embeddings
            self.store.add(docs)
            self.store.save()

            return "Website processed successfully."

        except Exception as e:
            return f" Error during ingestion:{str(e)}"

    def query(self,question):
        try:
            if not self.store:
                return "Please process a website first."

            history=self.memory.get_context()


            context=route_query(self.store, self.memory, question)

            answer=generate_answer(context, question, history)

            self.memory.add(question, answer)

            return answer

        except Exception as e:
            return f" Error during query: {str(e)}"