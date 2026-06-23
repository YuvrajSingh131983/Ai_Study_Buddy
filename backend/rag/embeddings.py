from langchain_ollama import OllamaEmbeddings
from backend.config.settings import EMBEDDING_MODEL

def get_embedding_model():
    return OllamaEmbeddings(model=EMBEDDING_MODEL)