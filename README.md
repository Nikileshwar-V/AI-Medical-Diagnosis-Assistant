# Multi-Agent Medical Triage & Advisory System

## Overview

MediSense AI is a multi-agent clinical triage system designed to extract symptoms, suggest a likely medical interpretation, offer general safe care guidance, and flag emergency red-flags. The system uses LangGraph to orchestrate autonomous agents and Ollama models for local offline inference. Retrieval-augmented knowledge improves reliability.

This project demonstrates AI-assisted clinical triage workflows for academic research purposes. It does not perform medical diagnosis and is intended for educational demonstration only.

## Features

* Symptom extraction from natural language
* Probable clinical condition inference (non-diagnostic)
* Safe supportive treatment suggestions
* Red-flag and safety guidance
* Structured medical report generation
* RAG-enhanced medical context
* Streamlit UI with patient case history
* Fully local execution using Ollama

## Architecture

The system follows a multi-agent pipeline:

1. Symptom extraction agent
2. Clinical interpretation agent
3. Supportive care recommendation agent
4. Safety and emergency check agent
5. Report generator agent

## Project Structure

```
MediSense-AI/
│
├── app.py                 # Streamlit UI
├── graph.py               # LangGraph agent pipeline
├── main.py                # CLI mode
├── ollama_client.py    
│
├── agents/
│   ├── symptom_agent.py
│   ├── diagnosis_agent.py
│   ├── treatment_agent.py
│   ├── safety_agent.py
│   └── report_agent.py
│
├── rag.py                 # Medical RAG helper
├── data/
│   └── medical_reference.txt
│
├── requirements.txt
└── README.md
```

## Technology Stack

* Python 3.10+
* LangGraph
* Ollama (local LLM)
* Streamlit
* Local RAG with embeddings

## Installation

```
git clone <repo-url>
cd MediSense-AI
python -m venv .venv
.venv\Scripts\activate  # Windows
# OR
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

## Model Setup

Install Ollama from [https://ollama.com/download](https://ollama.com/download)

Download lightweight models:

```
ollama pull phi3:mini
ollama pull all-minilm
```

If running low GPU memory:

```
set OLLAMA_NUM_GPU=0   # Windows
export OLLAMA_NUM_GPU=0 # Linux/Mac
```

## Run Application

### Streamlit UI

```
streamlit run app.py
```

### CLI Mode

```
python main.py
```

## Output Example

```
Symptoms
- Fever (3 days)
- Cough
- Fatigue

Possible Interpretation
Likely viral respiratory illness

Supportive Guidance
Hydration, rest, paracetamol if needed

Safety
Seek urgent care if breathing difficulty, persistent chest pain, confusion
```

## Future Enhancements

* Expanded medical domain coverage
* PDF export for reports
* Secure cloud deployment
* Doctor feedback interface
* WhatsApp/Telegram triage bot

## Author

Nikileshwar V
MCA Research Project
GitHub: [https://github.com/Nikileshwar-V](https://github.com/Nikileshwar-V)
LinkedIn: [https://linkedin.com/in/nikileshwar-v](https://linkedin.com/in/nikileshwar-v)

## Disclaimer

This tool does not provide medical diagnosis. It is a research and educational demonstration of AI-assisted triage and safety reasoning. Always consult licensed medical professionals for healthcare decisions.
