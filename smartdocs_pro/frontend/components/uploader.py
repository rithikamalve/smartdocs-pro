import streamlit as st

def uploader():
    return st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"]) 