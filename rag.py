from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

DB_DIR = "medical_db"

def build_rag_database(text_file="data/medical_reference.txt"):
    with open(text_file, "r", encoding="utf-8") as f:
        data = f.read()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_text(data)

    # ✅ Super lightweight embedding model
    embeddings = OllamaEmbeddings(model="all-minilm")

    Chroma.from_texts(docs, embedding=embeddings, persist_directory=DB_DIR)
    print("✅ Medical RAG database created successfully.")

def get_medical_context(query):
    embeddings = OllamaEmbeddings(model="all-minilm")
    db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

    results = db.similarity_search(query, k=3)
    return "\n\n".join([r.page_content for r in results])
