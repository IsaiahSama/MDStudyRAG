from gemini.embedding import GeminiEmbeddingFunction
from md_to_json.md_to_json import md_to_json
from chroma.chroma import ChromaClient

from os import environ 
from dotenv import load_dotenv

load_dotenv("../.env")

GEMINI_API_KEY = environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise Exception("GEMINI_API_KEY not set in the .env file.")

GEMINI_EMBEDDING_MODEL = environ.get("GEMINI_EMBEDDING_MODEL", "models/embedding-001")