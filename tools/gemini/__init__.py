from os import environ 
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv("../.env")

GEMINI_API_KEY = environ.get("GEMINI_API_KEY")
GEMINI_EMBEDDING_MODEL = environ.get("GEMINI_EMBEDDING_MODEL", "models/embedding-001")

if not GEMINI_API_KEY:
    raise Exception("GEMINI_API_KEY not set in the .env file.")
else:
    genai.configure(api_key=GEMINI_API_KEY)
