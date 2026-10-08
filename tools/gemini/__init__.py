from os import environ 
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

GEMINI_API_KEY = environ.get("GEMINI_API_KEY")
GEMINI_EMBEDDING_MODEL = environ.get("GEMINI_EMBEDDING_MODEL", "models/gemini-embedding-001")
GEMINI_MODEL = environ.get("GEMINI_MODEL", "models/gemini-flash-lite-latest")

if not GEMINI_API_KEY:
    raise Exception("GEMINI_API_KEY not set in the .env file.")
else:
    genai.configure(api_key=GEMINI_API_KEY)
