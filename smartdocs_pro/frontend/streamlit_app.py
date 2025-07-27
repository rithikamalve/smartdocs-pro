import streamlit as st
import json
from utils.api import (
    upload_file,
    summarize_doc,
    classify_doc,
    translate_doc,
    ocr_doc,
    rag_qa  # ✅ New import
)

st.set_page_config(page_title="SmartDocs Pro", layout="wide")
st.title("SmartDocs Pro")

st.sidebar.header("Upload Document")
uploaded_file = st.sidebar.file_uploader("Choose a PDF or DOCX", type=["pdf", "docx"]) 
task = st.sidebar.selectbox("Task", [
    "Summarize",
    "Classify",
    "Translate",
    "OCR",
    "RAG QA"  # ✅ New task added
])

def display_result(result):
    """
    Utility to display API results cleanly
    """
    try:
        if isinstance(result, dict):
            if "summary" in result:
                st.markdown("### Summary")
                st.markdown(result["summary"])
            if "inference_time" in result:
                st.info(f"Inference Time: {result['inference_time']:.2f}s")
            if "classification" in result:
                st.markdown("### Classification")
                st.markdown(result["classification"])
            if "translation" in result:
                st.markdown("### Translation")
                
                translation_text = (
                    result["translation"].get("translation")
                    if isinstance(result["translation"], dict)
                    else result["translation"]
                )

                # Basic formatting fixes
                formatted = translation_text.strip()

                # Add line breaks after periods if not already there (for long blocks)
                import re
                formatted = re.sub(r'(?<=[^.\n])\.\s+', '.\n\n', formatted)

                # Convert bullets (• or hyphen) to markdown lists
                formatted = re.sub(r"[•\-]\s*", "- ", formatted)

                # Optional: Fix repeated spaces
                formatted = re.sub(r"\n{2,}", "\n\n", formatted)

                st.markdown(formatted)


            if "ocr_text" in result:
                st.markdown("### OCR Text")
                st.markdown(result["ocr_text"])
            if "answer" in result:  # ✅ For RAG QA
                st.markdown("### Answer")
                st.markdown(result["answer"])
        else:
            parsed = json.loads(result)
            display_result(parsed)
    except Exception as e:
        st.error(f"Error displaying result: {e}")
        st.write(result)

# Main flow
if uploaded_file:
    doc_info = upload_file(uploaded_file)
    st.sidebar.success(f"Uploaded: {doc_info['filename']}")
    doc_id = doc_info['document_id']
    ext = '.' + doc_info['filename'].split('.')[-1].lower()

    if task == "Summarize":
        if st.sidebar.button("Summarize"):
            result = summarize_doc(doc_id, ext)
            display_result(result)

    elif task == "Classify":
        if st.sidebar.button("Classify"):
            result = classify_doc(doc_id, ext)
            display_result(result)

    elif task == "Translate":
        languages = ["fr", "de", "es", "it", "pt", "nl", "sv", "pl", "ja", "ko"]
        lang = st.sidebar.selectbox("Target Language", languages)
        if st.sidebar.button("Translate"):
            result = translate_doc(doc_id, ext, lang)
            display_result(result)

    elif task == "OCR":
        if st.sidebar.button("Run OCR"):
            result = ocr_doc(doc_id, ext)
            display_result(result)


    elif task == "RAG QA":
        question = st.text_input("Ask a question about the document:")
        if st.button("Get Answer"):
            result = rag_qa(doc_id, ext, question)
            display_result(result)
