# app.py
import streamlit as st
import traceback
import gc
import time

from graph import app as medical_graph

st.set_page_config(page_title="AI Medical Assistant", page_icon=" ", layout="centered")

# ---- Session State ---- #
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "patient_reports" not in st.session_state:
    st.session_state.patient_reports = []

# ---- UI Header ---- #
st.title(" AI Medical Diagnosis Assistant")
st.write("Describe your symptoms and receive AI-driven medical triage, diagnosis, and safety advice.")

# ---- Sidebar ---- #
with st.sidebar:
    st.header(" Patient History")
    if st.session_state.patient_reports:
        for i, r in enumerate(st.session_state.patient_reports):
            st.write(f"**Case {i + 1}:** {r.get('input', '<no input>')}")
            if st.button(f"View Report {i + 1}", key=f"case_{i}"):
                st.code(r.get("report", "No report available"))
    else:
        st.info("No previous cases recorded.")

    if st.button(" Clear History"):
        st.session_state.patient_reports = []
        st.session_state.chat_history = []
        st.success("History cleared!")


# ---- Utility for pretty boxes ---- #
def pretty_box(title: str, text: str, placeholder_obj):
    formatted_value = text.strip().replace("\\n", "\n")
    placeholder_obj.markdown(f"""
        <div style='background:#111; padding:12px; border-radius:10px; margin-top:10px;'>
        <b>{title}</b><br>
        <pre style='white-space: pre-wrap; font-size: 14px;'>{formatted_value}</pre>
        </div>
        """, unsafe_allow_html=True)


# ---- Main Input ---- #
user_input = st.text_area("Describe symptoms:", placeholder="Example: Fever, cough, and chest pain for 3 days")

if st.button("Analyze Symptoms"):
    if not user_input.strip():
        st.warning("Please enter some symptoms first.")
    else:
        st.write(" Processing...")
        placeholder = st.empty()
        state = {"input": user_input}

        try:
            # Stream through the graph nodes
            for event in medical_graph.stream(state):
                for node_name, node_output in event.items():
                    if isinstance(node_output, dict):
                        state.update(node_output)
                    else:
                        state[node_name] = node_output

                    # Skip unnecessary outputs
                    if node_name in ["input", "report"] or not node_output:
                        continue

                    # Map for pretty titles
                    titles = {
                        "symptoms": " Symptoms Extracted",
                        "diagnosis": " Diagnosis",
                        "treatment": " Treatment Plan",
                        "safety": " Safety Review"
                    }
                    title = titles.get(node_name, node_name.capitalize())
                    display_text = node_output.get(node_name) if isinstance(node_output, dict) else str(node_output)

                    pretty_box(title, display_text, placeholder)

                    # Free memory between nodes
                    gc.collect()
                    time.sleep(0.2)

            # ---- Final Report ---- #
            result = state
            st.markdown("### Final Medical Report")

            final_report = result.get("report", " No structured report returned.")
            if isinstance(final_report, str):
                final_report = final_report.strip().replace("\\n", "\n")

            st.markdown(f"""
            <div style='background-color:#1E1E1E; color:#E6E6E6; padding:20px; border-radius:12px;'>
            <pre style='white-space: pre-wrap; font-family: "Segoe UI", sans-serif; font-size: 15px;'>{final_report}</pre>
            </div>
            """, unsafe_allow_html=True)

            # Save to session memory
            st.session_state.patient_reports.append(result)
            st.session_state.chat_history.append({"user": user_input, "report": result.get("report")})

        except Exception as e:
            tb = traceback.format_exc()
            st.error(" An error occurred during processing. See details below.")
            st.code(tb)
            if "memory" in str(e).lower() or "unable to load full model" in str(e).lower():
                st.warning(" The model exceeded available memory. Try a smaller model like `tinyllama:latest`.")
            gc.collect()
            time.sleep(0.2)
