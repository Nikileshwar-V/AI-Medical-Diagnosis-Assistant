
from ollama_client import shared_llm as llm

def safety_review(output):
    prompt = f"""
    Review the following medical advice for safety:
    {output['treatment']}

    Say if it is safe and when to seek urgent care.
    """
    response = llm.invoke(prompt)
    return {"safety": response.content}
