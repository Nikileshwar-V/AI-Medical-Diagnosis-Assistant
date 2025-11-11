from langchain_ollama import ChatOllama
from rag import get_medical_context

from langchain_ollama import ChatOllama

from ollama_client import shared_llm as llm


def treatment(diagnosis):
    query = diagnosis["diagnosis"]
    context = get_medical_context(query)

    prompt = f"""
    Medical Reference:
    {context}

    Diagnosis: {query}

    Task: Provide recommended treatment advice.
    Do NOT prescribe exact drugs — only general care instructions.
    """
    response = llm.invoke(prompt)
    return {"treatment": response.content}
