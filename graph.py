# graph.py
from langgraph.graph import StateGraph, END
from typing import Dict, Any

# Import agent functions
from agents.symptom_agent import extract_symptoms
from agents.diagnosis_agent import diagnose
from agents.treatment_agent import treatment
from agents.safety_agent import safety_review
from agents.report_agent import report_agent


# ---- Graph Node Wrappers ---- #
def symptom_node(state: Dict[str, Any]):
    text = state.get("input", "")
    result = extract_symptoms(text)
    return {**state, "symptoms": result.get("symptoms", "")}


def diagnosis_node(state: Dict[str, Any]):
    result = diagnose({"symptoms": state.get("symptoms", "")})
    return {**state, "diagnosis": result.get("diagnosis", "")}


def treatment_node(state: Dict[str, Any]):
    result = treatment({"diagnosis": state.get("diagnosis", "")})
    return {**state, "treatment": result.get("treatment", "")}


def safety_node(state: Dict[str, Any]):
    result = safety_review(state)
    return {**state, "safety": result.get("safety", "")}


def report_node(state: Dict[str, Any]):
    # Build final structured report
    result = report_agent(state)
    return {**state, "report": result["report"]}


# ---- Build Workflow Graph ---- #
builder = StateGraph(dict)

builder.add_node("symptoms", symptom_node)
builder.add_node("diagnosis", diagnosis_node)
builder.add_node("treatment", treatment_node)
builder.add_node("safety", safety_node)
builder.add_node("report", report_node)

builder.set_entry_point("symptoms")

builder.add_edge("symptoms", "diagnosis")
builder.add_edge("diagnosis", "treatment")
builder.add_edge("treatment", "safety")
builder.add_edge("safety", "report")
builder.add_edge("report", END)

# ✅ Compiled workflow
app = builder.compile()
