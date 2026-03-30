import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")

MODEL_NAME="groq/compound-mini"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

MAX_PAGES = 15
TOP_K = 5

DB_PAT="data/db/faiss.index"
META_PATH="data/db/meta.pkl"