from chromadb import EmbeddingFunction, Documents, Embeddings
import google.generativeai as genai
try:
    from gemini import GEMINI_EMBEDDING_MODEL
except ImportError:
    from tools.gemini import GEMINI_EMBEDDING_MODEL

class GeminiEmbeddingFunction(EmbeddingFunction):
    
    def __init__(self, title: str):
        self.title = title
    
    def __call__(self, input_: Documents) -> Embeddings:
        model: str = GEMINI_EMBEDDING_MODEL
        title: str = self.title
        return genai.embed_content(model, 
                                input_,
                                'retrieval_document',
                                title)['embedding']
        