from chromadb import EmbeddingFunction, Documents, Embeddings
from google.genai import types
try:
    from gemini import GEMINI_EMBEDDING_MODEL, client
except ImportError:
    from tools.gemini import GEMINI_EMBEDDING_MODEL, client

class GeminiEmbeddingFunction(EmbeddingFunction):
    
    def __init__(self, title: str):
        self.title = title
    
    def __call__(self, input_: Documents) -> Embeddings:
        model: str = GEMINI_EMBEDDING_MODEL
        title: str = self.title
        result = client.models.embed_content(model=model,
                                             contents=input_,
                                             config=types.EmbedContentConfig(task_type='RETRIEVAL_DOCUMENT', title=title))
        return [embedding.values for embedding in result.embeddings]
        