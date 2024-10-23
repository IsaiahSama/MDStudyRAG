from chromadb import EmbeddingFunction, Documents, Embeddings
import google.generativeai as genai
from dotenv import load_dotenv
from os import environ

load_dotenv()

class GeminiEmbeddingFunction(EmbeddingFunction):
    def __call__(self, input_: Documents) -> Embeddings:
        model: str = environ.get("GEMINI_EMBEDDING_MODEL", "models/embedding-001")
        title: str = "Custom Query"
        return genai.embed_content(model, 
                                input_,
                                'retrieval_document',
                                title)['embedding']
        