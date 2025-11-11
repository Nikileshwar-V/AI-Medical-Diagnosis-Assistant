from ollama_client import shared_llm as llm


from langchain_ollama import ChatOllama
from rag import get_medical_context


def diagnose(symptoms):
    query = symptoms["symptoms"]
    context = get_medical_context(query)

    prompt = f"""
    Medical Reference:
    {context}

    Symptoms:
    {query}

    Task: Provide most likely diagnosis (max 3 lines)
    """
    response = llm.invoke(prompt)
    return {"diagnosis": response.content}
