def report_agent(state):
    return {
        "report": f"""
--- MEDICAL REPORT ---

Symptoms:
{state['symptoms']}

Diagnosis:
{state['diagnosis']}

Treatment Advice:
{state['treatment']}

Safety Review:
{state['safety']}

-----------------------
Note: This is AI assistance, not medical confirmation.
"""
    }
