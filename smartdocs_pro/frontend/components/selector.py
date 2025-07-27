import streamlit as st

def selector():
    return st.selectbox("Select Task", ["Summarize", "Classify", "Translate", "OCR", "Structure Extraction"]) 