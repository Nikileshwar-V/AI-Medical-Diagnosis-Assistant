from langchain_ollama import ChatOllama
from rag import get_medical_context

from ollama_client import shared_llm as llm

def extract_symptoms(text):
    medical_context = get_medical_context(text)

    prompt = f"""
You are a medical symptom extraction assistant.

Medical reference notes:
{medical_context}

Patient text:
{text}

Task:
✅ Extract only clear symptoms and duration
❌ Do NOT add diagnosis or treatment
❌ No storytelling or unnecessary wording

Output format (bullet points):
- Fever for 3 days
- Persistent cough
- Fatigue
- Chest discomfort
"""
    response = llm.invoke(prompt)
    return {"symptoms": response.content.strip()}
