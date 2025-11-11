# ollama_client.py
from langchain_ollama import ChatOllama

# ✅ Shared lightweight Ollama model - CPU only
shared_llm = ChatOllama(
    model="tinyllama:latest",   # lightweight and fits in 8GB RAM
    options={"num_gpu": 0}      # force CPU mode
)
