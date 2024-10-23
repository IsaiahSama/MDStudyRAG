from chromadb import EmbeddingFunction, Documents, Embeddings
import google.generativeai as genai
from .. import GEMINI_EMBEDDING_MODEL

class GeminiEmbeddingFunction(EmbeddingFunction):
    def __call__(self, input_: Documents) -> Embeddings:
        model: str = GEMINI_EMBEDDING_MODEL
        title: str = "Custom Query"
        return genai.embed_content(model, 
                                input_,
                                'retrieval_document',
                                title)['embedding']
        